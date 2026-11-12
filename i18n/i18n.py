"""
Translations for the Lucky Alien site.

index.html (Ukrainian) is the single source of truth. This script:
  extract  - collects every Ukrainian text unit into i18n/source.json
  build    - writes ru/index.html, en/index.html, ro/index.html using
             i18n/ru.json, i18n/en.json, i18n/ro.json ({ukrainian: translation})
             and lists any text that still has no translation.

Usage (from the project root):
  python3 i18n/i18n.py extract
  python3 i18n/i18n.py build
"""
import html
import json
import os
import re
import sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "index.html")
I18N = os.path.join(ROOT, "i18n")
LANGS = ["ru", "en", "ro"]
ALL_LANGS = ["uk"] + LANGS
LANG_LABEL = {"uk": "UA", "ru": "RU", "en": "EN", "ro": "RO"}

CYR = re.compile(r"[А-Яа-яІіЇїЄєҐґ]")
INLINE = {"strong", "b", "em", "i", "br", "span", "small", "sup", "sub", "u", "a", "abbr", "mark"}
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}
SKIP = {"script", "style"}
ATTRS = ["alt", "aria-label", "title", "placeholder", "content"]


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


class Node:
    def __init__(self, tag, start, start_end, parent):
        self.tag, self.start, self.start_end, self.parent = tag, start, start_end, parent
        self.end_start = None
        self.children = []  # Node or ("text", a, b)


class Tree(HTMLParser):
    def __init__(self, src):
        super().__init__(convert_charrefs=False)
        self.src = src
        self.line_off = [0]
        for m in re.finditer("\n", src):
            self.line_off.append(m.end())
        self.root = Node("#root", 0, 0, None)
        self.cur = self.root
        self.tags = []  # (tag, a, b) for every start tag (attribute pass)

    def off(self):
        line, col = self.getpos()
        return self.line_off[line - 1] + col

    def handle_starttag(self, tag, attrs):
        a = self.off()
        b = a + len(self.get_starttag_text())
        self.tags.append((tag, a, b))
        node = Node(tag, a, b, self.cur)
        self.cur.children.append(node)
        if tag not in VOID:
            self.cur = node
        else:
            node.end_start = b

    def handle_startendtag(self, tag, attrs):
        a = self.off()
        b = a + len(self.get_starttag_text())
        self.tags.append((tag, a, b))
        node = Node(tag, a, b, self.cur)
        node.end_start = b
        self.cur.children.append(node)

    def handle_endtag(self, tag):
        a = self.off()
        n = self.cur
        while n is not self.root and n.tag != tag:
            n = n.parent
        if n is self.root:
            return
        # close everything up to n
        m = self.cur
        while m is not n:
            m.end_start = a
            m = m.parent
        n.end_start = a
        self.cur = n.parent

    def handle_data(self, data):
        a = self.off()
        self.cur.children.append(("text", a, a + len(data)))

    def handle_entityref(self, name):
        a = self.off()
        self.cur.children.append(("text", a, a + len(name) + 2))

    def handle_charref(self, name):
        a = self.off()
        self.cur.children.append(("text", a, a + len(name) + 3))


def all_inline(node):
    for c in node.children:
        if isinstance(c, Node):
            if c.tag not in INLINE or not all_inline(c):
                return False
    return True


def units(src):
    """Return list of (a, b, ukrainian_key) ranges to replace, plus attribute ranges."""
    t = Tree(src)
    t.feed(src)
    out = []

    def visit(node):
        if isinstance(node, Node):
            if node.tag in SKIP:
                return
            if node.tag != "#root" and node.end_start is not None and node.children and all_inline(node):
                inner = src[node.start_end:node.end_start]
                if CYR.search(inner):
                    out.append((node.start_end, node.end_start, inner))
                return
            for c in node.children:
                visit(c)
        else:
            _, a, b = node
            txt = src[a:b]
            if CYR.search(txt):
                out.append((a, b, txt))

    visit(t.root)

    for tag, a, b in t.tags:
        tagtxt = src[a:b]
        for attr in ATTRS:
            for m in re.finditer(r'(?<![\w-])%s="([^"]*)"' % re.escape(attr), tagtxt):
                raw = m.group(1)
                if CYR.search(raw):
                    out.append((a + m.start(1), a + m.end(1), ("attr", raw)))
    return out


def key_of(u):
    if isinstance(u, tuple):
        return norm(html.unescape(u[1]))
    return norm(u)


def extract():
    src = open(SRC, encoding="utf-8").read()
    seen, keys = set(), []
    for a, b, u in sorted(units(src), key=lambda x: x[0]):
        k = key_of(u)
        if k and k not in seen:
            seen.add(k)
            keys.append(k)
    with open(os.path.join(I18N, "source.json"), "w", encoding="utf-8") as f:
        json.dump(keys, f, ensure_ascii=False, indent=1)
    print(f"{len(keys)} text units, {sum(len(k) for k in keys)} characters -> i18n/source.json")


def lang_switch(src, lang):
    """Point every language link at the right page and mark the current one."""
    prefix = "" if lang == "uk" else "../"

    def href(target):
        return prefix + ("" if target == "uk" else target + "/") or "./"

    def repl(m):
        target = m.group(1)
        h = href(target) or "./"
        active = "true" if target == lang else "false"
        cur = ' aria-current="page"' if target == lang else ""
        return (f'<a class="lang-item" data-lang="{target}" href="{h}" hreflang="{target}" '
                f'data-active="{active}"{cur}>{LANG_LABEL[target]}</a>')

    return re.sub(r'<a class="lang-item" data-lang="(\w+)"[^>]*>\w+</a>', repl, src)


def build():
    src = open(SRC, encoding="utf-8").read()
    us = units(src)
    report = {}
    for lang in LANGS:
        path = os.path.join(I18N, f"{lang}.json")
        tr = json.load(open(path, encoding="utf-8")) if os.path.exists(path) else {}
        out, missing = src, []
        for a, b, u in sorted(us, key=lambda x: x[0], reverse=True):
            k = key_of(u)
            if k not in tr or not tr[k].strip():
                missing.append(k)
                continue
            t = tr[k]
            if isinstance(u, tuple):
                rep = html.escape(t, quote=True).replace("&#x27;", "'")
            else:
                seg = out[a:b]
                lead = seg[: len(seg) - len(seg.lstrip())]
                trail = seg[len(seg.rstrip()):]
                rep = lead + t + trail
            out = out[:a] + rep + out[b:]
        out = out.replace('<html lang="uk">', f'<html lang="{lang}">', 1)
        out = re.sub(r'((?:src|href|poster)=")assets/', r"\1../assets/", out)
        out = out.replace("url(assets/", "url(../assets/")
        out = lang_switch(out, lang)
        os.makedirs(os.path.join(ROOT, lang), exist_ok=True)
        with open(os.path.join(ROOT, lang, "index.html"), "w", encoding="utf-8") as f:
            f.write(out)
        report[lang] = sorted(set(missing))
    # keep the Ukrainian page's switcher consistent too
    fixed = lang_switch(src, "uk")
    if fixed != src:
        with open(SRC, "w", encoding="utf-8") as f:
            f.write(fixed)
    for lang in LANGS:
        miss = report[lang]
        print(f"{lang}: {'all translated' if not miss else str(len(miss)) + ' missing'}")
        for k in miss[:20]:
            print("   -", k[:110])


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "extract":
        extract()
    elif cmd == "build":
        build()
    else:
        print(__doc__)
