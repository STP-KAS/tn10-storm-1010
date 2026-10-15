> **Experimental. We are just trying this.** [Disclaimer](DISCLAIMER.md)
>
> **Part of [tn-master](https://github.com/STP-KAS/tn-master)**, the map of every TN10 storm. Renamed on 11 Oct 2026 from `tn10-storm-1010`; old links redirect here.
>
> ← previous storm: [tn10-storm-2026-10-09](https://github.com/STP-KAS/tn10-storm-2026-10-09) | next storm: [tn10-storm-2026-10-10-plan](https://github.com/STP-KAS/tn10-storm-2026-10-10-plan) →

# tn10-storm-2026-10-10 · Sat 10 Oct 18:10 - Sun 11 Oct 02:35 UTC (20:10-04:35 CEST): the bot run and the build run

**Window.** Count window 18:10Z Sat to 02:35Z Sun (the window set for outside counters); bot T0 18:30Z, END 02:30Z. Not to be mixed up with [tn10-storm-2026-10-11](https://github.com/STP-KAS/tn10-storm-2026-10-11) (Sun 11 Oct, 07:30-12:33 UTC).

**Status:** run finished END **04:30 CEST Sun 11 Oct 2026** (02:30 UTC). Logs on GitHub; made public after wrap-up. Kaspa Testnet-10 only; tKAS has no value.

## Map: where to find what

| Folder or file | What is in it |
|---|---|
| [README.md](README.md) | This page: map, intro, briefing, results |
| [DISCLAIMER.md](DISCLAIMER.md) | Experimental; what this repo is and is not |
| [docs/](docs/README.md) | Long pages behind the highlights below |
| [docs/TIMELINE.md](docs/TIMELINE.md) | Tonight's full timeline, step by step, CEST first, UTC second |
| [docs/RESULTS.md](docs/RESULTS.md) | Tonight's results in detail (filled after END) |
| [docs/RESULTS-public-nodes.md](docs/RESULTS-public-nodes.md) | The afternoon public-node test, 14:23 to 16:18 CEST, in short |
| [docs/LESSONS.md](docs/LESSONS.md) | Every lesson behind this plan, with labels |
| [docs/PLANS.md](docs/PLANS.md) | Plans old and new, and which repo holds each |
| [go/](go/README.md) | The plan: goals, timeline, targets, who sends where, gates, fees, node-dead rule, coins, disk, miners, kept and cut |
| [go/bot-run/](go/bot-run/GO-BOT-RUN.md) | The bot's prompt: `GO-BOT-RUN.md` |
| [go/build-run/](go/build-run/GO-BUILD-RUN.md) | Build's prompt: `GO-BUILD-RUN.md` |
| [go/LOGGING.md](go/LOGGING.md) | Every log file, every column with units, example rows, events, how to read the run in 5 minutes |
| [go/clock.py](go/clock.py) | The one source of all times; it writes every time table |
| [go/steps-utc.json](go/steps-utc.json) | The timeline, machine-readable (UTC) |
| [logs/](logs/README.md) | Where the results land |
| [logs/bot/](logs/bot/README.md) | Bot run logs; [`SUMMARY.md`](logs/bot/SUMMARY.md) is the live summary, updated every 15 min during the run |
| [logs/build/](logs/build/README.md) | Build run logs, after the run |
| [history/](history/README.md) | All earlier runs, one file each |
| [history/MASTER.md](history/MASTER.md) | The one master file: every TN10 storm, late Sep to 10 Oct 2026 |
| [credits/](credits/KASPA-PULSE.md) | Kaspa Pulse's inputs, with sources and what we changed |
| [credits/kaspa-pulse/](credits/kaspa-pulse/) | Kaspa Pulse's own counts |
| [credits/kaspa-pulse/2026-10-09-night/](credits/kaspa-pulse/2026-10-09-night/README.md) | His count of the 9 Oct night storm (CSV, notes) |
| [tn10-storm-2026-10-10-public-nodes](https://github.com/STP-KAS/tn10-storm-2026-10-10-public-nodes) | Sister repo: the afternoon public-node test, report and data |
| [tn10-storm-2026-10-10-plan](https://github.com/STP-KAS/tn10-storm-2026-10-10-plan), [tn10-storm-2026-10-09](https://github.com/STP-KAS/tn10-storm-2026-10-09) | Earlier plans (see [docs/PLANS.md](docs/PLANS.md)) |
| Kaspa Pulse ([@gokugalax](https://x.com/gokugalax), [kaspapulse.com](https://kaspapulse.com)) | Independent counts: accepted in block counts on two external nodes |

## Intro

**What.** One TN10 storm on Saturday evening, 10 Oct 2026, by two sides on one clock. The **bot run** (TN10 ops, with tn ops2, on the box) submits **only to the five public TN10 nodes**; its private node n2 is for reads, coins, the chain count and its miner. The **build run** (Grok Build on stp's desk) sends to **its own desk node**, with the five public nodes as **fallback only**. Split **25% bot, 75% Build**, with the bot's rates +10% since 19:03 CEST (Build unchanged); goal **over 3,000 tx/s combined**, network unique accepted, counted once.

**Why.** Earlier runs never held a clean 3,000 tx/s because a node broke under the load, and the senders kept firing at it. This afternoon the bot alone reached about 3,168 tx/s submitted on the public nodes, and Build pushed over 3,000 tx/s from its desk last week. Details: [docs/LESSONS.md](docs/LESSONS.md).

**How.** One clock from [go/clock.py](go/clock.py), two gates with a **Build started?** check, a short ramp, MAX, then a long hold. Senders move away from a failing node instead of dying with it (Kaspa Pulse's node-dead rule). Count from the chain, once. Log everything in one format ([go/LOGGING.md](go/LOGGING.md)).

**Thank you first to Kaspa Pulse ([@gokugalax](https://x.com/gokugalax), [kaspapulse.com](https://kaspapulse.com)).** Independent counts by Kaspa Pulse: accepted in block counts on two external nodes. He counted our chain from outside and shaped this plan with his questions, method and fixes ([credits/KASPA-PULSE.md](credits/KASPA-PULSE.md)).

## GO

Landing this repo (or `go/bot-run` / `go/build-run`) in the bot's or Build's chat is the GO: each side gets ready without questions and launches at the times in its file. Bot: [GO-BOT-RUN.md](go/bot-run/GO-BOT-RUN.md). Build: [GO-BUILD-RUN.md](go/build-run/GO-BUILD-RUN.md).

## Briefing

**Rewritten 10 Oct 2026, 17:43 CEST, by stp's order**, for a new start at 20:30 CEST (the 17:00 CEST run was halted at 17:39 CEST because Build had not started). Build's own desk node became its primary at 18:18 CEST.

- **20:00 CEST G1**: each side reads its setup, logging starts. **20:15 CEST G2**: ready check, **Build started?**, miners on. **20:30 CEST T0**.
- Ramp in 15-minute steps with 5-minute drains, MAX 22:20 CEST, long hold until 04:15 Sun CEST, END 04:30 Sun CEST. Full timeline: [docs/TIMELINE.md](docs/TIMELINE.md).
- Fees: half the lanes at 400, half at 600 sompi/gram. Node-dead rule per node. n2 lagging never zeros the bot. Rules: [go/README.md](go/README.md).

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

**Change 10 Oct 2026, 19:03 CEST (stp): bot rates +10%.** Bot column ×1.1 (X250 60→66, C1000 250→275, C1500 375→413, C2000 500→550, C2500 625→688, MAX 900→990, HOLD 800→880; bot fallback hold 60→66). Build rates unchanged. Combined targets rise to 256, 1,025, 1,538, 2,050, 2,563, 3,590 and 3,280; step labels (X250, C1000 …) are kept as names.

<!-- clock:targets -->
| Step | Brussels (CEST) | UTC | Combined | Bot (25% base +10%) | Build (75% base) |
|---|---|---|---|---|---|
| X250 | 20:40–20:55 | 18:40–18:55 | 256 | 66 | 190 |
| C1000 | 21:00–21:15 | 19:00–19:15 | 1,025 | 275 | 750 |
| C1500 | 21:20–21:35 | 19:20–19:35 | 1,538 | 413 | 1,125 |
| C2000 | 21:40–21:55 | 19:40–19:55 | 2,050 | 550 | 1,500 |
| C2500 | 22:00–22:15 | 20:00–20:15 | 2,563 | 688 | 1,875 |
| MAX | 22:20–22:35 | 20:20–20:35 | 3,590 | 990 | 2,600 |
| HOLD | 22:50–04:15 Sun | 20:50–02:15 Sun | 3,280 | 880 | 2,400 |

Bot rates +10% (stp 10 Oct 19:03 CEST); Build unchanged; step labels kept as names. Fees, both sides: half the lanes at **400** and half at **600** sompi/gram, frozen per step. Floor 100, cap 600. Success line: network unique accepted at or above **3,000 tx/s**, median of a step's valid minutes, at least 10 valid minutes, counted once from chain data.
<!-- /clock:targets -->

### Highlights

- **Who sends where:** bot = five public nodes only; Build = own desk node, public nodes as fallback (lag over 60 s, DAA stall 30 s, not synced, dead, or desk RAM under 4 GB free), back after 2 minutes healthy. [go/README.md](go/README.md#who-sends-where)
- **Gates:** a failed G1 never blocks the public-node senders; G2 needs Build confirmed started. [go/README.md](go/README.md#gates)
- **Afternoon public-node test (Claim (measured on TN10)):** bot peak about 3,168 tx/s submitted (2,969 accepted); clean hold about 880 to 985 tx/s on 14 senders, zero rejects in the clean phase, fees 400. [docs/RESULTS-public-nodes.md](docs/RESULTS-public-nodes.md)
- **What broke before, and the fix:** n0's disk, locus aborts, n2's tip freeze, the launcher overspawn, desk memory. [docs/LESSONS.md](docs/LESSONS.md)
- **After the run:** once the logs are on GitHub, TN10 ops makes this repo public. [go/README.md](go/README.md#key-times)
- **Logs, easy to read:** one format for both sides, a live bot summary every 15 min, a 5-minute reading guide. [go/LOGGING.md](go/LOGGING.md#how-to-read-the-run-in-5-minutes)

## Results

> **Correction, 11 Oct 2026 21:45 CEST.** The first `logs/bot/chain-count.csv` counted 89 minutes twice in the 18:10-02:29Z window: minutes inside a lumped recount row (a boundary block off the final chain merges several minutes into one row) also got a value from the live chain logger, so their transactions were in the lumped row **and** in their own row. Sum 18:10-02:29Z was 38,362,793; corrected **32,299,895** (6,062,898 counted twice). The same minutes were also flagged `complete_minute=yes`, and the 'recount avg' divided lumped rows by 60 instead of by their length. Fixed file: [logs/bot/chain-count.csv](logs/bot/chain-count.csv) (rule: [METHOD](logs/bot/chain-count.csv.METHOD.md)); old file kept as [chain-count.csv.superseded](logs/bot/chain-count.csv.superseded). Step numbers below are recomputed. The 3,000 line is still not met; the earlier 'recount avg above 3,000' for C2500 and MAX was an artifact and is withdrawn. The workbook `run-2026-10-10.xlsx` predates this fix.

**Filled after END (04:30 Sun CEST / 02:30 Sun UTC) and the chain count.** Combined: [`logs/COMBINED.md`](logs/COMBINED.md) · write-up: [`logs/WRITE-UP.md`](logs/WRITE-UP.md). Bot workbook: [`logs/bot/run-2026-10-10.xlsx`](logs/bot/run-2026-10-10.xlsx). Detail: [docs/RESULTS.md](docs/RESULTS.md). Build: [`logs/build/SUMMARY.md`](logs/build/SUMMARY.md).

| Key number | Value | Detail |
|---|---|---|
| Network unique accepted, best step median (tx/s) | **2,642.4** (MAX; `complete_minute=yes`, n=9, below the 10-minute rule; corrected 11 Oct, was 2,644.9 n=12) | [logs/COMBINED.md](logs/COMBINED.md) |
| HOLD median, network unique accepted (tx/s) | **939.1** (complete n=123; many WS stalls; corrected 11 Oct, was 936.5 n=177) | [logs/COMBINED.md](logs/COMBINED.md) |
| Success line (3,000 tx/s) met? | **No** on plan metric (median of ≥10 complete minutes). Corrected recount averages: C2500 2,512.7, MAX 2,617.2 (the earlier >3000 was a counting artifact, withdrawn). Build HOLD desk median **4,032** (Build clock, 175 min). | [logs/COMBINED.md](logs/COMBINED.md) |
| Bot: submit / n2-accepted mean (steps.csv) | X250 64.29/64.22 clean; C1000 274.06/273.58 unclean; C1500 0/0.69 unclean; C2000 544.16/543.69 clean; C2500 673.68/672.51 clean; **MAX 916.69/915.38 clean**; HOLD 638.74/637.93 unclean | [logs/bot/steps.csv](logs/bot/steps.csv) |
| Build: submit (own clock / UTC-overlap) | Own-clock: C2500 mean 1,949; MAX mean 2,687 (before bot T0); HOLD mean **1,718** @1875. UTC-overlap during bot C2500/MAX ~1.6–1.8k. Build T0 was 15:00Z (joined ~17:28Z). | [logs/build/](logs/build/README.md) |
| Miners at END | **Off** at 02:30Z; after-END wrap senders=0 miner=0 | [logs/bot/timeline.md](logs/bot/timeline.md) |
| Independent counts by Kaspa Pulse ([@gokugalax](https://x.com/gokugalax), [kaspapulse.com](https://kaspapulse.com)): accepted in block counts on two external nodes | 18:10Z Sat - 02:35Z Sun: **32.3 million** tx accepted; best minute **2,785 tx/s** (21:20Z). Includes ~56 tx/s base load. | [credits/kaspa-pulse/2026-10-10-night/](credits/kaspa-pulse/2026-10-10-night/README.md) |

**Comparison with Kaspa Pulse (@gokugalax, kaspapulse.com), approved by him 12 Oct 2026:** Our corrected chain count for 18:10-02:29Z is 32,299,895 tx, against Kaspa Pulse (@gokugalax, kaspapulse.com)'s 32,303,122 for the same minutes (-0.01%). Per-step means agree within a few tx/s (MAX 20:20-20:35Z: ours 2,617.2, his 2,615.3).

**Correction credit:** Our first 10 Oct chain-count.csv double-counted 89 lumped minutes (38.36M, corrected to 32.30M), fixed in d90eb26. Found by comparing with the independent count of Kaspa Pulse (@gokugalax, kaspapulse.com).

### Bot per-step headline (steps.csv means)

| Step | Target | Submit-ok mean | n2-accepted mean | Clean |
|---|---:|---:|---:|---|
| X250 | 66 | 64.29 | 64.22 | yes |
| C1000 | 275 | 274.06 | 273.58 | no (disk/freeze) |
| C1500 | 413 | 0 | 0.69 | no (21:08 disk/freeze zeroed) |
| C2000 | 550 | 544.16 | 543.69 | yes |
| C2500 | 688 | 673.68 | 672.51 | yes |
| MAX | 990 | 916.69 | 915.38 | yes |
| HOLD | 880 | 638.74 | 637.93 | no (WS/RPC stalls overnight) |


<details>
<summary><b>Certainty labels</b></summary>

| Label | Meaning |
|---|---|
| **Claim (measured on TN10)** | Seen on Testnet-10 by us, with a number and a source. |
| **Not sure / open for debate** | A reading that fits, but other readings fit too. |
| **Needs more testing** | One run is not enough to say. |

</details>

Counts only: no txid, key, seed, host IP, port or wallet address in this repo. The public TN10 node names are the community resolver nodes, not ours.

---

Si vis pacem, para bellum.
