import pandas as pd
import numpy as np
from sklearn.mixture import GaussianMixture
from sklearn.neighbors import KernelDensity
import random
from datetime import date, timedelta

df = pd.read_csv("bank-additional-full.csv", sep=';')

# Age
# Data augmentation with noise
age = df.age.values
augmented_age_gen = np.zeros((len(age),))

for i in range(len(age)):
    idx = np.random.randint(0,len(age))
    augmented_age_gen[i] = age[idx] + np.random.randint(-3,3)

# Gaussian mixture model (GMM) 
n_components = 3  # Number of mixture components
gmm = GaussianMixture(n_components=n_components).fit(age.reshape(-1, 1))

gmm_age = gmm.sample(n_samples=len(age))[0].flatten()
gmm_age = np.round(gmm_age).astype(int)

# Kernel Density Estimation (KDE)
bandwidth = 2  # Bandwidth parameter
kde = KernelDensity(bandwidth=bandwidth).fit(age.reshape(-1, 1))

kde_age = kde.sample(n_samples=len(age), random_state=0).flatten()
kde_age = np.round(kde_age).astype(int)

# Creating a dataframe for synthetic data
product_gen_data = pd.DataFrame()
product_gen_data['age'] = kde_age

# Job and Education
joint_dist = pd.crosstab(df['job'], df['education'], normalize=True)

# calculate the marginal distributions of job and education
job_marginal = joint_dist.sum(axis=1)
edu_marginal = joint_dist.sum(axis=0)

# create synthetic data based on the joint distribution
n_samples = len(df)

synth_job = np.random.choice(job_marginal.index, n_samples, p=job_marginal.values)
synth_edu = np.empty(n_samples, dtype=object)

for i in range(n_samples):
    job = synth_job[i]
    p_edu_given_job = joint_dist.loc[job] / job_marginal.loc[job]
    synth_edu[i] = np.random.choice(edu_marginal.index, p=p_edu_given_job.values)

product_gen_data['job'] = synth_job
product_gen_data['education'] = synth_edu

# Marital
product_gen_data['marital'] = np.where(product_gen_data['age'] < 21, 'no', 
                                       np.random.choice(['yes', 'no'], 
                                       len(product_gen_data)))

# Housing and Loan
product_gen_data['housing'] = np.where(product_gen_data['age'] < 24, 
                                       'no', np.random.choice(['yes', 'no'], 
                                                              len(product_gen_data)))
product_gen_data['loan'] = np.where(product_gen_data['age'] < 21, 
                                       'no', np.random.choice(['yes', 'no'], 
                                                              len(product_gen_data)))

# All other columns like term, product, funded amount etc.
approval_Date1 = []
start_Date1 = []
term1 = []
end_Date1 = []
customer_ID1 = []

for i in range(len(df)):
    approval_Date = date.today() - timedelta(days=random.randint(365, 365*5))
    start_Date = approval_Date + timedelta(days=30)
    term = random.randint(60, 180)
    end_Date = start_Date + timedelta(days=term*30)
    customer_ID = str(random.randint(1000000, 9999999))
    
    approval_Date1.append(approval_Date)
    start_Date1.append(start_Date)
    term1.append(term)
    end_Date1.append(end_Date)
    customer_ID1.append(customer_ID)
    
product_gen_data['Approval_Date'] = approval_Date1
product_gen_data['Start_Date'] = start_Date1
product_gen_data['Term'] = term1
product_gen_data['End_Date'] = end_Date1
product_gen_data['customer_ID'] = customer_ID1

def get_product_code(row):
    if row['housing'] == 'yes' and row['loan'] == 'no':
        return 'Home Loan'
    elif row['housing'] == 'no' and row['loan'] == 'yes':
        return 'Personal Loan'
    elif row['housing'] == 'yes' and row['loan'] == 'yes':
        return np.random.choice(['Home Loan', 'Personal Loan'])
    else:
        return np.random.choice(['Mortgage', 'Real Estate Loan', 'Car Loan'])

def get_commitment_amount(row):
    if row['Product_Code'] == 'Home Loan':
        return random.randint(400000, 600000)
    elif row['Product_Code'] == 'Personal Loan':
        return random.randint(20000, 80000)
    elif row['Product_Code'] == 'Mortgage':
        return random.randint(300000, 500000)
    elif row['Product_Code'] == 'Real Estate Loan':
        return random.randint(250000, 550000)
    else:
        return random.randint(30000, 75000)

def get_funded_amount(row):
    return random.randint(int(row['Commitment_Amount']*random.uniform(0.7,0.9)), row['Commitment_Amount'])

def get_available_amount(row):
    return row['Commitment_Amount'] - row['Funded_Amount']

product_gen_data['Product_Code'] = product_gen_data.apply(get_product_code, axis=1)
product_gen_data['Commitment_Amount'] = product_gen_data.apply(get_commitment_amount, axis=1)
product_gen_data['Funded_Amount'] = product_gen_data.apply(get_funded_amount, axis=1)
product_gen_data['Available_Amount'] = product_gen_data.apply(get_available_amount, axis=1)

product_gen_data.to_csv("product_synthetic_data.csv", index=False)