import wiringpi2 as wp
from bbcon import BBCON

def main():
    wp.wiringPiSetupGpio()
    bbcon = BBCON()
    while True:
        bbcon.run_one_timestep()

if __name__ == "__main__":
    main()