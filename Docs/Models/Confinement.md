---
title: Confinement
---

## Output Hierarchy:

## Confinement

### Tier 1 Products
*Only run once*

**Confining Margins**: The actual margins of confinement generated by intersecting the valley bottom with the buffered stream channel polygon.

**Raw confining State**: line network that contains the left, right, both (constricted) or none confinement states. Basically this is the transfer of the confining margins to the original stream network.

### Tier 2 Products 

**Products vary by segmenting methods and settings   
**Can be run multiple times, depending on segmentation requirements*

**Confinement_Segments**: Line network that contains calculated confinement values along its network, generated from the raw confining state. This could be any type of segmentation, fixed length, smart segments, etc.

**Moving Window**
This is another method of looking at confinement values at multiple segmentation lengths.

**Moving Window Seed Points** Common points from which confinement values are generated over a user specified set of window sizes. Each window is centered at each point and a confinement value is generated for each window size. Spacing between seed points are also user defined.

**Moving Window Lines** The actual "windows" (line segments) that the confinement was calculated over. The windows may overlap depending on the user specified window sizes and seed point distance.



## Resources:

* [Sample Project XML](https://github.com/Riverscapes/Program/blob/master/Project/Confinement.xml)