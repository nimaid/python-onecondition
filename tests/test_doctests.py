import unittest
import doctest

import onecondition
import onecondition.validate
import onecondition.test

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(onecondition))
    tests.addTests(doctest.DocTestSuite(onecondition.validate))
    tests.addTests(doctest.DocTestSuite(onecondition.test))
    return tests
