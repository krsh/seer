import argparse

from utils.plot import plot
from utils.similarity import similarity


def arch(bin, wr):
    fbytes = [0] * 256

    with open(bin, "rb") as f:
        data = f.read()

    for d in data:
        if((d % 0x40) != 0):
            fbytes[d] += 1

    entries = [sum(fbytes[i:i+4]) for i in range(0, len(fbytes), 4)]
    me = max(entries)
    values = [int(100 * e/1.0/me) for e in entries]
    # print(values)
    if wr:
        plot(values)

    for s in similarity(values):
        print(f"{s['arch']}\t\t{s['val']}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--windrose", dest="windrose", default=False,
                        action="store_true", help="show windrose chart")
    parser.add_argument('filename', type=str, nargs=None,
                        help='binary to analyze')
    args = parser.parse_args()

    arch(args.filename, args.windrose)
