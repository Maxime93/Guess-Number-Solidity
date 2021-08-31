import pytest
import brownie
from brownie import Wei, accounts, GuessNumber

contract_init_account_index = 8
number_to_guess = 4

@pytest.fixture
def guess_number():
    deployment_details = {
        'from': accounts[contract_init_account_index],
        'value': Wei('10 ether')
    }
    return GuessNumber.deploy(number_to_guess, deployment_details)

def test_wrong_amount(guess_number):
    player_index = 3
    with brownie.reverts("You must pay exactly 10 eth to play"):
        guess_number.play(9, accounts[player_index],{'from': accounts[player_index], 'value':'1 ether'})

def test_wrong_guess(guess_number):
    # the balance of the player will decrease by 10 eth
    player_index = 4
    init_player_balance = accounts[player_index].balance()
    init_contract_balance = guess_number.balance()

    guess_number.play(9, accounts[player_index],{'from': accounts[player_index], 'value':'10 ether'})
    # contract wins 10, player looses 10.

    post_wrong_amount_player_balance = accounts[player_index].balance()
    post_wrong_amount_contract_balance = guess_number.balance()

    assert init_contract_balance == post_wrong_amount_contract_balance - Wei('10 ether')
    assert init_player_balance == post_wrong_amount_player_balance + Wei('10 ether')
    assert guess_number.currState() == 0

def test_play_right_guess(guess_number):
    # the balance of the player will increase by 10 eth
    player_index = 5
    init_player_balance = accounts[player_index].balance()
    init_contract_balance = guess_number.balance()

    guess_number.play(number_to_guess, accounts[player_index],{'from': accounts[player_index], 'value':'10 ether'})
    # contract wins 10, player looses 10.

    post_right_amount_player_balance = accounts[player_index].balance()
    # post_right_amount_contract_balance = guess_number.balance()

    assert guess_number.getBalance() == 0
    assert post_right_amount_player_balance == init_player_balance + init_contract_balance
    assert guess_number.currState() == 1

