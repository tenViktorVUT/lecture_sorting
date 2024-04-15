import csv
import os


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """

    num_dict = dict()

    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)

    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)
        iteration = 0
        # print(reader)
        for row in reader:
            for key, value in row.items():
                if iteration == 0:
                    num_dict[key] = [int(value)]
                else:
                    num_dict[key].append(int(value))
            iteration += 1
        return num_dict

def selection_sort(numdict: dict):
    """
    sorts values in a dictionary numdict
    :param numdict: dictionary of numbers
    :return: numdict: sorted dictionary of numbers
    """

    for value in numdict.values():
        for i in range(0, len(value)):
            for num in value:
                if num > value[i]:
                    value[value.index(num)], value[i] = value[i], value[value.index(num)]
                else:
                    continue

    return numdict

def main():
    # print(os.getcwd())
    print(selection_sort(read_data("numbers.csv")))
    # pass


if __name__ == '__main__':
    main()
