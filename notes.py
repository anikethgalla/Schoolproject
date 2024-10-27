import streamlit as st
import os


def load_notes():
    if os.path.exists("notes.txt"):
        with open("notes.txt", "r") as f:
            return f.readlines()
    return []


def save_notes(notes):
    with open("notes.txt", "w") as f:
        f.writelines(notes)


def clear_notes():
    with open("notes.txt", "w") as f:
        f.write("") 


notes = load_notes()


st.title("MUN Notes")


if notes:
    st.subheader("Your Notes:")
    for i, note in enumerate(notes):
        st.write(f"{i + 1}: {note.strip()}")  


new_note = st.text_area("Type your note here:", height=100)


if st.button("Save Note"):
    if new_note:
        notes.append(new_note + '\n')  
        save_notes(notes)  
        st.success("Note saved!")  
        notes = load_notes()  
    else:
        st.warning("Please enter a note before saving.")


clear_confirm = st.checkbox("Check this box to confirm clearing all notes")


if st.button("Clear All Notes"):
    if clear_confirm:
        clear_notes()  
        notes = []  
        st.success("All notes cleared!")  
    else:
        st.warning("Please check the box to confirm clearing all notes.")
