class circulo:
    PI = 3.14162425

    def __init__(self, radio):
        self.radio = radio

    def circunferencia(self):
        return 2*self.PI*self.radio

if __name__ == "__main__":
    instancia_circulo = circulo(10)
    print(f"La circunferencia es: {instancia_circulo.circunferencia()}")

