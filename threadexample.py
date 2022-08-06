from threading import *
from time import sleep

class Hello(Thread):

    def run(self) -> None:
        for i in range(10):
            print("hello")
            sleep(0.5)

class Hi(Thread):
    def run(self) -> None:
        for i in range(10):
            print("hi")
            sleep(0.5)

thread_1 = Hello()
thread_2 = Hi()

thread_1.start()
thread_2.start()

thread_2.join()
thread_1.join()

print("bye")