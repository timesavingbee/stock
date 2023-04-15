#import FinanceDataReader as fdr #재무 정보 다운로드
import pandas as pd
import streamlit as st
# code_a='086520' #에코프로
# df_a=fdr.DataReader(code_a)
# df_a.plot()

st.write('test')
pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})

import pandas as pd
df = pd.DataFrame({'col1': [1,2,3]})
df  # 👈 Draw the dataframe

x = 10
'x', x  # 👈 Draw the string 'x' and then the value of x

# Also works with most supported chart types
import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

fig  # 👈 Draw a Matplotlib chart

import FinanceDataReader as fdr #재무 정보 다운로드
import pandas as pd
code_a='086520' #에코프로
df_a=fdr.DataReader(code_a)
df_a.plot()
