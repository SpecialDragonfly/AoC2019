class Wire:
    Locations = []

    def trace(self, path):
        current_x = 0
        current_y = 0
        for value in path:
            direction = value[:1]
            distance = int(value[1:])
            if direction == "R":
                for i in range(0, distance):
                    current_x += 1
                    self.Locations.append(str(current_x) + "," + str(current_y))
            elif direction == "U":
                for i in range(0, distance):
                    current_y += 1
                    self.Locations.append(str(current_x) + "," + str(current_y))
            elif direction == "L":
                for i in range(0, distance):
                    current_x -= 1
                    self.Locations.append(str(current_x) + "," + str(current_y))
            elif direction == "D":
                for i in range(0, distance):
                    current_y -= 1
                    self.Locations.append(str(current_x) + "," + str(current_y))

    def locations(self):
        self.Locations = list(set(self.Locations))
        return self.Locations