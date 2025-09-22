"""
pytest tests for transaction recording module
Intentionally includes only basic tests, missing boundary tests and complex scenario tests
"""

import pytest
from decimal import Decimal
from datetime import datetime

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from transaction import Transaction, TransactionManager, TransactionType


class TestTransaction:
    """Basic tests for Transaction class"""
    
    def test_create_transaction_basic(self):
        """Test basic transaction creation"""
        transaction = Transaction(
            id=1,
            account_id=1,
            amount=Decimal('100'),
            transaction_type=TransactionType.EXPENSE,
            description="Groceries"
        )
        assert transaction.id == 1
        assert transaction.account_id == 1
        assert transaction.amount == Decimal('100')
        assert transaction.transaction_type == TransactionType.EXPENSE
        assert transaction.description == "Groceries"
        assert isinstance(transaction.date, datetime)
    
    def test_transaction_auto_date(self):
        """Test transaction auto-sets date"""
        transaction = Transaction(account_id=1, amount=Decimal('50'))
        assert transaction.date is not None
        assert isinstance(transaction.date, datetime)


class TestTransactionManager:
    """Basic tests for TransactionManager class"""
    
    def setup_method(self):
        """Setup before each test"""
        self.manager = TransactionManager()
    
    def test_add_transaction_success(self):
        """Test successful transaction addition"""
        transaction = self.manager.add_transaction(
            account_id=1,
            amount=Decimal('100'),
            transaction_type=TransactionType.EXPENSE,
            description="Test expense"
        )
        assert transaction.id == 1
        assert transaction.account_id == 1
        assert transaction.amount == Decimal('100')
        assert len(self.manager.transactions) == 1
    
    def test_add_transaction_zero_amount(self):
        """Test adding zero amount transaction"""
        with pytest.raises(ValueError, match="Transaction amount must be positive"):
            self.manager.add_transaction(1, Decimal('0'), TransactionType.EXPENSE)
    
    def test_add_transaction_negative_amount(self):
        """Test adding negative amount transaction"""
        with pytest.raises(ValueError, match="Transaction amount must be positive"):
            self.manager.add_transaction(1, Decimal('-50'), TransactionType.EXPENSE)
    
    def test_get_transactions_by_account(self):
        """Test getting transactions by account"""
        # Add transactions for different accounts
        self.manager.add_transaction(1, Decimal('100'), TransactionType.EXPENSE)
        self.manager.add_transaction(2, Decimal('200'), TransactionType.INCOME)
        self.manager.add_transaction(1, Decimal('50'), TransactionType.EXPENSE)
        
        account_1_transactions = self.manager.get_transactions_by_account(1)
        assert len(account_1_transactions) == 2
        assert all(t.account_id == 1 for t in account_1_transactions)
    
    def test_get_recent_transactions(self):
        """Test getting recent transactions"""
        # Add multiple transactions
        for i in range(15):
            self.manager.add_transaction(1, Decimal('10'), TransactionType.EXPENSE)
        
        recent = self.manager.get_recent_transactions(5)
        assert len(recent) == 5
        
        # Verify sorted by time in descending order
        for i in range(len(recent) - 1):
            assert recent[i].date >= recent[i + 1].date
    
    def test_get_recent_transactions_default_limit(self):
        """Test getting recent transactions with default limit"""
        # Add 15 transactions
        for i in range(15):
            self.manager.add_transaction(1, Decimal('10'), TransactionType.EXPENSE)
        
        recent = self.manager.get_recent_transactions()
        assert len(recent) == 10  # Default limit is 10