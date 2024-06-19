#coding=utf8
import os.path
from typing import Dict
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings, StorageContext
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.storage.docstore import SimpleDocumentStore
from llama_index.core.storage.index_store import SimpleIndexStore
from llama_index.core.vector_stores import SimpleVectorStore
from llama_index.core import load_index_from_storage
import tiktoken
from pathlib import Path
import json
import argparse
from functools import partial


# retrieved_docs_llama_index.txt

Settings.tokenizer = tiktoken.encoding_for_model("gpt-3.5-turbo").encode
Settings.llm = None

APPS_TO_WEBSITES = {
                'metabase': 'www.metabase.com',
                'superset': 'superset.apache.org',
                'bigquery': 'cloud.google.com',
                'jupyter': 'jupyterlab.readthedocs.io',
                'airbyte': 'airbyte.com',
                'dbt': 'docs.getdbt.com',
                'dagster': 'release-1-7-2.dagster.dagster-docs.io',
                'airflow': 'docs.astronomer.io',
                'snowflake': 'docs.snowflake.com'}


ALL_DOMAINS = ['excel', 'servicenow', 'jupyter', 'dbt', 'airflow', 'dagster', 'airbyte', 'snowflake', 'bigquery', 'superset', 'metabase']


def get_meta(file_path, page_titles=None):
    def _get_subpath(full_path):
        path = Path(full_path)
        for website in APPS_TO_WEBSITES.values():
            if website in path.parts:
                try:
                    start_index = path.parts.index(website)
                except ValueError:
                    return ""

                subpath = Path(*path.parts[start_index:])

                return str(subpath)
        return ""

    sub_path = _get_subpath(file_path)
    return {"page_title": page_titles[sub_path], "file_path": sub_path}


class LlamaIndexRetrieval:

    def __init__(self, doc_directory, chunk_size: int = 512, chunk_overlap=20, embed_model_name_or_path="openai"):
        if embed_model_name_or_path != 'openai':
            Settings.embed_model = HuggingFaceEmbedding(
                model_name=embed_model_name_or_path
            )
        # Load storage_context
        storage_name = f'storage_chunk_size_{args.chunk_size}_chunk_overlap_{args.chunk_overlap}_' \
                       f'embed_{Path(args.embed_model_name_or_path).name}'
        try:
            print('Start to load context ...')
            storage_context = StorageContext.from_defaults(persist_dir=os.path.join(doc_directory, storage_name))
            print('Storage context loaded!')
        except FileNotFoundError:
            storage_context = StorageContext.from_defaults(
                docstore=SimpleDocumentStore(),
                vector_store=SimpleVectorStore(),
                index_store=SimpleIndexStore(),
            )

        # Load vector index
        indices_dict = dict.fromkeys(APPS_TO_WEBSITES.keys())

        with open(os.path.join(doc_directory, 'webpage_title.json'), 'r') as f:
            webpage_titles = json.load(f)

        for app, website in APPS_TO_WEBSITES.items():
            try:
                indices_dict[app] = load_index_from_storage(storage_context, index_id=app)
                print(f'Indice dict for {app} loaded!')
            except ValueError:
                print(f'build index of app-{app} from scratch...')
                node_parser = SentenceSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap,
                                               tokenizer=tiktoken.encoding_for_model("gpt-3.5-turbo").encode)
                website_doc_dir = os.path.join(doc_directory, website)
                get_meta_with_title = partial(get_meta, page_titles=webpage_titles)
                documents = SimpleDirectoryReader(website_doc_dir,
                                                  recursive=True,
                                                  file_metadata=get_meta_with_title).load_data()
                print(f'total {len(documents)} documents in {website_doc_dir}')
                nodes = node_parser.get_nodes_from_documents(
                    documents, show_progress=True
                )
                print(f'total {len(nodes)} snippets in {website_doc_dir}')
                storage_context.docstore.add_documents(nodes)
                index = VectorStoreIndex(nodes, storage_context=storage_context, show_progress=True)
                index.set_index_id(app)
                indices_dict[app] = index
                index.storage_context.persist(persist_dir=os.path.join(doc_directory, storage_name))

        self.indices_dict = indices_dict
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def retrieve_docs_by_instruction_data(self, data: Dict, topk: int = 4):
        """
        @args:
            data: Dict, the json data to be used for retrieval
                instruction: str, the instruction for the retrieval
                related_apps: List[str], the related apps for the retrieval
            topk: retrieve top-k relevant data snippets
        @return:
            doc_prompt: str
        """
        query = data['instruction']
        related_apps = data['related_apps']

        all_retrieved_nodes = []
        for possible_app in related_apps:
            if possible_app in self.indices_dict:
                retrieve_engine = self.indices_dict[possible_app].as_retriever(similarity_top_k=topk)
                retrieved_nodes = retrieve_engine.retrieve(query)
                all_retrieved_nodes += retrieved_nodes

        sorted_nodes = sorted(all_retrieved_nodes, key=lambda x: x.score, reverse=True)[:topk]
        doc_prompt = ""
        for node in sorted_nodes:
            doc_prompt += f"Documentation Source:\n{node.metadata['file_path']}\n\n" \
                          f"Documentation Title:\n{node.metadata['page_title']}\n\n" \
                          f"Documentation Content:\n{node.text}\n\n\n\n"

        return doc_prompt


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--doc_directory', type=str, default='evaluation_examples/documents/docs/doc_txt')
    parser.add_argument('--example_directory', type=str, default='evaluation_examples/examples')
    parser.add_argument('--chunk_size', type=int, default=512)
    parser.add_argument('--chunk_overlap', type=int, default=20)
    parser.add_argument('--topk', type=int, default=4)
    parser.add_argument('--embed_model_name_or_path', type=str, default="evaluation_examples/documents/bge-large-en-v1.5")
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    # Sample usage:
    # python llama_index_retrieval.py --example_directory evaluation_examples/examples/ --doc_directory evaluation_examples/documents/docs/doc_txt/ --embed_model_name_or_path evaluation_examples/documents/bge-large-en-v1.5

    args = parse_args()

    retrieval = LlamaIndexRetrieval(args.doc_directory, args.chunk_size, args.chunk_overlap,
                                    args.embed_model_name_or_path)
    all_examples_path = []
    for domain in ALL_DOMAINS:
        domain_dir = Path(args.example_directory) / domain
        for example_dir in domain_dir.iterdir():
            example_path = example_dir / f'{example_dir.name}.json'
            if example_path.exists() and example_path.is_file():
                all_examples_path.append(example_path)

    suffix = args.doc_directory.rstrip(os.sep).split('_')[-1]
    retrieved_filename = f'retrieved_chunk_size_{args.chunk_size}_chunk_overlap_{args.chunk_overlap}_' \
                            f'topk_{args.topk}_embed_{Path(args.embed_model_name_or_path).name}.{suffix}'
    for example_path in all_examples_path:
        print(f'retrieving documents for {example_path}...')
        with open(example_path, 'r') as f:
            query_data = json.load(f)
        retrieved_data = retrieval.retrieve_docs_by_instruction_data(query_data, args.topk)
        with open(example_path.parent / (retrieved_filename), 'w') as f:
            f.write(retrieved_data)
