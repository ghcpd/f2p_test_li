"""
pytest tests for budget management module
Intentionally includes only basic tests, missing complex business logic tests
"""

import pytest
from decimal import Decimal
from datetime import date

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from budget import Budget, BudgetManager, BudgetPeriod


class TestBudget:
    """Basic tests for Budget class"""
    
    def test_create_budget_basic(self):
        """Test basic budget creation"""
        budget = Budget(
            id=1,
            name="Groceries",
            category="Food",
            amount=Decimal('500'),
            period=BudgetPeriod.MONTHLY
        )
        assert budget.id == 1
        assert budget.name == "Groceries"
        assert budget.category == "Food"
        assert budget.amount == Decimal('500')
        assert budget.period == BudgetPeriod.MONTHLY
        assert budget.is_active is True
        assert isinstance(budget.start_date, date)
    
    def test_budget_auto_start_date(self):
        """Test budget auto-sets start date"""
        budget = Budget(name="Test", category="Test", amount=Decimal('100'))
        assert budget.start_date is not None
        assert isinstance(budget.start_date, date)


class TestBudgetManager:
    """Basic tests for BudgetManager class"""
    
    def setup_method(self):
        """Setup before each test"""
        self.manager = BudgetManager()
    
    def test_create_budget_success(self):
        """Test successful budget creation"""
        budget = self.manager.create_budget(
            name="Groceries",
            category="Food",
            amount=Decimal('500'),
            period=BudgetPeriod.MONTHLY
        )
        assert budget.id == 1
        assert budget.name == "Groceries"
        assert len(self.manager.budgets) == 1
    
    def test_create_budget_zero_amount(self):
        """Test creating zero amount budget"""
        with pytest.raises(ValueError, match="Budget amount must be positive"):
            self.manager.create_budget("Test", "Test", Decimal('0'))
    
    def test_create_budget_negative_amount(self):
        """Test creating negative amount budget"""
        with pytest.raises(ValueError, match="Budget amount must be positive"):
            self.manager.create_budget("Test", "Test", Decimal('-100'))
    
    def test_create_duplicate_budget_name(self):
        """Test creating budget with duplicate name"""
        self.manager.create_budget("Groceries", "Food", Decimal('500'))
        with pytest.raises(ValueError, match="Active budget with name 'Groceries' already exists"):
            self.manager.create_budget("Groceries", "Food", Decimal('600'))
    
    def test_get_budget_by_id_exists(self):
        """Test getting budget by ID - exists"""
        budget = self.manager.create_budget("Test", "Test", Decimal('100'))
        found_budget = self.manager.get_budget_by_id(budget.id)
        assert found_budget == budget
    
    def test_get_budget_by_id_not_exists(self):
        """Test getting budget by ID - does not exist"""
        found_budget = self.manager.get_budget_by_id(999)
        assert found_budget is None
    
    def test_get_active_budgets(self):
        """Test getting active budgets"""
        budget1 = self.manager.create_budget("Budget 1", "Category 1", Decimal('100'))
        budget2 = self.manager.create_budget("Budget 2", "Category 2", Decimal('200'))
        budget2.is_active = False  # Deactivate the second budget
        
        active_budgets = self.manager.get_active_budgets()
        assert len(active_budgets) == 1
        assert active_budgets[0] == budget1
    
    def test_get_total_budget_amount(self):
        """Test getting total budget amount"""
        self.manager.create_budget("Budget 1", "Category 1", Decimal('100'))
        budget2 = self.manager.create_budget("Budget 2", "Category 2", Decimal('200'))
        budget2.is_active = False  # Deactivate the second budget
        
        total = self.manager.get_total_budget_amount()
        assert total == Decimal('100')  # Only count active budgets
    
    def test_budget_periods(self):
        """Test different budget periods"""
        monthly = self.manager.create_budget("Monthly", "Test", Decimal('100'), BudgetPeriod.MONTHLY)
        quarterly = self.manager.create_budget("Quarterly", "Test", Decimal('300'), BudgetPeriod.QUARTERLY)
        yearly = self.manager.create_budget("Yearly", "Test", Decimal('1200'), BudgetPeriod.YEARLY)
        
        assert monthly.period == BudgetPeriod.MONTHLY
        assert quarterly.period == BudgetPeriod.QUARTERLY
        assert yearly.period == BudgetPeriod.YEARLY