import logging
import pandas as pd
from utils import *

def transform_data(data):
    # Transform
    logging.info("Transforming data started ...")
    df = pd.DataFrame(data)
    specificData = df[
        ['name', 'email', 'phone', 'website']]  # 08084259372 , +2348084259372 +234 8084 259 372  +234-8084-259-372
    df['has_website'] = df['website'].notnull()
    df["phone"] = df["phone"].apply(cleanPhone)
    df["email"] = df["email"].apply(cleanEmail)
    df["email_domain"] = df["email"].apply(getEmailDomain)

    df["domain_type"] = df["email_domain"].apply(lambda x: "BUSINESS" if "biz" in x else "INDIVIDUAL")
    df["website_score"] = df["has_website"].apply(lambda x: 5 if x else 0)
    df["business_score"] = df["domain_type"].apply(lambda x: 3 if x == "BUSINESS" else 2)

    df["total_score"] = df["website_score"] + df["business_score"] + df["username"].str.len()

    df.sort_values("total_score", inplace=True, ascending=True)
    # Analysis
    df['has_website'].value_counts()
    df['has_website'].value_counts(normalize=True)
    # print(df["email_domain"])
    df["has_website"].value_counts()

    print(df[["name", "email", "phone", "website", "has_website","email_domain","domain_type","website_score","business_score","total_score"]])
    return df


