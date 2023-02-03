import streamlit as st 
import pandas as pd
from geopy.geocoders import Nominatim
from PIL import Image
import time



st.set_page_config(
    page_title="My Map",
    page_icon="👋",
)


geolocator = Nominatim(user_agent="city_coordinates")

def get_coordinates(city):
    location = geolocator.geocode(city)
    return location.latitude, location.longitude


st.title("_🗺 My Map 🗺_")

with st.expander("**_About This App_**"):  
    st.markdown("Developed by **:blue[_Ali Hasnain✨_]**")
    col1, col2 = st.columns(2)
    with col1:
        img = Image.open("profile.png")
        st.image(img, width=200)
    with col2:
        # github 
        st.markdown("[Github](https://github.com/AliArain87)")
        # linkedin
        st.markdown("[Linkedin](https://www.linkedin.com/in/ali-hasnain-8b047a210/)")
        # facebook
        st.markdown("[Facebook](https://www.facebook.com/alibaba.arain.75)")




    st.warning("This app is used to get the coordinates of a city.")
    st.info("Enter the city name in the sidebar and click on the submit button to get the coordinates")
    




st.sidebar.title("City Coordinates")
city = st.sidebar.text_input("Enter the city name")

status = st.progress(0)
if st.sidebar.button("Submit",help="Click to get the coordinates"):
    with st.spinner('**Wait for it...!!**'):
        time.sleep(2)
    lat, lon = get_coordinates(city)
    st.success(city)
    st.write(lat, lon)
    st.map(pd.DataFrame({"lat": [lat], "lon": [lon]}))




