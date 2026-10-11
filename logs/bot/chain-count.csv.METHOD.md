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
| **`complete_minute`** | `yes` = a single-minute recount row with no merge note, at most 400 chain blocks, and (where there is one) a valid live row. Everything else is `no`. The step medians on [COMBINED.md](../COMBINED.md) use `yes` rows only. |
| **Lumped rows** | `span_min` > 1: the recount row covers several minutes (a boundary tip did not end up on the final chain). The **total sits in the first minute of the span**; `accepted_tx_per_s` there = total / (60 × `span_min`). The other minutes of the span are **empty** (their transactions are in that total). |
| **`strict_source`** | why a row is or is not a complete minute |
| **`live_logger_accepted`** | for minutes inside a lumped span only: what the live chain logger on n2 read for that minute. Reference only; **never add it to the totals** (those transactions are already in the lumped row). |

## Correction, 11 Oct 2026 21:45 CEST

The first version of this file (kept as [chain-count.csv.superseded](chain-count.csv.superseded)) filled the minutes inside a lumped recount span with the live logger's value and flagged most of them `complete_minute = yes`. Those transactions were then counted twice: once in the lumped row and once in their own minute. Over 18:10-02:29Z that was 89 minutes and 6,062,898 tx: the old file sums to 38,362,793, the corrected file to **32,299,895**, which equals the recount itself ([recount-1m.csv](recount-1m.csv.METHOD.md)). Over the whole file (17:30-02:29Z): 41,032,754 → 34,689,524. One one-minute row with more than 400 chain blocks (a boundary block off the final chain) is also no longer complete; `complete_minute = yes` went from 313 to 219 rows. Per-step medians and recount averages are recomputed in [COMBINED.md](../COMBINED.md). Same rule as the 11 Oct run's `headline_strict`.

Counts only: no txid, key, seed, IP, host, port or wallet address in the file. Kaspa Testnet-10 only; tKAS has no value.
