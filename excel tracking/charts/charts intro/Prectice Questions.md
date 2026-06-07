# Industry-Level Chart Analysis Assignment

## Analysis Framework

For every question, use:

**Question → Data Type → Best Chart → Why → Insights → Business Decision**

---

# Level 1: Chart Selection (Easy-Medium)

## 1. Most In-Demand Job Roles

### Using
- `job_title_short`

### Question
Which 10 job roles appear most frequently in the dataset?

### Tasks
1. Identify the data type.
2. Choose the best chart.
3. Create the chart.
4. Explain why the top role may be in high demand.

---

## 2. Jobs by Country

### Using
- `job_country`

### Question
Which countries have the highest number of job postings?

### Tasks
1. Create an appropriate chart.
2. Rank the top 10 countries.
3. Identify hiring hotspots.

---

## 3. Remote vs Non-Remote Jobs

### Using
- `job_work_from_home`

### Question
What percentage of jobs are remote?

### Tasks
1. Calculate percentages.
2. Select the most suitable chart.
3. Explain what this says about industry trends.

---

## 4. Degree Requirement Analysis

### Using
- `job_no_degree_mention`

### Question
How many jobs do not mention a degree requirement?

### Tasks
1. Compare degree vs non-degree jobs.
2. Select a chart.
3. Suggest implications for students.

---

# Level 2: Line Chart Challenges (Medium)

## 5. Monthly Job Posting Trend

### Using
- `job_posted_date`

### Question
How does the number of job postings change month by month?

### Tasks
1. Extract month from date.
2. Create a Line Chart.
3. Identify growth and decline periods.
4. Explain possible reasons.

---

## 6. Hiring Season Detection

### Using
- `job_posted_date`

### Question
Which month has the highest hiring activity?

### Tasks
1. Create a monthly trend chart.
2. Detect hiring peaks.
3. Recommend best months for job seekers.

---

## 7. Remote Job Trend Over Time

### Using
- `job_posted_date`
- `job_work_from_home`

### Question
Has remote hiring increased or decreased over time?

### Tasks
1. Aggregate remote jobs by month.
2. Create a Line Chart.
3. Explain the trend.

---

# Level 3: Salary Analysis (Medium-Hard)

## 8. Highest Paying Job Titles

### Using
- `job_title_short`
- `salary_year_avg`

### Question
Which job titles have the highest average salaries?

### Tasks
1. Group salaries by job title.
2. Find average salary.
3. Visualize results.
4. Explain why some roles pay more.

---

## 9. Salary Distribution by Country

### Using
- `job_country`
- `salary_year_avg`

### Question
Which countries offer the highest average salaries?

### Tasks
1. Calculate country averages.
2. Compare countries visually.
3. Identify global salary leaders.

---

## 10. Hourly vs Annual Salary

### Using
- `salary_hour_avg`
- `salary_year_avg`

### Question
Compare jobs with hourly pay versus annual pay.

### Tasks
1. Create suitable visualizations.
2. Explain differences.
3. Discuss which salary metric is more useful.

---

# Level 4: Business Intelligence Questions (Hard)

## 11. Health Insurance Availability

### Using
- `job_health_insurance`

### Question
What percentage of jobs provide health insurance?

### Tasks
1. Calculate shares.
2. Visualize results.
3. Explain implications for job seekers.

---

## 12. Job Schedule Analysis

### Using
- `job_schedule_type`

### Question
Which schedule type is most common?

### Examples
- Full-time
- Part-time
- Contract

### Tasks
1. Rank schedule types.
2. Create an appropriate chart.
3. Explain labor market trends.

---

## 13. Top Hiring Companies

### Using
- `company_name`

### Question
Which companies post the most jobs?

### Tasks
1. Find top 15 companies.
2. Visualize rankings.
3. Discuss recruitment strategies.

---

# Level 5: Advanced Industry Questions (Very Hard)

## 14. Salary vs Remote Work

### Using
- `job_work_from_home`
- `salary_year_avg`

### Question
Do remote jobs pay more than non-remote jobs?

### Tasks
1. Compare average salaries.
2. Choose an appropriate chart.
3. Explain findings.
4. Provide hiring recommendations.

---

## 15. Skill Demand Analysis

### Using
- `job_skills`

### Question
Which skills appear most frequently in job postings?

### Tasks
1. Extract skills.
2. Count occurrences.
3. Create a ranked chart.
4. Recommend skills students should learn.

---

# Executive-Level Challenge (Industry Project)

## 16. Build a Hiring Dashboard

### Using
- `job_title_short`
- `job_country`
- `salary_year_avg`
- `job_work_from_home`
- `job_health_insurance`
- `job_posted_date`
- `company_name`

### Create a dashboard answering:

1. Which jobs are most in demand?
2. Which countries hire the most?
3. Which jobs pay the most?
4. Are remote jobs growing?
5. Which companies hire the most?
6. What benefits are most common?

### For every chart explain:

- Data Type
- Chart Chosen
- Why Chosen
- Insights
- Business Decision