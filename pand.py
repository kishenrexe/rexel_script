import pandas as pd

df = pd.read_excel('EC011141.xlsx')


test =df.sort_values(['code','waarde'], ascending = [False,True])


print(test)