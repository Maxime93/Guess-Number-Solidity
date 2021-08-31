import os
from dotenv import load_dotenv
from brownie import accounts, GuessNumber, Wei

load_dotenv()
def main():
    deploy_account = accounts.add(os.environ['PRIVATE_KEY_1'])
    deployment_details = {
        'from': deploy_account,
        'value': Wei('10 ether')
    }
    guess_number = GuessNumber.deploy(9, deployment_details)
    return guess_number
