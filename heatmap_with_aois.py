import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import cv2
import os

# Load gaze data
df = pd.read_csv("gaze_data.csv")

# Load background from image or first frame of video
if os.path.exists("stimulus_input.jpg"):
    bg = cv2.imread("stimulus_input.jpg")
else:
    cap = cv2.VideoCapture("stimulus_input.mp4")
    success, bg = cap.read()
    cap.release()

bg = cv2.resize(bg, (1280, 720))
bg_rgb = cv2.cvtColor(bg, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(12.8, 7.2))
plt.imshow(bg_rgb)

sns.kdeplot(
    x=df["x"], y=df["y"],
    cmap=plt.get_cmap("jet"), fill=True,
    alpha=0.4, bw_adjust=0.2, thresh=0.05
)

AOIS = {
    "TopLeft": (100, 100, 400, 300),
    "Center": (500, 300, 800, 500),
    "BottomRight": (900, 500, 1200, 700)
}
for name, (x1, y1, x2, y2) in AOIS.items():
    plt.gca().add_patch(plt.Rectangle((x1, y1), x2-x1, y2-y1,
                                      edgecolor='lime', facecolor='none', lw=2))
    plt.text(x1, y1 - 10, name, color='lime', fontsize=12)

plt.axis('off')
plt.tight_layout()
plt.savefig("gaze_heatmap_with_aois.png")
plt.show()
