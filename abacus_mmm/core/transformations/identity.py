"""Module for identity transformations."""

from typing import Any
import jax.numpy as jnp


def identity_transform(
    data: jnp.ndarray,  # pylint-ignore: unused-argument
    *args: Any,
    **kwargs: Any,
) -> jnp.ndarray:
  """Identity transform. Returns the main input as is."""
  return data
