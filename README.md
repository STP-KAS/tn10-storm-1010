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

## Why

Same 8-hour plan as Friday night. Friday failed because the shared desk node **locus** died at about 01:28 UTC and the senders kept firing at it. Kaspa Pulse's count shows the chain at base load (about 55 tx/s) from then on ([his notes](credits/kaspa-pulse/2026-10-09-night/tn10-2026-10-09-2125-0535-notes.txt)). The bot's node **keel** sat behind a tunnel and lagged. Saturday's take 2 on the same desk nodes hit two more locus aborts and was halted at 08:06 UTC. So today: same plan, each side on its own node, and a sender stops by itself when its node dies.

## Plans, old and new

| Plan | Nodes | Result |
|---|---|---|
| Up to 8 Oct | Box node n0 (+ public nodes for Build) | n0 filled its disk while pruning and was retired. |
| 9 Oct night, 10 Oct take 2 ([tn10-locus](https://github.com/STP-KAS/tn10-locus)) | Two nodes on one desk: locus (Build) and keel (bot, via a tunnel) | keel lagged; locus aborted at 01:28, 06:52 and 07:26 UTC. Failed as a test of the plan. |
| **Today** ([tn10-private](https://github.com/STP-KAS/tn10-private) @ `517fb43`, refined here, clock 2 h later) | Two private, non-archival nodes on two machines: n2 (box) and Build's new desk node | This run. |

## Sources

- TN10 ops' plan: [tn10-private @ 517fb43](https://github.com/STP-KAS/tn10-private/tree/517fb43). This repo keeps its step shape, gates, rates and fees. The clock is 2 hours later (T0 15:00Z, not 13:00Z), as relayed by TN10 ops at 11:32 CEST.
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
