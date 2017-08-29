from .default import DefaultGenerator


class NewGen(DefaultGenerator):

    def generate(self):
        additions = ["Random addition 1.", "Random addition 2.", "I'm not terribly interesting."]

        return "Hi, I'm NewGen: {addition}".format(addition=self.random.choice(additions))

