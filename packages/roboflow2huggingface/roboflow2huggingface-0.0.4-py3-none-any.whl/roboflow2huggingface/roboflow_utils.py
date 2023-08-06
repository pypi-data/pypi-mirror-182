import logging
import shutil

LOGGER = logging.getLogger(__name__)


def parse_citation(universe_url) -> str:
    """
    Parses the citation from a Roboflow Universe URL.

    Args:
        universe_url (str): Roboflow Universe URL
            example: https://universe.roboflow.com/boxer5/123-qq5ea/dataset/6

    Returns:
        citation (str): Citation for the dataset
    """
    import requests
    import urllib
    from bs4 import BeautifulSoup

    url = urllib.parse.urlparse(universe_url)
    if url[1] != "universe.roboflow.com":
        raise ValueError("Not a valid Roboflow Universe URL.")

    project_url = universe_url.split("/dataset")[0] + "/"
    request = requests.get(project_url)
    soup = BeautifulSoup(request.text, "html.parser")
    citation = soup.find("code").get_text(strip=True)
    citation = citation.replace("\\", "\\\\")
    return citation


def download_roboflow_dataset(
    universe_url, api_key, location="roboflow_dataset"
) -> tuple:
    """
    Downloads a Roboflow dataset to a local directory.

    Args:
        universe_url (str): Roboflow Universe URL
            example: https://universe.roboflow.com/boxer5/123-qq5ea/dataset/6
        api_key (str): Roboflow API key
        location (str): Directory to download the dataset to

    Returns:
        project (roboflow.core.project.Project): Roboflow project object
        dataset (roboflow.core.version.Version): Roboflow dataset object
        task (str): Huggingface dataset task type. Supported types: ('image-classification', 'object-detection')
    """
    import urllib
    import roboflow

    url = urllib.parse.urlparse(universe_url)
    if url[1] != "universe.roboflow.com":
        raise ValueError("Not a valid Roboflow Universe URL.")
    _, workspace, project, _, version = url[2].split("/")

    rf = roboflow.Roboflow(api_key=api_key)
    project = rf.workspace(workspace).project(project)
    dataset = project.version(version)
    dataset_type = dataset.type
    if dataset_type == "classification":
        task = "image-classification"
        dataset.download("folder", location=location)
    elif dataset_type == "object-detection":
        task = "object-detection"
        dataset.download("coco", location=location)
    else:
        raise ValueError(
            "Roboflow dataset type not supported {dataset_type}. Supported types: ('classification', 'object-detection')"
        )

    return project, dataset, task


def zip_roboflow_dataset(roboflow_dir, roboflow_dataset):
    """
    Zips the Roboflow dataset splits.

    Args:
        roboflow_dir (str): Path to the Roboflow dataset directory.
        roboflow_dataset (roboflow.core.version.Version): The Roboflow dataset object.
    """
    from pathlib import Path

    LOGGER.info("Zipping Roboflow dataset splits...")

    for split in roboflow_dataset.splits.keys():
        source = Path(roboflow_dir) / split
        shutil.make_archive(
            Path(roboflow_dir) / "data" / split, format="zip", root_dir=source
        )
        shutil.rmtree(source)

    LOGGER.info("Roboflow dataset splits zipped!")
