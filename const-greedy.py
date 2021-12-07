import pandas as pd
from pprint import pprint
"""

"""

class Greedy():
    a = 1
    data = None
    df = None
    teamWork = {}
    teamCount = 0
    maxDayPerTeam = 30*3
    
    def __init__(self):
        pass

    def load(self, fname):
        self.df = pd.read_csv(fname)
        return self
    
    def loadSet(self, fname):
        self.load(fname)
        self.data = self.df
        return self

    # df compatible data
    def setData(self, data):
        self.data = data
        return self
    
    def addWorkToTeam(self, key, data):
        self.teamWork[key]['works'].append(data)
        current = self.teamWork[key]['totalDay']
        self.teamWork[key]['totalDay'] = current + data['dur']
        return self

    # df compatible data
    def addTeam(self, key, data):
        self.teamWork[key] = data
        return self

    def isFeasible(self, idx, data):
        """
        fdata = {
            "team": self.teamCount,
            "work": d,
        }
        """
        try:
            c1 = not len(self.teamWork.keys()) < 1
            c2 = self.maxDayPerTeam >= self.teamWork[idx]['totalDay']
        except:
            return False
        return c1 & c2
    
    def doGreedy(self):
        res = {}
        # for i,d in enumerate(self.data):
        for i,d in self.data.iterrows():
            print(i)
            # print(d)
            fdata = {
                "team": self.teamCount,
                "work": d,
            }
            teamidx = str(self.teamCount)
            if self.isFeasible(teamidx, fdata):
                # add to existing teamwork
                self.addWorkToTeam(teamidx, d)
            else:
                # add new data to teamwork
                idx = str(self.teamCount+1)
                self.addTeam(idx, {
                    "works":[],
                    "totalDay": 0,
                })
                self.addWorkToTeam(idx, d)
                self.teamCount += 1
            # print(self.teamWork)
        return res

g = Greedy()
result = g.loadSet("const-greedy.csv").doGreedy()
print(g.data)
pprint(g.teamWork)
print(result)