abacusMMM Class
===============

The `abacusMMM` class is designed to streamline the process of fitting, evaluating, and making predictions with Bayesian Marketing Mix Models. The class provides a high-level interface to the modeling capabilities of the `abacusMMM` library, simplifying the complexities involved in model specification, fitting, and evaluation.

Simple Usage
------------

Below is a basic example of how to use the `abacusMMM` class:

.. code-block:: python

    mmm = abacus_mmm.abacusMMM()
    mmm.fit(media=media_data,
            extra_features=extra_features,
            media_prior=costs,
            target=target,
            number_samples=1000,
            number_chains=2)

    # For obtaining media contribution percentage and ROI
    predictions, media_contribution_hat_pct, roi_hat = mmm.get_posterior_metrics()

    # For running predictions on unseen data
    mmm.predict(media=media_data_test, extra_features=extra_features_test)

The class provides methods for fitting models to data, extracting key metrics like media contribution percentages and ROI, and making predictions on new data.

Features
--------

- **Model Fitting**: Fit a Bayesian Marketing Mix Model to your data with customizable settings for priors, sampling, and model specifications.
- **Posterior Metrics**: Easily obtain metrics such as media contribution percentages and ROI based on the fitted model.
- **Predictions**: Use the model to make predictions on unseen data, with support for including extra features in the prediction process.

For more details on the `abacusMMM` class, including its methods and attributes, please refer to the full API documentation.
