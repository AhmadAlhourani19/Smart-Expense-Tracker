import streamlit as st
import pandas as pd
from src.db_connector import connect_db
from src.expense_manager import add_expense, update_expense, delete_expense
from src.data_processing import fetch_expenses, categorize_expenses, summarize_expenses

st.title("💰 Smart Expense Tracker")
st.write("Track, analyze, and manage your expenses easily.")

# Fetch expenses from database
expenses_df = fetch_expenses()

if expenses_df is not None:
    # Categorize expenses
    categorized_df = categorize_expenses(expenses_df)

    # Display expenses
    st.subheader("📊 Expense Records")
    st.dataframe(categorized_df)

    # Summarize expenses
    st.subheader("💡 Expense Summary")
    summary_df = summarize_expenses(categorized_df)
    st.dataframe(summary_df)

# Add a new expense
st.subheader("➕ Add a New Expense")
with st.form(key="expense_form"):
    date = st.date_input("Date")
    category = st.text_input("Category")
    amount = st.number_input("Amount", min_value=0.0, format="%.2f")
    description = st.text_area("Description")
    submit = st.form_submit_button("Add Expense")

    if submit:
        add_expense(str(date), category, amount, description)
        st.success("✅ Expense added successfully!")
        st.experimental_rerun()

# Delete an expense
st.subheader("❌ Delete an Expense")
expense_id = st.number_input("Enter Expense ID to Delete", min_value=1, step=1)
if st.button("Delete Expense"):
    delete_expense(expense_id)
    st.warning("⚠ Expense deleted!")
    st.experimental_rerun()
