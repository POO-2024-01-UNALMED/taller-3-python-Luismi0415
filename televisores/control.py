class Control:
    
    def __init__(self):
        self.tv = None

    def turnOn(self):
        if self.tv:
            self.tv.turnOn()

    def turnOff(self):
        if self.tv:
            self.tv.turnOff()

    def canalUp(self):
        if self.tv:
            self.tv.canalUp()

    def canalDown(self):
        if self.tv:
            self.tv.canalDown()

    def volumenUp(self):
        if self.tv:
            self.tv.volumenUp()

    def volumenDown(self):
        if self.tv:
            self.tv.volumenDown()

    def setCanal(self, canal):
        if self.tv:
            self.tv.setCanal(canal)

    def setVolumen(self, volumen):
        if self.tv:
            self.tv.setVolumen(volumen)

    def enlazar(self, tv):
        tv.setControl(self)
        self.tv = tv

    def getTv(self):
        return self.tv

    def setTv(self, tv):
        self.tv = tv