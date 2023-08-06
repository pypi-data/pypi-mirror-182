import requests

def get_ip():
    res = requests.get('https://ipinfo.io/json')
    return res.text

def get_content(url):
    res_two = requests.get(url)
    return res_two.text
