class Body:
    def __init__(self):
        self.Parent = ''
        self.Satellite = []

    def add_orbiting_body(self, name):
        self.Satellite.append(name)

    def set_parent(self, parent):
        self.Parent = parent


class Orbits:
    def __init__(self, values):
        self.Orbits = {}
        for orbit in values:
            name, satellite = orbit.split(")")
            if self.Orbits.get(name) is None:
                self.Orbits[name] = Body()
            if self.Orbits.get(satellite) is None:
                self.Orbits[satellite] = Body()
            self.Orbits[satellite].set_parent(name)
            self.Orbits[name].add_orbiting_body(satellite)

    def orbit_recurse(self, key, count):
        total = count
        for child in self.Orbits[key].Satellite:
            value = self.orbit_recurse(child, count + 1)
            total += value
        return total

    def orbits_to_start(self, current_key, wanted):
        path = []
        current_key = self.Orbits[current_key].Parent
        path.append(current_key)
        while current_key != wanted:
            current_key = self.Orbits[current_key].Parent
            path.append(current_key)
        return path

    def checksum(self):
        return self.orbit_recurse('COM', 0)

    def distance_between(self, start, end):
        # iterate through the path from YOU to COM
        start_to_com = self.orbits_to_start('YOU', 'COM')
        end_to_com = self.orbits_to_start('SAN', 'COM')
        x = len(set(start_to_com) - set(end_to_com))
        y = len(set(end_to_com) - set(start_to_com))

        return x + y
