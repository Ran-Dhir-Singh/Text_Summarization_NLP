import os
from box.exceptions import BoxValueError
import yaml
from src.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from typing import Any
from pathlib import Path



@ensure_annotations
def read_yaml(yaml_path:Path) -> ConfigBox:
    """
    Reads Yaml file using path and returns a configbox

    Args:
        yaml_path (str): path input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """

    try:
        with open(yaml_path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file : {yaml_path} loaded successfully")

            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError("yaml file is empty")
    
    except Exception as e:
        raise e
    


@ensure_annotations
def get_size(path : Path) -> str:
    """
    To get size fot file in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """

    size_kb = round(os.path.getsize(path)/1024)
    return f"~{size_kb}KB"



@ensure_annotations
def create_directories(directories_path : list, verbose=True):
    """
    create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """

    for path in directories_path:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info()