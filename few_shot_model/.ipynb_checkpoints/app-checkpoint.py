
import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow import keras

# Load the pre-trained model
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("keras-io/lowlight-enhance-mirnet", compile=False)

model = load_model()

# Define a function for processing images
def enhance_image(uploaded_image):
    # Open and preprocess the image
    low_light_img = Image.open(uploaded_image).convert('RGB')
    low_light_img = low_light_img.resize((256, 256), Image.NEAREST)
    image = keras.preprocessing.image.img_to_array(low_light_img)
    image = image.astype('float32') / 255.0
    image = np.expand_dims(image, axis=0)

    # Model prediction
    output = model.predict(image)

    # Post-process the output
    output_image = output[0] * 255.0
    output_image = output_image.clip(0, 255)
    output_image = np.uint8(output_image)

    # Convert output to an image
    enhanced_image = Image.fromarray(output_image, 'RGB')
    
    return enhanced_image

# Streamlit UI
st.title("Light Enhancement App")
st.write("Upload a low-light PNG image to enhance its quality.")

uploaded_image = st.file_uploader("Choose an image...", type="png")

if uploaded_image is not None:
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
    st.write("Enhancing the image...")

    # Enhance the image
    enhanced_image = enhance_image(uploaded_image)

    st.image(enhanced_image, caption="Enhanced Image", use_column_width=True)
    st.write("Enhancement complete!")
    