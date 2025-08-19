#!/bin/bash
# LinkedIn Connections Analyzer - Startup Script
# This script sets up a Python virtual environment and launches the application

# Exit immediately if a command exits with a non-zero status
set -e

echo "🔗 Setting up LinkedIn Connections Analyzer..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed or not in PATH"
    echo "Please install Python 3.8 or higher and try again"
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "🔧 Creating virtual environment..."
    python3 -m venv venv
else
    echo "✓ Using existing virtual environment"
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip and install dependencies
echo "📦 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt
pip install watchdog

# Run the application
echo "🚀 Launching LinkedIn Connections Analyzer..."
streamlit run app.py

# Note: The script will end when streamlit is closed