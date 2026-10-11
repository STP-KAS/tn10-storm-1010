> **Experimental. We are just trying this.** [Disclaimer](../../DISCLAIMER.md) · Method sidecar: kept next to the CSV so the CSV itself stays plain (header row first) for parsers.

# Method: chain-count.csv (10-11 Oct 2026 night, bot side)

| | |
|---|---|
| **One row** | one UTC minute, 17:30Z Sat 10 Oct (T0 − 1 h) to 02:29Z Sun 11 Oct (END 02:30Z) |
| **Timezone** | UTC (`minute_utc`). CEST = UTC+2. |
| **What is counted** | `network_unique_accepted`: transaction ids accepted by the virtual chain of **n2** (the bot's own pruned TN10 node), each id once, minus one coinbase per chain block. All senders plus TN10 base load (about 56 tx/s). `accepted_tx_per_s` = that / 60. |
| **Which node** | **One node: n2.** From the post-END recount on n2 ([recount-1m.csv](recount-1m.csv.METHOD.md)), before pruning; where the recount has no clean row, the live chain logger on n2. |
| **Bucketing** | **By n2's receive time, not block time:** a minute = chain blocks between the chain tips n2 had at two UTC-minute boundaries of its wall clock |
| **`blocks`, `our_mined_blocks`** | blocks n2 received that minute (by n2 receive time), and of those, blocks paying the bot's one miner |
| **`complete_minute`** | `yes` = a clean single-minute recount row (and a valid live row, where there is one). Lumped or missing minutes are `no` and empty. The step medians on [COMBINED.md](../COMBINED.md) use `yes` rows only. |

Counts only: no txid, key, seed, IP, host, port or wallet address in the file. Kaspa Testnet-10 only; tKAS has no value.
