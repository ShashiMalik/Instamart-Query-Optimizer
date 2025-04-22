import pandas as pd

# Load raw_queries search query data
df = pd.read_csv("data/raw_queries.csv")

# dictionary for category mapping
category_keywords = {
    "Dairy": ["milk", "cheese", "butter", "paneer"],
    "Bakery": ["bread", "bun", "croissant", "cake"],
    "Cleaning Supplies": ["detergent", "soap", "phenyl", "cleaner"],
    "Beverages": ["juice", "coffee", "tea", "soda"],
    "Snacks": ["biscuit", "chips", "namkeen", "chocolate"],
    "Fruits & Vegetables": ["apple", "banana", "tomato", "onion"],
    "Staples": ["rice", "atta", "dal", "sugar", "salt"]
}

# Function to map raw query to category
def map_category(query):
    query = query.lower()
    for category, keywords in category_keywords.items():
        if any(keyword in query for keyword in keywords):
            return category
    return "Uncategorized"

# Apply mapping to each raw_query
df["Category"] = df["Query"].apply(map_category)

# Save the result in csv file
df.to_csv("output/mapped_queries.csv", index=False)

print("Raw Query Mapping completed. Mapped queries are saved to 'output/mapped_queries.csv'")