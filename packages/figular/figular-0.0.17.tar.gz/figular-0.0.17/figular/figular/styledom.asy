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

import "figular/dom" as dom;
import "figular/domtree" as dom;
import "figular/logger" as ilogger;
import "figular/style" as style;

struct stylerule {
  selectorlist sel;
  style sty;

  void operator init(selectorlist sel, style sty) {
    this.sel = sel;
    this.sty = sty;
  }

  bool match(selectorlist s) {
    return s.isselectedby(this.sel);
  }
}

struct styledom {
  private static logger log = logger.getlogger("styledom");
  stylerule[] rules;
  private domtree dt;

  // 'default' colours
  // this is really like a palette/theme and something that should
  // be controllable in future
  static pen coldark = heavygray;
  static pen collight = lightgray;

  public style findstyle(selectorlist justadded) {
    log.debug("finding style for " + (string)justadded);
    style result = nullstyle;
    // TODO: should we not add styles together as we find them
    //       to arrive at the final result? Starting from defaultsty
    for(var sr: rules) {
      if(sr.match(justadded)) {
        log.debug("match on " + (string)sr.sel);
        log.debug("with style " + (string)sr.sty);
        result += sr.sty;
      }
    }
    return result;
  }

  // dom interface

  void nextparentisatextbox(){ dt.nextparentisatextbox(); }
  void nextparentisacircle(){ dt.nextparentisacircle(); }
  void nextparentisashape(){ dt.nextparentisashape(); }
  void nextparentisaline(){ dt.nextparentisaline(); }

  style addtextbox(){ return findstyle(dt.addtextbox()); }
  style addcircle(){ return findstyle(dt.addcircle()); }
  style addshape(){ return findstyle(dt.addshape()); }
  style addline(){ return findstyle(dt.addline()); }

  // styledom's own methods

  public void addrule(stylerule sr) {
    rules.push(sr);
  }

  public void clearrules() {
    rules.delete();
  }

  void operator init() {
    style circlestyle = style(border_width=0,
                              background_color=coldark,
                              font_family=font.computermodern_roman,
                              color=collight);
    style shapestyle = style(border_width=0,
                             background_color=coldark);
    style textstyle = style(font_family=font.computermodern_roman,
                            color=collight);
    style linestyle = style(border_width=1, border_color=coldark);

    // Default stylesheet
    style defaultsty = style(border_color=black,
                             strokeopacity=defaultpen,
                             border_width=0,
                             border_style=solid,
                             join=roundjoin,
                             cap=roundcap,
                             background_color=coldark,
                             font_family=font.computermodern_roman,
                             color=collight,
                             font_size=12pt);
    addrule(stylerule(selectorlist(), defaultsty));
    addrule(stylerule(selectorlist(selector(elementtype.circle)), circlestyle));
    addrule(stylerule(selectorlist(selector(elementtype.shape)), shapestyle));
    addrule(stylerule(selectorlist(selector(elementtype.textbox)), textstyle));
    addrule(stylerule(selectorlist(selector(elementtype.line)), linestyle));
  }
}

dom operator cast(styledom sd) {
  dom result;
  result.nextparentisatextbox = sd.nextparentisatextbox;
  result.nextparentisacircle = sd.nextparentisacircle;
  result.nextparentisashape = sd.nextparentisashape;
  result.nextparentisaline = sd.nextparentisaline;
  result.addtextbox = sd.addtextbox;
  result.addcircle = sd.addcircle;
  result.addshape = sd.addshape;
  result.addline = sd.addline;
  return result;
}

// Set ourselves as a global, singleton styledom for those
// who need to grab us by our actual type
styledom dom_styledom = styledom();
// Set ourselves as the global, singleton dom for those who need a dom type
dom = dom_styledom;
