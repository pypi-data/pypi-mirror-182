import boto3


def show_all_available_regions():
    """
    Prints current available regions

    :return: None
    """
    client = boto3.client("ec2")
    for region in client.describe_regions()["Regions"]:
        print(region["RegionName"])


def show_all_regions():
    """
    Prints current available regions

    :return: None
    """
    client = boto3.client("ec2")
    for region in client.describe_regions(AllRegions=True)["Regions"]:
        print(region["RegionName"])
