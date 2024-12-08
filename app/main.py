
from fastapi import FastAPI, HTTPException
from app.database import get_connection
from app.crud import *

app = FastAPI()

@app.post("/add_book/")
def add_book_endpoint(title: str, author: str, isbn: str, available_copies: int):
    if add_book(title, author, isbn, available_copies):
        return {"message": f"Book '{title}' added successfully!"}
    else:
        raise HTTPException(status_code=500, detail="Failed to add the book.")

@app.get("/books/")
def get_books_endpoint():
    books = get_all_books()
    if books:
        return {"books": books}
    else:
        return {"message": "No books found."}

@app.post("/add_user/")
def add_user_endpoint(name: str, email: str, password: str):
    if add_user(name, email, password):
        return {"message": f"User '{name}' added successfully!"}
    else:
        raise HTTPException(status_code=500, detail="Failed to add the user.")

@app.get("/borrow_requests_history/")
def get_borrow_requests_endpoint():
    borrow_requests = get_all_borrow_requests()
    if borrow_requests:
        return {"borrow_requests": borrow_requests}
    else:
        return {"message": "No borrow requests found."}

@app.get("/user_history/")
def get_user_history_endpoint(user_id:int):
    borrow_requests = get_user_history_requests(user_id)
    if borrow_requests:
        return {"borrow_requests": borrow_requests}
    else:
        return {"message": "No borrow requests found."}
    
@app.post("/borrow_request/")
def create_borrow_req_endpoit(user_id:int,book_id:int,borrow_from:str,borrow_till:str):
    if create_borrow_req(user_id,book_id,borrow_from,borrow_till):
        return{"Borrow request send successfully!"}
    else:
        raise HTTPException(status_code=500, detail="Failed to send the request.")

@app.patch("/approve_request/")
def approve_request_endpoint(request_id: int):
    if approve_borrow_request(request_id):
        return {"message": f"Borrow request ID {request_id} approved successfully!"}
    else:
        raise HTTPException(status_code=500, detail="Failed to approve the borrow request.")

@app.patch("/deny_request/")
def deny_request_endpoint(request_id: int):
    if deny_borrow_request(request_id):
        return {"message": f"Borrow request ID {request_id} denied successfully!"}
    else:
        raise HTTPException(status_code=500, detail="Failed to deny the borrow request.")
