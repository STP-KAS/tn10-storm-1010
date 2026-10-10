# Bot side, live summary (TN10 storm, Sat 10 Oct 2026)

Updated **22:30:07 CEST / 20:30:07 UTC**, about every 10 minutes from G1 to END. Counts only, written on the box by `live-summary.py` (read-only, sends nothing). Column meanings: [go/LOGGING.md](../../go/LOGGING.md). Plan and times: [go/README.md](../../go/README.md).

## Now

| What | Value |
|---|---|
| Step | **MAX**, until 22:35 CEST / 20:35 UTC |
| Bot target (plan) | 990 tx/s |
| Bot submitted, last 10 min | 912.9 tx/s (547,764 tx) |
| Bot accepted on n2, last 10 min | 912.9 tx/s (547,760 tx) |
| Rejects, last 10 min | 58 consensus/mempool; 5,360 public-node transport errors |
| Senders writing rows | 15 (processes up: 15) |
| Scheduler / watchdog | running / running |
| Build started? | yes (BUILD-OK present) |
| HALT | no |

## Public nodes, last 10 min

| Node | Submits ok | Rejects | Errors | Down (s) |
|---|---:|---:|---:|---:|
| boson-10.kaspa.red | 84,058 | 12 | 1,692 | 0 |
| electron-10.kaspa.blue | 166,841 | 24 | 759 | 0 |
| muon-10.kaspa.blue | 85,936 | 0 | 624 | 0 |
| neutrino-10.kaspa.stream | 117,126 | 7 | 886 | 0 |
| vector-10.kaspa.green | 93,803 | 15 | 1,399 | 0 |

Rejects by class: already_in_mempool 26, orphan 32, rpc 5,360

## n2 (bot's private reader node) and the box

| What | Value |
|---|---|
| n2 synced / UTXO index | True / False |
| n2 sink age (lag) | 0.5 s |
| n2 virtual DAA score | 593,301,901 |
| Miner processes | 1 |
| Coins left (unclaimed) | 719,142 tKAS in 22,767 coins |
| Disk free / RAM available | 41 GB / 4,676 MB |

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
| MAX | 990 | – | – | – | – | running or not evaluated |

## Last events

| CEST | Event | Step | Detail |
|---|---|---|---|
| 22:00:00 | step-start | C2500 | C2500 bot 688 |
| 22:04:41 | sender-relaunch | C2500 | S6 relaunch 5/30 |
| 22:04:41 | sender-start | C2500 | S6 mode=pub |
| 22:04:44 | sender-relaunch | C2500 | S14 relaunch 5/30 |
| 22:04:44 | sender-start | C2500 | S14 mode=pub |
| 22:04:47 | sender-relaunch | C2500 | S15 relaunch 5/30 |
| 22:04:47 | sender-start | C2500 | S15 mode=pub |
| 22:15:00 | step-end | C2500 | C2500 |
| 22:15:00 | step-start | C2500-drain | C2500-drain bot 0 |
| 22:20:00 | step-end | C2500-drain | C2500-drain |
| 22:20:00 | step-start | MAX | MAX bot 990 |
| 22:29:32 | coin-refresh | MAX | buffer check 719142 tKAS 22767 coins |

How to read: *Now* answers "is the bot sending what the plan says?"; *Public nodes* shows which node rejects or errors; *Steps so far* is the per-step verdict (clean = at least 90% of target delivered, at least 99% accepted, p90 at most 10 s). Final per-second files land here after END.
