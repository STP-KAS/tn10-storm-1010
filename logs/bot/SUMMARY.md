# Bot side, live summary (TN10 storm, Sat 10 Oct 2026)

Updated **20:45:15 CEST / 18:45:15 UTC**, about every 10 minutes from G1 to END. Counts only, written on the box by `live-summary.py` (read-only, sends nothing). Column meanings: [go/LOGGING.md](../../go/LOGGING.md). Plan and times: [go/README.md](../../go/README.md).

## Now

| What | Value |
|---|---|
| Step | **X250**, until 20:55 CEST / 18:55 UTC |
| Bot target (plan) | 66 tx/s |
| Bot submitted, last 10 min | 32.0 tx/s (19,185 tx) |
| Bot accepted on n2, last 10 min | 31.9 tx/s (19,140 tx) |
| Rejects, last 10 min | 0 consensus/mempool; 0 public-node transport errors |
| Senders writing rows | 15 (processes up: 15) |
| Scheduler / watchdog | running / running |
| Build started? | yes (BUILD-OK present) |
| HALT | no |

## Public nodes, last 10 min

| Node | Submits ok | Rejects | Errors | Down (s) |
|---|---:|---:|---:|---:|
| boson-10.kaspa.red | 4,472 | 0 | 0 | 0 |
| electron-10.kaspa.blue | 3,188 | 0 | 0 | 0 |
| muon-10.kaspa.blue | 4,135 | 0 | 0 | 0 |
| neutrino-10.kaspa.stream | 4,156 | 0 | 0 | 0 |
| vector-10.kaspa.green | 3,234 | 0 | 0 | 0 |

## n2 (bot's private reader node) and the box

| What | Value |
|---|---|
| n2 synced / UTXO index | True / True |
| n2 sink age (lag) | 0.3 s |
| n2 virtual DAA score | 593,239,529 |
| Miner processes | 1 |
| Coins left (unclaimed) | 934,337 tKAS in 29,485 coins |
| Disk free / RAM available | 24 GB / 4,495 MB |

## Steps so far

| Step | Bot target | Submitted tx/s | Accepted tx/s | Rejects | Transport errors | Clean |
|---|---:|---:|---:|---:|---:|---|
| B0 | 0 | – | – | – | – | running or not evaluated |
| X250 | 66 | – | – | – | – | running or not evaluated |

## Last events

| CEST | Event | Step | Detail |
|---|---|---|---|
| 20:40:36 | sender-relaunch | X250 | S10 relaunch 1/8 |
| 20:40:36 | sender-start | X250 | S10 mode=pub |
| 20:40:39 | sender-relaunch | X250 | S11 relaunch 1/8 |
| 20:40:39 | sender-start | X250 | S11 mode=pub |
| 20:40:42 | sender-relaunch | X250 | S12 relaunch 1/8 |
| 20:40:42 | sender-start | X250 | S12 mode=pub |
| 20:40:45 | sender-relaunch | X250 | S13 relaunch 1/8 |
| 20:40:45 | sender-start | X250 | S13 mode=pub |
| 20:40:48 | sender-relaunch | X250 | S14 relaunch 1/8 |
| 20:40:48 | sender-start | X250 | S14 mode=pub |
| 20:40:51 | sender-relaunch | X250 | S15 relaunch 1/8 |
| 20:40:51 | sender-start | X250 | S15 mode=pub |

How to read: *Now* answers "is the bot sending what the plan says?"; *Public nodes* shows which node rejects or errors; *Steps so far* is the per-step verdict (clean = at least 90% of target delivered, at least 99% accepted, p90 at most 10 s). Final per-second files land here after END.
