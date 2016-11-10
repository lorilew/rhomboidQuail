import requests


def count_words_at_url(url):
    resp = requests.get(url)
    result = len(resp.text.split())
    print(result)
    return result