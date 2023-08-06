import mmh3


def f(j: int, key: int) -> int:
    raku = [0xB76D5EED, 0xEE281300, 0x85BCAE01, 0x4B387AF7]
    lo, hi = key & 0xFF, (key & 0xFF00) // 0x100
    hash_key = f"{chr(lo)}{chr(hi)}".encode("latin_1")
    return mmh3.hash(hash_key, raku[j], signed=False)


def loop_hi_lo_init(v):
    lo = v & 0xFFFFFFFF
    hi = v & 0xFFFFFFFF00000000
    return hi, lo


def feis(m: int) -> int:
    c = fe(4, 65535, 65536, m)
    return c if c < 0xFFFFFFFF else fe(4, 65535, 65536, c)


def fe(r: int, a: int, b: int, m: int) -> int:
    right, left = divmod(m, a)
    return fe_loop(r, a, b, 1, left, right)


def fe_loop(r: int, a: int, b: int, j: int, ell: int, arr: int):
    if j > r:
        if r % 2 != 0 or arr == a:
            return (a * arr) + ell
        return (a * ell) + arr
    eff = f(j - 1, arr)
    tmp = ell + eff
    if j % 2 != 0:
        tmp = tmp % a
    else:
        tmp = tmp % b
    return fe_loop(r, a, b, j + 1, arr, tmp)


def fen_loop(a: int, b: int, j: int, ell: int, arr: int) -> int:
    if j < 1:
        return (a * arr) + ell
    eff = f(j - 1, ell)
    use_value = b if j % 2 == 0 else a
    tmp = (arr + use_value - (eff % use_value)) % use_value
    return fen_loop(a, b, j - 1, tmp, ell)


def fen(r: int, a: int, b: int, m: int) -> int:
    ale, ahh = divmod(m, a)
    if r % 2 == 1:
        ale, ahh = ahh, ale
    return fen_loop(a, b, r, ale, ahh)


def tail(v: int) -> int:
    c = fen(4, 65535, 65536, v)
    return c if c < 0xFFFFFFFF else fen(4, 65535, 65536, c)


def fein(pyn: int) -> int:
    hi, lo = loop_hi_lo_init(pyn)
    if 0x10000 <= pyn <= 0xFFFFFFFF:
        return 0x10000 + feis(pyn - 0x10000)
    if 0x100000000 <= pyn <= 0xFFFFFFFFFFFFFFFF:
        return hi | fein(lo)
    return pyn


def fynd(cry: int) -> int:
    hi, lo = loop_hi_lo_init(cry)
    if 0x10000 <= cry <= 0xFFFFFFFF:
        return 0x10000 + tail(cry - 0x10000)
    if 0x100000000 <= cry <= 0xFFFFFFFFFFFFFFFF:
        return hi | fynd(lo)
    return cry
