from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import psycopg2
from passlib.context import CryptContext

# FastAPI instance
app = FastAPI()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# PostgreSQL Database Connection
DB_CONFIG = {
    "host" : "localhost",
    "database" : "sql_project_p3",
    "user" : "postgres",
    "password" : "admin123"
}

def get_db_connection():
    """Establish connection to PostgreSQL"""
    return psycopg2.connect(**DB_CONFIG)


# ------------------------- Models ------------------------- #
class LoginRequest(BaseModel):
    username: str
    password: str

class IssueBookRequest(BaseModel):
    issued_id: str
    member_id: str
    book_isbn: str
    employee_id: str

class ReturnBookRequest(BaseModel):
    return_id: str
    issued_id: str


# ------------------------- API Endpoints ------------------------- #

@app.post("/login_page")
def employee_login(request: LoginRequest):
    """Login Page API Endpoint"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT emp_id, password_hash FROM employees WHERE user_name = %s", (request.username,))
        employee = cursor.fetchone()
        cursor.close()
        conn.close()

        return {"message": f"Successfully Login, Employee ID = {employee[0]}"}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/issue_book")
def issue_book(request: IssueBookRequest):
    """Issue a book by calling stored procedure add_issue_book()"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Fetch book title and status
        cursor.execute("SELECT book_title, status FROM books WHERE isbn = %s", 
                    (request.book_isbn,)) 
        book_title = cursor.fetchone()

        # If book not found in the database
        if not book_title:
            cursor.close()
            conn.close()
            return {"message": "Book not found in the database"}

        # Check if book is available
        if book_title[1] == 'yes':
            cursor.execute("CALL add_issue_book(%s, %s, %s, %s)", 
                        (request.issued_id, request.member_id, request.book_isbn, request.employee_id))
            conn.commit()
            message = f"The Book **{book_title[0]}** Issued Successfully"

        else:
            message = f"Currently Unavailable The Book: **{book_title[0]}**"

        # Close connection **after** all operations
        cursor.close()
        conn.close()
        return {"message": message}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.post("/return_book")
def return_book(request: ReturnBookRequest):
    """Return a book by calling stored procedure add_return_status()"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("CALL add_return_status(%s, %s)", 
                       (request.return_id, request.issued_id))
        
        # Fetch book title
        cursor.execute("SELECT issued_book_name FROM issued_status WHERE issued_id = %s", 
                    (request.issued_id,))  
        book_title = cursor.fetchone()

        conn.commit()

        cursor.close()
        conn.close()
        
        return {"message": f"The Book **{book_title[0]}** returned successfully"}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/book_status/{book_isbn}")
def get_book_status(book_isbn: str):
    """Check if a book is available or not"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT status, book_title FROM books WHERE isbn = %s", (book_isbn,))
        book_status = cursor.fetchone()
        
        cursor.close()
        conn.close()
        
        if book_status[0] == 'yes':
            return {'status': f"The Book **{book_status[1]}** Available"}  # 'available' or 'not available'
        
        elif book_status[0] == 'no':
            return {'status': f"The Book **{book_status[1]}** is Not Available"} # default status if book is not found
        
        else:
            raise HTTPException(status_code=404, detail="Book not found")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
