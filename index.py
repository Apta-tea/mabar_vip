import streamlit as st
from streamlit_option_menu import option_menu
from utils import login, is_authenticated
from user import _profile_content
from dashboard import _dashboard_content
from member import _member_content
from mabar import _mabar_content

def main():
    st.set_page_config(page_title="Mabar", layout="wide")
    
    # Session state initialization
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    
    # Authentication check
    if not st.session_state.authenticated:
        show_login_page()
    else:
        show_dashboard()

def show_login_page():
    st.title("Login Page")

    with st.form(key='login_form'):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit_button = st.form_submit_button(label='Login')

        if submit_button:
            login(st.session_state, username, password)
            if st.session_state.authenticated:
                st.success("Login successful!")
                st.rerun()  # Redirect to dashboard
            else:
                st.error("Invalid credentials")

def show_dashboard():
    #st.title("Mabar :red[coeg] :sunglasses: ")

    # Side menu
    with st.sidebar:
        selected = option_menu(
            "Menu Utama",
            options=["Beranda", "Admin", "Member","Mabar", "Logout"],
            icons=["house", "gear", "person", "list-task", "log-out"],
            default_index=0,
        )

        if selected == "Logout":
            st.session_state.authenticated = False
            st.rerun()  # Redirect to login page

    # Content based on selection
    if selected == "Beranda":
        _dashboard_content()
    elif selected == "Admin":
        _profile_content()
    elif selected == "Member":
        _member_content()
    elif selected == "Mabar":
        _mabar_content()
    
main()
