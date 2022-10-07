# Q1. Load your dataset into python using the pandas library and save data into a dataframe named dfi (where i is one of your datasets, for a total of 4).
import pandas as pd
dfi=pd.read_table("https://raw.githubusercontent.com/data602sps/datasetspractice/main/salarydata.csv")
df2=pd.read_table("https://raw.githubusercontent.com/data602sps/datasetspractice/main/salarydata.csv")
df3=pd.read_table("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv")
df4=pd.read_table("https://raw.githubusercontent.com/emorisse/FBI-Hate-Crime-Statistics/master/2013/table13.csv")

# Q2. Preview your data by calling your dataframe’s name. How many columns and rows
# do you see?
#There are fifty one rows and three columns
print(dfi)

# Q3. Examine the shape of your data using the .shape command and the data types of
# your columns using .dtypes.
#returns the dimensions of the table
print(df2.shape)

# Q4. Use .describe() on your data. What do you notice about your data? What does this
# command return?

#prints the stats like column names, unique values, frequent items in the data, the first row
print(df3.describe())



# Q5. Use the .head() and .tail() command - what does this do?

#Head() prints the firt 5 rows data frame
print(df4.head())

#.tails() prints the last 5 rows of the data frame
print(df4.tail())



# 1. Choose one of your datasets and remove the header information. (Can delete the row in excel, etc..)

#we are going to ignore the headers assumption and reassign with .columns
df5=pd.read_table("https://raw.githubusercontent.com/tategallery/collection/master/artist_data.csv",header=None)

# 2. Import the data into your environment using pandas. Display the .head() of your data showing no header information.
print(df5.head())


# 3. Using pandas, update the dataset to include the header information. Display the
# updated data using .head().

df5.columns=df5.iloc[0]
df5=df5.drop(0)
print(df5.head())


