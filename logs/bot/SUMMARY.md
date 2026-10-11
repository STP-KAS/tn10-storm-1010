# Bot side, live summary (TN10 storm, Sat 10 Oct 2026)

Updated **02:45:17 CEST / 00:45:17 UTC**, about every 10 minutes from G1 to END. Counts only, written on the box by `live-summary.py` (read-only, sends nothing). Column meanings: [go/LOGGING.md](../../go/LOGGING.md). Plan and times: [go/README.md](../../go/README.md).

## Now

| What | Value |
|---|---|
| Step | **HOLD**, until 04:15 CEST / 02:15 UTC |
| Bot target (plan) | 880 tx/s |
| Bot submitted, last 10 min | 586.3 tx/s (351,777 tx) |
| Bot accepted on n2, last 10 min | 585.0 tx/s (350,987 tx) |
| Rejects, last 10 min | 2 consensus/mempool; 3,000 public-node transport errors |
| Senders writing rows | 15 (processes up: 8) |
| Scheduler / watchdog | running / running |
| Build started? | yes (BUILD-OK present) |
| HALT | no |

## Public nodes, last 10 min

| Node | Submits ok | Rejects | Errors | Down (s) |
|---|---:|---:|---:|---:|
| boson-10.kaspa.red | 58,625 | 0 | 500 | 0 |
| electron-10.kaspa.blue | 87,680 | 0 | 750 | 0 |
| muon-10.kaspa.blue | 70,631 | 0 | 600 | 0 |
| neutrino-10.kaspa.stream | 70,220 | 2 | 600 | 0 |
| vector-10.kaspa.green | 64,621 | 0 | 550 | 0 |

Rejects by class: orphan 2, rpc 3,000

## n2 (bot's private reader node) and the box

| What | Value |
|---|---|
| n2 synced / UTXO index | True / False |
| n2 sink age (lag) | 0.6 s |
| n2 virtual DAA score | 593,452,235 |
| Miner processes | 1 |
| Coins left (unclaimed) | 130,163 tKAS in 4,116 coins |
| Disk free / RAM available | 37 GB / 3,384 MB |

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
| 02:45:02 | sender-relaunch | HOLD | S3 relaunch 10/30 |
| 02:45:02 | sender-start | HOLD | S3 mode=pub |
| 02:45:06 | sender-relaunch | HOLD | S4 relaunch 10/30 |
| 02:45:06 | sender-start | HOLD | S4 mode=pub |
| 02:45:09 | sender-relaunch | HOLD | S5 relaunch 11/30 |
| 02:45:09 | sender-start | HOLD | S5 mode=pub |
| 02:45:12 | sender-relaunch | HOLD | S6 relaunch 11/30 |
| 02:45:12 | sender-start | HOLD | S6 mode=pub |
| 02:45:15 | sender-relaunch | HOLD | S7 relaunch 11/30 |
| 02:45:15 | sender-start | HOLD | S7 mode=pub |
| 02:45:18 | sender-relaunch | HOLD | S8 relaunch 10/30 |
| 02:45:18 | sender-start | HOLD | S8 mode=pub |

How to read: *Now* answers "is the bot sending what the plan says?"; *Public nodes* shows which node rejects or errors; *Steps so far* is the per-step verdict (clean = at least 90% of target delivered, at least 99% accepted, p90 at most 10 s). Final per-second files land here after END.
