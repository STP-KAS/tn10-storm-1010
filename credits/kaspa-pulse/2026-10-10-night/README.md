# Kaspa Pulse's count, night of 10-11 Oct 2026, 18:10-02:35 UTC

Credit: Kaspa Pulse ([@gokugalax](https://x.com/gokugalax), [kaspapulse.com](https://kaspapulse.com)). Published with his OK (12 Oct 2026). Credit him when you reuse it.

**Method:** tx accepted in blocks, two independent nodes, per UTC minute, bucketed by block time; every minute confirmed by both nodes. Includes ~56 tx/s TN10 base load. Testnet-10 only. Counts only. All times UTC (CEST = UTC+2).

**Window:** Sat 18:10Z - Sun 02:35Z. **32.3 million** tx accepted; best minute **2,785 tx/s** (21:20Z).

| File | What |
|---|---|
| [tn10-2026-10-10-1810-0235-accepted.csv](tn10-2026-10-10-1810-0235-accepted.csv) | His own per-minute file, unchanged: minute_utc, complete_minute, accepted_tx, accepted_tx_per_s, blocks, confirmed_by_both_nodes, different_miners. 18:10-02:34Z, 505 complete minutes, all confirmed by both nodes; 32,319,902 tx. |


## Comparison and correction (approved by Kaspa Pulse, 12 Oct 2026)

- Our corrected chain count for 18:10-02:29Z is 32,299,895 tx, against Kaspa Pulse (@gokugalax, kaspapulse.com)'s 32,303,122 for the same minutes (-0.01%). Per-step means agree within a few tx/s (MAX 20:20-20:35Z: ours 2,617.2, his 2,615.3).
- Our first 10 Oct chain-count.csv double-counted 89 lumped minutes (38.36M, corrected to 32.30M), fixed in d90eb26. Found by comparing with the independent count of Kaspa Pulse (@gokugalax, kaspapulse.com).
