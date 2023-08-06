"""Shared utilities for tests."""

import cbor2

from pycddl import Schema

BSTR_SCHEMA = Schema("object = bstr")

BSTR_1K = cbor2.dumps(b"A" * 1_000)
BSTR_1M = cbor2.dumps(b"A" * 1_000_000)
BSTR_100M = cbor2.dumps(b"A" * 100_000_000)
