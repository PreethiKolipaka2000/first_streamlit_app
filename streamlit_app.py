import streamlit 
import pandas
import requests

streamlit.header("Breakfast Favorites")
streamlit.text("🥣 Omego 3 and Blueberry Oatmeal") 
streamlit.text("🥗 Kale, Spinach & Rocket Smoothie")
streamlit.text("🐔 Hard-Boiled Free-range egg")
streamlit.text("🥑🍞 Avocado Toast") 
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index("Fruit")
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

streamlit.dataframe(fruits_to_show)
streamlist.text(fruityvice_response)


