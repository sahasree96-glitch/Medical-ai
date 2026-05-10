import csv
import os
from datetime import datetime
from config import *

class PatientRecordManager:
    """Manages patient records and lesion history"""
    
    def __init__(self):
        self.initialize_log()
    
    def initialize_log(self):
        """Initialize CSV log file if it doesn't exist"""
        if not os.path.exists(LOG_FILE):
            os.makedirs(LOG_DIR, exist_ok=True)
            with open(LOG_FILE, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=PATIENT_RECORD_COLUMNS)
                writer.writeheader()
    
    def add_record(self, patient_id, image_path, measurements):
        """Add analysis record to patient history"""
        record = {
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'patient_id': patient_id,
            'lesion_id': f"L_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            'image_path': image_path,
            'area_pixels': measurements['area_pixels'],
            'area_mm2': measurements['area_mm2'],
            'perimeter_pixels': measurements['perimeter_pixels'],
            'perimeter_mm': measurements['perimeter_mm'],
            'circularity_index': measurements['circularity_index'],
            'asymmetry_score': measurements['asymmetry_score'],
            'edge_definition': 'N/A',
            'color_dominance': 'N/A',
            'size_category': measurements['size_category'],
            'recommendation': measurements['recommendation'],
            'notes': ''
        }
        
        with open(LOG_FILE, 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=PATIENT_RECORD_COLUMNS)
            writer.writerow(record)
        
        print(f"✅ Record saved for patient {patient_id}")
