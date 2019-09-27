# manage file and dir

import os


def get_filelist(path):
    # get file list
    files = os.listdir(path)
    # print(dirs)
    return files
    # for file in dirs:
    #     print(file)


def read_file(file_name):
    # read file and get raw data
    raw_data=[]
    with open(file_name) as data_file:
        for line in data_file:
            line = line.replace('\n','').strip()
            raw_data.extend(line.split(','))
        # print(raw_data)
    return raw_data


def get_data(raw_data, type='float'):
    # get data and convert to target type
    data = []
    if type == 'float':
        data = list(map(float,raw_data))
    elif type == 'int':
        data = list(map(int, raw_data))
    else:
        data = raw_data
    return data


def main():
    path = r'D:\workspace\pycharm201803\cdes1201dataanalysis\session02\data'
    files = get_filelist(path)
    # print(files,type(files))

    raw_data = read_file(os.path.join(path, files[1]))
    # print(raw_data)

    print(get_data(raw_data))
    print(get_data(raw_data, 'int'))


if __name__ == "__main__":
    main()
