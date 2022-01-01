#!/usr/bin/env python

import xml.etree.ElementTree as ET

evdev_path="/usr/share/X11/xkb/rules/evdev.xml"

def parseXML():
 tree = ET.parse(evdev_path)
 root = tree.getroot()

 for item in root.findall("./layoutList/layout/configItem"):
    for child in item:
        print(child.tag.title())
        print(child.text)

def main():
    parseXML()

if __name__ == "__main__":
    main()