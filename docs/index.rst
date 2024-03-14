:github_url: https://github.com/FixedPointIO/abacus_mmm/tree/main/docs

Abacus MMM Documentation
========================

ABACUS enhances the utility of open-source MMM (Marketing Mix Modeling) libraries by simplifying the process of MMM analyses.

ABACUS builds on the Lightweight MMM library, incorporating its advanced features for modern media data analysis. Future updates will include support for additional libraries as required. ABACUS strives to incorporate the most efficient design patterns from libraries like Robyn and PyMC. Despite their contributions, these libraries do not always offer a practical solution for MMM analytics. ABACUS seeks to bridge this gap.

It allows users to:

- Conduct MMM analyses easily using a standard CSV file.
- Start with standardized defaults while offering customization options.
- Produce various plots, organized in timestamped folders for easy access.

It is built in python3 and makes use of Numpyro and JAX.

.. toctree::
   :caption: Overview
   :maxdepth: 2

   abacus

.. toctree::
   :caption: Detailed Model Documentation
   :maxdepth: 2

   models

.. toctree::
   :caption: Custom Priors
   :maxdepth: 1

   custom_priors

.. toctree::
   :caption: API Documentation
   :maxdepth: 2

   api

.. toctree::
   :caption: Additional Resources
   :maxdepth: 2

   results.md
   config.md

.. toctree::
   :caption: FAQ
   :maxdepth: 2

   faq

Contribute
----------

- Issue tracker: https://github.com/FixedPointIO/abacus_mmm/issues
- Source code: https://github.com/FixedPointIO/abacus_mmm/tree/main

Support
-------

If you are having issues, please let us know by filing an issue on our
`issue tracker <https://github.com/FixedPointIO/abacus_mmm/issues>`_.

Indices and tables
==================

* :ref:`genindex`
