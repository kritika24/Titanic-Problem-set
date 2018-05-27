# Import the Pandas library
import pandas as pd
# Load the train and test datasets to create two DataFrames
train_url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv"
train = pd.read_csv(train_url)

test_url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/test.csv"
test = pd.read_csv(train_url)
#Print the `head` of the train and test dataframes
print(train.head())
print(test.head())

# Passengers that survived vs passengers that passed away
print(train["Survived"].value_counts())

# As proportions
print(train["Survived"].value_counts(normalize =True))

# Males that survived vs males that passed away
print(train["Survived"][train["Sex"] == 'male'].value_counts())

# Females that survived vs Females that passed away
print(train["Survived"][train["Sex"] == 'female'].value_counts())

# Normalized male survival
print(train["Survived"][train["Sex"] == 'male'].value_counts(normalize =True))

# Normalized female survival
print(train["Survived"][train["Sex"] == 'female'].value_counts(normalize =True))

print("--------------training set--------------")
print(train.describe())
print("--------------training shape--------------")
print(train.shape)
print("--------------testing set--------------")
print(test.describe())
print("--------------testing shape--------------")
print(test.shape)

#checking for children -> if the passenger is a child then that child has more chances of getting saved.
import sys
# Create the column Child and assign to 'NaN'
train["Child"] = float('NaN')

# Assign 1 to passengers under 18, 0 to those 18 or older. Print the new column
train["Child"][train["Age"]<18.0]=1
train["Child"][train["Age"]>=18.0]=0
print(train["Child"])

# Print normalized Survival Rates for passengers under 18
print(train["Survived"][train["Child"] == 1].value_counts(normalize = True))

# Print normalized Survival Rates for passengers 18 or older
print(train["Survived"][train["Child"] == 0].value_counts(normalize = True))

# Create a copy of test: test_one
test_one=test
print(test_one)

# Initialize a Survived column to 0
test_one["Survived"]=0

# Set Survived to 1 if Sex equals "female" and print the `Survived` column from `test_one`
test_one["Survived"][test_one["Sex"]=="female"]=1
print(test_one["Survived"])

