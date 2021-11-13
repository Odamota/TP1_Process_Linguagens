def slurp(filename):
    with open(filename, "r") as fh:
        contents = fh.read()
    return contents

