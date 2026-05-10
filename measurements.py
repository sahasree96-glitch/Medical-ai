import cv2
import numpy as np
from config import *

class LesionMeasurement:
    """Calculate metrics and measurements for detected lesions"""
    
    @staticmethod
    def calculate_area_and_perimeter(contour):
        """Calculate area and perimeter of lesion"""
        area_pixels = cv2.contourArea(contour)
        perimeter_pixels = cv2.arcLength(contour, True)
        
        # Convert to mm²
        area_mm2 = area_pixels * (PIXEL_TO_MM_RATIO ** 2)
        perimeter_mm = perimeter_pixels * PIXEL_TO_MM_RATIO
        
        return {
            'area_pixels': area_pixels,
            'area_mm2': round(area_mm2, 2),
            'perimeter_pixels': perimeter_pixels,
            'perimeter_mm': round(perimeter_mm, 2)
        }
    
    @staticmethod
    def calculate_circularity(contour):
        """Calculate circularity index (0=irregular, 1=circle)"""
        area = cv2.contourArea(contour)
        perimeter = cv2.arcLength(contour, True)
        
        if perimeter == 0:
            return 0
        
        circularity = (4 * np.pi * area) / (perimeter ** 2)
        return min(round(circularity, 3), 1.0)
    
    @staticmethod
    def calculate_asymmetry(contour):
        """Calculate asymmetry score (0=symmetric, 1=asymmetric)"""
        # Approximate contour to polygon
        epsilon = CONTOUR_EPSILON_FACTOR * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        
        # Calculate moments for center
        M = cv2.moments(contour)
        if M["m00"] == 0:
            return 0
        
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
        
        # Calculate distances from center
        distances = []
        for point in approx:
            x, y = point[0]
            dist = np.sqrt((x - cx)**2 + (y - cy)**2)
            distances.append(dist)
        
        if len(distances) > 1:
            asymmetry = np.std(distances) / np.mean(distances)
            return min(round(asymmetry, 3), 1.0)
        
        return 0
    
    @staticmethod
    def classify_size_category(area_mm2):
        """Classify lesion size category"""
        if area_mm2 < SIZE_CATEGORY_SMALL:
            return "Small"
        elif area_mm2 < SIZE_CATEGORY_MEDIUM:
            return "Medium"
        elif area_mm2 < SIZE_CATEGORY_LARGE:
            return "Large"
        else:
            return "Very Large"
    
    @staticmethod
    def generate_recommendation(metrics):
        """Generate clinical recommendation based on metrics"""
        recommendations = []
        
        # Size-based recommendation
        if metrics['area_mm2'] > 10:
            recommendations.append("Large lesion - consider professional evaluation")
        
        # Asymmetry-based recommendation
        if metrics['asymmetry_score'] > ASYMMETRY_THRESHOLD:
            recommendations.append("Asymmetry detected - irregular shape observed")
        
        # Circularity-based recommendation
        if metrics['circularity_index'] < CIRCULARITY_IRREGULAR:
            recommendations.append("Irregular borders detected")
        
        if not recommendations:
            recommendations.append("Lesion appears regular - routine monitoring recommended")
        
        return " | ".join(recommendations)
