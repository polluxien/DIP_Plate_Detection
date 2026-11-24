# License Plate Recognition under Motion Blur: A Restoration-Based Approach

**CMPE7144 Digital Image Processing — Term Project Proposal (Fall 2026)**

Bennet Worrmann | Student ID: 9850260002 | 19.10.2026

---

## 1. Problem Statement and Motivation

Vehicle images from traffic, parking or handheld cameras are often degraded by motion blur, which smears plate characters and causes automatic license plate recognition (ALPR) to fail. This project investigates whether classical restoration techniques can make motion-blurred plates readable again, and quantifies the resulting gain in recognition accuracy.

## 2. Objectives

- Build a pipeline covering plate localization, deblurring, character segmentation and recognition.
- Compare several restoration methods for linear motion blur.
- Measure how blur length, blur angle and noise affect recognition, with and without restoration.

## 3. Methodology

- **Blur simulation:** Sharp plate images are artificially blurred with motion blur of different strengths and directions, and noise is added.
- **Plate detection:** The plate region is located using edge detection and contour analysis.
- **Restoration:** Three methods are compared: inverse filtering (baseline), Wiener filtering and Richardson–Lucy deconvolution.
- **Recognition:** The restored plate is binarized and read with Tesseract OCR.

## 4. Data and Evaluation

About 100–200 plate images from [platesmania.com/tr/gallery](https://platesmania.com/tr/gallery), synthetically blurred so that exact ground truth is available. A few real blurred photos will be tested qualitatively. The metrics are:

- **Restoration quality:** PSNR and SSIM.
- **Recognition:** character error rate and full-plate accuracy vs. blur length, blur angle and noise level.
- **Robustness:** sensitivity to PSF estimation errors and noise, plus runtime.

## 5. Tools

Python (OpenCV, NumPy, SciPy, scikit-image, pytesseract) for processing and experiments, and a TypeScript web front end for interactive visualization.

## 6. Expected Outcome

A working restoration-and-recognition application, and a quantitative comparison showing under which blur and noise conditions each method restores readability, and where recovery fails.

---

## To Run this project 

```shell
uv run dip-coding-project
```

*right now image inout hardcoded will change with frontend*