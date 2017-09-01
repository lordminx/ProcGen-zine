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
