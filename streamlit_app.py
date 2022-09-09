import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner')
streamlit.header ('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text ('🥗 Kale, Spinach & ROcket Smoothie')
streamlit.text ('🐔 Hard-Boiled Free-Range Egg')
streamlit.text ('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#pick list for customers
streamlit.multiselect("Pick some fruits:", list(my_fruits_list.index))
#display table
streamlit.dataframe(my_fruit_list)
