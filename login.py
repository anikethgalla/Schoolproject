import streamlit as st
import importlib

# Set page configuration
st.set_page_config(
    page_title="MUN Connect",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.current_page = "Login"  # Default page on load

# Logout function
def logout():
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.current_page = "Login"
    st.rerun()  # Refresh the app to log out immediately

# Sidebar: Custom menu with logout
def custom_sidebar():
    with st.sidebar:
        if st.session_state.logged_in:
            st.write(f"👋 Welcome, **{st.session_state.username}**")
            st.markdown("---")

            # Menu options (linked to script names)
            menu_options = {
                "Home": "scripts.website",
                "MUN Database": "scripts.demo",
                "Notes": "scripts.notes",
            }

            # Radio button for navigation
            selected_page = st.radio(
                "Menu",
                list(menu_options.keys()),
                index=list(menu_options.keys()).index(st.session_state.current_page),
                key="menu_radio",
            )

            # Update the session state only if the selected page changes
            if selected_page != st.session_state.current_page:
                st.session_state.current_page = selected_page
                st.rerun()  # Rerun the app immediately on selection

            st.markdown("---")
            # Logout button
            if st.button("Logout"):
                logout()

            st.markdown("---")
            # Static Links (External URLs or Internal Navigation)
            st.markdown("### UN MUN Links")
            st.markdown("[Video tutorials](https://www.youtube.com/watch?v=BYYwBLJ9q5E)")  # External link
            st.markdown("[Rules of Procedure](https://docs.google.com/document/d/170jzbuCzIFEeF6p1C6MhRfFBfoPt1wQI9srwmH_j2fk/edit)")
            st.markdown("[UN documents](https://digitallibrary.un.org/?_gl=1*1mdo6z5*_ga*ODg0MjE5NTMzLjE3MDI1NzgwNTc.*_ga_TK9BQL5X7Z*MTcwNTA3NjEyNC44LjEuMTcwNTA3NjU4OC4wLjAuMA..)")
            st.markdown("[Research tips](https://docs.google.com/document/d/1jNiIhSdG2EZeWg1RU3CeVRL9aNjY-IBC03iwp3SJPgE/edit?usp=sharing)")
            st.markdown("[UN News](https://www.reuters.com/)")

            return menu_options[selected_page]
        else:
            st.write("Please log in to access the app.")
            st.stop()  # Prevent further rendering if not logged in

# Main logic
if not st.session_state.logged_in:
    # Login page
    row_input = st.columns((3, 3, 2))
    with row_input[1]:
        st.title("Welcome to MUN Connect")
    row_input = st.columns((5, 2, 5))
    with row_input[1]:
        username = st.text_input("Username", max_chars=20, placeholder="Enter your username")
    row_input = st.columns((5, 2, 5))
    with row_input[1]:
        password = st.text_input("Password", type="password", max_chars=20, placeholder="Enter your password")
    row_input = st.columns((5, 2, 5))
    with row_input[1]:
        login_button = st.button("Login")

    if login_button:
        # Mock credentials for demonstration
        USER_CREDENTIALS = {"user": "user123", "admin": "admin123"}
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.current_page = "Home"  # Redirect to Home on login
            st.rerun()
        else:
            row_input = st.columns((3, 3, 2))
            with row_input[1]:
                st.error("Invalid username or password!")
else:
    # Display custom sidebar and get the selected script
    selected_script = custom_sidebar()

    try:
        # Dynamically load the selected page script
        page_module = importlib.import_module(selected_script)
        page_module.show_page()
    except ModuleNotFoundError:
        st.error(f"Page `{selected_script}` not found. Please check your configuration.")
    except Exception as e:
        st.error(f"An error occurred while loading `{selected_script}`: {e}")