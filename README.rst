Basic Image Processing Panel
======================

by Carla Acosta (Idrobo Lab)

A Nion Swift plug-in for Processing (used in Nion Swift)
--------------------------------------------------------
This plugin adds a Basic Image Processing Panel to Nion Swift that streamlines commonly used image processing tasks.

Overview

The panel provides checkboxes for quick access to:
	•	Align
	•	Integrate
	•	Gaussian Filter
	•	Median Filter

Once the desired operations are selected, users can click the Compile button to apply them in sequence as a single processing pipeline.

Inspector Panel Integration

Below the Basic Image Processing Panel, the Inspector Panel can be used to adjust computation parameters.

This plugin works best when the Inspector Panel (found under the Window menu) is open, allowing real-time adjustment of Gaussian sigma values.


 .. image:: https://raw.githubusercontent.com/idrobo-lab/nionswift-plugin-basic-image-processing/master/images/plugin_sample.png
    :alt: Basic Image Processing Panel with check boxes that include Align, Integrate, Gaussian, and Median options with a compile button below. 
    This panel is followed by Inspector Panel on the bottom of the Basic Image Processing Panel with the purpose of using the Computations part with a slider where
    users can adjust sigma value when Gaussian filter is applied. 
    :width: 400px
    :align: center


.. start-badges

.. list-table::
    :stub-columns: 1

    * - package
      - |version|

.. |version| image:: https://img.shields.io/pypi/v/idrobo-lab-nionswift-plugin-basic-image-processing.svg
   :target: https://pypi.org/project/idrobo-lab-nionswift-plugin-basic-image-processing/
   :alt: Latest PyPI version

.. end-badges

More Information
----------------

- `Changelog <https://github.com/idrobo-lab/nionswift-plugin-basic-image-processing/blob/master/CHANGES.rst>`_

