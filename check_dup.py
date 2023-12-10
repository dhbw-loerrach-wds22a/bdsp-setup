import pandas as pd

# Define the chunk size
chunk_size = 500000  # Adjust this based on your system's memory

# Hash set to store unique row hashes
seen_hashes = set()
duplicates = []

# Function to hash a row (you can customize this)
def hash_row(row):
    return hash(tuple(row))

# Read the CSV in chunks
for chunk in pd.read_csv('./data/2019-Oct.csv', chunksize=chunk_size):
    for index, row in chunk.iterrows():
        row_hash = hash_row(row)
        if row_hash in seen_hashes:
            duplicates.append(row)
        else:
            seen_hashes.add(row_hash)

# Now 'duplicates' list contains all duplicate rows
print(duplicates)