from src.db_connector import connect_db

def add_expense(date, category, amount, description):
    """Insert a new expense into the database."""
    conn = connect_db()
    if not conn:
        print("Database connection failed.")
        return

    cursor = conn.cursor()
    query = "INSERT INTO expenses (date, category, amount, description) VALUES (%s, %s, %s, %s)"
    values = (date, category, amount, description)
    
    try:
        cursor.execute(query, values)
        conn.commit()
        print("Expense added successfully!")
    except Exception as e:
        print(f"Error adding expense: {e}")
    finally:
        cursor.close()
        conn.close()

def update_expense(expense_id, category, amount, description):
    """Update an existing expense."""
    conn = connect_db()
    if not conn:
        print("Database connection failed.")
        return

    cursor = conn.cursor()
    query = "UPDATE expenses SET category = %s, amount = %s, description = %s WHERE id = %s"
    values = (category, amount, description, expense_id)
    
    try:
        cursor.execute(query, values)
        conn.commit()
        print("Expense updated successfully!")
    except Exception as e:
        print(f"Error updating expense: {e}")
    finally:
        cursor.close()
        conn.close()

def delete_expense(expense_id):
    """Delete an expense from the database."""
    conn = connect_db()
    if not conn:
        print("Database connection failed.")
        return

    cursor = conn.cursor()
    query = "DELETE FROM expenses WHERE id = %s"
    values = (expense_id,)
    
    try:
        cursor.execute(query, values)
        conn.commit()
        print("Expense deleted successfully!")
    except Exception as e:
        print(f"Error deleting expense: {e}")
    finally:
        cursor.close()
        conn.close()