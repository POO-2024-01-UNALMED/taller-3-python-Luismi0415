class TV:
    numTV = 0 

    def __init__(self, marca, estado):
        self.marca = marca
        self.canal = 1
        self.precio = 500
        self.estado = estado
        self.volumen = 1
        self.control = None
        TV.numTV += 1 

    def turnOff(self):
        self.estado = False

    def turnOn(self):
        self.estado = True

    def getEstado(self):
        return self.estado

    def canalUp(self):
        if self.canal < 120 and self.estado:
            self.canal += 1

    def canalDown(self):
        if self.canal > 1 and self.estado:
            self.canal -= 1

    def volumenUp(self):
        if self.volumen < 7 and self.estado:
            self.volumen += 1

    def volumenDown(self):
        if self.volumen > 0 and self.estado:
            self.volumen -= 1

    def getMarca(self):
        return self.marca

    def setMarca(self, nueva_marca):
        self.marca = nueva_marca

    def getCanal(self):
        return self.canal

    def setCanal(self, nuevo_canal):
        if 1 <= nuevo_canal <= 120 and self.estado:
            self.canal = nuevo_canal

    def getPrecio(self):
        return self.precio

    def setPrecio(self, nuevo_precio):
        self.precio = nuevo_precio

    def getVolumen(self):
        return self.volumen

    def setVolumen(self, nuevo_volumen):
        if 0 <= nuevo_volumen <= 7 and self.estado:
            self.volumen = nuevo_volumen

    def getControl(self):
        return self.control

    def setControl(self, control):
        self.control = control

   
    def getNumTV():
        return TV.numTV

    
    def setNumTV(num_tv):
        TV.numTV = num_tv