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
missing_percentage = (missing_count / total_rows) * 100
```

Filter percentages above 50.

---

### 12. Jobs containing salary information
- solution: df['salary_year_avg'].isna().sum()
**Hint:**
- Use `salary_year_avg`
- Count rows that are NOT missing

---

### 13. Countries with most missing salaries
- solution: 
**Hint:**
1. Filter missing salaries
2. Group by country
3. Count rows

---

### 14. Companies having at least one salary available

**Hint:**
1. Remove missing salaries
2. Count unique companies

---

### 15. Percentage missing for every column

**Hint:**

```python
(isna().sum() / len(df)) * 100
```

---

### 16. Remote jobs with missing salary

**Hint:**
- Remote
- Salary missing

Combine using AND (`&`)

---

### 17. Jobs where skills are available

**Hint:**

```python
job_skills.notna()
```

---

### 18. Countries where over 50% salaries are missing

**Hint:**
1. Group by country
2. Calculate missing percentage per country
3. Filter > 50%

---

# Filtering

### 19. Remote Data Analyst jobs

**Hint:**
- `job_title_short`
- `job_work_from_home`

---

### 20. Remote Data Scientist jobs with salary available

**Hint:**
- Data Scientist
- Remote
- Salary exists

---

### 21. Jobs from USA, Germany, Canada

**Hint:**

```python
isin([...])
```

---

### 22. Jobs posted by top 5 companies

**Hint:**

Step 1:
- Find top 5 companies

Step 2:
- Use `isin()`

---

### 23. Jobs with health insurance and no degree requirement

**Hint:**
- Use AND (`&`)

---

### 24. Data Engineer jobs outside USA

**Hint:**
- Use NOT (`!=`)

---

### 25. Jobs with salary above average

**Hint:**

First calculate:

```python
avg_salary
```

Then filter:

```python
salary > avg_salary
```

---

### 26. Top 20 highest-paying remote jobs

**Hint:**
1. Filter remote jobs
2. Sort salary descending
3. Take first 20

---

# Sorting

### 27. Top 15 highest-paying companies

**Hint:**
1. Group by company
2. Calculate mean salary
3. Sort descending

---

### 28. 20 newest jobs with salary

**Hint:**
1. Remove missing salaries
2. Sort by date descending

---

### 29. Top 10 highest-paying countries

**Hint:**
1. Group by country
2. Calculate average salary
3. Sort descending

---

### 30. Top 25 highest-paying remote jobs

**Hint:**
1. Filter remote jobs
2. Sort salary descending
3. Take first 25

---

# GroupBy

### 31. Average salary for each job title

**Hint:**

Group by:

```python
job_title_short
```

Calculate mean salary.

---

### 32. Average salary by country

**Hint:**

Group by:

```python
job_country
```

Calculate mean.

---

### 33. Average salary by remote status

**Hint:**

Group by:

```python
job_work_from_home
```

Calculate mean.

---

### 34. Number of jobs by company

**Hint:**
1. Group by company
2. Count rows

---

### 35. Average salary by country and remote status

**Hint:**

```python
groupby(['job_country', 'job_work_from_home'])
```

---

# agg()

### 36. Country salary statistics

Find:
- Mean
- Max
- Min
- Count

**Hint:**
- Use a single `agg()` call

---

### 37. Job title salary statistics

Find:
- Mean
- Median
- Max

**Hint:**
- Group by title
- Use aggregation list

---

### 38. Company statistics

Find:
- Job count
- Average salary
- Highest salary

**Hint:**
- Mix count and salary aggregations

---

# Real Analyst Questions

### 39. Country Salary Report

Create:

| Country | Jobs Posted | Avg Salary |
|----------|------------|------------|

Sorted by Avg Salary descending.

**Hint:**

```python
groupby()
agg()
sort_values()
```

---

### 40. Executive Summary

Create a report containing:

- Total jobs
- Total companies
- Total countries
- Remote %
- Average salary
- Highest paying country
- Highest paying job title
- Company posting most jobs

**Hint:**

```python
shape
nunique
groupby
mean
value_counts
sort_values
```

---

# Challenge Level

| Questions | Difficulty |
|------------|------------|
| 1–10 | Easy |
| 11–18 | Easy-Medium |
| 19–30 | Medium |
| 31–38 | Medium-Hard |
| 39–40 | Analyst Level |