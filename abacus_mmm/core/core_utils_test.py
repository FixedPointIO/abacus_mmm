"""Tests for core_utils."""

from lightweight_mmm.core import core_utils
from absl.testing import absltest
import jax
import jax.numpy as jnp
import numpy as np


class CoreUtilsTest(absltest.TestCase):

  def test_apply_exponent_safe_produces_same_exponent_results(self):
    data = jnp.arange(50).reshape((10, 5))
    exponent = jnp.full(5, 0.5)

    output = core_utils.apply_exponent_safe(data=data, exponent=exponent)

    np.testing.assert_array_equal(x=output, y=data**exponent)

  def test_apply_exponent_safe_produces_correct_shape(self):
    data = jnp.ones((10, 5))
    exponent = jnp.full(5, 0.5)

    output = core_utils.apply_exponent_safe(data=data, exponent=exponent)

    self.assertEqual(output.shape, data.shape)

  def test_apply_exponent_safe_produces_non_nan_or_inf_grads(self):

    def f_safe(data, exponent):
      x = core_utils.apply_exponent_safe(data=data, exponent=exponent)
      return x.sum()

    data = jnp.ones((10, 5))
    data = data.at[0, 0].set(0.)
    exponent = jnp.full(5, 0.5)

    grads = jax.grad(f_safe)(data, exponent)

    self.assertFalse(np.isnan(grads).any())
    self.assertFalse(np.isinf(grads).any())


if __name__ == '__main__':
  absltest.main()
