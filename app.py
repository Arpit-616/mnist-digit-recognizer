import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image, ImageOps

# Load trained model
model = tf.keras.models.load_model("mnist_model.h5")

st.title("🖊️ MNIST Handwritten Digit Recognizer")
st.write("Draw or upload a digit (0-9) and the model will predict it.")

# File uploader
uploaded_file = st.file_uploader("Upload an image of a digit", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Show uploaded image
    image = Image.open(uploaded_file).convert("L")  # grayscale
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Preprocess
    img = ImageOps.invert(image)       # MNIST digits are white on black
    img = img.resize((28, 28))         # resize to 28x28
    arr = np.array(img).astype("float32") / 255.0
    arr = arr.reshape(1, 28, 28, 1)

    # Predict
    preds = model.predict(arr)[0]
    pred_label = np.argmax(preds)

    st.subheader(f"Prediction: {pred_label}")
    st.bar_chart(preds)

# Option: Draw inside the app (using Streamlit-drawable-canvas)
try:
    from streamlit_drawable_canvas import st_canvas

    st.subheader("Or draw a digit below 👇")

    canvas_result = st_canvas(
        fill_color="white",
        stroke_width=10,
        stroke_color="black",
        background_color="white",
        width=200,
        height=200,
        drawing_mode="freedraw",
        key="canvas"
    )

    # Add proper error handling for canvas data
    if canvas_result is not None and hasattr(canvas_result, 'image_data') and canvas_result.image_data is not None:
        try:
            img = Image.fromarray((255 - canvas_result.image_data[:, :, 0]).astype(np.uint8))  # invert
            img = img.resize((28, 28))
            arr = np.array(img).astype("float32") / 255.0
            arr = arr.reshape(1, 28, 28, 1)

            preds = model.predict(arr)[0]
            pred_label = np.argmax(preds)

            st.subheader(f"Prediction from Canvas: {pred_label}")
            st.bar_chart(preds)
        except Exception as e:
            st.error(f"Error processing canvas data: {e}")
            st.info("Try drawing a clearer digit or use the upload option instead.")
except ImportError:
    st.warning("The streamlit_drawable_canvas package is not installed. Please install it with: pip install streamlit-drawable-canvas")

