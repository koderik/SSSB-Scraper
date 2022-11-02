import scanner
import sssbdata
import timeseries
import time
import sys

def main():
  
    while True:
        df = scanner.scan()
        df.to_csv("sssb.csv", index=False)
        time_series = timeseries.update_time()
        
        for remaining in range(61, 0, -1):
            sys.stdout.write("\r")
            sys.stdout.write("{:2d} seconds remaining.".format(remaining)) 
            sys.stdout.flush()
            time.sleep(1)

if __name__ == "__main__":
    main()