import multiprocessing


def square(number):
    return number ** 2


def compute_squares(numbers):
    pool = multiprocessing.Pool()
    results = pool.map(square, numbers)
    pool.close()
    pool.join()
    print(results)


if __name__ == '__main__':
    numbers = [1, 3, 5]
    compute_squares(numbers)
