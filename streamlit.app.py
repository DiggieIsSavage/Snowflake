#importing libraries
import streamlit
import pandas as pd

#declaring variables and then selecting the name of the fruit as the index
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit.list.set_index("Fruit")

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


