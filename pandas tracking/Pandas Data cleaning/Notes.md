df = df.drop(5)                # Remove row with index 5
df = df.drop([2, 4, 6])        # Remove multiple rows
df = df.reset_index(drop=True) # Create fresh index