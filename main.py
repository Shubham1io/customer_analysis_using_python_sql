from src.extract import load_customer_data
from src.transform import clean_customer_behavior_data
from src.database import get_connection
from src.load import load_data



# Extract

df = load_customer_data()

#Transform

df = clean_customer_behavior_data(df)

# save processed data
df.to_csv("data/processed/clean_customer_shopping_behavior.csv", index=False)

# database connection

engine = get_connection()

# load data

load_data(df,engine)

print('Data loaded successfully !')