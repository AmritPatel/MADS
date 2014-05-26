MADS
====

Map of Absorber Degradation Sensitivity (MADS) interpolates between an initial and final degradation state point based on data calculated from BWR/PWR SFP fixed neutron absorber degradation sensitivity studies.

Dependencies
============

- Python 2.7
- Numpy
- PyLab

Command-line Execution
======================

```
./mads.py type solbor1 npanels1 adens1 solbor2 npanels2 adens2
```

Command-line Argument Definitions
=================================

```
type	    # fuel and rack type; options are "pwr" or "bwr"
solbor1		# initial soluble boron concentration in ppm; pwr takes input between 0 and 2500
npanels1	# initial number of degraded panels; must be an integer between 1 and 200
adens1		# initial areal density; must be a number between 0 and 0.022
solbor2		# final soluble boron concentration in ppm; pwr takes input between 0 and 2500
npanels2	# final number of degraded panels; must be an integer between 1 and 200
adens2		# final degraded areal density; must be a number between 0 and 0.022
```

Summary Plots
=============

[Delta-k-eff vs. Number of Fully Degraded Panels (BWR SFP)](http://rcharts.io/viewer/?ac77c1d20ad6893806b0#.U4M2VVhdWxw "View in rCharts Viewer")

[Delta-k-eff vs. Number of Fully Degraded Panels (PWR SFP)](http://rcharts.io/viewer/?117ca86a2d5d3f5fbf0a#.U4M251hdWxw "View in rCharts Viewer")

