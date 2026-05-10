import cv2
import numpy as np
import matplotlib.pyplot as plt
from config import *

class Visualizer:
    """Handles visualization and report generation"""
    
    @staticmethod
    def draw_contours(image, contours):
        """Draw contours on image"""
        output = image.copy()
        cv2.drawContours(output, contours, -1, COLOR_CONTOUR, CONTOUR_THICKNESS)
        return output
    
    @staticmethod
    def draw_bounding_boxes(image, contours):
        """Draw bounding boxes around lesions"""
        output = image.copy()
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(output, (x, y), (x+w, y+h), COLOR_BOUNDING_BOX, 
                         BOUNDING_BOX_THICKNESS)
        return output
    
    @staticmethod
    def create_comparison_figure(original, segmented, annotated, metrics):
        """Create side-by-side comparison figure"""
        fig, axes = plt.subplots(1, 3, figsize=(15, 5))
        
        axes[0].imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
        axes[0].set_title("Original Image")
        axes[0].axis('off')
        
        axes[1].imshow(segmented, cmap='gray')
        axes[1].set_title("Segmentation Mask")
        axes[1].axis('off')
        
        axes[2].imshow(cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB))
        axes[2].set_title("Detected Lesion")
        axes[2].axis('off')
        
        plt.suptitle(f"Lesion Analysis Report\nArea: {metrics['area_mm2']} mm²", 
                     fontsize=14, fontweight='bold')
        
        return fig
    
    @staticmethod
    def print_report(metrics):
        """Print diagnostic report"""
        print("\n" + "="*60)
        print("MEDSCAN AI - DIAGNOSTIC REPORT")
        print("="*60)
        print(f"\nMEASUREMENTS:")
        print(f"  Area: {metrics['area_mm2']} mm² ({metrics['area_pixels']} pixels²)")
        print(f"  Perimeter: {metrics['perimeter_mm']} mm ({metrics['perimeter_pixels']} pixels)")
        print(f"\nDIAGNOSTIC METRICS:")
        print(f"  Circularity Index: {metrics['circularity_index']}")
        print(f"  Asymmetry Score: {metrics['asymmetry_score']}")
        print(f"  Size Category: {metrics['size_category']}")
        print(f"\nRECOMMENDATION:")
        print(f"  {metrics['recommendation']}")
        print("="*60 + "\n")
