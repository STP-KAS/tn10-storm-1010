> **Experimental. We are just trying this.** [Disclaimer](../../DISCLAIMER.md) · Method sidecar: kept next to the CSV so the CSV itself stays plain (header row first) for parsers.

# Method: chain-count.csv (10 Oct 2026, Build side)

| | |
|---|---|
| **One row** | one UTC minute, 14:00Z to 22:59Z Sat 10 Oct (Build's own clock; Build stopped 23:00Z) |
| **Timezone** | UTC (`minute_utc`). CEST = UTC+2. |
| **What is counted** | `network_unique_accepted`: accepted transaction ids, each once, on Build's desk node; all senders plus TN10 base load (about 56 tx/s). `accepted_tx_per_s` = / 60. `blocks`, `our_mined_blocks`: blocks that minute and those paying Build's one miner. `complete_minute` = 1 when every block of the minute was read. |
| **Which node** | **One node: Build's own private, non-archival desk node** |
| **Bucketing** | **Not stated in Build's files** (block time or node receive time). **Not sure / open for debate** until Build confirms. |

Written by Grok Build; this sidecar only describes it. The network headline for the night uses the bot's [chain-count.csv](../bot/chain-count.csv.METHOD.md).

Counts only: no txid, key, seed, IP, host, port or wallet address in the file. Kaspa Testnet-10 only; tKAS has no value.
