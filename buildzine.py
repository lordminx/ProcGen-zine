from tempfile import TemporaryDirectory
from uuid import uuid4
from glob import glob
from os.path import join

from weasyprint import HTML
from generators.default import CoverGenerator
from jinja2 import Environment, FileSystemLoader


class ProcGenZine:
    def __init__(self, seed=None):

        if not seed: # generate a random UUID as seed
            self.seed = str(uuid4())
        self.template = self.get_template("zine.html")

    def get_template(self, template):
        """Get Jinja template from templates folder."""


        env = Environment(
            loader=FileSystemLoader('templates')
            )
        return env.get_template(template)

    def collect_css(self, location):
        """Collect CSS files from location."""
        css_files = glob(join(location, "*.css"))

        return css_files

    def create_zine(self, filename=None):
        """Build zine pdf from generators."""

        from generators import all_generators

        if not filename:
            filename = self.seed + ".pdf"

        with TemporaryDirectory(dir=".") as target:
            cover = CoverGenerator("./delete", self.seed)

            all_instances = [generator(target, self.seed) for generator in all_generators]

            source = self.template.render(cover=cover.generate(), generators=all_instances)
            HTML(string=source, base_url=".").write_pdf(filename)

        return filename

if __name__ == "__main__":
    zinemaker = ProcGenZine()

    print(zinemaker.create_zine())
