from ultralytics import YOLO
from multiprocessing import freeze_support

if __name__ == '__main__':
    model = YOLO('.\\runs\\classify\\plants_yolov8x\\weights\\best.pt')
    metrics = model.val()
    print(metrics.top1)
    freeze_support()
