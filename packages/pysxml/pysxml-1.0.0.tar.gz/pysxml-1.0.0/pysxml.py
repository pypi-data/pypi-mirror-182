"""Generate XML and HTML using an SXML-like syntax."""

from functools import reduce
from typing import Union
import xml.etree.ElementTree as ET

_void_tags = ("area", "base", "br", "col", "command", "embed", "hr", "img",
              "input", "keygen", "link", "meta", "param", "source", "track",
              "wbr")


def _sxml_to_xml(sxml, html):
    if not isinstance(sxml, (tuple, list)):
        return sxml
    elif len(sxml) > 1 and sxml[1][0] == "@":
        attrs = reduce(lambda acc, x: acc + f'{x[0]}="true" ' if len(x) < 2
                       else acc + f'{x[0]}="{x[1]}" ', sxml[1][1:], " ").rstrip()
        start_index = 2
    else:
        attrs, start_index = "", 1
    content = reduce(lambda acc, x: acc + x,
                     [_sxml_to_xml(x, html) for x in sxml[start_index:]], "")
    tag = sxml[0]
    if tag == "@":
        raise ValueError(f"Invalid tag {tag}.")
    if html and tag in _void_tags:
        return f"<{tag}{attrs}>"
    elif not html and not content:
        return f"<{tag}{attrs}/>"
    else:
        return f"<{tag}{attrs}>{content}</{tag}>"


def sxml_to_xml(sxml: Union[list, tuple], html=False) -> str:
    """Convert an SXML expression to a string containing XML.

    Args:
        sxml (list, tuple): Structured SXML data.
        html (bool): Whether to use HTML void tags.
    Returns:
        str: String containing XML.
    """
    try:
        return _sxml_to_xml(sxml, html=html)
    except Exception:
        raise ValueError("Malformed psuedo-SXML. Check commas, tuple unpacking, \
and structure.")


def _list_to_tuple(lst):
    return tuple(_list_to_tuple(x) if isinstance(x, list) else x for x in lst)


def Element_to_sxml(tree: ET.Element) -> tuple:
    """Convert an ET.Element into an SXML expression (nested lists)."""
    content = [tree.text.strip()] if tree.text and not str.isspace(tree.text) else []
    tail = [tree.tail.strip()] if tree.tail and not str.isspace(tree.tail) else []
    attributes = [[x, y] for x, y in tree.items()]
    attributes = [["@", *attributes]] if attributes else []
    for child in tree:
        content.append(Element_to_sxml(child))
    return _list_to_tuple(tail + [tree.tag] + attributes + content)


if __name__ == "__main__":
    import argparse
    from pprint import pprint
    parser = argparse.ArgumentParser(
        "pysxml",
        description="Utilities for XML and pysxml's pseudo-SXML format.")
    parser.add_argument("filename", type=str)
    parser.add_argument("--convert", action="store_true",
                        help="Convert [filename] from XML to SXML.")
    parser.add_argument("--html", action="store_true",
                        help="Use HTML output format.")
    args = parser.parse_args()
    with open(args.filename) as f:
        newstr = f.read()
    if args.convert:
        root = ET.fromstring(newstr)
        pprint(Element_to_sxml(root))
    else:
        from ast import literal_eval
        print(sxml_to_xml(literal_eval(newstr), html=args.html))
