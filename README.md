# Real-Time Object Detection with YOLOv8

A lightweight computer vision script that performs object detection on video files using **YOLOv8 (Ultralytics)** and **OpenCV**. The script processes a video frame-by-frame, detects specific object classes, draws bounding boxes, and saves the annotated result as a new video file.

##  Features

- Pre-trained **YOLOv8n** (nano) model for fast inference
- Detects and annotates three object classes:
  - `0` — Person
  - `2` — Car
  - `67` — Cell phone
- Automatically preserves the original video's resolution and frame rate
- Draws bounding boxes with class labels and confidence scores on every frame
- Exports a fully processed `.mp4` video with annotations

##  Project Structure

```
.
├── app.py                  # Main detection script
├── sample_input.mp4        # Input video (1280x320, ~22.4s)
└── output_processed.mp4    # Output video with bounding boxes drawn
```

##  Requirements

- Python 3.8+
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- OpenCV

Install dependencies:

```bash
pip install ultralytics opencv-python
```

> Note: On first run, `yolov8n.pt` weights will be automatically downloaded by the Ultralytics library if not already present locally.

##  Usage

1. Place your input video in the project directory and name it `sample_input.mp4` (or update `input_path` in `app.py`).
2. Run the script:

```bash
python app.py
```

3. The annotated video will be saved as `output_processed.mp4` in the same directory.

## ⚙️ How It Works

1. **Load Model** — Loads the pre-trained `yolov8n.pt` weights.
2. **Read Video** — Opens the input video and reads its properties (width, height, FPS).
3. **Initialize Writer** — Sets up an `mp4v`-encoded `VideoWriter` matching the input dimensions.
4. **Frame-by-Frame Inference** — For each frame, YOLOv8 runs inference restricted to the target classes (`person`, `car`, `cell phone`).
5. **Annotate** — Bounding boxes and labels are drawn using `results[0].plot()`.
6. **Write Output** — Each annotated frame is written to the output video file.
7. **Cleanup** — Releases video capture and writer resources once processing is complete.

##  Sample Video Info

| Property | Input | Output |
|---|---|---|
| Resolution | 1280x320 | 1280x320 |
| Frame Count | 149 | 149 |
| Approx. Duration | ~22.4s | ~24.8s |

## 🔧 Customization

- **Change detected classes**: Modify the `classes=[0, 2, 67]` argument in the `model()` call. Refer to the [COCO class list](https://docs.ultralytics.com/datasets/detect/coco/) for all available class IDs.
- **Use a larger model**: Swap `yolov8n.pt` for `yolov8s.pt`, `yolov8m.pt`, `yolov8l.pt`, or `yolov8x.pt` for higher accuracy at the cost of speed.
- **Adjust confidence threshold**: Add `conf=0.5` (or your preferred value) to the `model()` call to filter low-confidence detections.

##  Notes

- This script is CPU/GPU agnostic — Ultralytics will automatically use a GPU if available (CUDA).
- Processing time scales with video length and model size.

##  License

This project uses the [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) library, which is licensed under AGPL-3.0. Review their license terms before commercial use.
