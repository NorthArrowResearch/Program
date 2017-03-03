---
title: RVD
---

RVD characterizes riparian vegetation condition for a given stream reach (500 m segment) as the ratio of existing vegetation to an estimation of pre-European settlement vegetation coverage. To numerically calculate condition, native riparian vegetation is coded as ‘1’ and invasive and upland classes are coded as ‘0’in both the existing, and pre-European settlement vegetation rasters and condition is calculated as the ratio of current to historic native riparian coverage for a given reach.



## Output Hierarchy:

**Polyline shapefile output**

Attributes:

- EVT_MEAN: the number of existing riparian cells associated with the given feature.
- BPS_MEAN: the number of historic riparian cells associated with the given feature.
- DEP_RATIO: the ratio of existing riparian cells to historic riparian cells for the given feature. (EVT_MEAN/BPS_MEAN).
- COUNT: the number of cells within an analysis area (for RVCT) that were historically riparian.
- sum_noch: the number of cells within the analysis area that have not experienced a change from riparian to another land cover type.
- sum_grsh: the number of cells within the analysis area that have been converted from riparian to grassland or shrubland.
- sum_deveg: the number of cells within the analysis area that were historically riparian but are now devegetated or denuded.  
- sum_con: the number of cells within the analysis area that have been converted from riparian to conifer forest.
- sum_inv: the number of cells within the analysis area that have been converted from riparian to invasive vegetation.
- sum_dev: the number of cells within the analysis area that have were historically riparian that have now been developed.
- sum_ag: the number of cells within the analysis area that have been converted from riparian to agriculture.
- prop_noch: the proportion of cells for the analysis area whose conversion type is 'no change.'
- prop_grsh: the proportion of cells for the analysis area that have been converted to grass or shrubland.
- prop_deveg: the proportion of cells for the analysis area that have been devegetated or denuded.    
- prop_con: the proportion of cells for the analysis area that have been converted to conifer forest.
- prop_inv: the proportion of cells for the analysis area that have been converted to invasive vegetation.
- prop_dev: the proportion of riparian cells for the analysis area that have been developed.
- prop_ag: the proportion of cells for the analysis area that have been converted to agriculture.
- conv_code: a unique integer value that represents different conversion types based on which conversion proportion constitutes a majority for the analysis area.
- conv_type: text field associated with the conv_code value that is used to symbolize the output network for 'Riparian Vegetation Conversion Type (RVCT)'

**Conversion Type Raster Output**

Values:

- 0: No Change
- 50: Conversion to Grass/Shrubland
- 60: Devegetated or Denuded
- 80: Conifer Encroachment
- 97: Conversion to Invasive Vegetation
- 98: Developed
- 99: Conversion to Agriculture

## Resources:

* [Sample Project XML](https://github.com/Riverscapes/Program/blob/master/Project/RVD.xml)