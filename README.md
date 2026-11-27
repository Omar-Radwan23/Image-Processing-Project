# Image-Processing-Project

# Classical Image Processing Pipeline for Car License Plate Detection

## Problem Formulation
Automated vehicle identification relies on accurately localizing license plates under real-world surveillance conditions, including varying illumination, shadows, perspective distortion, and background clutter. This project implements a purely classical, modular image processing pipeline—using zero machine learning or deep learning—to detect and localize license plate bounding boxes on the **Car License Plate Dataset** (433 images, 471 annotated plates). Detection performance is evaluated primarily via **Intersection over Union (IoU)** against ground-truth bounding boxes.

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
