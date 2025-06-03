import cv2
import pandas as pd
import os

print("📽️ Starting gaze replay video generation...")

# Load gaze data
df = pd.read_csv("gaze_data.csv")

# Load frames
if os.path.exists("stimulus_input.mp4"):
    cap = cv2.VideoCapture("stimulus_input.mp4")
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.resize(frame, (1280, 720))
        frames.append(frame)
    cap.release()
    print(f"✅ Loaded {len(frames)} frames from video")
else:
    img = cv2.imread("stimulus_input.jpg")
    frame = cv2.resize(img, (1280, 720))
    frames = [frame for _ in range(len(df))]
    print(f"✅ Loaded single image for {len(frames)} gaze entries")

# Trim or pad gaze data to match frames
min_len = min(len(df), len(frames))
df = df.iloc[:min_len]
frames = frames[:min_len]

# Create output video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("gaze_video.mp4", fourcc, 30.0, (1280, 720))

trail = []
for i, row in df.iterrows():
    x, y = int(row["x"]), int(row["y"])
    trail.append((x, y))
    frame = frames[i].copy()

    for t in trail[-30:]:
        cv2.circle(frame, t, 5, (0, 0, 255), -1)

    out.write(frame)

out.release()
cv2.destroyAllWindows()

# Verify video output
if os.path.exists("gaze_video.mp4") and os.path.getsize("gaze_video.mp4") > 1000:
    print("✅ Gaze replay video generated successfully and is non-empty.")
else:
    print("❌ Gaze replay video not created or is empty.")
