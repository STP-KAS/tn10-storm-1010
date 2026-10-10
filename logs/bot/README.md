> **Experimental. We are just trying this.** [Disclaimer](../../DISCLAIMER.md)

# logs/bot

Written by TN10 ops and tn ops2 after the run. Submits: the five public TN10 nodes. Reads: n2 (the bot's private node on the box). Raw logs stay on the box; this folder gets the copy.

Status: **empty until the run.**

| File | What |
|---|---|
| `sec.csv` | Every second: sent, submit-ok, rejects, accepted, mempool, lag, sync, DAA, blue score, fees, node state |
| `minute.csv` | Every minute: the same, plus network unique accepted, blocks, our mined blocks, CPU, RAM, disk |
| `rejects.csv` | Rejects by reason |
| `miner.csv` | Miner state, hashrate, blocks found, every 10 s |
| `host.csv` | CPU, RAM, disk, datadir size, every 10 s |
| `node.csv` | Node health every 10 s |
| `public-nodes.csv` | Per minute, per public node: submits ok, rejects, errors |
| `events.csv` | Gates, steps, sender pause and stop, node-dead and node-back, restarts, miner on and off, deviations |
| `steps.csv` | One row per step, with clean yes or no |
| `gates.csv` | The G1 and G2 reads, incl. the Build-started check |
| `ntp.csv` | Clock offset at start and end |
| `chain-count.csv` | Per-minute chain count, one hour before T0 to END, made in the COUNT row before pruning |
| `confirm.csv` | Confirmation time by fee tier |
| `SUMMARY.md` | Counts per step, what broke, what was done |

Columns: [go/LOGGING.md](../../go/LOGGING.md). Counts only. Per-transaction logs and ids stay local.
