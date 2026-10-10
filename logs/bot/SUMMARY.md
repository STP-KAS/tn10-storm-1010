# Bot side, live summary (TN10 storm, Sat 10 Oct 2026)

Updated **23:15:08 CEST / 21:15:08 UTC**, about every 10 minutes from G1 to END. Counts only, written on the box by `live-summary.py` (read-only, sends nothing). Column meanings: [go/LOGGING.md](../../go/LOGGING.md). Plan and times: [go/README.md](../../go/README.md).

## Now

| What | Value |
|---|---|
| Step | **HOLD**, until 04:15 CEST / 02:15 UTC |
| Bot target (plan) | 880 tx/s |
| Bot submitted, last 10 min | 878.6 tx/s (527,142 tx) |
| Bot accepted on n2, last 10 min | 878.3 tx/s (526,972 tx) |
| Rejects, last 10 min | 1 consensus/mempool; 2 public-node transport errors |
| Senders writing rows | 15 (processes up: 15) |
| Scheduler / watchdog | running / running |
| Build started? | yes (BUILD-OK present) |
| HALT | no |

## Public nodes, last 10 min

| Node | Submits ok | Rejects | Errors | Down (s) |
|---|---:|---:|---:|---:|
| boson-10.kaspa.red | 114,262 | 1 | 2 | 0 |
| electron-10.kaspa.blue | 105,554 | 0 | 0 | 0 |
| muon-10.kaspa.blue | 104,994 | 0 | 0 | 0 |
| neutrino-10.kaspa.stream | 96,759 | 0 | 0 | 0 |
| vector-10.kaspa.green | 105,573 | 0 | 0 | 0 |

Rejects by class: already_in_mempool 1, rpc 2

## n2 (bot's private reader node) and the box

| What | Value |
|---|---|
| n2 synced / UTXO index | True / False |
| n2 sink age (lag) | 0.1 s |
| n2 virtual DAA score | 593,328,609 |
| Miner processes | 1 |
| Coins left (unclaimed) | 618,443 tKAS in 19,567 coins |
| Disk free / RAM available | 40 GB / 4,351 MB |

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
| 22:54:10 | sender-start | HOLD | S10 mode=pub |
| 22:54:13 | sender-relaunch | HOLD | S11 relaunch 5/30 |
| 22:54:13 | sender-start | HOLD | S11 mode=pub |
| 22:54:16 | sender-relaunch | HOLD | S12 relaunch 5/30 |
| 22:54:16 | sender-start | HOLD | S12 mode=pub |
| 22:54:19 | sender-relaunch | HOLD | S13 relaunch 5/30 |
| 22:54:19 | sender-start | HOLD | S13 mode=pub |
| 22:54:22 | sender-relaunch | HOLD | S14 relaunch 6/30 |
| 22:54:22 | sender-start | HOLD | S14 mode=pub |
| 22:54:25 | sender-relaunch | HOLD | S15 relaunch 6/30 |
| 22:54:25 | sender-start | HOLD | S15 mode=pub |
| 22:59:33 | coin-refresh | HOLD | buffer check 618443 tKAS 19567 coins |

How to read: *Now* answers "is the bot sending what the plan says?"; *Public nodes* shows which node rejects or errors; *Steps so far* is the per-step verdict (clean = at least 90% of target delivered, at least 99% accepted, p90 at most 10 s). Final per-second files land here after END.
