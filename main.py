import cv2
import os
import sys
import argparse
from datetime import datetime
from config import *
from image_processor import ImageProcessor
from lesion_detector import LesionDetector
from measurements import LesionMeasurement
from visualizer import Visualizer
from patient_record import PatientRecordManager

class MedScanAI:
    """Main MedScan AI application"""
    
    def __init__(self):
        self.create_directories()
        self.record_manager = PatientRecordManager()
    
    def create_directories(self):
        """Create necessary directories"""
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        os.makedirs(LOG_DIR, exist_ok=True)
        os.makedirs(SAMPLE_IMAGES_DIR, exist_ok=True)
    
    def analyze_image(self, image_path, patient_id):
        """Analyze single image"""
        try:
            # Load and preprocess image
            image = ImageProcessor.load_image(image_path)
            hsv, bilateral, original = ImageProcessor.preprocess_image(image)
            
            # Detect lesions
            mask, contours = LesionDetector.detect_lesions(hsv)
            
            if not contours:
                print("❌ No lesions detected in image")
                return None
            
            # Process first detected lesion
            contour = contours[0]
            
            # Calculate measurements
            measurements = LesionMeasurement.calculate_area_and_perimeter(contour)
            measurements['circularity_index'] = LesionMeasurement.calculate_circularity(contour)
            measurements['asymmetry_score'] = LesionMeasurement.calculate_asymmetry(contour)
            measurements['size_category'] = LesionMeasurement.classify_size_category(
                measurements['area_mm2'])
            measurements['recommendation'] = LesionMeasurement.generate_recommendation(measurements)
            
            # Visualize results
            annotated = Visualizer.draw_contours(original, [contour])
            Visualizer.print_report(measurements)
            
            # Save results
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_path = os.path.join(OUTPUT_DIR, f"analysis_{timestamp}.jpg")
            cv2.imwrite(output_path, annotated)
            print(f"✅ Analysis saved to: {output_path}")
            
            # Record in database
            self.record_manager.add_record(patient_id, image_path, measurements)
            
            return measurements
            
        except Exception as e:
            print(f"❌ Error analyzing image: {e}")
            return None
    
    def run(self, args):
        """Run the application"""
        if args.image:
            self.analyze_image(args.image, args.patient_id)
        else:
            print("Please provide image path: python main.py --image path/to/image.jpg")

def main():
    parser = argparse.ArgumentParser(description="MedScan AI - Skin Lesion Diagnostic Assistant")
    parser.add_argument("--image", type=str, help="Path to skin lesion image")
    parser.add_argument("--patient_id", type=str, default="UNKNOWN", help="Patient ID")
    
    args = parser.parse_args()
    
    app = MedScanAI()
    app.run(args)

if __name__ == "__main__":
    main()
