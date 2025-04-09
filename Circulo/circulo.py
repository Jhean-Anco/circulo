class circulo:
    PI = 3.14162425

    def __init__(self, radio):
        self.radio = radio

    def circunferencia(self):
        return 2*self.PI*self.radio

    def area(self):
        return self.PI*self.radio**2

if __name__ == "__main__":
    instancia_circulo = circulo(10)
    print(f"La circunferencia es: {instancia_circulo.circunferencia()}")
    print(f"El area de la circunferencia es: {instancia_circulo.area()}")


