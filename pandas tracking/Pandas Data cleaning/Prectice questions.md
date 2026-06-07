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

# IPL Dataset Practice Questions

## Missing Values Analysis

### 13. Cities with the Most Missing Match Information

**Hint:**
1. Choose a column that may have missing values (e.g., `city`)
2. Filter missing values
3. Count occurrences

---

### 14. Venues Having at Least One Match Recorded

**Hint:**
1. Remove missing venues
2. Count unique venues

---

### 15. Percentage Missing for Every Column

**Hint:**

```python
(df.isna().sum() / len(df)) * 100
```

---

### 16. Matches with Missing Player of Match

**Hint:**

```python
df['player_of_match'].isna()
```

---

### 17. Matches Where Match Referee Information Is Available

**Hint:**

```python
df['match_referee'].notna()
```

---

### 18. Venues Where More Than 50% of Player of Match Entries Are Missing

**Hint:**
1. Group by venue
2. Calculate missing percentage
3. Filter > 50%

---

# Filtering

### 19. Matches Won by Chennai Super Kings (CSK)

**Hint:**

```python
df['winner'] == 'Chennai Super Kings'
```

---

### 20. Matches Where Mumbai Indians Won After Losing the Toss

**Hint:**
Conditions:

- winner = Mumbai Indians
- toss_winner ≠ Mumbai Indians

Combine using `&`

---

### 21. Matches Played in Mumbai, Delhi, and Bengaluru

**Hint:**

```python
df['city'].isin(['Mumbai', 'Delhi', 'Bengaluru'])
```

---

### 22. Matches Played at Top 5 Most Frequently Used Venues

**Hint:**

Step 1:

```python
top_5_venues = df['venue'].value_counts().head(5)
```

Step 2:

```python
df['venue'].isin(top_5_venues.index)
```

---

### 23. Matches Won by More Than 50 Runs

**Hint:**

```python
df['win_by_runs'] > 50
```

---

### 24. Matches Not Played in Mumbai

**Hint:**

```python
df['city'] != 'Mumbai'
```

---

### 25. Matches Having Total Runs Greater Than Average

**Hint:**

Create:

```python
df['total_runs'] = df['team1_runs'] + df['team2_runs']
```

Calculate average total runs and filter above average matches.

---

### 26. Top 20 Highest Scoring Matches

**Hint:**
1. Create `total_runs`
2. Sort descending
3. Take first 20

---

# Sorting

### 27. Top 15 Venues with Highest Average Match Runs

**Hint:**
1. Create `total_runs`
2. Group by venue
3. Calculate mean
4. Sort descending

---

### 28. 20 Most Recent Matches

**Hint:**
1. Convert date column to datetime
2. Sort descending

---

### 29. Top 10 Cities with Highest Average Match Runs

**Hint:**
1. Group by city
2. Average total runs
3. Sort descending

---

### 30. Top 25 Closest Matches (Won by Fewest Runs)

**Hint:**

```python
sort_values('win_by_runs')
```

Take first 25.

---

# GroupBy

### 31. Average Runs Scored by Each Winning Team

**Hint:**

Group by:

```python
winner
```

Calculate average runs scored.

---

### 32. Average Total Runs by City

**Hint:**

Group by:

```python
city
```

Calculate mean total runs.

---

### 33. Average Runs Based on Toss Decision

**Hint:**

Group by:

```python
toss_decision
```

Calculate average total runs.

---

### 34. Number of Matches Won by Each Team

**Hint:**
1. Group by winner
2. Count rows

---

### 35. Average Total Runs by City and Toss Decision

**Hint:**

```python
groupby(['city', 'toss_decision'])
```

---

# agg()

### 36. City Match Statistics

Find:

- Mean Runs
- Maximum Runs
- Minimum Runs
- Match Count

**Hint:**
Use a single `agg()` call.

---

### 37. Team Winning Statistics

Find:

- Mean Runs
- Median Runs
- Maximum Runs

**Hint:**
Group by winner and use aggregation list.

---

### 38. Venue Statistics

Find:

- Match Count
- Average Total Runs
- Highest Total Runs

**Hint:**
Use multiple aggregations.

---

# Real IPL Analyst Questions

### 39. Venue Performance Report

Create:

| Venue | Matches Played | Avg Total Runs |
|--------|---------------|----------------|
| ... | ... | ... |

Sorted by Avg Total Runs descending.

**Hint:**

```python
groupby()
agg()
sort_values()
```

---

### 40. IPL Executive Summary

Create a report containing:

- Total Matches
- Total Cities
- Total Venues
- Total Teams
- Average Match Runs
- Highest Scoring City
- Highest Scoring Venue
- Most Successful Team
- Most Common Toss Decision
- Most Frequent Player of the Match

**Hint:**

```python
shape
nunique
groupby
value_counts
mean
sort_values
```

---

# Advanced Analyst-Level Questions

### 41. Does Winning the Toss Increase the Chance of Winning the Match?

**Objective:**
Compare toss winners and match winners to calculate win percentage.

---

### 42. Which Venues Favor Batting First?

**Objective:**
Analyze venue-wise outcomes based on toss decisions and match winners.

---

### 43. Which Team Performs Best in High-Scoring Matches (350+ Total Runs)?

**Objective:**
Filter high-scoring matches and analyze winning teams.

---

### 44. Which Player Has Won the Most Player of the Match Awards?

**Objective:**
Rank players by number of awards.

---

### 45. Which Umpire Has Officiated the Most Matches?

**Objective:**
Analyze umpire participation frequency.

---

### 46. Which Team Has the Highest Average Winning Margin?

**Objective:**
Compare teams using run and wicket victory margins.

---

### 47. Home Advantage Analysis

**Objective:**
Determine whether teams perform better in specific cities.

---

### 48. Toss Decision Trend by Season

**Objective:**
Analyze how batting-first and fielding-first decisions changed over seasons.

---

# Difficulty Breakdown

| Questions | Difficulty |
|------------|------------|
| 13–18 | Easy-Medium |
| 19–30 | Medium |
| 31–38 | Medium-Hard |
| 39–40 | Analyst Level |
| 41–48 | Industry-Level Analyst |