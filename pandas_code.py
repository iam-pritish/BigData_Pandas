# Pandas-101
# Installation
!pip install pandas
import pandas as pd
df = pd.read_csv("https://gist.githubusercontent.com/iam-pritish/6aed789bba0431f0b933aac718624a37/raw/6907bb3a38bfbb6fccf3a8b1edfb90e39714d14f/titanic_dataset.csv")
df
df.set_index('PassengerId')
df
df.loc[100]
df.iloc[100]
df.set_index('PassengerId' , inplace=True)
df
df.loc[100]
df.iloc[100]
df.iloc[99]

df.reset_index('PassengerId', inplace=True)
df
df.iloc[100]
df.loc[100]
# Add Column
df['new_col'] = df['Survived'] + df['Pclass']
df
# Delete Column
df.drop('new_col', axis=1)
df

# Still 'new_col' Exsist
# now we have to inplace the boolean value to modify in same DataFrame

df.drop('new_col', axis = 1, inplace=True )
df

# GroupBy

data1 = {'Name':['Abhishekh', 'Bhuvi', 'Churchil', 'Dipak','Prashik','Rohan', 'Sameer', 'Tushar','Bhuvi'],
         'Age':[23, 22, 25, 31, 30, 28, 27, 26,52],
         'Address':['Nagpur','Kanpur','Pune','Hyderabad','Bangalore','Delhi','Mohali','Kolkata', 'Mumbai'],
         'Qualification':['MBA','MCA','MBBS','BA','BCA','BE','M-Pharma','MA', 'Phd',]
         }
type(data1)
df_new= pd.DataFrame(data1)
df_new

# GroupBy using 'NAME'

df_new.groupby('Name')
print(df_new.groupby('Name').groups)

# Here as you can see, Group-by Name column showcasing 'Index' and 'Name' of individuals.
# "Bhuvi" appears in two 'Indices'.
# Make group-key 

gk = df_new.groupby('Name')
gk
print(gk)
print(list(gk))
list(gk)

# Can Iterate over it
for i in gk:
    print(i)
# now observe the upper Table with is in Tuple
# we created It by groupby 'Name'- like 'Abhishekh','Bhuvi','Tushar'...etc


# GroupBy using Multiple Keys

data2 = {'Name':['Jai','Anuj','Jai','Prince','Gaurav','Anuj','Prince','Abhi','Gaurav'],
         'Age':[27,24,22,32,33,36,27,32,22],
         'Address':['Nagpur','Kanpur','Allahabad','Pune','Jaipur','Kanpur','Allahabad','Aligarh','Mumbai'],
         'Qualification':['M.sc','MA','MCA','Phd','B-Tech','B.com','M.sc','MA','B-Tech']
         }
df = pd.DataFrame(data2)
df
df.groupby(['Name' , 'Qualification'])
print(df.groupby(['Name' ,  'Qualification']).groups)

# Here You Can See that : Gavrav Has same Qualification and Name so it's Group together ('Gaurav', 'B-Tech'): [4, 8] ; dispit being Different Address and Age.

df.groupby(['Address']).sum(["Age"])

# Here you can see that the repeting Members Having their 'Age' got SUM and sum() arragument is only work with integer values


# Merging Two Data-Frames 
data1 = {'Name':['Abhishekh', 'Bhuvi', 'Churchil', 'Dipak','Prashik','Rohan', 'Sameer', 'Tushar','Bhuvi'],
         'Age':[23, 22, 25, 31, 30, 28, 27, 26,52],
         'Address':['Nagpur','Kanpur','Pune','Hyderabad','Bangalore','Delhi','Mohali','Kolkata', 'Mumbai'],
         'Qualification':['MBA','MCA','MBBS','BA','BCA','BE','M-Pharma','MA', 'Phd',]
         }

data2 = {'Name':['Jai','Anuj','Jai','Prince','Gaurav','Anuj','Prince','Abhi','Gaurav'],
         'Age':[27,24,22,32,33,36,27,32,22],
         'Address':['Nagpur','Kanpur','Allahabad','Pune','Jaipur','Kanpur','Allahabad','Aligarh','Mumbai'],
         'Qualification':['M.sc','MA','MCA','Phd','B-Tech','B.com','M.sc','MA','B-Tech']
         }

# Convert Directory Into DataFrame of data1:-

df1 = pd.DataFrame(data1, index = [0,1,2,3,4,5,6,7,8])

# Convert Directory Into DataFrame of data2 :-

df2 = pd.DataFrame(data2 , index = [9,10,11,12,13,14,15,16,17])

df1
df2
# Now If you want to Add both of the lists together then Use CONCAT Method
frames = [ df1 , df2 ]

result = pd.concat(frames)
result
