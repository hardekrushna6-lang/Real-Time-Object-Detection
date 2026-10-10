import cv2

def draw_info(frame, detections):
    count = len(detections)

    cv2.rectangle(frame, (10, 10), (330, 55), (0, 0, 0), -1)
    cv2.putText(
        frame,
        f"Objects detected: {count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        "Press Q to quit",
        (20, 85),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )

    return frame
