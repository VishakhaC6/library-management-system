from app.database import get_connection

# Add a book
def add_book(title, author, isbn, available_copies):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = """
            INSERT INTO books (title, author, isbn, available_copies)
            VALUES (?, ?, ?, ?)
            """
            cursor.execute(query, (title, author, isbn, available_copies))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error adding book: {e}")
            return False
        finally:
            conn.close()
    return False

# Get all books
def get_all_books():
    conn = get_connection()
    books = []
    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM books"
            cursor.execute(query)
            books = [
                {
                    "id": row.id,
                    "title": row.title,
                    "author": row.author,
                    "isbn": row.isbn,
                    "available_copies": row.available_copies,
                }
                for row in cursor.fetchall()
            ]
        except Exception as e:
            print(f"Error retrieving books: {e}")
        finally:
            conn.close()
    return books

# Add a user
def add_user(name, email, password):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = """
            INSERT INTO users (name, email, password)
            VALUES (?, ?, ?)
            """
            cursor.execute(query, (name, email, password))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error adding user: {e}")
            return False
        finally:
            conn.close()
    return False

def get_user_history_requests(user_id):
    conn = get_connection()
    borrow_requests = []
    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM borrow_history where user_id=?"
            cursor.execute(query,(user_id))
            borrow_requests = [
                {
                    "id": row.id,
                    "user_id": row.user_id,
                    "book_id": row.book_id,
                    "borrow_start_date": row.borrow_start_date,
                    "borrow_end_date": row.borrow_end_date,
                    "status": row.status,
                }
                for row in cursor.fetchall()
            ]
        except Exception as e:
            print(f"Error retrieving borrow requests: {e}")
        finally:
            conn.close()
    return borrow_requests

# Get all borrow requests
def get_all_borrow_requests():
    conn = get_connection()
    borrow_requests = []
    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM borrow_history"
            cursor.execute(query)
            borrow_requests = [
                {
                    "id": row.id,
                    "user_id": row.user_id,
                    "book_id": row.book_id,
                    "borrow_start_date": row.borrow_start_date,
                    "borrow_end_date": row.borrow_end_date,
                    "status": row.status,
                }
                for row in cursor.fetchall()
            ]
        except Exception as e:
            print(f"Error retrieving borrow requests: {e}")
        finally:
            conn.close()
    return borrow_requests


def create_borrow_req(user_id,book_id,borrow_from,borrow_till):
    conn=get_connection()
    if conn:
        try:
            cursor=conn.cursor()
            query=f"""INSERT INTO borrow_history (user_id, book_id, borrow_start_date, borrow_end_date, status)
            VALUES ({user_id}, {book_id}, '{borrow_from}', '{borrow_till}', 'pending')"""
            cursor.execute(query)
            conn.commit()
            return True
        except Exception as e:
            print(f"error sending request")
        finally:
            conn.close()
    return False

def update_borrow_request_status(request_id, status):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = """
            UPDATE borrow_history
            SET status = ?
            WHERE id = ?
            """
            cursor.execute(query, (status, request_id))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error updating borrow request status: {e}")
            return False
        finally:
            conn.close()
    return False

def approve_borrow_request(request_id):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = """
            UPDATE borrow_history
            SET status = 'Approved'
            WHERE id = ?
            """
            cursor.execute(query, (request_id,))
            if cursor.rowcount > 0:  # Check if any row was updated
                conn.commit()
                return True
            return False
        except Exception as e:
            print(f"Error approving borrow request: {e}")
            return False
        finally:
            conn.close()
    return False

# Deny a borrow request
def deny_borrow_request(request_id):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = """
            UPDATE borrow_history
            SET status = 'Denied'
            WHERE id = ?
            """
            cursor.execute(query, (request_id,))
            if cursor.rowcount > 0:  # Check if any row was updated
                conn.commit()
                return True
            return False
        except Exception as e:
            print(f"Error denying borrow request: {e}")
            return False
        finally:
            conn.close()
    return False