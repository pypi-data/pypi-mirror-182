#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import typing
import pathlib
from plum import dispatch, add_conversion_method
from lxml import etree

def countConsecutive(element, l: typing.Iterable, start: int = 0):
	if len(l) == 0 or start > len(l) - 1 or element not in l:
		return -1
	
	c = start
	while c + 1 < len(l) and l[c] == element and l[c + 1] == element:
		c += 1
	return  c - start

class NodePathPart:
	@dispatch
	def __init__(self, name: "NodePathPart", index: int):
		self.name = name.name
		self.index = index
	
	@dispatch
	def __init__(self, other: "NodePathPart"):
		self.name = other.name
		self.index = other.index
	
	@dispatch
	def __init__(self, s: str, index: typing.Optional[int] = None):
		self.name, self.index = self.splitNameIndex(s)
		if self.index == None:
			self.index = index
	
	@staticmethod
	def splitNameIndex(s):
		index = None
		name = s
		if "[" in s and "]" in s:
			name, index = s.split("[")
			index = int(index.split("]")[0])
		return name, index
	
	@dispatch
	def __eq__(self, other: "NodePathPart"):
		return self.index == other.index and self.name == other.name
	
	@dispatch
	def __eq__(self, other: str):
		other = NodePathPart(other)
		return self == other
	
	@dispatch
	def __ne__(self, other: "NodePathPart"):
		return self.index != other.index or self.name != other.name
	
	@dispatch
	def __ne__(self, other: str):
		other = NodePathPart(other)
		return self != other
	
	def __bool__(self):
		return self.name not in ("", ".")
	
	def __repr__(self):
		if self.index != None:
			return f"{self.name}[{self.index}]"
		else:
			return str(self.name)
	
	def __str__(self):
		if self.index != 0:
			return repr(self)
		else:
			return str(self.name)

class NodePath:
	@dispatch
	def __init__(self, parts: typing.Sequence[str]):
		self.parts = map(NodePathPart, parts or [])
		self._filterPathParts()
	
	@dispatch
	def __init__(self, parts: typing.Sequence[NodePathPart]):
		self.parts = parts or []
		self._filterPathParts()
	
	@dispatch
	def __init__(self, path: typing.Optional[str]=None):
		if path != None:
			self.parts = map(NodePathPart, (path or "").split("/"))
		else:
			self.parts = []
		self._filterPathParts()
	
	# copy constructor
	@dispatch
	def __init__(self, other: "NodePath"):
		self.parts = other.parts
		self._filterPathParts()
	
	def __repr__(self):
		return "/".join(map(repr, self.parts)) or "/"
	
	def __str__(self):
		return "/".join(map(str, self.parts)) or "/"
	
	def _filterPathParts(self):
		self.parts = list(self.parts)
		parts = []
		for i, part in enumerate(self.parts):
			if part:
				if len(self.parts) < i + 1 and self.parts[i + 1] == "..":
					self.parts[i + 1] = None
				else:
					parts.append(part)
		self.parts = parts
	
	@dispatch
	def __add__(self, other: typing.Sequence[typing.Union[NodePathPart, str]]) -> "NodePath":
		new = NodePath(self)
		new.parts += other
		new._filterPathParts()
		return new
	
	@dispatch
	def __add__(self, other: "NodePath") -> "NodePath":
		new = NodePath(self)
		new.parts += other.parts
		return new
	
	@dispatch
	def __iadd__(self, other: typing.Sequence[typing.Union[NodePathPart, str]]) -> "NodePath":
		self.parts += other
		self._filterPathParts()
		return self
	
	@dispatch
	def __iadd__(self, part: typing.Union[str, NodePathPart]) -> "NodePath":
		self.parts.append(part)
		self._filterPathParts()
		return self
	
	@dispatch
	def __iadd__(self, other: "NodePath") -> "NodePath":
		self.parts += other.parts
		return self
	
	@dispatch
	def __truediv__(self, other: typing.Union["NodePath", str, NodePathPart, typing.Sequence[typing.Union[NodePathPart, str]]]) -> "NodePath":
		return self.__iadd__(other)
	
	@dispatch
	def __itruediv__(self, other: typing.Union["NodePath", str, NodePathPart, typing.Sequence[typing.Union[NodePathPart, str]]]) -> "NodePath":
		return self.__iadd__(other)
	
	def __iter__(self) -> typing.Iterator["NodePath"]:
		return iter(self.parts)
	
	def __len__(self) -> int:
		return len(self.parts)
	
	@dispatch
	def __getitem__(self, index: slice) -> "NodePath":
		start, stop, _ = index.indices(len(self.parts))
		indices = range(start, stop, 1)
		return NodePath([self.parts[i] for i in indices])
	
	@dispatch
	def __getitem__(self, index: int) -> NodePathPart:
		return self.parts[index]

