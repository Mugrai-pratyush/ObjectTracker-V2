# ObjectTracker-V2

An improved Python-based object detection simulation that identifies a square in a noisy pixel environment using data-driven analysis instead of hardcoded values.

---

## Overview
ObjectTracker-V2 simulates a grayscale image environment where a square is embedded in a randomly generated background.  
Unlike V1, the system automatically detects the square regardless of its pixel value, making it more robust and scalable.

---

## Key Improvements (V2)
- Removed hardcoded pixel dependency (no fixed "255" assumption)
- Dynamic square detection using frequency-based analysis
- Robust against random background noise
- Uses histogram and dictionary mapping for pixel clustering
- Generalized to detect squares of any pixel intensity

---

## How it Works
1. Background Generation  
   - Creates a 2D grid with random grayscale values (0–254)

2. Square Injection  
   - Inserts a square of size `side × side` with a consistent pixel value

3. Pixel Analysis  
   - Builds:
     - Histogram of pixel frequencies  
     - Dictionary mapping pixel values to coordinates  

4. Square Detection  
   - Identifies the square by:
     - Finding pixel values with at least `side²` occurrences  
     - Selecting the most dominant cluster  
     - Computing bounding box using min/max row and column  

5. Visualization  
   - Displays frames using matplotlib  

---

## Core Concept
Instead of relying on predefined values, the system detects objects based on:
- Pixel density  
- Spatial grouping  
- Statistical dominance  

This reflects foundational ideas used in computer vision pipelines.

---

## How to Run

```bash
python main.py