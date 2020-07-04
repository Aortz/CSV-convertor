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

df.to_csv('timetable.csv', index = 'False')

# for i in df:
# 	monday_lessons = df[1]
# 	timings = df[0]


# class_series = df.to_dict(orient='split')
# del class_series['index']
# del class_series['columns']

# schedule = {}
# # schedule[class_series[0]] = class_series[1]
# for key, value in class_series.items():
# 	for item in value:
# 		# schedule[item[0]] = item[1:6]
# 		schedule_list =item[0:7]
# 		break

# programms_by_day = []
# which_day = int(4) + 1 #if possible, can create input value asking for users to give a date from Mon to Fri as numeric value
# splice = int(which_day - 1)
# for key, value in class_series.items():
# 	for item in value[1:]:

# 		try:
# 			programms_by_day.append(item[0:which_day:splice])
# 		except ValueError:
# 			programms_by_day.append(item[0:splice])
# 		finally:
# 			pass
		

# 	for days in schedule_list[(splice):]:
# 		schedule[days] = programms_by_day
# 		break

# Days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

# splice = Days[splice - 1]	



# specifiedtime = '1030-1100' #if possible, create input value asking for specified time period, possible creating dropdown list

# for day, time in schedule.items():
# 	for timeperiod in time:
# 		if specifiedtime in timeperiod:
# 			print(splice, specifiedtime, timeperiod[1])





