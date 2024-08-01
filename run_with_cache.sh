#!/bin/bash

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the cache server in the background
# Adjust the command according to how you run your cache server
gunicorn -w 1 -b 0.0.0.0:5001 app.cache_server:app > cache_server.log 2>&1 &

# Run the Flask app with Gunicorn
# In production, increase number of workers and use a distributed cache like redis.
gunicorn -w 4 -b 0.0.0.0:8000 app.app_with_external_cache:app

# Output the PIDs of the processes
echo "Cache server and Flask app are running."