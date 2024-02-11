# 📈**TREND PULSE**

This repository implements LSTM is for the purpose of stock prediction​.

### - Team Information:
    - We are the students of Second Year E&CS Department.
    - Group L-13
    - Details have been linked below the image.




![ALT Devansh Shahane](https://i.pinimg.com/474x/c4/08/26/c408266d4330863f5e0803668750dd59.jpg)

Devansh Shahane (Team Lead)
- [Email ID: shahane.rhythm@gmail.com](mailto:shahane.rhythm@gmail.com)
- [Linkedin ID: Devansh Shahane](https://www.linkedin.com/in/devansh-shahane/)

Prathamesh Sharma 
- [Email ID: prathameshsharma27@gmail.com](mailto:prathameshsharma27@gmail.com)
- [Linkedin ID: Prathamesh Sharma](www.linkedin.com/in/prathamesh-sharma/)

Nirbhay Tiwari 
-  [Email ID: nirbhay.tcet26@gmail.com](mailto:prathameshsharma27@gmail.com)
-  [Linkedin ID: Nirbhay Tiwari](https://www.linkedin.com/in/nirbhay-tiwari/)

 
 ## **Motto: " We Together Can Bring A Change "**

# 📈 **Trend Pulse**
### **Predicting Stocks with ML**

**Trend Pulse is an ML-powered stock price prediction app built with Python and Streamlit. It utilizes machine learning models to forecast stock prices and help investors make data-driven decisions.**

# **👓 Quick OverView**


## **We have Deployed Over Model:**

### - **Please check it over here:**
### - **[📈TREND PULSE ](https://trend-pulse.streamlit.app/#tesla-stock-price-prediction)**

### - **To Run it effectively, with more krips understanding:**
### - [Run On Google Colab](https://colab.research.google.com/drive/1B5wsSNTY5YGUqBKkAFUgLJjG5TFu6qUG?usp=sharing)

# **📊Dataset Description**

The dataset provided appears to be historical stock market data for Tesla, Inc. (TSLA). 
Here's a summary of its structure and key statistics:

## The Dataset Contains:

- Date: The date of the stock data, formatted as MM/DD/YYYY.
- Open: The price of the stock at the opening of the trading day.
- High: The highest price of the stock during the trading day.
- Low: The lowest price of the stock during the trading day.
- Close: The closing price of the stock for the trading day.
- Volume: The number of shares traded during the trading day.
- Adj Close: The adjusted closing price, accounting for any corporate actions such as dividends, stock splits, etc.

## Data Anaylsis:

### - There are 1,692 entries, indicating stock data for 1,692 trading days.
### - The dataset starts from June 29, 2010, with the first few entries showing significant volatility in the stock price and trading volume.
### - The Volume of shares traded also varies greatly, from as low as 118,500 to as high as 37,163,900, with a mean trading volume of around 4,270,741 shares.

# **🔼Dataset Split Info**

The dataset data is divided into training and validation sets as follows:

- **Training the model by some old data from the dataset.**
- **Validating Data on the previous closing values from the dataset.**
- **Predicting Data by using the trained model.**

# **💡Approach**

### 1. First The Model fetch Dataset File (with an ext of .csv)
### 2. Secondly the Model understands the Data Injection By Kaggle
### 3. Then the data is cleaned and then trained
### 4. Training model on the closing values of each day from the dataset file.
### 5. The Lib like Numpy manipulates the array, along side Lib Panda Transforms and Visualises the Data.
### 6. The Lib Matplot, it plots the data, along with plotty for more reactive graphs.
### 7. Using Keras, Sequential, Dense & the most prominent LSTM model, we train the model layer by layer.
### 8. At the last the Output has been trained on the older data from the CSV file.
### 9. The Trained model gives the predicted the plotting with the valid values, 
### 10. Hence generated the final output of the next day closing value on the basis of previous 60 days.

# **🚀Results**

## Here are The Entered Dataset Values :
![Alt Text](https://i.pinimg.com/736x/1f/36/8b/1f368b46552afe13cf3f64dc6b3abfde.jpg)

## Here is the Final Result Graph:
![Alt Text](https://i.pinimg.com/736x/fe/e3/08/fee30839ce62e9f6f9d88a6a7fc2facc.jpg)

## Here is the prediction for the Closing Price of the next day:
![Alt Text](https://i.pinimg.com/736x/c7/b5/82/c7b582a691493d4fde4efd4361c03336.jpg)

# 🏗️ **Dependences**

Trend Pulse is built with these core frameworks and modules:

- **Streamlit** - To create the web app UI and interactivity 
- **LSTM** - To build the Long Short Term Memory model
- **Plotly** - To create interactive financial charts

# ⛩️ **Workflow**
The app workflow is:

1. User feeds the CSV file.
2. Historical data is fetched with CSV file.
3. LSTM model is trained on the data 
4. Model makes multi-day price forecasts
5. Results are plotted with Plotly

# ➼ **Accuracy**

## We Use Root Mean Square Deviation:
### Here is the result

![Alt Text](https://i.pinimg.com/736x/63/18/af/6318af6de91da69856b4e33c0380c724.jpg)

# **▶Video Explanation Of The Deployed Web APP**

## Click On The Image to play the Video.

[![Watch the video](https://i.pinimg.com/736x/b4/cc/1e/b4cc1e3c683ccc93084879ead9f69c89.jpg)](https://www.youtube.com/watch?v=8ZsUzq01A3w)

## **⚖️ Disclaimer**
**This is not financial advice! Use forecast data to inform your own investment research. No guarantee of trading performance.**


