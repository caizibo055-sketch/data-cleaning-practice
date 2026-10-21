import pandas as pd

# 我的第一个数据清洗脚本
data = {
    "name": ["robot_arm", "robot_leg", None],
    "score": [95, None, 60]
}

df = pd.DataFrame(data)
print("原始数据：")
print(df)

# 删掉有空值的行
df_clean = df.dropna()
print("\n清洗后的数据：")
print(df_clean)