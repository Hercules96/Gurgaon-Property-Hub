import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns
import ast

st.set_page_config(page_title="Gurgaon Apartment Hub - Visualizations", layout="wide")

st.title('Analytics')

#Scatter plot using langitude and longitude
new_df = pd.read_csv('C:\Project_Real_Estate_Prediction\Abhinav-Real-estate-Project-Website\dataset\data_viz1.csv')

group_df = new_df.groupby('sector').mean(numeric_only=True)[['price', 'price_per_sqft','built_up_area','latitude', 'longitude']]

st.title("Gurgaon Apartment Hub: Interactive Visualizations")
st.markdown("Explore property data in Gurgaon with various insightful visualizations.")

# Visualization 1: Sector Price per Sqft Geomap
st.header("1. Sector Price per Sqft Geomap")
st.subheader("Visualize the price per square foot across various sectors in Gurgaon.")

fig = px.scatter_mapbox(group_df, lat="latitude", lon="longitude", color="price_per_sqft", size='built_up_area',
                  color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                  mapbox_style="open-street-map",width=1200,height=700,hover_name=group_df.index)
st.plotly_chart(fig,use_container_width=True)

# Summary for Geomap
st.markdown("""
**Summary**:  
This map visualizes the price per square foot in various sectors of Gurgaon. Larger and darker circles represent higher prices, with a clear distinction of premium sectors.
""")

# Visualization 2: Wordcloud of Common Features in the Selected Sector
st.header("2. Wordcloud of Features Common in Selected Sector")
wordcloud_df = pd.read_csv('C:\Project_Real_Estate_Prediction\Abhinav-Real-estate-Project-Website\dataset\wordcloud.csv')
# st.dataframe(wordcloud_df)

list = ['all sector']+sorted(wordcloud_df['sector'].unique())

sector = st.selectbox("Select the sector",sorted(list))

def sector_wordcloud(sector):
    feature=[]
    if sector=='all sector':
        for item in wordcloud_df['features'].dropna().apply(ast.literal_eval):
            feature.extend(item)
    else:
        sample = wordcloud_df[wordcloud_df['sector']==sector]
        for item in sample['features'].dropna().apply(ast.literal_eval):
            feature.extend(item)
    feature= ' '.join(feature)
    feature= feature.replace('/','')
    return feature

st.set_option('deprecation.showPyplotGlobalUse', False)
if st.button('Create Wordcloud'):
    sector_features = sector_wordcloud(sector)

    wordcloud = WordCloud(width=800, height=800,
                          background_color='black',
                          stopwords=set(['s']),  # Any stopwords you'd like to exclude
                          min_font_size=10).generate(sector_features)

    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.tight_layout(pad=0)
    st.pyplot()
else:
    pass

# Summary for Wordcloud
st.markdown(f"""
**Summary**:  
This word cloud highlights the most common features in properties listed in **Sector {sector}**. Larger words represent features that are more frequently mentioned.
""")

# Visualization 3: Area vs Price Scatter Plot with Bedrooms as Hue
st.header("3. Area vs. Price Scatter Plot (Hue: Bedrooms)")

property_type = st.selectbox('Select Property Type', ['flat','house'])

if property_type == 'house':
    fig1 = px.scatter(new_df[new_df['property_type'] == 'house'], x="built_up_area", y="price", color="bedRoom", title="Area Vs Price")

    st.plotly_chart(fig1, use_container_width=True)
else:
    fig1 = px.scatter(new_df[new_df['property_type'] == 'flat'], x="built_up_area", y="price", color="bedRoom",
                      title="Area Vs Price")

    st.plotly_chart(fig1, use_container_width=True)

# Summary for Scatter Plot
st.markdown("""
**Summary**:  
This scatter plot visualizes the relationship between the **area of a property** and its **price**, with the number of bedrooms indicated by different colors. Properties with more bedrooms tend to have a higher price.
""")


# Visualization 4: Bed-Room-Hall-Kitchen (BHK) Pie Chart
st.header("4. Bed-Room-Hall-Kitchen (BHK) Distribution Pie Chart")

selected_sector_list = new_df['sector'].unique().tolist()
selected_sector_list.insert(0,'Overall')

sector_pie = st.selectbox("Select Sector",sorted(selected_sector_list))

if sector_pie=='Overall':
    fig2 = px.pie(new_df,names='bedRoom',labels=new_df['bedRoom'].unique())

    st.plotly_chart(fig2,use_container_width=True)

else:
    fig2 = px.pie(new_df[new_df['sector']==sector_pie],names='bedRoom',labels=new_df[new_df['sector']==sector_pie]['bedRoom'].unique())

    st.plotly_chart(fig2,use_container_width=True)

# Summary for BHK Price Comparison
st.markdown("""
**Summary**:  
This bar chart compares the **average price** of properties based on the number of bedrooms. Properties with more bedrooms tend to have a significantly higher average price.
""")

## Visualization 5: Side-by-Side Distribution Plot for Property Type
st.header("6. Side-by-Side Distribution Plot for Property Type")

sample= new_df[new_df['bedRoom'] <= 4]
count=0
sector_list = new_df['sector'].unique().tolist()
sector_list.insert(0,'Overall')
sector_box = st.selectbox("Select Sector",sorted(sector_list),key=count)
st.write('Selected',sector_box)

if sector_box == 'Overall':
    fig3 = px.box(new_df[new_df['bedRoom']<=4], x='bedRoom', y='price', title='BHK Price Range')

    st.plotly_chart(fig3,use_container_width=True)

else:
    fig3 = px.box(sample[sample['sector']==sector_pie], x='bedRoom', y='price', title='BHK Price Range')

    st.plotly_chart(fig3,use_container_width=True)

# Summary for BHK Price Comparison
st.markdown("""
**Summary**:  
This bar chart compares the **average price** of properties based on the number of bedrooms. Properties with more bedrooms tend to have a significantly higher average price.
""")

#6 Side by Side Distplot for property type
st.header('Side by Side Distplot for property type')

count=1
sector_list = new_df['sector'].unique().tolist()
sector_list.insert(0,'Overall')
sector_box = st.selectbox("Select Sector",sorted(sector_list),key=count)
st.write('Selected',sector_box)

sample1 = new_df[new_df['sector']==sector_box]

if sector_box=='Overall':
    fig3 = plt.figure(figsize=(10, 4))
    sns.distplot(new_df[new_df['property_type'] == 'house']['price'], label='house')
    sns.distplot(new_df[new_df['property_type'] == 'flat']['price'], label='flat')
    plt.legend()
    st.pyplot(fig3)

else:
    fig3 = plt.figure(figsize=(10, 4))
    sns.distplot(sample1[sample1['property_type'] == 'house']['price'], label='house')
    sns.distplot(sample1[sample1['property_type'] == 'flat']['price'], label='flat')
    plt.legend()
    st.pyplot(fig3)

# Summary for Property Type Distribution
st.markdown("""
**Summary**:  
This distribution plot shows the price distributions for different property types. It allows you to compare the price trends and spread for various categories, such as apartments, villas, and flats.
""")

# Footer
st.markdown("### Explore more insights and details about the Gurgaon real estate market.")