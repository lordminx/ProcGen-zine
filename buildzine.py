from tempfile import TemporaryDirectory
from weasyprint import HTML
from uuid import uuid4

class ProcGenZine:
    def __init__(self, seed=None):

        if not seed:
            self.seed = str(uuid4())
        self.template = self.get_template("zine.html")


    def get_template(self, template):
        from jinja2 import Environment, FileSystemLoader, select_autoescape
        env = Environment(
            loader=FileSystemLoader('templates'),
            autoescape=select_autoescape(['html', 'xml'])
            )
        return env.get_template(template)

    def create_zine(self, filename=None):
        from generators import all_generators

        if not filename:
            filename = self.seed + ".pdf"

        with TemporaryDirectory() as target:
            all_instances = [generator(target, self.seed) for generator in all_generators]

            source = self.template.render(cover="Testcover", generators=all_instances)

            HTML(string=source).write_pdf(filename)

        return "Done building file: " + filename


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
