import streamlit_authenticator as stauth
import streamlit as st
from config.Settings import UseSettings

class Auth:
    @staticmethod
    def __create_auth():
        settings = UseSettings.get_settings()
        authenticator = stauth.Authenticate(
            settings.USERS,
            "my_cookie_name", 
            "my_signature_key", 
            cookie_expiry_days=0
        )
        return authenticator
    
    @staticmethod
    def is_auth():
        return st.session_state.get("authentication_status")

    @staticmethod
    def login_page():
        authenticator = Auth.__create_auth()
        authenticator.login(location='main')

    @staticmethod
    def logout_page():
        authenticator = Auth.__create_auth()
        authenticator.logout("Logout")

    @staticmethod
    def auth_page(pages):
        if Auth.is_auth():
            with st.container():
                _, col2 = st.columns([85, 15])
                with col2:
                    Auth.logout_page()
                pg = st.navigation(pages)
                pg.run()
        else:
            Auth.login_page()

