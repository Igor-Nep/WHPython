import pandas as pd
import random
import numpy as np
#1
np.random.seed(42)
random.seed(42)

def generate_user_id(n=15):
  return ''.join([random.choice('1234567890abcdefghijk') for _ in range(n)])

def generate_user_id2(n=15):
  s = ''
  for i in range(n):
    s = s + random.choice('1234567890abcdefghijk')
  return s

generate_user_id2()


[random.choice('1234567890abcdefghijk') for _ in range(15)]

N = 10_000
n = 10_000

def generate_df(N):
  data = {
      'user_id': [generate_user_id() for _ in range(N)],
      'order_num': [random.randint(1, 10) for _ in range(N)],
      'click2delivery': np.random.normal(1440, 200, size=N),
      'order_items_sum': np.random.exponential(1, size=N) + 1,
      'retention': np.random.choice([1, 2, 3, 4, 5], size=N, p=[0.35, 0.25, 0.2, 0.15, 0.05])
  }
  return pd.DataFrame(data)

df = pd.DataFrame()

while True:
  new_df = generate_df(n)
  df = pd.concat([df, new_df], ignore_index=True)
  df = df.drop_duplicates(subset='user_id', keep='first')
  n = N - len(df)

  if n <= 0:
    break
  
print(df)  
len(df['user_id'].unique())
    
#2
orders = (
    df
    .groupby('order_num')['click2delivery']
    .agg(mean_time='mean')
    .reset_index()
)

print(orders)

df = df.merge(
    orders,
    how='inner',
    left_on='order_num',
    right_on='order_num'
)

print(df)

#3

arr = [0, 1]

for i in range(10):
  arr.append(sum(arr[-2:]))

arr

arr = [0, 1]

for i in range(9998):
  arr.append(sum(arr[-2:]) * 0.5)

len(arr)

arr[:10]

df['seq'] = arr

print(df.head())

arr = [1, 2, 3, 4, 5]

sum(arr[-2:])

#4
df['user_id'][0]

# ibcjj13372820746208203536
# 3656886756 ** 2

list(filter(str.isalpha, 'ibcjj13372820746208203536'))

def process_user_id(user_id):
  letters = ''.join(filter(str.isalpha, user_id))
  digits = ''.join(filter(str.isdigit, user_id))

  return f'{letters}{int(digits) ** 2}'

process_user_id('i36b56c88j675j6')

df['transformed_user_id'] = df['user_id'].apply(process_user_id)
df.head()

df2 = df[['click2delivery', 'order_items_sum', 'retention']]

df2

df2.describe()

#5

df2 = df[['click2delivery', 'order_items_sum', 'retention']]

df2

df_rounded = df2.copy()

df_rounded[['click2delivery', 'order_items_sum']] = df_rounded[['click2delivery', 'order_items_sum']].astype(int)

df_rounded

modes = (
    df_rounded
    .mode()
    .head(1)
    .set_index(pd.Index(['mode']))
)

modes

described_df = (
    df2
    .describe()
    .loc[['mean', 'std', '50%'], :]
)

print(described_df)

described_df = pd.concat([described_df, modes])

described_df

import seaborn as sns

sns.pairplot(df[['click2delivery', 'order_items_sum', 'retention']], corner=True);
import matplotlib.pyplot as plt
plt.show()