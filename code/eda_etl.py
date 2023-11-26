#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import os


# My opinion: -Jing


# 1. alltrails (Y)
# I would suggest to use this dataset, because it includes many columns which are necessary for the recommender, especially if our first DEMO is focus on a certain region (col: location)

# 2. komoot (N)
# I would first NOT use it, however,
# the columns ['Highest point', 'Lowest point'] may be necessary to have. 
# I would try to scrap the two columns from other website, e.g. wanderweg

# 3. sac-cas (N)
# the samples only contain information about the mountain huts
# I would use this link to scrape samples: https://www.sac-cas.ch/en/huts-and-tours/sac-route-portal/
# however, I think it should be fine that we don't use it. It provides similar info as AllTrails

# 4. schweizmobil (Y, maybe for further step)
# the sample were from the filtered link with 'national-routes', each national route contains multiple sub-routes, e.g. please scroll down to this national route: https://schweizmobil.ch/en/hiking-in-switzerland/route-6
# so the sub-routes also have to be scraped and then merged. I guess it might be too much workload for the DEMO. Thus, I would suggest first not use it. Let's check it at the later stage, because the website contains the latest status of the trail which I didn't find in other website. The latest status (trail closed due to extrem weather or maintainance) is important to the user. 

# 5. wegwandern (Y)
# I would recommend to use it
# because these columns ['Level', 'Depression','Seasons'] are not available in alltrails samples, yet the user may be interested in knowing them. Explanation to T1~T5: https://www.sbfi.admin.ch/dam/sbfi/en/dokumente/2017/08/wanderleiter.pdf.download.pdf/notiz_wanderleiter_e.pdf


# Next steps:
# 1) Scrape data from website 1 and 5, and try to get ['Highest point', 'Lowest point'] of each sample in one of the website

# 2) For the first DEMO, I think it should be enough to focus on one region. For later, we can always add all regions. 

# 3) Which region for the DEMO? Basically, I would start with the region that has the most trails. To find the most-trail-region, e.g. in AllTrails, enter each region, it will show all trails of this region.

# 2) Is it possible to scrape photos for each sample? In the frontend, we may need photos to show how the trail looks like besides text. 


# In[115]:


ds_folder = 'C:/Users/jingxian.he/OneDrive - Deutsche Glasfaser Holding GmbH/self_learning/DI/hikemate/datasets/test_samples'


# load csvs

ds_dict = {}

df_list = os.listdir(ds_folder)

for file in df_list:
    ds_dict[file.split('.')[0]] = pd.read_csv(ds_folder + '/' + file)
    
    
for key in ds_dict.keys():
    display(key, ds_dict[key].columns, ds_dict[key].head())

