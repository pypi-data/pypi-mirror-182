import re
from typing import List, T, Collection

from urbitob import ob

PREFIXES = """\
dozmarbinwansamlitsighidfidlissogdirwacsabwissib\
rigsoldopmodfoglidhopdardorlorhodfolrintogsilmir\
holpaslacrovlivdalsatlibtabhanticpidtorbolfosdot\
losdilforpilramtirwintadbicdifrocwidbisdasmidlop\
rilnardapmolsanlocnovsitnidtipsicropwitnatpanmin\
ritpodmottamtolsavposnapnopsomfinfonbanmorworsip\
ronnorbotwicsocwatdolmagpicdavbidbaltimtasmallig\
sivtagpadsaldivdactansidfabtarmonranniswolmispal\
lasdismaprabtobrollatlonnodnavfignomnibpagsopral\
bilhaddocridmocpacravripfaltodtiltinhapmicfanpat\
taclabmogsimsonpinlomrictapfirhasbosbatpochactid\
havsaplindibhosdabbitbarracparloddosbortochilmac\
tomdigfilfasmithobharmighinradmashalraglagfadtop\
mophabnilnosmilfopfamdatnoldinhatnacrisfotribhoc\
nimlarfitwalrapsarnalmoslandondanladdovrivbacpol\
laptalpitnambonrostonfodponsovnocsorlavmatmipfip\
"""
SUFFIXES = """\
zodnecbudwessevpersutletfulpensytdurwepserwylsun\
rypsyxdyrnuphebpeglupdepdysputlughecryttyvsydnex\
lunmeplutseppesdelsulpedtemledtulmetwenbynhexfeb\
pyldulhetmevruttylwydtepbesdexsefwycburderneppur\
rysrebdennutsubpetrulsynregtydsupsemwynrecmegnet\
secmulnymtevwebsummutnyxrextebfushepbenmuswyxsym\
selrucdecwexsyrwetdylmynmesdetbetbeltuxtugmyrpel\
syptermebsetdutdegtexsurfeltudnuxruxrenwytnubmed\
lytdusnebrumtynseglyxpunresredfunrevrefmectedrus\
bexlebduxrynnumpyxrygryxfeptyrtustyclegnemfermer\
tenlusnussyltecmexpubrymtucfyllepdebbermughuttun\
bylsudpemdevlurdefbusbeprunmelpexdytbyttyplevmyl\
wedducfurfexnulluclennerlexrupnedlecrydlydfenwel\
nydhusrelrudneshesfetdesretdunlernyrsebhulryllud\
remlysfynwerrycsugnysnyllyndyndemluxfedsedbecmun\
lyrtesmudnytbyrsenwegfyrmurtelreptegpecnelnevfes\
"""

prefix = {i: PREFIXES[i * 3 : i * 3 + 3] for i in range(256)}
suffix = {i: SUFFIXES[i * 3 : i * 3 + 3] for i in range(256)}
iprefix = {v: k for k, v in prefix.items()}
isuffix = {v: k for k, v in suffix.items()}


def _dec_to_bin(idx: int) -> str:
    return f"{idx:08b}"


def _dec_to_hex(dec: int) -> str:
    return f"{dec:02x}"


def _bex(n: int) -> int:
    return 2**n


def _rsh(a: int, b: int, c: int) -> int:
    return c // (_bex(_bex(a) * b))


def _met(a: int, b: int, c: int = 0) -> int:
    if b == 0:
        return c
    return _met(a, _rsh(a, 1, b), c + 1)


def _end(a: int, b: int, c: int) -> int:
    return c % (_bex(_bex(a) * b))


