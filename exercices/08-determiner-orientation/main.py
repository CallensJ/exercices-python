# main.py
from get_orientation import orientation

dimensions = [
    (1920, 1080),
    (1080, 1350),
    (800, 800),
    (1200, 628),
    (600, 900),
]

for width, height in dimensions:
    image_orientation = orientation(width, height)
    print(f"{width} x {height} => {image_orientation}")
