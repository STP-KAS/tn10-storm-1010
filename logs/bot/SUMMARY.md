# Bot side, live summary (TN10 storm, Sat 10 Oct 2026)

Updated **04:30:18 CEST / 02:30:18 UTC**, about every 10 minutes from G1 to END. Counts only, written on the box by `live-summary.py` (read-only, sends nothing). Column meanings: [go/LOGGING.md](../../go/LOGGING.md). Plan and times: [go/README.md](../../go/README.md).

## Now

| What | Value |
|---|---|
| Step | **END (senders stopped)** |
| Bot target (plan) | 0 tx/s |
| Bot submitted, last 10 min | 0.0 tx/s (0 tx) |
| Bot accepted on n2, last 10 min | 0.0 tx/s (0 tx) |
| Rejects, last 10 min | 0 consensus/mempool; 0 public-node transport errors |
| Senders writing rows | 15 (processes up: 0) |
| Scheduler / watchdog | running / running |
| Build started? | yes (BUILD-OK present) |
| HALT | no |

## Public nodes, last 10 min

| Node | Submits ok | Rejects | Errors | Down (s) |
|---|---:|---:|---:|---:|
| boson-10.kaspa.red | 0 | 0 | 0 | 0 |
| electron-10.kaspa.blue | 0 | 0 | 0 | 0 |
| muon-10.kaspa.blue | 0 | 0 | 0 | 0 |
| neutrino-10.kaspa.stream | 0 | 0 | 0 | 0 |
| vector-10.kaspa.green | 0 | 0 | 0 | 0 |

## n2 (bot's private reader node) and the box

| What | Value |
|---|---|
| n2 synced / UTXO index | True / False |
| n2 sink age (lag) | 0.6 s |
| n2 virtual DAA score | 593,517,323 |
| Miner processes | 0 |
| Coins left (unclaimed) | 0 tKAS in 0 coins |
| Disk free / RAM available | 36 GB / 4,705 MB |

## Steps so far

| Step | Bot target | Submitted tx/s | Accepted tx/s | Rejects | Transport errors | Clean |
|---|---:|---:|---:|---:|---:|---|
| B0 | 0 | – | – | – | – | running or not evaluated |
| X250 | 66 | 66.0 | 66.0 | 0 | 1 | yes |
| X250-drain | 0 | – | – | – | – | running or not evaluated |
| C1000 | 275 | 139.3 | 139.2 | 0 | 22 | no |
| C1000-drain | 0 | – | – | – | – | running or not evaluated |
| C1500 | 413 | 0.0 | 0.3 | 0 | 9,086 | no |
| C1500-drain | 0 | – | – | – | – | running or not evaluated |
| C2000 | 550 | 545.5 | 545.6 | 0 | 0 | yes |
| C2000-drain | 0 | – | – | – | – | running or not evaluated |
| C2500 | 688 | 674.7 | 674.3 | 24 | 1,076 | yes |
| C2500-drain | 0 | – | – | – | – | running or not evaluated |
| MAX | 990 | 919.1 | 919.3 | 92 | 7,857 | yes |
| MAX-drain | 0 | – | – | – | – | running or not evaluated |
| B1 | 0 | – | – | – | – | running or not evaluated |
| HOLD | 880 | 469.2 | 468.6 | 61,152 | 107,927 | no |
| DRAIN | 0 | – | – | – | – | running or not evaluated |

## Last events

| CEST | Event | Step | Detail |
|---|---|---|---|
| 04:14:58 | sender-start | HOLD | S13 mode=pub |
| 04:14:59 | miner-on | HOLD | n2 synced again / process relaunch |
| 04:15:00 | step-end | HOLD | HOLD |
| 04:15:00 | step-start | DRAIN | DRAIN bot 0 |
| 04:15:01 | sender-relaunch | DRAIN | S14 relaunch 24/30 |
| 04:15:01 | sender-start | DRAIN | S14 mode=pub |
| 04:15:04 | sender-relaunch | DRAIN | S15 relaunch 24/30 |
| 04:15:04 | sender-start | DRAIN | S15 mode=pub |
| 04:30:00 | miner-off | DRAIN | 02:30 UTC end |
| 04:30:00 | step-end | DRAIN | DRAIN |
| 04:30:01 | sender-stop | - | END: all senders 0 and stop |
| 04:30:01 | miner-off | - | 02:30 UTC end |

How to read: *Now* answers "is the bot sending what the plan says?"; *Public nodes* shows which node rejects or errors; *Steps so far* is the per-step verdict (clean = at least 90% of target delivered, at least 99% accepted, p90 at most 10 s). Final per-second files land here after END.
