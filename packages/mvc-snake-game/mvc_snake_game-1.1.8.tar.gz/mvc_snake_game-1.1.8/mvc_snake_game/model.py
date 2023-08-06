import random, pygame

clock = pygame.time.Clock()

class Game:
    def __init__(self) -> None:
        self.fps = 120

    def update(self):
        pygame.display.update()
        clock.tick(self.fps)

    def menu(self,window):
        window.main_menu()
        self.update()
    
    def score_menu(self,window):
        window.high_score_menu()
        self.update()
    
    def game(self,window):
        window.update()
        self.update()
    
    def select_diff(self,window, game):
        window.select_difficult(game)
        self.update()

class Fruit:

    def __init__(self, num_grid):
        self.num_grid = num_grid
        self.move()

    def move(self):
        self.x = random.randint(0, self.num_grid - 1)
        self.y = random.randint(0, self.num_grid - 1)

class Snake:

    def __init__(self, num_grid):
        self.x = num_grid / 2
        self.y = num_grid / 2
        self.direction = (1, 0)
        self.count = 0
        self.fruit = Fruit(num_grid)
        self.tail = []
        self.num_grid = num_grid
        self.score = 0

    def get_head_pos(self):
        return self.x, self.y

    def set_direction(self, direction):
        if self.direction[0] == 0 and not direction[0] == 0:
            self.direction = direction
        if self.direction[1] == 0 and not direction[1] == 0:
            self.direction = direction
        
    def update(self):
        if self.x == self.fruit.x and self.y == self.fruit.y:
            self.score += 1
            self.fruit.move()
            self.tail.append([self.x, self.y])
        if self.x >= self.num_grid or self.y >= self.num_grid or self.x < 0 or self.y < 0:
            return True
        if self.count % 20 == 0:
            for i, segment in enumerate(reversed(self.tail)):
                if i == len(self.tail) - 1:
                    segment[0] = self.x
                    segment[1] = self.y

                else:
                    segment[0] = list(reversed(self.tail))[i + 1][0]
                    segment[1] = list(reversed(self.tail))[i + 1][1]
            dx, dy = self.direction
            self.x += dx
            self.y += dy
            for segment in self.tail:
                if segment[0] == self.x and segment[1] == self.y:
                    return True

        self.count += 1
        return False
    
    def dead(self):
        self.score = 0
        self.tail = []