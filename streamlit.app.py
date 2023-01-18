#importing libraries
import streamlit
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

#declaring variables and then selecting the name of the fruit as the index
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index("Fruit")


#displaying objects in streamlit
streamlit.title("My Parents New Healthy Diner")
streamlit.header("Breakfast Menu")
streamlit.text( "🥞 Omega 3 & Blueberry Oatmeal" + "\n" + "🥗" + "Kale, Spinach & Rocket Smoothie" + "\n" + "🐔" + "Hard Boiled Free-Range Eggs"
              + "\n" + "🥑" + "🍞" + "Avocado Toast")  
streamlit.header("🍌 🍎 Build your own smoothie 🥝 🍇") 

#let's put a picklist here so they can pick the fruit they want to include and assign a variable name

fruits_selected = streamlit.multiselect("Pick some fruits", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the table on the page
streamlit.dataframe(fruits_to_show)

#create the repeatable code block (called a function)
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    #streamlit.write('The user entered ', fruit_choice)
    #streamlit.text(fruityvice_response.json())
    #take the json version of the response and normalize it
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

#putting in new header and text in new app
# streamlit.text(fruityvice_response) # will not show a value as you need to work on the format
streamlit.header('Fruityvice Fruit Advice!')

try: 
  fruit_choice = streamlit.text_input('What fruit would you like information about?', 'kiwi')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else: 
    back_from_function = get_fruityvice_data(fruit_choice)
  
    #output it in the screen as a table
    streamlit.dataframe(fruityvice_normalized)

except URLError as e: 
  streamlit.error()

#to stop a streamlit code below during troubleshooting use the script below
streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
my_data_row = my_cur.fetchall()
streamlit.text("The fruit load list contains:")
streamlit.dataframe(my_data_row)

#Adding an additional text input
add_my_fruit = streamlit.text_input('What fruit would you like to add?', 'jackfruit')
added_fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + add_my_fruit)
streamlit.write('Thanks for adding', add_my_fruit)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")
