# Image-Processing-Project

# Classical Image Processing Pipeline for Car License Plate Detection

## Problem Formulation
Automated vehicle identification relies on accurately localizing license plates under real-world surveillance conditions, including varying illumination, shadows, perspective distortion, and background clutter. This project implements a purely classical, modular image processing pipeline—using zero machine learning or deep learning—to detect and localize license plate bounding boxes on the **Car License Plate Dataset** (433 images, 471 annotated plates). Detection performance is evaluated primarily via **Intersection over Union (IoU)** against ground-truth bounding boxes.

## Team Roles & Responsibilities
| Role | Team Member & GitHub | Work Package (Owner) | Code They Must Write | Image-Processing Contribution |
| :--- | :--- | :--- | :--- | :--- |
| **1 & 2. Tech Lead, Data & Baseline Engineer** | Omar Abed (`@your-username`) | Problem formulation, repository structure, integration, code review, final pipeline selection, image loading, splitting, ground truth, controlled degradation, metrics, both baselines | Project skeleton, config files, `data.py`, `metrics.py`, `pipeline.py`, baseline scripts, merges | Runs the resolution and gray-level study, compares Pipeline A with baselines, runs final pipeline at 3 noise levels and 3 seeds, and owns the final results table |
| **3. Enhancement Engineer** | Member 2 (`@member2-username`) | Histogram analysis, point transformations, histogram equalization, smoothing and sharpening filters | `enhancement.py` | Runs the enhancement comparison and the kernel-size study |
| **4. Restoration & Frequency Engineer** | Member 3 (`@member3-username`) | Noise models, restoration filters, DFT and frequency-domain filters | `restoration.py`, `frequency.py` | Runs the PSNR study per noise type and the spatial vs. frequency ablation |
| **5. Segmentation Engineer** | Member 4 (`@member4-username`) | Edge, point and line detection, thresholding, edge linking or Hough transform | `segmentation.py` | Runs the detector and threshold-method studies |
| **6. Morphology & Evaluation Engineer** | Member 5 (`@member5-username`) | Morphological refinement, measurement, test-set evaluation, failure analysis, demo | `morphology.py`, `evaluate.py`, `run_pipeline.py`, demo app | Runs the structuring-element studies and produces the failure-case analysis for every pipeline |

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
