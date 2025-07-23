import pandas as p

data = {'names':['ravi','soori','anu','rajesh','sravya','kavya'],
        'salary': [10000,150000,None,25000,500000,1500000],
        'department':['dev','test',None,'test','analyst','analyst']
        }

pd = p.DataFrame(data)
res = pd[['names','department']]

# print(pd)

res = pd.groupby('department').count()

res = pd['names']

res = pd.groupby('department').sum('salary')

res = pd['salary'].mean()

res = pd['salary'].describe()


#print(res)

# pd.dropna(inplace=True)

pd.fillna(method='bfill',inplace=True)

pd['bonus'] = pd['salary']*0.1

res = pd.head(2)

# print(res)

res = pd[pd['salary']>100000]

res = pd['names'].str.contains('a')

# print(pd)

# print(res)

# print(pd)


data = {'name':['siva','ravi','krishna','thilak','katraj'],
        'salary':[15000,10000,20000,180000,250000],
        'department':['dev','testing','dev','testing','management']}


pd = p.DataFrame(data)

res = pd[pd['name'].str.contains('a')]

res = pd.groupby('department').count()

res = pd.groupby('department').sum('salary')

# pd = pd[pd['salary']>15000]

res = pd.groupby('department')['salary'].sum()

res = pd.loc[3,'salary']

print(res)


# print(pd)


