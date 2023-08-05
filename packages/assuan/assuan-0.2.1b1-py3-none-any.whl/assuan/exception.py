# Copyright (C) 2012 W. Trevor King <wking@tremily.us>
#
# This file is part of assuan.
#
# assuan is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# assuan is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# assuan.  If not, see <http://www.gnu.org/licenses/>.

"""Assuan errors as defined in `libgpg-error`_.

The Assuan_ docs_ suggest these error codes.

.. _libgpg-error: http://www.gnupg.org/related_software/libgpg-error/
.. _Assuan:
  http://www.gnupg.org/documentation/manuals/assuan/Server-responses.html
.. _docs: http://www.gnupg.org/documentation/manuals/assuan/Error-codes.html
"""

from typing import Dict, Optional

# extracted from libgpg-error-1.10/src/err-codes.h and gpg-error.h
MESSAGE: Dict[int, str] = {
    0: 'Success',
    1: 'General error',
    2: 'Unknown packet',
    3: 'Unknown version in packet',
    4: 'Invalid public key algorithm',
    5: 'Invalid digest algorithm',
    6: 'Bad public key',
    7: 'Bad secret key',
    8: 'Bad signature',
    9: 'No public key',
    10: 'Checksum error',
    11: 'Bad passphrase',
    12: 'Invalid cipher algorithm',
    13: 'Keyring open',
    14: 'Invalid packet',
    15: 'Invalid armor',
    16: 'No user ID',
    17: 'No secret key',
    18: 'Wrong secret key used',
    19: 'Bad session key',
    20: 'Unknown compression algorithm',
    21: 'Number is not prime',
    22: 'Invalid encoding method',
    23: 'Invalid encryption scheme',
    24: 'Invalid signature scheme',
    25: 'Invalid attribute',
    26: 'No value',
    27: 'Not found',
    28: 'Value not found',
    29: 'Syntax error',
    30: 'Bad MPI value',
    31: 'Invalid passphrase',
    32: 'Invalid signature class',
    33: 'Resources exhausted',
    34: 'Invalid keyring',
    35: 'Trust DB error',
    36: 'Bad certificate',
    37: 'Invalid user ID',
    38: 'Unexpected error',
    39: 'Time conflict',
    40: 'Keyserver error',
    41: 'Wrong public key algorithm',
    42: 'Tribute to D. A.',
    43: 'Weak encryption key',
    44: 'Invalid key length',
    45: 'Invalid argument',
    46: 'Syntax error in URI',
    47: 'Invalid URI',
    48: 'Network error',
    49: 'Unknown host',
    50: 'Selftest failed',
    51: 'Data not encrypted',
    52: 'Data not processed',
    53: 'Unusable public key',
    54: 'Unusable secret key',
    55: 'Invalid value',
    56: 'Bad certificate chain',
    57: 'Missing certificate',
    58: 'No data',
    59: 'Bug',
    60: 'Not supported',
    61: 'Invalid operation code',
    62: 'Timeout',
    63: 'Internal error',
    64: 'EOF (gcrypt)',
    65: 'Invalid object',
    66: 'Provided object is too short',
    67: 'Provided object is too large',
    68: 'Missing item in object',
    69: 'Not implemented',
    70: 'Conflicting use',
    71: 'Invalid cipher mode',
    72: 'Invalid flag',
    73: 'Invalid handle',
    74: 'Result truncated',
    75: 'Incomplete line',
    76: 'Invalid response',
    77: 'No agent running',
    78: 'agent error',
    79: 'Invalid data',
    80: 'Unspecific Assuan server fault',
    81: 'General Assuan error',
    82: 'Invalid session key',
    83: 'Invalid S-expression',
    84: 'Unsupported algorithm',
    85: 'No pinentry',
    86: 'pinentry error',
    87: 'Bad PIN',
    88: 'Invalid name',
    89: 'Bad data',
    90: 'Invalid parameter',
    91: 'Wrong card',
    92: 'No dirmngr',
    93: 'dirmngr error',
    94: 'Certificate revoked',
    95: 'No CRL known',
    96: 'CRL too old',
    97: 'Line too long',
    98: 'Not trusted',
    99: 'Operation cancelled',
    100: 'Bad CA certificate',
    101: 'Certificate expired',
    102: 'Certificate too young',
    103: 'Unsupported certificate',
    104: 'Unknown S-expression',
    105: 'Unsupported protection',
    106: 'Corrupted protection',
    107: 'Ambiguous name',
    108: 'Card error',
    109: 'Card reset required',
    110: 'Card removed',
    111: 'Invalid card',
    112: 'Card not present',
    113: 'No PKCS15 application',
    114: 'Not confirmed',
    115: 'Configuration error',
    116: 'No policy match',
    117: 'Invalid index',
    118: 'Invalid ID',
    119: 'No SmartCard daemon',
    120: 'SmartCard daemon error',
    121: 'Unsupported protocol',
    122: 'Bad PIN method',
    123: 'Card not initialized',
    124: 'Unsupported operation',
    125: 'Wrong key usage',
    126: 'Nothing found',
    127: 'Wrong blob type',
    128: 'Missing value',
    129: 'Hardware problem',
    130: 'PIN blocked',
    131: 'Conditions of use not satisfied',
    132: 'PINs are not synced',
    133: 'Invalid CRL',
    134: 'BER error',
    135: 'Invalid BER',
    136: 'Element not found',
    137: 'Identifier not found',
    138: 'Invalid tag',
    139: 'Invalid length',
    140: 'Invalid key info',
    141: 'Unexpected tag',
    142: 'Not DER encoded',
    143: 'No CMS object',
    144: 'Invalid CMS object',
    145: 'Unknown CMS object',
    146: 'Unsupported CMS object',
    147: 'Unsupported encoding',
    148: 'Unsupported CMS version',
    149: 'Unknown algorithm',
    150: 'Invalid crypto engine',
    151: 'Public key not trusted',
    152: 'Decryption failed',
    153: 'Key expired',
    154: 'Signature expired',
    155: 'Encoding problem',
    156: 'Invalid state',
    157: 'Duplicated value',
    158: 'Missing action',
    159: 'ASN.1 module not found',
    160: 'Invalid OID string',
    161: 'Invalid time',
    162: 'Invalid CRL object',
    163: 'Unsupported CRL version',
    164: 'Invalid certificate object',
    165: 'Unknown name',
    166: 'A locale function failed',
    167: 'Not locked',
    168: 'Protocol violation',
    169: 'Invalid MAC',
    170: 'Invalid request',
    171: 'Unknown extension',
    172: 'Unknown critical extension',
    173: 'Locked',
    174: 'Unknown option',
    175: 'Unknown command',
    176: 'Not operational',
    177: 'No passphrase given',
    178: 'No PIN given',
    179: 'Not enabled',
    180: 'No crypto engine',
    181: 'Missing key',
    182: 'Too many objects',
    183: 'Limit reached',
    184: 'Not initialized',
    185: 'Missing issuer certificate',
    198: 'Operation fully cancelled',
    199: 'Operation not yet finished',
    200: 'Buffer too short',
    201: 'Invalid length specifier in S-expression',
    202: 'String too long in S-expression',
    203: 'Unmatched parentheses in S-expression',
    204: 'S-expression not canonical',
    205: 'Bad character in S-expression',
    206: 'Bad quotation in S-expression',
    207: 'Zero prefix in S-expression',
    208: 'Nested display hints in S-expression',
    209: 'Unmatched display hints',
    210: 'Unexpected reserved punctuation in S-expression',
    211: 'Bad hexadecimal character in S-expression',
    212: 'Odd hexadecimal numbers in S-expression',
    213: 'Bad octal character in S-expression',
    257: 'General IPC error',
    258: 'IPC accept call failed',
    259: 'IPC connect call failed',
    260: 'Invalid IPC response',
    261: 'Invalid value passed to IPC',
    262: 'Incomplete line passed to IPC',
    263: 'Line passed to IPC too long',
    264: 'Nested IPC commands',
    265: 'No data callback in IPC',
    266: 'No inquire callback in IPC',
    267: 'Not an IPC server',
    268: 'Not an IPC client',
    269: 'Problem starting IPC server',
    270: 'IPC read error',
    271: 'IPC write error',
    273: 'Too much data for IPC layer',
    274: 'Unexpected IPC command',
    275: 'Unknown IPC command',
    276: 'IPC syntax error',
    277: 'IPC call has been cancelled',
    278: 'No input source for IPC',
    279: 'No output source for IPC',
    280: 'IPC parameter error',
    281: 'Unknown IPC inquire',
    1024: 'User defined error code 1',
    1025: 'User defined error code 2',
    1026: 'User defined error code 3',
    1027: 'User defined error code 4',
    1028: 'User defined error code 5',
    1029: 'User defined error code 6',
    1030: 'User defined error code 7',
    1031: 'User defined error code 8',
    1032: 'User defined error code 9',
    1033: 'User defined error code 10',
    1034: 'User defined error code 11',
    1035: 'User defined error code 12',
    1036: 'User defined error code 13',
    1037: 'User defined error code 14',
    1038: 'User defined error code 15',
    1039: 'User defined error code 16',
    16381: 'System error w/o errno',
    16382: 'Unknown system error',
    16383: 'End of file',
}

CODE: Dict[str, int] = {message: code for code, message in MESSAGE.items()}

# TODO: system errors (GPG_ERR_E2BIG = GPG_ERR_SYSTEM_ERROR | 0, etc.)


class AssuanError(Exception):
    r"""Represent assuan errors.

    >>> e = AssuanError(1)
    >>> print(e)
    1 General error

    >>> e = AssuanError(1024, 'testing!')
    >>> print(e)
    1024 testing!

    >>> e = AssuanError(message='Unknown packet')
    >>> print(e)
    2 Unknown packet
    """

    def __init__(
        self, code: Optional[int] = None, message: Optional[str] = None
    ) -> None:
        """Intialize assuan exception."""
        if code and message:
            pass
        elif code:
            message = MESSAGE.get(code, 'Unknown error code')
        elif message:
            code = CODE.get(message, 1)
        else:
            raise ValueError('missing both `code` and `message`')

        self.code = code
        self.message = message
        super().__init__(f"{code} {message}")
