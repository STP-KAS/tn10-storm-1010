> **Experimental. We are just trying this.** [Disclaimer](../DISCLAIMER.md)

# Tonight's timeline

Back to [README](../README.md). Written by [go/clock.py](../go/clock.py); the same tables are in [go/README.md](../go/README.md#timeline) and both GO files. Machine-readable: [go/steps-utc.json](../go/steps-utc.json). Times: CEST first, UTC second.

## Key times

<!-- clock:key -->
| What | Brussels (CEST) | UTC |
|---|---|---|
| Gate 1 (G1), logging starts | 20:00 | 18:00 |
| Gate 2 (G2), ready check incl. **Build started?**, miners on | 20:15 | 18:15 |
| **T0** (B0 starts) | **20:30** | **18:30** |
| First send step (X250) | 20:40 | 18:40 |
| MAX | 22:20–22:35 | 20:20–20:35 |
| Long hold (HOLD) | 22:50–04:15 Sun | 20:50–02:15 Sun |
| **END**, senders stop, miners off | **04:30 Sun** | **02:30 Sun** |
| Chain count (COUNT) | 04:30 Sun–06:30 Sun | 02:30 Sun–04:30 Sun |
| Logs pushed (PUSH) | by 07:30 Sun | by 05:30 Sun |
| Suggested window for Kaspa Pulse's counter | 20:10–04:35 Sun | 18:10–02:35 Sun |
<!-- /clock:key -->

## Every step

<!-- clock:table -->
| Step | Brussels (CEST) | UTC | Bot tx/s | Build tx/s | Combined tx/s |
|---|---|---|---|---|---|
| PREP | until 20:00 | until 18:00 | Re-armed. n2 synced. Coins topped up. No sends. Miner off. | Read this file. Desk node synced with UTXO index, coins, senders, public fallback. No sends. Miner off. | – |
| G1 | 20:00 | 18:00 | Gate 1: n2 health, coin buffer, the five public nodes reachable. Logging starts. | Gate 1: desk node health, RAM >= 4 GB free, public fallback reachable, coins, disk. Logging starts. Stop every sender not in this plan. | – |
| G2 | 20:15 | 18:15 | Gate 2, **ready check**: stp confirms Build has started. Miner on. | Gate 2, **ready check**: write `FOR-TN10-OPS-ready-1010.txt`, stp passes it to the bot. Miner on. | – |
| **B0** | 20:30–20:40 | 18:30–18:40 | **T0.** No load. Miner on. | **T0.** No load. Miner on. | 0 |
| X250 | 20:40–20:55, drain to 21:00 | 18:40–18:55, drain to 19:00 | 60 | 190 | 250 |
| C1000 | 21:00–21:15, drain to 21:20 | 19:00–19:15, drain to 19:20 | 250 | 750 | 1,000 |
| C1500 | 21:20–21:35, drain to 21:40 | 19:20–19:35, drain to 19:40 | 375 | 1,125 | 1,500 |
| C2000 | 21:40–21:55, drain to 22:00 | 19:40–19:55, drain to 20:00 | 500 | 1,500 | 2,000 |
| C2500 | 22:00–22:15, drain to 22:20 | 20:00–20:15, drain to 20:20 | 625 | 1,875 | 2,500 |
| **MAX** | 22:20–22:35, drain to 22:40 | 20:20–20:35, drain to 20:40 | 900 | 2,600 (may go above, never below) | 3,500 |
| B1 | 22:40–22:50 | 20:40–20:50 | No load | No load | 0 |
| **HOLD** | 22:50–04:15 Sun | 20:50–02:15 Sun | 800 (see the hold rule) | 2,400 (see the hold rule) | 3,200 |
| DRAIN | 04:15 Sun–04:30 Sun | 02:15 Sun–02:30 Sun | Senders 0 | Senders 0 | 0 |
| **END** | 04:30 Sun | 02:30 Sun | Senders stop. Miner off. Live loggers stop. | Senders stop. Miner off. Live loggers stop. Node stays up. | – |
| COUNT | 04:30 Sun–06:30 Sun | 02:30 Sun–04:30 Sun | Chain count from n2, before pruning | Chain count from your desk node, before pruning | – |
| PUSH | by 07:30 Sun | by 05:30 Sun | Logs to `logs/bot/` | Logs to `logs/build/`, plus `FOR-TN10-OPS-result-1010.txt` to stp | – |
<!-- /clock:table -->

## Targets

<!-- clock:targets -->
| Step | Brussels (CEST) | UTC | Combined | Bot (25%) | Build (75%) |
|---|---|---|---|---|---|
| X250 | 20:40–20:55 | 18:40–18:55 | 250 | 60 | 190 |
| C1000 | 21:00–21:15 | 19:00–19:15 | 1,000 | 250 | 750 |
| C1500 | 21:20–21:35 | 19:20–19:35 | 1,500 | 375 | 1,125 |
| C2000 | 21:40–21:55 | 19:40–19:55 | 2,000 | 500 | 1,500 |
| C2500 | 22:00–22:15 | 20:00–20:15 | 2,500 | 625 | 1,875 |
| MAX | 22:20–22:35 | 20:20–20:35 | 3,500 | 900 | 2,600 |
| HOLD | 22:50–04:15 Sun | 20:50–02:15 Sun | 3,200 | 800 | 2,400 |

Fees, both sides: half the lanes at **400** and half at **600** sompi/gram, frozen per step. Floor 100, cap 600. Success line: network unique accepted at or above **3,000 tx/s**, median of a step's valid minutes, at least 10 valid minutes, counted once from chain data.
<!-- /clock:targets -->

Rules for each step (gates, fees, node-dead rule, hold rule): [go/README.md](../go/README.md).
