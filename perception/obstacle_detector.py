import cv2
import torch

class ObstacleDetector:
    def __init__(self, model_path="yolov8.pt", device="cuda"):
        self.device = device if torch.cuda.is_available() else "cpu"
        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)
        self.model.to(self.device)
        self.model.eval()

    def detect(self, image):
        """
        Runs YOLOv8 object detection on input image.
        Returns detected bounding boxes and confidence scores.
        """
        results = self.model(image)
        detections = results.xyxy[0]  # x1, y1, x2, y2, conf, class
        obstacles = []
        for *box, conf, cls in detections.cpu().numpy():
            if conf > 0.5:  # Confidence threshold
                obstacles.append({
                    "bbox": box,
                    "confidence": conf,
                    "class": int(cls)
                })
        return obstacles
