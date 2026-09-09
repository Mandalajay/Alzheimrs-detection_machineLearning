# 🧠 Advancing Alzheimer's Disease Diagnosis

An AI-driven project focused on **enhancing predictive accuracy** for Alzheimer's disease diagnosis using a Convolutional Neural Network (CNN) built in TensorFlow/Keras. 

This repository showcases the implementation, testing, and evaluation of deep learning models trained to identify patterns in multimodal medical sensors and imaging data.

---

## 🚀 Project Overview
Alzheimer's disease is a progressive neurologic disorder that causes the brain to shrink and brain cells to die. Early and accurate detection is critical for patient care and intervention. This project utilizes custom **Convolutional Neural Networks (CNNs)** to analyze complex data patterns, aiming to provide an explainable, highly accurate framework for medical diagnostics.

---

## 📂 Repository Structure

```text
├── .gitattributes                  # Configurations for Git Large File Storage (LFS)
├── Alzheimers R1.ipynb             # Core notebook containing data processing and model architecture
├── alzheimer_model_testing.ipynb   # Notebook dedicated to testing predictions and visual evaluations
├── Untitled.ipynb                  # Experimental notebook / scratchpad
└── alzheimers_cnn_model.h5         # Pre-trained CNN weights (Managed securely via Git LFS, 254MB)
```

---

## 🛠️ Requirements & Installation

To run the notebooks locally, make sure you have Python installed along with the required libraries. 

### 1. Clone the repository
```bash
git clone https://github.com/Mandalajay/Alzheimrs-detection_machineLearning.git
cd Alzheimrs-detection_machineLearning
```

### 2. Install Git LFS (Required to pull the model)
Because the pre-trained model file is **254 MB**, you must initialize Git LFS before cloning or pulling to get the actual model data:
```bash
git lfs install
git lfs pull
```

### 3. Install Python Dependencies
```bash
pip install tensorflow notebook numpy matplotlib pandas scikit-learn
```

---

## 💻 How to Use

### Loading the Pre-trained Model
You can load the complete model into your environment directly with TensorFlow using the following snippet:

```python
import tensorflow as tf

# Load the H5 binary model file
model_path = "alzheimers_cnn_model.h5"
model = tf.keras.models.load_model(model_path)

# Verify model architecture and parameters
model.summary()
```

### Testing Predictions
Open the `alzheimer_model_testing.ipynb` notebook in Jupyter Lab or Jupyter Notebook to run test images/data through the network and visualize the predictive outputs.

---

## 📊 Model & Features
* **Architecture**: Deep Convolutional Neural Network (CNN) optimized for complex feature extraction.
* **Large File Optimization**: Employs **Git Large File Storage (LFS)** to seamlessly host binary model components on GitHub without cluttering text logs.

---

## 👤 Author
* **Mandalajay** - *Initial Work & Deep Learning Development* - [GitHub Profile](https://github.com/Mandalajay)

---

## 📜 License
This project is open-source. Please check back later for specific license details.
