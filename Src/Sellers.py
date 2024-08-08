import Block
import random
import os, binascii     # To generate random auction IDs


class Sellers:
    def __init__(self, id, location):
        self.id = id
        self.location = location
        self.auctionId = []
        self.quantity = []
        self.LinkOfBlocks = Block.LinkOfBlocks()

    def createAuction(self):
        for x in self.quantity:
            roomid = binascii.b2a_hex(os.urandom(4)).decode('utf-8')
            self.auctionId.append(roomid)

    def genBlock(self, price, amount, discount):
        self.LinkOfBlocks.head.set_price(price)
        self.LinkOfBlocks.head.set_amount(amount)
        self.LinkOfBlocks.head.set_discount(discount)
        self.LinkOfBlocks.head.set_Object("Block")

    def addBlock(self, price, amount, discount):
        block = Block.AuctionBlock()
        block.set_price(price)
        block.set_amount(amount)
        block.set_Object = (
            "Block " + str(price) + " " + str(amount) + " " + str(discount)
        )  # For debugging mostly
        self.LinkOfBlocks.add(block)
        block.set_discount(discount + block.prev().get_discount())
    
    def __repr__(self) -> str:
        return f"{self.id} {self.location}"
