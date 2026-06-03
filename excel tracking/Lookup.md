# Excel Lookup Functions - Complete Notes

## Topics Covered

- VLOOKUP (Explain full working how it works)
- HLOOKUP (Explain full working how it works)
- XLOOKUP (Explain full working how it works)
- INDEX + MATCH
- Nested Lookups
- Multiple Criteria Lookups
- Approximate Match Lookups
- Error Handling (IFERROR)
- Two-Way Lookups
- Dynamic Lookups

---

# 1. What is a Lookup?

A lookup means:

> Find something and return related information.

## Example

| ID | Name | Salary |
|----|------|--------|
| 101 | Raj | 30000 |
| 102 | Amit | 40000 |
| 103 | Ravi | 50000 |

### Question

Find Salary of ID 102.

Excel first finds **102**, then returns **40000**.

This process is called **lookup**.

---

# Lookup Family

Excel mainly provides:

1. VLOOKUP
2. HLOOKUP
3. XLOOKUP
4. INDEX + MATCH

### Advanced Concepts

5. Nested Lookups
6. Multiple Criteria Lookups
7. Approximate Match Lookups
8. IFERROR
9. Two-Way Lookups
10. Dynamic Lookups

---

# 2. VLOOKUP

## Meaning

**V = Vertical**

Searches vertically (top to bottom).

## Syntax

```excel
=VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup])
```

### Parameters

#### 1. lookup_value

What you want to find.

Example:

```excel
102
```

#### 2. table_array

Entire table containing data.

Example:

```excel
A2:C10
```

#### 3. col_index_num

Column number from which value will be returned.

| A | B | C |
|---|---|---|
| ID | Name | Salary |

Column positions:

```text
A = 1
B = 2
C = 3
```

If you want Salary:

```excel
3
```

#### 4. range_lookup

```excel
FALSE
```

or

```excel
TRUE
```

- FALSE = Exact Match
- TRUE = Approximate Match

---

## How VLOOKUP Works Internally

Suppose:

| ID | Name | Salary |
|----|------|--------|
| 101 | Raj | 30000 |
| 102 | Amit | 40000 |
| 103 | Ravi | 50000 |

Formula:

```excel
=VLOOKUP(102,A2:C4,3,FALSE)
```

### Step 1

Looks only at first column.

```text
101
102
103
```

### Step 2

Searches for 102.

Found in row 2.

### Step 3

Moves to column 3.

```text
Salary
```

### Step 4

Returns:

```text
40000
```

## Biggest Limitation

Cannot look left.

Example:

| Name | ID |
|------|----|
| Raj | 101 |
| Amit | 102 |

This fails:

```excel
=VLOOKUP(102,A2:B3,1,FALSE)
```

Because VLOOKUP only searches in the first column.

---

# 3. HLOOKUP

## Meaning

**H = Horizontal**

Searches left to right.

## Syntax

```excel
=HLOOKUP(lookup_value, table_array, row_index_num, FALSE)
```

## Example

|   | A | B | C |
|---|---|---|---|
| 1 | ID | 101 | 102 |
| 2 | Name | Raj | Amit |
| 3 | Salary | 30000 | 40000 |

Formula:

```excel
=HLOOKUP(102,A1:C3,3,FALSE)
```

### How it Works

#### Step 1

Search first row.

```text
ID 101 102
```

Find:

```text
102
```

#### Step 2

Move to row 3.

#### Step 3

Return:

```text
40000
```

---

# 4. XLOOKUP

Modern replacement for VLOOKUP.

Much more powerful.

## Syntax

```excel
=XLOOKUP(
 lookup_value,
 lookup_array,
 return_array,
 [if_not_found],
 [match_mode],
 [search_mode]
)
```

## Example

```excel
=XLOOKUP(102,A2:A4,C2:C4)
```

Excel does:

1. Searches 102 in A2:A4
2. Finds matching row
3. Returns corresponding value from C2:C4

Result:

```text
40000
```

## Why XLOOKUP Is Better

### Can Lookup Left

```excel
=XLOOKUP(102,B2:B3,A2:A3)
```

Result:

```text
Amit
```

### Can Search From Bottom

```excel
=XLOOKUP(102,A:A,C:C,,0,-1)
```

### Can Return Custom Error

```excel
=XLOOKUP(999,A:A,C:C,"Not Found")
```

Result:

```text
Not Found
```

---

# 5. INDEX + MATCH

Most important concept.

Many interview questions use this.

## MATCH

Finds position.

```excel
=MATCH(102,A2:A4,0)
```

Result:

```text
2
```

Because 102 is the second item.

## INDEX

Returns value at a position.

```excel
=INDEX(C2:C4,2)
```

Result:

```text
40000
```

## Combine Them

```excel
=INDEX(C2:C4,MATCH(102,A2:A4,0))
```

Excel does:

```text
MATCH -> Position 2
INDEX -> Value at Position 2
```

Result:

```text
40000
```

## Why INDEX + MATCH Is Powerful

- Can lookup left
- Can lookup right
- Faster on huge datasets
- Flexible

---

# 6. Nested Lookups

One lookup inside another lookup.

Example:

```excel
=VLOOKUP(
 VLOOKUP("Raj",A2:B10,2,FALSE),
 D2:F10,
 3,
 FALSE
)
```

Inner lookup runs first.

Outer lookup uses the result.

---

# 7. Multiple Criteria Lookups

Need more than one condition.

| Name | Dept | Salary |
|--------|------|--------|
| Raj | IT | 30000 |
| Raj | HR | 40000 |

Find salary where:

```text
Name = Raj
Dept = HR
```

## Helper Column Method

```excel
=A2&B2
```

Creates:

```text
RajIT
RajHR
```

Lookup:

```excel
=XLOOKUP("RajHR",D2:D10,C2:C10)
```

Returns:

```text
40000
```

## Modern Method

```excel
=INDEX(C2:C10,
 MATCH(1,
 (A2:A10="Raj")*
 (B2:B10="HR"),
 0))
```

---

# 8. Approximate Match Lookups

Used in:

- Grades
- Tax Slabs
- Commission
- Incentives

| Marks | Grade |
|--------|------|
| 0 | F |
| 40 | C |
| 60 | B |
| 80 | A |

Formula:

```excel
=VLOOKUP(75,A2:B5,2,TRUE)
```

Excel finds:

```text
75 not found
```

Moves to nearest smaller value:

```text
60
```

Returns:

```text
B
```

## Important Rule

For TRUE lookup:

> Table must be sorted in ascending order.

---

# 9. Error Handling (IFERROR)

Without IFERROR:

```excel
=VLOOKUP(999,A:C,3,FALSE)
```

Result:

```text
#N/A
```

Using IFERROR:

```excel
=IFERROR(
 VLOOKUP(999,A:C,3,FALSE),
 "Not Found"
)
```

Result:

```text
Not Found
```

Very common in dashboards.

---

# 10. Two-Way Lookup

Need both row and column.

|      | Jan | Feb | Mar |
|------|-----|-----|-----|
| Raj  | 100 | 120 | 140 |
| Amit | 200 | 250 | 300 |

Question:

Find Amit's February sales.

## Solution

```excel
=INDEX(B2:D3,
 MATCH("Amit",A2:A3,0),
 MATCH("Feb",B1:D1,0)
)
```

Excel does:

```text
Amit -> Row 2
Feb -> Column 2
```

Returns:

```text
250
```

This is called a **Two-Way Lookup**.

---

# 11. Dynamic Lookups

Lookup formula changes automatically based on user selection.

User chooses:

- Salary
- Department

from a dropdown.

Formula:

```excel
=INDEX(
 B2:D10,
 MATCH(ID,A2:A10,0),
 MATCH(F1,B1:D1,0)
)
```

Where:

```text
F1 = Salary
```

or

```text
F1 = Department
```

The returned column changes automatically.

---

# Interview-Level Understanding

If you understand these four concepts deeply:

1. MATCH = Finds Position
2. INDEX = Returns Value
3. XLOOKUP = Modern Lookup
4. INDEX + MATCH = Row + Column Control

Then you can solve nearly every lookup problem asked in:

- Data Analyst Interviews
- Excel Assessments
- MIS Executive Tests
- Business Analyst Tests
- Operations Reporting Tasks

Because most advanced lookup questions are simply combinations of these building blocks.