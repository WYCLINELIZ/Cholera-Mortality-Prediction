import streamlit as st
import joblib

# Load the model
model = joblib.load('cholera_prediction_model .joblib')


st.image("engage_jooust_branding.png", caption="Engage brands")
st.markdown("[ENGAGE Program](https://engage.uonbi.ac.ke)")
 #Title of the App        
st.title('Cholera Mortality Prediction')

# Define categorical to numerical mappings
Test_result = {'Negative': 0, 'Positive': 1}
Sex = {'Male': 1, 'Female': 2}
Subcounty = {'South': 1, 'East': 2, 'West': 3, 'North': 4, 'North East': 6}
Water = {'piped': 1, 'borehole': 2, 'public well': 3, 'other': 4}
Sanitation = {'private toilet': 1, 'public toilet': 2, 'public latrine': 3, 'other': 4}
Income = {'lowest': 1, 'low': 2, 'average': 3, 'high': 4, 'highest': 5}
Informal_settlement = {'yes': 1, 'no': 2}
Outcome = {0: 'survived', 1: 'Died'}

# Input fields for user data
test_result = st.selectbox('Test Result', ['Negative', 'Positive'])
sex = st.selectbox('Sex', ['Male', 'Female'])
age = st.slider('Age', min_value=0, max_value=100, step=1)
subcounty = st.selectbox('Subcounty', ['South', 'East', 'West', 'North', 'North East'])
income = st.selectbox('Income', ['lowest', 'low', 'average', 'high', 'highest'])
water = st.selectbox('Water', ['piped', 'borehole', 'public well', 'other'])
sanitation = st.selectbox('Sanitation', ['private toilet', 'public toilet', 'public latrine', 'other'])
informal_settlement = st.selectbox('Informal Settlement', ['yes', 'no'])

if st.button('Predict'):
    # Map inputs to numerical values
    input_data = [
        Sex[sex],
        age,
        Income[income],
        Test_result[test_result],
        Subcounty[subcounty],
        Water[water],
        Sanitation[sanitation],
        Informal_settlement[informal_settlement]
    ]
    
    # Make prediction
    prediction = model.predict([input_data])
    
    # Display result
    st.write('Prediction:', Outcome[prediction[0]])
