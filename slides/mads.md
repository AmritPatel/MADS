---
title       : Spent Fuel Pool Neutron Absorber Degradation 
subtitle    : K-effective Sensitivity Studies
author      : Amrit D. Patel
job         : NRR/DSS/SRXB/SFT
logo        : NRC.gif
biglogo     : NRC.jpg
framework   : io2012        # {io2012, html5slides, shower, dzslides, ...}
highlighter : highlight.js  # {highlight.js, prettify, highlight}
hitheme     : tomorrow      # 
widgets     : [rCharts: libraries/nvd3]  # {quiz, mathjax, bootstrap} -- can't get mathjax to work
mode        : selfcontained # {standalone, draft}
--- .quote .nobackground .segue

<style>
.title-slide {
  background-color: #FFFFFF; /* #EDE0CF; ; #CA9F9D*/
}
</style>

<q> Any degradation should be modeled <span class = 'red'>conservatively</span>, consistent with the certainty with which the material condition can be established.</q>

Source: [DSS-ISG-2010-01](http://pbadupws.nrc.gov/docs/ML1106/ML110620086.pdf)

---

## Overview

- Motivation
- Degradation studies
- Takeaways

---

## Motivation

- [GL 201X-XX: Monitoring of Neutron Absorbing Materials in Spent Fuel Pools](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0CB0QFjAA&url=http%3A%2F%2Fpbadupws.nrc.gov%2Fdocs%2FML1310%2FML13100A086.pdf&ei=QxfQU_fdG42HogTdnILABQ&usg=AFQjCNH5uxSzF_IA7t-rEecH4wFzkdzvIw&sig2=dooFQi9GJzz0d6EvyKN5Wg&bvm=bv.71667212,d.ZGU) (2014)
- [IN 2014-09: Spent Fuel Storage or Transportation System Misloading](http://pbadupws.nrc.gov/docs/ML1412/ML14121A469.pdf) (2014)
- [IN 2012-13: Boraflex Degradation Surveillance Programs and Corrective Actions in the Spent Fuel Pool](http://pbadupws.nrc.gov/docs/ML1216/ML121660156.pdf) (2012)
- [IN 2009-26: Degradation of Neutron-Absorbing Materials in the Spent Fuel Pool](http://pbadupws.nrc.gov/docs/ML0924/ML092440545.pdf) (2009)
- [GL 96-04: Boraflex Degradation In Spent Fuel Pool Storage](http://www.nrc.gov/reading-rm/doc-collections/gen-comm/gen-letters/1996/gl96004.html) (1996)
- [IN 95-38: Degradation of Boraflex Neutron Absorber in Spent Fuel Storage Racks](http://www.nrc.gov/reading-rm/doc-collections/gen-comm/info-notices/1995/in95038.html) (1995)
- [IN 93-70: Degradation of Boraflex Neutron Absorber Coupons](http://www.nrc.gov/reading-rm/doc-collections/gen-comm/info-notices/1993/in93070.html) (1993)
- [IN 87-43: Gaps in Neutron Absorbing Material in High-Density Spent Fuel Storage Racks](http://www.nrc.gov/reading-rm/doc-collections/gen-comm/info-notices/1987/in87043.html) (1987)

---

## Motivation

- Currently a wide range of degraded conditions among existing plants:
  + Boraflex
  + Carborundum
  + Boral?
  
- Potential for regulatory compliance issues that could lead to safety concerns

- Questions:
  + How much sub-critical margin actually exists in SFPs?
  + How bad can it get?
  + How much benefit to crediting higher burnup fuel?
  + What's the minimum absorber needed at these higher burnups?
  
- Assessment capability

<!-- Need to quickly assess severity for a wide range of scenarios. Need to determine if any margin can be regained. Consequently, we turn to additional BUC: (1) this has already been done extensively for PWRs but (2) there is high value for BWRs.-->

---

## Sensitivity studies 

- Areal density varied between 0 and 0.022 g/cm2
- Degraded panels varied between 1 and 200 
- PWR SFP:
  + W17x17 OFA fuel
  + Burnup at 37, 41, and 44 GWd/MTU
  + Soluble boron between 0 and 2500 ppm
- BWR SFP:
  + GE14 10x10 fuel
  + Burnup at 12 (peak reactivity), 24, and 35 GWd/MTU
  + Void fraction at 0.0 and 0.7
  
<!-- Goals: (1) cover a wide range of conditions; (2) use "modern" fuel designs; (3) for PWR
case, define a "medium burnup credit" reference point and look at benefit of crediting the remaining
burnup; (4) for the BWR case, use the typical peak reactivity approach as the reference point
and look at the benefit of conservatively crediting higher burnup fuel; (5) for the BWR case,
conservatively crediting higher burnup fuel means using limiting depletion conditions up to
the burnup point where credit is being taken; this will involve consideration of void conditions,
control blade insertion and associated axial burnup profile effects, different lattice designs, etc. -- in this work, only sensitivity to void conditions was studied for simplicity.-->

---

## How much sub-critical margin actually exists in SFPs?

<iframe src=' figure/rplot1.html ' scrolling='no' frameBorder='0' seamless class='rChart polycharts ' id=iframe- chart1a4c6c8c73e4 ></iframe> <style>iframe.rChart{ width: 100%; height: 400px;}</style>

<!-- Start with nominal point; explain that as material degrades (i.e. moving up and to the left)
that keff increases eventually surpassing the regulatory limit; this study looks at the potential 
benefit of crediting higher burnup fuel relative to two "typical" design basis SFP criticality 
analyses -- one BWR pool and one PWR pool. For the BWR pool, the design basis analysis is at peak 
reactivity and for the PWR pool it is around 75% of the max creditable burnup.

In the PWR case, it is likely pretty clear that there is less to be gained by crediting burnup
compared to the BWR case since taking full burnup credit is now common practice with PWR fuel. It
is also clear that PWRs have the added benefit of soluble boron (point out huge keff range due to soluble boron). Due to the conservative nature of BWR SFP criticality analyses, it is not so
clear how much margin exists (can see some benefit by looking at the blue points -- the lower
blue points are associated with higher burnup).

NOTE: Areal density sensitivity for BWRs is much greater than PWRs. This is likely due to the
harder spectrum in the PWR case, which reduces the worth of the absorber panels. For the PWR case,
it is seen that there is very little sensitivity between 0.016 and 0.022 g/cm2 (independent of the
number of panels affected) and still little sensitivity at lower areal densities when only a
handful of panels are affected. --> 

---

## How bad can it get?

### PWR case

<iframe src=' figure/nvd3plot2.html ' scrolling='no' frameBorder='0' seamless class='rChart nvd3 ' id=iframe- chart1a4c65e97347 ></iframe> <style>iframe.rChart{ width: 100%; height: 400px;}</style>

<!-- Shows sensitivity to full panel degradation at various soluble boron conditions. It can 
get pretty bad as seen in the cases with no soluble boron. In this case, very localized
degradation (e.g. 4-8 panels) can cause reactivity increases between 500 and 3000 pcm. It is
clear from this plot that PWR SFPs will be limited by the zero soluble boron case when dealing
with degradation in order to meet 10 CFR 50.68. --> 

---

## How bad can it get?

### BWR case

<iframe src=' figure/nvd3plot3.html ' scrolling='no' frameBorder='0' seamless class='rChart nvd3 ' id=iframe- chart1a4c38e075 ></iframe> <style>iframe.rChart{ width: 100%; height: 400px;}</style>

<!-- The sensitivity to varying depletion conditions can be seen here. Note that there are
three clusters of points for each degradation case. The top cluster corresponds to the
reference burnup and the bottom corresponds to the highest burnup case. We can see that as the
burnup increases (i.e. moving from the top cluster to the bottom cluster), the higher void
fraction cases result in a larger reactivity effect. By establishing the limiting depletion 
condition as a function of burnup, conservatism can still be maintained while gaining margin at
the same time. --> 

---

## How much benefit to crediting higher burnup fuel?
### Net k-eff change with degradation at higher burnup
### (PWR, 44 GWd/MTU, 0 ppm solbor)

<iframe src=' figure/nvd3plot4.html ' scrolling='no' frameBorder='0' seamless class='rChart nvd3 ' id=iframe- chart1a4c30a141a2 ></iframe> <style>iframe.rChart{ width: 100%; height: 400px;}</style>

<!-- The 0 ppm case is plotted since it will be limiting with respect to meeting 10 CFR 50.68.
We can see that extensive degradation is still manageable for a range of scenarios; however, it
is important to keep in mind that any net keff increases takes away from margin that might be 
needed for limiting accident analyses.

We can see that substantial degradation could be tolerated in many cases (~25% global) -- point
out close to zero net effect going from 0.022 to 0.016 g/cm2. --> 

---

## How much benefit to crediting higher burnup fuel?
### Net k-eff change with degradation at higher burnup
### (BWR, 35 GWd/MTU, 0 void fraction)

<iframe src=' figure/nvd3plot5.html ' scrolling='no' frameBorder='0' seamless class='rChart nvd3 ' id=iframe- chart1a4c52bc39e4 ></iframe> <style>iframe.rChart{ width: 100%; height: 400px;}</style>

<!-- We can again see that extensive degradation is still manageable for a range of scenarios.

We can see that substantial degradation could be tolerated in many cases (~75% global) -- point
out close to zero net effect going from 0.022 to 0.006 g/cm2. --> 

---

## Assessment capability developed

Utility developed covering full range of degraded conditions to:
  - Give a quick assessment of k-eff impact
  - Give an idea of the value of increased burnup credit
  - Support enforcement activities
  - Perform confirmatory analysis

*** pnotes

- this
- that
- other thing

---

## Assessment capability developed

<img src="https://dl.dropboxusercontent.com/u/22056684/MADS/assets/img/mads.png">

<!-- Histogram plots were added as output to the program in order for the user to explore trends for specific degradation scenarios -->

---

## Takeaways

>  1. Difficult to generically quantify reactivity effects (highly plant-dependent)

>  2. PWRs have to meet two regulatory limits:
    - Potentially significant margin to cope with accidents (crediting soluble boron)
    - For cases without soluble boron, absorber degradation management is limited

>  3. BWRs have to meet one regulatory limit:
    - Employ a very limiting analysis => significant margin (but unquantified)
    - Burnup credit past peak reactivity useful to counter significant absorber degradation
    - Depletion is complex, but bounding approach could be taken

>  4. Assessment capabilities developed to support enforcement and licensing activities
 
<!-- Notes:
(1) 1oo4, 2oo4, etc. not preferable since it opens up possibility for fuel misloads. --> 

---

## References

The data from this presentation (including the scripts used to generate the various plots), and other resources related to this work, are accessible at [https://github.com/AmritPatel/MADS](https://github.com/AmritPatel/MADS).
