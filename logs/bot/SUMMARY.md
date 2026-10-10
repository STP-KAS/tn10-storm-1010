# Bot side, live summary (TN10 storm, Sat 10 Oct 2026)

Updated **22:15:17 CEST / 20:15:17 UTC**, about every 10 minutes from G1 to END. Counts only, written on the box by `live-summary.py` (read-only, sends nothing). Column meanings: [go/LOGGING.md](../../go/LOGGING.md). Plan and times: [go/README.md](../../go/README.md).

## Now

| What | Value |
|---|---|
| Step | **C2500-drain**, until 22:20 CEST / 20:20 UTC |
| Bot target (plan) | 0 tx/s |
| Bot submitted, last 10 min | 668.0 tx/s (400,815 tx) |
| Bot accepted on n2, last 10 min | 669.5 tx/s (401,696 tx) |
| Rejects, last 10 min | 1 consensus/mempool; 722 public-node transport errors |
| Senders writing rows | 15 (processes up: 15) |
| Scheduler / watchdog | running / running |
| Build started? | yes (BUILD-OK present) |
| HALT | no |

## Public nodes, last 10 min

| Node | Submits ok | Rejects | Errors | Down (s) |
|---|---:|---:|---:|---:|
| boson-10.kaspa.red | 88,088 | 0 | 268 | 0 |
| electron-10.kaspa.blue | 74,629 | 0 | 185 | 0 |
| muon-10.kaspa.blue | 66,860 | 0 | 0 | 0 |
| neutrino-10.kaspa.stream | 82,971 | 0 | 0 | 0 |
| vector-10.kaspa.green | 88,267 | 1 | 269 | 0 |

Rejects by class: already_in_mempool 1, rpc 722

## n2 (bot's private reader node) and the box

| What | Value |
|---|---|
| n2 synced / UTXO index | True / False |
| n2 sink age (lag) | 0.4 s |
| n2 virtual DAA score | 593,293,092 |
| Miner processes | 1 |
| Coins left (unclaimed) | 719,142 tKAS in 22,767 coins |
| Disk free / RAM available | 41 GB / 5,144 MB |

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
| C2500 | 688 | – | – | – | – | running or not evaluated |
| C2500-drain | 0 | – | – | – | – | running or not evaluated |

## Last events

| CEST | Event | Step | Detail |
|---|---|---|---|
| 21:58:26 | node-restart | C2000-drain | kaspad pid changed (n2 restarted on the same flags by its guard), uptime 1 s |
| 21:59:25 | coin-refresh | C2000-drain | buffer check 831799 tKAS 26273 coins |
| 22:00:00 | step-end | C2000-drain | C2000-drain |
| 22:00:00 | step-start | C2500 | C2500 bot 688 |
| 22:04:41 | sender-relaunch | C2500 | S6 relaunch 5/30 |
| 22:04:41 | sender-start | C2500 | S6 mode=pub |
| 22:04:44 | sender-relaunch | C2500 | S14 relaunch 5/30 |
| 22:04:44 | sender-start | C2500 | S14 mode=pub |
| 22:04:47 | sender-relaunch | C2500 | S15 relaunch 5/30 |
| 22:04:47 | sender-start | C2500 | S15 mode=pub |
| 22:15:00 | step-end | C2500 | C2500 |
| 22:15:00 | step-start | C2500-drain | C2500-drain bot 0 |

How to read: *Now* answers "is the bot sending what the plan says?"; *Public nodes* shows which node rejects or errors; *Steps so far* is the per-step verdict (clean = at least 90% of target delivered, at least 99% accepted, p90 at most 10 s). Final per-second files land here after END.
