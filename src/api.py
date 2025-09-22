"""
Personal Finance Management System - FastAPI REST API
Intentionally implements only basic interfaces, missing authentication, authorization and advanced features
"""

from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse, HTMLResponse
from pydantic import BaseModel
from decimal import Decimal
from datetime import datetime, date
from typing import List, Optional

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from account import AccountManager, AccountType
from transaction import TransactionManager, TransactionType
from budget import BudgetManager, BudgetPeriod
from web_interface import get_web_interface

# Initialize FastAPI application
app = FastAPI(
    title="Personal Finance Manager API",
    description="A simple personal finance management system (incomplete)",
    version="0.1.0"
)

# Global manager instances (should use database in real applications)
account_manager = AccountManager()
transaction_manager = TransactionManager()
budget_manager = BudgetManager()


# Pydantic model
class AccountCreate(BaseModel):
    name: str
    account_type: AccountType
    initial_balance: Decimal = Decimal('0')


class AccountResponse(BaseModel):
    id: int
    name: str
    account_type: AccountType
    balance: Decimal
    is_active: bool
    created_at: datetime


class TransactionCreate(BaseModel):
    account_id: int
    amount: Decimal
    transaction_type: TransactionType
    description: str = ""


class TransactionResponse(BaseModel):
    id: int
    account_id: int
    amount: Decimal
    transaction_type: TransactionType
    description: str
    date: datetime


class BudgetCreate(BaseModel):
    name: str
    category: str
    amount: Decimal
    period: BudgetPeriod = BudgetPeriod.MONTHLY


class BudgetResponse(BaseModel):
    id: int
    name: str
    category: str
    amount: Decimal
    period: BudgetPeriod
    start_date: date
    is_active: bool


# Account related endpoints
@app.post("/accounts", response_model=AccountResponse, status_code=status.HTTP_201_CREATED)
async def create_account(account_data: AccountCreate):
    """Create new account"""
    try:
        account = account_manager.create_account(
            name=account_data.name,
            account_type=account_data.account_type,
            initial_balance=account_data.initial_balance
        )
        return AccountResponse(
            id=account.id,
            name=account.name,
            account_type=account.account_type,
            balance=account.balance,
            is_active=account.is_active,
            created_at=account.created_at
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/accounts", response_model=List[AccountResponse])
async def get_accounts():
    """Get all accounts"""
    accounts = []
    for account in account_manager.accounts:
        accounts.append(AccountResponse(
            id=account.id,
            name=account.name,
            account_type=account.account_type,
            balance=account.balance,
            is_active=account.is_active,
            created_at=account.created_at
        ))
    return accounts


@app.get("/accounts/{account_id}", response_model=AccountResponse)
async def get_account(account_id: int):
    """Get account by ID"""
    account = account_manager.get_account_by_id(account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    
    return AccountResponse(
        id=account.id,
        name=account.name,
        account_type=account.account_type,
        balance=account.balance,
        is_active=account.is_active,
        created_at=account.created_at
    )


# Transaction related endpoints
@app.post("/transactions", response_model=TransactionResponse, status_code=status.HTTP_201_CREATED)
async def create_transaction(transaction_data: TransactionCreate):
    """Create new transaction"""
    try:
        # Verify account exists
        account = account_manager.get_account_by_id(transaction_data.account_id)
        if not account:
            raise HTTPException(status_code=400, detail="Account not found")
        
        transaction = transaction_manager.add_transaction(
            account_id=transaction_data.account_id,
            amount=transaction_data.amount,
            transaction_type=transaction_data.transaction_type,
            description=transaction_data.description
        )
        
        return TransactionResponse(
            id=transaction.id,
            account_id=transaction.account_id,
            amount=transaction.amount,
            transaction_type=transaction.transaction_type,
            description=transaction.description,
            date=transaction.date
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/transactions", response_model=List[TransactionResponse])
async def get_transactions(limit: int = 10):
    """Get recent transaction records"""
    transactions = transaction_manager.get_recent_transactions(limit)
    return [TransactionResponse(
        id=t.id,
        account_id=t.account_id,
        amount=t.amount,
        transaction_type=t.transaction_type,
        description=t.description,
        date=t.date
    ) for t in transactions]


# Budget related endpoints
@app.post("/budgets", response_model=BudgetResponse, status_code=status.HTTP_201_CREATED)
async def create_budget(budget_data: BudgetCreate):
    """Create new budget"""
    try:
        budget = budget_manager.create_budget(
            name=budget_data.name,
            category=budget_data.category,
            amount=budget_data.amount,
            period=budget_data.period
        )
        
        return BudgetResponse(
            id=budget.id,
            name=budget.name,
            category=budget.category,
            amount=budget.amount,
            period=budget.period,
            start_date=budget.start_date,
            is_active=budget.is_active
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/budgets", response_model=List[BudgetResponse])
async def get_budgets():
    """Get all active budgets"""
    budgets = budget_manager.get_active_budgets()
    return [BudgetResponse(
        id=b.id,
        name=b.name,
        category=b.category,
        amount=b.amount,
        period=b.period,
        start_date=b.start_date,
        is_active=b.is_active
    ) for b in budgets]


# Basic information endpoints
@app.get("/", response_class=HTMLResponse)
async def root():
    """Web interface homepage"""
    return get_web_interface()


@app.get("/api")
async def api_info():
    """API information (JSON format)"""
    return {
        "message": "Personal Finance Manager API",
        "version": "0.1.0",
        "status": "incomplete - many features missing"
    }


@app.get("/health")
async def health_check():
    """Health check"""
    return {"status": "healthy"}


# TODO: Need to add the following API endpoints:
# - PUT /accounts/{id}: Update account information
# - DELETE /accounts/{id}: Delete account
# - POST /accounts/{id}/deposit: Deposit operation
# - POST /accounts/{id}/withdraw: Withdrawal operation
# - POST /accounts/transfer: Transfer between accounts
# - GET /transactions/{id}: Get specific transaction
# - PUT /transactions/{id}: Update transaction
# - DELETE /transactions/{id}: Delete transaction
# - GET /accounts/{id}/transactions: Get account transaction history
# - PUT /budgets/{id}: Update budget
# - DELETE /budgets/{id}: Delete budget
# - GET /budgets/{id}/utilization: Get budget utilization
# - GET /reports/summary: Financial summary report
# - GET /reports/monthly: Monthly report
# - Authentication and authorization middleware
# - Request validation and error handling
# - API documentation and test cases