def _patp_loop(dyy: int, tsxz: int, timp: int, trep: str) -> str:
    if timp == dyy:
        return trep
    log = _end(4, 1, tsxz)
    pre = prefix.get(_rsh(3, 1, log) // 1)
    suf = suffix.get(_end(3, 1, log) // 1)
    etc = "-" if timp % 4 != 0 else "--" if timp != 0 else ""
    res = pre + suf + etc + trep
    return _patp_loop(dyy, _rsh(4, 1, tsxz), timp + 1, res)


def _rev_chunk(s: Collection[T], size: int) -> Collection[Collection[T]]:
    rem = len(s) % size
    if rem != 0:
        yield s[:rem]
        s = s[rem:]
    for i in range(0, len(s), size):
        yield s[i : i + size]


def _pat_to_syls(name: str) -> List[str]:
    name_partition_pattern = ".{1,3}"
    remove_chars_pattern = re.compile(r"[\^~-]")
    normalized_name = remove_chars_pattern.sub("", name)
    partition_pattern = re.compile(name_partition_pattern)
    return partition_pattern.findall(normalized_name)


def patp(v: int) -> str:
    """
    Convert a number to a @p-encoded string.
    :param v:
    :return:
    """
    sxz = ob.fein(v)
    dyy = _met(4, sxz, 0)
    dyx = _met(3, sxz, 0)
    p = "~"
    if dyx <= 1:
        p += suffix.get(sxz // 1)
    else:
        p += _patp_loop(dyy, sxz, 0, "")
    return p


def patq(v: int) -> str:
    """
    Convert a number to a @q-encoded string.
    :param v:
    :return:
    """
    hex_str = _dec_to_hex(v)

    if len(hex_str) == 2:
        return "~" + suffix.get(int(hex_str, 16))

    ret = []
    for chunk in _rev_chunk(hex_str, 4):
        chunk = str(chunk).zfill(4)
        pre = chunk[:2]
        suf = chunk[2:]
        ret.append(prefix.get(int(pre, 16)) + suffix.get(int(suf, 16)))
    return "~" + "-".join(ret)


def _pat_to_hex(name: str) -> str:
    syls = _pat_to_syls(name)
    if len(syls) == 1:
        return _dec_to_hex(isuffix.get(syls[0]))
    ret = ""
    for i in range(0, len(syls), 2):
        ret += _dec_to_hex(iprefix.get(syls[i])) + _dec_to_hex(isuffix.get(syls[i + 1]))
    return ret


def patp_to_hex(name: str) -> str:
    """
    Convert a @p-encoded string to a hex-encoded string.
    :param name:
    :return:
    """
    if not is_valid_pat(name):
        raise ValueError(f"Invalid @p {name}")
    hex_value = _pat_to_hex(name)
    v = ob.fynd(int(hex_value, 16))
    hex_v = f"{v:x}"
    return f"0{hex_v}" if len(hex_v) % 2 != 0 else hex_v


def patq_to_hex(name: str) -> str:
    """
    Convert a @q-encoded string to a hex-encoded string.
    :param name:
    :return:
    """
    if not is_valid_pat(name):
        raise ValueError(f"Invalid @p {name}")
    return "00" if len(name) == 0 else _pat_to_hex(name)


def is_valid_pat(who: str) -> bool:
    """
    Weakly check if a string is a valid @p or @q value
    :param who:
    :return:
    """
    if len(who) < 4 or who[0] != "~":
        return False
    syls = _pat_to_syls(who)

    if len(syls) == 1:
        return syls[0] in isuffix
    if len(syls) % 2 != 0:
        return False

    for i in range(0, len(syls), 2):
        if syls[i] not in iprefix or syls[i + 1] not in isuffix:
            return False
    return True


def is_valid_patp(s: str) -> bool:
    """
    Validate a @p string.
    :param s:
    :return:
    """
    try:
        v = patp_to_num(s)
    except ValueError:
        return False
    return is_valid_pat(s) and s == patp(v)


def is_valid_patq(s: str) -> bool:
    """
    Validate a @q string.
    :param s:
    :return:
    """
    try:
        v = patq_to_num(s)
    except ValueError:
        return False
    p = patq(v)
    return is_valid_pat(s) and eq_patq(s, p)


def eq_patq(p: str, q: str) -> bool:
    """
    Equality comparison on @q values.
    :param p:
    :param q:
    :return:
    """
    return patq_to_hex(p).lstrip("0") == patq_to_hex(q).lstrip("0")


def patp_to_num(who: str) -> int:
    """
    Convert a @p-encoded string to a number
    :param who:
    :return:
    """
    hex_str = patp_to_hex(who)
    return int(hex_str, 16)


def patq_to_num(who: str) -> int:
    """
    Convert a @q-encoded string to a number
    :param who:
    :return:
    """
    hex_str = patq_to_hex(who)
    return int(hex_str, 16)


def hex_to_patq(hex_str: str) -> str:
    """
    Convert a hex-encoded string to a @p-encoded string
    :param hex_str: hex
    :return: @p string
    """
    return patq(int(hex_str, 16))


def hex_to_patp(hex_str: str) -> str:
    """
    Convert a hex-encoded string to a @p-encoded string
    :param hex_str: hex
    :return: @p string
    """

    return patp(int(hex_str, 16))


def clan(who: str) -> str:
    """
    Determine the ship class of a @p value.
    :param who: @p
    :return:
    """
    p = patp_to_num(who)
    wid = _met(3, p)

    if wid <= 1:
        return "galaxy"
    elif wid <= 2:
        return "star"
    elif wid <= 4:
        return "planet"
    elif wid <= 8:
        return "moon"
    else:
        return "comet"


def sein(who: str) -> str:
    """
    Determine the parent of a @p value
    :param who: @p
    :return:
    """
    p = patp_to_num(who)
    c = clan(who)

    if c == "galaxy":
        res = p
    elif c == "star":
        res = _end(3, 1, p)
    elif c == "planet":
        res = _end(4, 1, p)
    elif c == "moon":
        res = _end(5, 1, p)
    else:
        res = 0
    return patp(res)
