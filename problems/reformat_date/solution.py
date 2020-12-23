from datetime import datetime

class Solution:
    def reformatDate(self, date: str) -> str:
        # trim day and get day
        # %b for shortened month
               
        date=date.split(' ')
        date[0] = "{:02d}".format(int(date[0][:-2]))
        
        dt = datetime.strptime(" ".join(date), "%d %b %Y")
        return dt.strftime("%Y-%m-%d")
        