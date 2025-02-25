# 📚 **Library Management System**  
A web-based Library Management System built using **FastAPI**, **PostgreSQL**, and **Streamlit** to manage book issuing, returns, and status updates efficiently.  

---

## 📌 **Project Overview**

This Library Management System is a web-based application built using **FastAPI**, **PostgreSQL**, and **Streamlit**. It allows library staff to **Issue Books, Return Books, and Check Book Status** seamlessly through an interactive interface.

## 🔗 **Reference Repository**

This project builds on a previous SQL-based implementation where the **database, tables, and stored procedures** were initially created. You can check out that repository here: 👉 [**Library Management System (SQL Version)**](your-repo-link-here)

---

## 🚀 **Features**

- ✅ **Employee Authentication** (Login System for Library Staff)
- 📘 **Book Issuing & Returning** (Stored procedures to handle transactions)
- 📊 **Book Availability Check** (Real-time book status updates)
- 🌐 **User-Friendly Web Interface** (Built with Streamlit)
- 🔄 **FastAPI Backend** (Handles API requests efficiently)

---

The backend is powered by **FastAPI**, handling API requests and communicating with a **PostgreSQL database**. The frontend is built using **Streamlit**, providing an interactive and user-friendly interface.

**Login Page :** 
![login](https://github.com/user-attachments/assets/985f44d8-eb09-4d0d-94b2-86bdd215b8ab)
**After Login :** 
![image](https://github.com/user-attachments/assets/78beba09-112b-494d-a87b-62561830877c)

---

## 🛠 **Tech Stack**  
🔹 **Backend:** FastAPI (Python)  
🔹 **Frontend:** Streamlit  
🔹 **Database:** PostgreSQL (with Stored Procedures)  
🔹 **Authentication:** bcrypt (password hashing)  
🔹 **Deployment:** Local system (GitHub for version control)  

---

## 📂 **Project Structure**

```
📁 library-management-system
│-- 📄 api.py              # FastAPI backend (Handles authentication & book transactions)
│-- 📄 creating_store_procedures.sql # SQL procedures for book issuing/return
│-- 📄 web_interface.py    # Streamlit frontend (User interface for library staff)
│-- 📄 requirements.txt    # Dependencies
│-- 📄 README.md           # Project documentation
```


---

## 🎯 **Features & Functionality**  
🔹 **Employee Authentication** – Secure login system for library staff.  
🔹 **Book Issuing & Returning** – Automatic updates using PostgreSQL stored procedures.  
🔹 **Book Availability Status** – Check if a book is available before issuing.  
🔹 **Fast & Interactive UI** – Built with Streamlit for a smooth experience.  

---

## 🚀 **How to Run the Project Locally**  
1️⃣ Clone the repository:  
   ```sh
   git clone https://github.com/Kmnikhil/A-web-based-Library-Management-System.git
   ```
2️⃣ Install dependencies:  
   ```sh
   pip install -r requirements.txt
   ```
3️⃣ Start the FastAPI backend:  
   ```sh
   uvicorn api_file:app --reload
   ```
4️⃣ Run the Streamlit frontend:  
   ```sh
   streamlit run web_interface.py
   ```
---

## 🎯 **Usage**

1️⃣ **Login as a Library Employee** using your credentials.\
2️⃣ **Select an Action** (Issue Book, Return Book, Check Status).\
3️⃣ **Enter Required Details** and submit.\
4️⃣ **View the Response** (Book issued/returned or availability status).

---

## 🎯 **Future Enhancements**  
✅ Add a **book search feature** using filters.  
✅ Implement **email notifications** for overdue books.  
✅ Deploy the project to **a cloud database & hosting service**.  

---

### **📌 Contributing**  
Contributions are welcome! Feel free to fork the repo and submit pull requests.  
