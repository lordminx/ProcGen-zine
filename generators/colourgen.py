from .default import DefaultGenerator

class ColourGen(DefaultGenerator):

    def generate(self):
        # select number from #000000 to #ffffff to represent colour
        colourNumber = self.random.randint(0,0xffffff)

        # convert random number to colour representation string
        colourString = hex(colourNumber)[2:]

        return colourString
