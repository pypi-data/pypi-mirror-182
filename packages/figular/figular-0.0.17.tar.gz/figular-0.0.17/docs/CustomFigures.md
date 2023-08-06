<!--
SPDX-FileCopyrightText: 2021-2 Galagic Limited, et al. <https://galagic.com>

SPDX-License-Identifier: CC-BY-SA-4.0

figular generates visualisations from flexible, reusable parts

For full copyright information see the AUTHORS file at the top-level
directory of this distribution or at
[AUTHORS](https://gitlab.com/thegalagic/figular/AUTHORS.md)

This work is licensed under the Creative Commons Attribution 4.0 International
License. You should have received a copy of the license along with this work.
If not, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to
Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
-->

# Custom Figures

There are two ways to add your own figures to Figular:

* [External Figures](#external-figures) - add an external Figure, usable at the
  cmdline only. Can be as simple as one file.
* [Internal Figures](#internal-figures) - add an internal Figure, usable at the
  cmdline, API and on the web.
  * [Cmdline](#cmdline)
  * [API](#api)
  * [Web](#web)
* [Note on Figure Input](#note-on-figure-input)
* [Debugging](#debugging)

## External Figures

To develop your own external figures you can provide custom Asymptote code to
the `fig` command:

```bash
fig mycode.asy DATA [STYLE]
```

Figular will expect your code to provide a `run` method we will call into:

```asymptote
void run(picture pic, string[] input) {
  ...
}
```

Any DATA provided on the cmdline will be available through the `input` argument,
split by lines. If DATA is not provided it will be taken from stdin. Any styling
will have already been setup as rules on our styledom. To take advantage just
use our drawing primitives and they will be styled accordingly. For example if
you create a file `myfile.asy` with this content:

```asymptote
import "figular/primitives" as primitives;

void run(picture pic, string[] input) {
  real radius = 20;
  page p = page(pic);

  for(int i = 0 ; i < input.length ; ++i) {
    pair pos = (i*radius*3, 0);
    circle c = circle(p, radius, pos);
    textbox(p, 2*radius, pos, input[i], c=c);
  }
  p.print();
}
```

You could then use it below supplying data and styling just like we do with the
build-in figures:

```bash
fig myfile.asy $'Hello\nThere' '{ "circle":{ "background_color": "pink" } }'
```

See [debugging](#debugging) below for help on solving issues.

## Internal Figures

There are several steps to adding a new figure. It's best to get it working at
the cmdline first for fast feedback before making it available via API and Web.

### Cmdline

Regarding the Asymptote code every figure has to provide this interface:

```asy
void run(picture pic, string[] input)
```

It is passed an array of lines of string input and a picture to draw on. Input
that will end up as text in a figure should be correctly escaped for LaTeX.

New figures should be created in the right subdir following our naming
convention of grouping similar figures together, e.g. `org/orgchart.asy`. If you
had to create a new directory than also place an empty `__init__.py` file there
so the dir is picked up for packaging.

Once a file is is placed the figure should then be runnable from the cmdline the
usual way:

```asy
fig org/orgchart DATA STYLE
```

See [debugging](#debugging) below for help on solving issues.

Then add tests in the style of those already at `tests/python/FIGURE` e.g.
`test/python/org/test_orgchart.py`. These should test the basic figures works
at the cmdline.

### API

To make your new figure available at the API add a new method to the end of `app/main.py`
that defines the route. It should be identical to the others already there apart
from the route and the figure filename. In future we hope to eliminate the need
for this.

Then add more tests to `tests/python/FIGURE`. These should now test some fuzzing
around the API input values to ensure safe results are always returned.

### Web

To make your new figure available as a web widget it requires corresponding
HTML. Look at our hugo widget `hugo/layouts/partials/widgets/figular.html` for
how others have been added. To test the HTML produced your new figure should be
added to the hugo test site at `tests/hugosite/content`, see the other figures
there for examples.

You can try the test site by running `hugo serve -s tests/hugosite`. Changes in
the source tree will be picked up by hugo and reflected immediately.

If you bring up the docker container you'll have a backend to hit and then be
able to test your Figure with a complete roundtrip: `podman run -d -p 8080:8080 figular`.

The resulting pages should be diffed against expected content as we already do
for existing figures so we know the HTML is correct. See the diff cmd in
`build.ninja` and expand it with your expected HTML under the dir `tests/html`.

### Documentation

Add documentation under dir `docs/figures`. Usually a figure will link
to this documentation from its `help_link` page param when added to a Hugo site.
A new entry for the figure should also be added to the complete list at `docs/Figular.md`

The cmdline tool also documents the available figures. Add the new figure to the
usage in the file `figular/command_line.py`.

## Note on Figure Input

The normal way a figure is run means input actually comes via a stdin pipe but
thanks to Asymptote's implicit casting of file to string[] we can not be aware
of this. We do not use Asymptote's built-in `stdin` as it enforces a '#'
[comment
character](https://asymptote.sourceforge.io/doc/Files.html#index-comment-character)
and this interferes with our interpretation (e.g. markdown).

## Debugging

There are several ways we can debug depending on what we want to examine:

* Debugging cmdline/python/package/figures - you can install the pip package as
  editable to get rapid feedback. Due to an open bug in Python this requires a
  bit of extra syntax.
  [Cannot install into user site directory with editable source](https://github.com/pypa/pip/issues/7953)
  The best solution is:

```bash
python3 -m pip install --prefix=$(python3 -m site --user-base) -e .
```

* Debugging standalone Asymptote code. Run a test asy file from anywhere with
  `fig FILE`, it can make imports as if it was running from the figular dir. If
  you combine this with the editable pip package above then you'll also get
  immediate feedback on any changes to asy or python code.

* Internal logging. Some code logs messages. At the moment we
  only support debug level. Switch debug logging on like this:

```asy
import "figular/logger" as ilogger;
logger.debugloglevel();
```

You can write to your own named logs too:

```asy
logger log = logger.getlogger("NAME");
log.debug("msg");
```
