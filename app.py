from flask import Flask
from redis import Redis

# Create a Flask app
app = Flask(__name__)

# Connect to Redis server
redis = Redis(host='redis', port=6379)

# Define a route for the homepage '/'
@app.route('/')
def hello():
    # Increment the 'hits' counter in Redis
    redis.incr('hits')
    
    # Display the number of page views to the user
    return f'Hello! This page has been viewed {redis.get("hits").decode("utf-8")} times.'

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0')