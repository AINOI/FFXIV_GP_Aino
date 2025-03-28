import csv
import re


def contains_japanese_kana(text):
    kana_pattern = re.compile(r'[\u3040-\u30FF]')
    return bool(kana_pattern.search(text))


def process_csv_files(first_csv, second_csv, target_col_index, copy_to_col_index):
    # Read the first CSV file
    with open(first_csv, 'r', encoding='utf-8', newline='') as file1:
        reader1 = csv.reader(file1)
        data1 = list(reader1)

    # Read the second CSV file
    with open(second_csv, 'r', encoding='utf-8', newline='') as file2:
        reader2 = csv.reader(file2)
        data2 = list(reader2)

    data2_dict = {row[0]: row for row in data2}

    for i, row in enumerate(data1):
        if i < 4:
            continue

        target_cell = row[target_col_index]

        # Check if the target cell contains Japanese Kana
        if contains_japanese_kana(target_cell):
            continue

        key = row[0]

        # Find the matching row in the second CSV using the key
        if key in data2_dict:
            data2_dict[key][copy_to_col_index] = target_cell

    # Write the modified data back to the second CSV file
    with open(second_csv, 'w', encoding='utf-8', newline='') as file2:
        writer2 = csv.writer(file2)
        writer2.writerows(data2)


# Example usage
# first_csv = 'H:\\Downloads\\rawexd_v2\\rawexd\\EObjName.csv'
# second_csv = 'D:\\FFXIV\\FFXIVChnTextPatchGP\\FFXIVChnTextPatch\\resource\\rawexd\\EObjName.csv'

first_csv = 'D:\\FFXIV\\FFXIVChnTextPatchGP\\FFXIVChnTextPatch\\resource\\rawexd\\BNpcName.csv'
second_csv = 'D:\\FFXIV\\FFXIVChnTextPatchGP\\FFXIVChnTextPatch\\docs\\scripts\\jp-700-eobj.csv'
target_col_index = 1
copy_to_col_index = 1

process_csv_files(first_csv, second_csv, target_col_index, copy_to_col_index)

first_csv = 'H:\\Downloads\\rawexd_v2\\rawexd\\BNpcName.csv'
process_csv_files(first_csv, second_csv, target_col_index, copy_to_col_index)


