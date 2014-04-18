import sys
import warnings

import numpy as np
import pylab as plt

def autolabel(rects, ax):

  ''' This function prints values on top of bar graph bars. ''' 

    # attach some text labels
  for rect in rects:
    height = rect.get_height()
    ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
            ha='center', va='bottom')

def barsumm(a, b):

  ''' This function produces degradation summary plots that are a function of soluble boron and fuel type.'''

  solbor = a
  type   = b

  n = 12

  # List of x-values that will be used to generate y-values in various plots.
  dens = [0, 0.002, 0.004, 0.006, 0.008, 0.01, 0.012, 0.014, 0.016, 0.018, 0.02, 0.022]
 
  # Generate subplot 1 of 3. This is a plot of the degradation data at the reference BU.
  ax = plt.subplot(311)

  # Iterate over x-values to produce a list of y-values in 'state' for each data series.
  diff1 = []
  for i in dens:
    # The number of panels on the summary plot can be changed if desired.
    state = sens(i, 4, solbor, type)
    diff1.append(state[0]/1e5)

  diff2 = []
  for i in dens:
    # The number of panels on the summary plot can be changed if desired.
    state = sens(i, 20, solbor, type)
    diff2.append(state[0]/1e5)

  diff3 = []
  for i in dens:
    # The number of panels on the summary plot can be changed if desired.
    state = sens(i, 200, solbor, type)
    diff3.append(state[0]/1e5)       

  # Create the x-axis indices.
  ind = np.arange(n)
  # Define the bar width.
  width = 0.30
  # Define the bar opacity.
  opacity = 0.6
 
  # Populate the subplot with each data series.
  rects1 = ax.bar(ind, diff1, width, alpha=opacity, facecolor='0.9', align='center')
  rects2 = ax.bar(ind+width, diff2, width, alpha=opacity, facecolor='0.5', align='center')
  rects3 = ax.bar(ind+2*width, diff3, width, alpha=opacity, facecolor='0.0', align='center')

  # Create the figure title depending on fuel type.
  if type == 'bwr':
   ax.set_title('Reactivity Effect from Varying Panel B-10 Areal Density for Various Degraded\n Absorber Panel Configurations Relative\
 to the Non-Degraded Reference Model\n(BWR SFP Model)', fontsize=12)
  elif type == 'pwr':
   ax.set_title('Reactivity Effect from Varying Panel B-10 Areal Density for Various Degraded\nAbsorber Panel Configurations Relative\
 to the Non-Degraded Reference Model\n(PWR SFP Model, {0} ppm Soluble Boron)'.format(solbor), fontsize=12)  

  # Add x-axis tick marks to the plot.
  ax.set_xticks(ind+width)
  # Add x-axis labels.
  ax.set_xticklabels( ('0', '0.002', '0.004', '0.006', '0.008', '0.010', '0.012', '0.014', '0.016', '0.018', '0.020', '0.022') )
  #ax.set_xlabel(r'Areal Density (g/cm$^2$)')
  #ax.set_ylabel(r'$\Delta$k$_{eff}$ (pcm)')  
  
  # Add the plot legend.
  ax.legend( (rects1[0], rects2[0], rects3[0]), ('4 panels', '20 panels', '200 panels'), loc=1, prop={'size':12}, labelspacing=0.2 )
  # Add a line at y=0 for easy plot reading.
  ax.axhline(linewidth=1, color='black')
  # Auto-fit the data for legibility.
  ax.autoscale(tight=True)

  # This is a plot of the degradation data at 1.1 or 2.0 times reference BU depending on fuel type.
  ax = plt.subplot(312)
   
  diff1 = []
  for i in dens:
    # The number of panels on the summary plot can be changed if desired.
    state = sens(i, 4, solbor, type)
    diff1.append((state[0] - state[1])/1e5)

  diff2 = []
  for i in dens:
    # The number of panels on the summary plot can be changed if desired.
    state = sens(i, 20, solbor, type)
    diff2.append((state[0] - state[1])/1e5)

  diff3 = []
  for i in dens:
    # The number of panels on the summary plot can be changed if desired.
    state = sens(i, 200, solbor, type)
    diff3.append((state[0] - state[1])/1e5) 

  rects1 = ax.bar(ind, diff1, width, alpha=opacity, facecolor='0.9', align='center')
  rects2 = ax.bar(ind+width, diff2, width, alpha=opacity, facecolor='0.5', align='center')
  rects3 = ax.bar(ind+2*width, diff3, width, alpha=opacity, facecolor='0.0', align='center')
  
  ax.set_xticks(ind+width)
  ax.set_xticklabels( ('0', '0.002', '0.004', '0.006', '0.008', '0.010', '0.012', '0.014', '0.016', '0.018', '0.020', '0.022') )
  #ax.set_xlabel(r'Areal Density (g/cm$^2$)')
  ax.set_ylabel(r'$\Delta$k$_{eff}$', fontsize=14)  
  ax.legend( (rects1[0], rects2[0], rects3[0]), ('4 panels', '20 panels', '200 panels'), loc=1, prop={'size':12}, labelspacing=0.2 )  
  ax.axhline(linewidth=1, color='black')
  ax.autoscale(tight=True)

  # This is a plot of the degradation data at 1.2 or 3.0 times reference BU depending on fuel type.
  ax = plt.subplot(313)
 
  diff1 = []
  for i in dens:
    # The number of panels on the summary plot can be changed if desired.
    state = sens(i, 4, solbor, type)
    diff1.append((state[0] - state[2])/1e5)

  diff2 = []
  for i in dens:
    # The number of panels on the summary plot can be changed if desired.
    state = sens(i, 20, solbor, type)
    diff2.append((state[0] - state[2])/1e5)

  diff3 = []
  for i in dens:
    # The number of panels on the summary plot can be changed if desired.
    state = sens(i, 200, solbor, type)
    diff3.append((state[0] - state[2])/1e5) 

  rects1 = ax.bar(ind, diff1, width, alpha=opacity, facecolor='0.9', align='center')
  rects2 = ax.bar(ind+width, diff2, width, alpha=opacity, facecolor='0.5', align='center')
  rects3 = ax.bar(ind+2*width, diff3, width, alpha=opacity, facecolor='0.0', align='center')

  ax.set_xticks(ind+width)
  ax.set_xticklabels( ('0', '0.002', '0.004', '0.006', '0.008', '0.010', '0.012', '0.014', '0.016', '0.018', '0.020', '0.022') )
  ax.set_xlabel(r'Areal Density (g/cm$^2$)', fontsize=14)
  #ax.set_ylabel(r'$\Delta$k$_{eff}$ (pcm)')  
  ax.legend( (rects1[0], rects2[0], rects3[0]), ('4 panels', '20 panels', '200 panels'), loc=1, prop={'size':12}, labelspacing=0.2 )    
  ax.axhline(linewidth=1, color='black')
  ax.autoscale(tight=True)

  # Add subtitles to subplots describing the fuel burnup.
  if type == 'bwr':
    plt.figtext( 0.5, 0.8, '1.0 x Burnup', fontsize=14, ha='center')
    plt.figtext( 0.5, 0.525, '2.0 x Burnup', fontsize=14, ha='center' )
    plt.figtext( 0.5, 0.25, '3.0 x Burnup', fontsize=14, ha='center' )
  elif type == 'pwr':
    plt.figtext( 0.5, 0.8, '1.0 x Burnup', fontsize=14, ha='center' )
    plt.figtext( 0.5, 0.525, '1.1 x Burnup', fontsize=14, ha='center' )
    plt.figtext( 0.5, 0.25, '1.2 x Burnup', fontsize=14, ha='center' )   

  #autolabel(rects1, ax)
  #autolabel(rects2, ax)
  #autolabel(rects3, ax)  

  # Make the plots prettier.
  plt.tight_layout()
  # Display the final plot.
  plt.show()

