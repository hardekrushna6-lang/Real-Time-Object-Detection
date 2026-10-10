from detector import ObjectDetector
from database import Database
from ui import draw_info

def main():
    detector = ObjectDetector()
    db = Database()

    print("Starting Real-Time Object Detection...")
    print("Press Q to quit.")

    try:
        while True:
            frame, detections = detector.process_frame()

            for detection in detections:
                db.log_detection(
                    object_name=detection["name"],
                    confidence=detection["confidence"]
                )

            frame = draw_info(frame, detections)
            detector.show(frame)

            if detector.should_quit():
                break
    finally:
        detector.release()
        db.close()

if __name__ == "__main__":
    main()
