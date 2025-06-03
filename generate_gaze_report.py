import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from fpdf import FPDF
import cv2
import os

# Check required files
assert os.path.exists("aoi_report.csv"), "Missing: aoi_report.csv"
assert os.path.exists("aoi_timeline.csv"), "Missing: aoi_timeline.csv"
assert os.path.exists("gaze_heatmap_with_aois.png"), "Missing: gaze_heatmap_with_aois.png"

# Load data
aoi_report = pd.read_csv("aoi_report.csv")
aoi_timeline = pd.read_csv("aoi_timeline.csv")

# Generate AOI timeline plot
plt.figure(figsize=(12, 2))
sns.scatterplot(data=aoi_timeline, x="Frame", y="AOI", s=10)
plt.title("AOI Timeline")
plt.tight_layout()
timeline_img = "aoi_timeline_plot.png"
plt.savefig(timeline_img)
plt.close()

# PDF report
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(0, 10, "Gaze Tracking Summary Report", ln=True)

pdf.set_font("Arial", "", 12)
pdf.ln(10)
pdf.cell(0, 10, "AOI Duration (seconds):", ln=True)
for _, row in aoi_report.iterrows():
    pdf.cell(0, 10, f"  {row['AOI']}: {row['TimeSpent(s)']} sec", ln=True)

pdf.ln(10)
pdf.cell(0, 10, "Heatmap with AOIs:", ln=True)
pdf.image("gaze_heatmap_with_aois.png", w=180)

pdf.ln(10)
pdf.cell(0, 10, "AOI Timeline Chart:", ln=True)
pdf.image(timeline_img, w=180)

# Save report
pdf_path = "gaze_tracking_report.pdf"
pdf.output(pdf_path)
print(f"✅ PDF report saved as {pdf_path}")
