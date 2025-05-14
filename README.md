# License-Plate-Detection-using-Yolov8
🚘 License Plate Detection using YOLOv8
This project implements a real-time License Plate Detection system using the YOLOv8 object detection algorithm. The model is trained on a custom annotated dataset of vehicles and their license plates, enabling it to identify license plates from images and video streams with high accuracy.

📌 Features
Real-time license plate detection

Trained on custom annotated dataset

Based on YOLOv8 – state-of-the-art object detection

High accuracy and fast inference

Easy to extend for license plate recognition (OCR)

📁 Dataset
The dataset consists of images of vehicles with annotated bounding boxes around license plates.

Annotations are in YOLO format (.txt files with class and bounding box coordinates).

Tools like LabelImg or Roboflow were used for annotation.

Dataset is split into train, val, and test folders.

🧠 Model
Model: YOLOv8 (from Ultralytics)

Framework: PyTorch

Training: Fine-tuned YOLOv8 on custom dataset using ultralytics Python package.

🛠️ Setup
1. Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/license-plate-detection-yolov8.git
cd license-plate-detection-yolov8
2. Install Requirements
bash
Copy code
pip install -r requirements.txt
Requirements include:

ultralytics

opencv-python

matplotlib

torch

3. Dataset Setup
Place your dataset folder in the root directory, structured like this:

bash
Copy code
dataset/
├── images/
│   ├── train/
│   ├── val/
│   └── test/
├── labels/
│   ├── train/
│   ├── val/
│   └── test/
Update the data.yaml file with your paths and class names.

🚀 Training
bash
Copy code
yolo task=detect mode=train model=yolov8n.pt data=data.yaml epochs=50 imgsz=640
You can change yolov8n.pt to other variants like yolov8s.pt, yolov8m.pt, etc., based on accuracy/speed requirements.

📊 Evaluation
bash
Copy code
yolo task=detect mode=val model=runs/detect/train/weights/best.pt data=data.yaml
The model will output mAP, precision, and recall values for validation data.

📷 Inference
On an Image
bash
Copy code
yolo task=detect mode=predict model=best.pt source="test.jpg"
On a Video or Webcam
bash
Copy code
yolo task=detect mode=predict model=best.pt source=0  # for webcam
Results will be saved in the runs/detect/predict directory.

📈 Results
Include sample images with bounding boxes from your predictions here.

<p align="center"> <img src="sample_results/example1.jpg" width="400" /> <img src="sample_results/example2.jpg" width="400" /> </p>
🔮 Future Work
Integrate OCR (Optical Character Recognition) to extract plate numbers.

Improve performance on night-time images.

Deploy using Flask or Streamlit for a web-based interface.

📄 License
This project is licensed under the MIT License.

🙌 Acknowledgements
Ultralytics YOLOv8

Roboflow for dataset preprocessing

LabelImg for annotation

