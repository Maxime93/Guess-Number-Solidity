pragma solidity ^0.8.1;

contract GuessNumber {

    address payable player;
    enum State {OPEN, COMPLETE}
    State public currState;
    uint private secretNumber;
    uint public balance;

    constructor (uint _secretNumber) payable {
        require(msg.value == 10*10**18, 'Contract needs to be funded with exactly 10 eth');
        secretNumber = _secretNumber;
        currState = State.OPEN;
        balance = balance + msg.value;
    }

    function getBalance() public view returns (uint) {
        return address(this).balance;
    }

    function play(uint guessedNumber, address _player) external payable {
        require(msg.value == 10*10**18, 'You must pay exactly 10 eth to play');
        require(currState == State.OPEN);
        player = payable(_player);
        balance = balance + msg.value;
        if (guessedNumber == secretNumber) {
            // This is before the transfer because happening in the same block
            player.transfer(address(this).balance);
            currState = State.COMPLETE;
        }
    }
}
