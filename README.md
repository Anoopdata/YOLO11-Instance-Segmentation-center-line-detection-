# YOLO11-Instance-Segmentation-center-line-detection-

# YOLO11 Instance Segmentation

## 📌 Overview

Instance segmentation goes a step beyond object detection by not only locating objects with bounding boxes, but also **segmenting each individual object at the pixel level**.

With **Ultralytics YOLO11 Segment models**, you get:

* Object **class labels**
* **Confidence scores**
* **Precise object masks/contours** for each instance

This is especially useful for:

* Autonomous driving & lane/center-line detection
* Medical imaging
* Robotics & perception systems
* Industrial inspection
* Scene understanding

---

## 🧠 What is Instance Segmentation?

| Task                      | Output                                              |
| ------------------------- | --------------------------------------------------- |
| Object Detection          | Bounding boxes + labels                             |
| Semantic Segmentation     | Pixel-wise class labels (no instance separation)    |
| **Instance Segmentation** | Bounding boxes + **separate masks for each object** |

YOLO11 instance segmentation models return **individual masks for each detected object**, even if they belong to the same class.

---

## 🚀 YOLO11 Segmentation Models

YOLO11 segmentation models use the `-seg` suffix and are pretrained on the **COCO dataset**.

| Model       | Image Size | mAP(box) | mAP(mask) | Params (M) | FLOPs (B) |
| ----------- | ---------- | -------- | --------- | ---------- | --------- |
| YOLO11n-seg | 640        | 38.9     | 32.0      | 2.9        | 9.7       |
| YOLO11s-seg | 640        | 46.6     | 37.8      | 10.1       | 33.0      |
| YOLO11m-seg | 640        | 51.5     | 41.5      | 22.4       | 113.2     |
| YOLO11l-seg | 640        | 53.4     | 42.9      | 27.6       | 132.2     |
| YOLO11x-seg | 640        | 54.7     | 43.8      | 62.1       | 296.4     |

> Models are downloaded automatically on first use.

---

## 📦 Installation

```bash
pip install ultralytics
```

Check installation:

```bash
yolo checks
```

---

## 🏋️ Training

Train a YOLO11 segmentation model on a custom dataset.

### Using pretrained weights (recommended)

```bash
yolo segment train \
  data=path/to/dataset.yaml \
  model=yolo11n-seg.pt \
  epochs=100 \
  imgsz=640
```

### Train from scratch

```bash
yolo segment train \
  data=path/to/dataset.yaml \
  model=yolo11n-seg.yaml \
  epochs=100 \
  imgsz=640
```

---

## 📊 Validation

Validate a trained or pretrained segmentation model:

```bash
yolo segment val model=yolo11n-seg.pt
```

For a custom model:

```bash
yolo segment val model=path/to/best.pt
```

Outputs include:

* mAP@0.5:0.95 (box & mask)
* Precision & Recall

---

## 🔍 Prediction

### Image prediction

```bash
yolo segment predict \
  model=yolo11n-seg.pt \
  source=https://ultralytics.com/images/bus.jpg
```

### Video prediction

```bash
yolo segment predict \
  model=path/to/best.pt \
  source=video.mp4
```

### Webcam

```bash
yolo segment predict model=path/to/best.pt source=0
```

📂 Results saved to:

```text
runs/segment/predict/
```

---

## 📁 Dataset Format

YOLO segmentation datasets require **polygon annotations**.

Use:

* **LabelMe**
* **Roboflow**
* **CVAT**

Convert COCO → YOLO using:

```bash
json2yolo
```

See Ultralytics Dataset Guide for details.

---

## 📤 Export Models

Export trained models to deployment-friendly formats.

### ONNX

```bash
yolo export model=path/to/best.pt format=onnx
```

### TensorRT

```bash
yolo export model=path/to/best.pt format=engine
```

Supported formats include:

* ONNX
* TensorRT
* OpenVINO
* CoreML
* TFLite
* NCNN
* PaddlePaddle
* RKNN

---

## ❓ FAQ

### Detection vs Instance Segmentation?

* **Detection**: Bounding boxes only
* **Instance Segmentation**: Bounding boxes + pixel-level masks

### Why YOLO11?

* Real-time performance
* High accuracy
* Easy training & deployment
* Supports end-to-end pipelines

### Can I extract centerlines or skeletons?

Yes. Post-processing masks with:

* Morphological thinning
* Skeletonization
* Polynomial fitting

Ideal for:

* Airport center-line detection
* Lane detection
* Robotics navigation

---

## 🧩 References

* [https://docs.ultralytics.com](https://docs.ultralytics.com)
* [https://github.com/ultralytics/ultralytics](https://github.com/ultralytics/ultralytics)

---

## 👤 Author

**Anoop Morya**
Computer Vision Engineer | AI & Robotics

---

⭐ If this repo helped you, consider starring it!

related dataset link 
https://drive.google.com/drive/folders/12bzLYhaKnyCDuSFqHrScNDY-ye20VWTD?usp=drive_link
