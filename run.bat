@echo off
echo 🚀 Soldiers Management System
echo ================================

echo.
echo 📦 Installing dependencies...
pip install -r requirements.txt

echo.
echo 🔗 Testing MongoDB connection...
python test_connection.py

echo.
echo 🎯 Running example...
python example.py

echo.
echo 🌐 Starting API server...
echo Press Ctrl+C to stop the server
python services/api.py

pause
