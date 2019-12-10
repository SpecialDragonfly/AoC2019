class Util:
    def parse(self, file):
        print("Opening file " + file)
        f = open(file, "r")
        values = []
        if f.mode == 'r':
            lines = f.readlines()
            for line in lines:
                for x in line.strip().split(","):
                    values.append(int(x))
        f.close()
        return values
