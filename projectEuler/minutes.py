import sys


def Hours(min):

    min = int(sys.argv[1])

    m = min % 60

    h = min // 60

    return m, h


def main():

    try:
        if min >= 0:
            h, m = Hours(min)
            print("[] H,[] M".format(h, m))
        else:
            raise ValueError
    except ValueError:
        print("ValueError:Input number cannot be negative")


if __name__ == '__main__':

    if len(sys.argv) > 1:

        Hours(min)

    else:

        sys.exit(-1)

sys.exit(0)

