import numpy as np


def compute_mse(img1, img2):
    """Computes Mean Squared Error between two images."""
    diff = img1.astype(np.float64) - img2.astype(np.float64)
    return float(np.mean(diff ** 2))


def compute_psnr(img1, img2, max_pixel=255.0):
    """Computes Peak Signal-to-Noise Ratio (dB) between two images."""
    mse = compute_mse(img1, img2)
    if mse == 0:
        return float("inf")
    return float(10.0 * np.log10((max_pixel ** 2) / mse))


def compute_iou(box_a, box_b):
    """Computes Intersection over Union for two boxes (x1, y1, x2, y2)."""
    x_left = max(box_a[0], box_b[0])
    y_top = max(box_a[1], box_b[1])
    x_right = min(box_a[2], box_b[2])
    y_bottom = min(box_a[3], box_b[3])

    if x_right <= x_left or y_bottom <= y_top:
        return 0.0

    inter_area = (x_right - x_left) * (y_bottom - y_top)
    area_a = (box_a[2] - box_a[0]) * (box_a[3] - box_a[1])
    area_b = (box_b[2] - box_b[0]) * (box_b[3] - box_b[1])
    union_area = float(area_a + area_b - inter_area)

    return float(inter_area / union_area) if union_area > 0 else 0.0
