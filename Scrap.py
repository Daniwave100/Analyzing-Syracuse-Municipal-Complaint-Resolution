'''

Datasets:
- Syracuse Roadwork Map

SYRCityline map seems cool
App that lets you report non-emergency problems in Syracuse. Things users can report:

Adopt-a-Block Trash Pick-Up
Dead/Loose Animal
Debris on Street or Road
Junk Cars/Yard Debris
Parks & Recreation Field Maintenance
Pothole
Snow Plow Request
Street Light Repair
Street Sign
Traffic Signal Issue
Trash/Illegal Dumping
Tree Limb Down/Obstructing Sidewalk
Vacant or Abandoned Buildings
Water Main Break/Leak
Carts
Bulk Setouts

Things I can analyze:
- Whether or not there are more requests during a given time of year and why

Clean data.         We will need a NLP text-classification model to label our data for us into different categories.
    - Take care of issues that were not closed
    -

Main question to ask: How efficient is the city at resolving issues?

We can also get the time taken to resolve an issue and see how long it takes to resolve different types of issues

Question: How efficient is the city at resolving issues? and what type of complaints get the most attention?
          What type of complaints get the most attention?
            - Analyze which type of complaint takes longest to resolve (what can city get better at)
            - Analyze which type of complaint takes shortest to resolve (what does city prioritize)
                - Stacked bar charts, complaint types by resolution time


            - Which department does a good job at fixing results?
            - Make a ML model that predicts how long an issue will take to fix depending on issue type
                    - Consider linear regression
                    - Consider decision tree regressor
                    - Consider random forest regressor


'''



import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("SYRCityline_Requests.csv")

category = pd.read_csv("DatathonCategories.csv")
category.head()
category.info()


# Question 1: When and where are we getting more reports? (Presumably in winter)
#             - Analyze what season we get more reports (Focus on pothole, water main break/leak,street light repair, street sign, traffic sign issue)
#             - do streetlight repairs change with shorter daylight
#                 - Time-series plot: Number of pothole reports per month
#                 - Bar-chart: Complaint types by season
#                 - Complaint map density before vs. after snowstorm















