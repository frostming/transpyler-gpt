import codecs
import encodings
import io
import sys

utf_8 = encodings.search_function("utf-8")


def decode(inp, errors="strict"):
    """Decode the given text using the UTF-8 encoding."""
    from ._core import transpile

    u, length = utf_8.decode(inp, errors)
    if not u:
        return u, length
    target_python = f"{sys.version_info[0]}.{sys.version_info[1]}"
    return transpile(u, target_python), length


class IncrementalDecoder(codecs.BufferedIncrementalDecoder):
    def _buffer_decode(self, input, errors, final):  # pragma: no cover
        if final:
            return decode(input, errors)
        else:
            return "", 0


class StreamReader(utf_8.streamreader, object):
    """decode is deferred to support better error messages"""

    _stream = None
    _decoded = False

    @property
    def stream(self):
        if not self._decoded:
            text, _ = decode(self._stream.read())
            self._stream = io.BytesIO(text.encode("UTF-8"))
            self._decoded = True
        return self._stream

    @stream.setter
    def stream(self, stream):
        self._stream = stream
        self._decoded = False


def search_function(name):
    if name != "transpyler":
        return None
    return codecs.CodecInfo(
        name=name,
        encode=utf_8.encode,
        decode=decode,
        incrementalencoder=utf_8.incrementalencoder,
        incrementaldecoder=IncrementalDecoder,
        streamreader=StreamReader,
        streamwriter=utf_8.streamwriter,
    )


def register():
    codecs.register(search_function)
