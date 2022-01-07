# Copyright 2021 The T5X Authors.
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

"""Tests for clu.metrics."""

from absl.testing import parameterized
import numpy as np
from t5x import metrics
import tensorflow as tf


class MetricsTest(tf.test.TestCase, parameterized.TestCase):

  @parameterized.named_parameters(
      ("0d_values", 2., 2.), ("1d_values", [1, 2, 3], 6.),
      ("2d_values", [[1, 2], [2, 3], [3, 4]], 15.),
      ("3d_values", [[[1, 2], [2, 3]], [[2, 1], [3, 4]], [[3, 1], [4, 1]]], 27.)
  )
  def test_sum(self, values, expected_result):
    self.assertAllClose(
        metrics.Sum.from_model_output(values).compute(), expected_result)

  def test_time_rate(self):
    value = np.array([3.])
    duration = 2.
    metric = metrics.TimeRate.from_model_output(value).replace_duration(
        duration)
    self.assertAllClose(metric.compute(), value / duration)


if __name__ == "__main__":
  tf.test.main()