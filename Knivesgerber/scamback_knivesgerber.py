import requests
import names
import random
import string
import time


website = 'https://www.knivesgerber.com/my-account/'

email_provider = ["gmail.com", "gmx.net", "hotmail.com", "yahoo.com", "hotmail.co.uk", "msn.com"]


user_agent_list = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 12; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.360',
    'Mozilla/5.0 (Linux; Android 12; SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36'
]


def scam_back():
    email = names.get_full_name().replace(" ", ".") + "@" + random.choice(email_provider)
    password = ''.join(random.choice(string.ascii_letters) for i in range(random.randint(8, 12)))
    user_agent = random.choice(user_agent_list)
    headers = {'User-Agent': user_agent}

    payload = {
        'username': email.lower(),
        'password': password,
        'woocommerce-login-nonce': 'c74274b91b',
        '_wp_http_referer': '/my-account/',
        'login': 'Log in'
    }

    result = requests.post(website, allow_redirects=False, data=payload, headers=headers)
    print(f'Sending Fake Data to {website} with E-Mail: {email.lower()}, Password: {password}')
    print(result)


if __name__=="__main__":
    while True:
        scam_back()
        time.sleep(random.randint(1, 100))
