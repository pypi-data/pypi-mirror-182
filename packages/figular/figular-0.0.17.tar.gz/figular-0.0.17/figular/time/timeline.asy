// SPDX-FileCopyrightText: 2021-2 Galagic Limited, et al. <https://galagic.com>
//
// SPDX-License-Identifier: AGPL-3.0-or-later
//
// figular generates visualisations from flexible, reusable parts
//
// For full copyright information see the AUTHORS file at the top-level
// directory of this distribution or at
// [AUTHORS](https://gitlab.com/thegalagic/figular/AUTHORS.md)
//
// This program is free software: you can redistribute it and/or modify it under
// the terms of the GNU Affero General Public License as published by the Free
// Software Foundation, either version 3 of the License, or (at your option) any
// later version.
//
// This program is distributed in the hope that it will be useful, but WITHOUT
// ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
// FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more
// details.
//
// You should have received a copy of the GNU Affero General Public License
// along with this program. If not, see <https://www.gnu.org/licenses/>.

import "figular/cleanse.asy" as icleanse;
import "figular/date.asy" as idate;
import "figular/page.asy" as ipage;
import "figular/styledom" as istyledom;
import "figular/stylereset.asy" as istylereset;

/******************************************************************************
* Our styling
*******************************************************************************/

style textstyle = style(font_family=font.helvetica, font_size=9pt);
dom_styledom.addrule(stylerule(selectorlist(selector(elementtype.textbox, 1)), textstyle));
style titlestyle = style(font_family=font.computermodern_roman_bold, font_size=12pt);
dom_styledom.addrule(stylerule(selectorlist(selector(elementtype.shape),
                               selector(elementtype.textbox, 2)),
                               titlestyle));

/******************************************************************************
* Dated Entry
*******************************************************************************/

struct datedentry {
  date d;
  string title;
  string entry;

  void operator init(date d, string title, string entry) {
    this.d = d;
    this.title = title;
    this.entry = entry;
  }
}

/******************************************************************************
* Gapper
*******************************************************************************/

struct gapper {
  private real mingap;
  private real mintime = realMax;
  private real[] gaps;

  public void operator init(datedentry[] de, real mingap) {
    this.mingap = mingap;
    date prevdate = nulldate;

    for(int i = 0; i < de.length ; ++i) {
      if(i == 0) {
        gaps.push(0);
      }
      if(de[i].d != nulldate) {
        if(prevdate != nulldate) {
          if(de[i].d < prevdate) {
            abort("dates must be in ascending order");
          }
          // use gap to fill array we've fallen behind in
          real timediff = (de[i].d - prevdate) / (i - (gaps.length-1));
          int diff = i - (gaps.length-1);
          while(--diff >= 0) {
            gaps.push(timediff);
          }
          if(timediff < mintime) {
            mintime = timediff;
          }
        } else {
          int diff = i - (gaps.length-1);
          while(--diff >= 0) {
            gaps.push(-1);
          }
        }
        prevdate = de[i].d;
      }
    }

    int diff = de.length - gaps.length;
    while(--diff >= 0) {
      gaps.push(-1);
    }
  }

  public real[] gaps() {
    real[] result;
    real cumulativegap;
    real nextgap;

    for(real gap: gaps) {
      if(gap == 0) {
        nextgap = 0;
      } else if(gap == -1) {
        nextgap = mingap;
      } else {
        nextgap = (gap/mintime) * mingap;
      }
      cumulativegap += nextgap;
      result.push(cumulativegap);
    }
    return result;
  }
}

/******************************************************************************
* Timeline Functions
*******************************************************************************/

