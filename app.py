import streamlit as st

st.set_page_config(
    page_title="Trend Pulse",
    page_icon="😎",
)

st.markdown(
    """# 📈 **Trend Pulse**
### **Predicting Stocks with ML**

**Stockastic is an ML-powered stock price prediction app built with Python and Streamlit. It utilizes machine learning models to forecast stock prices and help investors make data-driven decisions.**

## 🏗️ **How It's Built**

Trend Pulse is built with these core frameworks and modules:

- **Streamlit** - To create the web app UI and interactivity 
- **LSTM** - To build the Long Short Term Memory model
- **Plotly** - To create interactive financial charts
- **Keras** - To Train the Model layer by layer.
- **Tensorflow** - To Primarily Build & Train LSTM Neural Network model.

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
