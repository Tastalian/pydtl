#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 Stéphane Caron
#
# This file is part of PyDTL.
#
# PyDTL is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# PyDTL is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with PyDTL. If not, see <http://www.gnu.org/licenses/>.

import pydtl
import unittest


class TestTables(unittest.TestCase):
    def setUp(self):
        with pydtl.SQLiteDB('sample.sqlite') as db:
            self.table = db.dump_table('events')

    def test_count(self):
        self.assertEqual(self.table.count(), 1000)

    def test_mean(self, attr='activity'):
        pass

    def test_variance(self, attr='activity'):
        pass

    def test_sample(self, attr='activity'):
        rows = self.table.sample_rows(12)
        self.assertEqual(len(rows), 12)
        self.assertEqual(len(rows[0].keys()), len(self.table.get_attrs()))
        self.assertEqual(len(self.table.sample_attr(attr, 42)), 42)

    def test_split(self):
        lt, rt, nt = self.table.split('completion', 2)
        self.assertEqual(lt.count(), self.table.count())
        self.assertEqual(rt.count(), 0)
        self.assertEqual(nt.count(), 0)


if __name__ == '__main__':
    unittest.main()
