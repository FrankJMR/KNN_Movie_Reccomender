
from csv import reader

#data set from kaggle
fileName = "imdb.csv"

movieSet = list()
#function to load data
def loadData(fileName):
    

    with open(fileName,'r', encoding='utf-8') as file:
        csv_reader = reader(file)
        """empty rows continue the loop
           appending only the rows that 
           have data to my list movieSet
        """
        for rows in csv_reader:
            if not rows:
                continue
            movieSet.append(rows)
        return movieSet


movieSet = loadData(fileName)
print('Loaded data set {} with {} rows and {} columns'.format(fileName, len(movieSet), len(movieSet[0])))

for i in range(1):
    print(movieSet[i],"\n")
    print(movieSet[i+1])