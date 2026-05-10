import cv2
import numpy as np
from config import *

class LesionDetector:
    """Detects and segments skin lesions using HSV thresholding"""
    
    @staticmethod
    def segment_lesion(hsv_image):
        """Segment lesion using HSV thresholding"""
        # Create mask using HSV thresholds
        mask = cv2.inRange(hsv_image, HSV_LOWER, HSV_UPPER)
        
        # Apply morphological operations
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, KERNEL_SIZE)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, 
                               iterations=MORPHOLOGY_ITERATIONS)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, 
                               iterations=MORPHOLOGY_ITERATIONS)
        
        return mask
    
    @staticmethod
    def find_contours(mask):
        """Find and filter contours in the mask"""
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, 
                                      cv2.CHAIN_APPROX_SIMPLE)
        
        valid_contours = []
        for contour in contours:
            area = cv2.contourArea(contour)
            perimeter = cv2.arcLength(contour, True)
            
            # Filter by size and perimeter
            if (MIN_CONTOUR_AREA < area < MAX_CONTOUR_AREA and 
                perimeter > MIN_CONTOUR_PERIMETER):
                valid_contours.append(contour)
        
        return valid_contours
    
    @staticmethod
    def detect_lesions(hsv_image):
        """Complete lesion detection pipeline"""
        mask = LesionDetector.segment_lesion(hsv_image)
        contours = LesionDetector.find_contours(mask)
        return mask, contours
