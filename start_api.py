"""
API Server Startup Script
Automatically detects available ports and starts FastAPI server
"""

import socket
import subprocess
import sys
import os


def is_port_available(port):
    """Check if port is available"""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex(('localhost', port))
            return result != 0
    except:
        return False


def find_available_port(start_port=8000, max_attempts=10):
    """Find available port"""
    for i in range(max_attempts):
        port = start_port + i
        if is_port_available(port):
            return port
    return None


def start_api_server():
    """Start API server"""
    print("🚀 Personal Finance Management System - API Server Launcher")
    print("=" * 50)
    
    # Find available port
    available_port = find_available_port()
    
    if available_port is None:
        print("❌ Error: Unable to find available port (8000-8009)")
        print("💡 Solutions:")
        print("1. Manually specify port: uvicorn src.api:app --reload --port 8080")
        print("2. Check port usage: netstat -ano | findstr :8000")
        print("3. Kill process: taskkill /PID <ProcessID> /F")
        return
    
    print(f"✅ Found available port: {available_port}")
    print(f"📚 API Documentation: http://localhost:{available_port}/docs")
    print(f"🔗 API Root URL: http://localhost:{available_port}/")
    print("-" * 50)
    
    # Build startup command
    cmd = [
        sys.executable, "-m", "uvicorn", 
        "src.api:app", 
        "--reload", 
        "--port", str(available_port),
        "--host", "127.0.0.1"
    ]
    
    try:
        print(f"🎯 Startup command: {' '.join(cmd)}")
        print("Press Ctrl+C to stop server")
        print("=" * 50)
        
        # Start server
        subprocess.run(cmd, cwd=os.path.dirname(os.path.abspath(__file__)))
        
    except KeyboardInterrupt:
        print("\n👋 Server stopped")
    except FileNotFoundError:
        print("❌ Error: uvicorn not found, please install: pip install uvicorn")
    except Exception as e:
        print(f"❌ Startup failed: {e}")


if __name__ == "__main__":
    start_api_server()