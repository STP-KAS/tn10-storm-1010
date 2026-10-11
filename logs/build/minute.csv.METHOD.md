> **Experimental. We are just trying this.** [Disclaimer](../../DISCLAIMER.md) · Method sidecar: kept next to the CSV so the CSV itself stays plain (header row first) for parsers.

# Method: minute.csv (10 Oct 2026, Build side)

| | |
|---|---|
| **One row** | one UTC minute, Build side, 17:28Z to 22:58Z Sat 10 Oct (no 22:59Z row: Build's clock stopped at 23:00Z before that flush) |
| **Timezone** | UTC (`minute_utc`). CEST = UTC+2. |
| **Sender columns** | Build's own senders only; `submit_ok` = taken into a node's mempool (not accepted) |
| **Network columns** | from Build's desk node (`network_unique_accepted`, `blocks`, `tx_per_block`, `our_mined_blocks`); all senders plus TN10 base load |
| **Which node** | **One node: Build's desk node** (public TN10 nodes as submit fallback) |
| **Bucketing** | **Not stated in Build's files. Not sure / open for debate.** |

Written by Grok Build; this sidecar only describes it. Columns: [go/LOGGING.md](../../go/LOGGING.md#minutecsv).

Counts only: no txid, key, seed, IP, host, port or wallet address in the file. Kaspa Testnet-10 only; tKAS has no value.
