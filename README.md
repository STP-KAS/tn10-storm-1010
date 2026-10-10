> **Experimental. We are just trying this.** [Disclaimer](DISCLAIMER.md)

# tn10-storm-1010

> 📘 **[MASTER: every storm, late Sep to 10 Oct 2026, in one file](history/MASTER.md)**

**Thank you first to Kaspa Pulse ([@gokugalax](https://x.com/gokugalax)).** He counted our chain from outside, on his own two nodes, and shaped this plan with his questions, method and fixes. Every input he gave us, with its source and what we changed, is in [credits/KASPA-PULSE.md](credits/KASPA-PULSE.md).

Kaspa Testnet-10 (TN10) only. tKAS has no value. Counts only: no txid, key, seed, host, IP, port or address in this repo. This repo is public. It includes Kaspa Pulse's night count, published with his yes (as relayed by stp on 10 Oct 2026).

## What

One TN10 storm on Saturday 10 Oct 2026, run by two sides at the same time:

- **The bot** (TN10 ops, with tn ops2) on the box, on its own node **n2**.
- **Grok Build** on stp's Windows desk, on its own new desk node.

Each node is private and not archival. No shared node. No tunnel between the sides. One miner per side.

<!-- clock:key -->
| What | UTC | Brussels (CEST) |
|---|---|---|
| First gate G1 | 14:15 | 16:15 |
| Second gate G2, miners on, rehearsal | 14:30 | 16:30 |
| **T0** (B0 starts) | **15:00** | **17:00** |
| Miners off (OFF0 to ON) | 16:00–16:25 | 18:00–18:25 |
| End (END), miners off | 23:00 | 01:00 Sun |
| Chain count (COUNT) | 23:00–01:00 Sun | 01:00 Sun–03:00 Sun |
| Logs pushed (PUSH) | by 02:00 Sun | by 04:00 Sun |
| Suggested window for Kaspa Pulse's counter | 14:25–23:05 | 16:25–01:05 Sun |
<!-- /clock:key -->

All times are set in one place, [go/clock.py](go/clock.py). The full timeline is in [go/README.md](go/README.md#timeline).

## Tonight

<!-- clock:targets -->
**Changed 10 Oct 2026, 12:05 CEST, by stp:** "make sure that bot and Build go over 3,000 tx/s, share the load." The goal is now **over 3,000 tx/s combined**, with the load shared between the two sides. The scaled rule, combined = (multiplier − 1) × B, is dropped. Friday's B was about 55 to 59 tx/s, so scaling would have shrunk every step (the 2,500 step to about 1,700) and the run could never reach 3,000. **The combined targets are now fixed.** B0 is still measured and reported, but it no longer sets any rate. Times, rows, gates, fees, the node-dead rule, the miners and logging are unchanged. Only the rates changed.

Rates in tx/s, send window only (drains are 0). S1, S2, S3 and the rehearsal keep their rates from the timeline table.

| Step | UTC | Brussels (CEST) | Combined target | Bot | Build |
|---|---|---|---|---|---|
| X2 | 15:40–15:55 | 17:40–17:55 | 250 | 60 | 190 |
| OFF | 16:05–16:20 | 18:05–18:20 | 250 | 60 | 190 |
| C1000 | 16:30–16:45 | 18:30–18:45 | 1,000 | 400 | 600 |
| C1500 | 16:50–17:05 | 18:50–19:05 | 1,500 | 700 | 800 |
| C2000 | 17:10–17:25 | 19:10–19:25 | 2,000 | 950 | 1,050 |
| C2500 | 17:30–17:45 | 19:30–19:45 | 2,500 | 1,200 | 1,300 |
| MAX | 17:50–18:05 | 19:50–20:05 | 3,500 | 1,600 | 1,900 |
| HOLD | 18:25–22:45 | 20:25–00:45 Sun | 3,200 | 1,500 | 1,700 |

- **MAX:** Build may go above 1,900 (up to 9 senders), never below its share.
- **HOLD:** each side holds its HOLD rate only if it was clean at that rate or higher at MAX. If not, it holds its last clean rate (bot: or 30 if none; Build: or 250 if none). Neither side raises its rate mid-step to cover the other's shortfall.
- **Success line:** network unique accepted ≥ **3,000 tx/s**, as the median of a step's valid minutes, over at least 10 valid minutes (a valid minute is a complete minute in the chain count). The headline is counted once from chain data, never summed across the two nodes. Report the signed shape (Build) and the no-signature hop shape (bot) separately.

**Not sure / open for debate: n2's disk at 2,000+ tx/s.** On this same box, the old pruned node n0 grew 2 to 3 GB a minute under sustained load of about 2,000 tx/s or more and filled its disk. n2 has the same disk, and it also runs the UTXO index. So n2 may hit its disk guard during MAX or the long hold. If it does, the bot's senders stop (logged as `disk-guard` and `node-dead`) and Build carries on alone. Then the combined rate can fall below 3,000. We have not measured n2's growth at these rates yet.
<!-- /clock:targets -->

## Why

Same 8-hour plan as Friday night. Friday failed because the shared desk node **locus** died at about 01:28 UTC and the senders kept firing at it. Kaspa Pulse's count shows the chain at base load (about 55 tx/s) from then on ([his notes](credits/kaspa-pulse/2026-10-09-night/tn10-2026-10-09-2125-0535-notes.txt)). The bot's node **keel** sat behind a tunnel and lagged. Saturday's take 2 on the same desk nodes hit two more locus aborts and was halted at 08:06 UTC. So today: same plan, each side on its own node, and a sender stops by itself when its node dies.

## Plans, old and new

| Plan | Nodes | Result |
|---|---|---|
| Up to 8 Oct | Box node n0 (+ public nodes for Build) | n0 filled its disk while pruning and was retired. |
| 9 Oct night, 10 Oct take 2 ([tn10-locus](https://github.com/STP-KAS/tn10-locus)) | Two nodes on one desk: locus (Build) and keel (bot, via a tunnel) | keel lagged; locus aborted at 01:28, 06:52 and 07:26 UTC. Failed as a test of the plan. |
| **Today** ([tn10-private](https://github.com/STP-KAS/tn10-private) @ `517fb43`, refined here, clock 2 h later) | Two private, non-archival nodes on two machines: n2 (box) and Build's new desk node | This run. |

## Sources

- TN10 ops' plan: [tn10-private @ 517fb43](https://github.com/STP-KAS/tn10-private/tree/517fb43). This repo keeps its step shape, gates and fees. The rates changed on 10 Oct 12:05 CEST (stp): fixed combined targets, shared load, over 3,000 tx/s combined. The clock is 2 hours later (T0 15:00Z, not 13:00Z), as relayed by TN10 ops at 11:32 CEST.
- Friday and take 2: [tn10-locus](https://github.com/STP-KAS/tn10-locus), its [run report](https://github.com/STP-KAS/tn10-locus/blob/main/tn10-storm-2026-10-09/build/RUN-REPORT.md) and [abort note](https://github.com/STP-KAS/tn10-locus/blob/main/tn10-storm-2026-10-10/build/INCIDENT-0652.md).
- Method and questions: [tn10-storm-throughput-questions](https://github.com/STP-KAS/tn10-storm-throughput-questions).
- Everything earlier: [history/MASTER.md](history/MASTER.md).

## Map

| Folder | What is in it |
|---|---|
| [go/](go/README.md) | Goals, the timeline, gates, fees and rules |
| [go/bot/GO-BOT.md](go/bot/GO-BOT.md) | The prompt stp pastes to the bot |
| [go/build/GO-BUILD.md](go/build/GO-BUILD.md) | The prompt stp pastes into Grok Build |
| [go/LOGGING.md](go/LOGGING.md) | What both sides log, file names and columns |
| [logs/](logs/README.md) | Where each side drops its logs after the run ([bot](logs/bot/README.md), [Build](logs/build/README.md)) |
| [history/](history/README.md) | All earlier runs. [MASTER.md](history/MASTER.md) is the one master file |
| [credits/](credits/KASPA-PULSE.md) | Kaspa Pulse's inputs, and his night count in [kaspa-pulse/2026-10-09-night/](credits/kaspa-pulse/2026-10-09-night/README.md) |

---

Intentions are good; thought process is questionable. STP remains delusional. Si vis pacem, para bellum.
