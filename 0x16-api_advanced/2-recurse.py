import requests

def recurse(subreddit, hot_list=[], after=None):
    # Define the Reddit API URL for hot posts with optional pagination
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {}
    if after:
        params['after'] = after

    try:
        # Make the GET request to the Reddit API
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, params=params, allow_redirects=False)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            
            # Extract the list of hot posts
            posts = data.get('data', {}).get('children', [])
            
            # If no posts are found, return None
            if not posts:
                return hot_list if hot_list else None

            # Add titles of the current page to the hot_list
            hot_list.extend(post.get('data', {}).get('title') for post in posts)
            
            # Get the 'after' parameter for pagination
            after = data.get('data', {}).get('after')
            
            # If there is more data, recurse with the new 'after' parameter
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
            
        else:
            # Print None if the subreddit is invalid
            return None
    except requests.RequestException:
        # Handle any exceptions (network issues, etc.) and return None
        return None

