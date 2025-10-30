import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image, ImageOps
from streamlit_drawable_canvas import st_canvas

model = load_model("digit_recognition_model.h5", compile=False)

st.title("🧠 Handwritten Digit Recognizer")
st.write("Upload an image or draw a digit below 👇")

option = st.radio("Choose input method:", ["🖼️ Upload Image", "✍️ Draw Digit"])

def preprocess_image(img, invert=True):
    img = img.convert("L")
    if invert:
        img = ImageOps.invert(img)
    img = img.resize((28, 28))
    img = np.array(img).astype("float32") / 255.0
    img = img.reshape(1, 28, 28, 1)
    return img

def predict_digit(processed):
    pred = model.predict(processed)
    digit = np.argmax(pred)
    return digit

if option == "🖼️ Upload Image":
    uploaded_file = st.file_uploader("Upload a digit image (PNG/JPG)", type=["png", "jpg", "jpeg"])
    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Image", width=150)
        processed = preprocess_image(img, invert=True)
        digit = predict_digit(processed)
        st.success(f"Predicted Digit: {digit}")

elif option == "✍️ Draw Digit":
    st.write("Draw a digit below (0–9)")
    canvas_result = st_canvas(
        fill_color="#000000",
        stroke_width=12,
        stroke_color="#FFFFFF",
        background_color="#000000",
        height=280,
        width=280,
        drawing_mode="freedraw",
        key="canvas",
    )

    if canvas_result.image_data is not None:
        img = Image.fromarray(np.uint8(canvas_result.image_data[:, :, 0]))
        processed = preprocess_image(img, invert=False)
        if st.button("Predict"):
            digit = predict_digit(processed)
            st.success(f"Predicted Digit: {digit}")
