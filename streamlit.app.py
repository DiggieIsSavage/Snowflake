#importing libraries
import streamlit
import pandas as pd
import requests
import snowflake.connector

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

#putting in new header and text in new app
# streamlit.text(fruityvice_response) # will not show a value as you need to work on the format
streamlit.header('Fruityvice Fruit Advice!')
fruit_choice = streamlit.text_input('What fruit would you like information about?', 'kiwi')
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
streamlit.write('The user entered ', fruit_choice)

#streamlit.text(fruityvice_response.json())

#take the json version of the response and normalize it
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
#output it in the screen as a table
streamlit.dataframe(fruityvice_normalized)


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM FRUIT.LOAD.LIST")
my_data_row = my_cur.fetchone()
streamlit.text("The fruit load list contains:")
streamlit.text(my_data_row)
