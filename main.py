import robodemo

from motors import Motors

def main():
    m = Motors()
    while True:
        robodemo.random_step(m)

if __name__ == "__main__":
    main()