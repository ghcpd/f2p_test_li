"""
Personal Finance Management System - Web Interface
Provides user-friendly HTML interface as an alternative to complex API documentation
"""

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os

# Add Web interface routes in api.py

web_interface_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Personal Finance Management System</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            color: #333;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        .header {
            background: rgba(255, 255, 255, 0.95);
            padding: 30px;
            border-radius: 15px;
            margin-bottom: 30px;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        }
        
        .header h1 {
            color: #4a5568;
            margin-bottom: 10px;
            font-size: 2.5em;
        }
        
        .header p {
            color: #718096;
            font-size: 1.2em;
        }
        
        .status {
            background: #48bb78;
            color: white;
            padding: 8px 16px;
            border-radius: 20px;
            display: inline-block;
            margin-top: 10px;
        }
        
        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 25px;
            margin-bottom: 30px;
        }
        
        .feature-card {
            background: rgba(255, 255, 255, 0.95);
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }
        
        .feature-card:hover {
            transform: translateY(-5px);
        }
        
        .feature-card h3 {
            color: #4a5568;
            margin-bottom: 15px;
            font-size: 1.4em;
            display: flex;
            align-items: center;
        }
        
        .feature-card .icon {
            font-size: 1.5em;
            margin-right: 10px;
        }
        
        .feature-list {
            list-style: none;
            margin-bottom: 20px;
        }
        
        .feature-list li {
            padding: 8px 0;
            color: #4a5568;
            position: relative;
            padding-left: 25px;
        }
        
        .feature-list li::before {
            content: "✓";
            position: absolute;
            left: 0;
            color: #48bb78;
            font-weight: bold;
        }
        
        .missing-features {
            color: #e53e3e;
            font-style: italic;
            margin-top: 15px;
        }
        
        .missing-features li::before {
            content: "✗";
            color: #e53e3e;
        }
        
        .quick-actions {
            background: rgba(255, 255, 255, 0.95);
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            margin-bottom: 30px;
        }
        
        .quick-actions h3 {
            color: #4a5568;
            margin-bottom: 20px;
            font-size: 1.4em;
        }
        
        .action-buttons {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
        }
        
        .btn {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 12px 20px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 1em;
            transition: all 0.3s ease;
            text-decoration: none;
            text-align: center;
            display: inline-block;
        }
        
        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
        }
        
        .btn-secondary {
            background: linear-gradient(135deg, #4299e1 0%, #3182ce 100%);
        }
        
        .footer {
            background: rgba(255, 255, 255, 0.95);
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        }
        
        .footer p {
            color: #718096;
            margin-bottom: 10px;
        }
        
        .footer a {
            color: #4299e1;
            text-decoration: none;
        }
        
        .footer a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🏦 Personal Finance Management System</h1>
            <p>Simple and practical personal finance management tool</p>
            <span class="status">API Service Running</span>
        </div>
        
        <div class="features-grid">
            <!-- Account Management -->
            <div class="feature-card">
                <h3><span class="icon">💳</span>Account Management</h3>
                <ul class="feature-list">
                    <li>Create checking, savings, credit card accounts</li>
                    <li>View account balance and details</li>
                    <li>Basic deposit and withdrawal operations</li>
                </ul>
                <ul class="feature-list missing-features">
                    <li>Inter-account transfers</li>
                    <li>Interest calculation</li>
                    <li>Credit limit management</li>
                </ul>
            </div>
            
            <!-- Transaction Recording -->
            <div class="feature-card">
                <h3><span class="icon">📊</span>Transaction Recording</h3>
                <ul class="feature-list">
                    <li>Record income and expenses</li>
                    <li>View transaction history</li>
                    <li>Filter transactions by account</li>
                </ul>
                <ul class="feature-list missing-features">
                    <li>Transaction category statistics</li>
                    <li>Monthly income/expense reports</li>
                    <li>Transaction search functionality</li>
                </ul>
            </div>
            
            <!-- Budget Management -->
            <div class="feature-card">
                <h3><span class="icon">🎯</span>Budget Management</h3>
                <ul class="feature-list">
                    <li>Set monthly and quarterly budgets</li>
                    <li>Manage budgets by category</li>
                    <li>View total budget amounts</li>
                </ul>
                <ul class="feature-list missing-features">
                    <li>Budget utilization monitoring</li>
                    <li>Overspending alert notifications</li>
                    <li>Budget adjustment recommendations</li>
                </ul>
            </div>
        </div>
        
        <div class="quick-actions">
            <h3>🚀 Quick Actions</h3>
            <div class="action-buttons">
                <a href="/docs" class="btn">📚 API Documentation</a>
                <a href="/redoc" class="btn btn-secondary">📖 ReDoc Documentation</a>
                <a href="/health" class="btn btn-secondary">💚 Health Check</a>
                <button class="btn" onclick="createTestAccount()">🆕 Create Test Account</button>
                <button class="btn" onclick="viewAccounts()">👀 View All Accounts</button>
                <button class="btn" onclick="addTestTransaction()">💰 Add Test Transaction</button>
            </div>
        </div>
        
        <div class="footer">
            <p>This is a feature-incomplete demo system designed for AI assistant extension</p>
            <p>
                <a href="https://github.com" target="_blank">GitHub Project</a> | 
                <a href="/docs" target="_blank">Developer Documentation</a> | 
                <a href="mailto:support@example.com">Technical Support</a>
            </p>
        </div>
    </div>
    
    <script>
        const API_BASE = '';
        
        async function apiCall(endpoint, method = 'GET', data = null) {
            try {
                const options = {
                    method: method,
                    headers: {
                        'Content-Type': 'application/json',
                    },
                };
                
                if (data) {
                    options.body = JSON.stringify(data);
                }
                
                const response = await fetch(endpoint, options);
                const result = await response.json();
                
                if (response.ok) {
                    return { success: true, data: result };
                } else {
                    return { success: false, error: result };
                }
            } catch (error) {
                return { success: false, error: error.message };
            }
        }
        
        async function createTestAccount() {
            const accountData = {
                name: "Test_Account_" + Date.now(),
                account_type: "checking",
                initial_balance: "1000.00"
            };
            
            const result = await apiCall('/accounts', 'POST', accountData);
            
            if (result.success) {
                alert(`✅ Account created successfully!\\nAccount ID: ${result.data.id}\\nAccount Name: ${result.data.name}\\nBalance: $${result.data.balance}`);
            } else {
                alert(`❌ Creation failed: ${JSON.stringify(result.error)}`);
            }
        }
        
        async function viewAccounts() {
            const result = await apiCall('/accounts');
            
            if (result.success) {
                const accounts = result.data;
                if (accounts.length === 0) {
                    alert('📭 No accounts found, please create an account first!');
                } else {
                    let message = `📋 Account List (${accounts.length} total):\\n\\n`;
                    accounts.forEach(account => {
                        message += `🏦 ${account.name}\\n`;
                        message += `   ID: ${account.id}\\n`;
                        message += `   Type: ${account.account_type}\\n`;
                        message += `   Balance: $${account.balance}\\n`;
                        message += `   Status: ${account.is_active ? 'Active' : 'Inactive'}\\n\\n`;
                    });
                    alert(message);
                }
            } else {
                alert(`❌ Failed to get account list: ${JSON.stringify(result.error)}`);
            }
        }
        
        async function addTestTransaction() {
            // First get account list
            const accountsResult = await apiCall('/accounts');
            
            if (!accountsResult.success || accountsResult.data.length === 0) {
                alert('❌ Please create at least one account first!');
                return;
            }
            
            const account = accountsResult.data[0]; // Use the first account
            
            const transactionData = {
                account_id: account.id,
                amount: "250.50",
                transaction_type: "expense",
                description: "Test_Expense_" + Date.now()
            };
            
            const result = await apiCall('/transactions', 'POST', transactionData);
            
            if (result.success) {
                alert(`✅ Transaction added successfully!\\nTransaction ID: ${result.data.id}\\nAccount: ${account.name}\\nAmount: $${result.data.amount}\\nType: ${result.data.transaction_type}\\nDescription: ${result.data.description}`);
            } else {
                alert(`❌ Failed to add transaction: ${JSON.stringify(result.error)}`);
            }
        }
        
        // Check API status when page loads
        window.addEventListener('load', async () => {
            const result = await apiCall('/health');
            if (!result.success) {
                document.querySelector('.status').textContent = 'API Service Error';
                document.querySelector('.status').style.background = '#e53e3e';
            }
        });
    </script>
</body>
</html>
"""


def get_web_interface():
    """Return Web interface HTML"""
    return HTMLResponse(content=web_interface_html)