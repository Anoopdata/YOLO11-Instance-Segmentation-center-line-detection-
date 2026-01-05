from ultralytics import YOLO
import cv2
import os

# Load YOLO model
model = YOLO("/home/Downloads/Flight-CameraData.v17-batch8-gray.yolov11/runs/segment/train2/weights/best.pt")

# Video path
video_path = "/media/5b4fb098-6ac9-4474-b3af-d4e564ebd5ad1/video_vdgs/HD_surveillance_2025-01-11_10-28-49_Inxee.mp4"
cap = cv2.VideoCapture(video_path)

# Check if video opened successfully
if not cap.isOpened():
    print(f"Failed to open video: {video_path}")
    exit()

# Create output dirs
os.makedirs("cropped_frames", exist_ok=True)
os.makedirs("labels", exist_ok=True)
os.makedirs("frames", exist_ok=True)

target_class_id = 4   # A320
confidence_threshold = 0.50
frame_count = 0

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run inference
    results = model(frame)

    boxes = results[0].boxes.xyxy.cpu().numpy()
    class_ids = results[0].boxes.cls.cpu().numpy()
    confidences = results[0].boxes.conf.cpu().numpy()

    annotation_lines = []

    for i, (cls_id, conf) in enumerate(zip(class_ids, confidences)):
        if cls_id == target_class_id and conf >= confidence_threshold:
            x1, y1, x2, y2 = boxes[i].astype(int)

            # Save cropped image
            cropped_img = frame[y1:y2, x1:x2]
            crop_filename = f"cropped_frames/frame_{frame_count}_a320_{i}.jpg"
            cv2.imwrite(crop_filename, cropped_img)
            print(f"Saved crop: {crop_filename}")

            # Convert to YOLO format (normalized center x, center y, width, height)
            x_center = ((x1 + x2) / 2) / frame_width
            y_center = ((y1 + y2) / 2) / frame_height
            width = (x2 - x1) / frame_width
            height = (y2 - y1) / frame_height

            annotation_line = f"{int(cls_id)} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}"
            annotation_lines.append(annotation_line)

    # Save frame if any object was detected
    if annotation_lines:
        img_filename = f"frames/frame_{frame_count:05}.jpg"
        label_filename = f"labels/frame_{frame_count:05}.txt"

        cv2.imwrite(img_filename, frame)

        with open(label_filename, "w") as f:
            f.write("\n".join(annotation_lines))
        print(f"Saved label: {label_filename}")

    # Optional: Show annotated frame
    annotated_frame = results[0].plot()
    cv2.imshow("Detections", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
         break

    frame_count += 1

cap.release()
cv2.destroyAllWindows()

