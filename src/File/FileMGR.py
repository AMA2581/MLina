class FileMGR:
    def fileReader(path):
        try:
            with open(path, "r") as file:
                return file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"The file at '{path}' was not found.")
        except IOError as e:
            raise IOError(f"An error occurred while reading the file: {e}")
