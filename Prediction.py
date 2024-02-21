
import streamlit as st

st.set_page_config(
    page_title="Trend Pulse",
    page_icon="🏆",
)

background_image_style = """
<style>
/* Adds a background image to the full page */
body:before {
content: '';
position: fixed;
left: 0;
right: 0;
z-index: -1;
display: block;
background-image: url('https://i.pinimg.com/564x/49/a6/1e/49a61e26d5905c8a41291d80c3aa999a.jpg');
background-size: cover;
width: 100%;
height: 100%;
opacity: 0.5; /* Lower the opacity to ensure text readability */
}

/* Additional styling to improve text readability against the background */
.css-18e3th9 {
background-color: rgba(255,255,255,0.8) !important;
border-radius: 10px;
padding: 20px;
}

.stButton>button {
color: white !important;
border: 1px solid #4CAF50 !important;
background-color: #4CAF50 !important;
border-radius: 20px !important;
padding: 10px 24px !important;
margin: 10px 0 !important;
cursor: pointer !important;
}

.stButton>button:hover {
background-color: #45a049 !important;
}
</style>
"""

st.markdown(background_image_style, unsafe_allow_html=True)


st.markdown(
    """# 📈 **Trend Pulse**
### **Predicting Stocks with ML**

**Trend Pulse is an ML-powered stock price prediction app built with Python and Streamlit. It utilizes machine learning models to forecast stock prices and help investors make data-driven decisions.**

## 🏗️ **How It's Built**

Trend Pulse is built with these core frameworks and modules:

- **Streamlit** - To create the web app UI and interactivity 
- **LSTM** - To build the Long Short Term Memory model
- **Plotly** - To create interactive financial charts
- **Keras** - To Train the Model layer by layer.
- **Tensorflow** - To Primarily Build & Train LSTM Neural Network model

The app workflow is:

1. User feeds the CSV file.
2. Historical data is fetched with CSV file.
3. LSTM model is trained on the data 
4. Model makes multi-day price forecasts
5. Results are plotted with Plotly

## 🎯 **Key Features**

- **Financial charts** - Interactive historical and forecast charts
- **LSTM forecasting** - Make statistically robust predictions
- **Backtesting** - Evaluate model performance
- **Responsive design** - Works on all devices

## 🚀 **Getting Started**

### **Local Installation**

1. Clone the repo

```bash
git clone https://github.com/Rhythm-shahane/Trend-Pulse.git
```

2. Install requirements

```bash
pip install -r requirements.txt
```

3. Change directory
```bash
cd app.py
```

4. Run the app

```bash
streamlit run app.py
```

## 📈 **Future Roadmap**

Some potential features for future releases:

- **More advanced forecasting models like Transformer**
- **Quantitative trading strategies**
- **Portfolio optimization and tracking**
- **Additional fundamental data**
- **User account system**
- **Real Time Data Fetching**

## **⚖️ Disclaimer**
**This is not financial advice! Use forecast data to inform your own investment research. No guarantee of trading performance.**
"""
)
