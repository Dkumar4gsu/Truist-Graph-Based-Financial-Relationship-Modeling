# Week 9 

Tried to create a more meaningful synthetic data keeping the target feature. Generated around 18 features out of which 7 are completely randomly generated, and the rest 11 with respect to some rules. 

Generated missed payments, delinquent days etc. with respect to distribution (with 60% for 0, 20% for 1-4, 10% for 5-10, 10% for 11-20).

Credit score was calculated with respect to market research. Utilized weights for payment history, credit history, credit usage, total balance etc. and achieved a good distribution for the credit score.

Probability of default is calculated with a tree-based model using credit score, debt to income ratio, delinquent days.

We then created a graph on the dataset, queried on them to get insights on the synthetic data generated.