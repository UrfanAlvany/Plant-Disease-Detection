from ultralytics import YOLO

model = YOLO('.\\runs\\classify\\plants_yolov8x\\weights\\best.pt')

#HEALTHY:
results = model('.\\Archive\\plants\\test\\healthy')