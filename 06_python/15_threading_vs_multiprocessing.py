#multiprocessing


from multiprocessing import Process
import os
import time


def square_numbers():
    for i in range(100):
        result = i * i



if __name__ == "__main__":
    processes = []
    num_processes = os.cpu_count()

    # create processes and asign a function for each process
    for i in range(num_processes):
        process = Process(target=square_numbers) # if arg in func (target=square_numbers, args=(i,))
        processes.append(process)

    # start all processes
    for process in processes:
        process.start()

    # wait for all processes to finish
    # block the main thread until these processes are finished
    for process in processes:
        process.join()

    print("end main")


from threading import Thread
import time

def square_numbers():
    for i in range(100):
        result = i * i


if __name__ == "__main__":
    threads = []
    num_threads = 15

    # create threads and asign a function for each thread
    for i in range(num_threads):
        thread = Thread(target=square_numbers) # if arg in func (target=square_numbers, args=(i,))
        threads.append(thread)

    # start all threads
    for thread in threads:
        thread.start()

    # wait for all threads to finish
    # block the main thread until these threads are finished
    for thread in threads:
        thread.join()

    print("end main")