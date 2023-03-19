from ultralytics import YOLO
from multiprocessing import freeze_support


if __name__ == '__main__':
    model = YOLO('yolov8n-cls.pt')
    model.train(data='.\\Archive\\plants', epochs=100, imgsz=256, save_period=5, device=0, name="plants_yolov8n", verbose=True)
    freeze_support()




