# MedScan AI Configuration
# Image Processing Parameters
GAUSSIAN_BLUR_KERNEL = (5, 5)
BILATERAL_D = 9
BILATERAL_SIGMA_COLOR = 75
BILATERAL_SIGMA_SPACE = 75

# CLAHE Parameters
CLAHE_CLIP_LIMIT = 2.0
CLAHE_TILE_GRID_SIZE = (8, 8)

# HSV Thresholding Range (for skin lesion detection)
HSV_LOWER = (0, 20, 20)
HSV_UPPER = (180, 255, 200)

# Morphological Operations
KERNEL_SIZE = (5, 5)
MORPHOLOGY_ITERATIONS = 2

# Contour Detection
MIN_CONTOUR_AREA = 100
MAX_CONTOUR_AREA = 50000
MIN_CONTOUR_PERIMETER = 20
CONTOUR_EPSILON_FACTOR = 0.02

# Measurement Parameters
PIXEL_TO_MM_RATIO = 0.264  # Calibrate based on camera DPI

# Size Category Thresholds (mm²)
SIZE_CATEGORY_SMALL = 4
SIZE_CATEGORY_MEDIUM = 10
SIZE_CATEGORY_LARGE = 25

# Clinical Thresholds
CIRCULARITY_IRREGULAR = 0.7
ASYMMETRY_THRESHOLD = 0.3

# Visualization Parameters
COLOR_CONTOUR = (0, 255, 0)  # Green in BGR
COLOR_BOUNDING_BOX = (255, 0, 0)  # Blue in BGR
CONTOUR_THICKNESS = 2
BOUNDING_BOX_THICKNESS = 2

# Image Size Constraints
MAX_IMAGE_WIDTH = 2048
MAX_IMAGE_HEIGHT = 2048

# Output Directories
OUTPUT_DIR = 'data/results'
LOG_DIR = 'logs'
SAMPLE_IMAGES_DIR = 'data/sample_images'

# Database
LOG_FILE = 'logs/analysis_logs.csv'
PATIENT_RECORD_COLUMNS = [
    'timestamp', 'patient_id', 'lesion_id', 'image_path',
    'area_pixels', 'area_mm2', 'perimeter_pixels', 'perimeter_mm',
    'circularity_index', 'asymmetry_score', 'edge_definition',
    'color_dominance', 'size_category', 'recommendation', 'notes'
]
