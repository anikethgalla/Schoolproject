import streamlit as st
import pandas as pd
import csv
from datetime import datetime

url_video = "https://www.youtube.com/watch?v=BYYwBLJ9q5E"
url_rop = "https://docs.google.com/document/d/170jzbuCzIFEeF6p1C6MhRfFBfoPt1wQI9srwmH_j2fk/edit"
url_tips = "https://docs.google.com/document/d/1jNiIhSdG2EZeWg1RU3CeVRL9aNjY-IBC03iwp3SJPgE/edit?usp=sharing "
url_regs = ""
url_undocs = " https://digitallibrary.un.org/?_gl=1*1mdo6z5*_ga*ODg0MjE5NTMzLjE3MDI1NzgwNTc.*_ga_TK9BQL5X7Z*MTcwNTA3NjEyNC44LjEuMTcwNTA3NjU4OC4wLjAuMA.."

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
    date = st.date_input("Enter date:")

    if st.button("Add Information"):
        with open("munmaster_list.csv", "a", newline="") as passage_1:
            writer_1 = csv.writer(passage_1)
            if passage_1.tell() == 0:
                writer_1.writerow(["MUN name", "Email", "Reg_Cost", "Website", "Reg_Link", "Delegation Requirement", "insta", "date"])
            record = [name, email, cost, hyplink, reglink, delreq, insta, date]
            writer_1.writerow(record)
        st.success("Information added successfully!")

def read_info():
    st.subheader("MUN DATABASE")
    try:
        df = pd.read_csv("munmaster_list.csv")

        # Edit button is outside the loop
        if st.button("Edit"):
            for index, row in df.iterrows():
                edit_name = st.text_input(f"Edit Name for {index}", value=row["MUN name"])
                edit_email = st.text_input(f"Edit Email for {index}", value=row["Email"])
                edit_cost = st.number_input(f"Edit Cost for {index}", value=row["Reg_Cost"], min_value=0)
                edit_hyplink = st.text_input(f"Edit Website Link for {index}", value=row["Website"])
                edit_reglink = st.text_input(f"Edit Registration Link for {index}", value=row["Reg_Link"])
                edit_delreq = st.number_input(f"Edit Min No. of Delegates for {index}", value=row["Delegation Requirement"], min_value=0, step=1)
                edit_insta = st.text_input(f"Edit Socials for {index}", value=row["insta"])

                # Check if the existing date value is a valid date
                existing_date = row["date"]
                if pd.notna(existing_date) and isinstance(existing_date, str):
                    try:
                        existing_date = datetime.strptime(existing_date, "%Y-%m-%d").date()
                    except ValueError:
                        existing_date = None

                # Provide a default date if the existing date is not valid
                edit_date = st.date_input(f"Edit date for {index}", value=existing_date) if existing_date else st.date_input(f"Edit date for {index}")

                # Update the DataFrame with edited values
                df.at[index, "MUN name"] = edit_name
                df.at[index, "Email"] = edit_email
                df.at[index, "Reg_Cost"] = edit_cost
                df.at[index, "Website"] = edit_hyplink
                df.at[index, "Reg_Link"] = edit_reglink
                df.at[index, "Delegation Requirement"] = edit_delreq
                df.at[index, "insta"] = edit_insta
                df.at[index, "date"] = edit_date

                st.success(f"Record for {index} edited successfully!")

        st.dataframe(df)  # Display the updated DataFrame

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

# Navigation bar
video_tutorial = st.sidebar.link_button("Video tutorials", url_video)
rop = st.sidebar.link_button("Rules of Procedure", url_rop)
tips = st.sidebar.link_button("Research tips", url_tips)
df_dates_regs = st.sidebar.link_button("Upload muns", url_regs)
un_docs = st.sidebar.link_button("UN documents", url_undocs)
