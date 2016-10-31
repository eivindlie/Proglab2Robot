import wiringpi2 as wp
from bbcon import BBCON
from behaviors.run_forward import RunForward

def main():
    wp.wiringPiSetupGpio()
    bbcon = BBCON()
    bbcon.add_behavior(RunForward(bbcon, 1, []))
    while True:
        bbcon.run_one_timestep()

if __name__ == "__main__":
    main()