class ListenerCallback:
	def __init__(self, node, func, subnodes=True):
		self.listenedToNode = node
		self.func = func
		self.subnodes = subnodes
	
	def __call__(self, changedNode=None):
		if self.subnodes:
			self.func(self.listenedToNode, changedNode or self.listenedToNode)
		else:
			self.func(self.listenedToNode)
	
	def remove(self):
		self.listenedToNode.removeListener(self)

class Node:
	@dispatch
	def __init__(self, name="/"):
		self.setName(name)
		self._index = 0
		self._parent = None
		self._children = []
		self._listeners = []
		self._attrs = {}
		self._value = None
		self._type = str
	
	def __repr__(self):
		return f"props.Node(path={repr(self.getPath())})"
	
	@dispatch
	def addListener(self, path: typing.Union[NodePath, str, NodePathPart, typing.Sequence[typing.Union[NodePathPart, str]]], func: typing.Callable, subnodes: bool=False):
		return self.getNode(path, True).addListener(func, subnodes)
	
	@dispatch
	def addListener(self, func: typing.Callable, subnodes: bool=False):
		l = ListenerCallback(self, func, subnodes)
		if not l in self._listeners:
			self._listeners.append(l)
		return l
	
	def removeListener(self, l):
		if l in self._listeners:
			self._listeners.remove(l)
		
	@dispatch
	def addNode(self, path: typing.Union[NodePath, str, NodePathPart, typing.Sequence[typing.Union[NodePathPart, str]]], n: "Node"):
		path = NodePath(path)
		existing = self.getNode(path / n.getName(), False)
		if not existing:
			self._children.append(n)
		else:
			existing.addNodes("/", n.getChildren())
	
	@dispatch
	def addNodes(self, path: typing.Union[NodePath, str, NodePathPart, typing.Sequence[typing.Union[NodePathPart, str]]], ns: typing.Iterable["Node"]):
		for n in ns:
			self.addNode(path, n)
	
	def hasChildren(self):
		return self.countChildren() > 0
	
	def countChildren(self, name: typing.Optional[typing.Union[str, NodePathPart]] = None):
		if name:
			c = 0
			for node in self.getChildren():
				if node.getName() == name:
					c += 1
			return c
		else:
			return len(self._children)
	
	@dispatch
	def getChildren(self, name: typing.Optional[typing.Union[str, NodePathPart]] = None):
		name = NodePathPart(name)
		return sorted(filter(lambda c: c.getName().name == name.name, self._children), key=lambda c: c.getIndex())
	
	@dispatch
	def getChildren(self):
		return sorted(self._children, key=lambda c: c.getIndex())
	
	def getRootNode(self):
		if self._parent:
			return self._parent.getRootNode()
		else:
			return self
	
	def getParent(self):
		return self._parent
	
	def getPath(self) -> NodePath:
		if not self._parent:
			return NodePath("/")
		else:
			return self._parent.getPath() / NodePathPart(self.getName(), self.getIndex())
	
	def getPathString(self) -> str:
		return str(self.getPath())
	
	def getIndex(self) -> int:
		return self._index
	
	def setIndex(self, i: int):
		self._index = i
		self._name.index = i
	
	@dispatch
	def _findUnusedIndex(self, child: typing.Union[str, NodePathPart]):
		m = 0
		for c in self._children:
			if c.getName() == child:
				m = max(m, c.getIndex())
		return m
	
	@dispatch
	def getNode(self, path: typing.Union[NodePath, str, NodePathPart, typing.Sequence[typing.Union[NodePathPart, str]]], create: bool=False):
		path = NodePath(path)
		path[0].index = path[0].index or 0
		if not len(path):
			return self
		elif countConsecutive("..", path, 0) > len(self.getPath()):
			print("Warning: attempting moving up in the property tree past the root node, returning the root node")
			return self.getRootNode()
		elif path[0] == "..":
			return self.getParent().getNode(path[1:])
		
		node = None
		for child in self._children:
			if child.getName().name == path[0].name and (child.getIndex() or 0) == (path[0].index or 0):
				if len(path) > 1:
					node = child.getNode(path[1:], create)
				else:
					node = child
		
		if node == None and create:
			child = Node()
			child._parent = self
			child.setName(path[0].name)
			index = path[0].index
			if index == None:
				index = self._findUnusedIndex(child.getName())
			child.setIndex(index)
			
			self._children.append(child)
			if len(path) > 1:
				node = child.getNode(path[1:], True)
			else:
				node = child
		return node
	
	@dispatch
	def initNode(self, path: typing.Union[NodePath, str, NodePathPart, typing.Sequence[typing.Union[NodePathPart, str]]], typ: typing.Callable = str, value: typing.Optional[typing.Any] = None):
		node = self.getNode(path, create=True)
		node.setType(typ)
		if value != None:
			node.setValue(typ(value))
		return node
	
	@dispatch
	def remove(self):
		self.getParent().remove(self.getPath()[-1])
	
	@dispatch
	def remove(self, path: typing.Union[NodePath, str, NodePathPart, typing.Sequence[typing.Union[NodePathPart, str]]]):
		path = NodePath(path)
		if not len(path):
			self.remove()
		else:
			for c in self.getChildren():
				if c.getName() == path[0]:
					self._children.remove(c)
				break
	
	@dispatch
	def setType(self, type: typing.Callable):
		self._type = type
		if self._value != None:
			self._value = self._type(self._value)
	
	@dispatch
	def getType(self):
		return self._type
	
	@dispatch
	def setName(self, name: typing.Union[str, NodePathPart]):
		self._name = NodePathPart(name)
	
	@dispatch
	def getName(self) -> NodePathPart:
		return self._name
	
	@dispatch
	def getNameString(self) -> str:
		return str(self._name)
	
	@dispatch
	def _fireListeners(self):
		for l in self._listeners:
			l()
		self.getParent()._fireListeners(self)
	
	@dispatch
	def _fireListeners(self, subnode):
		for l in self._listeners:
			if l.subnodes:
				l(subnode)
	
	def getStringValue(self, path: typing.Optional[typing.Union[NodePath, str, NodePathPart, typing.Sequence[typing.Union[NodePathPart, str]]]] = None, default: typing.Optional[str] = None):
		path = NodePath(path)
		if path:
			return self.initNode(path, str).getStringValue(default=default)
		else:
			if self._value != None:
				return str(self._value)
			else:
				return default
	
	@dispatch
	def getBoolValue(self, path: typing.Union[NodePath, str, NodePathPart, typing.Sequence[typing.Union[NodePathPart, str]]], default: typing.Optional[bool] = None):
		path = NodePath(path)
		if path:
			return self.initNode(path, bool).getBoolValue(default)
		else:
			return self.getBoolValue(default)
	
	@dispatch
	def getBoolValue(self, default: typing.Optional[int] = None):
		if str(self._value).lower() == "false":
			return False
		elif str(self._value).lower() == "true":
			return True
		else:
			if self._value != None:
				return bool(self._value)
			else:
				return default
	
	@dispatch
	def getIntValue(self, path: typing.Union[NodePath, str, NodePathPart, typing.Sequence[typing.Union[NodePathPart, str]]], default: typing.Optional[int] = None):
		path = NodePath(path)
		if path:
			return self.initNode(path, int).getIntValue(default)
		else:
			return self.getIntValue(default)
	
	@dispatch
	def getIntValue(self, default: typing.Optional[int] = None):
		if self._value != None:
			return int(self._value)
		else:
			return default
	
	@dispatch
	def getFloatValue(self, path: typing.Union[NodePath, str, NodePathPart, typing.Sequence[typing.Union[NodePathPart, str]]], default: typing.Optional[float] = None):
		path = NodePath(path)
		if path:
			return self.initNode(path, float).getFloatValue(default)
		else:
			return self.getFloatValue(default)
	
	@dispatch
	def getFloatValue(self, default: typing.Optional[float] = None):
		if self._value != None:
			return float(self._value)
		else:
			return default
	
	@dispatch	
	def getValue(self, path: typing.Union[NodePath, str, NodePathPart, typing.Sequence[typing.Union[NodePathPart, str]]], default: typing.Optional[typing.Any] = None):
		path = NodePath(path)
		if default != None:
			typ = type(default)
		else:
			typ = str
		if path:
			return self.initNode(path, typ).getValue(default)
		else:
			return self.getValue(default)
	
	@dispatch
	def getValue(self, default: typing.Optional[typing.Any] = None):
		if self._value != None:
			return self._type(self._value)
		else:
			return default
	
	def setValue(self, value: typing.Any, path: typing.Optional[typing.Union[NodePath, str, NodePathPart, typing.Sequence[typing.Union[NodePathPart, str]]]] = None):
		path = NodePath(path)
		if path:
			self.initNode(path, type(value), value)
			return
		
		if self.countChildren() != 0:
			raise TypeError(f"cannot set a value on node {self.getPathString()} that has children")
		
		try:
			self._value = self._type(value)
		except ValueError:
			raise ValueError(f"could not convert {value} to type {self._type} of node {self.getPathString()}")
		self._fireListeners()

