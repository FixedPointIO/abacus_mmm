"""Module for modeling the intercept."""

from typing import Mapping

import immutabledict
import jax.numpy as jnp
import numpyro
from numpyro import distributions as dist

from abacus_mmm.core import core_utils
from abacus_mmm.core import priors


def simple_intercept(
    data: jnp.ndarray,
    custom_priors: Mapping[str,
                           dist.Distribution] = immutabledict.immutabledict(),
) -> jnp.ndarray:
  """Calculates a national or geo incercept.
  Note that this intercept is constant over time.

  Args:
    data: Media input data. Media data must have either 2 dims for national
      model or 3 for geo models.
    custom_priors: The custom priors we want the model to take instead of the
      default ones. Refer to the full documentation on custom priors for
      details.

  Returns:
    The values of the intercept.
  """
  default_priors = priors.get_default_priors()
  n_geos = core_utils.get_number_geos(data=data)

  with numpyro.plate(name=f"{priors.INTERCEPT}_plate", size=n_geos):
    intercept = numpyro.sample(
        name=priors.INTERCEPT,
        fn=custom_priors.get(priors.INTERCEPT,
                             default_priors[priors.INTERCEPT]),
    )
  return intercept
