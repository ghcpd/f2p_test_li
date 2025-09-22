"""
Personal Finance Management System - Account Management Module
Intentionally implements only basic functionality, missing advanced features
"""

from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import Optional, List


class AccountType(Enum):
    """Account types"""
    CHECKING = "checking"      # Checking account
    SAVINGS = "savings"        # Savings account
    CREDIT = "credit"          # Credit card account
    INVESTMENT = "investment"  # Investment account


class Account:
    """Bank account class"""
    
    def __init__(self, name: str, account_type: AccountType, initial_balance: Decimal = Decimal('0')):
        self.id = None  # Will be assigned by AccountManager
        self.name = name
        self.account_type = account_type
        self.balance = initial_balance
        self.created_at = datetime.now()
        self.is_active = True
        
    def deposit(self, amount: Decimal) -> Decimal:
        """Make a deposit"""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount: Decimal) -> Decimal:
        """Make a withdrawal"""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance
    
    def get_balance(self) -> Decimal:
        """Get current balance"""
        return self.balance
    
    def __str__(self):
        return f"Account({self.name}, {self.account_type.value}, ${self.balance})"


class AccountManager:
    """Account manager, functionality intentionally incomplete"""
    
    def __init__(self):
        self.accounts: List[Account] = []
        self.next_id = 1
    
    def create_account(self, name: str, account_type: AccountType, 
                      initial_balance: Decimal = Decimal('0')) -> Account:
        """Create new account"""
        # Simple duplicate name check
        if any(acc.name == name for acc in self.accounts):
            raise ValueError(f"Account with name '{name}' already exists")
        
        account = Account(name, account_type, initial_balance)
        account.id = self.next_id
        self.next_id += 1
        
        self.accounts.append(account)
        return account
    
    def get_account_by_id(self, account_id: int) -> Optional[Account]:
        """Get account by ID"""
        for account in self.accounts:
            if account.id == account_id:
                return account
        return None
    
    def get_total_balance(self) -> Decimal:
        """Get total balance of all accounts"""
        return sum(acc.balance for acc in self.accounts if acc.is_active)
    
    def delete_account(self, account_id: int) -> bool:
        """
        Delete an account by ID
        
        Args:
            account_id: The ID of the account to delete
            
        Returns:
            bool: True if account was deleted successfully, False if account not found
            
        Raises:
            ValueError: If account has a non-zero balance
        """
        account = self.get_account_by_id(account_id)
        if account is None:
            return False
            
        # Check if account has zero balance before deletion
        if account.balance != Decimal('0'):
            raise ValueError(f"Cannot delete account with non-zero balance: ${account.balance}")
            
        # Remove account from the list
        self.accounts = [acc for acc in self.accounts if acc.id != account_id]
        return True
    
    # TODO: Need to add the following features:
    # - update_account(account_id, **kwargs): Update account information
    # - get_accounts_by_type(account_type): Filter accounts by type
    # - transfer_funds(from_id, to_id, amount): Transfer between accounts
    # - deactivate_account(account_id): Deactivate account
    # - get_account_history(account_id): Get account history
    # - export_accounts(): Export account data
    # - import_accounts(): Import account data
    # - calculate_interest(): Calculate interest
    # - set_credit_limit(): Set credit limit