#lesson6Task1


import time
import intertools


class TrafficLight:
    __color = [['red', [7, 31]], ['yellow', [2, 33]], ['green', [7, 32]], ['yellow', [2, 33]]]

    def running(self):
        for light in intertools.cycle(self.__color):
            print(f"\r\033[{light[1][1]}n\033(1m{light[0]}\033[0m", end="")
            time.sleep(light[1][0])


trafficlight_1 = TrafficLight()
trafficlight_1.running()