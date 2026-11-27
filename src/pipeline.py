
import cv2
import numpy as np


def _largest_contour_box(binary_mask):
    """Extracts the bounding box (x1, y1, x2, y2) of the largest white component."""
    contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        return (0, 0, 0, 0)
    largest = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(largest)
    return (x, y, x + w, y + h)


def trivial_baseline(gray_image):
    """Baseline 1: Fixed global threshold at 127 on raw grayscale image."""
    _, binary = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
    return _largest_contour_box(binary), binary


def simple_baseline(gray_image):
    """Baseline 2: Otsu thresholding followed by one 3x3 morphological opening."""
    _, binary = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    kernel = np.ones((3, 3), np.uint8)
    opened = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations=1)
    return _largest_contour_box(opened), opened