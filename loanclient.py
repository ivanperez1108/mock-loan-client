import requests


class LoanClient:
    """
    A class used to interface with the mock-loan-system REST API
    """

    URL = "https://mock-loan-system.herokuapp.com"

    def create_loan(self, amount: float, interest_rate: float, length: int) -> dict:
        """
        Creates a loan and returns the loan properties in a dict

        Parameters
        amount : float, The amount of the loan
        interest_rate : float, The interest rate of the loan
        length: int, The length of the loan in months
        """

        url_to_hit = self.URL + "/create-loan"

        data = {
            'amount': amount,
            'interest_rate': interest_rate,
            'length': length
        }

        response = requests.post(url_to_hit, data=data)
        json = response.json()

        if json['success']:
            return json['loan']
        else:
            raise Exception("Unable to create loan: " + json['error_message'])

    def get_loan(self, loan_id: int) -> dict:
        """
        Returns a loan with the given loan_id

        Parameters
        loan_id : int, The unique id of the loan to grab
        """

        url_to_hit = self.URL + "/get-loan"

        data = {
            'id': loan_id
        }

        response = requests.get(url_to_hit, params=data)
        json = response.json()

        if json['success']:
            return json['loan']
        else:
            raise Exception("Unable to get loan: " + json['error_message'])

    def update_loan(self, loan_id: int, amount: float, interest_rate: float, length: int):
        """
        Updates a loan and returns the loan properties in a dict

        Parameters
        loan_id : int, The unique id of the loan to update
        amount : float, The amount of the loan
        interest_rate : float, The interest rate of the loan
        length: int, The length of the loan in months
        """

        url_to_hit = self.URL + "/update-loan"

        data = {
            'id': loan_id,
            'amount': amount,
            'interest_rate': interest_rate,
            'length': length
        }

        response = requests.post(url_to_hit, data=data)
        json = response.json()

        if json['success']:
            return json['loan']
        else:
            raise Exception("Unable to update loan: " + json['error_message'])
