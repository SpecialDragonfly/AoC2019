class Util:
    def parse(self, file):
        print("Opening file " + file)
        f = open(file, "r")
        values = []
        if f.mode == 'r':
            lines = f.readlines()
            for line in lines:
                values.append(line.strip().split(","))
        f.close()
        return values
