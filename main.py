#!/usr/bin/env python

from xml.etree import ElementTree
import json

evdev_path="/usr/share/X11/xkb/rules/evdev.xml"

def main():
    tree = parse_xml()
    set_flags_in_xml(tree)
    write_xml(tree)

def parse_xml():
    parser = ElementTree.XMLParser(target=ElementTree.TreeBuilder(insert_comments=True))
    return ElementTree.parse(evdev_path, parser = parser)

def set_flags_in_xml(tree):
    flags = load_flags()
    root = tree.getroot()
    for item in root.findall("./layoutList/layout/configItem"):
        set_flag(item, flags)

def load_flags():
    f = open("./flags.json")
    return json.load(f)

def set_flag(item, flags):
    country_code, language = get_layout_id_from_xml(item)
    layout = get_layout_info(country_code, language, flags)
    if len(layout) > 0:
        item.find("./shortDescription").text = layout[0]["flag"]

def get_layout_id_from_xml(item):
    country_code = item.find("./name")
    language = item.find("./shortDescription")
    if country_code is not None and language is not None:
        return country_code.text, language.text
    else:
        return "", "" 

def get_layout_info(country_code, language, flags):
    return list(filter(lambda x:(x["code"]==country_code and x["shortDescription"]==language), flags))

def write_xml(tree):
    tree.write("./evdev.xml", encoding='utf-8', xml_declaration=True)

if __name__ == "__main__":
    main()