# Document Warehouse

Download pre-processed document files from [Google Drive](https://drive.usercontent.google.com/download?id=1aGaHXDkBeoUZ9EOIPj7iIRFra_2FjJoZ&export=download&authuser=0&confirm=t) into folder `evaluation_examples/documents/`. Unzip this file and we will get the following folder structure:
```
- evaluation_examples/documents/:
  - docs.zip
  - docs/
    - doc_orig.zip
    - doc_txt.zip
    - doc_md.zip
    - doc_html.zip
```
Among them, suffix `_orig` means the crawled raw HTML web pages (using tool [HTTrack](https://www.httrack.com/)), and other suffixes represent $3$ different pre-processed formats.

## .txt Format
Let's take `.txt` format as an example. Unzip the archive file `doc_txt.zip`, we will get the following structure:
```
- evaluation_examples/documents/docs/doc_txt/:
  - webpage_title.json
  - airbyte.com/
    - quickstarts.txt
    - quickstart/
      - aggregating-data-from-mysql-and-postgres-into-bigquery-with-airbyte.txt
      - ...
    - blog/
    - tutorials/
    - docs.airbyte.com/
  - cloud.google.com/bigquery/docs/
    - access-control-basic-roles.txt
    - admin-intro.txt
    - ...
  - ...
```
Here, each `.txt` in a sub-folder represent a pre-processed text file which can be retrieved. We also preserve the website structure for each `.txt` file. For the meta file `webpage_title.json`, it records the web page title for each `.txt` file. We believe both the web page path and title are meaningful during retrieval. For the other two formats, namely `.html` and `.md`, the only difference is that each `.txt` file is pre-processed into Markdown or simplified HTML formats.

## How to Use

We present a simple retrieval baseline (`mm_agents/retrieval/llama_index_retrieval.py`) in Spider2-V. It utilizes the task instruction as the query vector, huggingface `BAAI/bge-large-en-v1.5` as the embedding model, and [LlamaIndex](https://pypi.org/project/llama-index/) framework as the retrieval to generate context for each task example. The retrieved context file is also provided under each task-specific folder (*e.g.*, `retrieved_chunk_size_512_chunk_overlap_20_topk_4_embed_bge-large-en-v1.5.txt`). We get all context files via script:
```bash
cd evaluation_examples/documents
git lfs install
git clone https://huggingface.co/BAAI/bge-large-en-v1.5
cd ../../
# you can use other document formats, e.g., --doc_directory evaluation_examples/documents/docs/doc_md
# this step may take some time to build the embedding index
python mm_agents/retrieval/llama_index_retrieval.py --embed_model_name_or_path evaluation_examples/documents/bge-large-en-v1.5 --doc_directory evaluation_examples/documents/docs/doc_txt
```
Feel free to use more advanced RAG method based on the document warehouse!