import pandas as pd

DataFrame = pd.read_html('https://coronavirus.jhu.edu/data/mortality')

DataFrame[0].to_csv('Covid.csv')

print(DataFrame)



#DataFrame[0].to_csv('Covid.csv')
#https://covid19.who.int/table
#https://www.worldometers.info/coronavirus/