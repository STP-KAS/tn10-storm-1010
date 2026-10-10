> **Experimental. We are just trying this.** [Disclaimer](DISCLAIMER.md)

# tn10-storm-1010: the bot run and the build run

> 📘 **[MASTER: every storm, late Sep to 10 Oct 2026, in one file](history/MASTER.md)**

**Thank you first to Kaspa Pulse ([@gokugalax](https://x.com/gokugalax)).** He counted our chain from outside, on his own two nodes, and shaped this plan with his questions, method and fixes. Every input he gave us, with its source and what we changed, is in [credits/KASPA-PULSE.md](credits/KASPA-PULSE.md).

Kaspa Testnet-10 (TN10) only. tKAS has no value. Counts only: no txid, key, seed, host IP, port or wallet address in this repo. This repo is public. The public TN10 node names below are the community resolver nodes, not ours.

**Rewritten 10 Oct 2026, 17:43 CEST, by stp's order**, for a new start at **20:30 CEST**. The 17:00 CEST run was halted by stp at 17:39 CEST because Build had not been started. Nothing from that run is resumed. The old `go/bot` and `go/build` prompts are gone; there is one plan, in two prompts.

## What

One TN10 storm on Saturday evening, 10 Oct 2026, run by two sides at the same time, on one clock:

- **The bot run**: the bot (TN10 ops, with tn ops2) on the box. It **submits only to the five public TN10 nodes**, spread at random. Its own private node **n2** is used for reads, coins, the chain count and its one miner. Prompt: [go/bot-run/GO-BOT-RUN.md](go/bot-run/GO-BOT-RUN.md).
- **The build run**: Grok Build on stp's Windows desk, with its own coins. Build sends to the same five public nodes or to its own desk node, as it decides. Prompt: [go/build-run/GO-BUILD-RUN.md](go/build-run/GO-BUILD-RUN.md).

Load split: **25% bot, 75% Build**. Goal: **over 3,000 tx/s combined**, network unique accepted, counted once.

<!-- clock:key -->
| What | Brussels (CEST) | UTC |
|---|---|---|
| Gate 1 (G1), logging starts | 20:00 | 18:00 |
| Gate 2 (G2), ready check incl. **Build started?**, miners on | 20:15 | 18:15 |
| **T0** (B0 starts) | **20:30** | **18:30** |
| First send step (X250) | 20:40 | 18:40 |
| MAX | 22:20–22:35 | 20:20–20:35 |
| Long hold (HOLD) | 22:50–04:15 Sun | 20:50–02:15 Sun |
| **END**, senders stop, miners off | **04:30 Sun** | **02:30 Sun** |
| Chain count (COUNT) | 04:30 Sun–06:30 Sun | 02:30 Sun–04:30 Sun |
| Logs pushed (PUSH) | by 07:30 Sun | by 05:30 Sun |
| Suggested window for Kaspa Pulse's counter | 20:10–04:35 Sun | 18:10–02:35 Sun |
<!-- /clock:key -->

## Tonight

<!-- clock:targets -->
| Step | Brussels (CEST) | UTC | Combined | Bot (25%) | Build (75%) |
|---|---|---|---|---|---|
| X250 | 20:40–20:55 | 18:40–18:55 | 250 | 60 | 190 |
| C1000 | 21:00–21:15 | 19:00–19:15 | 1,000 | 250 | 750 |
| C1500 | 21:20–21:35 | 19:20–19:35 | 1,500 | 375 | 1,125 |
| C2000 | 21:40–21:55 | 19:40–19:55 | 2,000 | 500 | 1,500 |
| C2500 | 22:00–22:15 | 20:00–20:15 | 2,500 | 625 | 1,875 |
| MAX | 22:20–22:35 | 20:20–20:35 | 3,500 | 900 | 2,600 |
| HOLD | 22:50–04:15 Sun | 20:50–02:15 Sun | 3,200 | 800 | 2,400 |

Fees, both sides: half the lanes at **400** and half at **600** sompi/gram, frozen per step. Floor 100, cap 600. Success line: network unique accepted at or above **3,000 tx/s**, median of a step's valid minutes, at least 10 valid minutes, counted once from chain data.
<!-- /clock:targets -->

The full timeline, with both columns, is in [go/README.md](go/README.md#timeline). All times come from one file, [go/clock.py](go/clock.py). Both prompts carry the same tables.

## Why

Earlier runs never held a clean 3,000 tx/s because a node broke under the load: n0 filled its disk (to 8 Oct), the shared desk node locus aborted three times (9 and 10 Oct morning), and today at about 15:57 CEST the bot's private node n2 froze at its tip. Each time, the senders kept firing at a node that could not take them.

Today's afternoon public-node test changed the picture (**Claim (measured on TN10)**): from one box, the bot alone reached a peak of about **3,170 tx/s** submitted (2,970 accepted) on the five public nodes, and held about **900 to 985 tx/s** clean on 14 senders, with zero rejects in the clean phase. Build sent to the same nodes at the same time. So tonight the bot submits to the public nodes and keeps n2 out of the submit path, and Build's 75% share does the heavy lifting.

## How

1. **One clock.** T0 20:30 CEST. Two gates before it, at 20:00 and 20:15 CEST. The second gate is a **ready check**: both sides must be started, and stp confirms Build is running before T0. That is the lesson of 17:39 CEST.
2. **A short ramp.** B0 (no load), then 250, 1,000, 1,500, 2,000, 2,500 combined, then MAX at 3,500 combined, a short no-load B1, and a **long hold at 3,200 combined until 04:15 CEST**. END 04:30 CEST.
3. **Senders that do not die with a node.** Each bot sender holds four of the five public nodes. A node that fails is cooled and the load moves to the others. n2 lagging does **not** zero the senders.
4. **Count from the chain.** Network unique accepted per minute, once, from chain data. Each side reports its own submitted and accepted next to it.
5. **Log everything** in one format ([go/LOGGING.md](go/LOGGING.md)). Build hands its results to the bot as a text file, because the bot cannot see Build's screen.

## Plans, old and new

| Plan | Nodes | Result |
|---|---|---|
| Up to 8 Oct | Box node n0 (+ public nodes for Build) | n0 filled its disk while pruning and was retired. |
| 9 Oct night, 10 Oct take 2 ([tn10-locus](https://github.com/STP-KAS/tn10-locus)) | Two nodes on one desk: locus (Build) and keel (bot, via a tunnel) | keel lagged; locus aborted at 03:28, 08:52 and 09:26 CEST. Failed as a test of the plan. |
| 10 Oct 17:00 CEST ([tn10-private](https://github.com/STP-KAS/tn10-private) shape, refined here) | n2 for the bot (public-node submit from 14:36 CEST), a desk node for Build | Halted by stp at 17:39 CEST: Build had not been started. The bot's S1 row (60 tx/s) was evaluated clean; S3 ran at 60 tx/s and was not evaluated before the halt. [history/2026-10-10-1700-halted.md](history/2026-10-10-1700-halted.md). |
| 10 Oct public-node test, 14:23 to 16:18 CEST (private repo `tn10-storm-1010-public-nodes`) | Bot senders on the five public nodes, n2 for reads | Peak about 3,170 bot tx/s; clean hold about 900 to 985 bot tx/s on 14 senders. Lessons are folded into this plan. |
| **Tonight, T0 20:30 CEST** (this repo) | Bot: five public nodes, n2 for reads. Build: public nodes or its own node | This run. |

## Map

| Folder | What is in it |
|---|---|
| [go/](go/README.md) | Goals, the timeline, gates, fees, rules, what we kept and what we cut |
| [go/bot-run/GO-BOT-RUN.md](go/bot-run/GO-BOT-RUN.md) | The prompt stp pastes to the bot |
| [go/build-run/GO-BUILD-RUN.md](go/build-run/GO-BUILD-RUN.md) | The prompt stp pastes into Grok Build |
| [go/LOGGING.md](go/LOGGING.md) | What both sides log, file names, columns, and Build's handoff text files |
| [go/steps-utc.json](go/steps-utc.json) | The timeline, machine-readable (UTC) |
| [logs/](logs/README.md) | Where each side drops its logs after the run ([bot](logs/bot/README.md), [Build](logs/build/README.md)) |
| [history/](history/README.md) | All earlier runs. [MASTER.md](history/MASTER.md) is the one master file |
| [credits/](credits/KASPA-PULSE.md) | Kaspa Pulse's inputs, and his night count in [kaspa-pulse/2026-10-09-night/](credits/kaspa-pulse/2026-10-09-night/README.md) |

## Certainty labels

| Label | Meaning |
|---|---|
| **Claim (measured on TN10)** | Seen on Testnet-10 by us, with a number and a source. |
| **Not sure / open for debate** | A reading that fits, but other readings fit too. |
| **Needs more testing** | One run is not enough to say. |

---

Intentions are good; thought process is questionable. STP remains delusional. Si vis pacem, para bellum.
