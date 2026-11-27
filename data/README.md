# Dataset: Car License Plate Detection

## Overview
* **Dataset Name:** Car License Plate Detection
* **Source:** [Dataset Ninja - Car License Plate](https://datasetninja.com/car-license-plate) (originally released by Make ML).
* **License:** CC0 1.0 Universal (Public Domain — permitted for academic and non-commercial use).
* **Size:** 433 real-world vehicle/surveillance images with 471 annotated license plate bounding boxes (1 class: `license plate`).
* **Image Characteristics:** Varied image resolutions (e.g., 225×400, 400×301), real-world illumination changes, shadows, perspective angles, and dense vertical edge structures within the plate region.

## Download & Setup Instructions
Raw images are excluded from version control via `.gitignore`. To download and prepare the dataset locally or on Google Colab:

1. **Automated Download (Recommended):**
   Install `dataset-tools` and run the provided download script from the repository root:
   ```bash
   pip install dataset-tools
   python data/download_data.py
