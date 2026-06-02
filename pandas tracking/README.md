# Pandas Notes - Basics

## 1. Exploring a DataFrame

### What You Learned

```python
df.head()
df.tail()
df.shape
df.columns
df.dtypes
```

### Why It Matters

Whenever you receive a new dataset, the first step is to understand it.

Questions to answer:

- How many rows are there?
- How many columns are there?
- What are the column names?
- What data types are present?

This is usually the first 2–5 minutes of any data analysis project.

### Examples

```python
df.head()      # First 5 rows
df.tail()      # Last 5 rows
df.shape       # (rows, columns)
df.columns     # Column names
df.dtypes      # Datatypes of all columns
```

---

## 2. Selecting Columns

### What You Learned

```python
df['name']
```

and

```python
df[['name', 'salary']]
```

### Important Concept

#### Single Column

```python
df['salary']
```

Returns a **Series**

#### Multiple Columns

```python
df[['name', 'salary']]
```

Returns a **DataFrame**

### Why It Matters

Understanding the difference between Series and DataFrame is extremely important in Pandas.

---

## 3. Understanding Data Types

### What You Learned

```python
df.dtypes
```

### Common Data Types

| Type | Meaning |
|--------|---------|
| int64 | Integer |
| float64 | Decimal Number |
| object | String/Text |
| bool | True/False |
| datetime64 | Date & Time |

### Why It Matters

Many Pandas operations depend on datatype.

Example:

```python
df['salary'].mean()
```

Works only on numeric columns.

This will fail:

```python
df['name'].mean()
```

Because names are text.

---

## 4. Missing Value Analysis

### What You Learned

```python
df.isnull().sum()
```

or

```python
df.isna().sum()
```

### Why It Matters

Real-world datasets almost always contain missing values.

Example:

| Salary |
|----------|
| 50000 |
| NaN |
| 70000 |

Finding missing data is one of the first tasks in data cleaning.

### Example

```python
df.isnull().sum()
```

Returns the number of missing values in each column.

---

## 5. Aggregation Functions

### What You Learned

```python
mean()
max()
min()
count()
```

### Examples

```python
df['salary'].mean()
df['salary'].max()
df['salary'].min()
df['salary'].count()
```

### Why It Matters

Aggregation functions summarize many values into one value.

Example:

```
50000
60000
70000
```

Average:

```
60000
```

---

## 6. Unique Values

### What You Learned

```python
unique()
nunique()
```

### Example

```python
df['department'].unique()
```

Output:

```python
['IT', 'HR', 'Finance']
```

### Difference

#### unique()

Returns actual unique values.

#### nunique()

Returns count of unique values.

Example:

```python
df['department'].nunique()
```

Output:

```python
3
```

---

## 7. Boolean Filtering

### What You Learned

```python
df[df['salary'] > 50000]
```

or

```python
df[df['department'] == 'IT']
```

### Concept

Each condition creates a Boolean mask:

```python
True
False
True
False
```

Pandas keeps only rows where the condition is `True`.

### Examples

```python
df[df['salary'] > 50000]
```

```python
df[df['city'] == 'Delhi']
```

---

## 8. Multiple Conditions

### AND Condition

```python
&
```

### OR Condition

```python
|
```

### Example

```python
df[
    (df['salary'] > 50000)
    &
    (df['department'] == 'IT')
]
```

### Another Example

```python
df[
    (df['city'] == 'Delhi')
    |
    (df['city'] == 'Mumbai')
]
```

---

## 9. Comparison Operators

### Operators Used in Pandas

| Operator | Meaning |
|-----------|----------|
| > | Greater Than |
| < | Less Than |
| >= | Greater Than or Equal |
| <= | Less Than or Equal |
| == | Equal To |
| != | Not Equal To |

### Examples

```python
salary > 50000
```

```python
age >= 30
```

```python
city == "Delhi"
```

These operators are used constantly in filtering.

---

## 10. Sorting Data

### What You Learned

```python
sort_values()
```

### Ascending Order

```python
df.sort_values('salary')
```

### Descending Order

```python
df.sort_values(
    'salary',
    ascending=False
)
```

### Why It Matters

Sorting helps find:

- Highest sales
- Top earners
- Oldest employees
- Lowest performers

---

## 11. Getting Top Records

### Example

```python
df.sort_values(
    'salary',
    ascending=False
).head(5)
```

### Business Use Cases

Finding:

- Top 5 Customers
- Top 5 Employees
- Top 5 Products
- Top 5 Sales Regions

This is one of the most common analysis tasks.

---

## 12. Understanding Shape

### What You Learned

```python
df.shape
```

### Output

```python
(rows, columns)
```

Example:

```python
(1000, 12)
```

Meaning:

- 1000 rows
- 12 columns

### Why It Matters

Quickly tells you the size of the dataset.

---

## 13. Understanding DataFrame vs Series

### Series

```python
df['salary']
```

Output Type:

```python
Series
```

### DataFrame

```python
df[['salary']]
```

Output Type:

```python
DataFrame
```

### Key Difference

| Series | DataFrame |
|----------|------------|
| 1-D | 2-D |
| Single Column | Multiple Columns |
| Simpler Structure | Table Structure |

---

## 14. Understanding NumPy ndarray

### What You Learned

```python
df['department'].unique()
```

Returns:

```python
numpy.ndarray
```

### Why It Matters

Pandas is built on top of NumPy.

Many Pandas functions return NumPy objects.

Example:

```python
type(df['department'].unique())
```

Output:

```python
numpy.ndarray
```

### Key Takeaway

- NumPy is the foundation.
- Pandas is built on NumPy.
- Many Pandas operations internally use NumPy arrays.

---

# Quick Revision

### Data Exploration

```python
df.head()
df.tail()
df.shape
df.columns
df.dtypes
```

### Column Selection

```python
df['col']
df[['col1', 'col2']]
```

### Missing Values

```python
df.isnull().sum()
```

### Aggregation

```python
mean()
max()
min()
count()
```

### Unique Values

```python
unique()
nunique()
```

### Filtering

```python
df[df['salary'] > 50000]
```

### Multiple Conditions

```python
&
|
```

### Sorting

```python
sort_values()
```

### Top Records

```python
head()
```

### Dataset Size

```python
shape
```

### Data Structures

```python
Series
DataFrame
numpy.ndarray
```

### Date Time 

