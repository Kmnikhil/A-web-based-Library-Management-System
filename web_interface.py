import streamlit as st
from passlib.context import CryptContext
import requests


# FastAPI backend URL
API_URL = "http://127.0.0.1:8000"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Streamlit UI
st.title("📚 Library Management System")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.subheader("Employee Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        payload = {
            "username": username,
            "password": password
        }
        response = requests.post(f"{API_URL}/login_page", json=payload)
        # st.success(response.json()["message"]) if response.status_code == 200 else st.error(response.json()["error"])

        if response.status_code == 200:
            st.session_state.logged_in = True
            st.success("Login Successful")
            st.rerun()
        else:
            st.error("Invalid Credentials")

else:
    action = st.selectbox("Select Action", ["Issue a Book", "Return a Book", "Check Book Status"])
    if action == "Issue a Book":
        st.subheader("📖 Issue a Book")
        issued_id = st.text_input("Issued ID")
        member_id = st.text_input("Member ID")
        book_isbn = st.text_input("Book ISBN")
        employee_id = st.text_input("Employee ID")

        if st.button("Issue Book"):
            payload = {
                "issued_id": issued_id,
                "member_id": member_id,
                "book_isbn": book_isbn,
                "employee_id": employee_id
            }
            response = requests.post(f"{API_URL}/issue_book", json=payload)
            st.success(response.json()["message"]) if response.status_code == 200 else st.error(response.json()["error"])


    elif action == "Return a Book":
        st.subheader("🔄 Return a Book")
        return_id = st.text_input("Return ID")
        issued_id = st.text_input("Issued ID")

        if st.button("Return Book"):
            payload = {
                "return_id": return_id,
                "issued_id": issued_id
            }
            response = requests.post(f"{API_URL}/return_book", json=payload)
            st.success(response.json()["message"]) if response.status_code == 200 else st.error(response.json()["error"])

    elif action == "Check Book Status":
        st.subheader("✅ Check Book Status")
        book_isbn = st.text_input("Enter Book ISBN")

        if st.button("Check Status"):
            response = requests.get(f"{API_URL}/book_status/{book_isbn}")
            if response.status_code == 200:
                st.info(f"Book Status: {response.json()['status']}")
            else:
                st.error(response.json()["error"])

