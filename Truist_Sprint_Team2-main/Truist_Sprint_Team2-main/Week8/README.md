# Week 8

As the whole dataset was discussed and the key point of the project being proper meaningful synthetic data creation, started working on creating the dataset.

For our team, we chose the ‘probability_of_default’ as our target feature. We check this feature if it is 1 or 0. If 1, we can select those customers and create some ML algorithm to suggest a new product to them. If 0, we could check which aspects the customer need to work on to become a safer customer.

We generated data randomly with small rules but for prob of default, we used a linear formula with credit score, missed payments, debt to income ratio and segregated customer.

We then created a graph on the dataset, queried on them to get insights on the synthetic data generated.