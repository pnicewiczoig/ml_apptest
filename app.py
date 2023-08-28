import easyocr as ocr  #OCR
import streamlit as st  #Web App
from PIL import Image #Image Processing
import numpy as np #Image Processing 

import re

#title
st.title("OCR - ML Example")

#subtitle
st.markdown("## Optical Character Recognition")

#image uploader
image = st.file_uploader(label = "Upload your image here",type=['png','jpg','jpeg'])


@st.cache
def load_model(): 
    reader = ocr.Reader(['en'],model_storage_directory='.')
    return reader 

reader = load_model() #load model

if image is not None:

    input_image = Image.open(image) #read image
    st.image(input_image) #display image

    with st.spinner("Please wait ... processing"):
        

        result = reader.readtext(np.array(input_image))

        result_text = [] #empty list for results


        for text in result:
            # only output if numbers and spaces
            if re.match("^[0-9 ]+$", text[1]):
                result_text.append(text[1])

        st.write(result_text)
    st.balloons()
else:
    st.write("Upload an Image")
