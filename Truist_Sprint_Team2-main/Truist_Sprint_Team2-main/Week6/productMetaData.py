import random
from datetime import date, timedelta
import pandas as pd


def generate_metadata(num_rows):
    customer_data = []
    for i in range(num_rows):
        customer_ID = str(random.randint(100000000000, 999999999999))
        LOB_Code = random.choice(['C', 'R'])
        if LOB_Code == 'C':
            product_Name = random.choice(["Equipment Finance", "Line of Credit", "Real Estate"])
            if product_Name == "Equipment Finance":
                commitment_Amount = random.randint(1000000, 4000000)
            elif product_Name == "Line of Credit":
                commitment_Amount = random.randint(2000000, 4000000)
            elif product_Name == "Real Estate":
                commitment_Amount = random.randint(6000000, 10000000)
        elif LOB_Code == 'R':
            product_Name = random.choice(["Mortgage", "Car Loan", "Home Improvement", "Personal"])
            if product_Name == "Mortgage":
                commitment_Amount = random.randint(400000, 600000)
            elif product_Name == "Car Loan":
                commitment_Amount = random.randint(25000, 75000)
            elif product_Name == "Home Improvement":
                commitment_Amount = random.randint(50000, 125000)
            elif product_Name == "Personal":
                commitment_Amount = random.randint(10000, 30000)
        approval_Date = date.today() - timedelta(days=random.randint(365, 365*5))
        start_Date = approval_Date + timedelta(days=30)
        term = random.randint(60, 180)
        end_Date = start_Date + timedelta(days=term*30)
        funded_Amount = random.randint(int(commitment_Amount*0.8), commitment_Amount)
        available_Amount = commitment_Amount - funded_Amount

        customer_data.append({
            "customer_ID": customer_ID,
            "LOB_Code": LOB_Code,
            "Product_name": product_Name,
            "Approval_Date": approval_Date,
            "Start_Date": start_Date,
            "Term": term,
            "End_Date": end_Date,
            "Commitment_Amount": commitment_Amount,
            "Funded_Amount": funded_Amount,
            "Available_Amount": available_Amount
        })

    return customer_data

num_rows = int(input("How many rows of data do you want to create? "))
customer_data = generate_metadata(num_rows)

df = pd.DataFrame(customer_data)
df.to_csv("customer_data.csv", index=False)