# Pandas Filtering Techniques

## 1. Basic Boolean Filtering

Suppose:

```python
df.head()
```

| job_title_short | salary_year_avg |
|-----------------|----------------|
| Data Analyst | 70000 |
| Data Scientist | 120000 |
| Data Analyst | 90000 |

### Equal To (`==`)

```python
df[df['job_title_short'] == 'Data Analyst']
```

Returns only Data Analyst jobs.

### Not Equal To (`!=`)

```python
df[df['job_title_short'] != 'Data Analyst']
```

Returns everything except Data Analyst jobs.

---

## 2. Numeric Filtering

### Greater Than (`>`)

```python
df[df['salary_year_avg'] > 100000]
```

### Less Than (`<`)

```python
df[df['salary_year_avg'] < 50000]
```

### Greater Than or Equal (`>=`)

```python
df[df['salary_year_avg'] >= 100000]
```

### Less Than or Equal (`<=`)

```python
df[df['salary_year_avg'] <= 100000]
```

---

## 3. Multiple Conditions

### AND (`&`)

Both conditions must be true.

```python
df[
    (df['job_title_short'] == 'Data Analyst')
    &
    (df['salary_year_avg'] > 100000)
]
```

> **Important:** Use parentheses around each condition.

### OR (`|`)

At least one condition must be true.

```python
df[
    (df['job_title_short'] == 'Data Analyst')
    |
    (df['job_title_short'] == 'Data Scientist')
]
```

### NOT (`~`)

Reverse the condition.

```python
df[
    ~(df['job_title_short'] == 'Data Analyst')
]
```

---

## 4. `isin()`

Used when checking multiple values.

Instead of:

```python
df[
    (df['job_country'] == 'India')
    |
    (df['job_country'] == 'Germany')
    |
    (df['job_country'] == 'Canada')
]
```

Use:

```python
df[
    df['job_country'].isin(
        ['India', 'Germany', 'Canada']
    )
]
```

Much cleaner.

---

## 5. Missing Values Filtering

### `isna()`

Find missing values.

```python
df[df['salary_year_avg'].isna()]
```

### `notna()`

Find non-missing values.

```python
df[df['salary_year_avg'].notna()]
```

---

## 6. String Filtering

### Exact Match

```python
df[df['company_name'] == 'Google']
```

### `str.contains()`

Find text inside strings.

```python
df[
    df['job_title'].str.contains(
        'Engineer',
        na=False
    )
]
```

Returns all job titles containing `"Engineer"`.

### Case Insensitive Search

```python
df[
    df['job_title'].str.contains(
        'engineer',
        case=False,
        na=False
    )
]
```

### Starts With

```python
df[
    df['job_title'].str.startswith(
        'Senior',
        na=False
    )
]
```

### Ends With

```python
df[
    df['job_title'].str.endswith(
        'Engineer',
        na=False
    )
]
```

---

## 7. Range Filtering

### Between Values

Instead of:

```python
df[
    (df['salary_year_avg'] >= 50000)
    &
    (df['salary_year_avg'] <= 100000)
]
```

Use:

```python
df[
    df['salary_year_avg'].between(
        50000,
        100000
    )
]
```

---

## 8. Index-Based Filtering

### Using `loc`

```python
df.loc[100:200]
```

Rows 100 to 200.

### Using `iloc`

```python
df.iloc[100:200]
```

Rows by position.

---

## 9. Top-N Filtering

### Highest Salaries

```python
df.nlargest(
    10,
    'salary_year_avg'
)
```

Returns the top 10 salaries.

### Lowest Salaries

```python
df.nsmallest(
    10,
    'salary_year_avg'
)
```

Returns the lowest 10 salaries.

---

## 10. Query Method

Many analysts like this style.

```python
df.query(
    "salary_year_avg > 100000"
)
```

### Multiple Conditions

```python
df.query(
    "salary_year_avg > 100000 and job_work_from_home == True"
)
```

---

## 11. Filtering After GroupBy

### Example: Countries with Average Salary Above 100k

```python
avg_salary = (
    df.groupby('job_country')
      ['salary_year_avg']
      .mean()
)

avg_salary[avg_salary > 100000]
```

---

## 12. Filtering Using Value Counts

### Example: Countries Having More Than 100 Jobs

```python
country_counts = df['job_country'].value_counts()

country_counts[country_counts > 100]
```

---

# Most Important Filtering Techniques for Data Analysts

You should be comfortable with:

```python
==
!=
>
<
>=
<=
&
|
~
isin()
isna()
notna()
str.contains()
between()
query()
loc[]
iloc[]
```

---

# Example Real Analyst Filter

```python
df[
    (df['job_title_short'] == 'Data Analyst')
    &
    (df['job_work_from_home'] == True)
    &
    (df['salary_year_avg'].notna())
    &
    (df['salary_year_avg'] > 100000)
    &
    (df['job_country'].isin(
        ['United States', 'Canada']
    ))
]
```

This single filter combines:

- Equality filtering
- Boolean conditions
- Missing-value filtering
- Numeric filtering
- `isin()`

This is very close to what Data Analysts do in real-world projects.