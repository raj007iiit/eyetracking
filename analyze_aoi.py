import pandas as pd
from collections import defaultdict

# Load gaze data
df = pd.read_csv("gaze_data.csv")

# Define AOIs manually
AOIS = {
    "TopLeft": (100, 100, 400, 300),
    "Center": (500, 300, 800, 500),
    "BottomRight": (900, 500, 1200, 700)
}

# Frame-accurate logs
aoi_log = []
aoi_durations = defaultdict(float)
sample_interval = 1 / 30.0

for i, row in df.iterrows():
    x, y = row["x"], row["y"]
    matched = False
    for name, (x1, y1, x2, y2) in AOIS.items():
        if x1 <= x <= x2 and y1 <= y <= y2:
            aoi_durations[name] += sample_interval
            aoi_log.append((i, name))
            matched = True
            break
    if not matched:
        aoi_log.append((i, "None"))

# Write duration report
with open("aoi_report.csv", "w") as f:
    f.write("AOI,TimeSpent(s)\n")
    for name, dur in aoi_durations.items():
        print(f"  {name:12s}: {dur:.2f} sec")
        f.write(f"{name},{dur:.2f}\n")

# Write frame-wise AOI transitions
with open("aoi_timeline.csv", "w") as f:
    f.write("Frame,AOI\n")
    for frame, aoi in aoi_log:
        f.write(f"{frame},{aoi}\n")