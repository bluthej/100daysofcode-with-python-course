from datetime import timedelta
from time import sleep

STUDY_TIME = 25  # in minutes


def main():
    one_sec = timedelta(seconds=1)
    time_left = timedelta(minutes=STUDY_TIME)
    zero = timedelta(minutes=0)

    input(f"Press enter to start studying for {STUDY_TIME} minutes")

    while time_left > zero:
        print(time_left, end="\r")
        time_left -= one_sec
        sleep(1)
    print(zero)

    print("Time to take a break!")


if __name__ == "__main__":
    main()
