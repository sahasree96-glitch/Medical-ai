import cv2
import numpy as np
from config import *

class ImageProcessor:
    """Handles image preprocessing and preparation for lesion detection"""
    
    @staticmethod
    def load_image(image_path):
        """Load image from file path"""
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError(f"Cannot load image: {image_path}")
        return image
    
    @staticmethod
    def preprocess_image(image):
        """Apply preprocessing pipeline"""
        # 1. Resize if too large
        height, width = image.shape[:2]
        if width > MAX_IMAGE_WIDTH or height > MAX_IMAGE_HEIGHT:
            scale = min(MAX_IMAGE_WIDTH/width, MAX_IMAGE_HEIGHT/height)
            new_width = int(width * scale)
            new_height = int(height * scale)
            image = cv2.resize(image, (new_width, new_height))
        
        # 2. Apply Gaussian blur
        blurred = cv2.GaussianBlur(image, GAUSSIAN_BLUR_KERNEL, 0)
        
        # 3. Apply bilateral filtering
        bilateral = cv2.bilateralFilter(blurred, BILATERAL_D, 
                                       BILATERAL_SIGMA_COLOR, 
                                       BILATERAL_SIGMA_SPACE)
        
        # 4. Convert BGR to HSV
        hsv = cv2.cvtColor(bilateral, cv2.COLOR_BGR2HSV)
        
        return hsv, bilateral, image
    
    @staticmethod
    def enhance_contrast(image):
        """Apply CLAHE for contrast enhancement"""
        lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
        l_channel, a_channel, b_channel = cv2.split(lab)
        
        clahe = cv2.createCLAHE(clipLimit=CLAHE_CLIP_LIMIT, 
                               tileGridSize=CLAHE_TILE_GRID_SIZE)
        l_enhanced = clahe.apply(l_channel)
        
        enhanced_lab = cv2.merge([l_enhanced, a_channel, b_channel])
        enhanced_image = cv2.cvtColor(enhanced_lab, cv2.COLOR_LAB2BGR)
        
        return enhanced_image