def barstate(a, b, c, d, e):

  ''' This function produces degradation summary plots given two statepoints. See comments in 'barsumm' function for specifics
      on various statements as they are similar. '''

  pan1 = a
  pan2 = b
  solbor1 = c
  solbor2 = d
  type    = e

  dens = [0, 0.002, 0.004, 0.006, 0.008, 0.01, 0.012, 0.014, 0.016, 0.018, 0.02, 0.022]
  
  n = 12
  ind = np.arange(n)
  width = 0.30
  opacity = 0.6

  ax = plt.subplot(311)

  diffs1 = []
  for i in dens:
    state1 = sens(i, pan1, solbor1, type)
    state2 = sens(i, pan2, solbor2, type)  
    diffs1.append(state2[0] - state1[0])

  rects1 = ax.bar(ind+width, diffs1, width, alpha=opacity, facecolor='0.9', align='center')

  if type == 'bwr':
   ax.set_title('Reactivity Effect from Varying Panel B-10 Areal Density for Various Degraded\n Absorber Panel Configurations Relative\
 to the Non-Degraded Reference Model\n(BWR SFP Model)', fontsize=12)
  elif type == 'pwr':
   ax.set_title('Reactivity Effect from Varying Panel B-10 Areal Density for Various Degraded\nAbsorber Panel Configurations Relative\
 to the Non-Degraded Reference Model\n(PWR SFP Model, {0}->{1} ppm Soluble Boron)'.format(solbor1, solbor2), fontsize=12)  

  ax.set_xticks(ind+width)
  ax.set_xticklabels( ('0', '0.002', '0.004', '0.006', '0.008', '0.010', '0.012', '0.014', '0.016', '0.018', '0.020', '0.022') )
  #ax.set_xlabel(r'Areal Density (g/cm$^2$)')
  #ax.set_ylabel(r'$\Delta$k$_{eff}$ (pcm)')
  #ax.legend('panels', loc=1, prop={'size':10}, labelspacing=0.2 )  
  ax.axhline(linewidth=1, color='black')
  #ax.autoscale(tight=True)

  ax = plt.subplot(312)
   
  diffs2 = []
  for i in dens:
    state1 = sens(i, pan1, solbor1, type)
    state2 = sens(i, pan2, solbor2, type)
    diffs2.append( (state2[0] - state2[1]) - (state1[0] - state1[1]) )

  rects1 = ax.bar(ind+width, diffs2, width, alpha=opacity, facecolor='0.9', align='center')
  
  ax.set_xticks(ind+width)
  ax.set_xticklabels( ('0', '0.002', '0.004', '0.006', '0.008', '0.010', '0.012', '0.014', '0.016', '0.018', '0.020', '0.022') )
  #ax.set_xlabel(r'Areal Density (g/cm$^2$)')
  ax.set_ylabel(r'$\Delta$k$_{eff}$ (pcm)')
  #ax.legend( (rects1[0], rects2[0], rects3[0]), ('4 panels', '20 panels', '200 panels'), loc=1, prop={'size':10}, labelspacing=0.2 )  
  ax.axhline(linewidth=1, color='black')
  #ax.autoscale(tight=True)

  ax = plt.subplot(313)
 
  diffs3 = []
  for i in dens:
    state1 = sens(i, pan1, solbor1, type)
    state2 = sens(i, pan2, solbor2, type)  
    diffs3.append( (state2[0] - state2[2]) - (state1[0] - state1[2]) )

  rects1 = ax.bar(ind+width, diffs3, width, alpha=opacity, facecolor='0.9', align='center')

  ax.set_xticks(ind+width)
  ax.set_xticklabels( ('0', '0.002', '0.004', '0.006', '0.008', '0.010', '0.012', '0.014', '0.016', '0.018', '0.020', '0.022') )
  ax.set_xlabel(r'Areal Density (g/cm$^2$)')
  #ax.set_ylabel(r'$\Delta$k$_{eff}$ (pcm)')  
  #ax.legend( (rects1[0], rects2[0], rects3[0]), ('4 panels', '20 panels', '200 panels'), loc=1, prop={'size':10}, labelspacing=0.2 ) 
  ax.axhline(linewidth=1, color='black')
  #ax.autoscale(tight=True)

  if type == 'bwr':
    plt.figtext( 0.5, 0.8, '1.0 x Burnup\n{0}->{1} panels'.format(pan1, pan2), fontsize=12, ha='center')
    plt.figtext( 0.5, 0.525, '2.0 x Burnup\n{0}->{1} panels'.format(pan1, pan2), fontsize=12, ha='center' )
    plt.figtext( 0.5, 0.25, '3.0 x Burnup\n{0}->{1} panels'.format(pan1, pan2), fontsize=12, ha='center' )
  elif type == 'pwr':
    plt.figtext( 0.5, 0.8, '1.0 x Burnup\n{0}->{1} panels'.format(pan1, pan2), fontsize=12, ha='center' )
    plt.figtext( 0.5, 0.525, '1.1 x Burnup\n{0}->{1} panels'.format(pan1, pan2), fontsize=12, ha='center' )
    plt.figtext( 0.5, 0.25, '1.2 x Burnup\n{0}->{1} panels'.format(pan1, pan2), fontsize=12, ha='center' )   

  #autolabel(rects1, ax)
  #autolabel(rects2, ax)
  #autolabel(rects3, ax)  

  plt.tight_layout()
  plt.show()

def zindex(a):
  
  ''' This function returns the index of the requested soluble boron state for use with sensdata. Also returned
      is the upper and lower soluble boron statepoints surrounding the requested soluble boron state in order to 
      perform linear interpolation in the sens function. '''
  
  nums = [0, 500, 1000, 1500, 2000, 2500]
  
  count = -1
  for i in nums:
    count = count + 1
    if float(a) <= i:
      break
  
  return count, nums[count], nums[count-1]

