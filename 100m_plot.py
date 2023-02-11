import pandas as pd
import matplotlib.pyplot as plt

#create dataframe with height and speed of 10 olympic male sprinters 
sprinter_data = {'Name':['Usain Bolt','Justin Gatlin','Tyson Gay','Yohan Blake','Asafa Powell','Noah Lyles','Christian Coleman','Andre De Grasse','Wayde Van Niekerk','Kirani James'], 
        'Height':[6.5,5.9,5.9,5.11,5.11,5.9,5.11,5.10,6.0,5.10],
        '100M':[9.58,9.79,9.71,9.69,9.72,9.86,9.76,9.91,9.94,9.76]}

df = pd.DataFrame(sprinter_data,columns=['Name','Height','100M'])

print(df)

#plot graph to visualize the data
plt.scatter(df['Height'], df['Speed'], color='red')
plt.xlabel('Height (in feet)')
plt.ylabel('100M Speed (in seconds)')
plt.title('Height vs Speed of Olympic Male Sprinters')
plt.show()