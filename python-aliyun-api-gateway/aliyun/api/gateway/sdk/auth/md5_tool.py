import hashlib
import base64


def _get_md5(content):
    m = hashlib.md5()
    m.update(memoryview(content.encode("utf-8")))
    return m.digest()


def get_md5_base64_str(content):
    return base64.encodebytes(_get_md5(content)).strip().decode()
