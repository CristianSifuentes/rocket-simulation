# src/physics.py
class Physics:
    def __init__(self, mass, velocity):
        self.mass = mass
        self.velocity = velocity
        self.gravity = 9.81  # m/s^2
    
    def update(self, thrust, time):
        # Simula la aceleración y el impacto de la gravedad
        acceleration = (thrust - (self.mass * self.gravity)) / self.mass
        self.velocity += acceleration * time
        return self.velocity
