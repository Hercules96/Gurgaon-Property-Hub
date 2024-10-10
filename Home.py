import streamlit as st

st.set_page_config(
    page_title="Gurgaon Apartment Hub",
    page_icon="👋",
    layout="wide"
)

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

# Applying the custom CSS class to a heading
st.markdown('<h1 class="custom-heading">Gurgaon Apartment Hub</h1>', unsafe_allow_html=True)

st.image("dataset/Resident-property-in-gugram.png", caption="Gurgaon Skyline", use_column_width=True)

# Title
st.title("Welcome to Gurgaon Apartment Hub")

# Introduction
st.markdown(
    """
    At Gurgaon Apartment Hub, we are dedicated to helping you find your perfect home in the vibrant city of Gurgaon. Our platform offers a range of features designed to make your property search and decision-making process as smooth and informed as possible:
    """
)

# Features
st.markdown(
    """
    ### 🌟 Explore Diverse Listings
    Browse through a comprehensive collection of apartment listings, including flats, houses, and luxury residences. Each listing is detailed with high-quality images, floor plans, and property specifics.

    ### 🔍 Advanced Search Filters
    Use our intuitive search filters to narrow down options based on location, budget, property type, number of bedrooms, and more. Find the apartment that best matches your needs with ease.

    ### 📍 Interactive Maps
    Visualize property locations on interactive maps to get a better sense of the neighborhood, nearby amenities, and transport links.

    ### 🔧 Personalized Recommendations
    Receive tailored property suggestions based on your preferences and search history. Let us help you discover the best options suited to your lifestyle.
    """
)

# Conclusion
st.markdown(
    """
    Thank you for choosing Gurgaon Apartment Hub. We are excited to help you find your next dream apartment. Explore, search, and connect with us today!
    """
)

# Page Title
st.markdown("<h3 style='text-align: center;'>See howGurgaon Apartment Hub can help</h3>", unsafe_allow_html=True)

# Columns to divide the content into three sections
col1, col2, col3 = st.columns(3)

from PIL import Image

# Open the image using PIL
image_Apartment = Image.open("dataset/Apartment Recommendation.png")
image_price = Image.open("dataset/Price Predictor.jpg")
image_recommendation = Image.open("dataset/Visualization.png")

# Resize the image to your desired dimensions
resized_image_Apartment = image_Apartment.resize((300, 200))  # Width: 300, Height: 200
resized_image_price = image_price.resize((300, 200))  # Width: 300, Height: 200
resized_image_recommendation = image_recommendation.resize((300, 200))  # Width: 300, Height: 200

#Column 1: Price predictor
with col1:
    st.image(resized_image_price)  # Add your own image link
    st.markdown("<h4 style='text-align: center;'>Price Predictor</h4>", unsafe_allow_html=True)
    st.write(
        "Predict apartment prices with precision using our advanced price prediction modules, designed to deliver accurate and insightful market valuations."
    )


# Column 2: Rent a Home
with col2:
    st.image(resized_image_recommendation)  # Add your own image link
    st.markdown("<h4 style='text-align: center;'>Visualization</h4>", unsafe_allow_html=True)
    st.write(
        "The Visualization module of the Gurgaon Properties Hub project offers interactive charts and graphs to analyze property prices, areas, and location-based trends."
    )

# Column 3: See Neighborhoods
with col3:
    st.image(resized_image_Apartment)  # Add your own image link
    st.markdown("<h4 style='text-align: center;'>Apartment Recommendation</h4>", unsafe_allow_html=True)
    st.write(
        "The Apartment Recommendation module of the Gurgaon Properties Hub provides personalized apartment suggestions based on user preferences like budget, location, and amenities."
    )





