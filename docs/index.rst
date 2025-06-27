==========================================
Stormwater Monitoring Datasheet Extraction
==========================================

Includes typical CLI and library setup. Just the template with example structure for now.

See also the GitHub repository: https://github.com/crickets-and-comb/stormwater_monitoring_datasheet_extraction

This is a `Crickets and Comb <https://cricketsandcomb.org>`_ resource.

Contents
--------

.. toctree::
   :maxdepth: 3

   CLI
   modules

Installation
------------

To install the package, run:

.. code:: bash

    pip install stormwater_monitoring_datasheet_extraction

See https://pypi.org/project/stormwater-monitoring-datasheet-extraction/.


Library
-------

Avoid calling library functions directly and stick to the public API:

.. code:: python

    from stormwater_monitoring_datasheet_extraction import wait_a_second

    wait_a_second()

If you're a power user, you can use the internal API:

.. code:: python

    from stormwater_monitoring_datasheet_extraction.api.internal import wait_a_second

    wait_a_second()


Nothing is stopping you from importing from lib directly, but you should avoid it unless you're developing:

.. code:: python

    from stormwater_monitoring_datasheet_extraction.lib.example import wait_a_second

    wait_a_second()

CLI
---

When this package is installed, it comes with CLI tools. See :doc:`CLI` for more information.