# Bot side, live summary (TN10 storm, Sat 10 Oct 2026)

Updated **20:15:16 CEST / 18:15:16 UTC**, about every 10 minutes from G1 to END. Counts only, written on the box by `live-summary.py` (read-only, sends nothing). Column meanings: [go/LOGGING.md](../../go/LOGGING.md). Plan and times: [go/README.md](../../go/README.md).

## Now

| What | Value |
|---|---|
| Step | **G2 (no sends)**, until 20:30 CEST / 18:30 UTC |
| Bot target (plan) | 0 tx/s |
| Bot submitted, last 10 min | 0.0 tx/s (0 tx) |
| Bot accepted on n2, last 10 min | 0.0 tx/s (0 tx) |
| Rejects, last 10 min | 0 consensus/mempool; 0 public-node transport errors |
| Senders writing rows | 15 (processes up: 15) |
| Scheduler / watchdog | running / running |
| Build started? | yes (BUILD-OK present) |
| HALT | no |

## Public nodes, last 10 min

| Node | Submits ok | Rejects | Errors | Down (s) |
|---|---:|---:|---:|---:|
| (no sends in this window) | – | – | – | – |

## n2 (bot's private reader node) and the box

| What | Value |
|---|---|
| n2 synced / UTXO index | True / True |
| n2 sink age (lag) | 0.4 s |
| n2 virtual DAA score | 593,217,511 |
| Miner processes | 1 |
| Coins left (unclaimed) | 1,034,706 tKAS in 32,565 coins |
| Disk free / RAM available | 24 GB / 3,846 MB |

## Steps so far

| Step | Bot target | Submitted tx/s | Accepted tx/s | Rejects | Transport errors | Clean |
|---|---:|---:|---:|---:|---:|---|
| (T0 is 20:30 CEST / 18:30 UTC) | – | – | – | – | – | – |

## Last events

| CEST | Event | Step | Detail |
|---|---|---|---|
| 20:14:21 | sender-start | - | S8 mode=pub |
| 20:14:24 | sender-start | - | S9 mode=pub |
| 20:14:27 | sender-start | - | S10 mode=pub |
| 20:14:30 | sender-start | - | S11 mode=pub |
| 20:14:33 | sender-start | - | S12 mode=pub |
| 20:14:36 | sender-start | - | S13 mode=pub |
| 20:14:39 | sender-start | - | S14 mode=pub |
| 20:14:42 | sender-start | - | S15 mode=pub |
| 20:15:00 | gate | - | G2 pass synced true utxoindex true lag 0.4 |
| 20:15:00 | build-confirmed | - | at G2 |
| 20:15:00 | build-confirmed | - | BUILD-OK |
| 20:15:00 | miner-on | - | 18:15 UTC start, n2 synced |

How to read: *Now* answers "is the bot sending what the plan says?"; *Public nodes* shows which node rejects or errors; *Steps so far* is the per-step verdict (clean = at least 90% of target delivered, at least 99% accepted, p90 at most 10 s). Final per-second files land here after END.
