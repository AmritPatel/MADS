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

./mads.py type solbor1 npanels1 adens1 solbor2 npanels2 adens2

Command-line Argument Definitions
=================================

```
[...]
* [Essential Pascal Version 1 and 2](http://www.marcocantu.com/epascal/)


###DTrace
* [IllumOS Dynamic Tracing Guide](http://dtrace.org/guide/preface.html)
* [Some Other Book](http://so.me/other/book.html)

BAD : * [IllumOS Dynamic Tracing Guide](http://dtrace.org/guide/preface.html)(PDF)
GOOD: * [IllumOS Dynamic Tracing Guide](http://dtrace.org/guide/preface.html) (PDF)

BAD : * [IllumOS Dynamic Tracing Guide](http://dtrace.org/guide/preface.html)- Robert
GOOD: * [IllumOS Dynamic Tracing Guide](http://dtrace.org/guide/preface.html) - Robert

```

type	    # fuel and rack type; options are "pwr" or "bwr"
solbor1		# initial soluble boron concentration in ppm; pwr takes input between 0 and 2500
npanels1	# initial number of degraded panels; must be an integer between 1 and 200
adens1		# initial areal density; must be a number between 0 and 0.022
solbor2		# final soluble boron concentration in ppm; pwr takes input between 0 and 2500
npanels2	# final number of degraded panels; must be an integer between 1 and 200
adens2		# final degraded areal density; must be a number between 0 and 0.022

