from fastapi import APIRouter
from src.models import Expense
from src.storage import expenses, save_expenses

router = APIRouter()

@router.post("/expenses")
def add_expense(expense: Expense):
    expenses.append(expense.model_dump(mode="json"))
    save_expenses(expenses)
    return {
        "message": "Expense added successfully",
        "expense": expense
    }
@router.get("/expenses")
def get_expenses():
    return expenses
@router.get("/expenses/category/{category}")
def get_expenses_by_category(category: str):
    filtered_expenses = []

    for expense in expenses:
        if expense["category"].lower() == category.lower():
            filtered_expenses.append(expense)

    return filtered_expenses
@router.get("/expenses/total")
def get_total_expenses():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return {"total_expenses": total}
@router.delete("/expenses/{id}")
def delete_expense(id: int):
    for expense in expenses:
        if expense["id"] == id:
            expenses.remove(expense)
            save_expenses(expenses)

            return {"message": "Expense deleted successfully"}

    return {"message": "Expense not found"}