# Bot side, live summary (TN10 storm, Sat 10 Oct 2026)

Updated **22:00:10 CEST / 20:00:10 UTC**, about every 10 minutes from G1 to END. Counts only, written on the box by `live-summary.py` (read-only, sends nothing). Column meanings: [go/LOGGING.md](../../go/LOGGING.md). Plan and times: [go/README.md](../../go/README.md).

## Now

| What | Value |
|---|---|
| Step | **C2500**, until 22:15 CEST / 20:15 UTC |
| Bot target (plan) | 688 tx/s |
| Bot submitted, last 10 min | 274.5 tx/s (164,719 tx) |
| Bot accepted on n2, last 10 min | 274.1 tx/s (164,478 tx) |
| Rejects, last 10 min | 0 consensus/mempool; 12 public-node transport errors |
| Senders writing rows | 15 (processes up: 15) |
| Scheduler / watchdog | running / running |
| Build started? | yes (BUILD-OK present) |
| HALT | no |

## Public nodes, last 10 min

| Node | Submits ok | Rejects | Errors | Down (s) |
|---|---:|---:|---:|---:|
| boson-10.kaspa.red | 27,739 | 0 | 0 | 0 |
| electron-10.kaspa.blue | 35,419 | 0 | 0 | 0 |
| muon-10.kaspa.blue | 40,945 | 0 | 0 | 0 |
| neutrino-10.kaspa.stream | 30,262 | 0 | 12 | 0 |
| vector-10.kaspa.green | 30,354 | 0 | 0 | 0 |

Rejects by class: rpc 12

## n2 (bot's private reader node) and the box

| What | Value |
|---|---|
| n2 synced / UTXO index | True / False |
| n2 sink age (lag) | 0.3 s |
| n2 virtual DAA score | 593,284,040 |
| Miner processes | 1 |
| Coins left (unclaimed) | 741,104 tKAS in 23,461 coins |
| Disk free / RAM available | 41 GB / 3,579 MB |

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

## Last events

| CEST | Event | Step | Detail |
|---|---|---|---|
| 21:56:19 | sender-relaunch | C2000-drain | S14 relaunch 4/30 |
| 21:56:19 | sender-start | C2000-drain | S14 mode=pub |
| 21:56:22 | sender-relaunch | C2000-drain | S15 relaunch 4/30 |
| 21:56:22 | sender-start | C2000-drain | S15 mode=pub |
| 21:57:55 | miner-off | C2000-drain | n2 not synced for 60 s |
| 21:58:01 | deviation | C2000-drain | pubMode: n2 utxoindex off, sink lag 66.9 s > 60, virtual DAA stalled >= 30 s; senders continue on public nodes |
| 21:58:01 | miner-on | C2000-drain | n2 synced again / process relaunch |
| 21:58:07 | node-restart | C2000-drain | kaspad pid changed (n2 restarted on the same flags by its guard), uptime 8 s |
| 21:58:26 | node-restart | C2000-drain | kaspad pid changed (n2 restarted on the same flags by its guard), uptime 1 s |
| 21:59:25 | coin-refresh | C2000-drain | buffer check 831799 tKAS 26273 coins |
| 22:00:00 | step-end | C2000-drain | C2000-drain |
| 22:00:00 | step-start | C2500 | C2500 bot 688 |

How to read: *Now* answers "is the bot sending what the plan says?"; *Public nodes* shows which node rejects or errors; *Steps so far* is the per-step verdict (clean = at least 90% of target delivered, at least 99% accepted, p90 at most 10 s). Final per-second files land here after END.
