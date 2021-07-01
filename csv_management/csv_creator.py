import os
import pathlib
import csv

def create_csv(folder, csv_name, headers, information_lists):
    """create csv file with a list of lists

    :param folder: name of the folder the file will be created into
    :param csv_name: name of the csv file
    :param headers: headers of the csv file (first row)
    :param information_lists: a list of lists of information
    """
    os.makedirs(pathlib.Path.cwd() / 'data' / folder, exist_ok=True)
    with open(
            pathlib.Path.cwd() / 'data' / folder / csv_name, 'w', newline='', encoding='utf-8-sig'
    ) as f:
        csv.writer(f).writerow(headers)
        for i in range(0, len(information_lists)):
            csv.writer(f).writerow(information_lists[i])