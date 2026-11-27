
import os
import json
import random
import cv2
import numpy as np


def load_image(image_path, target_size=(480, 320), grayscale=False):
    """Unified image loader: converts BGR to RGB/Grayscale and resizes."""
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Image not found: {image_path}")

    orig_h, orig_w = img.shape[:2]
    if grayscale:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    if target_size is not None:
        img = cv2.resize(img, target_size, interpolation=cv2.INTER_AREA)

    return img.astype(np.uint8), (orig_w, orig_h)


def load_ground_truth(ann_path, orig_size, target_size=(480, 320)):
    """Loads bounding boxes from JSON and scales them to match target_size."""
    with open(ann_path, "r") as f:
        data = json.load(f)

    orig_w, orig_h = orig_size
    scale_x = target_size[0] / orig_w if target_size else 1.0
    scale_y = target_size[1] / orig_h if target_size else 1.0

    boxes = []
    for obj in data.get("objects", []):
        pts = obj["points"]["exterior"]
        x1 = int(round(pts[0][0] * scale_x))
        y1 = int(round(pts[0][1] * scale_y))
        x2 = int(round(pts[1][0] * scale_x))
        y2 = int(round(pts[1][1] * scale_y))
        boxes.append((x1, y1, x2, y2))

    return boxes


def split_dataset(img_dir, train_ratio=0.7, seed=42):
    """Splits image filenames deterministically into dev and test sets."""
    files = sorted([f for f in os.listdir(img_dir) if f.endswith((".png", ".jpg"))])
    rng = random.Random(seed)
    rng.shuffle(files)

    split_idx = int(len(files) * train_ratio)
    dev_files = files[:split_idx]
    test_files = files[split_idx:]
    return dev_files, test_files


def add_noise(image, noise_type="gaussian", level=25.0, seed=42):
    """Adds controlled noise (gaussian, salt_pepper, speckle) with fixed seed."""
    rng = np.random.default_rng(seed)
    img_float = image.astype(np.float32)

    if noise_type == "gaussian":
        noise = rng.normal(0, level, img_float.shape)
        noisy = img_float + noise
    elif noise_type == "salt_pepper":
        noisy = img_float.copy()
        prob = level / 100.0  # e.g., level=5 means 5% corrupted pixels
        rand_mat = rng.random(img_float.shape[:2])
        noisy[rand_mat < (prob / 2)] = 0
        noisy[rand_mat > 1 - (prob / 2)] = 255
    elif noise_type == "speckle":
        noise = rng.normal(0, level / 100.0, img_float.shape)
        noisy = img_float + img_float * noise
    else:
        raise ValueError(f"Unsupported noise type: {noise_type}")

    return np.clip(noisy, 0, 255).astype(np.uint8)
