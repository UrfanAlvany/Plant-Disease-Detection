from ultralytics import YOLO

model = YOLO('.\\runs\\classify\\plants_yolov8x\\weights\\best.pt')

# SICK:
results = model('.\\Archive\\plants\\test\\sick')