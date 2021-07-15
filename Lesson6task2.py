#lesson6Task1


class Road:
    def __init__(self, leghth, width):
        self._leghth = leghth
        self._width = width

    def get_full_proffit(self, weight=25, thickners=0.05):
        return  f'{self._leghth} m * {self._width} m +{weight} kg * {thickners} m ='\
                f'{(self._leghth * self._width * weight * thickners) / 1000} t'


road_1 = Road(5000, 200)
print( road_1.get_full_proffit())