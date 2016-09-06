import unittest
import os
import sys
import MV2
import cdms2
from CDP.PMP.PMPIO import *

class testPMPIO(unittest.TestCase):

    def setUp(self):
        self.path = os.path.realpath(__file__).replace('test_PMPIO.py', '')
        self.filename = 'test'
        self.pmp_io = PMPIO(self.path, self.filename)

    def test_write_with_failing_extension(self):
        with self.assertRaises(RuntimeError):
            self.pmp_io.write({}, extension='py')

    def test_write_json_with_no_failures(self):
        try:
            self.pmp_io.write({}, extension='json')
        except:
            self.fail('Cannot write json file. Test failed.')
        finally:
            os.remove(self.path + '/' + self.filename + '.json')

    def test_write_txt_with_no_failures(self):
        try:
            self.pmp_io.write({}, extension='txt')
        except:
            self.fail('Cannot write txt file. Test failed.')
        finally:
            os.remove(self.path + '/' + self.filename + '.txt')

    def test_write_nc_with_no_failures(self):
        try:
            self.pmp_io.write(MV2.arange(12.), extension='nc')
        except:
            self.fail('Cannot write Net-CDF file. Test failed.')
        finally:
            os.remove(self.path + '/' + self.filename + '.nc')

    def test_set_target_grid_with_noncdms2_and_no_failures(self):
        try:
            self.pmp_io.set_target_grid('2.5x2.5', 'regrid2', 'linear')
        except:
            self.fail('Error using set_target_grid(). Test failed.')

    def test_set_target_grid_with_cdms2_and_no_failures(self):
        try:
            grid=cdms2.grid.createUniformGrid(
                -90, 181, 1, 0, 361, 1, order="yx"
            )
            self.pmp_io.set_target_grid(grid, 'regrid2', 'linear')
        except:
            self.fail('Error using set_target_grid(). Test failed.')


if __name__ == '__main__':
    unittest.main()
