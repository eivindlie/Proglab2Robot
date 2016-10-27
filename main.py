import robodemo

from motors import Motors

def main():
    while True:
        robodemo.random_step(Motors())

if __name__ == "__main__":
    main()