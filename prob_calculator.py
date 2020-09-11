import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = [key for key, value in kwargs.items() for i in range(value)]

    def draw(self, draw_number):
        if draw_number <= len(self.contents):
            return random.sample(self.contents,draw_number)
        else:
            return self.contents

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    for i in range(num_experiments):
        match = False
        result = {}
        for x in hat.draw(num_balls_drawn):
            result[x] = result.get(x, 0) + 1

        for k in expected_balls:
            if k in result and result[k] >= expected_balls[k]:
                match = True
            else:
                match = False
                break

        if match == True: M += 1 
    return M / num_experiments