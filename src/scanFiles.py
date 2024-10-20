import os


def scanFiles(filepath):
    if not os.path.exists(filepath):
        os.mkdir(filepath)
    files = dict()
    queue = [filepath]
    while queue:
        path = queue.pop(0)
        if os.path.isdir(path):
            queue += [os.path.join(path, file) for file in os.listdir(path)]
        else:
            filename = os.path.split(path)[0]
            files[filename] = path
    return files


def getCurDirectory():
    return os.path.dirname(__file__)[:-3]


if __name__ == '__main__':
    print(getCurDirectory())
