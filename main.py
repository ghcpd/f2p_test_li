"""
Personal Finance Management System - Main Program Entry Point
Demonstrates basic functionality, intentionally missing advanced features and complete error handling
"""

import sys
import os
from decimal import Decimal

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from account import AccountManager, AccountType
from transaction import TransactionManager, TransactionType
from budget import BudgetManager, BudgetPeriod


def demo_accounts():
    """Demonstrate account management functionality"""
    print("=== Account Management Demo ===")
    account_mgr = AccountManager()
    
    # Create different types of accounts
    checking = account_mgr.create_account("Main Checking Account", AccountType.CHECKING, Decimal('5000'))
    savings = account_mgr.create_account("Savings Account", AccountType.SAVINGS, Decimal('10000'))
    
    print(f"Created account: {checking}")
    print(f"Created account: {savings}")
    
    # Basic operations demonstration
    checking.deposit(Decimal('1000'))
    print(f"Balance after deposit: ${checking.balance}")
    
    checking.withdraw(Decimal('500'))
    print(f"Balance after withdrawal: ${checking.balance}")
    
    print(f"Total assets: ${account_mgr.get_total_balance()}")
    
    return account_mgr


def demo_transactions(account_mgr):
    """Demonstrate transaction recording functionality"""
    print("\n=== Transaction Recording Demo ===")
    transaction_mgr = TransactionManager()
    
    # Add some transaction records
    checking_account = account_mgr.accounts[0]  # Get first account
    
    transaction_mgr.add_transaction(
        checking_account.id, 
        Decimal('2500'), 
        TransactionType.INCOME, 
        "Salary Income"
    )
    
    transaction_mgr.add_transaction(
        checking_account.id,
        Decimal('500'),
        TransactionType.EXPENSE,
        "Grocery Shopping"
    )
    
    transaction_mgr.add_transaction(
        checking_account.id,
        Decimal('1200'),
        TransactionType.EXPENSE,
        "Rent Payment"
    )
    
    # Display recent transactions
    print("Recent transaction records:")
    recent_transactions = transaction_mgr.get_recent_transactions(5)
    for t in recent_transactions:
        print(f"  {t.date.strftime('%Y-%m-%d')} - {t.transaction_type.value}: ${t.amount} ({t.description})")
    
    return transaction_mgr


def demo_budgets():
    """Demonstrate budget management functionality"""
    print("\n=== Budget Management Demo ===")
    budget_mgr = BudgetManager()
    
    # Create budgets
    groceries = budget_mgr.create_budget("Groceries", "Food", Decimal('800'), BudgetPeriod.MONTHLY)
    rent = budget_mgr.create_budget("Rent", "Housing", Decimal('1500'), BudgetPeriod.MONTHLY)
    entertainment = budget_mgr.create_budget("Entertainment", "Entertainment", Decimal('300'), BudgetPeriod.MONTHLY)
    
    print(f"Created budget: {groceries.name} - ${groceries.amount}/{groceries.period.value}")
    print(f"Created budget: {rent.name} - ${rent.amount}/{rent.period.value}")
    print(f"Created budget: {entertainment.name} - ${entertainment.amount}/{entertainment.period.value}")
    
    print(f"Monthly budget total: ${budget_mgr.get_total_budget_amount()}")
    
    return budget_mgr


def demo_api_info():
    """Demonstrate API information"""
    print("\n=== API Interface Information ===")
    print("This project includes a complete FastAPI REST interface:")
    print("- 🚀 Start API server: python start_api.py")
    print("- 🌐 User-friendly interface: http://localhost:8000/")
    print("- 📚 API technical documentation: http://localhost:8000/docs")
    print("- ❤️ Health check: http://localhost:8000/health")
    print("- 🔧 Core features: Account management, transaction recording, budget management")
    print("💡 Tip: API server supports automatic port detection, will try other ports if 8000 is occupied")


def main():
    """Main function"""
    print("🏦 Welcome to Personal Finance Management System!")
    print("This is a feature-incomplete demo program including account, transaction and budget management.\n")
    
    try:
        account_mgr = demo_accounts()
        transaction_mgr = demo_transactions(account_mgr)
        budget_mgr = demo_budgets()
        demo_api_info()
        
    except Exception as e:
        # Simple exception handling, missing detailed error classification and handling
        print(f"❌ Program execution error: {e}")
        return
    
    print("\n✅ Program demo completed!")
    print("\n📝 Features to be added:")
    print("- Delete account functionality")
    print("- Monthly summary functionality")
    print("- Data persistence storage")
    print("- User authentication and authorization")


if __name__ == "__main__":
    main()