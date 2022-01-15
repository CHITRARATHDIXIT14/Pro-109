import statistics
import pandas as pd
import csv

df = pd.read_csv('StudentsPerformance.csv')
maths_score = df['math score']

mean = statistics.mean(maths_score)
mode = statistics.mode(maths_score)
median = statistics.median(maths_score)
std_dev = statistics.stdev(maths_score)

print("The maths score mean is :-",mean)
print("The maths score mode is :-",mode)
print("The maths score median is :-",median)
print("The maths score standard deviation is :-",std_dev)

std_dev1_start,std_dev1_end = mean-std_dev , mean+std_dev
std_dev2_start,std_dev2_end = mean-(2*std_dev) , mean+(2*std_dev)
std_dev3_start,std_dev3_end = mean-(3*std_dev) , mean+(3*std_dev)
listOfDataWithInFirstStandardDeviation = [result for result in maths_score if result > std_dev1_start and result < std_dev1_end ]
listOfDataWithInSecondStandardDeviation = [result for result in maths_score if result > std_dev2_start and result < std_dev2_end ]
listOfDataWithInThirdStandardDeviation = [result for result in maths_score if result > std_dev3_start and result < std_dev3_end ]

print(len(listOfDataWithInFirstStandardDeviation)*100.0/len(maths_score),"% Percentage of data lies between 1st standard deviation" )
print(len(listOfDataWithInSecondStandardDeviation)*100.0/len(maths_score),"% Percentage of data lies between 2nd standard deviation")
print("Percentage of data lies between 3rd standard deviation" , len(listOfDataWithInThirdStandardDeviation)*100.0/len(maths_score))


