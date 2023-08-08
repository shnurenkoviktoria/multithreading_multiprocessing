import multiprocessing
import requests
import time


def fetch_url(url):
    response = requests.get(url)

    with open(f"multiprocessing_{url.split('//')[1]}.html", "wb") as f:
        f.write(response.content)

    print(f"Fetched {url}, status code: {response.status_code}")


def multiprocessing_task():
    print(
        f"""
_______________________________________________________________
Task 4: Write a program that makes parallel requests toDevelop
an application that uses multiprocessing to make HTTP requests
to different websites at the same time. Use the requests
library and the multiprocessing module.
__________"""
    )

    urls = ["https://lms.ithillel.ua", "https://ithillel.ua", "https://github.com"]
    start_time = time.time()
    processes = []
    for url in urls:
        process = multiprocessing.Process(target=fetch_url, args=(url,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    end_time = time.time()

    print(
        f"""
_______    
Time : {end_time - start_time}
_______________________________________________________________"""
    )


if __name__ == "__main__":
    multiprocessing_task()
