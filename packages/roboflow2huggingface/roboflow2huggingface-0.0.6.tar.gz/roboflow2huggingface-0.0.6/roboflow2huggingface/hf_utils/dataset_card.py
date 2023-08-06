def export_hf_dataset_card(export_dir, task="object-detection"):
    """
    Exports a dataset card to the specified directory.

    Args:
        export_dir (str): Path to the directory to export the dataset card to.
        task (str, optional): The task of the dataset. Defaults to "object-detection".
    """

    card = f"""---
task_categories:
- {task}
tags:
- roboflow
---
    """
    from pathlib import Path

    with open(Path(export_dir) / "README.md", "w") as f:
        f.write(card)
