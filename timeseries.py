# import dataframe library
import pandas as pd


def create_time_series(df):
    time_series = pd.DataFrame()

    # map dagar to time series for each unique address
    for address in df.address.unique():
        # create a dataframe for each address
        address_df = df[df["address"] == address]
        print(address_df)
        # create a time series for each address
        address_df = address_df.set_index("time")
    # create a time series for each address with dagar as values

    return time_series


# import sssb.csv as dataframe


def group_by_day(df):
    # group by registration and day
    vle_group = df.groupby(by=["address", "time"])
    # sum up the clicks for each day for each student
    sum_clicks = vle_group.sum(numeric_only=True).reset_index()
    sum_clicks = sum_clicks[["address", "time", "dagar"]]

    # sort by student and day
    sum_clicks = sum_clicks.sort_values(by=["address", "time"])
    return sum_clicks


def create_time_series(df):
    # Create a new dataframe to hold our timeseries data.
    time_series = pd.DataFrame()
    # Create one row for each student address
    time_series["address"] = df["address"].unique()

    # Iterate through the days of the course:

    for date in df["time"].unique():

        # create a views of the data, one day at a time.
        single_time_df = df[df["time"] == date]
        single_time_df = single_time_df.drop(columns=["time"])
        # rename columns to describe time and data.
        new_cols = ["address"] + [f"clicks_on_day_{date}"]
        single_time_df.columns = new_cols
        # merge into the time series dataframe.
        time_series = time_series.merge(single_time_df, how="left", on="address")

    # Missing data represents no clicks that day, so fill with 0.
    time_series = time_series.fillna(0)
    time_series = time_series.set_index("address", drop=True)
    return time_series


def update_time():
    df = pd.read_csv("sssb.csv")
    time_series = create_time_series(group_by_day(df))

    df.drop(df.columns[1], inplace=True, axis=1)
    # save time series to csv
    time_series.to_csv("time_series.csv")
