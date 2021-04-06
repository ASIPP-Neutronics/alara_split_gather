"""tests for alara_split_gather.alara_split_task"""
import os

import nose
from nose.tools import assert_equal, assert_not_equal, assert_raises, raises, \
    assert_in, assert_true

from numpy.testing import assert_array_equal, assert_array_almost_equal

import numpy as np
import filecmp
from alara_split_gather.alara_split_task import *
from alara_split_gather.utils import diff_check_file

cwd = os.getcwd()

def diff_check_file(f1, f2):
    command = ''.join(["diff ", "--strip-trailing-cr ", f1, " ", f2])
    flag = os.system(command)
    return flag


def test_alara_split_inp():
    workdir = os.path.join(cwd, "files_test_split", "split_4_2")
    inp = os.path.join(workdir, "alara_inp")
    exp_sub0 = os.path.join(workdir, "exp_alara_inp_0")
    exp_sub1 = os.path.join(workdir, "exp_alara_inp_1")
    sub0 = os.path.join(workdir, "task0", "alara_inp_0")
    sub1 = os.path.join(workdir, "task1", "alara_inp_1")

    # run alara_split_task
    os.chdir(workdir)
    os.system("alara_split_task -n 2")

    # compare result
    diff_flag_0 = diff_check_file(sub0, exp_sub0)
    diff_flag_1 = diff_check_file(sub1, exp_sub1)

    # check
    assert(diff_flag_0==0)
    assert(diff_flag_1==0)

    # remove A, B, X, Y
    os.system(f"rm -rf {os.path.join(workdir, 'task0')}")
    os.system(f"rm -rf {os.path.join(workdir, 'task1')}")


