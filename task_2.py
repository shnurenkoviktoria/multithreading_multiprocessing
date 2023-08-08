import time
import threading
import multiprocessing


def root(num):
    x = 1
    x1 = 2

    while abs(x - x1) >= (1e-4):
        x = x1
        x1 = (x + num / x) / 2

    print(x1)


def input_num():
    global num
    print(
        """
_______________________________________________________________
Task 2: Develop a program to perform the same computational task in two ways: 
using multithreading and multiprocessing. 
Draw conclusions about the performance of each method.


The square root of according to Heron's irational formula.
_______________________________________________________________
"""
    )
    num = float(
        input("will enter a fixed positive number whose root we want to calculate:")
    )
    while num <= 0:
        num = float(
            input("will enter a fixed positive number whose root we want to calculate:")
        )


def threading_task():
    global time_thread
    print(
        f"""
_______________________________________________________________
Write a program with threads:
_______
the square root of {num} according to Heron's irational formula:
    """
    )
    time_start = time.time()
    thread1 = threading.Thread(target=root, args=[num])

    thread1.start()

    thread1.join()

    time_end = time.time()
    time_thread = time_end - time_start

    print(
        f"""
_______
Time : {time_thread}
_______________________________________________________________
    
    
    """
    )


def multiprocessing_task():
    global time_process
    print(
        f"""
_______________________________________________________________
Write a program with processes:
_______
the square root of {num} according to Heron's irational formula:"""
    )

    time_start = time.time()
    process1 = multiprocessing.Process(target=root, args=[num])

    process1.start()

    process1.join()

    time_end = time.time()

    time_process = time_end - time_start
    print(
        f"""
_______
Time : {time_process}
_______________________________________________________________
    
    

""")


def result():
    print("*" * 63)
    print("Result:")
    if time_thread > time_process:
        print(f"{time_thread} > {time_process}")
        print("Time of threading is more than multiprocessing")
    elif time_thread < time_process:
        print(f"{time_thread} < {time_process}")
        print("Time of threading is less than multiprocessing")
    else:
        print(f"{time_thread} = {time_process}")
        print("Time of threading is equal to multiprocessing")
    print("*" * 63)


if __name__ == "__main__":
    input_num()
    threading_task()
    multiprocessing_task()
    result()
