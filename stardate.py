import time;
import math
from dateutil.parser import parse
from datetime import datetime
import sys
import argparse

class StarDate(object):
    now = True
    verbose = False
    date = None
    
    def __init__(self):
        if(self.verbose):
            print("---Initializing---")

    def getStardate(self):
        self.now = datetime.now()
        stardateOrigin = parse("1987-07-15T00:00:00-00:00").timestamp()
        stardateToday = self.now.timestamp()
        
        if(self.verbose):
        	print("Start Date : " + stardateToday.strftime('%Y-%m-%d %H:%M:%S'))
        	print("Origin Date : " + stardateOrigin.strftime('%Y-%m-%d %H:%M:%S'))
        	print("---------------------")
        	
        if(self.verbose):
        	year = self.now.strftime('%Y')
        	month = self.now.strftime('%m')
        	day = self.now.strftime('%d')
        	hour = self.now.strftime('%H')
        	minutes = self.now.strftime('%M')
        	seconds = self.now.strftime('%S')
        	print("Year : " + year)
        	print("Month : " + month)
        	print("Day : " + day)
        	print("Hour : " + hour)
        	print("Minutes : " + minutes)
        	print("Seconds : " + seconds)
        	print("---------------------")
        	
        stardate =  stardateToday - stardateOrigin
        stardate = stardate / (60.0 * 60.0 * 24.0 * 0.036525)
        stardate = math.floor(stardate + 410000.0)
        stardate = stardate / 10.0
        
        print(stardate)
        
        if(self.verbose):
        	print("Selection Date - Origin Date = " + stardate)
        	print("---------------------")
        	
        	print("Previous Value / (60.0 * 60.0 * 24.0 * 0.036525) = " + stardate)
        	print("---------------------")
        	
        	print("Floor(Previous Value + 410000.0) = " + stardate)
        	print("---------------------")
        	
        	print("Previous Value / 10.0 = " + stardate)
        	print("---------------------")
       
    def main(self):
        try:
        	parser = argparse.ArgumentParser()
        	parser.add_argument('-n', '--now', help='useful if you want the star date for the current date(now).', action="store_true")
        	parser.add_argument('-v', '--verbose', help='if you want to see more variables and the calculation process', action="store_true", default=True)
        	parser.add_argument('-d', '--date', help='Enter the date to convert to stardate, format YYYY-MM-DD', type=str)
        	args = parser.parse_args()
        	
        	self.now = args.now
        	self.verbose = args.verbose
        	self.date = args.date
        	
        	if(self.verbose):
        		print("Now : " + now)
        		print("Verbose : " + verbose)
        		print("Date : " + date)
        		
        	self.getStardate()
        except:
        	e = sys.exc_info()[0]
        	#if(self.verbose):
        	print(e)

if __name__ == '__main__':
	starDate = StarDate()
	starDate.main()
 
