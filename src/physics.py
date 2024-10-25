# src/physics.py
# ¡Cambio inesperado en el archivo por killer2!
class Propulsion:
    def __init__(self, fuel_mass, burn_rate):
        self.fuel_mass = fuel_mass
        self.burn_rate = burn_rate
    
    def update_fuel(self, time):
        fuel_consumed = self.burn_rate * time
        self.fuel_mass -= fuel_consumed
        return self.fuel_mass
    def update(self, thrust, time):
        # Simula la aceleración y el impacto de la gravedad
        acceleration = (thrust - (self.mass * self.gravity)) / self.mass
        self.velocity += acceleration * time
        return self.velocity

