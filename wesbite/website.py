import streamlit as st
import pandas as pd
from PIL import Image

# URLs
url_video = "https://www.youtube.com/watch?v=BYYwBLJ9q5E"
url_rop = "https://docs.google.com/document/d/170jzbuCzIFEeF6p1C6MhRfFBfoPt1wQI9srwmH_j2fk/edit"
url_tips = "https://docs.google.com/document/d/1jNiIhSdG2EZeWg1RU3CeVRL9aNjY-IBC03iwp3SJPgE/edit?usp=sharing"
url_undocs = "https://digitallibrary.un.org/?_gl=1*1mdo6z5*_ga*ODg0MjE5NTMzLjE3MDI1NzgwNTc.*_ga_TK9BQL5X7Z*MTcwNTA3NjEyNC44LjEuMTcwNTA3NjU4OC4wLjAuMA.."
url_regs = "https://munconnectupload.streamlit.app/"
url_news = "https://www.reuters.com/"
url_notes = "https://anikethgalla-schoolproject-notes-zdgvq9.streamlit.app/"

# Create the Streamlit web app
st.set_page_config(
    page_title="MUN CONNECT",
    page_icon=":link:",
    layout="wide"
)

# Title
title_text = "MUN CONNECT"
styled_title = f"<h1 style='text-align: center; font-size: 48px; text-decoration: underline; font-family: Arial, sans-serif;'>{title_text}</h1>"
st.markdown(styled_title, unsafe_allow_html=True)

# Image
img = Image.open(r"C:\Users\archa\.vscode\Schoolproject\wesbite\0_L4Y0o4yoqY5fBpgD.png")
st.image(
    img,
    width=1200,
    channels="RGB"
)

# Navigation bar
st.sidebar.link_button("Video tutorials", url_video)
st.sidebar.link_button("Rules of Procedure", url_rop)
st.sidebar.link_button("Research tips", url_tips)
st.sidebar.link_button("MUN database", url_regs)
st.sidebar.link_button("UN documents", url_undocs)
st.sidebar.link_button("UN News", url_news)
st.sidebar.link_button("Notes", url_notes)

# Function to display the DataFrame from the CSV file
def display_munmaster_list():
    try:
        # Load the CSV file into a DataFrame
        df = pd.read_csv(r"C:\Users\archa\.vscode\Schoolproject\munmaster_list.csv")
        st.subheader("MUN Master List")
        st.dataframe(df)  # Display the DataFrame
    except FileNotFoundError:
        st.error("The file 'munmaster_list.csv' was not found.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Call the function to display the DataFrame
display_munmaster_list()

