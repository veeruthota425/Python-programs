import pandas as pd
data = pd.Series([10, 20, 30, 40, 50])
print("Pandas Series:")
print(data)
py_list=data.tolist()
print(py_list)
print("\nType of the converted object:", type(py_list))