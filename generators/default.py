import random


class DefaultGenerator:
    def __init__(self, filetarget, seed=None):
        self.dir = filetarget

        self.random = random.Random()
        if seed:
            self.random.seed(seed)

    def generate(self):
        return "DefaultValue"
