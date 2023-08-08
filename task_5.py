import requests
import concurrent.futures
import time


def fetch_url(url):
    response = requests.get(url)
    return f"Fetched {url}, status code: {response.status_code}"


def sequential_requests():
    global sequential_time
    print("""
_______________________________________________________________
Task 5: Write a program that uses concurrent.futures to make 
many requests to the same website and compare the execution 
time with sequential requests.
_______________________________________________________________
Sequential requests:""")
    url = "https://ithillel.ua"
    num_requests = 10

    start_time = time.time()
    for _ in range(num_requests):
        result = fetch_url(url)
        print(result)
    end_time = time.time()
    sequential_time = end_time - start_time

    print(f"""
_______
Sequential requests took {sequential_time} seconds
_______________________________________________________________


""")


def parallel_requests():
    global parallel_time
    print("""
_______________________________________________________________
Parallel requests:""")
    url = "https://ithillel.ua"
    num_requests = 10

    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(fetch_url, url) for _ in range(num_requests)]

        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            print(result)
    end_time = time.time()
    parallel_time = end_time - start_time

    print(f"""
_______
Parallel requests took {parallel_time} seconds
_______________________________________________________________


""")


def result():
    print("*" * 63)
    print("Result:")
    if parallel_time < sequential_time:
        print(f"{parallel_time} < {sequential_time}")
        print("Parallel requests were faster")
    elif parallel_time > sequential_time:
        print(f"{parallel_time} > {sequential_time}")
        print("Sequential requests were faster")
    else:
        print(f"{parallel_time} = {sequential_time}")
        print("Sequential and parallel requests took the same time")
    print("*" * 63)


if __name__ == "__main__":
    sequential_requests()
    parallel_requests()
    result()
