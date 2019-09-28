# manage file and dir
# read files from specified path

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


def get_basedir():
    base_dir = os.path.dirname(os.path.abspath(__name__))
    return base_dir


def get_current_path():
    pwd = os.getcwd()
    return pwd


def get_father_path():
    pwd = get_current_path()
    father_path = os.path.abspath(os.path.dirname(pwd) + os.path.sep + ".")
    return father_path


def get_grader_father():
    pwd = get_current_path()
    grader_father = os.path.abspath(os.path.dirname(pwd) + os.path.sep + "..")
    return grader_father


def main():
    # path = r'D:\workspace\pycharm201803\cdes1201dataanalysis\session02\data'
    path = get_father_path() + os.path.sep + "data"
    files = get_filelist(path)
    # print(files,type(files))

    raw_data = read_file(os.path.join(path, files[1]))
    # print(raw_data)

    print(get_data(raw_data))
    print(get_data(raw_data, 'int'))


def print_dirs():
    print("baseDir=",get_basedir())
    print("currentPath=", get_current_path())
    print("fatherPath=", get_father_path())
    print("graderFather=", get_grader_father())


if __name__ == "__main__":
    main()
    print_dirs()
