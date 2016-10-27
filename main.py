import robodemo
import wiringpi2 as wp

from motors import Motors

def main():
    wp.wiringPiSetupGpio()
    robodemo.dancer()

if __name__ == "__main__":
    main()