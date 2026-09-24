from PIL import Image
from pathlib import Path
from image_metadata import get_image_metadata

image_path = Path('sample_images/img1.jpeg')  # Remplacez par le chemin de votre dossier d'images
print(get_image_metadata(image_path))
