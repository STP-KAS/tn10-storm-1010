> **Experimental. We are just trying this.** [Disclaimer](../../DISCLAIMER.md) · Method sidecar: kept next to the CSV so the CSV itself stays plain (header row first) for parsers.

# Method: minute.csv (10-11 Oct 2026 night, bot side)

| | |
|---|---|
| **One row** | one UTC minute, bot side, 18:00Z Sat to 02:29Z Sun |
| **Timezone** | UTC (`minute_utc`). CEST = UTC+2. |
| **Sender columns** (`sent`, `submit_ok`, `rejects`, `node_accepted`) | the bot's own senders only, summed from their per-second files; `submit_ok` = taken into a public node's mempool (not accepted); `node_accepted` = own transactions seen accepted on n2's virtual chain |
| **Network columns** (`network_unique_accepted`, `blocks`, `tx_per_block`, `our_mined_blocks`) | **n2**: `network_unique_accepted` from the post-END recount (empty where the recount minute was not clean); `blocks`, `tx_per_block`, `our_mined_blocks` from the live chain logger |
| **Which node** | **One node: n2** for reads and network columns; submits went to the five public TN10 nodes |
| **Bucketing** | **By n2's receive time** (n2 wall-clock UTC minute), not by block time |

For the network headline use [chain-count.csv](chain-count.csv.METHOD.md). Columns: [go/LOGGING.md](../../go/LOGGING.md#minutecsv).

Counts only: no txid, key, seed, IP, host, port or wallet address in the file. Kaspa Testnet-10 only; tKAS has no value.
