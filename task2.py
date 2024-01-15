import threading
import multiprocessing
import time


def calculate_square(numbers):
    result = []
    start_time = time.time()
    for num in numbers:
        result.append(num * num)
        time.sleep(0.1)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Result: {result}")
    print(f"Execution time: {elapsed_time} seconds")


if __name__ == "__main__":
    numbers = list(range(1, 6))

    thread = threading.Thread(target=calculate_square, args=(numbers,))
    thread.start()
    thread.join()

    process = multiprocessing.Process(target=calculate_square, args=(numbers,))
    process.start()
    process.join()
