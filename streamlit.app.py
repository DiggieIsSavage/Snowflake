import streamlit
import pandas as pd

myfruitlist = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")


streamlit.title("My Parents New Healthy Diner")
streamlit.header("Breakfast Menu")
streamlit.text( "🥞 Omega 3 & Blueberry Oatmeal" + "\n" + "🥗" + "Kale, Spinach & Rocket Smoothie" + "\n" + "🐔" + "Hard Boiled Free-Range Eggs"
              + "\n" + "🥑" + "🍞" + "Avocado Toast")  
streamlit.header("🍌 🍎 Build your own smoothie 🥝 🍇") 
streamlit.dataframe(my_fruit_list)
