import argparse
import json
import requests


def url_shorten(url):
    headers = {"content-type": "application/json"}
    api_url = "https://yesno.wtf/api"
    return requests.get(api_url)


def main():
    request = url_shorten("hoge")
    print(json.loads(request.text).get("answer"))


if __name__ == "__main__":
    main()
