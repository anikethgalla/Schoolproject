import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth
from PIL import Image

url_video="https://www.youtube.com/watch?v=BYYwBLJ9q5E"
url_rop="https://docs.google.com/document/d/170jzbuCzIFEeF6p1C6MhRfFBfoPt1wQI9srwmH_j2fk/edit"
url_tips="https://docs.google.com/document/d/1jNiIhSdG2EZeWg1RU3CeVRL9aNjY-IBC03iwp3SJPgE/edit?usp=sharing "
url_regs="https://munconnectupload.streamlit.app/"
url_undocs=" https://digitallibrary.un.org/?_gl=1*1mdo6z5*_ga*ODg0MjE5NTMzLjE3MDI1NzgwNTc.*_ga_TK9BQL5X7Z*MTcwNTA3NjEyNC44LjEuMTcwNTA3NjU4OC4wLjAuMA.."
# Create the Streamlit web app
st.set_page_config(
    page_title="MUN CONNECT",
    page_icon=":link:",
    layout="wide"
)

#title
title_text = "MUN CONNECT "

styled_title = f"<h1 style='text-align: center; font-size: 48px; text-decoration: underline; font-family: Arial, sans-serif;'>{title_text}</h1>"

st.markdown(styled_title, unsafe_allow_html=True)


#image
img=Image.open(r"C:\Users\archa\.vscode\Schoolproject\wesbite\un-afp.jpg")
st.image(
    img,
    width=1200 ,
    channels= "RGB"
)


df = pd.read_csv("munmaster_list.csv")

st.write('Upcoming MUNs:')
st.dataframe(df)


#navigation bar
video_tutorial = st.sidebar.link_button("Video tutorials", url_video )
rop=st.sidebar.link_button("Rules of Procedure", url_rop)
tips=st.sidebar.link_button("Research tips",url_tips)
df_dates_regs=st.sidebar.link_button("Upload muns",url_regs)
un_docs=st.sidebar.link_button("UN documents",url_undocs)



