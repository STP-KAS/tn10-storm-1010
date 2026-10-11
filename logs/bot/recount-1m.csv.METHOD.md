> **Experimental. We are just trying this.** [Disclaimer](../../DISCLAIMER.md) · Method sidecar: kept next to the CSV so the CSV itself stays plain (header row first) for parsers.

# Method: recount-1m.csv (10-11 Oct 2026 night, bot side)

| | |
|---|---|
| **One row** | one UTC minute of the recount (a `note` marks a minute merged with later ones) |
| **Timezone** | UTC (`minute_utc`, ISO with milliseconds). CEST = UTC+2. |
| **What is counted** | `chain_blocks`, `accepted_ids` (accepted ids of those chain blocks), `unique_accepted` = ids minus one coinbase per chain block, `unique_accepted_s` = / 60. All senders plus TN10 base load (about 56 tx/s). |
| **Which node** | **One node: n2**, read-only, after END and before pruning |
| **Bucketing** | **By n2's receive time:** the walk of n2's selected chain is cut at the chain tips n2 had at each UTC-minute boundary of its wall clock (logged live, kept local), not by block timestamp |

Raw source behind [chain-count.csv](chain-count.csv.METHOD.md).

Counts only: no txid, key, seed, IP, host, port or wallet address in the file. Kaspa Testnet-10 only; tKAS has no value.
