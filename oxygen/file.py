from oxygen import buffer

def load(filename: str) -> buffer.Buffer:
    with open(filename) as file:
        return buffer.Buffer(file.readlines())