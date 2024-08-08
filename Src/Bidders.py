import random
import Behaviour
import math
from itertools import combinations


class Bidders:
    def __init__(self, id, location, needs, maxRound, behaviour, distanceLimit, distancePenalty):
        self.id = id
        self.location = location
        self.needs = needs
        self.maxRound = maxRound
        self.behaviour = behaviour
        self.distanceLimit = distanceLimit
        self.distancePenalty = distancePenalty
        self.marketPrice = 0
        #self.stopBid = 0
        #self.marketPriceFactor = self.behaviour["marketPriceFactor"]
        self.wonItems = 0
        self.currentRound = 0
        self.bidIndex = 0

    def generateBids(self, inputAuction):
        "Generate a bid we should place"
        bids = []
        for auction in inputAuction:
            price = round(auction['top_bid'] + self.marketPrice * self.behaviour.marketPriceFactor * self.behaviour.aggressiveness * auction['quantity'],2)
            bids.append({'id':auction['id'], 'user':self.id, 'top_bid':price})

        return bids

    def evalAuction(self, inputAuction, remainingDemand):
        "Evaluate if we want to bid on the auction or not"
        distancePercentage = self.distanceCalc(inputAuction['location'])/self.distanceLimit
        randomFactor = self.behaviour.adaptiveBidLikelyhoood(self.currentRound, self.maxRound, self.bidIndex, remainingDemand/self.needs, distancePercentage)
        if(inputAuction["top_bid"] > inputAuction["quantity"] * self.marketPrice * self.behaviour.stopBid):
            return False
        elif(randomFactor >= random.uniform(0,1)):
            return True
        return False

    def bidUpdate(self, inputAuction):
        self.bidIndex += 1
        satisfiedNeed = 0
        remainingDemand = 0

        # Place auctions which we want to bid on here
        validAuctions = []
        
        # Find out how many auctions we are winning
        for auction in inputAuction:
            if auction['user'] == self.id:
                satisfiedNeed += auction['quantity']
            else:
                validAuctions.append(auction)
        
        remainingDemand = self.needs - satisfiedNeed - self.wonItems
        # Evaluate if we should bid on any auctions
        for i in range(len(validAuctions)-1, -1, -1):
            if not self.evalAuction(validAuctions[i], remainingDemand):
                validAuctions.pop(i)
        
        # Dont need to do any processing for bids if we dont need anything more currently
        # or if we have no auctions which we want to bid on
        if remainingDemand <= 0 or len(validAuctions) == 0:
            return []

        # Check if we need to bid on multiple auctions to satisfy demand
        # or if we can exclude some of them (to avoid bidding more than needed)
        if len(validAuctions) > 1:
            validAuctions = self.auctionCombos(validAuctions, remainingDemand)
        
        bids = self.generateBids(validAuctions)
        return bids
    
    #Generates and checks combinations of auctions for the best combination to fulfill demand
    def auctionCombos(self, auctions, quantity):
        combos = []
        quantityDifferences = []
        i = 1
        while i <= len(auctions):
            temp = list(combinations(auctions, i))
            i += 1
            for combo in temp:
                combos.append(combo)
        
        for combo in combos:
            temp = 0
            for auction in combo:
                temp += auction['quantity']
            quantityDifferences.append(quantity - temp)
        
        # Find the combination which yields the best demand satisfaction
        # preferring fulfilled demand (negative difference)
        bestIndex = 0
        bestDifference = quantityDifferences[0]
        for i in range(len(quantityDifferences)):
            if bestDifference < 0 and quantityDifferences[i] > 0:
                continue
            elif quantityDifferences[i] < 0 and bestDifference > 0:
                bestIndex = i
                bestDifference = quantityDifferences[i]
            elif abs(bestDifference) > abs(quantityDifferences[i]):
                bestIndex = i
                bestDifference = quantityDifferences[i]
        
        return combos[bestIndex]
    
    def distanceCalc(self, location):
        distance = math.sqrt((location[0]-self.location[0])**2 + (location[1]-self.location[1])**2)
        return distance

    def updateWonItems(self, wonItems):
        self.wonItems += wonItems
    
    def newRound(self):
        self.currentRound += 1
        self.bidIndex = 0
        self.behaviour.updateVariables(self.currentRound, self.maxRound)
    
    def setMarketprice(self, price):
        self.marketPrice = price
