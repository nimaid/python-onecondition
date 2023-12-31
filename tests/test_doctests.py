import os
import unittest
import doctest

import onecondition
import onecondition.test
import onecondition.validate


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocFileSuite(os.path.join("..", "README.md")))
    tests.addTests(doctest.DocFileSuite(os.path.join("..", "README_pypi.md")))

    tests.addTests(doctest.DocTestSuite(onecondition))
    tests.addTests(doctest.DocTestSuite(onecondition.test))
    tests.addTests(doctest.DocTestSuite(onecondition.validate))
    return tests
