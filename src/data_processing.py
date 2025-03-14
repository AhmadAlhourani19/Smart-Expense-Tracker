import pandas as pd
from src.db_connector import connect_db

def fetch_expenses():
    """Fetch all expenses from the database and return as a Pandas DataFrame."""
    conn = connect_db()
    if not conn:
        print("❌ Database connection failed.")
        return None

    query = "SELECT id, date, category, amount, description FROM expenses"
    df = pd.read_sql(query, conn)  # Convert MySQL query result into DataFrame
    conn.close()
    return df

def categorize_expenses(df):
    """Add a new column to categorize expenses based on predefined rules."""
    categories = {
        "Groceries": ["grocery", "supermarket", "food"],
        "Transport": ["bus", "train", "uber", "taxi", "fuel"],
        "Entertainment": ["movie", "concert", "game", "netflix"],
        "Bills": ["electricity", "water", "internet", "phone"]
    }

    def categorize(row):
        for category, keywords in categories.items():
            if any(keyword in row["description"].lower() for keyword in keywords):
                return category
        return "Other"

    df["Category"] = df.apply(categorize, axis=1)
    return df

def summarize_expenses(df):
    """Generate basic summary statistics for expenses."""
    summary = df.groupby("Category")["amount"].sum().reset_index()
    summary = summary.sort_values(by="amount", ascending=False)
    return summary

if __name__ == "__main__":
    # Fetch expenses from database
    expenses_df = fetch_expenses()
    
    if expenses_df is not None:
        print("\n📊 Raw Expenses Data:")
        print(expenses_df.head())

        # Categorize expenses
        categorized_df = categorize_expenses(expenses_df)
        print("\n📌 Categorized Expenses:")
        print(categorized_df.head())

        # Summarize expenses
        summary_df = summarize_expenses(categorized_df)
        print("\n💰 Expense Summary:")
        print(summary_df)
