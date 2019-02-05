import random
from jinja2 import Template


class DefaultGenerator:
    def __init__(self, filetarget, seed=None):
        self.dir = filetarget

        self.random = random.Random()
        if seed:
            self.random.seed(seed)

        self.one_page = Template("<h2>{{title}}</h2>\n<em>by <b>{{author}}</b></em>\n<p>{{content}}</p>")

    def generate(self):
        return self.one_page.render(title="Default Text", author="DefaultGenerator", content="Some terribly boring default text like Lorem Ipsum, but I couldn't be arsed to even implement that.")


class CoverGenerator(DefaultGenerator):
    def __init__(self, filetarget, seed):
        DefaultGenerator.__init__(self, filetarget, seed)

    def _random_image(self, size=(800, 1130), tag="random"):
        import io

        import requests as r
        from PIL import Image

        response = r.get("http://loremflickr.com/{size[0]}/{size[1]}/{tag}".format(size=size, tag=tag))

        image = Image.open(io.BytesIO(response.content))

        filepath = self.dir + "/cover.png"

        image.save(filepath)

        return filepath

    def generate(self):

        return "<img src='{}' alt='cover.png' />".format(self._random_image())


