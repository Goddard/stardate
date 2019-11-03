import math
from dateutil.parser import parse
from datetime import datetime
import sys
import argparse
import time


class StarDate():
    verbose = False
    date = None
    stardate = None

    def __init__(self, date=None, verbose=False):
        if(self.verbose):
            print("---Initializing---")

        self.date = date
        self.verbose = verbose

    def setDate(self, date):
        self.date = date

    def to_seconds(self, date):
        return time.mktime(date.timetuple())

    def getStardate(self):
        if(self.date != None):
            stardateRequested = parse(self.date)
        else:
            stardateRequested = datetime.now()

        stardateOrigin = parse("1987-07-15T00:00:00-00:00")

        if(self.verbose):
            print("Start Date : " + stardateRequested.strftime('%Y-%m-%d %H:%M:%S'))
            print("Origin Date : " + stardateOrigin.strftime('%Y-%m-%d %H:%M:%S'))
            print("---------------------")

        if(self.verbose):
            year = stardateRequested.strftime('%Y')
            month = stardateRequested.strftime('%m')
            day = stardateRequested.strftime('%d')
            hour = stardateRequested.strftime('%H')
            minutes = stardateRequested.strftime('%M')
            seconds = stardateRequested.strftime('%S')
            print("Year : " + year)
            print("Month : " + month)
            print("Day : " + day)
            print("Hour : " + hour)
            print("Minutes : " + minutes)
            print("Seconds : " + seconds)
            print("---------------------")

        self.stardate = self.to_seconds(
            stardateRequested) - self.to_seconds(stardateOrigin)
        self.stardate = self.stardate / (60.0 * 60.0 * 24.0 * 0.036525)
        self.stardate = math.floor(self.stardate + 410000.0)
        self.stardate = self.stardate / 10.0

        if(self.verbose):
            print("Selection Date - Origin Date = " + str(self.stardate))
            print("---------------------")

            print("Previous Value / (60.0 * 60.0 * 24.0 * 0.036525) = " +
                  str(self.stardate))
            print("---------------------")

            print("Floor(Previous Value + 410000.0) = " + str(self.stardate))
            print("---------------------")

            print("Previous Value / 10.0 = " + str(self.stardate))
            print("---------------------")

        if(self.verbose):
            print()
            print("Stardate Final : " + str(self.stardate))

        return self.stardate

    def main(self):
        try:
            parser = argparse.ArgumentParser()
            parser.add_argument(
                '-v', '--verbose', help='if you want to see more variables and the calculation process', action='store_true')
            parser.add_argument(
                '-d', '--date', help='Enter the date to convert to stardate, format YYYY-MM-DD', metavar='D', type=str, default=None)
            args = parser.parse_args()

            self.verbose = args.verbose
            self.date = args.date

            if(self.verbose):
                print("Argument Verbose : " + str(self.verbose))
                if(self.date != None):
                    print("Argument Date : " + self.date)
                else:
                    print("Argument Date : " +
                          datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                    print()

            self.getStardate()

        except SystemExit:
            e = sys.exc_info()[0]
            # if(self.verbose):
            print(e)


if __name__ == '__main__':
    starDate = StarDate()
    starDate.main()
