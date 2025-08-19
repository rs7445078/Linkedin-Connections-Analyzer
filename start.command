#!/bin/bash
# LinkedIn Connections Analyzer - macOS Startup Script
# This is a clickable script for macOS users to easily launch the application

# Change to the directory containing this script
cd "$(dirname "$0")"

# Display welcome banner
echo "=================================================="
echo "📊 LinkedIn Connections Analyzer - macOS Launcher"
echo "=================================================="

# Check for Python installation
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed"
    echo "Please install Python 3.8 or higher from python.org"
    echo ""
    echo "Press any key to exit..."
    read -n 1
    exit 1
fi

# Check Python version
PY_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
if (( $(echo "$PY_VERSION < 3.8" | bc -l) )); then
    echo "❌ Error: Python $PY_VERSION detected, but version 3.8 or higher is required"
    echo "Please upgrade your Python installation"
    echo ""
    echo "Press any key to exit..."
    read -n 1
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "🔧 Creating virtual environment..."
    python3 -m venv venv
else
    echo "✅ Using existing virtual environment"
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Install dependencies with progress indicator
echo "📦 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Launch the application
echo "🚀 Launching LinkedIn Connections Analyzer..."
echo "The dashboard will open in your default web browser shortly"
echo ""
echo "(Close this terminal window to exit the application when done)"
echo "=================================================="

# Run the application
streamlit run app.py

# This line will only execute after the user closes streamlit
echo "Application closed. Press any key to exit..."
read -n 1