import pandas as pd
df=pd.DataFrame({
    "Class":["A","A","B","B"],
    "Marks":[80,90,70,60]
})
print(df)
# df.groupby("job_title_short").min()
mean,median,min,max=df.groupby("Class").mean(),df.groupby("Class").median(),df.groupby("Class").min(),df.groupby("Class").max()
print(max)
print(min)
print(median)
print(mean)

