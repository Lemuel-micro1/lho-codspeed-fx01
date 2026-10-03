from fxlib import core

TEXT = "\n".join(f" Vessel{i % 97} ,Port{i % 13}, {i} " for i in range(2000))
ROWS = core.parse_records(TEXT)
IDS = [(i * 7919) % 1500 for i in range(3000)]
DATA = bytes((i * 31) % 256 for i in range(20000))
VALUES = [float((i * 37) % 101) for i in range(20000)]


def test_parse(benchmark):
    benchmark(core.parse_records, TEXT)


def test_index(benchmark):
    benchmark(core.build_index, ROWS)


def test_dedupe(benchmark):
    benchmark(core.dedupe, IDS)


def test_popcount(benchmark):
    benchmark(core.popcount, DATA)


def test_window(benchmark):
    benchmark(core.window_means, VALUES, 50)