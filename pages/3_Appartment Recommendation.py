import pickle
import pandas as pd
import numpy as np
import streamlit as st

st.set_page_config(page_title='Appartment Recommendation')
#Loading the dataset to fetch the indexes
location_df = pickle.load(open('C:\Project_Real_Estate_Prediction\Abhinav-Real-estate-Project-Website\dataset\location_df.pkl','rb'))


#Loading the similarity based on the features
cosine_sim1 = pickle.load(open('C:\Project_Real_Estate_Prediction\Abhinav-Real-estate-Project-Website\dataset\cosine1.pkl','rb'))

#Loading the similarity based on the PriceDetails
cosine_sim2 = pickle.load(open('C:\Project_Real_Estate_Prediction\Abhinav-Real-estate-Project-Website\dataset\cosine2.pkl','rb'))

# #Loading the similarity based on the PriceDetails
cosine_sim3 = pickle.load(open('C:\Project_Real_Estate_Prediction\Abhinav-Real-estate-Project-Website\dataset\cosine3.pkl','rb'))

def recommend_properties_with_scores(property_name, top_n=247):
    # Calculating the collected similarity by providing weights to the individual features
    cosine_sim_matrix = 0.6 * cosine_sim1 + 0.4 * cosine_sim2   + cosine_sim3

    # Basically finding the respected property
    sim_scores = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))

    # Sorting the features based upon there enumerate score
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the indices and scores of the top_n most similar properties
    top_indices = [i[0] for i in sorted_scores[1:top_n + 1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n + 1]]

    # Prefencial list of properties
    properties = location_df.index[top_indices].tolist()

    # Fetching the preferred list of the properties
    recommendations_df = pd.DataFrame({
        'properties_name': properties,
        'similarity_scores': top_scores
    })

    return recommendations_df

st.header("Select Location and the desired distance in kms")
location = st.selectbox("Select the Location",sorted(location_df.columns.to_list()))

radius = st.number_input('Enter the distance in kms')
if st.button('Suggest Property'):
    result = location_df[location_df[location]< radius*1000][location].sort_values()
    #st.dataframe(result)
    suggestion = result.index.tolist()
    label_suggetsion = []
    for key,value in result.items():
        # st.text(str(key)+' '+str(round(value/1000,3))+' kms Away')
        label_suggetsion.append(value)
    str_label = [str(round((num/1000),2))+' kms from {}'.format(location) for num in label_suggetsion]
    genre = st.radio(
        "What's your favorite movie genre",
        suggestion,
        captions=str_label,
    )
    # recommendations_df = recommend_properties_with_scores(genre)
    # st.dataframe(recommendations_df)

property_name = st.selectbox('Select your Prefered Apartment',sorted(location_df.index.tolist()))
recommendations_df = recommend_properties_with_scores(property_name)
if st.button('Recommend'):
    st.dataframe(recommendations_df)