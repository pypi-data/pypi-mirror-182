import boto3


def get_current_account_id():
    account = boto3.client("sts").get_caller_identity().get("Account")
    return account


def get_current_user_id():
    user_id = boto3.client("sts").get_caller_identity().get("UserId")
    return user_id


def get_current_arn():
    arn = boto3.client("sts").get_caller_identity().get("Arn")
    return arn


def get_current_assumed_role():
    arn = get_current_arn()
    assumed_role = arn.split("/")[1]
    return assumed_role


def get_current_caller_identity():
    caller_identity = boto3.client("sts").get_caller_identity()
    return caller_identity
