import requests

def top_ten(subreddit):
    # Define the Reddit API URL for hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    
    try:
        # Make the GET request to the Reddit API
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, allow_redirects=False)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            
            # Extract the list of hot posts
            posts = data.get('data', {}).get('children', [])
            
            # Print the titles of the first 10 posts
            for i, post in enumerate(posts[:10]):
                print(post.get('data', {}).get('title', 'No title'))
        else:
            # Print None if the subreddit is invalid
            print(None)
    except requests.RequestException:
        # Handle any exceptions (network issues, etc.) and print None
        print(None)

