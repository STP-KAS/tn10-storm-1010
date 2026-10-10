# Bot side, live summary (TN10 storm, Sat 10 Oct 2026)

Updated **22:45:47 CEST / 20:45:47 UTC**, about every 10 minutes from G1 to END. Counts only, written on the box by `live-summary.py` (read-only, sends nothing). Column meanings: [go/LOGGING.md](../../go/LOGGING.md). Plan and times: [go/README.md](../../go/README.md).

## Now

| What | Value |
|---|---|
| Step | **B1**, until 22:50 CEST / 20:50 UTC |
| Bot target (plan) | 0 tx/s |
| Bot submitted, last 10 min | 0.0 tx/s (0 tx) |
| Bot accepted on n2, last 10 min | 0.0 tx/s (0 tx) |
| Rejects, last 10 min | 0 consensus/mempool; 79 public-node transport errors |
| Senders writing rows | 15 (processes up: 15) |
| Scheduler / watchdog | running / running |
| Build started? | yes (BUILD-OK present) |
| HALT | no |

## Public nodes, last 10 min

| Node | Submits ok | Rejects | Errors | Down (s) |
|---|---:|---:|---:|---:|
| boson-10.kaspa.red | 0 | 0 | 20 | 0 |
| electron-10.kaspa.blue | 0 | 0 | 0 | 0 |
| muon-10.kaspa.blue | 0 | 0 | 16 | 0 |
| neutrino-10.kaspa.stream | 0 | 0 | 0 | 0 |
| vector-10.kaspa.green | 0 | 0 | 43 | 0 |

Rejects by class: rpc 79

## n2 (bot's private reader node) and the box

| What | Value |
|---|---|
| n2 synced / UTXO index | – / – |
| n2 sink age (lag) | – s |
| n2 virtual DAA score | – |
| Miner processes | 1 |
| Coins left (unclaimed) | 713,059 tKAS in 22,567 coins |
| Disk free / RAM available | 41 GB / 3,651 MB |

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

## Last events

| CEST | Event | Step | Detail |
|---|---|---|---|
| 22:15:00 | step-start | C2500-drain | C2500-drain bot 0 |
| 22:20:00 | step-end | C2500-drain | C2500-drain |
| 22:20:00 | step-start | MAX | MAX bot 990 |
| 22:29:32 | coin-refresh | MAX | buffer check 719142 tKAS 22767 coins |
| 22:33:12 | sender-relaunch | MAX | S7 relaunch 5/30 |
| 22:33:12 | sender-start | MAX | S7 mode=pub |
| 22:35:00 | step-end | MAX | MAX |
| 22:35:00 | step-start | MAX-drain | MAX-drain bot 0 |
| 22:45:30 | node-restart | MAX-drain | n2 frozen, lag 470.2 s |
| 22:45:30 | step-end | MAX-drain | MAX-drain |
| 22:45:30 | step-start | B1 | B1 bot 0 |
| 22:45:49 | node-restart | B1 | kaspad pid changed (n2 restarted on the same flags by its guard), uptime 7 s |

How to read: *Now* answers "is the bot sending what the plan says?"; *Public nodes* shows which node rejects or errors; *Steps so far* is the per-step verdict (clean = at least 90% of target delivered, at least 99% accepted, p90 at most 10 s). Final per-second files land here after END.
