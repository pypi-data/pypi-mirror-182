import hashlib
from typing import Tuple


def hash_feature(data: Tuple):
    sha256 = hashlib.sha256()
    sha256.update(str(data).encode())
    return sha256.hexdigest()
