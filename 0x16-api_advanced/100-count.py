import requests
import re
from collections import defaultdict

def count_words(subreddit, word_list, counts=None, after=None):
    # Initialize counts dictionary on first call
    if counts is None:
        counts = defaultdict(int)
    
    # Define the Reddit API URL for hot posts with optional pagination
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after} if after else {}

    try:
        # Make the GET request to the Reddit API
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, params=params, allow_redirects=False)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            
            # Extract the list of hot posts
            posts = data.get('data', {}).get('children', [])
            
            # If no posts are found, handle base case
            if not posts:
                return counts if any(counts.values()) else None

            # Process each post
            for post in posts:
                title = post.get('data', {}).get('title', '').lower()
                # Count occurrences of each keyword in the title
                for word in word_list:
                    word = word.lower()
                    # Create a regex pattern to match the keyword
                    pattern = re.compile(r'\b' + re.escape(word) + r'\b')
                    counts[word] += len(pattern.findall(title))
            
            # Get the 'after' parameter for pagination
            after = data.get('data', {}).get('after')
            
            # If there is more data, recurse with the new 'after' parameter
            if after:
                return count_words(subreddit, word_list, counts, after)
            else:
                # Print the results
                sorted_counts = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
                for word, count in sorted_counts:
                    if count > 0:
                        print(f"{word}: {count}")
                return counts
            
        else:
            # Print nothing if the subreddit is invalid
            return None
    except requests.RequestException:
        # Handle any exceptions (network issues, etc.) and return None
        return None

