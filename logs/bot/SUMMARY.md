# Bot side, live summary (TN10 storm, Sat 10 Oct 2026)

Updated **21:45:19 CEST / 19:45:19 UTC**, about every 10 minutes from G1 to END. Counts only, written on the box by `live-summary.py` (read-only, sends nothing). Column meanings: [go/LOGGING.md](../../go/LOGGING.md). Plan and times: [go/README.md](../../go/README.md).

## Now

| What | Value |
|---|---|
| Step | **C2000**, until 21:55 CEST / 19:55 UTC |
| Bot target (plan) | 550 tx/s |
| Bot submitted, last 10 min | 282.9 tx/s (169,727 tx) |
| Bot accepted on n2, last 10 min | 275.9 tx/s (165,511 tx) |
| Rejects, last 10 min | 1 consensus/mempool; 2,881 public-node transport errors |
| Senders writing rows | 15 (processes up: 14) |
| Scheduler / watchdog | running / running |
| Build started? | yes (BUILD-OK present) |
| HALT | no |

## Public nodes, last 10 min

| Node | Submits ok | Rejects | Errors | Down (s) |
|---|---:|---:|---:|---:|
| boson-10.kaspa.red | 27,904 | 1 | 679 | 0 |
| electron-10.kaspa.blue | 37,665 | 0 | 503 | 0 |
| muon-10.kaspa.blue | 42,463 | 0 | 618 | 0 |
| neutrino-10.kaspa.stream | 30,842 | 0 | 618 | 0 |
| vector-10.kaspa.green | 30,853 | 0 | 463 | 0 |

Rejects by class: already_in_mempool 1, rpc 2,881

## n2 (bot's private reader node) and the box

| What | Value |
|---|---|
| n2 synced / UTXO index | True / True |
| n2 sink age (lag) | 0.4 s |
| n2 virtual DAA score | 593,274,458 |
| Miner processes | 1 |
| Coins left (unclaimed) | 838,114 tKAS in 26,473 coins |
| Disk free / RAM available | 28 GB / 4,028 MB |

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
| C2000 | 550 | – | – | – | – | running or not evaluated |

## Last events

| CEST | Event | Step | Detail |
|---|---|---|---|
| 21:39:37 | sender-relaunch | C1500-drain | S12 relaunch 3/8 |
| 21:39:37 | sender-start | C1500-drain | S12 mode=pub |
| 21:39:40 | sender-relaunch | C1500-drain | S13 relaunch 3/8 |
| 21:39:40 | sender-start | C1500-drain | S13 mode=pub |
| 21:39:43 | sender-relaunch | C1500-drain | S14 relaunch 3/8 |
| 21:39:43 | sender-start | C1500-drain | S14 mode=pub |
| 21:40:00 | step-end | C1500-drain | C1500-drain |
| 21:40:00 | step-start | C2000 | C2000 bot 550 |
| 21:43:33 | sender-relaunch | C2000 | S1 relaunch 4/8 |
| 21:43:33 | sender-start | C2000 | S1 mode=pub |
| 21:44:39 | sender-relaunch | C2000 | S1 relaunch 5/8 |
| 21:44:39 | sender-start | C2000 | S1 mode=pub |

How to read: *Now* answers "is the bot sending what the plan says?"; *Public nodes* shows which node rejects or errors; *Steps so far* is the per-step verdict (clean = at least 90% of target delivered, at least 99% accepted, p90 at most 10 s). Final per-second files land here after END.
