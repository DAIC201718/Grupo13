import gps
import time

latitude = 0.00
longitude = 0.00 
def main(): 
    coordinate = {}

    # Listen on port 2947 (gpsd) of localhost
    session = gps.gps("localhost", "2948")
    session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
 
    while True:
        try:
            report = session.next()
            # Wait for a 'TPV' report and display the current time
            # To see all report data, uncomment the line below
            #print report
            if report['class'] == 'TPV':
               if hasattr(report, 'lat'):
                    lati = report.lat
                    coordinate['latitude'] = lati
                    setLat(lati)
               if hasattr(report, 'lon'):
                   long = report.lon
                   coordinate['longitude'] = long
                   setLong(long)
               return coordinate
        except KeyError:
            pass
        except KeyboardInterrupt:
            quit()
        except StopIteration:
            session = None
            print ("GPSD has terminated")
        #time.sleep(5)
def setLat(lat):
    global latitude
    latitude = lat
def getLat():
    global latitude
    return latitude

def setLong(long):
    global longitude
    longitude = long
def getLong():
    global longitude
    return longitude

#while True:
coordinate = main()
#latitude = coordinate['latitude']
#longitude = coordinate['longitude']
#    print coordinate['latitude']
#    print coordinate['longitude']

