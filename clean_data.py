import re


def clean_data(string):
    date_pattern = '[0-2]?[1-9]/[0-3]?[0-9]/20[0-1][1-9]'
    clean_string = re.sub(date_pattern, '', string)
    speech_pattern = 'SPEECH [0-9]'
    clean_string = re.sub(speech_pattern, '', clean_string)
    return clean_string


def read_file(filename):
    with open(filename, 'r') as readable_file:
        content = readable_file.read()
    return content


def write_file(filename, content):
    with open(filename, 'w') as writeable_file:
        writeable_file.write(content)


if __name__ == '__main__':
    file_location = '..\\data\\trump_speeches.txt'
    text = read_file(file_location)
    clean_string = clean_data(text)
    write_file(file_location, clean_string)
