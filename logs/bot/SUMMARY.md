# Bot side, live summary (TN10 storm, Sat 10 Oct 2026)

Updated **18:29:07 CEST / 16:29:07 UTC**, about every 10 minutes from G1 to END. Counts only, written on the box by `live-summary.py` (read-only, sends nothing). Column meanings: [go/LOGGING.md](../../go/LOGGING.md). Plan and times: [go/README.md](../../go/README.md).

## Now

| What | Value |
|---|---|
| Step | **PREP (no sends)**, until 20:00 CEST / 18:00 UTC |
| Bot target (plan) | 0 tx/s |
| Bot submitted, last 10 min | 0.0 tx/s (0 tx) |
| Bot accepted on n2, last 10 min | 0.0 tx/s (0 tx) |
| Rejects, last 10 min | 0 consensus/mempool; 0 public-node transport errors |
| Senders writing rows | 0 (processes up: 0) |
| Scheduler / watchdog | running / running |
| Build started? | not confirmed (bot does not send) |
| HALT | no |

## Public nodes, last 10 min

| Node | Submits ok | Rejects | Errors | Down (s) |
|---|---:|---:|---:|---:|
| (no sends in this window) | – | – | – | – |

## n2 (bot's private reader node) and the box

| What | Value |
|---|---|
| n2 synced / UTXO index | True / True |
| n2 sink age (lag) | 0.1 s |
| n2 virtual DAA score | 593,154,361 |
| Miner processes | 0 |
| Coins left (unclaimed) | 1,034,706 tKAS in 32,565 coins |
| Disk free / RAM available | 25 GB / 7,052 MB |

## Steps so far

| Step | Bot target | Submitted tx/s | Accepted tx/s | Rejects | Transport errors | Clean |
|---|---:|---:|---:|---:|---:|---|
| (T0 is 20:30 CEST / 18:30 UTC) | – | – | – | – | – | – |

## Last events

| CEST | Event | Step | Detail |
|---|---|---|---|
| 17:58:06 | plan | - | STP-KAS/tn10-storm-1010 go/steps-utc.json @ 39c4554 |
| 17:58:26 | coin-refresh | - | added 0 coins 0 tKAS, dropped spent 0, unclaimed 1003835.4 tKAS (22656 coins), caught up false, method block walk, 4485 blocks/18 pages, kaspad RSS peak 2038 MB |
| 17:58:46 | coin-refresh | - | added 0 coins 0 tKAS, dropped spent 0, unclaimed 1003835.4 tKAS (22656 coins), caught up false, method block walk, 3735 blocks/15 pages, kaspad RSS peak 2141 MB |
| 17:59:06 | coin-refresh | - | added 0 coins 0 tKAS, dropped spent 0, unclaimed 1003835.4 tKAS (22656 coins), caught up false, method block walk, 4242 blocks/17 pages, kaspad RSS peak 2195 MB |
| 17:59:26 | coin-refresh | - | added 0 coins 0 tKAS, dropped spent 0, unclaimed 1003835.4 tKAS (22656 coins), caught up false, method block walk, 5488 blocks/22 pages, kaspad RSS peak 2207 MB |
| 17:59:46 | coin-refresh | - | added 0 coins 0 tKAS, dropped spent 0, unclaimed 1003835.4 tKAS (22656 coins), caught up false, method block walk, 16679 blocks/67 pages, kaspad RSS peak 2196 M |
| 18:00:06 | coin-refresh | - | added 0 coins 0 tKAS, dropped spent 0, unclaimed 1003835.4 tKAS (22656 coins), caught up false, method block walk, 19183 blocks/77 pages, kaspad RSS peak 2182 M |
| 18:00:26 | coin-refresh | - | added 0 coins 0 tKAS, dropped spent 0, unclaimed 1003835.4 tKAS (22656 coins), caught up false, method block walk, 19183 blocks/77 pages, kaspad RSS peak 2209 M |
| 18:00:46 | coin-refresh | - | added 0 coins 0 tKAS, dropped spent 0, unclaimed 1003835.4 tKAS (22656 coins), caught up false, method block walk, 16206 blocks/65 pages, kaspad RSS peak 2284 M |
| 18:00:57 | coin-refresh | - | added 9909 coins 30870.7 tKAS, dropped spent 0, unclaimed 1034706.1 tKAS (32565 coins), caught up true, method block walk, 3264 blocks/16 pages, kaspad RSS peak |

How to read: *Now* answers "is the bot sending what the plan says?"; *Public nodes* shows which node rejects or errors; *Steps so far* is the per-step verdict (clean = at least 90% of target delivered, at least 99% accepted, p90 at most 10 s). Final per-second files land here after END.
