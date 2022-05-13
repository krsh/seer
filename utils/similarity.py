from scipy.spatial import distance

from .conf import *


SIMILARITY = [ARM32, ARM64, PPC32, PPC64,
              X86_64, I686, M68K, MIPS32, MIPS64, SH4]


def get_name(x):
    return [i for i, a in globals().items() if a == x][0]


def similarity(values):
    results = []
    for sim in SIMILARITY:
        val = int(100 * (1 - distance.cosine(values, sim)))
        results.append({"arch": get_name(sim), "val": val})

    return sorted(results, key=lambda d: d['val'], reverse=True)
