import sys
import os

pwd = os.getcwd()
sys.path.append(pwd)

if __name__ == "__main__":
    from pygarth import __main__

    __main__.main()
