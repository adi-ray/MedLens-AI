# MedLens-AI 👨‍⚕️ 🩺 🏥

## 🚨 Problem Statement
In modern healthcare, the demand for quick, accurate, and accessible medical diagnosis is increasing. Medical professionals often face challenges such as:

- ⏰ **Time constraints** in reviewing medical images.
- 🧠 **Limited expertise** in analyzing specific types of medical images.
- ✅ **The need for a reliable second opinion.**

This project aims to assist healthcare professionals by providing **detailed analysis and recommendations** for medical images, helping them identify potential health issues efficiently and accurately.



## 🎯 Objective
Develop a **Streamlit-based application** called **MedLens-AI** that integrates **Google's Generative AI capabilities** to:

1.  **Analyze uploaded medical images.**
2.  **Generate a structured report** with:
     -  **Detailed insights.**
     -  **Recommendations** for further tests or treatments.
     -  **Potential treatments**, where applicable.



## ⚙️ Project Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/adi-ray/MedLens-AI  
```

### 2️⃣ Create a Virtual Environment
Using Conda:

```bash
conda create -p env python=3.10 -y  
conda activate ./env
```

### 3️⃣ Install Dependencies
Install all required Python packages using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4️⃣ Environment Configuration
Create a `.env` file in the root directory and add your Google API key:

```plaintext
GOOGLE_API_KEY=your_api_key_here
```

### 5️⃣ Run the Application
Launch the Streamlit application:

```bash
streamlit run app.py
```



## 🌟 Features

-  **Medical Image Analysis**: Quickly analyze medical images to identify abnormalities or conditions.
- **Structured Reporting**:
  - 📌 **Insights** into detected abnormalities or conditions.
  - ✅ **Recommendations** for follow-up actions or tests.
  - 💊 **Potential treatments**, when applicable.
-  **User-Friendly Interface**: A clean and intuitive UI built with Streamlit for seamless usage.



## 🛠️ Technologies Used

-  **Python 3.10**
-  **Streamlit**
-  **Google Generative AI**



## ⚠️ Disclaimer
This application is intended for **assistance purposes only** and does not replace professional medical advice. Always consult a certified medical practitioner for final decisions.

---
