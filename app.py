import streamlit as st
from pathlib import Path
import google.generativeai as genai
from dotenv import load_dotenv
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

# Access the API key
google_api_key = os.getenv("GOOGLE_API_KEY")
if not google_api_key:
    st.error("GOOGLE_API_KEY not found. Please check your .env file.")
    logging.error("GOOGLE_API_KEY not found. Ensure the .env file is properly configured.")
    st.stop() 

# Configure the Generative AI client
try:
    genai.configure(api_key=google_api_key)
except Exception as e:
    st.error("Failed to configure Generative AI client.")
    logging.error(f"Error configuring Generative AI client: {e}")
    st.stop()


GENERATION_CONFIG = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
}

SAFETY_SETTINGS = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

SYSTEM_PROMPT = ["""
    You are a domain expert in medical image analysis. You are tasked with examining medical images for a renowned hospital.
    Your expertise will help in identifying or discovering any anomalies, diseases, conditions or any health issues that might be present in the image.
    
    Your key responsibilites:
    1. Detailed Analysis : Scrutinize and thoroughly examine each image, focusing on finding any abnormalities.
    2. Analysis Report : Document all the findings and clearly articulate them in a structured format.
    3. Recommendations : Basis the analysis, suggest remedies, tests or treatments as applicable.
    4. Treatments : If applicable, lay out detailed treatments which can help in faster recovery.
    
    Important Notes to remember:
    1. Scope of response : Only respond if the image pertains to human health issues.
    2. Clarity of image : In case the image is unclear, note that certain aspects are 
    'Unable to be correctly determined based on the uploaded image'
    3. Disclaimer : Accompany your analysis with the disclaimer: 
    "Consult with a Doctor before making any decisions."
    4. Your insights are invaluable in guiding clinical decisions. 
    Please proceed with the analysis, adhering to the structured approach outlined above.
    
    Please provide the final response with these 4 headings : 
    Detailed Analysis, Analysis Report, Recommendations and Treatments
    
"""
]


try:
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro-latest",
        generation_config=GENERATION_CONFIG,
        safety_settings=SAFETY_SETTINGS,
    )
except Exception as e:
    st.error("Failed to initialize the Generative AI model.")
    logging.error(f"Error initializing the model: {e}")
    st.stop()

# Streamlit app configuration
st.set_page_config(page_title="Visual Medical Assistant", page_icon="🩺", layout="wide")
st.title("Visual Medical Assistant 👨‍⚕️ 🩺 🏥")
st.subheader("An app to assist with medical image analysis and report generation")

file_uploaded = st.file_uploader("Upload an image for analysis", type=["png", "jpg", "jpeg"])

if file_uploaded:
    st.image(file_uploaded, width=200, caption="Uploaded Image")

# Generate analysis button
if st.button("Generate Analysis"):
    if not file_uploaded:
        st.error("Please upload an image before generating analysis.")
    else:
        try:
            image_data = file_uploaded.getvalue()
            image_parts = [{"mime_type": "image/jpg", "data": image_data}]
            
            prompt_parts = [image_parts[0], SYSTEM_PROMPT[0]] 

            # Generate response
            response = model.generate_content(prompt_parts)
            if response and response.text:
                st.title("Detailed Analysis Based on the Uploaded Image")
                st.write(response.text)
            else:
                st.error("No response received. Please try again.")
                logging.warning("No response received from the Generative AI model.")
        except Exception as e:
            st.error("An error occurred while processing the image.")
            logging.error(f"Error during analysis: {e}")
