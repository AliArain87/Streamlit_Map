import streamlit as st 
import pandas as pd
from geopy.geocoders import Nominatim


geolocator = Nominatim(user_agent="city_coordinates")

def get_coordinates(city):
    location = geolocator.geocode(city)
    return location.latitude, location.longitude


st.title("🗺My Map🗺")
st.success("Developed by Ali Hasnain✨")
st.sidebar.title("City Coordinates")
city = st.sidebar.text_input("Enter the city name")


if st.sidebar.button("Submit",help="Click to get the coordinates"):
    lat, lon = get_coordinates(city)
    st.success(city)
    st.write(lat, lon)
    st.map(pd.DataFrame({"lat": [lat], "lon": [lon]}))



