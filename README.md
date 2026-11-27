# Image-Processing-Project

# Classical Image Processing Pipeline for Car License Plate Detection

## Problem Formulation:
Automated traffic enforcement and smart parking access control systems require accurate localization of vehicle license plates from surveillance camera imagery. Given an input RGB vehicle image (8-bit depth per channel, varying spatial resolutions), the classical image processing pipeline outputs bounding-box coordinates $(x_{\min}, y_{\min}, x_{\max}, y_{\max})$ surrounding each license plate. An inaccurate localization—either cropping out plate characters or including excessive background clutter—causes downstream optical character recognition (OCR) failures, leading to unauthorized gate access or missed traffic violations. Consequently, Intersection over Union (IoU) is selected as the primary evaluation metric because it simultaneously penalizes missed plate regions and oversized bounding boxes.

## Team Roles & Responsibilities
| Role | Team Member | GitHub Username | Primary Modules |
| :--- | :--- | :--- | :--- |
| **Tech Lead, Data & Baselines** | Omar Abed | `@your-username` | `data.py`, `metrics.py`, `pipeline.py`, `configs/` |
| **Enhancement Engineer** | Member 2 | `@member2-username` | `enhancement.py` |
| **Restoration & Frequency Engineer** | Member 3 | `@member3-username` | `restoration.py`, `frequency.py` |
| **Segmentation Engineer** | Member 4 | `@member4-username` | `segmentation.py` |
| **Morphology & Evaluation Engineer** | Member 5 | `@member5-username` | `morphology.py`, `evaluate.py`, `run_pipeline.py`, `app/` |

## Repository Structure
```text
├── README.md
├── requirements.txt
├── configs/                # YAML configuration files per pipeline
├── data/                   # Dataset download script and documentation
├── notebooks/              # Exploratory analysis and final results notebooks
├── src/                    # Modular classical image processing stages
├── experiments/            # Experiment logs (CSV) and saved figures
├── app/                    # Interactive demo application
└── report/                 # IEEE-format technical report (PDF) and slides
