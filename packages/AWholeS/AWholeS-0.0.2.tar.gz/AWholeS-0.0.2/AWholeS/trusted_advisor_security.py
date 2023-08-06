from dataclasses import dataclass

import boto3


@dataclass
class FailedSecurityChecks:
    error_checks: list
    warning_checks: list


class TrustedAdvisor:
    def __init__(self):
        self._support_client = boto3.client("support", region_name="us-east-1")

    def describe_checks(self):
        """
        Prints information about Trusted Advisor Security Checks

        :return: None
        """
        try:
            response = self._support_client.describe_trusted_advisor_checks(language="en")
            for check in response.get("checks"):
                if check.get("category") == "security":
                    print(f"{check.get('id')} - {check.get('name')} - {check.get('metadata')}")
        except Exception as e:
            print(e)

    def obtain_security_checks(self) -> list:
        """
        Returns the entire list of Trusted Advisor Security checks

        :return: list
        """
        security_checks = []
        try:
            response = self._support_client.describe_trusted_advisor_checks(language="en")
            for check in response.get("checks"):
                if check.get("category") == "security":
                    security_checks.append(check)
        except Exception as e:
            print(e)
        return security_checks

    def describe_check_by_check_id(self, check_id: str):
        """
        Prints the response of describing a given check by its id

        :param check_id: Id of the check
        :return: None
        """
        try:
            response = self._support_client.describe_trusted_advisor_check_result(checkId=check_id, language="en")
            print(response)
        except Exception as e:
            print(e)

    def obtain_failed_security_checks(self) -> FailedSecurityChecks:
        """
        Returns a list of all failed with error Trusted Advisor Security Checks

        :return: None
        """
        error_security_checks = []
        warning_security_checks = []
        for sec_check in self.obtain_security_checks():
            try:
                response = self._support_client.describe_trusted_advisor_check_result(
                    checkId=sec_check.get("id"), language="en"
                )
                check_status = response.get("result").get("status")
                if check_status in ["error"]:
                    error_security_checks.append(sec_check)
                if check_status in ["warning"]:
                    warning_security_checks.append(sec_check)
            except Exception as e:
                print(e)

        return FailedSecurityChecks(error_checks=error_security_checks, warning_checks=warning_security_checks)

    def show_failed_security_checks(self):
        """
        Prints failed Trusted Advisor Security Checks

        :return: None
        """
        failed_checks = self.obtain_failed_security_checks()
        print("ERROR")
        for sec_check in failed_checks.error_checks:
            print(sec_check.get("name"))
        print("WARNING")
        for sec_check in failed_checks.warning_checks:
            print(sec_check.get("name"))


def describe_severity_levels():
    """
    Prints the response of describing the security levels for the account

    :return: None
    """
    client = boto3.client("support")
    response = client.describe_severity_levels(language="en")
    print(response)
