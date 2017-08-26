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


