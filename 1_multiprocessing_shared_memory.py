import multiprocessing


def square_list(mylist, result, square_sum):
    """
    function to square a given list
    """
    # append squares of mylist to result array
    for idx, num in enumerate(mylist):
        result[idx] = num * num

        # square_sum value
    square_sum.value = sum(result)

    # print result Array
    print("Result(in process p1): {}".format(result[:]))

    # print square_sum Value
    print("Sum of squares(in process p1): {}".format(square_sum.value))


if __name__ == "__main__":
    # input list
    mylist = [1, 2, 3, 4]

    # tworzy w pamięci liste która może przechowywać 4
    # zmienne o typie int
    result = multiprocessing.Array('i', 4)

    # tworzy zmienną, obiekt o typie int, jako drugi parametr można podać wartość domyślną
    square_sum = multiprocessing.Value('i')

    # creating new process
    p1 = multiprocessing.Process(target=square_list, args=(mylist, result, square_sum))

    # starting process
    p1.start()

    # wait until the process is finished
    p1.join()

    # print result array
    print("Result(in main program): {}".format(result[:]))

    # print square_sum Value
    print("Sum of squares(in main program): {}".format(square_sum.value)) 