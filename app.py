import streamlit as st
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import math
import plotly.express as px

# Function to load the dataset
def load_dataset(uploaded_file):
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        return df
    return None

# Function to train LSTM model
def train_model(df):
    # Convert the Date column to datetime type and set it as the index
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)

    st.subheader('Closing Price of the stock')
    # Plotting the closing price history
    st.line_chart(df['Close'])

    # Prepare the data for training the LSTM model
    data = df.filter(['Close'])
    dataset = data.values # Convert the dataframe to a numpy array
    training_data_len = math.ceil(len(dataset) * .8) # 80% of the data for training

    # Scale the data
    scaler = MinMaxScaler(feature_range=(0,1))
    scaled_data = scaler.fit_transform(dataset)

    # Create the training data set
    train_data = scaled_data[0:training_data_len, :]
    x_train = []
    y_train = []

    for i in range(60, len(train_data)):
        x_train.append(train_data[i-60:i, 0])
        y_train.append(train_data[i, 0])

    # Convert the x_train and y_train to numpy arrays
    x_train, y_train = np.array(x_train), np.array(y_train)

    # Reshape the data into the shape accepted by the LSTM
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

        #Build the LSTM model
    model =Sequential()
    model.add(LSTM(64,return_sequences=True, input_shape=(x_train.shape[1],1)))
    model.add(LSTM(64, return_sequences= False))
    model.add(Dense(32))
    model.add(Dense(1))

    # Compile the model
    model.compile(optimizer='adam', loss='mean_squared_error')

    # Train the model
    with st.spinner('Training the model...'):
        model.fit(x_train, y_train, batch_size=1, epochs=1)

    return model, scaler, df, training_data_len

# Function to create testing data sets and make predictions
def create_test_and_predict(model, scaler, df, training_data_len):
    # Create the testing data sets
    data = df.filter(['Close'])
    dataset = data.values # Convert the dataframe to a numpy array
    training_data_len = math.ceil(len(dataset) * .8) # 80% of the data for training

    # Scale the data
    scaler = MinMaxScaler(feature_range=(0,1))
    scaled_data = scaler.fit_transform(dataset)
    #create the testing data sets
    #create a new array containing scale values from index 1543 to 2003
    test_data= scaled_data[training_data_len-60:, :]
    #create the data sets x_test and y_test
    x_test = []
    y_test = dataset[training_data_len:,:]
    for i in range(60,len(test_data)):
        x_test.append(test_data[i-60:i,0])
    #convert the data to a numpy array
    x_test = np.array(x_test)
    #reshape the data
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1],1))
    x_test.shape
    #predicting the data
    predictions = model.predict(x_test)
    predictions = scaler.inverse_transform(predictions)

    # Plot the data
    train = data[:training_data_len]
    valid = data[training_data_len:]
    valid['Predictions'] = predictions

    fig = px.line()
    fig.add_scatter(x=train.index, y=train['Close'], mode='lines', name='Train', line=dict(width=3.5))
    fig.add_scatter(x=valid.index, y=valid['Close'], mode='lines', name='Valid', line=dict(width=3.5))
    fig.add_scatter(x=valid.index, y=valid['Predictions'], mode='lines', name='Predictions', line=dict(width=3.5))
    fig.update_layout(title='Model', xaxis_title='Date', yaxis_title='Close Price')
    st.plotly_chart(fig)
    
# Function to predict next day's closing price
def predict_price(model, scaler, df):
    # Prepare the last 60 days closing price values for prediction
    last_60_days = df[-60:]['Close'].values # Extract 'Close' prices only
    last_60_days_scaled = scaler.transform(last_60_days.reshape(-1, 1))
    X_test = np.reshape(last_60_days_scaled, (1, last_60_days_scaled.shape[0], 1))

    # Predict the next day's closing price
    pred_price = model.predict(X_test)
    pred_price = scaler.inverse_transform(pred_price)
    return pred_price

# Main Streamlit app
def main():
    st.title('Stock Price Prediction')
    st.write('Upload a CSV file containing the stock data.')

    # File uploader for dataset upload
    uploaded_file = st.file_uploader("Upload CSV file", type=['csv'])

    if uploaded_file is not None:
        df = load_dataset(uploaded_file)
        if df is not None:
            st.write('Dataset loaded successfully!')
            st.write(df.head())

            # Train LSTM model
            model, scaler, df, training_data_len = train_model(df)

            # Create testing data sets and make predictions
            create_test_and_predict(model, scaler, df, training_data_len)

            st.subheader('Based On the Prevous 60 days Data.')
            # Predict next day's closing price
            pred_price = predict_price(model, scaler, df)
            st.write("Predicted Next Day's Closing Price: ", pred_price)

# Run the Streamlit app
if __name__ == "__main__":
    main()
