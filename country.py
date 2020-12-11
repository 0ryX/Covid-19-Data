import pandas as pd

df = pd.read_csv('Covid.csv')

country = df[(df['Country'] == input('Enter Country: '))]

print(country)






#country confirmed deaths case-fatality deaths/100k pop 