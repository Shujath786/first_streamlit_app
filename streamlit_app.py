import streamlit
import pandas
import requests
#import snowflake.connector
from urllib.error import URLError

streamlit.title('My Parents New Healthy Diner!')

streamlit.header('Breakfast Favorites!')
streamlit.text(' 🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
#import pandas
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a picklist here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Apple'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# display the table on the page
streamlit.dataframe(fruits_to_show)

# New Section to display fruityvice api response
#streamlit.header("Fruityvice Fruit Advice!")
#try:
  #fruit_choice = streamlit.text_input('What fruit would you like information about?')
  #if not fruit_choice:
     # streamlit.error("Please select a fruit to get information.")
  #else:
      #import requests
  #    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
      #The below line of code normalizes the response from JSON to regular text
  #    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
      #The below line of code puts the above result into a table
  #    streamlit.dataframe(fruityvice_normalized)
#except URLError as e:
  #  streamlit.error()
#create the repeatable code block (called a function)
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized
#New Section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
      streamlit.error("Please select a fruit to get information.")
  else:
      back_from_function = get_fruityvice_data(fruit_choice)
      streamlit.dataframe(back_from_function)
