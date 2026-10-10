# Bot side, live summary (TN10 storm, Sat 10 Oct 2026)

Updated **21:30:11 CEST / 19:30:11 UTC**, about every 10 minutes from G1 to END. Counts only, written on the box by `live-summary.py` (read-only, sends nothing). Column meanings: [go/LOGGING.md](../../go/LOGGING.md). Plan and times: [go/README.md](../../go/README.md).

## Now

| What | Value |
|---|---|
| Step | **C1500**, until 21:35 CEST / 19:35 UTC |
| Bot target (plan) | 413 tx/s |
| Bot submitted, last 10 min | 0.0 tx/s (0 tx) |
| Bot accepted on n2, last 10 min | 0.0 tx/s (0 tx) |
| Rejects, last 10 min | 0 consensus/mempool; 25 public-node transport errors |
| Senders writing rows | 15 (processes up: 15) |
| Scheduler / watchdog | running / running |
| Build started? | yes (BUILD-OK present) |
| HALT | no |

## Public nodes, last 10 min

| Node | Submits ok | Rejects | Errors | Down (s) |
|---|---:|---:|---:|---:|
| boson-10.kaspa.red | 0 | 0 | 7 | 0 |
| electron-10.kaspa.blue | 0 | 0 | 5 | 0 |
| muon-10.kaspa.blue | 0 | 0 | 4 | 0 |
| neutrino-10.kaspa.stream | 0 | 0 | 5 | 0 |
| vector-10.kaspa.green | 0 | 0 | 4 | 0 |

Rejects by class: rpc 25

## n2 (bot's private reader node) and the box

| What | Value |
|---|---|
| n2 synced / UTXO index | False / True |
| n2 sink age (lag) | 1,327.1 s |
| n2 virtual DAA score | 593,253,219 |
| Miner processes | 1 |
| Coins left (unclaimed) | 934,337 tKAS in 29,485 coins |
| Disk free / RAM available | 10 GB / 2,753 MB |

## Steps so far

| Step | Bot target | Submitted tx/s | Accepted tx/s | Rejects | Transport errors | Clean |
|---|---:|---:|---:|---:|---:|---|
| B0 | 0 | – | – | – | – | running or not evaluated |
| X250 | 66 | 66.0 | 66.0 | 0 | 1 | yes |
| X250-drain | 0 | – | – | – | – | running or not evaluated |
| C1000 | 275 | 139.3 | 139.2 | 0 | 22 | no |
| C1000-drain | 0 | – | – | – | – | running or not evaluated |
| C1500 | 413 | – | – | – | – | running or not evaluated |

## Last events

| CEST | Event | Step | Detail |
|---|---|---|---|
| 20:40:51 | sender-start | X250 | S15 mode=pub |
| 20:50:07 | coin-refresh | X250 | buffer check 934337 tKAS 29485 coins |
| 20:55:00 | step-end | X250 | X250 |
| 20:55:00 | step-start | X250-drain | X250-drain bot 0 |
| 21:00:00 | step-end | X250-drain | X250-drain |
| 21:00:00 | step-start | C1000 | C1000 bot 275 |
| 21:07:20 | disk-guard | C1000 | box disk 16.1 GB free (< 20) |
| 21:07:20 | deviation | C1000 | box disk 16.1 GB free (< 20): senders pause at 8 GB; n2 disk guard STOP at 5 GB, halt at 3 GB; pub submit fallback below 10 GB |
| 21:29:16 | deviation | C1000 | pubMode: n2 not synced, sink lag 1271.3 s > 60; senders continue on public nodes |
| 21:29:22 | coin-refresh | C1000 | buffer check 934337 tKAS 29485 coins |
| 21:29:22 | step-end | C1000 | C1000 |
| 21:29:22 | step-start | C1500 | C1500 bot 413 |

How to read: *Now* answers "is the bot sending what the plan says?"; *Public nodes* shows which node rejects or errors; *Steps so far* is the per-step verdict (clean = at least 90% of target delivered, at least 99% accepted, p90 at most 10 s). Final per-second files land here after END.
