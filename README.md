# Personal Finance Management System

This is a **deliberately feature-incomplete** personal finance management system designed specifically for AI assistant extension. The project includes account management, transaction recording, budget management, and a complete REST API interface, using modern Python technology stack.

## 🎯 Project Features

- **Real-world application scenario**: Personal finance management, more practically valuable than simple calculators
- **Modern technology stack**: FastAPI + Pydantic + pytest + Web interface
- **Good architecture**: Clear module separation and type hints
- **Complete testing**: 28 passing tests

## 📊 Current Test Status

```
==================================== test session starts ====================================
collected 30 items                                                                           

✅ 28 passed  - Core functionality fully implemented
================================================================================================
```

### 🎯 Intentionally Failing Test Cases (need AI to add features for fixing):

1. **Delete Account Functionality** (`test_delete_account_missing_feature`) 
   - Missing: `AccountManager.delete_account()` method
   - Purpose: Delete unnecessary accounts

2. **Monthly Summary Functionality** (`test_monthly_summary_missing_feature`)
   - Missing: `TransactionManager.get_monthly_summary()` method
   - Purpose: Financial monthly reports

## 📁 Project Structure

```
Sonnet4/
├── src/
│   ├── __init__.py
│   ├── account.py         # Account management module (incomplete functionality)
│   ├── transaction.py     # Transaction recording module (incomplete functionality)
│   ├── budget.py          # Budget management module (incomplete functionality)
│   └── api.py             # FastAPI REST interface (incomplete functionality)
├── tests/
│   ├── __init__.py
│   ├── test_account.py       # Account module pytest tests (incomplete tests)
│   ├── test_transaction.py  # Transaction module pytest tests (incomplete tests)
│   └── test_budget.py       # Budget module pytest tests (incomplete tests)
├── main.py                # Main program demonstration
├── requirements.txt       # Project dependencies
└── README.md             # Project documentation
```

## 🚀 Quick Start

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run Main Program
```bash
python main.py
```

### Run Tests
```bash
# Run all pytest tests
pytest

# Run specific test file
pytest tests/test_account.py -v

# Run tests and generate coverage report
pytest --cov=src tests/
```

### Start API Server
```bash
# Method 1: Use smart port detection startup script
python start_api.py

# Method 2: Direct startup (may encounter port conflicts)
uvicorn src.api:app --reload
```

**API Access Addresses:**
- 🌐 **User-friendly Interface**: http://localhost:8000/ (recommended)
- 📚 **API Documentation**: http://localhost:8000/docs
- 🔧 **Backup Ports**: If 8000 is occupied, will automatically try 8001, 8002, etc.

## 📊 Current Functionality Implementation Status

### ✅ Account Management Module (src/account.py)
**Implemented Features:**
- Create different types of accounts (checking, savings, credit card, investment)
- Basic deposit and withdrawal operations
- Account balance inquiry
- Account name duplication check

**❌ Missing Features:**
- Delete account functionality
- Update account information
- Filter accounts by type
- Inter-account transfers
- Deactivate account functionality
- Account history records
- Interest calculation
- Credit limit setting

### ✅ Transaction Recording Module (src/transaction.py)
**Implemented Features:**
- Add transaction records (income, expense, transfer)
- Query transactions by account
- Get recent transaction records

**❌ Missing Features:**
- Delete/update transaction records
- Filter transactions by type
- Query by date range
- Transaction categorization functionality
- Monthly income/expense summary
- Transaction search functionality
- Recurring transaction setup
- Financial report generation

### ✅ Budget Management Module (src/budget.py)
**Implemented Features:**
- Create budgets (monthly, quarterly, annual)
- Get active budgets
- Budget total amount calculation
- Budget name duplication check

**❌ Missing Features:**
- Update/delete budgets
- Filter budgets by category
- Budget utilization rate calculation
- Budget alert system
- Budget vs actual comparison
- Budget adjustment recommendations
- Budget rollover functionality

### ✅ REST API Interface (src/api.py)
**Implemented Features:**
- Basic account CRUD interfaces
- Basic transaction record interfaces
- Basic budget management interfaces
- Automatic API documentation generation

**❌ Missing Features:**
- Authentication and authorization
- Dedicated deposit/withdrawal interfaces
- Account transfer interfaces
- Advanced query and filtering
- Financial report interfaces
- File upload and download
- API rate limiting and caching
- Error handling middleware

## 🧪 Test Coverage

### pytest Test Features
- Uses modern pytest framework (not unittest)
- Concise functional testing style
- Parameterized test support
- Clear assertion syntax

### Current Test Coverage
**Account Management Tests (test_account.py):**
- ✅ Basic account creation and operations
- ✅ Deposit/withdrawal functionality tests
- ✅ Duplicate account name detection
- ❌ Missing boundary tests and exception scenarios

**Transaction Recording Tests (test_transaction.py):**
- ✅ Basic transaction creation
- ✅ Amount validation tests
- ✅ Transaction query tests
- ❌ Missing complex queries and integration tests

**Budget Management Tests (test_budget.py):**
- ✅ Basic budget creation
- ✅ Budget validation tests
- ✅ Budget period tests
- ❌ Missing business logic and calculation tests

## 🛠️ Technology Stack

- **Backend Framework**: FastAPI (async, high performance)
- **Data Validation**: Pydantic (type safety)
- **Testing Framework**: pytest (modern testing)
- **API Documentation**: Auto-generated OpenAPI/Swagger
- **Type Hints**: Comprehensive Python type annotations
- **Numeric Processing**: Decimal (precise monetary calculations)

## 📈 Extension Recommendations

When asking AI assistants to add functionality, it's recommended to follow this priority order:

### 1. Core Functionality Enhancement
```bash
"Please add delete account functionality and corresponding test cases to the account management module"
"Implement monthly summary statistical report functionality for transaction records"
```

### 2. API Functionality Enhancement
```bash
"Add JWT authentication and permission control to the API"
"Implement financial reporting and data analysis interfaces"
"Add file import/export functionality"
```

### 3. Testing Improvement
```bash
"Add boundary tests and exception handling tests for existing functionality"
"Add API integration tests and end-to-end tests"
"Implement test data factory and fixtures"
```

### 4. Advanced Features
```bash
"Add data persistence support (SQLAlchemy + PostgreSQL)"
"Implement recurring transactions and financial goal tracking"
"Add data visualization and chart generation"
```

## 🌟 Project Highlights

1. **Real Business Scenario**: Personal finance management is a practical application scenario
2. **Modern Technology Stack**: Adopts modern Python technologies like FastAPI
3. **Clear Architecture**: Good module separation and code organization
4. **Type Safety**: Comprehensive type hints and Pydantic validation
5. **Strong Extensibility**: Clear TODO lists and extension points
6. **pytest Testing**: Modern testing framework and practices

This project is more valuable than simple calculators, providing real business logic and expansion space!