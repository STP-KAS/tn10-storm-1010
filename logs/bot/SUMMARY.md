# Bot side, live summary (TN10 storm, Sat 10 Oct 2026)

Updated **03:32:07 CEST / 01:32:07 UTC**, about every 10 minutes from G1 to END. Counts only, written on the box by `live-summary.py` (read-only, sends nothing). Column meanings: [go/LOGGING.md](../../go/LOGGING.md). Plan and times: [go/README.md](../../go/README.md).

## Now

| What | Value |
|---|---|
| Step | **HOLD**, until 04:15 CEST / 02:15 UTC |
| Bot target (plan) | 880 tx/s |
| Bot submitted, last 10 min | 111.1 tx/s (66,636 tx) |
| Bot accepted on n2, last 10 min | 111.3 tx/s (66,805 tx) |
| Rejects, last 10 min | 2 consensus/mempool; 6,894 public-node transport errors |
| Senders writing rows | 11 (processes up: 11) |
| Scheduler / watchdog | running / running |
| Build started? | yes (BUILD-OK present) |
| HALT | no |

## Public nodes, last 10 min

| Node | Submits ok | Rejects | Errors | Down (s) |
|---|---:|---:|---:|---:|
| boson-10.kaspa.red | 12,048 | 2 | 1,205 | 0 |
| electron-10.kaspa.blue | 15,184 | 0 | 1,620 | 0 |
| muon-10.kaspa.blue | 13,643 | 0 | 1,400 | 0 |
| neutrino-10.kaspa.stream | 13,643 | 0 | 1,413 | 0 |
| vector-10.kaspa.green | 12,118 | 0 | 1,256 | 0 |

Rejects by class: already_in_mempool 2, rpc 6,894

## n2 (bot's private reader node) and the box

| What | Value |
|---|---|
| n2 synced / UTXO index | True / False |
| n2 sink age (lag) | 0.1 s |
| n2 virtual DAA score | 593,481,600 |
| Miner processes | 1 |
| Coins left (unclaimed) | 0 tKAS in 0 coins |
| Disk free / RAM available | 36 GB / 2,407 MB |

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
| 03:16:57 | sender-relaunch | HOLD | S14 relaunch 17/30 |
| 03:16:57 | sender-start | HOLD | S14 mode=pub |
| 03:17:00 | sender-relaunch | HOLD | S15 relaunch 16/30 |
| 03:17:00 | sender-start | HOLD | S15 mode=pub |
| 03:17:19 | sender-relaunch | - | S12 relaunch 17/30 |
| 03:17:19 | sender-start | - | S12 mode=pub |
| 03:17:22 | sender-relaunch | HOLD | S13 relaunch 17/30 |
| 03:17:22 | sender-start | HOLD | S13 mode=pub |
| 03:17:25 | sender-relaunch | HOLD | S14 relaunch 18/30 |
| 03:17:25 | sender-start | HOLD | S14 mode=pub |
| 03:17:28 | sender-relaunch | HOLD | S15 relaunch 17/30 |
| 03:17:28 | sender-start | HOLD | S15 mode=pub |

How to read: *Now* answers "is the bot sending what the plan says?"; *Public nodes* shows which node rejects or errors; *Steps so far* is the per-step verdict (clean = at least 90% of target delivered, at least 99% accepted, p90 at most 10 s). Final per-second files land here after END.
