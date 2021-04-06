"""alara_spliter utility tests"""
import os

import nose
from nose.tools import assert_equal, assert_not_equal, assert_raises, raises, \
    assert_in, assert_true

from numpy.testing import assert_array_equal, assert_array_almost_equal

import numpy as np
import filecmp
from alara_split_gather.utils import assign_subtasks

cwd = os.getcwd()

def test_assign_subtasks():
    # 
    total_num = 4
    num_tasks = 2
    exp_subtasks = [[0, 1], [2, 3]]
    subtasks = assign_subtasks(total_num, num_tasks=num_tasks)
    assert_array_equal(subtasks, exp_subtasks)
    #  
    total_num = 5
    num_tasks = 2
    exp_subtasks = [[0, 1], [2, 3, 4]]
    subtasks = assign_subtasks(total_num, num_tasks=num_tasks)
    assert_array_equal(subtasks, exp_subtasks)


