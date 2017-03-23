---
title: RCA
---

The Riparian Condition Assessment (RCA) tool models the condition of riparian areas based on three inputs: riparian vegetation departure (as modeled using the RVD tool), land use intensity, and floodplain connectivity. Each segment of an input network is attributed with values on continuous scales for each of these three inputs. The output (condition) of each segment is then assessed using a fuzzy inference system. The tool produces an output polyline shapefile which includes the three model inputs as attributes, as well as an output table that contains the calculated condition for each segment which can be joined to the polyline using the "FID" field.

# RCA Results

**Polyline shapefile output** 

Attributes:

- **RVD**: the Riparian Vegetation Departure score, which represents the proportion of historic or potential riparian vegetation that currently exists for the given feature.  
- **LUI**: Land Use Intensity index (0-1) where 0 is high intensity land use (e.g. urbanization) and 1 is no land use (i.e. a natural state).
- **CONNECT**: The proportion of the floodplain that is accessible to the stream (i.e. has not been cut off by transportation infrastructure).
- **VEG**: the proportion of historic vegetation (riparian or non-riparian) that currently exists for the given feature.
- **COND_VAL**: An index value from 0 (poor) to 1 (intact) for the unconfined stream segments that are run through an FIS to calculate riparian and floodplain condition. 
- **CONDITION**: Categorical condition based on the condition value (COND_VAL).  There are 5 categories for the unconfined segments whose value is calculated using an FIS, and 2 categories for the confined segments.

## Resources:

* [Sample Project XML](https://github.com/Riverscapes/Program/blob/master/Project/RCA.xml)