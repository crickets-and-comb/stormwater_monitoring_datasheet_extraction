==========================================
Stormwater Monitoring Datasheet Extraction
==========================================

Includes typical CLI and library setup. For now, just the template with example structure.

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

CLI
---

The user interface for this tool is the command-line interface (CLI). When this package is installed, it comes with a CLI tool. See :doc:`CLI` for more information.


Python Library
--------------

You can use this package as a Python library. The public API is available in the `stormwater_monitoring_datasheet_extraction` module.

Avoid calling library functions directly and stick to the public API:

.. code:: python

    from stormwater_monitoring_datasheet_extraction import run_etl

    run_etl(input_dir="path/to/input", output_dir="path/to/output")

If you're a power user, you can use the internal API:

.. code:: python

    from stormwater_monitoring_datasheet_extraction.api.internal import run_etl

    run_etl(input_dir="path/to/input", output_dir="path/to/output")


Nothing is stopping you from importing from lib directly, but you should avoid it unless you're developing:

.. code:: python

    from stormwater_monitoring_datasheet_extraction.lib.load_datasheets import run_etl

    run_etl(input_dir="path/to/input", output_dir="path/to/output")
