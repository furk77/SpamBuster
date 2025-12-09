#!/bin/bash

echo "Starting full setup and launch sequence..."

if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
else
    echo "Virtual environment already exists."
fi

echo "Activating virtual environment..."
source venv/bin/activate

if [ -f "requirements.txt" ]; then
    echo "Installing required packages..."
    pip install -r requirements.txt
else
    echo "requirements.txt not found! Make sure it's in the project directory."
    exit 1
fi

echo "Running model.py..."
python model.py

if [ $? -ne 0 ]; then
    echo "model.py failed. Stopping script."
    exit 1
fi

echo "Launching app.py..."
python3 app.py

echo "All processes completed."
