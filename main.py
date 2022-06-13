import requests as r
import time


def main():
    url = 'https://wallet-baiscs.kucoin-wallet.cc/basics/v1/promotion/add/email'
    with open('emails.txt', 'r') as file:
        emails = file.read().split("\n")

    for email in emails:
        res = r.post(url=url, json={"email": email})
        print(f"successful registered email {email}")
        print(res, res.text)
        time.sleep(1)


if __name__ == "__main__":
    main()
