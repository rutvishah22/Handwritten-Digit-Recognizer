# 🧠 Handwritten Digit Recognizer

This is a simple web app built with **Streamlit** that recognizes handwritten digits (0–9) using a trained **TensorFlow MNIST model**.  
You can either **upload an image** or **draw a digit** right on the screen — and the model will instantly predict what number it is!

---

### 🚀 How It Works
1. The model was trained on the **MNIST dataset** in Kaggle.  
2. Once trained, the model was saved as a `.keras` file and used here for prediction.  
3. The app uses **Streamlit** for the UI and **streamlit-drawable-canvas** for the drawing area.  

---

### 🖥️ Features
- ✍️ Draw digits directly on the canvas  
- 🖼️ Upload your own digit image (PNG/JPG)  
- ⚡ Real-time prediction  
- 🌐 Easy to deploy on Streamlit Cloud or Hugging Face  

---

### 🧩 Tech Stack
- Python  
- TensorFlow / Keras  
- Streamlit  
- Pillow  
- NumPy  

---

### ⚙️ How to Run Locally
```bash
git clone https://github.com/your-username/digit-recognizer.git
cd digit-recognizer
python -m venv venv
source venv/bin/activate     # (use 'venv\Scripts\activate' on Windows)
pip install -r requirements.txt
streamlit run app.py
