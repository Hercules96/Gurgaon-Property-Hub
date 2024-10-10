import streamlit as st
import pandas as pd
import numpy as np
import pickle
from PIL import Image


# Set up the page configuration
st.set_page_config(page_title="Price Predictor", layout="wide")

st.markdown("""
    <style>
        .custom-heading {
            color: #ffffff; /* Text color */
            font-size: 36px; /* Font size */
            font-weight: bold; /* Font weight */
            text-align: center; /* Text alignment */
            margin-top: 20px; /* Margin top */
            margin-bottom: 20px; /* Margin bottom */
            padding: 10px; /* Padding */
            border-bottom: 3px solid #2196F3; /* Bottom border */
        }
    </style>
    """, unsafe_allow_html=True)

# Title of the section
st.markdown('<h1 class="custom-heading">Gurgaon Properties Hub</h1>', unsafe_allow_html=True)

# Load the image
image_path = r'dataset/Price Predictor.jpg'
image = Image.open(image_path)

def image_to_base64(img):
    import base64
    from io import BytesIO
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode()

# Center-align the image using Markdown
st.markdown(
    """
    <div style="text-align: center;">
        <img src="data:image/jpeg;base64,{}" width="600">
    </div>
    """.format(image_to_base64(image)),
    unsafe_allow_html=True
)

st.header("Start Predicting Property Prices")

# Introduction text
st.write("""
Discover the estimated value of your property with just a few clicks. Our advanced prediction tool uses the latest data to provide you with accurate price estimates based on your property details.
""")

st.subheader("Enter your preferences")

# Load the data and model
with open(r'C:\Project_Real_Estate_Prediction\Abhinav-Real-estate-Project-Website\data_version2.pkl', 'rb') as file:
    df = pickle.load(file)

with open(r'C:\Project_Real_Estate_Prediction\Abhinav-Real-estate-Project-Website\model_version2.pkl', 'rb') as file:
    model = pickle.load(file)

# Property_type (assume this should be treated as categorical)
property_type = st.selectbox('Select the type of property_type', ['flat', 'house'])

# sector (assume this is categorical as well)
sector = st.selectbox('Select Sector Number', sorted(df['sector'].unique().tolist()))

# bedroom (numeric input)
bedroom = int(st.selectbox('Number of bedRoom', sorted(df['bedRoom'].unique().tolist())))

# bathroom (numeric input)
bathroom = int(st.selectbox('Number of bathroom', sorted(df['bathroom'].unique().tolist())))

# balcony (categorical input)
balcony = st.selectbox('Number of the balcony', sorted(df['balcony'].unique().tolist()))

# agePossession (categorical)
agePossession = st.selectbox('Age Possession of the Property', df['agePossession'].unique().tolist())

# built_up_area (numeric input)
built_up_area = float(st.number_input('Size of the property in square Feet'))

# servant_room (numeric input)
servant_room = float(st.selectbox('servant_room', df['servant room'].unique().tolist()))

# store_room (numeric input)
store_room = float(st.selectbox('Store Room', [0.0, 1.0]))

# furnishing_type (categorical)
furnishing_type = st.selectbox('Furnishing Type', sorted(df['furnishing_type'].unique().tolist()))

# luxury_category (categorical)
luxury_category = st.selectbox('Luxury Category', sorted(df['luxury_category'].unique().tolist()))

# floor_category (categorical)
floor_category = st.selectbox('Floor Category', sorted(df['floor_category'].unique().tolist()))

# Button to trigger the prediction
if st.button('Predict'):
    # Prepare the input data
    input_data = [
        [property_type, sector, bedroom, bathroom, balcony, agePossession, built_up_area, servant_room, store_room,
         furnishing_type, luxury_category, floor_category]]

    # Column names as expected by the model
    col = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
           'agePossession', 'built_up_area', 'servant room', 'store room',
           'furnishing_type', 'luxury_category', 'floor_category']

    # Create a DataFrame from the input data
    one_df = pd.DataFrame(input_data, columns=col)

    # You may need to encode categorical variables here based on the model's requirements

    # Display the input data for review
    #st.dataframe(one_df)

    # Make the prediction
    prediction = np.expm1(model.predict(one_df))
    lower_range = (prediction - 0.08)
    upper_range = (prediction + 0.08)


    # st.write("The Property price will fall in the range of {:.2f} Cr to {:.2f} Cr".format(
    #     np.round(lower_range[0], 2),
    #     np.round(upper_range[0], 2)))

    lower_range = np.round(lower_range[0], 2)
    upper_range = np.round(upper_range[0], 2)
    # Display with Markdown for special formatting
    st.markdown(
        """
        **The Property price will fall in the range of:**

        - **₹{:.2f} Cr** to **₹{:.2f} Cr**
        """.format(lower_range, upper_range),
        unsafe_allow_html=True
    )
