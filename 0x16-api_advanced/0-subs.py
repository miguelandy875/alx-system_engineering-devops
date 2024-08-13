import requests

def number_of_subscribers(subreddit):
    # Define the Reddit API URL for the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    try:
        # Make the GET request to the Reddit API
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, allow_redirects=False)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            
            # Extract the number of subscribers
            subscribers = data.get('data', {}).get('subscribers', 0)
            return subscribers
        else:
            # If status code is not 200, return 0 for invalid subreddit
            return 0
    except requests.RequestException:
        # Handle any exceptions (network issues, etc.) and return 0
        return 0

