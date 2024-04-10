import pandas as pd


def calculate_activity_per_cell(data: pd.DataFrame) -> pd.DataFrame:
    activity = data.groupby(["x", "y"])["uid"].count().reset_index()
    activity.rename({"uid": "count"}, axis=1, inplace=True)
    return activity


def calculate_number_of_unique_users_per_cell(data: pd.DataFrame) -> pd.DataFrame:
    unique_users = data.groupby(["x", "y"])["uid"].nunique().reset_index()
    unique_users.rename({"uid": "count"}, axis=1, inplace=True)
    return unique_users


def calculate_user_activity(data: pd.DataFrame) -> pd.DataFrame:
    user_activity = data.groupby("uid")["d"].count().reset_index()
    user_activity.rename({"d": "count"}, axis=1, inplace=True)
    # user_activity.columns = pd.Index(["uid", "activity"])
    return user_activity


if __name__ == "__main__":
    import argparse

    import structlog

    logger = structlog.get_logger()

    argparser = argparse.ArgumentParser()
    subparsers = argparser.add_subparsers(dest="command", help="sub-command help")
    parser_apc = subparsers.add_parser("all", help="calculate every descriptives")
    parser_apc = subparsers.add_parser(
        "cell-activity", help="calculate activity per cell"
    )
    parser_upc = subparsers.add_parser(
        "cell-user", help="calculate number of unique users per cell"
    )
    parser_apu = subparsers.add_parser(
        "user-activity", help="calculate activity per user"
    )
    argparser.add_argument(
        "--mobility-data",
        type=str,
        required=False,
        default="../data/yjmob100k",
        help="directory of the mobility data",
    )
    argparser.add_argument(
        "--output",
        type=str,
        required=False,
        default="../output",
        help="output directory",
    )
    opts = argparser.parse_args()

    data = pd.read_csv(f"{opts.mobility_data}/yjmob100k-dataset1.csv", engine="pyarrow")

    if opts.command in ["all", "cell-activity"]:
        logger.info("calculating activity per cell")
        activity = calculate_activity_per_cell(data)
        activity.to_csv(f"{opts.output}/activity.csv", index=False)

    if opts.command in ["all", "cell-user"]:
        logger.info("calculating number of unique users per cell")
        unique_users = calculate_number_of_unique_users_per_cell(data)
        unique_users.to_csv(f"{opts.output}/unique_users.csv", index=False)

    if opts.command in ["all", "user-activity"]:
        logger.info("calculating activity per user")
        user_activity = calculate_user_activity(data)
        user_activity.to_csv(f"{opts.output}/user_activity.csv", index=False)

    logger.info("finished")
