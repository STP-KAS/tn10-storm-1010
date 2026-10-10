# Bot side, live summary (TN10 storm, Sat 10 Oct 2026)

Updated **20:00:08 CEST / 18:00:08 UTC**, about every 10 minutes from G1 to END. Counts only, written on the box by `live-summary.py` (read-only, sends nothing). Column meanings: [go/LOGGING.md](../../go/LOGGING.md). Plan and times: [go/README.md](../../go/README.md).

## Now

| What | Value |
|---|---|
| Step | **G1 (no sends)**, until 20:15 CEST / 18:15 UTC |
| Bot target (plan) | 0 tx/s |
| Bot submitted, last 10 min | 0.0 tx/s (0 tx) |
| Bot accepted on n2, last 10 min | 0.0 tx/s (0 tx) |
| Rejects, last 10 min | 0 consensus/mempool; 0 public-node transport errors |
| Senders writing rows | 0 (processes up: 0) |
| Scheduler / watchdog | running / running |
| Build started? | yes (BUILD-OK present) |
| HALT | no |

## Public nodes, last 10 min

| Node | Submits ok | Rejects | Errors | Down (s) |
|---|---:|---:|---:|---:|
| (no sends in this window) | – | – | – | – |

## n2 (bot's private reader node) and the box

| What | Value |
|---|---|
| n2 synced / UTXO index | True / True |
| n2 sink age (lag) | 127.0 s |
| n2 virtual DAA score | 593,206,496 |
| Miner processes | 0 |
| Coins left (unclaimed) | 1,034,706 tKAS in 32,565 coins |
| Disk free / RAM available | 24 GB / 2,187 MB |

## Steps so far

| Step | Bot target | Submitted tx/s | Accepted tx/s | Rejects | Transport errors | Clean |
|---|---:|---:|---:|---:|---:|---|
| (T0 is 20:30 CEST / 18:30 UTC) | – | – | – | – | – | – |

## Last events

| CEST | Event | Step | Detail |
|---|---|---|---|
| 19:59:59 | deviation | - | pubMode: n2 sink lag 117.6 s > 60, virtual DAA stalled >= 30 s; senders continue on public nodes |
| 20:00:00 | deviation | - | pubMode: n2 sink lag 118.6 s > 60, virtual DAA stalled >= 30 s; senders continue on public nodes |
| 20:00:00 | gate | - | G1 fail synced true utxoindex true lag 118.6 |
| 20:00:01 | deviation | - | pubMode: n2 sink lag 119.6 s > 60, virtual DAA stalled >= 30 s; senders continue on public nodes |
| 20:00:02 | deviation | - | pubMode: n2 sink lag 120.6 s > 60, virtual DAA stalled >= 30 s; senders continue on public nodes |
| 20:00:03 | deviation | - | pubMode: n2 sink lag 121.6 s > 60, virtual DAA stalled >= 30 s; senders continue on public nodes |
| 20:00:04 | deviation | - | pubMode: n2 sink lag 122.7 s > 60, virtual DAA stalled >= 30 s; senders continue on public nodes |
| 20:00:05 | deviation | - | pubMode: n2 sink lag 123.7 s > 60, virtual DAA stalled >= 30 s; senders continue on public nodes |
| 20:00:06 | deviation | - | pubMode: n2 sink lag 124.7 s > 60, virtual DAA stalled >= 30 s; senders continue on public nodes |
| 20:00:07 | deviation | - | pubMode: n2 sink lag 125.7 s > 60, virtual DAA stalled >= 30 s; senders continue on public nodes |
| 20:00:08 | deviation | - | pubMode: n2 sink lag 126.7 s > 60, virtual DAA stalled >= 30 s; senders continue on public nodes |
| 20:00:09 | deviation | - | pubMode: n2 sink lag 127.7 s > 60, virtual DAA stalled >= 30 s; senders continue on public nodes |

How to read: *Now* answers "is the bot sending what the plan says?"; *Public nodes* shows which node rejects or errors; *Steps so far* is the per-step verdict (clean = at least 90% of target delivered, at least 99% accepted, p90 at most 10 s). Final per-second files land here after END.
