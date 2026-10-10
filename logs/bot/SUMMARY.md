# Bot side, live summary (TN10 storm, Sat 10 Oct 2026)

Updated **00:45:05 CEST / 22:45:05 UTC**, about every 10 minutes from G1 to END. Counts only, written on the box by `live-summary.py` (read-only, sends nothing). Column meanings: [go/LOGGING.md](../../go/LOGGING.md). Plan and times: [go/README.md](../../go/README.md).

## Now

| What | Value |
|---|---|
| Step | **HOLD**, until 04:15 CEST / 02:15 UTC |
| Bot target (plan) | 880 tx/s |
| Bot submitted, last 10 min | 0.0 tx/s (0 tx) |
| Bot accepted on n2, last 10 min | 0.0 tx/s (0 tx) |
| Rejects, last 10 min | 0 consensus/mempool; 28,522 public-node transport errors |
| Senders writing rows | 15 (processes up: 15) |
| Scheduler / watchdog | running / running |
| Build started? | yes (BUILD-OK present) |
| HALT | no |

## Public nodes, last 10 min

| Node | Submits ok | Rejects | Errors | Down (s) |
|---|---:|---:|---:|---:|
| boson-10.kaspa.red | 0 | 0 | 6,028 | 0 |
| electron-10.kaspa.blue | 0 | 0 | 5,791 | 0 |
| muon-10.kaspa.blue | 0 | 0 | 6,859 | 0 |
| neutrino-10.kaspa.stream | 0 | 0 | 3,610 | 0 |
| vector-10.kaspa.green | 0 | 0 | 6,234 | 0 |

Rejects by class: rpc 28,522

## n2 (bot's private reader node) and the box

| What | Value |
|---|---|
| n2 synced / UTXO index | True / False |
| n2 sink age (lag) | 0.2 s |
| n2 virtual DAA score | 593,381,912 |
| Miner processes | 1 |
| Coins left (unclaimed) | 488,999 tKAS in 15,426 coins |
| Disk free / RAM available | 38 GB / 4,076 MB |

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
| HOLD | 880 | – | – | – | – | running or not evaluated |

## Last events

| CEST | Event | Step | Detail |
|---|---|---|---|
| 00:28:23 | sender-relaunch | HOLD | S11 relaunch 6/30 |
| 00:28:23 | sender-start | HOLD | S11 mode=pub |
| 00:28:26 | sender-relaunch | HOLD | S12 relaunch 6/30 |
| 00:28:26 | sender-start | HOLD | S12 mode=pub |
| 00:28:29 | sender-relaunch | HOLD | S13 relaunch 6/30 |
| 00:28:29 | sender-start | HOLD | S13 mode=pub |
| 00:28:32 | sender-relaunch | HOLD | S14 relaunch 7/30 |
| 00:28:32 | sender-start | HOLD | S14 mode=pub |
| 00:28:35 | sender-relaunch | HOLD | S15 relaunch 7/30 |
| 00:28:35 | sender-start | HOLD | S15 mode=pub |
| 00:29:32 | miner-on | HOLD | n2 synced again / process relaunch |
| 00:29:52 | coin-refresh | HOLD | buffer check 488999 tKAS 15426 coins |

How to read: *Now* answers "is the bot sending what the plan says?"; *Public nodes* shows which node rejects or errors; *Steps so far* is the per-step verdict (clean = at least 90% of target delivered, at least 99% accepted, p90 at most 10 s). Final per-second files land here after END.
