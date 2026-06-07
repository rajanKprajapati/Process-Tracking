df = df.drop(5)                # Remove row with index 5
df = df.drop([2, 4, 6])        # Remove multiple rows
df = df.reset_index(drop=True) # Create fresh index
Today
.discribe()
.idxmin()
.iloc()
.unique()
.value_counts()
.min()
.median()
.max()
.groupby()
.agg()
df.groupby("job_title_short")[["salary_year_avg","salary_hour_avg"]].agg(["min","max","median","mean"])
df["job_title_short"].unique()
df.groupby("job_title_short")[["salary_year_avg","salary_hour_avg"]].min()


