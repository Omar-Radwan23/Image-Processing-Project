"""Download script for the Car License Plate dataset from Dataset Ninja."""

import os
import sys


def download_car_plate_dataset(destination_dir: str = "data/raw") -> None:
    """Download and extract the Car License Plate dataset using dataset-tools.

    Args:
        destination_dir: Local directory path where the dataset will be saved.
    """
    try:
        import dataset_tools as dtools
    except ImportError:
        print(
            "Error: 'dataset-tools' is not installed. "
            "Install it using: pip install dataset-tools",
            file=sys.stderr,
        )
        sys.exit(1)

    os.makedirs(destination_dir, exist_ok=True)
    print(f"Downloading 'Car License Plate' dataset into '{destination_dir}'...")
    dtools.download(dataset="Car License Plate", dst_dir=destination_dir)
    print("Download complete.")


if __name__ == "__main__":
    download_car_plate_dataset()
