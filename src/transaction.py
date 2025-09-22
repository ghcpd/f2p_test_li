"""
Personal Finance Management System - Transaction Recording Module
Intentionally implements only basic functionality, missing categorization, statistics and advanced query features
"""

from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import Optional, List
from dataclasses import dataclass


class TransactionType(Enum):
    """Transaction types"""
    INCOME = "income"      # Income
    EXPENSE = "expense"    # Expense
    TRANSFER = "transfer"  # Transfer


@dataclass
class Transaction:
    """Transaction record"""
    id: Optional[int] = None
    account_id: int = 0
    amount: Decimal = Decimal('0')
    transaction_type: TransactionType = TransactionType.EXPENSE
    description: str = ""
    date: datetime = None
    
    def __post_init__(self):
        if self.date is None:
            self.date = datetime.now()


class TransactionManager:
    """Transaction manager, functionality intentionally incomplete"""
    
    def __init__(self):
        self.transactions: List[Transaction] = []
        self.next_id = 1
    
    def add_transaction(self, account_id: int, amount: Decimal, 
                       transaction_type: TransactionType, description: str = "") -> Transaction:
        """Add transaction record"""
        if amount <= 0:
            raise ValueError("Transaction amount must be positive")
        
        transaction = Transaction(
            id=self.next_id,
            account_id=account_id,
            amount=amount,
            transaction_type=transaction_type,
            description=description
        )
        
        self.next_id += 1
        self.transactions.append(transaction)
        return transaction
    
    def get_transactions_by_account(self, account_id: int) -> List[Transaction]:
        """Get transaction records for specified account"""
        return [t for t in self.transactions if t.account_id == account_id]
    
    def get_recent_transactions(self, limit: int = 10) -> List[Transaction]:
        """Get recent transaction records"""
        sorted_transactions = sorted(self.transactions, key=lambda t: t.date, reverse=True)
        return sorted_transactions[:limit]
    
    # TODO: Need to add the following features:
    # - delete_transaction(transaction_id): Delete transaction record
    # - update_transaction(transaction_id, **kwargs): Update transaction record
    # - get_transactions_by_type(transaction_type): Filter transactions by type
    # - get_transactions_by_date_range(start_date, end_date): Filter by date range
    # - add_transaction_category(): Add transaction categorization feature
    # - calculate_monthly_summary(): Calculate monthly income/expense summary
    # - calculate_category_totals(): Calculate totals by category
    # - search_transactions(query): Search transaction records
    # - export_transactions(): Export transaction data
    # - import_transactions(): Import transaction data
    # - duplicate_transaction(): Duplicate transaction record
    # - add_recurring_transactions(): Add recurring transactions
    # - generate_reports(): Generate financial reports