from ....utils import W3CTestCase

class TestRtlBasic(W3CTestCase):
    vars().update(W3CTestCase.find_tests(__file__, 'rtl-basic'))
