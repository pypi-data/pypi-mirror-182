import logging
import os
import shutil
from .hf_utils.object_detection_dataset import export_hf_object_detection_dataset_script
from .hf_utils.image_classification_dataset import (
    export_hf_image_classification_dataset_script,
)
from .roboflow_utils import download_roboflow_dataset, zip_roboflow_dataset
from .hf_utils.dataset_card import export_hf_dataset_card
from .hf_utils.hub import upload_dataset_to_hfhub

LOGLEVEL = os.environ.get("LOGLEVEL", "INFO").upper()
logging.basicConfig(level=LOGLEVEL)
LOGGER = logging.getLogger(__name__)


__version__ = "0.0.1"


def roboflow_to_huggingface_pipeline(
    roboflow_universe_url: str,
    hf_dataset_id: str,
    roboflow_api_key: str = None,
    local_data_dir: str = "roboflow_dataset",
    hf_private: bool = False,
    hf_write_token: str = None,
    keep_local: bool = False,
):
    """
    Downloads a Roboflow dataset and uploads it to the Hugging Face Hub.

    Args:
        roboflow_universe_url (str): The Roboflow universe URL.
        hf_dataset_id (str): The name of the dataset on the Hugging Face Hub.
        roboflow_api_key (str, optional): The Roboflow API key. Defaults to None.
        local_data_dir (str, optional): The local directory to download the dataset to. Defaults to "roboflow_dataset".
        hf_private (bool, optional): Whether the dataset should be private on the Hugging Face Hub. Defaults to False.
        hf_write_token (str, optional): The token to use to authenticate to the Hugging Face Hub. Defaults to None.
        keep_local (bool, optional): Whether to keep the local dataset. Defaults to False.
    """
    roboflow_api_key = roboflow_api_key or os.environ.get("ROBOFLOW_API_KEY")

    project, dataset, task = download_roboflow_dataset(
        roboflow_universe_url, api_key=roboflow_api_key, location=local_data_dir
    )

    zip_roboflow_dataset(local_data_dir, roboflow_dataset=dataset)

    if task == "object-detection":
        export_hf_object_detection_dataset_script(
            hf_dataset_id=hf_dataset_id,
            roboflow_universe_url=roboflow_universe_url,
            roboflow_project=project,
            roboflow_dataset=dataset,
            export_dir=local_data_dir,
        )
    elif task == "image-classification":
        export_hf_image_classification_dataset_script(
            hf_dataset_id=hf_dataset_id,
            roboflow_universe_url=roboflow_universe_url,
            roboflow_project=project,
            roboflow_dataset=dataset,
            export_dir=local_data_dir,
        )

    export_hf_dataset_card(task=task, export_dir=local_data_dir)

    upload_dataset_to_hfhub(
        dataset_dir=local_data_dir,
        repo_id=hf_dataset_id,
        token=hf_write_token,
        private=hf_private,
    )

    if not keep_local:
        shutil.rmtree(local_data_dir)
