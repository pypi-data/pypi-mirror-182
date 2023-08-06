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

import "figular/page.asy" as page;

// nullpen is just a marker that a style setting was not set. It needs to be a
// valid pen (null is not) so we choose an unlikely one.
pen nullpen = linetype(new real[]{11,22,33,44,55,66,77,88,99});

struct style {
  pen border_color;
  pen strokeopacity;
  real border_width;
  pen border_style;
  pen join;
  pen cap;
  pen background_color;
  pen font_family;
  pen color;
  real font_size;

  private string colortostring(pen color) {
    string result = "";
    result += colorspace(color) + ",";
    for(real col: colors(color)) {
      result += (string)col + ",";
    }
    return result;
  }

  private string checkifset(pen p, string setstring) {
    if(p != nullpen) {
      return setstring;
    } 
    return "UNSET";
  }

  public string tostring() {
    string result = "(";
    result += "border_color=[";
    result += checkifset(this.border_color, colortostring(this.border_color));
    result += "], opacity=";
    result += checkifset(this.strokeopacity, (string)opacity(this.strokeopacity));
    result += ", border_width=";
    if(this.border_width != realMax) {
      result += (string)this.border_width;
    } else {
      result += "UNSET";
    }
    result += ", border_style=[";
    if(this.border_style != nullpen) {
      for(real c: linetype(this.border_style)) {
        result += (string)c + ",";
      }
      result += (string)offset(this.border_style) + ",";
      result += "scale=" + (scale(this.border_style) ? "true" : "false") + ",";
      result += "adjust=" + (adjust(this.border_style) ? "true" : "false") + ",";
    } else {
      result += "UNSET";
    }
    result += "], join=";
    result += checkifset(this.join, (string)linejoin(this.join));
    result += ", cap=";
    result += checkifset(this.cap, (string)linecap(this.cap));
    result += ", background_color=[" + colortostring(this.background_color);
    result += checkifset(this.background_color, colortostring(this.background_color));
    result += "], font_family=[";
    result += checkifset(this.font_family, font(this.font_family));
    result += "], color=[";
    result += checkifset(this.color, colortostring(this.color));
    result += "], font_size=";
    if(this.font_size != realMax) {
      result += (string)this.font_size;
    } else {
      result += "UNSET";
    }

    result += ")";
    return result;
  }

  private pen flattenstroke() {
    if(this.border_width == realMax) {
      abort("style cannot draw as border_width has not been set");
    } else if(this.border_width == 0) {
      return linewidth(0);
    } else if(this.border_color == nullpen ||
              this.strokeopacity == nullpen ||
              this.border_style == nullpen ||
              this.join == nullpen ||
              this.cap == nullpen) {
        abort("style cannot draw as border_width > 0 and other stroke properties have not been fully set");
    }
    // Regarding addition the asy manual states:
    // "All other non-default attributes of the rightmost pen will override those of the leftmost pen."
    // Therefore we are assuming the various pens in our addition below each
    // only override their one element of the defaults. If this is not true
    // then a 'red' join pen could override the intended color.
    // 
    // Strip out our colour first as otherwise asy will add the colours
    return colorless(defaultpen) + this.border_color
                                 + this.strokeopacity
                                 + this.border_width
                                 + this.border_style
                                 + this.join
                                 + this.cap;
  }

  private pen flattentextstyle() {
    if(this.font_size == realMax) {
      abort("style cannot label as font_size is unset");
    }
    return colorless(this.font_family) + this.color + fontsize(this.font_size);
  }

  void operator init(pen border_color=nullpen,
                     pen strokeopacity=nullpen,
                     real border_width=realMax,
                     pen border_style=nullpen,
                     pen join=nullpen,
                     pen cap=nullpen,
                     pen background_color=nullpen,
                     pen font_family=nullpen,
                     pen color=nullpen,
                     real font_size=realMax) {
    this.border_color=border_color;
    this.strokeopacity=strokeopacity;
    this.border_width=border_width;
    this.border_style=border_style;
    this.join=join;
    this.cap=cap;
    this.background_color=background_color;
    this.font_family=font_family;
    this.color=color;
    this.font_size=font_size;
  }

