import hashlib as h
from dataclasses import dataclass
import random
from datetime import datetime

TRANSACTION_JOURNAL = []
NUM_ZEROES = 4


@dataclass
class Block:
    def __init__(self, _data, _prev = None):
        self.prev = _prev

        self.data = _data
        self.ver = 1
        self.My_walet = Wallet()
        self.My_walet.amount = 0
        self.My_walet.owner = _data

    def get_hash(self):
        __data = str([self.prev, self.data, self.My_walet.amount, self.ver])

        if self.prev:
            __prev_hash = self.prev.get_hash()
            __data += str(__prev_hash)
        return h.sha256(__data.encode()).hexdigest()

    def __str__(self):
        if self.prev:
            return f"prev_hash = {self.prev.get_hash()},\n hash = {self.get_hash()},\n Name = {self.data}\n money amount = {self.My_walet.amount}\n"

        return f"hash = {self.get_hash()}, \n data = {self.data}\n nonce = {self.My_walet.amount}\n"

    def mine(self):
        while (self.get_hash()[0:NUM_ZEROES] != '0' * NUM_ZEROES) or (self.get_hash()[-1] != '1'):
            self.My_walet.amount += 1

class Blockchain:
    def __init__(self):
        self.blocks = []
        self.blocks.append(Block(_data="0"*64))

    def append(self, _data):
        self.blocks.append(Block(_prev=self.blocks[-1], _data=_data))
        self.blocks[-1].mine()

    def transactions(self):
        T = Transaction()
        i = 1
        while(i != (len(self.blocks)-1)):
            T.transaction_process(self.blocks[i].My_walet, self.blocks[i+1].My_walet)
            i+=1

    def __str__(self):
        for b in self.blocks:
            print(b.__str__())

class Wallet:
    def init(self, owner, amount):
        self.owner = owner
        self.amount = amount

class Transaction:

    def generate_transaction_data(self, sender, receiver, amount: int) -> dict:
        date = None
        date = datetime.now()
        if(date != None):
            TRANSACTION_JOURNAL.append({'sender': sender,'receiver': receiver,'amount': amount, 'date': date})
    
    def transaction_process(self,wallet1 : Wallet, wallet2 : Wallet):
        amount = random.randint(0, wallet1.amount)
        wallet1.amount -= amount
        wallet2.amount += amount
        self.generate_transaction_data(wallet1.owner, wallet2.owner, amount)
        

if __name__ == '__main__':
    b = Blockchain()
    b.append(_data="Алиса")
    b.append(_data="Николя")
    b.append(_data="Петр")
    b.append(_data="Джорджия")
    b.append(_data='Игорь Владимирович')

    b.transactions()
    for i in range(len(TRANSACTION_JOURNAL)):
        print(TRANSACTION_JOURNAL[i],'\n')
    print('\n\n')

    b.__str__()