from fpdf import FPDF
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import subprocess

print("\n🎯 Step 1: Running gaze tracker...")
subprocess.run(["python", "track_gaze_on_stimulus.py"])

print("\n🧭 Step 2: Analyzing AOI durations...")
subprocess.run(["python", "analyze_aoi.py"])

print("\n🌡️ Step 3: Generating heatmap with AOIs...")
subprocess.run(["python", "heatmap_with_aois.py"])

print("\n🎞️ Step 4: Exporting gaze trail video...")
subprocess.run(["python", "gaze_replay_video.py"])

# Step 5: Generate PDF report
print("\n📝 Step 5: Generating PDF report...")

# AOI Timeline Plot
plt.figure(figsize=(12, 2))
aoi_timeline = pd.read_csv("aoi_timeline.csv")
sns.scatterplot(data=aoi_timeline, x="Frame", y="AOI", s=10)
plt.title("AOI Timeline")
plt.tight_layout()
plt.savefig("aoi_timeline_plot.png")
plt.close()

# Generate PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(0, 10, "Gaze Tracking Summary Report", ln=True)

pdf.set_font("Arial", "", 12)
pdf.ln(10)
pdf.cell(0, 10, "AOI Duration (seconds):", ln=True)
aoi_report = pd.read_csv("aoi_report.csv")
for _, row in aoi_report.iterrows():
    pdf.cell(0, 10, f"  {row['AOI']}: {row['TimeSpent(s)']} sec", ln=True)

pdf.ln(10)
pdf.cell(0, 10, "Heatmap with AOIs:", ln=True)
pdf.image("gaze_heatmap_with_aois.png", w=180)

pdf.ln(10)
pdf.cell(0, 10, "AOI Timeline Chart:", ln=True)
pdf.image("aoi_timeline_plot.png", w=180)

pdf.output("gaze_tracking_report.pdf")
print("✅ Pipeline complete! All results and report saved.")