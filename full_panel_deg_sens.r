# Shows the effect of having the SFP @ various fuel burnups as a function of varying
# numbers of full panel degradation.

library(ggplot2)
library(rCharts)
library(dplyr)
library(RCurl)

# Read in the data
x <- getURL("https://raw.githubusercontent.com/AmritPatel/MADS/master/summary_database.csv")
summary_database <- read.csv(text = x)
# Use dataframe wrapper
summary_df <- tbl_df(summary_database)

# Create "case" as a function of number of degraded panels, pool type, pool soluble boron,
# burnup, and void fraction
case <- group_by(summary_df, panels_deg, type, solbor, burnup, vf)
# Calculate max delta-k-eff -- i.e. diff between full panel degradation and no degradation
adens_0 <- summarise(case,
                     dk =  nth(keff, 1) - last(keff))
# Filter the full degradation delta-k-effs to include only BWR results
bwr_full_deg <- filter(adens_0, type == "bwr")

# Create stacked rplot separating data by VF to summarize the BWR data
r1 <- rPlot(dk ~ panels_deg | vf, 
            data = bwr_full_deg,
            color = 'burnup', 
            type = 'point',
            size = list(const = 3)
            )
r1$guides(x = list(min = 0, max = 210),
          y = list(min = 0, max = 0.35)
          )
r1$addParams(title = "Delta-k-eff vs. Number of Fully Degraded Panels (BWR SFP)")
#r1$publish("Delta-k-eff vs. Number of Fully Degraded Panels (BWR SFP)", host = 'gist')

# Filter the full degradation delta-k-effs to include only PWR results
pwr_full_deg <- filter(adens_0, type == "pwr")

# Create stacked rplot separating data by solbor to summarize the PWR data
r2 <- rPlot(dk ~ panels_deg | solbor,
            data = pwr_full_deg,
            color = 'burnup', 
            type = 'point',
            size = list(const = 3)
            )
r2$guides(x = list(min = 0, max = 210),
          y = list(min = 0, max = 0.18)
          )
r2$addParams(title = "Delta-k-eff vs. Number of Fully Degraded Panels (PWR SFP)")
#r2$publish("Delta-k-eff vs. Number of Fully Degraded Panels (PWR SFP)", host = 'gist')