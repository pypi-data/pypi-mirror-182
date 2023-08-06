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

# Time/Timeline

A timeline used to describe events in time and their sequence.
You can try it on our website
[here](https://figular.com/tryit/time/timeline/). Here's a simple example:

![A basic example showing a timeline of the historic periods of Britain
 from Tudor times to present day](basic.png)

* [Suggested Purpose](#suggested-purpose)
* [Usage](#usage)
  * [Website Usage](#website-usage)
    * [Entering Data: Typing](#entering-data-typing)
    * [Entering Data: Spreadsheet](#entering-data-spreadsheet)
    * [Styling](#styling)
  * [Cmdline Usage](#cmdline-usage)
* [Limitations](#limitations)
* [Examples](#examples)

## Suggested Purpose

* To show past or future events and their relative position in time to each
  other.

## Usage

### Website Usage

Here's what you should see when you first visit the
[Timeline](https://figular.com/tryit/time/timeline/) page:

![A screenshot of https://figular.com/tryit/time/timeline/](website_screenshot.png)

You can enter the data for your timeline in the Data box, at the top left of
the page. The format of this data is in lines:

```text
DATE|TITLE|ENTRY
DATE|TITLE|ENTRY
...
```

There are up to three fields and they are separated by the `|` pipe symbol. The
three fields are:

* An optional DATE in YYYY/MM/DD format. For example 2022/01/23 represents the
  23rd Jan 2022.
  * If you do not specify a date then the it'll be assumed that this event sits
    evenly spaced between those before and after it. This can save typing.
  * Dates should be in ascending order. Dates which do not ascend are treated as
    if no date was given.
  * Date's which cannot be understood will be treated as a TITLE or
    ENTRY instead. If this happens check your date is correct.
* An optional TITLE for the label that'll be drawn over your date. Any
  text you like can go here.
* ENTRY is the text that'll describe the date you have entered. This is the
  minimum required to have something drawn.

Here's a full example for the British History timeline above:

```text1485/01/01|1485|Tudor Britain
1603/01/01|1603|Stuart Britain
1714/01/01|1714|Georgian Britain
1837/01/01|1837|Victorian Britain
1902/01/01|1902|Modern Britain
2022/01/01|2020s|Present Day
```

Finally you can hit the download button to get your image. By default this will
be in [PNG](https://en.wikipedia.org/wiki/Portable_Network_Graphics) format but
you can change this to
[SVG](https://en.wikipedia.org/wiki/Scalable_Vector_Graphics) with the toggles
underneath the download button.

#### Styling

In the 'Styling' section of the web page you can alter various style settings.
The settings are in groups which can be collapsed by clicking the shrink
icon in their header. There are four groups:

* Shape: these affect how the shape is drawn around the label of each date.
  * Background color: background of each shape.
  * Border color: the color of the border. Note the border will not be visible
    unless it has a width bigger than 0.
  * Border style: the style in which to draw the border: solid, dotted, dashed,
    longdashed, dashdotted, longdashdotted.
  * Border width: size or thickness of the border.
* Titles: these affect how the title is drawn for each date.
  * Color: color of the text.
  * Font size: size of the text/font, in points.
  * Font: the family or typeface to use for the text.
  * Font Weight: how heavy is the font, either normal or bold.
* Entries: these affect how the entry is drawn for each date.
  * Color: color of the text.
  * Font size: size of the text/font, in points.
  * Font: the family or typeface to use for the text.
  * Font Weight: how heavy is the font, either normal or bold.
* Lines: these affect how the lines are drawn between dates on the timeline.
  * Color: color of the lines.
  * Style: the style in which to draw the lines: solid, dotted, dashed,
    longdashed, dashdotted, longdashdotted.
  * Width: size or thickness of the lines.

See [Figular#styling](../../Figular.md#styling) for more detail on styling primitives.

### Cmdline Usage

Similar to the website the `fig` command expects the timeline expressed in
separate lines. Optional styling can be provided as a third argument:

```bash
fig time/timeline "$(cat << EOF
1485/01/01|1485|Tudor Britain
1603/01/01|1603|Stuart Britain
1714/01/01|1714|Georgian Britain
1837/01/01|1837|Victorian Britain
1902/01/01|1902|Modern Britain
EOF
)" "$(cat << EOF
{
  "shape": {
    "background_color": "white",
    "border_color": "black",
    "border_width": 3,
    "line": {
      "border_color": "red",
      "border_width": 2
    }
  },
  "textbox": {
    "color": "black",
    "font_family": "Helvetica"
  }
}
EOF
)"
```

All other rules and limitations apply expect that you can specify as much data
as a single cmdline will allow. See below for more cmdline examples.

You can style the primitive shapes, lines and text boxes of which the figure is
composed. The document object model looks like this:

* Shapes (per date). It has these children:
  * Text box (the entry) - 1st child
  * Text box (the title) - 2nd child
* Lines (drawn between dates on the timeline)

## Limitations

* Website only: we accept up to 5000 characters of data for now, so timelines
  will return an error. Let us know if this is a problem for you as we can
  adjust this.

## Examples

![Timeline of the final five films of Stanley Kubrick](kubrick.svg)

### On the Website

Enter the following into the text box:

```text
1971/01/01|1971|A Clockwork Orange
1975/01/01|1975|Barry Lyndon
1980/01/01|1980|The Shining
1987/01/01|1987|Full Metal Jacket
1999/01/01|1999|Eyes Wide Shut
```

Under Styling change the following:

* Shape: background color: darkmagenta, border width: 0
* Titles: font size: 20, font: courier, font weight: normal
* Lines: color: heavycyan, width: 3

### At the Cmdline

```bash
fig time/timeline "$(cat << EOF
1971/01/01|1971|A Clockwork Orange
1975/01/01|1975|Barry Lyndon
1980/01/01|1980|The Shining
1987/01/01|1987|Full Metal Jacket
1999/01/01|1999|Eyes Wide Shut
EOF
)" "$(cat << EOF
{
  "shape": {
    "background_color": "darkmagenta",
    "textbox_nth_child_2": {
      "font_size": 20,
      "font_family": "Courier",
      "font_weight": "normal"
    }
  },
  "line": {
    "border_color": "heavycyan",
    "border_width": 3
  }
}
EOF
)"
```

---

![Timeline of the Apollo 11 mission to the Moon](apollo11.svg)

This information is taken from Wikipedia's entry on [Apollo 11](https://en.wikipedia.org/wiki/Apollo_11)
and the official [Apollo 11 Timeline](https://history.nasa.gov/SP-4029/Apollo_11i_Timeline.htm).

### On the Website

Enter the following into the text box (truncated due to website size limits):

```text
1969/07/16|Liftoff|July 16th 1969
1969/07/19|Lunar Orbit|July 19th
1969/07/20|Lunar Landing|July 20th
1969/07/21|"One small step for man, one giant leap for mankind"|July 21st
1969/07/22|Return to Earth|July 22nd
1969/07/24|Splashdown|July 24th
```

Under Styling change:

* Shape: background color: royalblue, border width: 0
* Titles: color: palegrey, font size: 15, font: avant garde, font weight: bold
* Entries: color: heavygrey, font size: 9, font: helvetica, font weight: bold
* Lines: color: royalblue, style: solid, width: 9

### At the Cmdline

```bash
fig time/timeline "$(cat << EOF
1969/07/16|Liftoff|July 16th 1969
1969/07/19|Lunar Orbit|July 19th
1969/07/20|Lunar Landing|July 20th
1969/07/21|"One small step for man, one giant leap for mankind"|July 21st
1969/07/22|Return to Earth|July 22nd
1969/07/24|Splashdown|July 24th
EOF
)" "$(cat << EOF
{
  "shape": {
    "background_color": "royalblue",
    "textbox_nth_child_1": {
      "color": "heavygrey",
      "font_size": 9,
      "font_family": "Helvetica",
      "font_weight": "bold"
    },
    "textbox_nth_child_2": {
      "color": "palegrey",
      "font_size": 15,
      "font_family": "Avant Garde",
      "font_weight": "bold"
    }
  },
  "line": {
    "border_color": "royalblue",
    "border_width": 9
  }
}
EOF
)"
```
