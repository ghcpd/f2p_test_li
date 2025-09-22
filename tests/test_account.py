"""
pytest tests for account management module
Intentionally includes only basic tests, missing boundary tests, exception tests and integration tests
"""

import pytest
from decimal import Decimal
from datetime import datetime

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from account import Account, AccountManager, AccountType


class TestAccount:
    """Basic tests for Account class"""
    
    def test_create_account_basic(self):
        """Test basic account creation"""
        account = Account("Main Checking", AccountType.CHECKING, Decimal('1000'))
        assert account.name == "Main Checking"
        assert account.account_type == AccountType.CHECKING
        assert account.balance == Decimal('1000')
        assert account.is_active is True
        assert isinstance(account.created_at, datetime)
    
    def test_deposit_positive_amount(self):
        """Test deposit functionality"""
        account = Account("Test Account", AccountType.SAVINGS)
        new_balance = account.deposit(Decimal('500'))
        assert account.balance == Decimal('500')
        assert new_balance == Decimal('500')
    
    def test_withdraw_sufficient_funds(self):
        """Test withdrawal functionality - sufficient funds"""
        account = Account("Test Account", AccountType.CHECKING, Decimal('1000'))
        new_balance = account.withdraw(Decimal('300'))
        assert account.balance == Decimal('700')
        assert new_balance == Decimal('700')
    
    def test_withdraw_insufficient_funds(self):
        """Test withdrawal functionality - insufficient funds"""
        account = Account("Test Account", AccountType.CHECKING, Decimal('100'))
        with pytest.raises(ValueError, match="Insufficient funds"):
            account.withdraw(Decimal('200'))


class TestAccountManager:
    """Basic tests for AccountManager class"""
    
    def setup_method(self):
        """Setup before each test"""
        self.manager = AccountManager()
    
    def test_create_account_success(self):
        """Test successful account creation"""
        account = self.manager.create_account("Main Checking", AccountType.CHECKING, Decimal('1000'))
        assert account.name == "Main Checking"
        assert account.id == 1
        assert len(self.manager.accounts) == 1
    
    def test_create_duplicate_account_name(self):
        """Test creating account with duplicate name"""
        self.manager.create_account("Test Account", AccountType.CHECKING)
        with pytest.raises(ValueError, match="Account with name 'Test Account' already exists"):
            self.manager.create_account("Test Account", AccountType.SAVINGS)
    
    def test_get_account_by_id_exists(self):
        """Test getting account by ID - exists"""
        account = self.manager.create_account("Test Account", AccountType.CHECKING)
        found_account = self.manager.get_account_by_id(account.id)
        assert found_account == account
    
    def test_get_account_by_id_not_exists(self):
        """Test getting account by ID - does not exist"""
        found_account = self.manager.get_account_by_id(999)
        assert found_account is None
    
    def test_get_total_balance(self):
        """Test getting total balance"""
        self.manager.create_account("Account 1", AccountType.CHECKING, Decimal('1000'))
        self.manager.create_account("Account 2", AccountType.SAVINGS, Decimal('2000'))
        total = self.manager.get_total_balance()
        assert total == Decimal('3000')
    
    def test_delete_account_success(self):
        """Test successful account deletion with zero balance"""
        account = self.manager.create_account("Test Account", AccountType.CHECKING)
        account_id = account.id
        
        # Verify account exists
        assert self.manager.get_account_by_id(account_id) is not None
        
        # Delete account (zero balance should allow deletion)
        result = self.manager.delete_account(account_id)
        assert result is True
        
        # Verify account no longer exists
        assert self.manager.get_account_by_id(account_id) is None
        assert len(self.manager.accounts) == 0
    
    def test_delete_account_not_found(self):
        """Test deleting non-existent account"""
        # Try to delete account that doesn't exist
        result = self.manager.delete_account(999)
        assert result is False
    
    def test_delete_account_with_balance_fails(self):
        """Test that deleting account with non-zero balance raises error"""
        account = self.manager.create_account("Test Account", AccountType.CHECKING, Decimal('100'))
        account_id = account.id
        
        # Try to delete account with balance
        with pytest.raises(ValueError, match="Cannot delete account with non-zero balance"):
            self.manager.delete_account(account_id)
        
        # Verify account still exists
        assert self.manager.get_account_by_id(account_id) is not None
    
    def test_delete_account_after_zeroing_balance(self):
        """Test deleting account after withdrawing all funds"""
        account = self.manager.create_account("Test Account", AccountType.CHECKING, Decimal('100'))
        account_id = account.id
        
        # Withdraw all funds to zero the balance
        account.withdraw(Decimal('100'))
        assert account.balance == Decimal('0')
        
        # Now deletion should succeed
        result = self.manager.delete_account(account_id)
        assert result is True
        assert self.manager.get_account_by_id(account_id) is None