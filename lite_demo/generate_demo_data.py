from faker import Faker
import pandas as pd
import random

# Initialize Faker
fake = Faker()

# Generate demo data
data = {
    "ID": [fake.unique.random_int(min=1000, max=9999) for _ in range(50)],  # Unique identifier
    "Name": [fake.name() for _ in range(50)],  # Full name
    "Email": [fake.email() for _ in range(50)],  # Email address
    "Phone": [fake.phone_number() for _ in range(50)],  # Phone number
    "Date": [fake.date_this_year() for _ in range(50)],  # Date of transaction
    "Category": [fake.random_element(elements=("A", "B", "C", "D")) for _ in range(50)],  # Category
    "Value": [fake.random_int(min=10, max=1000) for _ in range(50)],  # Transaction value
    "City": [fake.city() for _ in range(50)],  # City
    "Country": [fake.country() for _ in range(50)],  # Country
    "Company": [fake.company() for _ in range(50)],  # Company name
    "Job_Title": [fake.job() for _ in range(50)],  # Job title
    "Payment_Method": [fake.random_element(elements=("Credit Card", "PayPal", "Bank Transfer")) for _ in range(50)],  # Payment method
    "Product": [fake.random_element(elements=("Product A", "Product B", "Product C", "Product D")) for _ in range(50)],  # Product name
    "Quantity": [fake.random_int(min=1, max=10) for _ in range(50)],  # Quantity purchased
    "Total_Cost": [round(random.uniform(100, 5000), 2) for _ in range(50)],  # Total cost of purchase
}

# Save to CSV
output_file = "lite_demo/demo_data.csv"
df = pd.DataFrame(data)
df.to_csv(output_file, index=False)

print(f"Generated demo dataset with {len(data['ID'])} records saved to {output_file}.")
