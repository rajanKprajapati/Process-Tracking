# Data Analyst Pandas Practice (40 Questions + Hints)

## Data Exploration

### 1. Top 10 countries with the most job postings

#### Solution: df["job_country"].value_counts().sort_values(ascending=False).head(10)

**Hint:**
- Count occurrences of `job_country`
- Sort descending
- Take first 10

---

### 2. Top 15 companies posting jobs

#### Solution:df["company_name"].value_counts().sort_values(ascending=False).head(15)

**Hint:**
- Focus on `company_name`
- Count frequency of each company
- Select top 15

---

### 3. Number of unique job titles and first 20 unique titles

#### Solution:
#### array=df["job_title_short"].unique()
#### length=len(array)
#### print(length)
#### array[:]

**Hint:**
- One function counts unique values
- Another function returns all unique values
- Slice first 20

---

### 4. Percentage of remote jobs

#### Solution:
#### (df["job_work_from_home"].value_counts().loc[True]*100)/(df.shape[0])

**Hint:**
- Use `job_work_from_home`
- Count `True`
- Divide by total rows

**Formula**

```python
(remote_jobs / total_jobs) * 100
```

---

### 5. Percentage of jobs offering health insurance

#### Solution:
#### (df["job_health_insurance"].value_counts().loc[True]*100)/(df.shape[0])

**Hint:**
- Column: `job_health_insurance`
- Count True values
- Convert to percentage

---

### 6. Percentage of jobs requiring no degree

#### Solution:
#### (df["job_no_degree_mention"].value_counts().loc[True]*100)/(df.shape[0])

**Hint:**
- Column: `job_no_degree_mention`
- Count True values

---

- [x]
### 7. Top 10 job locations 

**Hint:**
- Frequency count on `job_location`
- Sort descending

---

### 8. Unique companies posting remote jobs

#### solution: df=df[df['job_work_from_home']==False]
#### df["company_name"].value_counts()

**Hint:**
1. Filter remote jobs
2. Count unique companies

---

### 9. Schedule types and frequencies
- solution : df["job_schedule_type"].value_counts()
**Hint:**
- Use `job_schedule_type`
- Count every unique value

---

### 10. Top 20 job titles
- solution: df['job_title_short'].value_counts().sort_values(ascending=False).head(20)
**Hint:**
- Frequency count
- Highest counts first

---

# Missing Values

### 11. Columns with more than 50% missing values
- solution: df1=(df.isna().sum()/len(df))/100
- df1[df1>50]
**Hint:**

For each column:

```python
missing_percentage = (missing_count / total_rows) * 100\