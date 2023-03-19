from ultralytics import YOLO

model = YOLO('.\\runs\\classify\\plants_yolov8x\\weights\\best.pt')

results = model('.\\Archive\\plants\\test\\sick\\ffe98ff9-be33-4e8f-82f0-7b7c21b02958___JR_Sept.L.S 8455.JPG')
print("Sick example: ")
for result in results:
    print(result.boxes)
    print(result.probs)

results = model('.\\Archive\\plants\\test\\healthy\\ff774aec-2504-4d11-8a61-2fd74c689a6f___RS_HL 9904.JPG')

print("Healthy example: ")
for result in results:
    print(result.boxes)
    print(result.probs)