import requests
import concurrent.futures
import time


def fetch_url(url):
    response = requests.get(url)
    return response.text


def sequential_requests(urls):
    start_time = time.time()
    for url in urls:
        fetch_url(url)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Sequential Execution Time: {elapsed_time} seconds")


def concurrent_requests(urls):
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(fetch_url, url) for url in urls]
        concurrent.futures.wait(futures)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Concurrent Execution Time: {elapsed_time} seconds")


if __name__ == "__main__":
    urls = ["https://www.example.com"] * 5

    sequential_requests(urls)

    concurrent_requests(urls)
