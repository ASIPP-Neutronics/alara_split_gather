"""alara_spliter utility tests"""
import os

import nose
from nose.tools import assert_equal, assert_not_equal, assert_raises, raises, \
    assert_in, assert_true

from numpy.testing import assert_array_equal, assert_array_almost_equal

import numpy as np
import filecmp
from utils import *


cwd = os.getcwd()

def test_calc_subtask_ids():
    total_num = 5
    num_tasks = 2
    exp_subtask_ids = [[0, 1], [2, 3, 4]]
    subtask_ids = calc_subtask_ids(total_num, num_tasks=num_tasks)
    assert_array_equal(subtask_ids, exp_subtask_ids)


