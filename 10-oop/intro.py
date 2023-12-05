
class Car:
    def __init__(self) -> None:
        self.model = ''
        self.gas = 0
        self.speed = 0
        self.lights = False

    def turn_lights_on(self):
        self.lights = True

    def turn_lights_off(self):
        self.lights = False

    def accelerate(self):
        self.speed += 5

    def slow_down(self):
        self.speed -= 5

    def stop(self):
        self.speed = 0

class Truck(Car):
    def __init__(self) -> None:
        super().__init__()
        self.capacity = 0


a = Car()
a.turn_lights_on()
a.accelerate()

b = Car()
b.accelerate()
b.accelerate()

print("A: ", a.speed)
print("B: ", b.speed)

x = Truck()


