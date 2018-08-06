#   Copyright (c) 2018 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
import numpy as np
from op_test import OpTest

import paddle.fluid.core as core
from paddle.fluid.op import Operator


class TestSamplingIdOp(OpTest):
    def setUp(self):
        self.op_type = "sampling_id"
        self.use_mkldnn = False
        self.init_kernel_type()
        X = np.random.random((3, 4)).astype('float32')
        self.inputs = {"X": X}
        Y = np.random.random(3).astype('float32')
        self.outputs = {'Out': Y}
        self.attrs = {'use_mkldnn': self.use_mkldnn}

    def test_check_output(self):
        self.check_output()

    def test_check_grad(self):
        self.check_grad(['X'], 'Out')

    def init_kernel_type(self):
        pass


if __name__ == "__main__":
    unittest.main()
