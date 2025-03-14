from src.db_connector import connect_db


# Connect to the database
conn = connect_db()
if conn:
    cursor = conn.cursor()

    # Fetch expenses (test query)
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()

    # Display results
    print("📊 Expense Records:")
    for expense in expenses:
        print(expense)

    # Close connection
    cursor.close()
    conn.close()
else:
    print("Unable to connect to database.")
