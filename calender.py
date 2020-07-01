import pandas as pd
import requests
from bs4 import BeautifulSoup
import lxml as lxml

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 100000)

file = open("C://Users/LEE JUNWEI/Desktop/Coding/NTU Calender Parser/timetable.html")
contents = file.read()

soup = BeautifulSoup(contents, "lxml")

table = soup.find_all('table')
df = pd.read_html(str(table))[0]

df.to_csv('timetable.csv', index=False) 



