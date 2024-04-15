import pickle
with open("/home/user/.dagster/storage/customers", "rb") as f:
    result = pickle.load(f)
result.to_csv('/home/user/dbt-dagster-proj/customers.csv', index=False)