def yindex(a):

  ''' This function returns the index of the requested number of degraded panels for use with sensdata. Also returned
      is the upper and lower numbers of degraded panels surrounding the requested number of degraded panels in order to 
      perform linear interpolation in the sens function. '''

  nums = [0, 1, 2, 3, 4, 8, 12, 20, 40, 80, 200]
  
  count = -1
  for i in nums:
    count = count + 1
    if int(a) <= i:
      break

  return count, nums[count], nums[count-1]
  
def xindex(a):
  
  ''' This function returns the index of the requested degraded panel state for use with sensdata. Also returned
      is the upper and lower degraded panel statepoints surrounding the requested degraded panel state in order to 
      perform linear interpolation in the sens function. '''  
  
  nums = [0, 0.002, 0.004, 0.006, 0.008, 0.01, 0.012, 0.014, 0.016, 0.018, 0.02, 0.022]
  
  count = -1
  for i in nums:
    count = count + 1
    if float(a) <= i:
      break
     
  return count, nums[count], nums[count-1]
  
def sensdata(a, b):

  ''' This function retrieves the degradation sensitivity data for both type = 'pwr' and type = 'bwr'. For the 'pwr' case,
      the reference burnup is 37 GWd/MTU and for the 'bwr' case it is 12 GWd/MTU.'''
	  
  bwrdata0 =    [0, 249, 573, 1676, 3344, 8096, 11367, 16153, 21345, 25148, 30305, \
                 0, 126, 188, 384, 602, 1793, 3153, 5404, 8477, 10957, 14760, \
                 0, 100, 196, 246, 343, 917, 1439, 2819, 4924, 7025, 10216, \
                 0, 130, 153, 162, 269, 504, 918, 1672, 3212, 4819, 7665, \
                 0, 52, 79, 130, 221, 314, 543, 1072, 2153, 3565, 5814, \
                 0, 87, 75, 85, 167, 245, 419, 704, 1538, 2536, 4493, \
                 0, 78, 127, 86, 70, 232, 316, 513, 1037, 1848, 3439, \
                 0, 38, 23, 96, 57, 146, 199, 277, 659, 1243, 2530, \
                 0, 93, 26, 72, 46, 108, 141, 239, 496, 878, 1784, \
                 0, 58, 70, 44, 60, 100, 86, 124, 293, 527, 1134, \
                 0, 87, -40, 68, 108, 34, 141, 32, 160, 250, 606, \
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  pwrdata0 =    [0, 157, 556, 1728, 3151, 6104, 7836, 10271, 12642, 14343, 16442, \
                 0, 29, 154, 257, 574, 1561, 2472, 3829, 5561, 6722, 8425, \
                 0, 19, 51, 133, 184, 698, 1232, 2073, 3305, 4317, 5756, \
                 0, -24, 5, 50, 160, 328, 627, 1195, 2109, 2961, 4296, \
                 0, 6, 73, 93, 56, 243, 374, 749, 1466, 2113, 3321, \
                 0, 27, 13, 77, 115, 187, 264, 483, 942, 1452, 2559, \
                 0, -16, 31, 25, 29, 133, 163, 284, 634, 1064, 1919, \
                 0, 0, -18, -2, 26, 67, 80, 247, 415, 769, 1420, \
                 0, -55, 37, 9, -1, 7, 56, 123, 242, 495, 975, \
                 0, -47, -29, 18, -32, 26, 39, 17, 145, 271, 602, \
                 0, 28, -18, 5, -43, 22, -14, 53, 48, 46, 308, \
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  pwrdata500 =  [0, 189, 382, 1076, 2046, 4303, 5701, 7657, 9688, 11083, 12837, \
                 0, 56, 159, 232, 481, 1218, 2011, 3065, 4494, 5516, 6931, \
                 0, 28, 139, 125, 236, 563, 993, 1696, 2829, 3581, 4939, \
                 0, 87, 72, 83, 203, 295, 572, 994, 1838, 2570, 3682, \
                 0, 8, 79, 41, 138, 222, 349, 596, 1294, 1859, 2918, \
                 0, 87, 59, 74, 137, 187, 313, 435, 856, 1360, 2258, \
                 0, 68, 45, 72, 90, 161, 164, 326, 635, 964, 1694, \
                 0, 78, 31, 93, 71, 107, 149, 234, 359, 654, 1211, \
                 0, 51, 55, 87, 29, 75, 77, 134, 221, 455, 949, \
                 0, 72, 47, 42, 0, 60, 39, 79, 116, 233, 612, \
                 0, 71, 1, 39, 23, 45, 64, 34, 201, 154, 300, \
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  pwrdata1000 = [0, 135, 281, 691, 1429, 3177, 4308, 5949, 7644, 8905, 10504, \
                 0, 96, 95, 172, 316, 967, 1514, 2503, 3669, 4634, 5962, \
                 0, 2, 140, 128, 201, 469, 766, 1462, 2381, 3086, 4258, \
                 0, 14, 73, 15, 148, 307, 473, 824, 1515, 2235, 3227, \
                 0, 3, 60, 46, 92, 139, 267, 542, 1021, 1648, 2498, \
                 0, 33, 48, 12, 124, 159, 203, 294, 728, 1202, 1976, \
                 0, 56, 8, 63, 86, 105, 140, 251, 508, 837, 1492, \
                 0, 42, 82, 72, 5, 66, 109, 216, 300, 611, 1089, \
                 0, 51, 5, -29, 4, 89, 105, 148, 198, 428, 801, \
                 0, -4, -85, 80, -27, 33, 67, 113, 133, 233, 465, \
                 0, 3, 4, 16, 21, 47, 44, 73, 66, 139, 201, \
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  pwrdata1500 = [0, 59, 166, 493, 1062, 2467, 3464, 4866, 6288, 7435, 8831, \
                 0, 41, 52, 137, 274, 770, 1337, 2127, 3269, 4058, 5259, \
                 0, 72, 59, 99, 117, 407, 708, 1216, 2036, 2757, 3849, \
                 0, 11, 64, 55, 97, 261, 344, 632, 1323, 1932, 2886, \
                 0, 83, 39, 73, 96, 182, 224, 465, 912, 1414, 2268, \
                 0, 12, 46, 103, 86, 66, 164, 298, 671, 1028, 1769, \
                 0, -8, -8, 14, 56, 79, 129, 226, 393, 747, 1387, \
                 0, 1, 26, 59, 57, 42, 77, 100, 332, 556, 1014, \
                 0, 13, 36, -48, 11, 80, 43, 157, 217, 347, 774, \
                 0, -17, 63, 5, 8, 29, 17, 42, 126, 198, 452, \
                 0, -22, -41, 13, 4, 12, 29, 73, 51, 79, 232, \
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  pwrdata2000 = [0, -4, 113, 395, 774, 1927, 2763, 3928, 5366, 6287, 7604, \
                 0, 19, 16, 77, 145, 593, 1074, 1767, 2784, 3546, 4681, \
                 0, -1, 34, 48, 149, 275, 593, 1100, 1663, 2367, 3378, \
                 0, -44, -26, 14, 9, 174, 319, 673, 1173, 1777, 2597, \
                 0, -63, 15, 26, 50, 52, 222, 384, 795, 1237, 2045, \
                 0, -48, -58, -8, -19, 30, 131, 295, 580, 908, 1622, \
                 0, -45, -50, -2, 24, 35, 94, 164, 395, 679, 1209, \
                 0, -61, -13, 38, -47, 40, -37, 25, 272, 429, 845, \
                 0, -25, 8, -3, -50, 7, 29, 84, 75, 318, 636, \
                 0, -30, -20, -65, -23, -38, 44, -23, 108, 162, 361, \
                 0, -44, 1, -20, 1, -58, 7, -12, -23, 54, 198, \
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  pwrdata2500 = [0, 77, 156, 285, 538, 1535, 2335, 3333, 4559, 5497, 6717, \
                 0, 32, 72, 48, 176, 568, 943, 1490, 2425, 3174, 4217, \
                 0, 11, 38, 54, 143, 260, 513, 950, 1600, 2201, 3140, \
                 0, 28, 63, 90, 109, 161, 352, 581, 1033, 1615, 2483, \
                 0, -13, 65, 54, -1, 119, 212, 322, 773, 1172, 1919, \
                 0, -8, 42, 48, -10, 79, 180, 246, 540, 912, 1558, \
                 0, 40, -42, 86, 67, 40, 70, 161, 361, 637, 1161, \
                 0, 21, -18, 18, -22, 66, 37, 100, 141, 463, 800, \
                 0, -14, -3, -7, 22, 15, 12, 94, 131, 341, 626, \
                 0, -47, -17, -16, -21, 37, 16, 26, 114, 154, 388, \
                 0, -12, 17, -11, 31, 24, -36, 80, 83, 85, 231, \
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  
  bwr0    = tuple(bwrdata0[n:n+11]    for n in range(0, len(bwrdata0), 11))
  pwr0    = tuple(pwrdata0[n:n+11]    for n in range(0, len(pwrdata0), 11))
  pwr500  = tuple(pwrdata500[n:n+11]  for n in range(0, len(pwrdata500), 11))
  pwr1000 = tuple(pwrdata1000[n:n+11] for n in range(0, len(pwrdata1000), 11))
  pwr1500 = tuple(pwrdata1500[n:n+11] for n in range(0, len(pwrdata1500), 11))
  pwr2000 = tuple(pwrdata2000[n:n+11] for n in range(0, len(pwrdata2000), 11))
  pwr2500 = tuple(pwrdata2500[n:n+11] for n in range(0, len(pwrdata2500), 11))
  
  data = (bwr0, pwr0, pwr500, pwr1000, pwr1500, pwr2000, pwr2500)
  
  if b == 'bwr':
    request = data[0]
  elif b == 'pwr':
    request = data[a+1]
  
  return request
  
def ob1data(a, b):

  ''' This function retrieves the sensitivity data generated from using 10% overburned fuel for type = 'pwr' and 100%
      overburned fuel for type = 'bwr' at a void fraction of 0.0.'''

  bwrdata0 =    [0, 103, 199, 826, 1412, 2398, 2879, 3491, 3900, 4074, 4396, \
                 0, 90, 94, 217, 231, 940, 1655, 2499, 3188, 3523, 3974, \
                 0, 92, 111, 125, 124, 491, 850, 1624, 2546, 3207, 3822, \
                 0, 59, 145, 82, 143, 285, 592, 1156, 2058, 2783, 3758, \
                 0, 70, 110, 29, 138, 193, 414, 788, 1583, 2524, 3618, \
                 0, 73, 70, 97, 71, 183, 277, 546, 1350, 2149, 3550, \
                 0, 71, 115, 71, 62, 174, 313, 452, 1015, 1878, 3553, \
                 0, 53, 32, 100, 111, 155, 229, 294, 817, 1531, 3524, \
                 0, 119, 17, 86, 36, 134, 201, 354, 690, 1469, 3427, \
                 0, 61, 113, 39, 68, 114, 174, 249, 628, 1210, 3456, \
                 0, 139, -15, 96, 94, 74, 285, 260, 550, 1039, 3472, \
                 0, 83, 115, 115, 83, 51, 103, 277, 449, 1053, 3351]
  pwrdata0 =    [0, 24, 109, 270, 355, 496, 536, 567, 569, 614, 704, \
                 0, 67, 69, 3, 176, 213, 353, 406, 692, 549, 679, \
                 0, -17, -19, 29, -60, 208, 293, 382, 492, 530, 555, \
                 0, -49, -7, -22, 7, 90, 135, 226, 436, 535, 604, \
                 0, -10, 71, 38, 35, 105, 105, 226, 390, 484, 604, \
                 0, -24, -19, 104, 38, 82, 115, 183, 295, 365, 555, \
                 0, -25, 63, 56, 21, 89, 65, 109, 227, 383, 557, \
                 0, 74, -20, 33, 9, 4, 34, 154, 200, 359, 536, \
                 0, -109, 73, 55, 1, 3, 81, 145, 102, 279, 483, \
                 0, -54, -9, 29, -5, 30, 36, 58, 136, 213, 500, \
                 0, 96, 32, -5, -53, 24, -67, 96, 137, 168, 521, \
                 0, 48, 70, -51, 90, 11, -1, 82, 93, 163, 522]
  pwrdata500 =  [0, 5, 70, 212, 294, 431, 548, 549, 631, 667, 632, \
                 0, -33, -20, 11, 149, 206, 368, 421, 558, 546, 531, \
                 0, -24, -4, -19, 58, 100, 188, 351, 488, 486, 519, \
                 0, 62, 63, 12, 87, 34, 143, 239, 363, 478, 544, \
                 0, -27, -14, -37, 70, 60, 78, 136, 390, 459, 595, \
                 0, 36, 10, 31, 48, 99, 107, 160, 274, 432, 559, \
                 0, 33, 37, -10, 45, 56, 28, 135, 205, 321, 454, \
                 0, 24, -17, 75, -19, 53, 46, 104, 146, 281, 421, \
                 0, -9, 43, 65, -59, 42, 22, 79, 122, 265, 548, \
                 0, 25, -13, -10, -19, 46, -13, 35, 63, 165, 470, \
                 0, 62, -36, -9, -6, -8, 38, 27, 218, 252, 525, \
                 0, 35, 62, 87, -16, -19, 11, 17, 82, 163, 452]
  pwrdata1000 = [0, -18, 44, 152, 305, 343, 457, 546, 535, 651, 681, \
                 0, 37, -17, 14, 84, 231, 337, 424, 443, 467, 544, \
                 0, -2, 56, 14, 56, 134, 95, 331, 430, 442, 486, \
                 0, -31, 44, -78, 97, 72, 98, 234, 376, 502, 508, \
                 0, -2, 21, 4, 94, -42, 88, 197, 328, 445, 514, \
                 0, -2, 29, -57, 98, 136, 57, 105, 294, 448, 509, \
                 0, 9, 30, 9, 40, 63, 108, 113, 216, 323, 451, \
                 0, 36, 106, 96, -68, 52, 59, 93, 149, 326, 467, \
                 0, 31, -73, -105, -44, 103, -15, 57, 186, 307, 533, \
                 0, 10, -129, 44, -37, 41, 99, 149, 135, 190, 477, \
                 0, -39, -27, 11, 37, 46, 48, 69, 137, 211, 495, \
                 0, 3, 31, 8, 64, 65, 60, 81, 173, 114, 501]
  pwrdata1500 = [0, -17, -9, 177, 266, 419, 465, 545, 537, 639, 581, \
                 0, 82, 8, 2, 117, 209, 344, 317, 589, 476, 516, \
                 0, 64, 22, 9, 28, 166, 231, 279, 439, 475, 561, \
                 0, -16, 42, -14, 61, 93, 142, 128, 370, 385, 475, \
                 0, 42, 12, 32, 26, 80, 84, 150, 271, 373, 466, \
                 0, -51, 73, 78, 20, -17, 67, 85, 334, 346, 545, \
                 0, -7, -25, 11, 17, 39, 91, 91, 235, 260, 480, \
                 0, 5, 33, 13, 74, 11, 7, 83, 249, 315, 471, \
                 0, -32, 13, -75, -12, 59, -9, 91, 147, 251, 505, \
                 0, -60, 8, 14, -13, 31, 101, 42, 118, 188, 427, \
                 0, -75, -44, 49, -16, 15, -12, 115, 118, 120, 451, \
                 0, -28, -12, 24, 9, 20, 18, 90, 107, 160, 543]
  pwrdata2000 = [0, 13, 31, 165, 249, 339, 384, 394, 573, 534, 631, \
                 0, 42, -6, 0, 15, 159, 301, 337, 478, 545, 578, \
                 0, -20, 83, 5, 72, 85, 225, 343, 307, 469, 487, \
                 0, -8, -19, 9, -17, 29, 92, 259, 344, 442, 436, \
                 0, -50, 75, 4, 73, -9, 97, 95, 249, 381, 509, \
                 0, 2, -102, 30, -38, -13, 75, 121, 300, 364, 523, \
                 0, 10, -41, 14, 41, 8, 95, 94, 252, 329, 443, \
                 0, 17, 36, 62, -67, 35, -16, 7, 135, 211, 445, \
                 0, 33, 30, 21, -47, 42, 61, 91, 18, 236, 493, \
                 0, -4, 18, -34, 18, 59, 76, -34, 132, 217, 451, \
                 0, -33, 52, 39, -1, -65, 60, 38, 53, 203, 504, \
                 0, -23, 62, 14, 59, 28, -3, 119, 88, 120, 506]
  pwrdata2500 = [0, -7, 64, 73, 68, 264, 421, 398, 417, 545, 586, \
                 0, -47, 6, -71, 89, 155, 292, 312, 357, 477, 552, \
                 0, 29, 39, -19, 69, 125, 192, 320, 346, 443, 499, \
                 0, 7, 40, 95, 105, 54, 117, 198, 260, 457, 562, \
                 0, -20, 15, 51, -48, 33, 68, 24, 323, 327, 576, \
                 0, 31, 16, -15, -67, -14, 55, 104, 231, 346, 541, \
                 0, 51, 7, 42, -2, 30, 65, 72, 118, 305, 485, \
                 0, 33, -78, 9, -34, 50, 63, 41, 64, 274, 421, \
                 0, 73, 17, -18, 11, -4, 49, 69, 85, 240, 455, \
                 0, -59, -5, 32, 39, 84, 37, 59, 154, 129, 453, \
                 0, 23, 78, -2, -20, 95, -74, 73, 171, 201, 491, \
                 0, -54, 48, -5, 45, 28, 101, 1, 73, 125, 448]
  
  bwr0    = tuple(bwrdata0[n:n+11]    for n in range(0, len(bwrdata0), 11))
  pwr0    = tuple(pwrdata0[n:n+11]    for n in range(0, len(pwrdata0), 11))
  pwr500  = tuple(pwrdata500[n:n+11]  for n in range(0, len(pwrdata500), 11))
  pwr1000 = tuple(pwrdata1000[n:n+11] for n in range(0, len(pwrdata1000), 11))
  pwr1500 = tuple(pwrdata1500[n:n+11] for n in range(0, len(pwrdata1500), 11))
  pwr2000 = tuple(pwrdata2000[n:n+11] for n in range(0, len(pwrdata2000), 11))
  pwr2500 = tuple(pwrdata2500[n:n+11] for n in range(0, len(pwrdata2500), 11))
  
  data = (bwr0, pwr0, pwr500, pwr1000, pwr1500, pwr2000, pwr2500)
  
  if b == 'bwr':
    request = data[0]
  elif b == 'pwr':
    request = data[a+1]
  
  return request
  
def ob2data(a, b):

  ''' This function retrieves the sensitivity data generated from using 20% overburned fuel for type = 'pwr' and 200%
      overburned fuel for type = 'bwr' at a void fraction of 0.0.'''

  bwrdata0 =    [0, 241, 435, 1220, 2359, 4900, 6083, 7455, 8410, 9007, 9614, \
                 0, 154, 196, 316, 373, 1483, 2591, 4367, 6373, 7338, 8660, \
                 0, 167, 181, 247, 260, 809, 1331, 2647, 4460, 6137, 8305, \
                 0, 202, 183, 175, 271, 426, 938, 1732, 3254, 4983, 8076, \
                 0, 72, 117, 194, 237, 353, 589, 1129, 2400, 4175, 7836, \
                 0, 148, 77, 94, 159, 302, 494, 901, 1954, 3408, 7748, \
                 0, 131, 163, 95, 117, 332, 440, 766, 1563, 2936, 7630, \
                 0, 152, 12, 195, 133, 281, 391, 542, 1192, 2504, 7493, \
                 0, 89, 86, 153, 144, 219, 390, 549, 1103, 2171, 7450, \
                 0, 122, 170, 55, 110, 236, 238, 500, 987, 1902, 7425, \
                 0, 130, 35, 119, 133, 204, 383, 380, 842, 1668, 7404, \
                 0, 29, 61, 61, 29, 148, 329, 465, 753, 1514, 7265]
  pwrdata0 =    [0, 107, 188, 542, 763, 971, 1032, 1218, 1234, 1333, 1395, \
                 0, 10, 119, 61, 177, 539, 568, 840, 1129, 1096, 1293, \
                 0, -3, 46, -5, 50, 349, 514, 698, 837, 1047, 1083, \
                 0, -4, -30, 5, 141, 120, 299, 546, 790, 846, 1107, \
                 0, 5, 64, 77, 49, 194, 211, 387, 714, 838, 1106, \
                 0, 55, 68, 68, 104, 163, 149, 316, 549, 748, 1124, \
                 0, 39, 25, 21, 28, 79, 143, 170, 400, 661, 1076, \
                 0, 39, -52, -30, 65, 57, 92, 253, 296, 627, 1018, \
                 0, -35, 36, 46, 5, 15, 46, 156, 254, 487, 984, \
                 0, -14, 19, 8, -110, 27, 98, 78, 260, 404, 1060, \
                 0, 112, -47, -4, -20, 58, 8, 110, 175, 312, 995, \
                 0, 98, 44, -15, 83, 18, 8, 144, 189, 272, 952]
  pwrdata500 =  [0, 57, 89, 368, 537, 822, 972, 1081, 1219, 1246, 1250, \
                 0, -62, 63, 78, 195, 445, 672, 804, 1048, 1117, 1081, \
                 0, -57, 111, -4, 111, 241, 438, 635, 912, 910, 1074, \
                 0, 101, -38, -62, 59, 111, 273, 385, 804, 896, 1047, \
                 0, -34, 16, -51, 33, 45, 84, 302, 660, 803, 1087, \
                 0, 50, 36, 53, 25, 44, 226, 255, 515, 705, 1091, \
                 0, 63, 26, 11, 30, 129, 82, 235, 465, 556, 969, \
                 0, 20, 49, 7, 91, 25, 106, 119, 257, 510, 867, \
                 0, 9, 42, 23, -12, 38, 36, 97, 224, 473, 1042, \
                 0, 30, 69, 14, -58, 57, 8, 76, 163, 320, 996, \
                 0, 37, -46, -34, -22, 50, 57, 39, 294, 371, 959, \
                 0, -34, 118, 53, 26, 31, 10, 123, 182, 301, 923]
  pwrdata1000 = [0, 108, 131, 188, 529, 827, 821, 990, 1172, 1219, 1230, \
                 0, 49, 51, 8, 178, 409, 555, 793, 927, 1001, 1110, \
                 0, -6, 92, 42, 82, 263, 357, 642, 923, 898, 1032, \
                 0, 68, 62, -23, 149, 187, 223, 395, 703, 888, 1061, \
                 0, -26, 44, 48, 56, 63, 123, 308, 599, 857, 1064, \
                 0, 37, 31, 5, 103, 107, 75, 163, 443, 742, 1014, \
                 0, 76, -18, 3, 105, 72, 110, 205, 380, 603, 1003, \
                 0, 60, 77, 110, -49, 37, 77, 226, 250, 536, 897, \
                 0, 0, 21, -25, 26, 58, 155, 116, 161, 516, 986, \
                 0, -6, -83, 76, -7, 45, 83, 195, 158, 440, 887, \
                 0, -5, -61, 48, 7, 49, 68, 121, 150, 375, 911, \
                 0, 20, 44, -27, 77, 42, 92, 78, 188, 291, 948]
  pwrdata1500 = [0, -8, 48, 223, 446, 749, 864, 1029, 1038, 1183, 1129, \
                 0, 30, 39, 52, 138, 355, 591, 777, 1043, 1014, 1078, \
                 0, 59, 83, 8, 52, 121, 339, 550, 831, 919, 1073, \
                 0, -19, 32, 54, 10, 196, 160, 268, 616, 787, 1036, \
                 0, 89, 57, 55, 65, 123, 138, 205, 511, 797, 1023, \
                 0, -28, 30, 66, 55, 0, 92, 231, 432, 619, 921, \
                 0, 4, -20, 37, -8, 15, 115, 205, 303, 574, 983, \
                 0, -18, 0, 60, 14, 44, 102, 102, 284, 552, 926, \
                 0, -15, 39, -75, 71, 61, 65, 179, 211, 377, 1041, \
                 0, -38, 73, 61, 48, 65, 17, 46, 270, 339, 962, \
                 0, -45, -2, 19, 70, 19, 81, 138, 162, 290, 950, \
                 0, -61, 29, 16, 27, 59, 32, 111, 197, 249, 926]
  pwrdata2000 = [0, 48, 52, 285, 296, 685, 750, 881, 1108, 1107, 1147, \
                 0, 14, -16, -15, 31, 275, 502, 624, 909, 990, 1076, \
                 0, 50, 59, 37, 108, 145, 330, 568, 585, 827, 1021, \
                 0, -33, 37, 7, -53, 107, 206, 402, 661, 827, 936, \
                 0, -34, 16, 17, 18, 7, 173, 275, 486, 690, 988, \
                 0, 29, -53, 10, 0, 23, 87, 305, 461, 641, 1054, \
                 0, -1, -13, 10, 14, 21, 115, 157, 310, 634, 1003, \
                 0, -34, -8, 77, -32, 73, -23, 50, 312, 389, 900, \
                 0, 23, 85, 3, -30, 53, 44, 164, 163, 439, 955, \
                 0, 57, -6, -17, 43, 19, 110, 62, 228, 365, 842, \
                 0, -55, 58, -2, 21, -62, 116, 77, 94, 298, 938, \
                 0, 42, -18, 35, 90, 80, -23, 148, 127, 291, 882]
  pwrdata2500 = [0, 83, 82, 107, 192, 577, 717, 833, 1043, 1077, 1102, \
                 0, -31, 42, -5, 49, 295, 359, 555, 795, 967, 1007, \
                 0, 46, -1, 0, 124, 65, 286, 467, 705, 816, 958, \
                 0, 112, 45, 54, 78, 89, 176, 349, 540, 787, 996, \
                 0, -8, 42, 20, -24, 94, 156, 139, 473, 664, 913, \
                 0, 39, 45, 36, 53, 61, 136, 127, 366, 674, 984, \
                 0, 23, -46, 110, 32, -4, 23, 183, 364, 574, 928, \
                 0, 15, -2, 85, 3, 83, 24, 135, 90, 491, 866, \
                 0, -30, 35, -6, 14, 76, 72, 157, 169, 415, 931, \
                 0, -59, 52, 15, -56, 50, 4, 22, 234, 294, 896, \
                 0, -8, 31, -50, 37, 62, -17, 159, 233, 332, 942, \
                 0, -13, 44, 6, 118, -2, 60, 48, 151, 272, 856]
  
  bwr0    = tuple(bwrdata0[n:n+11]    for n in range(0, len(bwrdata0), 11))
  pwr0    = tuple(pwrdata0[n:n+11]    for n in range(0, len(pwrdata0), 11))
  pwr500  = tuple(pwrdata500[n:n+11]  for n in range(0, len(pwrdata500), 11))
  pwr1000 = tuple(pwrdata1000[n:n+11] for n in range(0, len(pwrdata1000), 11))
  pwr1500 = tuple(pwrdata1500[n:n+11] for n in range(0, len(pwrdata1500), 11))
  pwr2000 = tuple(pwrdata2000[n:n+11] for n in range(0, len(pwrdata2000), 11))
  pwr2500 = tuple(pwrdata2500[n:n+11] for n in range(0, len(pwrdata2500), 11))
  
  data = (bwr0, pwr0, pwr500, pwr1000, pwr1500, pwr2000, pwr2500)
  
  if b == 'bwr':
    request = data[0]
  elif b == 'pwr':
    request = data[a+1]
  
  return request
   
def ob3data(a):

  ''' This function retrieves the sensitivity data generated from using overburned fuel at a void fraction of 0.7.
      The bwrdata100 contains 100% overburned data and bwrdata200 contains the 200% overburned data. This function is only
      accessible for type = 'bwr'.'''

  bwrdata100 =  [0, 165, 216, 491, 1111, 1919, 2260, 2659, 2965, 3216, 3397, \
                 0, 84, 173, 179, 298, 739, 1326, 1908, 2523, 2797, 3079, \
                 0, 20, 125, 16, 156, 281, 720, 1291, 2112, 2460, 2961, \
                 0, 85, 83, 51, 91, 304, 451, 808, 1712, 2174, 2935, \
                 0, 136, 38, 60, -6, 214, 353, 706, 1334, 1954, 2742, \
                 0, 2, 44, 71, 76, 213, 280, 415, 1029, 1721, 2714, \
                 0, 53, 96, 51, -21, 185, 175, 412, 863, 1499, 2693, \
                 0, 48, 94, 30, 49, 106, 188, 290, 728, 1268, 2686, \
                 0, 81, 75, 66, 46, 148, 119, 328, 591, 1141, 2663, \
                 0, 64, 99, 62, 32, 54, 209, 287, 565, 988, 2670, \
                 0, 67, 66, -17, 51, 45, 131, 157, 400, 843, 2604, \
                 0, -8, 17, 22, -8, 75, 44, 128, 454, 737, 2565]
  bwrdata200 =  [0, 246, 454, 996, 2015, 4080, 5001, 6097, 6820, 7322, 7830, \
                 0, 176, 169, 367, 477, 1351, 2301, 3836, 5272, 6093, 6982, \
                 0, 92, 187, 192, 214, 636, 1215, 2331, 3992, 5301, 6673, \
                 0, 136, 105, 125, 207, 499, 786, 1498, 3004, 4401, 6506, \
                 0, 159, 92, 156, 58, 354, 631, 1119, 2245, 3670, 6342, \
                 0, 72, 155, 138, 174, 355, 543, 799, 1695, 3064, 6214, \
                 0, 121, 86, 92, 105, 311, 318, 710, 1427, 2614, 6137, \
                 0, 177, 81, 78, 55, 278, 298, 568, 1175, 2221, 6132, \
                 0, 119, 116, 67, 80, 236, 311, 483, 1020, 1886, 6053, \
                 0, 126, 123, 85, 94, 175, 289, 479, 886, 1675, 6032, \
                 0, 141, 125, 64, 88, 168, 181, 296, 732, 1459, 5944, \
                 0, 43, 68, 68, 43, 140, 202, 256, 693, 1271, 5864]
  
  bwr100    = tuple(bwrdata100[n:n+11]    for n in range(0, len(bwrdata100), 11))
  bwr200    = tuple(bwrdata200[n:n+11]    for n in range(0, len(bwrdata200), 11))
    
  data = (bwr100, bwr200)
  
  request = data[a]
  
  return request
 
def testdata():
  
  listdatatable = ob3data(0)
  list
  datatable = tuple(listdatatable[n:n+12] for n in range(0, len(listdatatable)+1, 13))
  
  print datatable[0][11]
  
def sens(a, b, c, d):

  ''' This function linearly interpolates between several data tables to calculate various reactivity sensitivities for a specified
      degraded panel state.'''

  dens   = a
  pan    = b
  solbor = c
  type   = d
  
  senslist = [ ]
  
  # Each iteration of the loop performs an interpolation on different sets of data.
  
  for i in range(1, 6):    
    
    if i == 4 and type == 'pwr':
      break
    
    # Here the data indices are determined based on the user input along with boundaries need to perform the various linear interpolation operations.
    
    (xind, dbnds1, dbnds2) = xindex(a)
    (yind, pbnds1, pbnds2) = yindex(b)
    (zind, bbnds1, bbnds2) = zindex(c)
    
    # This if block is used to determine the order of data retrieval.
    
    if i == 1:
      listdatatable = sensdata(zind-1, type)
    elif i == 2:
      listdatatable = ob1data(zind-1, type)
    elif i == 3:
      listdatatable = ob2data(zind-1, type)
    elif i == 4:
      listdatatable = ob3data(0)
    elif i == 5:
      listdatatable = ob3data(1)
  
    datatable = tuple(listdatatable[n:n+12] for n in range(0, len(listdatatable)+1, 13))
  
    # This block of code performs the first two linear interpolation operations.
    
    dsens1 = datatable[0][xind][yind-1] - ( datatable[0][xind][yind-1] - datatable[0][xind-1][yind-1] ) * ( float(dbnds1) - float(dens) ) / ( float(dbnds1) - float(dbnds2) )
    dsens2 = datatable[0][xind][yind]   - ( datatable[0][xind][yind]   - datatable[0][xind-1][yind] )  *  ( float(dbnds1) - float(dens) ) / ( float(dbnds1) - float(dbnds2) )
    
    # This is the third linear interpolation operation.
    
    psens1 = dsens2 - (dsens2 - dsens1) * (float(pbnds1) - int(pan)) / (float(pbnds1) - float(pbnds2))   
    
    if i == 1:  
      listdatatable = sensdata(zind, type)
    elif i == 2:
      listdatatable = ob1data(zind, type)
    elif i == 3:
      listdatatable = ob2data(zind, type)
    elif i == 4:
      listdatatable = ob3data(0)
    elif i == 5:
      listdatatable = ob3data(1) 
   
    datatable = tuple(listdatatable[n:n+12] for n in range(0, len(listdatatable)+1, 13))
   
    # This block of code performs the fourth and fifth linear interpolation operations.
   
    dsens3 = datatable[0][xind][yind-1] - ( datatable[0][xind][yind-1] - datatable[0][xind-1][yind-1] ) * ( float(dbnds1) - float(dens) ) / ( float(dbnds1) - float(dbnds2) )
    dsens4 = datatable[0][xind][yind]   - ( datatable[0][xind][yind]   - datatable[0][xind-1][yind] )  *  ( float(dbnds1) - float(dens) ) / ( float(dbnds1) - float(dbnds2) )
   
    # This is the sixth linear interpolation operation.
    
    psens2 = dsens4 - (dsens4 - dsens3) * (float(pbnds1) - int(pan)) / (float(pbnds1) - float(pbnds2))  
    
    # This is the seventh linear interpolation operation.
    
    bsens = psens2 - (psens2 - psens1) * (float(bbnds1) - float(solbor)) / (float(bbnds1) - float(bbnds2))
    
    # Here the result is rounded to the nearest pcm.
    
    bsens = int(round(bsens))
    
    # The result is then added to the list that is returned at the end of the loop.
    
    senslist.append(bsens)
    
  return senslist

def warn(a):

  ''' A function that generates warnings based on the rules defined in main. '''  

  if a == 1:
    print '\nWARNING: You are extrapolating (1 <= panels <= 200)!'
  elif a == 2:
    print '\nWARNING: You are extrapolating (0 <= soluble boron <= 2500)!'
  
def main():

  ''' The main function takes user input from the command line and feeds it to the sens function in order to:
        
		(1) calculate the k-eff sensitivity from one degradation state to another based on pre-calculated data,
	    (2) calculate the k-eff sensitivity from using higher burnup fuel based on pre-calculated data

      A summary of the calculated information is then printed to the screen. '''

  
  # Retrieve user input from command line.
  
  try:
    type    = sys.argv[1]
  except IndexError:
    sys.exit('\nSeven inputs are required: [type] [solbor1] [panels1] [dens1] [solbor2] [panels2] [dens2]')  
  try:
    solbor1 = sys.argv[2]
  except IndexError:
    sys.exit('\nSeven inputs are required: [type] [solbor1] [panels1] [dens1] [solbor2] [panels2] [dens2]')
  try:
    pan1    = sys.argv[3]
  except IndexError:
    sys.exit('\nSeven inputs are required: [type] [solbor1] [panels1] [dens1] [solbor2] [panels2] [dens2]')
  try:
    dens1   = sys.argv[4]
  except:
    sys.exit('\nSeven inputs are required: [type] [solbor1] [panels1] [dens1] [solbor2] [panels2] [dens2]')  
  try:
    solbor2 = sys.argv[5]
  except:
    sys.exit('\nSeven inputs are required: [type] [solbor1] [panels1] [dens1] [solbor2] [panels2] [dens2]')
  try:	
    pan2    = sys.argv[6]
  except:
    sys.exit('\nSeven inputs are required: [type] [solbor1] [panels1] [dens1] [solbor2] [panels2] [dens2]')
  try:	
    dens2   = sys.argv[7]
  except:
    sys.exit('\nSeven inputs are required: [type] [solbor1] [panels1] [dens1] [solbor2] [panels2] [dens2]')  
  
  # Perform error checking. Code exits if input is unacceptable. Code warns if input results in data extrapolation.
  
  if type != 'bwr' and type != 'pwr':
    sys.exit('\nAllowable type is either "pwr" or "bwr"!')
    
  if type == 'bwr' and ( float(solbor1) or float(solbor2) ) != 0:
    sys.exit('\nFor the "bwr" case, the soluble boron must be zero!')
    
  if ( round(float(pan1)) != float(pan1) ) or ( round(float(pan2)) != float(pan2) ):
    sys.exit('\nPanels must be an integer!')

  if int(pan2) < int(pan1):
    sys.exit('\nFinal number of panels >= initial number of panels!\n')

  if float(dens2) > float(dens1):
    sys.exit('\nFinal areal density <= initial areal density!\n')

  if int(pan1) < 1 :
    # This error is necessary due to a limitation of the data (i.e. there is no 0 panel data at higher burnups)
    # This is something that could be added, but doing so would not be worth the effort since the 1 panel data
    # would provide a good enough estimate.
    sys.exit('\nInitial number of panels must be >= 1 !')

  if float(dens1) > 0.022 :
    # This error is necessary due to a limitation of the algorithm. Cannot get indexing to work for the 0.022
    # row of data. 
    sys.exit('\nInitial density must be <= 0.022 !')

  if float(dens1) < 0.000 or float (dens2) < 0.000 :
    sys.exit('\nDensity cannot be < 0 !')	

  if type == 'pwr' and ( float(solbor1) < 0 or float(solbor2) < 0 ):
    sys.exit('\nSoluble boron concentration cannot be < 0 !')		
  
  if int(pan1) > 200 or int(pan2) > 200 :
    warnings.simplefilter("ignore")
    warn(1)

  if type == 'pwr' and ( float(solbor1) > 2500 or float(solbor2) > 2500 ):
    warnings.simplefilter("ignore")
    warn(2) 

  # Two calls to the sens function to calculate all reactivity differences; results are returned in a list.
  
  state1 = sens(dens1, pan1, solbor1, type)
  state2 = sens(dens2, pan2, solbor2, type)  
  
  # Results are printed to the screen.
  
  print '\nState 1: {0:>8} g/cm2, {1:>8} panel(s), {2:>8} ppm sol boron'.format(dens1, pan1, solbor1)
  print 'State 2: {0:>8} g/cm2, {1:>8} panel(s), {2:>8} ppm sol boron'.format(dens2, pan2, solbor2)

  if type == 'pwr':
    print '\nThe reference burnup = 37 GWd/MTU'
  elif type == 'bwr':
    print '\nThe reference burnup = 12 GWd/MTU'

  print '\nk-eff increase w/ fuel @ 1.0 x BU = {0:-5} pcm'.format( state2[0] - state1[0] )
  
  if type == 'pwr':
    print 'k-eff increase w/ fuel @ 1.1 x BU = {0:-5} pcm'.format( (state2[0] - state2[1]) - (state1[0] - state1[1]) )
    print 'k-eff increase w/ fuel @ 1.2 x BU = {0:-5} pcm'.format( (state2[0] - state2[2]) - (state1[0] - state1[2]) )	
  elif type == 'bwr':
    print 'k-eff increase w/ fuel @ 2.0 x BU = {0:-5} pcm  (0% V)'.format( (state2[0] - state2[1]) - (state1[0] - state1[1]) )
    print 'k-eff increase w/ fuel @ 3.0 x BU = {0:-5} pcm  (0% V)'.format( (state2[0] - state2[2]) - (state1[0] - state1[2]) )
    print 'k-eff increase w/ fuel @ 2.0 x BU = {0:-5} pcm (70% V)'.format( (state2[0] - state2[3]) - (state1[0] - state1[3]) )
    print 'k-eff increase w/ fuel @ 3.0 x BU = {0:-5} pcm (70% V)'.format( (state2[0] - state2[4]) - (state1[0] - state1[4]) )	

  barstate(pan1, pan2, solbor1, solbor2, type)
  
  # Uncomment statement below for summary plot that is a function of soluble boron and type.

  barsumm(0, 'bwr')
  barsumm(0, 'pwr')
 
if __name__ == '__main__':
  main()
