import os


class Cd:
    def __init__(self, dir_path):
        if not os.path.isdir(dir_path) or not os.path.exists(dir_path):
            raise ValueError(f"{dir_path} doesn't exist")
        self.dir_path = dir_path

    def __enter__(self):
        self.last_dir = os.getcwd()
        os.chdir(self.dir_path)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        os.chdir(self.last_dir)