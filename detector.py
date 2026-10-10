import cv2
from ultralytics import YOLO

class ObjectDetector:
    def __init__(self, model_path="yolo11n.pt", camera_index=0):
        self.model = YOLO(model_path)
        self.cap = cv2.VideoCapture(camera_index)

        if not self.cap.isOpened():
            raise RuntimeError(
                "Could not open webcam. Check macOS Camera permissions for Terminal/VS Code."
            )

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    def process_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            raise RuntimeError("Could not read a frame from the webcam.")

        results = self.model(frame, verbose=False)
        detections = []

        for result in results:
            for box in result.boxes:
                confidence = float(box.conf[0])
                class_id = int(box.cls[0])
                name = self.model.names[class_id]

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                label = f"{name} {confidence:.2f}"
                cv2.putText(
                    frame, label, (x1, max(y1 - 10, 20)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2
                )

                detections.append({
                    "name": name,
                    "confidence": confidence
                })

        return frame, detections

    def show(self, frame):
        cv2.imshow("Real-Time Object Detection", frame)

    def should_quit(self):
        return (cv2.waitKey(1) & 0xFF) == ord("q")

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()
