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
    if tx_hash_hex == "6ca432ab441502c17bfc4d60be0c4a78e4c399b002242c7aec456d2c63bb4aa1":
        return "01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff05026d020101ffffffff010056218300000000232102ae40fc16b68eb87ac197b7d8625c7004c1a71d618fb383631140bae6af0bdf95ac00000000"

    # Extract your chain's genesis transaction data from the first
    # block file and add it here, or better yet, patch your coin's
    # getrawtransaction to return it on request:
    #if tx_hash_hex == "<HASH>"
    #    return "<DATA>"

    return None
