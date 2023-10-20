import time
import requests

def my_function():
    # Your code here
    pass

# Wait for network initialization
while True:
    try:
        response = requests.get('http://www.google.com')
        print("Network initialized!")
        break
    except requests.exceptions.ConnectionError:
        print("Waiting for network initialization...")
        time.sleep(5)

# Execute the function as long as there is an internet connection
while True:
    try:
        my_function()
        print("Function executed successfully!")
        break
    except requests.exceptions.ConnectionError:
        print("No internet connection, retrying in 5 seconds...")
        time.sleep(5)