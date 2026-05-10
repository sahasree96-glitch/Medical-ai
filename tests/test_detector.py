import pytest
import numpy as np
import cv2
from config import *
from lesion_detector import LesionDetector
from measurements import LesionMeasurement

class TestLesionDetector:
    """Test suite for lesion detection"""
    
    def test_segment_lesion(self):
        """Test lesion segmentation"""
        # Create dummy HSV image
        hsv_image = np.zeros((100, 100, 3), dtype=np.uint8)
        
        # Add some darker pixels (lesion area)
        hsv_image[30:70, 30:70] = [90, 100, 80]
        
        # Segment
        mask = LesionDetector.segment_lesion(hsv_image)
        
        assert mask is not None
        assert mask.shape == (100, 100)
    
    def test_find_contours(self):
        """Test contour detection"""
        mask = np.zeros((100, 100), dtype=np.uint8)
        cv2.circle(mask, (50, 50), 20, 255, -1)
        
        contours = LesionDetector.find_contours(mask)
        
        assert len(contours) > 0
    
    def test_calculate_area(self):
        """Test area calculation"""
        # Create circular contour
        contour = np.array([[[50, 30]], [[70, 50]], [[50, 70]], [[30, 50]]], dtype=np.int32)
        
        measurements = LesionMeasurement.calculate_area_and_perimeter(contour)
        
        assert 'area_pixels' in measurements
        assert 'area_mm2' in measurements
        assert measurements['area_pixels'] > 0
    
    def test_calculate_circularity(self):
        """Test circularity calculation"""
        # Create circular contour
        contour = np.array([[[50, 30]], [[70, 50]], [[50, 70]], [[30, 50]]], dtype=np.int32)
        
        circularity = LesionMeasurement.calculate_circularity(contour)
        
        assert 0 <= circularity <= 1
    
    def test_size_classification(self):
        """Test size category classification"""
        assert LesionMeasurement.classify_size_category(2) == "Small"
        assert LesionMeasurement.classify_size_category(7) == "Medium"
        assert LesionMeasurement.classify_size_category(15) == "Large"
        assert LesionMeasurement.classify_size_category(30) == "Very Large"

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
