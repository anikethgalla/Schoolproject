import streamlit as st
import pandas as pd
import csv
import os
from datetime import datetime

# Get the directory of the current script
current_directory = os.path.dirname(__file__)

# Join the directory with the filename to create the full path
file_path = os.path.join(current_directory, "munmaster_list.csv")

def add_info():
    
    st.subheader("Add MUN Connect details")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        name = st.text_input("Enter Name:")

    with col2:
        email = st.text_input("Enter Email:")
    
    with col3:
        cost = st.number_input("Enter Cost:", min_value=0.0)  

    with col1:
        hyplink = st.text_input("Enter Website Link:")
    
    with col2:
        reglink = st.text_input("Enter Registration Link:")

    with col3:
        delreq = st.number_input("Enter Min No. of Delegates:", min_value=0, step=1)

    with col1:
        insta = st.text_input("Enter Socials:")

    with col2:
        date = st.date_input("Enter date:")

    if st.button("Add Information"):
        with open(file_path, "a", newline="") as passage_1:
            writer_1 = csv.writer(passage_1)
            if passage_1.tell() == 0:
                writer_1.writerow(["MUN name", "Email", "Reg_Cost", "Website", "Reg_Link", "Delegation Requirement", "insta", "date"])
            record = [name, email, cost, hyplink, reglink, delreq, insta, date]
            writer_1.writerow(record)
        st.rerun()

def read_info():
    st.subheader("Existing MUN Connects")
    try:
        df = pd.read_csv(file_path)

        
        df['Reg_Cost'] = pd.to_numeric(df['Reg_Cost'], errors='coerce')
        df['Delegation Requirement'] = pd.to_numeric(df['Delegation Requirement'], errors='coerce')

        if df.empty:
            st.warning("No records found in the MUN database.")
            return

        st.dataframe(df.fillna("")) 

    except pd.errors.EmptyDataError:
        st.warning("The CSV file is empty or does not contain valid data.")
    except FileNotFoundError:
        st.warning("File 'munmaster_list.csv' not found.")
    except Exception as e:
        st.error("An error occurred: {}".format(e))

def editAndDelete():
    
    st.subheader("Edit and Delete MUN Connects")
    try:
        df = pd.read_csv(file_path)

        
        df['Reg_Cost'] = pd.to_numeric(df['Reg_Cost'], errors='coerce')
        df['Delegation Requirement'] = pd.to_numeric(df['Delegation Requirement'], errors='coerce')
        
      
        st.session_state.df = df.fillna("")

        # delete a row
        def delete_row(index):
            st.session_state.df = st.session_state.df.drop(index).reset_index(drop=True)

        #uptdate a row
        def update_row(index, updated_values):
            for col, value in updated_values.items():
                st.session_state.df.at[index, col] = value

        col_headers = st.columns(len(df.columns) + 2)
        for j, col in enumerate(df.columns):
            col_headers[j].write(f"**{col}**")
        col_headers[len(df.columns)].write("**Edit**")
        col_headers[len(df.columns) + 1].write("**Delete**")


        for i, row in st.session_state.df.iterrows():
            cols = st.columns(len(row) + 2)  

            # Edit
            updated_values = {}
            for j, (col, value) in enumerate(row.items()):
                updated_values[col] = cols[j].text_input(f"{col}_{i}", value, label_visibility="collapsed")

            # Edit button
            if cols[len(row)].button("Save", key=f"save_{i}"):
                update_row(i, updated_values)
                df = st.session_state.df
                df.to_csv(file_path, index=False)
                st.rerun()

            # Delete button
            if cols[len(row) + 1].button("Delete", key=f"delete_{i}"):
                delete_row(i)
                df = st.session_state.df
                df.to_csv(file_path, index=False)
                st.rerun()
    except FileNotFoundError:
        st.warning("File 'munmaster_list.csv' not found.")
    except Exception as e:
        st.error("An error occurred: {}".format(e))

def show_page():
    title_text = "MUN CONNECT"

    styled_title = "<h1 style='text-align: center; font-size: 48px; text-decoration: underline; font-family: Arial, sans-serif;'>{}</h1>".format(title_text)

    st.markdown(styled_title, unsafe_allow_html=True)
    if st.session_state.username == "admin":
        # Add information
        add_info()

    # Read and display information
    read_info()

    if st.session_state.username == "admin":
        # Edit and Delete
        editAndDelete()                                     