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

struct date {
  private static bool nullcreated = false;
  bool imnull = false;
  int epoch = 0;

  public void operator init() {
    if(nullcreated) {
      abort("date's nulldate has already been created, illegal to create more.");
    }
    this.imnull = true;
    nullcreated = true;
  }

  public void operator init(int epoch) {
    this.epoch = epoch;
  }
}

date operator +(date a, date b) {
  assert(!a.imnull && !b.imnull, "cannot compare against nulldate");
  return date(a.epoch + b.epoch);
}

date operator -(date a, date b) {
  assert(!a.imnull && !b.imnull, "cannot compare against nulldate");
  return date(a.epoch - b.epoch);
}

bool operator <(date a, date b) {
  assert(!a.imnull && !b.imnull, "cannot compare against nulldate");
  return a.epoch < b.epoch;
}

bool operator <=(date a, date b) {
  assert(!a.imnull && !b.imnull, "cannot compare against nulldate");
  return a.epoch <= b.epoch;
}

bool operator >(date a, date b) {
  assert(!a.imnull && !b.imnull, "cannot compare against nulldate");
  return a.epoch > b.epoch;
}

bool operator >=(date a, date b) {
  assert(!a.imnull && !b.imnull, "cannot compare against nulldate");
  return a.epoch >= b.epoch;
}

bool operator ==(date a, date b) {
  if(alias(a, null) || alias(b, null)) { return false; }
  if(a.imnull || b.imnull) { return a.imnull && b.imnull; }
  return a.epoch == b.epoch;
}

bool operator !=(date a, date b) {
  return !(a == b);
}

string operator cast(date a) {
  return time(a.epoch);
}

int operator cast(date a) {
  return a.epoch;
}

date nulldate = date();

public date parsedate(string text) {
    date result = nulldate;
    int epoch = seconds(text, "%Y/%m/%d");
    if(epoch != -1) {
      result = date(epoch);
    }
    return result;
}

