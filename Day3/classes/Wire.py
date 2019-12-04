from __future__ import annotations


class Coord:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def to_string(self):
        return str(self.X) + "," + str(self.Y)

    def distance_from(self, x, y):
        return (abs(self.X) - abs(x)) + (abs(self.Y) - abs(y))


class Line:
    @staticmethod
    def intersect(line_one_start: Coord, line_one_end: Coord, line_two_start: Coord, line_two_end: Coord):
        if line_one_start.X != line_one_end.X:
            # line_one is horizontal
            # Make lines go outward from the origin regardless
            if abs(line_one_start.X) > abs(line_one_end.X):
                x = line_one_start
                line_one_start = line_one_end
                line_one_end = x

            if abs(line_two_start.Y) > abs(line_two_end.Y):
                y = line_two_start
                line_two_start = line_two_end
                line_two_end = y

            cross_in_x = line_one_start.X <= line_two_start.X <= line_one_end.X or \
                line_one_start.X >= line_two_start.X >= line_one_end.X
            cross_in_y = line_two_start.Y <= line_one_start.Y <= line_two_end.Y or \
                line_two_start.Y >= line_one_start.Y >= line_two_end.Y

            if cross_in_x and cross_in_y:
                return Coord(line_two_start.X, line_one_start.Y)
            else:
                return Coord(0, 0)
        else:
            val = Line.intersect(line_two_start, line_two_end, line_one_start, line_one_end)
            return val

    @staticmethod
    def orthogonal(line_one_start: Coord, line_one_end: Coord, line_two_start: Coord, line_two_end: Coord):
        v_vs_h = line_one_start.X == line_one_end.X and line_two_start.X != line_two_end.X
        h_vs_v = line_one_start.X != line_one_end.X and line_two_start.X == line_two_end.X
        return h_vs_v or v_vs_h

    @staticmethod
    def to_string(line_start, line_end):
        if line_start.X == line_end.X:
            return "(" + str(line_start.X) + ", " + str(line_start.Y) + "->" + str(line_end.Y) + ")"
        else:
            return "(" + str(line_start.X) + "->" + str(line_end.X) + ", " + str(line_start.Y) + ")"

    @staticmethod
    def contains_point(line_start, line_end, coord):
        if line_start.X == line_end.X == coord.X:
            return line_start.Y < coord.Y < line_end.Y or line_start.Y > coord.Y > line_end.Y
        elif line_start.Y == line_end.Y == coord.Y:
            return line_start.X < coord.X < line_end.X or line_start.X > coord.X > line_end.X
        return False

    @staticmethod
    def length(line_start, line_end):
        return abs(line_start.X - line_end.X) + abs(line_start.Y - line_end.Y)


class Wire:
    def __init__(self):
        self.Locations = []

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

    def distance_to(self, coord: Coord):
        distance = 0
        for i in range(0, len(self.Locations) - 1):
            if Line.contains_point(self.Locations[i], self.Locations[i + 1], coord):
                length = Line.length(self.Locations[i], coord)
                distance += length
                break
            else:
                length = Line.length(self.Locations[i], self.Locations[i + 1])
                distance += length
        return distance


class Grid:
    def __init__(self):
        self.Intersections = []

    def intersect(self, wire1: Wire, wire2:Wire):
        smallest_distance = 99999;
        for i in range(0, len(wire1.Locations) - 1):
            for j in range(0, len(wire2.Locations) - 1):
                if Line.orthogonal(wire1.Locations[i], wire1.Locations[i + 1], wire2.Locations[j], wire2.Locations[j + 1]):
                    intersect = Line.intersect(wire1.Locations[i], wire1.Locations[i + 1], wire2.Locations[j], wire2.Locations[j + 1])

                    # Non-intersecting lines will return 0,0
                    if not (intersect.X == 0 and intersect.Y == 0):
                        self.Intersections.append(intersect)
                        dist = intersect.distance_from(0, 0)
                        if dist < smallest_distance:
                            smallest_distance = dist
        return smallest_distance

