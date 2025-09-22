"""
Personal Finance Management System - Budget Management Module
Intentionally implements only basic functionality, missing alerts, analysis and advanced management features
"""

from datetime import datetime, date
from decimal import Decimal
from enum import Enum
from typing import Optional, List, Dict
from dataclasses import dataclass


class BudgetPeriod(Enum):
    """Budget periods"""
    MONTHLY = "monthly"
    QUARTERLY = "quarterly"
    YEARLY = "yearly"


@dataclass
class Budget:
    """Budget"""
    id: Optional[int] = None
    name: str = ""
    category: str = ""
    amount: Decimal = Decimal('0')
    period: BudgetPeriod = BudgetPeriod.MONTHLY
    start_date: date = None
    is_active: bool = True
    
    def __post_init__(self):
        if self.start_date is None:
            self.start_date = date.today()


class BudgetManager:
    """Budget manager, functionality intentionally incomplete"""
    
    def __init__(self):
        self.budgets: List[Budget] = []
        self.next_id = 1
    
    def create_budget(self, name: str, category: str, amount: Decimal, 
                     period: BudgetPeriod = BudgetPeriod.MONTHLY) -> Budget:
        """Create new budget"""
        if amount <= 0:
            raise ValueError("Budget amount must be positive")
        
        # Simple duplicate check
        if any(b.name == name and b.is_active for b in self.budgets):
            raise ValueError(f"Active budget with name '{name}' already exists")
        
        budget = Budget(
            id=self.next_id,
            name=name,
            category=category,
            amount=amount,
            period=period
        )
        
        self.next_id += 1
        self.budgets.append(budget)
        return budget
    
    def get_budget_by_id(self, budget_id: int) -> Optional[Budget]:
        """Get budget by ID"""
        for budget in self.budgets:
            if budget.id == budget_id:
                return budget
        return None
    
    def get_active_budgets(self) -> List[Budget]:
        """Get all active budgets"""
        return [b for b in self.budgets if b.is_active]
    
    def get_total_budget_amount(self) -> Decimal:
        """Get total amount of all active budgets"""
        return sum(b.amount for b in self.budgets if b.is_active)
    
    # TODO: Need to add the following features:
    # - update_budget(budget_id, **kwargs): Update budget
    # - delete_budget(budget_id): Delete budget
    # - deactivate_budget(budget_id): Deactivate budget
    # - get_budgets_by_category(category): Get budgets by category
    # - calculate_budget_utilization(): Calculate budget utilization
    # - check_budget_alerts(): Check budget alerts
    # - generate_budget_report(): Generate budget report
    # - compare_actual_vs_budget(): Compare actual spending vs budget
    # - suggest_budget_adjustments(): Suggest budget adjustments
    # - set_budget_alerts(): Set budget reminders
    # - copy_budget(): Copy budget to new period
    # - rollover_unused_budget(): Rollover unused budget