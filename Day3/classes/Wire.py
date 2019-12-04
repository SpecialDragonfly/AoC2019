from __future__ import annotations


class Coord:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def to_string(self):
        return str(self.X) + "," + str(self.Y)


class Line:
    @staticmethod
    def intersect(line_one_start: Coord, line_one_end: Coord, line_two_start: Coord, line_two_end: Coord):
        x = line_one_start.to_string() + "->" + line_one_end.to_string()
        y = line_two_start.to_string() + "->" + line_two_end.to_string()
        return x + " vs " + y

    @staticmethod
    def orthogonal(line_one_start: Coord, line_one_end: Coord, line_two_start: Coord, line_two_end: Coord):
        v_vs_h = line_one_start.X == line_one_end.X and line_two_start.X != line_two_end.X
        h_vs_v = line_one_start.X != line_one_end.X and line_two_start.X == line_two_end.X
        return h_vs_v or v_vs_h


class Wire:
    Locations = []

    def trace(self, path):
        current_x = 0
        current_y = 0
        self.Locations.append(Coord(0, 0))
        for value in path:
            direction = value[:1]
            distance = int(value[1:])
            if direction == "R":
                current_x += distance
            elif direction == "U":
                current_y += distance
            elif direction == "L":
                current_x -= distance
            elif direction == "D":
                current_y -= distance
            self.Locations.append(Coord(current_x, current_y))

    def intersect(self, wire: Wire):
        i = 0
        for j in range(0, len(wire.Locations), 2):
            print(
                self.Locations[i].to_string() + "->" +
                self.Locations[i+1].to_string() + " vs. " +
                wire.Locations[j].to_string() + "->" +
                wire.Locations[j+1].to_string()
            )
            if Line.orthogonal(self.Locations[i], self.Locations[i + 1], wire.Locations[j], wire.Locations[j+1]):
                print(Line.intersect(self.Locations[i], self.Locations[i + 1], wire.Locations[j], wire.Locations[j+1]))
            else:
                print("Lines weren't orthogonal")

