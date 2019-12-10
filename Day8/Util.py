class Util:
    def parse(self, file):
        print("Opening file " + file)
        f = open(file, "r")
        values = []
        if f.mode == 'r':
            lines = f.readlines()
            for line in lines:
                for digit in list(line):
                    values.append(int(digit))
        f.close()
        return values
