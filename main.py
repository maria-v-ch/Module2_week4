from multiprocessing import Process
import multiprocessing


def square_number(number):
    return number ** 2


def compute_squares(numbers):
    squared_numbers = []
    for number in numbers:
        p = multiprocessing.Process(target=square_number, args=(number,))
        p.start()
        squared_numbers.append(square_number(number))
        p.join()
    return squared_numbers


if __name__ == '__main__':
    numbers = [1, 2, 3]
    print(compute_squares(numbers))
