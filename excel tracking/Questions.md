# Excel Lookup Practice Set (15 Questions)

For your dataset, 15 carefully chosen questions are enough to master the lookup topics.

---

# Easy Level

## Q1

A user enters a **Company Name**.

Return the corresponding **Job Title**.

### Hint

**Search column:**

```text
company_name
```

**Return column:**

```text
job_title
```

**Use:**

```text
XLOOKUP
```

---

## Q2

A user enters:

```text
Data Analyst
```

Return:

```text
job_country
```

### Hint

**Search:**

```text
job_title_short
```

**Use:**

```text
VLOOKUP or XLOOKUP
```

---

## Q3

Find the posting source of a job.

**Input:**

```text
Data Engineer
```

**Output:**

```text
job_via
```

### Hint

**Use:**

```text
INDEX + MATCH
```

---

## Q4

Find whether a job is remote.

**Input:**

```text
Data Scientist
```

**Output:**

```text
job_work_from_home
```

### Hint

**Use:**

```text
XLOOKUP
```

---

## Q5

If a company is not found, show:

```text
Company Not Found
```

instead of:

```text
#N/A
```

### Hint

**Use:**

```text
IFERROR
```

---

# Medium Level

## Q6

Find the average yearly salary of:

```text
Senior Data Engineer
```

### Hint

**Return:**

```text
salary_year_avg
```

**Use:**

```text
XLOOKUP
```

---

## Q7

Find the required skills of:

```text
Data Analyst
```

### Hint

**Return:**

```text
job_skills
```

**Use:**

```text
INDEX + MATCH
```

---

## Q8

Find the company that posted:

```text
Senior Data Engineer
```

### Hint

Reverse Lookup.

**Use:**

```text
INDEX + MATCH
```

---

## Q9

Find the schedule type of:

```text
Data Engineer
```

### Hint

**Return:**

```text
job_schedule_type
```

---

## Q10

A dropdown contains:

```text
job_country
job_location
salary_year_avg
```

The user selects one option.

Return the selected information for a chosen company.

### Hint

Dynamic Lookup

**Use:**

```text
INDEX + MATCH + MATCH
```

---

# Hard Level

## Q11

Find salary where:

```text
job_title_short = Data Analyst

job_country = India
```

### Hint

Multiple Criteria Lookup

---

## Q12

Find company where:

```text
job_title_short = Data Engineer

job_country = Germany
```

### Hint

Combine two columns.

---

## Q13

Find skills where:

```text
job_title_short = Data Analyst

job_country = Mexico
```

### Hint

Multiple Criteria INDEX + MATCH

---

## Q14

First find the company of:

```text
Data Analyst
```

Then find the country of that company.

### Hint

Nested Lookup

---

## Q15

Create a mini dashboard.

The user enters:

```text
Company Name
```

Automatically return:

- Job Title
- Country
- Location
- Salary
- Posted Date

### Hint

Use:

```text
5 XLOOKUP formulas
```

or

```text
INDEX + MATCH
```

---

# My Recommendation

For Excel lookup mastery, stop after these 15 questions if you can solve them without looking at notes.

Then move to:

1. Pivot Tables
2. Power Query
3. Conditional Formatting
4. Excel Dashboards
5. Advanced Formulas

These topics will give you much more value for Data Analyst roles than solving another 35 lookup questions.