from sqlite3 import Time
import TimeDomainHRV


def main():
    myHRV = TimeDomainHRV()
    myHRV.run()

if __name__ == "__main__":
    main()