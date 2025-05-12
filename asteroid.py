from circleshape import *
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        
        if(self.radius < ASTEROID_MIN_RADIUS):
            return
        else:
            gen_angle = random.uniform(20,50)
            pos_angle = pygame.Vector2(self.velocity).rotate(gen_angle) 
            neg_angle = pygame.Vector2(self.velocity).rotate(-gen_angle) 
            new_rad = self.radius - ASTEROID_MIN_RADIUS

            new_a_1 = Asteroid(self.position.x, self.position.y, new_rad)
            new_a_2 = Asteroid(self.position.x, self.position.y, new_rad)
            new_a_1.velocity = pos_angle * 1.2
            new_a_2.velocity = neg_angle *1.2


        self.kill()