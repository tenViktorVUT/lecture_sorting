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


def selection_sort(num_dict: dict, direction: bool = True):
    """
    sorts values in a dictionary numdict
    :param direction: direction of the sort reverse == False
    :param num_dict: dictionary of numbers
    :return: numdict: sorted dictionary of numbers
    """

    for value in num_dict.values():
        for i in range(0, len(value)):
            for num in value:
                if direction:
                    if num > value[i]:
                        value[value.index(num)], value[i] = value[i], value[value.index(num)]
                    else:
                        continue
                else:
                    if num < value[i]:
                        value[value.index(num)], value[i] = value[i], value[value.index(num)]
                    else:
                        continue

    return num_dict


def bubble_sort(num_dict: dict):
    """
    sorts list within a dictionary using bubble sort method
    :param num_dict: (dict): unsorted dictionary
    :return: num_dict: sorted dictionary
    """

    for value in num_dict.values():
        n = len(value)
        for i in range(n - 1):
            for num_idx in range(n - 1 - i):
                if value[num_idx] > value[num_idx + 1]:
                    value[num_idx], value[num_idx + 1] = value[num_idx + 1], value[num_idx]
                else:
                    continue

    """
    legacy code
    
    for value in num_dict.values():
        for idx, num in enumerate(value):
            while num > value[]:
                if value.index(num) == (len(value) - 1 - idx):
                    break
                else:
                    num, value[value.index(num) + 1] = value[value.index(num) + 1], num
    """
    return num_dict


def main():
    # print(os.getcwd())
    # print(selection_sort(read_data("numbers.csv")))
    print(bubble_sort(num_dict=read_data("numbers.csv")))
    # pass


if __name__ == '__main__':
    main()
