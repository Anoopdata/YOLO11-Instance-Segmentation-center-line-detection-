from moviepy.editor import VideoFileClip
import math

# === Input video file ===
input_video = "/media/5b4fb098-6ac9-4474-b3af-d4e564ebd5ad1/pcap_and_json/Pratyush_sir_ssd/SVDGS_COMMISSIONING_MAA/Bay_26/6E1114_07-06-2025.mp4"
# === Duration of each split in seconds (5 minutes = 300 seconds) ===
chunk_duration = 1 * 60

# === Load the video ===
clip = VideoFileClip(input_video)

# === Get total duration of video ===
total_duration = clip.duration  # in seconds
print(f"Total video length: {total_duration/60:.2f} minutes")

# === Calculate number of parts ===
num_parts = math.ceil(total_duration / chunk_duration)
print(f"Splitting into {num_parts} parts of 5 minutes each")

# === Split and save clips ===
for i in range(num_parts):
    start_time = i * chunk_duration
    end_time = min((i + 1) * chunk_duration, total_duration)
    
    subclip = clip.subclip(start_time, end_time)
    output_filename = f"output_part_{i+1:02d}.mp4"
    
    print(f"Saving {output_filename} ({start_time:.2f}s - {end_time:.2f}s)")
    subclip.write_videofile(output_filename, codec="libx264", audio_codec="aac")
    
    subclip.close()

clip.close()
print("✅ All clips have been created successfully!")


import cv2
import os
import uuid

video_path = "/home//Downloads/Flight-CameraData.v17-batch8-gray.yolov11/f1"
output_dir = "/home//Downloads/Flight-CameraData.v17-batch8-gray.yolov11/f10"

os.makedirs(output_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)
frame_id = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_uuid = uuid.uuid4().hex  # unique ID per frame
    filename = f"{frame_id:05d}_{frame_uuid}.jpg"

    cv2.imwrite(os.path.join(output_dir, filename), frame)
    frame_id += 1

cap.release()
print("Done! Frames saved with UUIDs.")

