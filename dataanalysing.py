import pandas as p

'''
data = {
        'name':['siva','raju','anu','karthik','sravya'],
        'salary':[150000,20000,25000,50000,350000],
        'dept':['dev','test','management','dev','test'],
    }

'''


#df = p.DataFrame(data)


#data = df[df['salary']>20000]

#print(data)


#df['maxsal'] = df['salary'].apply(lambda x: 'max' if x == df['salary'].max() else '')

#df.loc[df['salary'].max() == df['salary'],'max'] = 'max'


#df.loc[df['salary'] == df['salary'].max(),'max'] = 'max'

#df['max'] = df['salary'].apply(lambda x: 'max' if x == df['salary'].max() else '')




'''
data = {
    'calories':[420,450,234],
    'duration':[50,20,60]
    }

df = p.DataFrame(data,index = ['day1','day2','day3'])

res = df.loc['day1']

#print(res)

print(df)


'''




#df = p.read_csv("D:\Vcube\data.csv")
#print(df)
#print(df.to_string())


      



data = {
        'name':['siva','anu','karthik','ram'],
        'salary':[10000,200000,300000,40000]
    }


df = p.DataFrame(data)


df['maxsal'] = df['salary'].apply(lambda x: 'max' if x == df['salary'].max() else '')


print(df)
























