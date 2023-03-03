df_new = pd.get_dummies(df, columns=["col1"], prefix="Planet")
import pandas as pd
df = pd.DataFrame({«col1»: [«Sun», «Sun», «Moon», «Earth», «Moon», «Venus»]})
print(«The original data»)
print(df)
print(«*» * 30)
df_new = pd.get_dummies(df, columns=[«col1″], prefix=»Planet»)
print(«The transform data using get_dummies»)
print(df_new)