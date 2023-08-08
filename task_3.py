import threading
import time

import requests


def fetch_url(url):
    response = requests.get(url)

    with open(f"threading_{url.split('//')[1]}.html", "wb") as f:
        f.write(response.content)
    print(f"Fetched {url}, status code: {response.status_code}")


def threading_task():
    print(
        f"""
_______________________________________________________________
Task 3: Write a program that makes parallel requests to 
multiple URLs and saves the responses to a file.
Use the requests library and the threading module.
__________
"""
    )
    urls = ["https://lms.ithillel.ua", "https://ithillel.ua", "https://github.com"]
    start_time = time.time()
    threads = []
    for url in urls:
        thread = threading.Thread(target=fetch_url, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

        end_time = time.time()

    print(
        f"""
_______    
Time : {end_time - start_time}
_______________________________________________________________"""
    )


if __name__ == "__main__":
    threading_task()
