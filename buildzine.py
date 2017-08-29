import inspect
import random

from tempfile import TemporaryDirectory


class ProcGenZine:
    def __init__(self, seed=None):

        self.seed = seed

    def create_zine(self):
        from generators import all_generators
        html = ""

        with TemporaryDirectory() as target:

            for gen in all_generators:
                try:
                    gen = gen(target, self.seed)
                    chapter = gen.generate()
                    html += chapter
                except Exception as e:
                    print("ERROR: Could not generate chapter from", gen)
                    raise e

        return html


"""
def get_generators():
    "Get a list of generators and return an instantiated list of them."
    gens = []
    for key, val in globals().copy().items():
        if inspect.ismodule(val):
            for x in dir(val):
                print("Inspecting:", key)
                item = getattr(val, x)
                if inspect.isclass(item):
                    if issubclass(item, default.ProcGen) and item is not default.ProcGen:
                        try:
                            gens.append(item())
                            print("Added:", item)
                        except Exception as e:
                            print(e)

    return gens

"""

if __name__ == "__main__":
    zinemaker = ProcGenZine()

    print(zinemaker.create_zine())
