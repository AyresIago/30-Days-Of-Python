import os
from statistics import mean, median, mode, stdev # importing all the statistics modules

#creating a directory
os.mkdir('directory_name')

#changing the current directory
os.chdir('path')

#getting current working directory
os.getcwd()

#removing directory
os.rmdir


ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3
