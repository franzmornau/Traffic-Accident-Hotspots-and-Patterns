# Traffic Accident Patterns in Seattle

### *Extending a project by Gulom Saidov*

The city of Seattle publicly provides comprehensive data on traffic, collisions, streets & thier conditions and more. In a first step we dig into timline patterns in the collision data. Further steps will look into accident hotspots in the city and their development over time.




# **Project Goal (step 1):**

- Explore accident data provided by the city of Seattle (2004 - 2019)
- Find time patterns by zooming into the timeline and comparison of time slices over all years
- Find hot spots by clustering using geospacial coordinates ( → later)


# **Motivation**

- Hot spots may be mitigated by planning/construction actions
- Commuters can try to avoid the hot spot, as well as the accident peak times


# **Data**

- Collisions: https://data-seattlecitygis.opendata.arcgis.com/datasets/5b5c745e0f1f48e7a53acec63a0022ab_0

For later use: 
- Roads: https://data-seattlecitygis.opendata.arcgis.com/datasets/seattle-streets
- Traffic flow: https://hub.arcgis.com/datasets/170b764c52f34c9497720c0463f3b58b_9



# **Project step 1:**

**1.** Get collisions data, and enrich them with specific timeline aggregation info$

**2.** Explore the data, zoom into the timeline and indentify some patterns

**3.** State a hypothesis about the distribution over the weeks in a year, and test it$

![Accidents by week](week_count_2015.png)



# Conclusion and next steps

- The Collision data timeline follows some clear patterns, even in a city with little weather variations (no ice/snow)
- Zooming into a timeline brings pattern to light that are not easy to see on first glance (in this case they were easy to guess by knowing the subject). Also: digging deep into one dataset might get farther than merging.
Advice to self: don’t get impatient …
- Let's to continue and find spatial patterns! (steps 2/3)

