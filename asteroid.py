from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.radius = radius
        super().__init__(x, y, self.radius)

        
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        rand_angle =  random.uniform(20, 50)
        vect_pos = self.velocity.rotate(rand_angle)
        vect_neg = self.velocity.rotate(-rand_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position.x, self.position.y, new_radius) 
        a1.velocity = vect_pos * 1.2
        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a2.velocity = vect_neg * 1.2
        

    def draw(self, screen):
        pygame.draw.circle(screen,"white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt