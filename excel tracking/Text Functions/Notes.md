# Excel Text Functions
## Importaint Text functions: 
- RIGHT()
- MID()
- LEN()
- FIND()
- TEXTJOIN()
- TEXTSPLIT()
- TEXTBEFORE()
- TEXTAFTER()
- FILTER()
- UNIQUE()
- SORT()

## 1. What Are Text Functions?

Text functions are used to:

- Join text
- Split text
- Extract characters
- Count characters
- Change case (UPPER/lower)
- Find specific words
- Remove spaces
- Replace text
- Format data

### Understanding Text Positions

Consider:

```excel
A1 = "Rajan Kumar"
```

Position numbering:

```text
R a j a n   K u m a r
1 2 3 4 5 6 7 8 9 10 11
```

Excel counts spaces too.

---

## 2. LEN()

Returns the total number of characters.

### Syntax

```excel
=LEN(text)
```

### Example

```excel
=LEN("Excel")
```

Output:

```text
5
```

### Example

```excel
=LEN("Rajan Kumar")
```

Output:

```text
11
```

Space is counted.

### Uses

- Count ID length
- Check phone numbers
- Validate codes

Example:

```excel
=LEN(A2)
```

---

## 3. LEFT()

Extracts characters from the left side.

### Syntax

```excel
=LEFT(text,num_chars)
```

### Example

```excel
=LEFT("RAJAN123",5)
```

Output:

```text
RAJAN
```

### Example

```excel
=LEFT(A2,3)
```

If A2 contains:

```text
IND56789
```

Output:

```text
IND
```

### Data Analyst Use

Extract country code.

Example data:

```text
IND56789
USA45321
```

Formula:

```excel
=LEFT(A2,3)
```

---

## 4. RIGHT()

Extracts characters from the right side.

### Syntax

```excel
=RIGHT(text,num_chars)
```

### Example

```excel
=RIGHT("RAJAN123",3)
```

Output:

```text
123
```

### Data Analyst Use

Extract last digits from employee IDs.

```excel
=RIGHT(A2,5)
```

---

## 5. MID()

Extracts text from the middle.

### Syntax

```excel
=MID(text,start_num,num_chars)
```

### Example

```excel
=MID("RAJAN123",6,3)
```

Output:

```text
123
```

Explanation:

```text
Start at position 6
Take 3 characters
```

### Example

```excel
=MID("ABCD123XYZ",5,3)
```

Output:

```text
123
```

---

## 6. UPPER()

Converts all letters to uppercase.

### Syntax

```excel
=UPPER(text)
```

### Example

```excel
=UPPER("rajan")
```

Output:

```text
RAJAN
```

---

## 7. LOWER()

Converts all letters to lowercase.

### Syntax

```excel
=LOWER(text)
```

### Example

```excel
=LOWER("RAJAN")
```

Output:

```text
rajan
```

---

## 8. PROPER()

Capitalizes the first letter of every word.

### Syntax

```excel
=PROPER(text)
```

### Example

```excel
=PROPER("rajan kumar prajapati")
```

Output:

```text
Rajan Kumar Prajapati
```

### Data Cleaning Use

Employee names.

---

## 9. TRIM()

Removes extra spaces.

### Syntax

```excel
=TRIM(text)
```

### Example

Input:

```text
"  Rajan    Kumar   "
```

Formula:

```excel
=TRIM(A2)
```

Output:

```text
Rajan Kumar
```

### Important

TRIM removes:

- Leading spaces
- Trailing spaces
- Multiple spaces

But keeps one space between words.

---

## 10. CONCAT()

Joins text.

### Syntax

```excel
=CONCAT(text1,text2,...)
```

### Example

```excel
=CONCAT("Rajan"," ","Kumar")
```

Output:

```text
Rajan Kumar
```

---

## 11. CONCATENATE()

Old version of CONCAT.

```excel
=CONCATENATE(A2," ",B2)
```

Still works, but CONCAT is preferred.

---

## 12. TEXTJOIN()

Most powerful joining function.

### Syntax

```excel
=TEXTJOIN(delimiter,ignore_empty,text1,...)
```

### Example

```excel
=TEXTJOIN("-",TRUE,A2:C2)
```

Output:

```text
A-B-C
```

---

## 13. FIND()

Case-sensitive search.

### Syntax

```excel
=FIND(find_text,within_text)
```

### Example

```excel
=FIND("K","Rajan Kumar")
```

Output:

```text
7
```

K starts at position 7.

### Case Sensitive Example

```excel
=FIND("k","Rajan Kumar")
```

Output:

```text
Error
```

Because:

```text
K ≠ k
```

---

## 14. SEARCH()

Not case-sensitive.

### Syntax

```excel
=SEARCH(find_text,within_text)
```

### Example

```excel
=SEARCH("k","Rajan Kumar")
```

Output:

```text
7
```

### Difference

| Function | Case Sensitive |
|----------|---------------|
| FIND | Yes |
| SEARCH | No |

---

## 15. REPLACE()

Replace by position.

### Syntax

```excel
=REPLACE(old_text,start_num,num_chars,new_text)
```

### Example

```excel
=REPLACE("AB123CD",3,3,"999")
```

Output:

```text
AB999CD
```

---

## 16. SUBSTITUTE()

Replace actual text.

### Syntax

```excel
=SUBSTITUTE(text,old_text,new_text)
```

### Example

```excel
=SUBSTITUTE("Apple Apple","Apple","Mango")
```

Output:

```text
Mango Mango
```

Replace only the second occurrence:

```excel
=SUBSTITUTE("Apple Apple","Apple","Mango",2)
```

Output:

```text
Apple Mango
```

---

## 17. TEXT()

Converts values into formatted text.

### Syntax

```excel
=TEXT(value,format_text)
```

### Date Example

```excel
=TEXT(A2,"dd-mm-yyyy")
```

Output:

```text
15-08-2025
```

### Currency Example

```excel
=TEXT(A2,"₹#,##0")
```

---

## 18. VALUE()

Convert text numbers into actual numbers.

### Example

Input:

```text
"100"
```

Formula:

```excel
=VALUE(A2)
```

Output:

```text
100
```

(Number)

---

## 19. EXACT()

Checks whether two texts are exactly the same.

Case-sensitive.

### Syntax

```excel
=EXACT(text1,text2)
```

### Example

```excel
=EXACT("RAJAN","RAJAN")
```

Output:

```text
TRUE
```

### Example

```excel
=EXACT("RAJAN","rajan")
```

Output:

```text
FALSE
```

---

## 20. REPT()

Repeats text.

### Syntax

```excel
=REPT(text,number_times)
```

### Example

```excel
=REPT("*",10)
```

Output:

```text
**********
```

---

## 21. CHAR()

Returns a character from an ASCII code.

```excel
=CHAR(65)
```

Output:

```text
A
```

---

## 22. CODE()

Reverse of CHAR.

```excel
=CODE("A")
```

Output:

```text
65
```

---

## 23. CLEAN()

Removes non-printable characters.

```excel
=CLEAN(A2)
```

Useful when importing data.

---

## 24. TEXTBEFORE() (Excel 365)

### Syntax

```excel
=TEXTBEFORE(text,delimiter)
```

### Example

```excel
=TEXTBEFORE("rajan@gmail.com","@")
```

Output:

```text
rajan
```

---

## 25. TEXTAFTER()

### Example

```excel
=TEXTAFTER("rajan@gmail.com","@")
```

Output:

```text
gmail.com
```

---

## 26. TEXTSPLIT()

Split text.

### Example

```excel
=TEXTSPLIT("A,B,C",",")
```

Output:

```text
A   B   C
```

---

# Data Analyst Level Combinations

## Extract First Name

```excel
=LEFT(A2,SEARCH(" ",A2)-1)
```

## Extract Last Name

```excel
=RIGHT(A2,LEN(A2)-SEARCH(" ",A2))
```

## Extract Email Username

```excel
=LEFT(A2,SEARCH("@",A2)-1)
```

## Extract Domain

```excel
=RIGHT(A2,LEN(A2)-SEARCH("@",A2))
```

## Create Employee ID

```excel
=UPPER(LEFT(A2,3))&RIGHT(B2,4)
```

Example:

```text
Rajan
987654
```

Output:

```text
RAJ7654
```