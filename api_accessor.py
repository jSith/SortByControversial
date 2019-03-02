import requests


def get_controversial_posts(subreddit, response_size=100):
    """
    :param subreddit: String containing subreddit name, like 'politics' (no r/ required)
    :param response_size: Int indicating how many results to return
    :return: A list of most controversial posts for that sub, contained in a dictionary
    """
    url = f"https://api.reddit.com/r/{subreddit}/controversial?limit={response_size}"
    response = requests.get(url)
    if response.ok and response.content is not None:
        return list(post['data'] for post in response.json()['data']['children'])
    else:
        raise RuntimeError()

