#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import os
import typing
from lxml import etree
from plum import dispatch

from pyproptree import Node, NodePath

TypeMapping = {
	"str": str,
	"int": int,
	"float": float,
	"double": float,
	"bool": bool,
}

@dispatch
def lxmlElementToNode(el: etree._Element, root: typing.Optional[Node] = None):
	if not root:
		root = Node()
		root.setName(el.tag)
	
	for element in el:
		index = root.countChildren(element.tag)
		child = root.getNode(NodePath(f"{element.tag}[{index}]"), True)
		if not child.hasChildren():
			t = TypeMapping.get(element.attrib.get("type", "str").lower(), str)
			child.setType(t)
			child.setValue(t(element.text))
		lxmlElementToNode(element, child)
	
	return root

@dispatch
def loadFile(file: typing.Union[str, typing.IO], n: typing.Optional[Node] = None):
	tree = etree.parse(file).getroot()
	return lxmlElementToNode(tree, n)

@dispatch
def loadString(s: str, n: typing.Optional[Node] = None):
	tree = etree.fromstring(s).getroot()
	return lxmlElementToNode(tree, n)

@dispatch
def nodeToLxmlElement(node: Node):
	element = etree.ElementBase()
	tag = node.getName()
	element.tag = tag.name
	element.attrib["n"] = str(tag.index or 0)
	if not node.hasChildren():
		element.text = node.getStringValue()
		element.attrib["type"] = node.getType().__qualname__
	else:
		for subnode in node.getChildren():
			subelement = nodeToLxmlElement(subnode)
			element.append(subelement)
	return element

@dispatch
def nodeToLxmlTree(node: Node):
	rootelement = nodeToLxmlElement(node)
	tree = etree.ElementTree(rootelement)
	return tree

@dispatch
def dumpString(node: Node, indent="\t"):
	tree = nodeToLxmlTree(node)
	etree.indent(tree, space=indent)
	return etree.tostring(tree, encoding="UTF-8", xml_declaration=True, pretty_print=True)

@dispatch
def dumpDict(node: Node):
	d = {}
	if node.hasChildren():
		d[node.getNameString()] = []
		for c in node.getChildren():
			d[node.getNameString()].append(dumpDict(c))
	else:
		d[node.getNameString()] = node.getValue()
	return d

@dispatch
def writeFile(node: Node, path: str):
	os.makedirs(os.path.abspath(os.path.join(*os.path.split(path)[:-1])), exist_ok=True)
	
	with open(path, "wb") as f:
		f.write(dumpString(node))

@dispatch
def writeFile(node: Node, f: typing.BinaryIO):
	f.write(dumpString(node))

