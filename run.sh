#!/bin/bash

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask app with Gunicorn
# In production, increase number of workers and use a distributed cache like redis.
gunicorn -w 1 -b 0.0.0.0:8000 app.app:app