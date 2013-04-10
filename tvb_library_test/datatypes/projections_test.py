# -*- coding: utf-8 -*-
#
#
# TheVirtualBrain-Framework Package. This package holds all Data Management, and 
# Web-UI helpful to run brain-simulations. To use it, you also need do download
# TheVirtualBrain-Scientific Package (for simulators). See content of the
# documentation-folder for more details. See also http://www.thevirtualbrain.org
#
# (c) 2012-2013, Baycrest Centre for Geriatric Care ("Baycrest")
#
# This program is free software; you can redistribute it and/or modify it under 
# the terms of the GNU General Public License version 2 as published by the Free
# Software Foundation. This program is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public
# License for more details. You should have received a copy of the GNU General 
# Public License along with this program; if not, you can download it here
# http://www.gnu.org/licenses/old-licenses/gpl-2.0
#
#
"""
Created on Mar 20, 2013

.. moduleauthor:: Bogdan Neacsa <bogdan.neacsa@codemart.ro>
"""
import unittest

from tvb.datatypes import projections
from tvb_library_test.base_testcase import BaseTestCase
        
class PatternsTest(BaseTestCase):
    
    def test_projectionmatrix(self):
        dt = projections.ProjectionMatrix()
        self.assertTrue(dt.sources is None)
        self.assertTrue(dt.sensors is None)
        self.assertTrue(dt.projection_data is None)
        
        
    def test_projectionregioneeg(self):
        dt = projections.ProjectionRegionEEG()
        self.assertTrue(dt.sources is None)
        self.assertTrue(dt.sensors is None)
        self.assertTrue(dt.projection_data is None)
        
        
    def test_projectionsurfaceeeg(self):
        dt = projections.ProjectionSurfaceEEG()
        self.assertTrue(dt.sources is None)
        self.assertTrue(dt.skin_air is None)
        self.assertTrue(dt.skull_skin is None)                        
        self.assertTrue(dt.sensors is None)
        self.assertTrue(dt.projection_data is None)
        
        
def suite():
    """
    Gather all the tests in a test suite.
    """
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(PatternsTest))
    return test_suite


if __name__ == "__main__":
    #So you can run tests from this package individually.
    TEST_RUNNER = unittest.TextTestRunner()
    TEST_SUITE = suite()
    TEST_RUNNER.run(TEST_SUITE) 