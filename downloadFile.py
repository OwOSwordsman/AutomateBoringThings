import requests

def main():
    file = requests.get('https://att-c.udemycdn.com/2020-04-01_07-52-38-341c4b5f71ee5d35e0e91685d4cd89fd/original.txt?response-content-disposition=attachment%3B+filename%3Dlesson39-recap.txt&Expires=1627930680&Signature=VKss~1q94DU38cb696PyPGBbdk~eIW6fOoAyIwQm2pH~7bFtQLh8cYHBwtEMuJUwkuIDKf24s8rCa5N56n7szsqswqcwlnX3aJFvdxKItsaQgNIgh3yUBlUftTBQ6ad1a5ayj8Rjp1VLFy3xoGYgH6-syku9WYX5q7vdFROROvL-f3rJj70YfHfrF6GS-Efi04thipO8OZxLepD8Ent07Ugx5QKEhFwD59FXzRV4ILLSJBIvsh5igDAnc078pCEdR70jhPQJV-wwpCZOPcID54jmDON9Q6Ljjhf3QHQfIZcVqHBrhLfVKRzC7ElMI-LO707OL034k3N4iaYXZulrzA__&Key-Pair-Id=APKAITJV77WS5ZT7262A')
    file.raise_for_status()
    with open('file.txt', 'wb') as f:
        for chunk in file.iter_content(10000):
            f.write(chunk)


if __name__ == '__main__':
    main()
