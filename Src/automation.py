from main import start
import numpy as np
import matplotlib.pyplot as plt
import yaml
# Define the config file here
TEST_NAME = "test"
CONFIG = {
  "run-id": None,                                # Files saved with this prefix
  "seed": 534,
  "sellers": 8,
  "bidders": 4,
  "resource-usage": 0.5,                   
  "min-block": 1,
  "max-block": 1,
  "distance-limit":None,
  "distance-penalty":None,
  "radius": 5,
  "slotsize": 2,
  "end-threshold": 2
}

# Can iterate over these parameters, will use the one with length > 1, order right to left
DISTANCE_PENALTY = [2]
DISTANCE_LIMIT = np.arange(7.1, 12, 1).tolist()
RESOURCE_USAGE = [0.5]

def saveConfig():
    # Save config for each test run, omitted for now
    #with open(CONFIG["run-id"],"w") as f:
        #yaml.dump(CONFIG, f, sort_keys=False)
    with open("config.yaml","w") as f:
        yaml.dump(CONFIG, f, sort_keys=False)

# Get fairness value for hard cap on distance
def processMatchmaking(combos):
    temp = []
    for combo in combos:
        if combo['avgDistance'] < CONFIG['distance-limit']:
            temp.append(combo)
    #output = sorted(temp, key=lambda i:i['fairness'], reverse=True)
    output = sorted(temp, key=lambda i:i['avgDistance'], reverse=True)
    if len(output) == 0: return 0
    
    return temp[0]['avgDistance']


def processAuction(auctions):
    ""

def plotGraph(inputList):
    ""
    plt.xlabel('Distance Limit')
    plt.ylabel('Average Distance')
    plt.scatter(*zip(*inputList), s=40)
    plt.show()

if __name__ == "__main__":
    runIndex = 1
    singleRun = False
    variable = []
    # Initial setup to identify which to iterate over, duplicates the others to make all lists equal length
    if len(DISTANCE_PENALTY) > 1:
        while len(RESOURCE_USAGE) < len(DISTANCE_PENALTY) and len(DISTANCE_LIMIT) < len(DISTANCE_PENALTY):
            RESOURCE_USAGE.append(RESOURCE_USAGE[0])
            DISTANCE_LIMIT.append(DISTANCE_LIMIT[0])
    elif len(DISTANCE_LIMIT) > 1:
        while len(RESOURCE_USAGE) < len(DISTANCE_LIMIT) and len(DISTANCE_PENALTY) < len(DISTANCE_LIMIT):
            RESOURCE_USAGE.append(RESOURCE_USAGE[0])
            DISTANCE_PENALTY.append(DISTANCE_PENALTY[0])
    elif len(RESOURCE_USAGE) > 1:
        while len(DISTANCE_PENALTY) < len(RESOURCE_USAGE) and len(DISTANCE_LIMIT) < len(RESOURCE_USAGE):
            DISTANCE_LIMIT.append(DISTANCE_LIMIT[0])
            DISTANCE_PENALTY.append(DISTANCE_PENALTY[0])
    else:
        singleRun = True
    
    if singleRun:
        CONFIG['run-id'] = TEST_NAME
        CONFIG['resource-usage'] = RESOURCE_USAGE[0]
        CONFIG['distance-limit'] = DISTANCE_LIMIT[0]
        CONFIG['distance-penalty'] = DISTANCE_PENALTY[0]
        saveConfig()
        start(True)
        exit()
    
    matchmakingResults = []
    auctionResults = []

    while len(RESOURCE_USAGE) > 0:
        CONFIG['run-id'] = TEST_NAME + '-' + str(runIndex)
        CONFIG['resource-usage'] = RESOURCE_USAGE.pop()
        CONFIG['distance-limit'] = DISTANCE_LIMIT.pop()
        CONFIG['distance-penalty'] = DISTANCE_PENALTY.pop()
        saveConfig()
        mmr, ar = start(False)
        matchmakingResults.append((CONFIG['distance-limit'], processMatchmaking(mmr)))
        runIndex += 1

    plotGraph(matchmakingResults)