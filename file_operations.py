def read_data(file_name):
    with open(file_name, 'r', encoding='utf-8', errors='ignore') as file:
        data = file.read().split()
    return data


clear_words = read_data("clear_words.txt")
