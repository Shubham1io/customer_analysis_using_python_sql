def load_data(df, engine):

    df.to_sql(
        "customer_purchase_data",
        con=engine,
        if_exists="replace",
        index=False
    )