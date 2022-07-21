import pandas as pd


def preprocess(df,region_df):

    df = df[df['Season'] == 'Summer']  # analysis only for summer olympics
    df = df.merge(region_df, on='NOC', how='left')  # merging the two datasets
    # dropping the duplicates
    df.drop_duplicates(inplace=True)
    # one hot encoding medals by assigning dummy variables
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    return df

