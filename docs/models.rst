Models in abacusMMM
===================

The ``abacusMMM`` library offers a range of models for Bayesian Marketing Mix Modeling (MMM) with different options for processing media data. These models allow for comprehensive analyses of media channel effectiveness and support media allocation optimization.

Model Types
-----------

The main model within the ``abacusMMM`` library provides three distinct options for media data transformation, catering to different modeling needs:

- **Adstock**: Implements the adstock transformation to account for the diminishing effect of advertisements over time.
- **Hill-Adstock**: Combines the adstock transformation with the Hill function to model the saturation effect on top of the adstock transformation.
- **Carryover**: Applies a carryover effect, capturing how past media exposures continue to influence outcomes over time.

These transformations enable the construction of three different model types, offering flexibility in addressing various MMM scenarios.

Model Components
----------------

**Transform Function Protocol**

A protocol for transform functions is defined to ensure compatibility and flexibility in processing media data. Transform functions are expected to accept media data and custom priors as inputs and produce transformed media data as output.

**Model and Transform Priors**

The library defines a set of priors for both model parameters and transform functions. These priors can be customized by the user to reflect specific assumptions about the data and the marketing environment.

.. code-block:: python

    Prior = Union[
        dist.Distribution,
        Dict[str, float],
        Sequence[float],
        float
    ]

**Default Priors**

Default priors for model parameters and transformation functions are provided, encapsulating common assumptions in MMM. Users can override these defaults with custom priors to tailor the models to their specific needs.

Transformation Functions
------------------------

Three main transformation functions are provided:

- ``transform_adstock``
- ``transform_hill_adstock``
- ``transform_carryover``

Each function is designed to transform media data according to the specified model type, with options for customization through custom priors and additional parameters.

Contribute
----------

Contributions to the ``abacusMMM`` library are welcome. If you have suggestions for improvements or have identified bugs, please file an issue on our GitHub repository:

- Issue tracker: https://github.com/FixedPointIO/abacus_mmm/issues
- Source code: https://github.com/FixedPointIO/abacus_mmm

