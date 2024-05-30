#coding=utf8
import io
import nbformat
from typing import Dict, Any
import json
from PIL import Image
from skimage.metrics import structural_similarity as ssim
import cv2

def is_jupyter_cell_executed(result: str, expected: Dict[str, Any], **options) -> float:
    """ Determine whether all cells in a Jupyter notebook are executed.
    @args:
        result: str - the path to the Jupyter notebook file.
        expected: Dict[str, Any] - the expected result.
            key: expected, value: List[int] - the expected unexecuted cell indices.
        options: Dict[str, Any] - the options.
    """
    try:
        with io.open(result, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=options.get('version', 4))
        cell_type = options.get('cell_type', 'code')
        
        unexecuted = []
        for idx, cell in enumerate(nb.cells):
            if cell.cell_type == cell_type:
                if not cell.get('execution_count'):
                    unexecuted.append(idx)
        print(unexecuted)
        if unexecuted != expected['expected']:
            return 0.0
        return 1.0
    except Exception as e:
        print(e)
        return 0.0
    
def compare_ipynb_files(result: str, expected: str, **options) -> float:
    """ Compare two Jupyter notebook files.
    @args:
        result: str - the path to the Jupyter notebook file.
        expected: str - the path to the expected Jupyter notebook file.
        options: Dict[str, Any] - the options.
    """
    try:
        with io.open(result, 'r', encoding='utf-8') as f:
            ipynb_file1 = json.load(f)
        with io.open(expected, 'r', encoding='utf-8') as f:
            ipynb_file2 = json.load(f)
        
        for (k1, v1), (k2, v2) in zip(ipynb_file1.items(), ipynb_file2.items()):
            if k1 != k2:
                return 0.0
            if k1 != 'metadata' and v1 != v2:
                return 0.0
        return 1.0
    except Exception as e:
        print(e)
        return 0.0
    

def compare_notebook_cells(result: str, expected: str) -> float:
    """ Compare two Jupyter notebook cells.
    @args:
        result: str - the path to the Jupyter notebook file.
        expected: str - the path to the expected Jupyter notebook file.
        options: Dict[str, Any] - the options.
    """
    try:
        with open(result, 'r', encoding='utf-8') as result_file:
            result_nb = nbformat.read(result_file, as_version=4)
        with open(expected, 'r', encoding='utf-8') as expected_file:
            expected_nb = nbformat.read(expected_file, as_version=4)
        
        result_cells = result_nb['cells']
        expected_cells = expected_nb['cells']
        
        if len(result_cells) != len(expected_cells):
            return 0.0
        
        for result_cell, expected_cell in zip(result_cells, expected_cells):
            if result_cell['cell_type'] != expected_cell['cell_type']:
                return 0.0
            if result_cell['source'] != expected_cell['source']:
                return 0.0
        return 1.0
    except Exception as e:
        print(e)
        return 0.0

def compare_notebook_outputs(result: str, expected: str) -> float:
    """ Compare two Jupyter notebook outputs.
    @args:
        result: str - the path to the Jupyter notebook file.
        expected: str - the path to the expected Jupyter notebook file.
        options: Dict[str, Any] - the options.
    """
    try:
        with open(result, 'r', encoding='utf-8') as result_file:
            result_nb = nbformat.read(result_file, as_version=4)
        with open(expected, 'r', encoding='utf-8') as expected_file:
            expected_nb = nbformat.read(expected_file, as_version=4)
        
        result_cells = result_nb['cells']
        expected_cells = expected_nb['cells']
        
        if len(result_cells) != len(expected_cells):
            print("Num of cells mismatch!")
            return 0.0
        
        for result_cell, expected_cell in zip(result_cells, expected_cells):
            if result_cell['cell_type'] != expected_cell['cell_type']:
                print("Cell type mismatch!")
                return 0.0
            if result_cell['cell_type'] == "code":
                result_cell_outputs = [output for output in result_cell['outputs'] if ('name' in output and output['name'] == 'stdout' and 'Requirement already satisfied:' not in output['text'] and 'Successfully installed' not in output['text']) or ('data' in output and 'text/plain' in output['data'])]
                expected_cell_outputs = [output for output in expected_cell['outputs'] if ('name' in output and output['name'] == 'stdout') or ('data' in output and 'text/plain' in output['data'])]
                if len(result_cell_outputs) != len(expected_cell_outputs):
                    print('Length of the following output mismatch:')
                    print(result_cell_outputs)
                    print(expected_cell_outputs)
                    return 0.0
                for result_output, expected_output in zip(result_cell_outputs, expected_cell_outputs):
                    if 'name' in result_output and result_output != expected_output:
                        print(result_output)
                        print(expected_output)
                        return 0.0
                    if 'data' in result_output and result_output['data']['text/plain'] != expected_output['data']['text/plain']:
                        print(result_output)
                        print(expected_output)
                        return 0.0
        return 1.0
    except Exception as e:
        print(e)
        return 0.0


def are_jupyter_outputs_cleared(result: str, expected: Dict[str, Any], **options) -> float:
    """ Determine whether all outputs in a Jupyter notebook are cleared.
    @args:
        result: str - the path to the Jupyter notebook file.
        expected: Dict[str, Any] - the expected result.
            key: expected, value: List[int] - the expected unexecuted cell indices.
        options: Dict[str, Any] - the options.
    """
    try:
        with io.open(result, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=options.get('version', 4))
        cell_type = options.get('cell_type', 'code')
        
        outputs_idx = []
        for idx, cell in enumerate(nb.cells):
            if cell.cell_type == cell_type:
                if cell.get('execution_count'):
                    outputs_idx.append(idx)
        print(outputs_idx)
        if outputs_idx != expected['expected']:
            return 0.0
        return 1.0
    except Exception as e:
        print(e)
        return 0.0
    
    
    
def compare_jupyterlab_images(image1_path, image2_path):
    # You would call this function with the paths to the two images you want to compare:
    # score = compare_images('path_to_image1', 'path_to_image2')
    # print("Similarity score:", score)

    if not image1_path or not image2_path:
        return 0

    # Open the images and convert to grayscale
    image1 = Image.open(image1_path).convert('L')
    image2 = Image.open(image2_path).convert('L')

    # Resize images to the smaller one's size for comparison
    image1_size = image1.size
    image2_size = image2.size
    
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)

    if image1_size > image2_size:
        image1 = cv2.resize(image1, (image2.shape[1], int(image1.shape[0] * image2.shape[1] / image1.shape[1])))
    else:
        image2 = cv2.resize(image2, (image1.shape[1], int(image2.shape[0] * image1.shape[1] / image2.shape[1])))
        
    # calculate the Histogram image of the two images
    H1 = cv2.calcHist([image1], [1], None, [256], [0, 256])
    H1 = cv2.normalize(H1, H1, 0, 1, cv2.NORM_MINMAX, -1)  # normalize the histogram

    H2 = cv2.calcHist([image2], [1], None, [256], [0, 256])
    H2 = cv2.normalize(H2, H2, 0, 1, cv2.NORM_MINMAX, -1)

    # compare the two histograms
    similarity = cv2.compareHist(H1, H2, 0)
    # import pdb; pdb.set_trace()
    if similarity == 1.0: # Account for image differences due to size change
        return 1
    return 0