void makelabel(page p, string title, string entry, real xpos, real assumed_font_size, real fixedwidth) {
  // Forced to make container first with a dummy path
  path g = (0,0) -- (10, 0) -- (10, 10) -- (0, 10) -- cycle;
  shape s = shape(p, g);
  real titleboxheight = 0;
  real entryboxheight = 0;

  // Create the textboxes with container parent
  if(length(entry) > 0) {
    textbox entrybox = textbox(p, width=fixedwidth, place=(xpos, 0), align=N, entry, c=s);
    entryboxheight = entrybox.size().y;
  }
  if(length(title) > 0) {
    textbox titlebox = textbox(p, width=fixedwidth, place=(xpos, -entryboxheight), align=N, title, c=s);
    titleboxheight = titlebox.size().y;
  }

  // Now we can make real container path as we have text sizes
  real corner_dia = assumed_font_size ;
  real card_width = fixedwidth + assumed_font_size;
  real card_height = entryboxheight + titleboxheight + assumed_font_size;
  path g = (-card_width/2, card_height/2 - corner_dia/2)--
              (-card_width/2,-card_height/2 + corner_dia/2){down}..
              (-card_width/2+corner_dia/2,-card_height/2)--
              (card_width/2-corner_dia/2,-card_height/2){right}..
              (card_width/2,-card_height/2 + corner_dia/2)--
              (card_width/2, card_height/2 - corner_dia/2){up}..
              (card_width/2-corner_dia/2,card_height/2)--
              (-card_width/2+corner_dia/2,card_height/2){left}..
              cycle;
  g = shift(xpos, min(g).y + (assumed_font_size/2))*g;
  s.change(g);
}

void drawtimeline(page p, datedentry[] de, real assumed_font_size) {
  // 12x is a good factor for a reasonable paragraph/col width
  real fixedwidth = assumed_font_size * 12 ;
  real fixedwidthpadded = fixedwidth + (2 * assumed_font_size);

  gapper g = gapper(de, fixedwidthpadded);
  real[] gaps = g.gaps();

  for(int i = 0 ; i < gaps.length ; ++i) {
    primitives.line(p, (gaps[i], 0) -- (gaps[i], (2*assumed_font_size)));
    makelabel(p, de[i].title, de[i].entry, gaps[i], assumed_font_size, fixedwidth);
  }

  if(gaps.length > 0) {
    path timeline = (0, (2*assumed_font_size)) -- (gaps[gaps.length-1], (2*assumed_font_size));
    primitives.line(p, timeline);
  }
}

datedentry[] normalise(string[] input) {
  datedentry[] de;
  string[] parts;
  date prevdate = nulldate;

  for(string line: input) {
    parts = split(line, "|");
    date d = nulldate;
    string title = "";
    string entry = "";
    bool content = false;

    if(length(parts[0]) > 0) {
      d = parsedate(parts[0]);
      if(d != nulldate) {
        content = true;
        parts.delete(0);
        if(prevdate == nulldate || d >= prevdate) {
          prevdate = d;
        } else {
          d = nulldate;
        }
      }
    }

    if(parts.length > 1) {
      string possible = icleanse.escape(parts[0]);
      parts.delete(0);
      if(length(possible) > 0) {
        content = true;
        title = possible;
      }
    }
    if(parts.length > 0) {
      string possible = icleanse.escape(parts[0]);
      if(length(possible) > 0) {
        content = true;
        entry = possible;
      }
    }
    if(content) {
      de.push(datedentry(d, title, entry));
    }
  }
  return de;
}

void run(picture pic, string[] input) {
  // Get the title or entry font size in order to size our elements
  style entryStyle = dom_styledom.findstyle(selectorlist(selector(elementtype.shape),
                                                         selector(elementtype.textbox, 1)));
  style titleStyle = dom_styledom.findstyle(selectorlist(selector(elementtype.shape),
                                                         selector(elementtype.textbox, 2)));

  // Use the entry size unless the titles are outsized in comparison
  real assumed_font_size = titleStyle.font_size > (5*entryStyle.font_size) ? 
                           titleStyle.font_size : entryStyle.font_size;

  page p = page(pic);
  datedentry[] de = normalise(input);
  drawtimeline(p, de, assumed_font_size);
  p.print();
}
