import wiringpi2 as wp
from bbcon import BBCON
from behaviors.run_forward import RunForward

def main():
    wp.wiringPiSetupGpio()
    bbcon = BBCON()
    run_forward = RunForward(bbcon, 1, [])
    bbcon.add_behavior(run_forward)
    bbcon.activate_behavior(run_forward)
    while True:
        bbcon.run_one_timestep()

if __name__ == "__main__":
    main()