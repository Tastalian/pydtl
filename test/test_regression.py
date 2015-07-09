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

import unittest
from pydtl import RegressionTree, SQLiteDB


class TestRegression(unittest.TestCase):
    def setUp(self):
        self.db = SQLiteDB('../sample.sqlite')
        self.table = self.db.dump_table('events')

    def test_local(self):
        tree = RegressionTree(self.table, 'activity')
        samples = self.table.sample_rows(10)
        return [tree.predict(inst) for inst in samples]


if __name__ == '__main__':
    unittest.main()
