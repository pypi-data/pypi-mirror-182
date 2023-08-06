from hashlib import sha256 as _sha256

from Crypto.Hash import RIPEMD160
from coincurve import PrivateKey as ECPrivateKey, PublicKey as ECPublicKey


def sha256(bytestr):
    return _sha256(bytestr).digest()


def double_sha256(bytestr):
    return _sha256(_sha256(bytestr).digest()).digest()


def double_sha256_checksum(bytestr):
    return double_sha256(bytestr)[:4]


def ripemd160_sha256(bytestr):
    rh = RIPEMD160.new()
    rh.update(sha256(bytestr))
    return rh.digest()


hash160 = ripemd160_sha256
