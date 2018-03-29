import os

try:
    import unittest2 as unittest
except ImportError:
    import unittest

import textdistance
import textdistance.libraries


# CONSTRAINTS = os.getenv('WITH_CONSTRAINTS', 'yes') == 'yes'
# NUMPY = os.getenv('WITH_NUMPY', 'yes') == 'yes'
CONSTRAINTS = os.environ['WITH_CONSTRAINTS'] == 'yes'
NUMPY = os.environ['WITH_NUMPY'] == 'yes'


from tests import *  # noQA


if __name__ == '__main__':
    unittest.main()
