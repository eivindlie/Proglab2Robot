import robodemo

from motors import Motors

def main():
    robodemo.random_step(Motors())

if __name__ == "__main__":
    main()