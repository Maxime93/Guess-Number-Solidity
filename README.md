# https://www.youtube.com/watch?v=yJQJ7pw_9C0

Lean about brownie, and connecting it to Ganache.
`pip install brownie-eth`
`npm install -g ganach-cli`

Ad a new network: `brownie networks add development local host=HTTP://127.0.0.1:7545 cmd=ganache`
Set it to default in brownie-config.yml:
```
networks:
    default:local
```

Then double check with `brownie console` and `network.account`. Should see the same as ganache UI.

Then we transfer some eth from one account to another using brownie `accounts[1].transfer(accounts[0], '10 ether')`

# https://www.youtube.com/watch?v=rDQRFuWVQpQ&list=PLFPZ8ai7J-iRa9eb1qTuepB1qaMYfhcWn&index=7

Now we are going to compile and deploy a smart contract (guess_number/contracts).
Compile: `brownie compile GuessNumber`
Deploy:
```
brownie console
GuessNumber.deploy(9, {'from':accounts[0],'value':'10 ether'})
# At that point a contract is deployed
GuessNumber # returns the contract address in a list.
GuessNumber[0].getBalance() # Balance
GuessNumber[0].play(7, accounts[3],{'from': accounts[3], 'value':'1 ether'}) # Does not work because we do not pay enough.
GuessNumber[0].play(9, accounts[3],{'from': accounts[3], 'value':'10 ether'}) # Works and we won.

```

# https://www.youtube.com/watch?v=lJd8-TLpAtY&list=PLFPZ8ai7J-iRa9eb1qTuepB1qaMYfhcWn&index=8

Now we create a script for the deployment. Writing `deploy_guess_number.py`.
We still need to compile `brownie compile GuessNumber.sol` before running the script.
We run like such `brownie run deploy_guess_number.py`

```
brownie console
GuessNumber # []
GuessNumber[0].getBalance() # error
GuessNumber.getBalance() # error
# We do not have the reference of the contract in the blockchain in the cli

GuessNumber.at('0xbfB5cbB31Ae0dC543FE424c812f52CFcefBDCA21') # We link with the address of the contract
GuessNumber.at('0xbfB5cbB31Ae0dC543FE424c812f52CFcefBDCA21').getBalance() # 10000000000000000000

GuessNumber.at('0xbfB5cbB31Ae0dC543FE424c812f52CFcefBDCA21').play(7, accounts[3],{'from': accounts[3], 'value':'10 ether'}) # Played and lost

GuessNumber.at('0xbfB5cbB31Ae0dC543FE424c812f52CFcefBDCA21').getBalance() # 20000000000000000000
GuessNumber.at('0xbfB5cbB31Ae0dC543FE424c812f52CFcefBDCA21').play(9, accounts[3],{'from': accounts[3], 'value':'10 ether'}) # Played and won
```