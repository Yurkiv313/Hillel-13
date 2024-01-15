import requests
from multiprocessing import Process


def fetch_url(url, result_file):
    response = requests.get(url)
    with open(result_file, 'a') as file:
        file.write(f"{url}: {response.text}\n")
    print(f"Downloaded from {url}")


if __name__ == "__main__":
    urls = ["https://example.com", "https://google.com", "https://python.org"]
    result_file = "responses.txt"

    processes = []
    for url in urls:
        process = Process(target=fetch_url, args=(url, result_file))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()
