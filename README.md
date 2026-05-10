# MedScan AI - Skin Lesion Diagnostic Assistant

A computer vision-based application that analyzes digital images of skin anomalies to assist medical professionals in early detection and consistent tracking of skin conditions.

## ⚠️ Disclaimer

This is an **educational and diagnostic assistance tool**, NOT a replacement for professional medical diagnosis. Results should be validated by qualified dermatologists. Always consult medical professionals before making any healthcare decisions based on this tool's output.

## 🎯 Project Overview

**Problem Statement:**
Medical professionals rely on subjective visual observation for skin condition assessment. This variability in interpretation can lead to inconsistent diagnoses and delayed detection of serious conditions.

**Solution:**
MedScan AI provides objective, data-driven analysis of skin lesions by:
- Automatically preprocessing images to remove noise and artifacts
- Segmenting and isolating abnormal tissue using advanced color-space thresholding
- Calculating precise surface area, perimeter, and shape metrics
- Visualizing detected anomalies with highlighted boundaries
- Tracking patient lesion history over time for progression analysis

**What It Does:**
- Analyzes digital images of skin lesions, rashes, and moles
- Provides exact measurements in pixels and millimeters
- Flags irregular patterns and asymmetries
- Assists in early detection and consistent tracking of skin conditions
- Generates professional diagnostic reports

## ✨ Features

### 1. **Image Pre-processing**
- ✅ Gaussian blur to remove noise (shadows, fine hairs)
- ✅ Bilateral filtering to preserve edge details
- ✅ CLAHE (Contrast Limited Adaptive Histogram Equalization)
- ✅ Automatic image resizing for optimization

### 2. **Lesion Segmentation**
- ✅ HSV color-space thresholding for abnormal tissue isolation
- ✅ Morphological operations (erosion, dilation, opening, closing)
- ✅ Multi-lesion detection and filtering
- ✅ Contour refinement and validation

### 3. **Automated Measurement**
- ✅ Surface area calculation (pixels and mm²)
- ✅ Perimeter measurement
- ✅ Circularity Index (0=irregular, 1=perfect circle)
- ✅ Asymmetry Score (0=symmetric, 1=highly asymmetric)
- ✅ Edge definition analysis
- ✅ Size category classification (Small, Medium, Large, Very Large)

### 4. **Visual Highlighting**
- ✅ Real-time contour detection and drawing
- ✅ Bounding box visualization
- ✅ Side-by-side before/after comparison
- ✅ Annotated measurements on output images
- ✅ Multiple export formats (JPG, PNG)

### 5. **Patient Record Management**
- ✅ CSV-based patient database
- ✅ Lesion history tracking
- ✅ Temporal analysis and progression detection
- ✅ Clinical recommendations based on metrics
- ✅ Patient search and export functionality

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- 200MB disk space

### Installation & Setup

#### Step 1: Clone the Repository
```bash
git clone https://github.com/sahasree96-glitchhey/medical-ai.git
cd medical-ai
