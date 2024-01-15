import threading


def print_even_numbers():
    for i in range(2, 21, 2):
        print(f"Even: {i}")


def print_odd_numbers():
    for i in range(1, 20, 2):
        print(f"Odd: {i}")


if __name__ == "__main__":
    thread1 = threading.Thread(target=print_even_numbers)
    thread2 = threading.Thread(target=print_odd_numbers)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
