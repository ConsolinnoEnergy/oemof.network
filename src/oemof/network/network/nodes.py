# -*- coding: utf-8 -*-
"""This package contains the differnt types of Node for
modelling an energy system graph.

SPDX-FileCopyrightText: Stephan Günther <>
SPDX-FileCopyrightText: Uwe Krien <krien@uni-bremen.de>
SPDX-FileCopyrightText: Simon Hilpert <>
SPDX-FileCopyrightText: Cord Kaldemeyer <>
SPDX-FileCopyrightText: Patrik Schönfeldt <patrik.schoenfeldt@dlr.de>

SPDX-License-Identifier: MIT
"""

from .edge import Edge
from .entity import Entity




class Node(Entity):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._in_edges = set()

        msg = "{} {!r} of {!r} not an instance of Node but of {}."

        for i in kwargs.get("inputs", {}):
            if not isinstance(i, Node):
                raise ValueError(msg.format("Input", i, self, type(i)))
            self._in_edges.add(i)
            try:
                flow = kwargs["inputs"].get(i)
            except AttributeError:
                flow = None
            edge = Edge.from_object(flow)
            edge.input = i
            edge.output = self
        for o in kwargs.get("outputs", {}):
            if not isinstance(o, Node):
                raise ValueError(msg.format("Output", o, self, type(o)))
            try:
                flow = kwargs["outputs"].get(o)
            except AttributeError:
                flow = None
            edge = Edge.from_object(flow)
            edge.input = self
            edge.output = o


class Bus(Node):
    pass


class Component(Node):
    pass


class Sink(Component):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Source(Component):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Transformer(Component):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
