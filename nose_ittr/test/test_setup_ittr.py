__author__ = 'Sergey'

from nose.tools import ok_

from nose_ittr import IttrMultiplayer, ittr


class TestSetupIttr(object):

    __metaclass__ = IttrMultiplayer

    def __init__(self):
        self.param_passed = False

    def setup(self):
        if hasattr(self, 'param'):
            self.param_passed = True

    def teardwon(self):
        self.param_passed = False

    @ittr(param=['val_1', 'val_2'])
    def test_ittr_params_to_setup(self):
        ok_(self.param_passed)