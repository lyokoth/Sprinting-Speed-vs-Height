#Importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Creating the DataFrame
sprinters_df = pd.DataFrame({'Name': ['Usain Bolt', 'Tyson Gay', 'Yohan Blake', 'Justin Gatlin', 'Asafa Powell', 'Christian Coleman', 'Noah Lyles', 'Andre De Grasse', 'Wayde Van Niekerk', 'Micahel Johnson'],
                         'Height (cm)': [195, 183, 186, 185, 183, 180, 183, 185, 184, 188],
                         '100m Sprint Time (s)': [9.58, 9.69, 9.90, 9.94, 9.72, 9.79, 9.86, 9.91, 9.91, 19.32]})

#Printing the DataFrame
sprinters_df

#Visualizing the DataFrame
plt.scatter(sprinters_df['Height (cm)'], sprinters_df['100m Sprint Time (s)'])

#Adding Labels
plt.xlabel('Height (cm)')
plt.ylabel('100m Sprint Time (s)')

#Calculating the correlation coefficient
np.corrcoef(sprinters_df['Height (cm)'], sprinters_df['100m Sprint Time (s)'])

#The correlation coefficient is 0.44 which indicates that there is a weak positive correlation between height and sprinting speed in the 100m.