  drawnpath draw(page p, path g) {
    pen finallinestyle = flattenstroke();
    drawnpath dp = drawnpath(g, new void(picture p) { draw(p, g, finallinestyle); });
    p.push(dp);
    return dp;
  }

  drawnpath filldraw(page p, path g) {
    if(this.background_color == nullpen) {
      abort("style cannot filldraw as background color has not been set");
    }
    pen finallinestyle = flattenstroke();
    drawnpath dp;

    // Asymptote's filldraw and draw seem to always draw an outline even when
    // linewidth=0. Bug?
    if(linewidth(finallinestyle) > 0) {
      dp = drawnpath(g, new void(picture p) { filldraw(p, g, this.background_color, finallinestyle); });
    } else {
      dp = drawnpath(g, new void(picture p) { fill(p, g, this.background_color); });
    }
    p.push(dp);
    return dp;
  }

  Label textframe(page p, pair place, align align, string text) {
    pen finaltextstyle = flattentextstyle();
    Label l = Label(text, place, align, finaltextstyle);
    p.push(l);
    return l;
  }
}

string operator cast(style s) {
  return s.tostring();
}

bool operator==(style a, style b) {
  return a.border_color == b.border_color &&
         a.strokeopacity == b.strokeopacity &&
         a.border_width == b.border_width &&
         a.border_style == b.border_style &&
         a.join == b.join &&
         a.cap == b.cap &&
         a.background_color == b.background_color &&
         a.font_family == b.font_family &&
         a.color == b.color &&
         a.font_size == b.font_size;
}

bool operator!=(style a, style b) {
  return !(a==b);
}

style operator+(style a, style b) {
  style result;
  if(b.border_color != nullpen) {
    // Strip out our colour first as otherwise asy will add the colours
    result.border_color = b.border_color;
  } else {
    result.border_color = a.border_color;
  }
  if(b.strokeopacity != nullpen) {
    result.strokeopacity = b.strokeopacity;
  } else {
    result.strokeopacity = a.strokeopacity;
  }
  if(b.border_width != realMax) {
    result.border_width = b.border_width;
  } else {
    result.border_width = a.border_width;
  }
  if(b.border_style != nullpen) {
    result.border_style = b.border_style;
  } else {
    result.border_style = a.border_style;
  }
  if(b.join != nullpen) {
    result.join = b.join;
  } else {
    result.join= a.join;
  }
  if(b.cap != nullpen) {
    result.cap = b.cap;
  } else {
    result.cap= a.cap;
  }
  if(b.background_color != nullpen) {
    result.background_color = b.background_color;
  } else {
    result.background_color= a.background_color;
  }
  if(b.font_family != nullpen) {
    result.font_family = b.font_family;
  } else {
    result.font_family = a.font_family;
  }
  if(b.color != nullpen) {
    result.color = b.color;
  } else {
    result.color= a.color;
  }
  if(b.font_size != realMax) {
    result.font_size = b.font_size;
  } else {
    result.font_size = a.font_size;
  }
  return result;
}

style nullstyle = style();

// ----------------------------------------------------------------------------
// Fonts
// ----------------------------------------------------------------------------

// To access system fonts - see asymptote_doc
usepackage("fontspec");

pen getfont(string fontname, string series="m") {
  return fontcommand("\setmainfont{"+fontname+
                     "}\fontseries{"+series+
                     "}\selectfont");
}

struct fontrec {
  pen wield;
  string family;
  string style;

  void operator init(pen wield, string family, string style) {
    this.wield = wield;
    this.family = family;
    this.style = style;
  }
}

