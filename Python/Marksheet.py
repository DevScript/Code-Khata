# Get GitHub Profile Picture URL from username

# Import required modules for program to run correctly and display output to user in terminal
import requests # Import requests module to send GET request to GitHub API
import json # Import json module to load JSON data from GitHub API

# Define function to get GitHub Profile Picture URL from username and return it to user in terminal
def getProfilePicture(username): # Define function with parameter username
    url = "https://api.github.com/users/" + username # Define url variable with GitHub API URL and username parameter
    r = requests.get(url) # Send GET request to URL and assign to r variable (r = response)
    data = json.loads(r.text) # Load JSON data from r.text and assign to data variable (data = response data)
    return data["avatar_url"] # Return the avatar_url from data

# Driver to test function
print(getProfilePicture('MLSA-Mehran-UET')) # Print the URL of the profile picture
