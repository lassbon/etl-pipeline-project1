import logging
def load_data(df):
    logging.info("Saving data into an excel file ...")
    df.to_csv("cleandData22.csv", index=False)

    logging.info("Saving Completed ...")
    print(df["company_name"].unique())
    print(df[["company"]['name']].value_counts())

    # print(df.groupby(["email_domain", "score"])["name"].count())

    # print(df.shape)
    # print(df.columns)
    # print(df.info())
    # print(df.value_counts())
    return df