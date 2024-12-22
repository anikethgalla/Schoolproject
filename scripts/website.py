import streamlit as st
import pandas as pd
import os
from PIL import Image

def show_page():
    # Title
    title_text = "MUN CONNECT"
    styled_title = f"<h1 style='text-align: center; font-size: 48px; text-decoration: underline; font-family: Arial, sans-serif;'>{title_text}</h1>"
    st.markdown(styled_title, unsafe_allow_html=True)
    # Get the directory of the current script
    current_directory = os.path.dirname(__file__)

    # Join the directory with the filename to create the full path
    file_path = os.path.join(current_directory, "un.png")

    # Image
    img = Image.open(file_path)
    st.image(
        img,
        width=1200,
        channels="RGB"
    )

# Function to display the DataFrame from the CSV file
def display_munmaster_list():
    try:
        # Get the directory of the current script
        current_directory = os.path.dirname(__file__)

        # Join the directory with the filename to create the full path
        file_path = os.path.join(current_directory, "../munmaster_list.csv")

        # Load the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        st.subheader("MUN Connects")
        st.dataframe(df)  # Display the DataFrame
    except FileNotFoundError:
        st.error("The file 'munmaster_list.csv' was not found.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
