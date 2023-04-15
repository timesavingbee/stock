import FinanceDataReader as fdr #재무 정보 다운로드
import pandas as pd
code_a='086520' #에코프로
df_a=fdr.DataReader(code_a)
df_a.plot()
