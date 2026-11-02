class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        self.planet_years = {
            "earth": 1.0,
            "mercury": 0.2408467,
            "venus": 0.61519726,
            "mars": 1.8808158,
            "jupiter": 11.862615,
            "saturn": 29.447498,
            "uranus": 84.016846,
            "neptune": 164.79132
        }

    def calculate_age(self, planet):
        result = self.seconds / 31557600 / self.planet_years[planet]
        return round(result, 2)

    def on_earth(self):
        return self.calculate_age("earth")

    def on_mercury(self):
        return self.calculate_age("mercury")

    def on_venus(self):
        return self.calculate_age("venus")

    def on_mars(self):
        return self.calculate_age("mars")

    def on_jupiter(self):
        return self.calculate_age("jupiter")

    def on_saturn(self):
        return self.calculate_age("saturn")

    def on_uranus(self):
        return self.calculate_age("uranus")

    def on_neptune(self):
        return self.calculate_age("neptune")