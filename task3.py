import requests
import threading


def fetch_url(url, result_file):
    response = requests.get(url)
    with open(result_file, 'a') as file:
        file.write(f"{url}: {response.text}\n")
    print(f"Downloaded from {url}")


if __name__ == "__main__":
    urls = ["https://example.com", "https://google.com", "https://python.org"]
    result_file = "responses.txt"

    threads = []
    for url in urls:
        thread = threading.Thread(target=fetch_url, args=(url, result_file))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
