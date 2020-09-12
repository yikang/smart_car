from gpiozero import LED,Motor
from time import sleep

# GPIO PIN number on PI for motors 
BACK_PIN_1 = 22 
BACK_PIN_2 = 23 
FRONT_PIN_1 = 24
FRONT_PIN_2 = 25 

#<todo> Camera; obstatcle sensor

class RemoteCar():
    def __init__(self):
        self._backMotor = Motor(forward=BACK_PIN_1, backward=BACK_PIN_2)
        self._frontMotor = Motor(forward=FRONT_PIN_1, backward=FRONT_PIN_2)
        self.stop() 
        
    def drive(self,dir):
        if dir == 1:
            self._backMotor.forward()
        elif dir == -1:
            self._backMotor.backward()
        else:
            self._backMotor.stop()
    def turn(self,dir):
        if dir == 1:
            # turn right
            self._frontMotor.backward() 
        elif dir == -1:
            self._frontMotor.forward()
        else:
            self._frontMotor.stop()
    def stop(self):
        self.drive(0) 
        self.turn(0)
        
