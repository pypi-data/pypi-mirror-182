#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy


class JonesVector():
    def __init__(self, jones_vector):
        self.jones_vector = numpy.array(jones_vector).astype(complex)

    def __repr__(self):
        return self.jones_vector.__repr__()

    def __add__(self, Other):
        if self.jones_vector.ndim == 1 and Other.jones_vector.ndim == 1:
            return JonesVector([self.jones_vector, Other.jones_vector])

        if self.jones_vector.ndim == 2 and Other.jones_vector.ndim == 1:
            return JonesVector([*self.jones_vector, Other.jones_vector])

        if self.jones_vector.ndim == 1 and Other.jones_vector.ndim == 2:
            return JonesVector([self.jones_vector, *Other.jones_vector])

        if self.jones_vector.ndim == 2 and Other.jones_vector.ndim == 2:
            return JonesVector([*self.jones_vector, *Other.jones_vector])


class RightCircularPolarization(JonesVector):
    def __init__(self):
        super().__init__([1, 1j])


class LeftCircularPolarization(JonesVector):
    def __init__(self):
        super().__init__([1, -1j])


class LinearPolarization(JonesVector):

    def __init__(self, *angle_list: list):
        if None in angle_list:
            raise ValueError("Unpolarized light source is not implemented yet...")

        angle_list = numpy.atleast_1d(angle_list)

        self.angle_list = [[numpy.cos(angle * numpy.pi / 180), numpy.sin(angle * numpy.pi / 180)]
                            if angle is not None else [numpy.nan, numpy.nan] for angle in angle_list]

        super().__init__(jones_vector=self.angle_list)
# -
