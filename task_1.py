import multiprocessing
import time


def even_numbers():
    for i in range(2, 21, 2):
        print("Even:", i)
        time.sleep(0.01)


def odd_numbers():
    for i in range(1, 20, 2):
        print("Odd:", i)
        time.sleep(0.01)


def start():
    print(
        """
_______________________________________________________________
Task 1: Write a program with double threads:
one potik displays guys numbers,
the last one is unpaired numbers from 1 to 20.
_______"""
    )
    print("_" * 20)
    process1 = multiprocessing.Process(target=odd_numbers)
    process2 = multiprocessing.Process(target=even_numbers)

    time_start = time.time()

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    time_end = time.time()

    print(
        f"""
_______
Time : {time_end - time_start}
_______________________________________________________________"""
    )


if __name__ == "__main__":
    start()
