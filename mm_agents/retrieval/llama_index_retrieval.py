#coding=utf8
from typing import Dict


# retrieved_docs_llama_index.txt

LLAMDA_INDEX_RETRIEVAL = None

class 

    def retrieve_docs_by_llama_index(self, data: Dict, format: str = 'text', topk: int = 4, chunk_size: int = 512, chunk_method: str = 'sentence'):
        """
        @args:
            data: Dict, the json data to be used for retrieval
                instruction: str, the instruction for the retrieval
                related_apps: List[str], the related apps for the retrieval
            format: str, the format of the retrieved documents, either 'text', 'html' or 'markdown'
        @return:
            {related_context: str
            title: xxx
            path: xxx}
        """
    
    def retrieve_docs_to_prompt(self, docs: dict, filename: str = None) -> str:
        """
        Retrieve the documents to prompt
        """
        pass


def get_llama_index_retrieval():
    """
    Get the llama index retrieval object
    """
    if LLAMDA_INDEX_RETRIEVAL is None:
        raise ValueError("LLAMDA_INDEX_RETRIEVAL is not initialized yet.")
    return LLAMDA_INDEX_RETRIEVAL


if __name__ == '__main__':

    import argparse

    python xxx.py --example_dir evaluation_examples/examples # skip
    pass
