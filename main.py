Points=0
Wins =0
Draws=0
Loses=0
class Day:
  def __init__(self,Date,PointsWon,PointsLost,cleansheet,):
    self.Date=Date
    self.PointsWon=PointsWon
    self.PointsLost=PointsLost
    PointsLost=self.PointsLost
    global result
    result=self.result
    self.cleansheet=cleansheet
    self.result=PointsWon-PointsLost
  
  if result>= 1:
    Points+=3
    Wins+=1
  elif result == 0:
    Draws+=1
    Points+=1
  else:
    Loses+=1
    Points+=0
  def report(self):
    TheDay=(self.Date,self.PointsWon,self.PointsLost,cleansheet,result)