struct fontinfo {
  // TODO:
  // * We desperately need a uniform way of categorising/referring to typefaces/fonts
  // * Some fonts such as the built-in helpers for standard PostScript fonts end up being
  //   substituted in final PDF. Should it not be the case that you get what
  //   you request or should it work like the web and substitute as/when
  //   needed.     
  fontrec[] all;
  fontrec avantgarde = all.push(fontrec(AvantGarde(), "Avant Garde", "Normal"));
  fontrec avantgarde_bold = all.push(fontrec(AvantGarde("b"), "Avant Garde", "Bold"));
  fontrec bookman = all.push(fontrec(Bookman(), "Bookman", "Normal"));
  fontrec bookman_bold = all.push(fontrec(Bookman("b"), "Bookman", "Bold"));
  fontrec computermodern_roman = all.push(fontrec(font("OT1", "cmr", "m", "n"), "Computer Modern Roman", "Normal"));
  fontrec computermodern_roman_bold = all.push(fontrec(font("OT1", "cmr", "b", "n"), "Computer Modern Roman", "Bold"));
  fontrec computermodern_sansserif = all.push(fontrec(font("OT1", "cmss", "m", "n"), "Computer Modern Sans Serif", "Normal"));
  fontrec computermodern_sansserif_bold = all.push(fontrec(font("OT1", "cmss", "b", "n"), "Computer Modern Sans Serif", "Bold"));
  fontrec computermodern_teletype = all.push(fontrec(font("OT1", "cmtt", "m", "n"), "Computer Modern Teletype", "Normal"));
  // There is no bold cmtt, it falls back to plain cmtt. We need to decide how
  // we'll deal with fonts that don't support all possible stylings.
  fontrec computermodern_teletype_bold = all.push(fontrec(font("OT1", "cmtt", "b", "n"), "Computer Modern Teletype", "Bold"));
  fontrec courier = all.push(fontrec(Courier(), "Courier", "Normal"));
  fontrec courier_bold = all.push(fontrec(Courier("b"), "Courier", "Bold"));
  fontrec dejavu_sansserif = all.push(fontrec(getfont("DejaVu Sans"), "DeJaVu Sans Serif", "Normal"));
  fontrec dejavu_sansserif_bold = all.push(fontrec(getfont("DejaVu Sans", "b"), "DeJaVu Sans Serif", "Bold"));
  fontrec helvetica = all.push(fontrec(Helvetica(), "Helvetica", "Normal"));
  fontrec helvetica_bold = all.push(fontrec(Helvetica("b"), "Helvetica", "Bold"));
  fontrec newcenturyschoolbook = all.push(fontrec(NewCenturySchoolBook(), "New Century Schoolbook", "Normal"));
  fontrec newcenturyschoolbook_bold = all.push(fontrec(NewCenturySchoolBook("b"), "New Century Schoolbook", "Bold"));
  fontrec palatino = all.push(fontrec(Palatino(), "Palatino", "Normal"));
  fontrec palatino_bold = all.push(fontrec(Palatino("b"), "Palatino", "Bold"));
  fontrec symbol = all.push(fontrec(Symbol(), "Symbol", "Normal"));
  fontrec symbol_bold = all.push(fontrec(Symbol("b"), "Symbol", "Bold"));
  fontrec timesroman = all.push(fontrec(TimesRoman(), "Times Roman", "Normal"));
  fontrec timesroman_bold = all.push(fontrec(TimesRoman("b"), "Times Roman", "Bold"));
  fontrec zapfchancery = all.push(fontrec(ZapfChancery(), "Zapf Chancery", "Normal"));
  fontrec zapfchancery_bold = all.push(fontrec(ZapfChancery("b"), "Zapf Chancery", "Bold"));
  fontrec zapfdingbats = all.push(fontrec(ZapfDingbats(), "Zapf Dingbats", "Normal"));
  fontrec zapfdingbats_bold = all.push(fontrec(ZapfDingbats("b"), "Zapf Dingbats", "Bold"));
}

fontinfo font;

pen operator cast(fontrec fs) { return fs.wield; };
