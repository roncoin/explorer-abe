# Copyright(C) 2013 by John Tobey <jtobey@john-edwin-tobey.org>

# genesis_tx.py: known transactions unavailable through RPC for
# historical reasons: https://bitcointalk.org/index.php?topic=119530.0

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public
# License along with this program.  If not, see
# <http://www.gnu.org/licenses/agpl.html>.

def get(tx_hash_hex):
    """
    Given the hexadecimal hash of the genesis transaction (as shown
    by, e.g., "bitcoind getblock 0") return the hexadecimal raw
    transaction.  This works around a Bitcoind limitation described at
    https://bitcointalk.org/index.php?topic=119530.0
    """

    # Main Bitcoin chain:
    if tx_hash_hex == "cdf1190e352155899d5f3138d7b29a1de9c76aea4794730ac8b38e22e1dceefc":
        return "01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff03510101ffffffff0100208ed2063c0000232102f6e61b9e306ccc3d8cb3d2c904950c3c064f7936d369ff5ca803ffb91c632c81ac00000000"

    # Extract your chain's genesis transaction data from the first
    # block file and add it here, or better yet, patch your coin's
    # getrawtransaction to return it on request:
    #if tx_hash_hex == "<HASH>"
    #    return "<DATA>"

    return None
