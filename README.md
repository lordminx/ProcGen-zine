# ProcGenZine, a procedurally generated zine on procedural generation.

## Basic Idea

This project aims to build a set of scripts (and eventually a website) to build a print-ready [zine](https://en.wikipedia.org/wiki/Zine) about [Procedural Generation](https://en.wikipedia.org/wiki/Procedural_generation), but instead of designing it manually, the zine would be procgen itself.

Individual issues would be built from stable sets of ProcGen generators (Issue 0 from one set, Issue 1 from another, etc.), but within an issue, every download/run of the ProcGenZine would run those generators from a different seed, resulting in a unique copy of each issue. 

(The generators should be deterministic, ie. running them with e same seed would result in the same ProcGenZine copy. Seeds would be visible in the copy to allow for easy recreation of particularly fun copies. Or personalization or whatever.)

This projects, for now, aims to build a framework for zine generation and hopes to find other weirdos interested in contributing both individual generators and to the framework itself.

## Rough sketch of an architecture

So far, I imagine that most of the tooling for this happens in python, mainly because I like and know python. (Although the generators could probably be written in any kind language later on.) 

To generate pdfs for printing the zine, I can see two options:

1. LaTeX:
    Generators produce content (Text, images, etc.) that is then barfed into some kind of LaTeX template and then rendered into a pdf. This would, almost certainly, work, but there are few things in IT that I dislike as much as LaTeX, so I'd prefer not to go that way.

2. Weasyprint:
    The other common tool to produce pdfs from python is Weasyprint, which takes HTML and CSS and uses it to render pdfs. While I'm not a big fan of HTML and CSS either, first test have been promising. (And CSS' paged media standards looks quite workable.)

So the software has to produce html somehow. Either the generators produce their own html source (and maybe their own stylesheet) which are then just glued together in a lean jinja template and fed into Weasyprint OR the generators just produce the content itself (Raw text, images, some metadata) which the progrem them puts into a slightly more complicated template before rendering.

The former would allow more control to the generators authors to style their entries, while making it harder to write and debug the generator code. The latter would make for same-y looking entries, but probably less of a headache.

(I could also see a hybrid method, where generators produce some standard object which comes with flags describing how the output should be used, allowing the authors to decide whether to fiddle with their own style or not. Some standardisation between generators would be necessary anyway.)


## API

The core of the API (as it stands now, anyway) is the `ProcGenZine` class in [buildzine.py](buildzine.py). (Which will almost certainly be renamed at some point.) It does most of the heavy listing regarding html source generation and also generate the pdf.

### The Basic Workflow:

1. Instantiate `ProcGenZine`:
    
    ```python
    from buildzine import ProcGenZine

    zinebuilder = ProcGenZine()

    # ProcGenZine can also take a seed value for use in the generation process
    deterministic_zine = ProcGenZine(seed="I can haz zine plz?")
    ```
    If no seed value is given, a random value will be generated with `uuid.uuid4` and used as seed.

2. Generate Zine:
    
    ```python
    zinebuilder.create_zine()   // Creates a pdf file called <seed value>.pdf

    # Optionally, a filename can be given.

    zinebuilder.create_zine("newzine.pdf")
    ```
    Under the hood, `ProcGenZine.generate_zine()` calls `from generators import all_generators`, which imports a list of generator classes. These classes are then instantiated with a `target` (A temporary directory where generated iimages, sourcefiles, etc. can be saved.) and the seed value.
    Then, the list of objects is handed over to [a Jinja2 template](templates/zine.html) which calls each generator objects `generate` method and renders that functions output into the html source.
    At last, this source is then used with `weasyprint.HTML` to render and save a pdf file.



## Project Status

So far, this is in the super-early stages. Besides this document, I have some vague scripts and templates which I intend to clean up and push to the repo soonish.
