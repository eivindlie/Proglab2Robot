import wiringpi2 as wp
from bbcon import BBCON
from behaviors.run_forward import RunForward
from behaviors.avoid_walls import AvoidWalls
from behaviors.stand_still import StandStill
from behaviors.line_follower import LineFollower

def main():
    wp.wiringPiSetupGpio()
    bbcon = BBCON()

    #run_forward = RunForward(bbcon, 1, [])
    #bbcon.add_behavior(run_forward)
    #bbcon.activate_behavior(run_forward)

    #avoid_walls = AvoidWalls(bbcon, 1, [bbcon.sensobs['distance'], bbcon.sensobs['proximity']])
    #bbcon.add_behavior(avoid_walls)
    #bbcon.activate_behavior(avoid_walls)

    #stand_still = StandStill(bbcon, 1, [])
    #bbcon.add_behavior(stand_still)
    #bbcon.activate_behavior(stand_still)

    line_follower = LineFollower(bbcon, 1, [bbcon.sensobs['line_pos']])
    bbcon.add_behavior(line_follower)
    bbcon.activate_behavior(line_follower)

    while True:
        bbcon.run_one_timestep()

if __name__ == "__main__":
    main()