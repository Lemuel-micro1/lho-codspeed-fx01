"""fx01 fixture library. Deterministic, pure Python."""


def _clean(token):
    return token.strip().lower()


def parse_records(text):
    rows = []
    for line in text.splitlines():
        rows.append(tuple(_clean(t) for t in line.split(",")))
    return rows


def build_index(rows):
    index = {}
    for i, row in enumerate(rows):
        index.setdefault(_clean(row[0]), []).append(i)
    return index


def dedupe(ids):
    seen = set()
    out = []
    for x in ids:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out


def popcount(data):
    total = 0
    for b in data:
        total += bin(b).count("1")
    return total


def window_means(values, k):
    s = sum(values[:k])
    out = [s / k]
    for i in range(k, len(values)):
        s += values[i] - values[i - k]
        out.append(s / k)
    return out