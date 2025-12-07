#!/bin/bash
# setup_dev.sh
# Automated script to set up the development environment for Raven-stars-omega.

echo "--- Raven-stars-omega Development Environment Setup ---"

# 1. Create a Python virtual environment
if [ -d ".venv" ]; then
    echo "Virtual environment (.venv) already exists. Skipping creation."
else
    echo "Creating virtual environment (.venv)..."
    python3 -m venv .venv
fi

# 2. Activate the virtual environment
source .venv/bin/activate
echo "Virtual environment activated."

# 3. Install required packages
echo "Installing dependencies from requirements.txt..."
pip install --upgrade pip
pip install -r requirements.txt

# 4. Success message
echo "------------------------------------------------------"
echo "Setup complete! To start developing, run:"
echo "source .venv/bin/activate"
echo "------------------------------------------------------"

# 5. Check environment status
python3 --version
pip list | grep -E 'pytest|black|matplotlib'

