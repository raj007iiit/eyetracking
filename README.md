
# 🎯 Eye Tracker Gaze Dashboard

This project provides a complete **web-based dashboard for webcam-based eye tracking** using only a standard camera — no additional hardware required. Built with **Streamlit**, the dashboard allows users to upload a stimulus (image or video), record gaze data in real time, and generate insightful reports including:

- 👁️ Gaze Heatmaps
- 📍 Area of Interest (AOI) Analysis
- 🎞️ Gaze Replay Video
- 📄 PDF Summary Reports

---

## 🔧 Features

- ✅ **Real-time webcam tracking** using MediaPipe Face Mesh
- 🧠 **Gaze prediction model** via quick on-screen calibration
- 📊 **AOI duration analysis** (how long users look at specific areas)
- 🌡️ **Gaze heatmap visualization**
- 🖼️ Works with both `.jpg` images and `.mp4` videos
- 💾 Export results as CSV, PNG, MP4, and PDF
- 🌐 **Interactive Streamlit dashboard** with sidebar controls

---

## 🚀 Getting Started

### 1. Clone the repo and install dependencies
```bash
git clone https://github.com/your-username/eye-tracker-dashboard.git
cd eye-tracker-dashboard
pip install -r requirements.txt
```

### 2. Run the Streamlit app
```bash
streamlit run gaze_tracker_dashboard.py
```

### 3. Calibrate (for first-time use)
Click **"📍 Calibrate My Gaze"** in the sidebar and follow the on-screen dots to build your gaze model.

---

## 📂 Outputs

After running the pipeline, the following outputs are generated:

- `gaze_data.csv` – Raw gaze points (x, y)
- `gaze_video.mp4` – Replay video showing gaze movement
- `gaze_heatmap_with_aois.png` – Heatmap + AOIs
- `aoi_report.csv` – Time spent in each AOI
- `aoi_timeline.csv` – Frame-wise AOI transitions
- `gaze_tracking_report.pdf` – Full summary PDF
- `gaze_tracking_outputs.zip` – Zipped output for download

---

## 🧪 Calibration

To predict gaze locations from eye landmarks, the app includes a quick calibration phase using a trained `gaze_model.pkl`. Users click **"Calibrate My Gaze"** to run this step.

---

## 🛠️ Built With

- [Streamlit](https://streamlit.io/)
- [OpenCV](https://opencv.org/)
- [MediaPipe Face Mesh](https://google.github.io/mediapipe/)
- [Seaborn + Matplotlib](https://seaborn.pydata.org/)
- [FPDF](https://py-pdf.github.io/fpdf2/)

---

## 📜 License

This project is open-source under the MIT License.
