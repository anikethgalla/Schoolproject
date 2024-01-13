import streamlit as st
import pandas as pd
import csv

url_video="https://www.youtube.com/watch?v=BYYwBLJ9q5E"
url_rop="https://docs.google.com/document/d/170jzbuCzIFEeF6p1C6MhRfFBfoPt1wQI9srwmH_j2fk/edit"
url_tips="https://docs.google.com/document/d/1jNiIhSdG2EZeWg1RU3CeVRL9aNjY-IBC03iwp3SJPgE/edit?usp=sharing "
url_regs=""
url_undocs=" https://digitallibrary.un.org/?_gl=1*1mdo6z5*_ga*ODg0MjE5NTMzLjE3MDI1NzgwNTc.*_ga_TK9BQL5X7Z*MTcwNTA3NjEyNC44LjEuMTcwNTA3NjU4OC4wLjAuMA.."

def add_info():
    st.subheader("ADD INFORMATION")
    st.write("After adding information refresh your page once")
    name = st.text_input("Enter Name:")
    email = st.text_input("Enter Email:")
    cost = st.number_input("Enter Cost:", min_value=0)
    hyplink = st.text_input("Enter Website Link:")
    reglink = st.text_input("Enter Registration Link:")
    delreq = st.number_input("Enter Min No. of Delegates:", min_value=0, step=1)
    insta = st.text_input("Enter Socials:")
    date=st.date_input("Enter date: ")

    if st.button("Add Information"):
        with open("munmaster_list.csv", "a", newline="") as passage_1:
            writer_1 = csv.writer(passage_1)
            if passage_1.tell() == 0:
                writer_1.writerow(["MUN name", "Email", "Reg_Cost", "Website", "Reg_Link", "Delegation Requirement", "insta","date"])
            record = [name, email, cost, hyplink, reglink, delreq, insta,date]
            writer_1.writerow(record)
        st.success("Information added successfully!")

def read_info():
    st.subheader("MUN DATABASE")
    try:
        df = pd.read_csv("munmaster_list.csv")
        st.dataframe(df)
    except pd.errors.EmptyDataError:
        st.warning("The CSV file is empty or does not contain valid data.")
    except FileNotFoundError:
        st.warning("File 'munmaster_list.csv' not found.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Streamlit app
st.set_page_config(
    page_title="MUN CONNECT",
    page_icon=":link:",
    layout="wide"
)

title_text = "MUN CONNECT "

styled_title = f"<h1 style='text-align: center; font-size: 48px; text-decoration: underline; font-family: Arial, sans-serif;'>{title_text}</h1>"

st.markdown(styled_title, unsafe_allow_html=True)

# Read and display information
read_info()

# Add information
add_info()


#navigation bar
video_tutorial = st.sidebar.link_button("Video tutorials", url_video )
rop=st.sidebar.link_button("Rules of Procedure", url_rop)
tips=st.sidebar.link_button("Research tips",url_tips)
df_dates_regs=st.sidebar.link_button("Upload muns",url_regs)
un_docs=st.sidebar.link_button("UN documents",url_undocs)

