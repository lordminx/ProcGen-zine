import random


class DefaultGenerator:
    def __init__(self, filetarget, seed):
        self.dir = filetarget

        self.random = random.Random()
        self.random.seed(seed)

    def generate(self):
        return "DefaultValue"
