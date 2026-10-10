> **Experimental. We are just trying this.** [Disclaimer](../../DISCLAIMER.md)

# GO, the build run: TN10 storm, Saturday 10 Oct 2026, T0 20:30 CEST

You are **Grok Build** on stp's Windows desk. You carry **75% of the load**. The bot carries 25% from the box. The bot's file is [GO-BOT-RUN.md](../bot-run/GO-BOT-RUN.md). The timeline and the rates are the same in both. The shared rules are in [go/README.md](../README.md).

**This prompt is locked once stp sends it.** Sending is not the start. It means: **start now, be armed by G2 (20:15 CEST)**, and follow the clock without stp watching. A fix after the lock goes in your `events.csv` as a `deviation`.

## GO

**When this repo, this folder or this file lands in Build's chat (a link or a paste), that is the GO.** No questions. Build gets ready at once: node or public nodes checked, coins checked, senders armed on this clock, and it launches at the listed times. Problems are fixed and logged as `deviation`, never turned into a question.

As soon as Build is armed, it writes `FOR-TN10-OPS-build-run.txt` with the line `BUILD STARTED <time CEST>` so stp can pass it to the bot. The bot does not send until Build is confirmed started.

<!-- clock:header -->
T0 is **20:30 CEST (18:30 UTC), Saturday 10 Oct 2026**. END is **04:30 Sun CEST (02:30 Sun UTC)**. Gate 1 20:00 CEST (18:00 UTC), Gate 2 20:15 CEST (18:15 UTC). Every time is in [Key times](#key-times) and the [Timeline](#timeline). Do not send before X250. Do not move T0.
<!-- /clock:header -->

Thank you, Kaspa Pulse ([@gokugalax](https://x.com/gokugalax)). The node-dead rule and the chain count right after END are his fixes.

## Why you must start now

The 17:00 CEST run was halted by stp at 17:39 CEST because Build had not been started. Tonight the bot **does not send** until stp confirms you have started. So: arm everything as soon as you read this, and write the ready file (below) by 20:15 CEST.

## You decide how you send

stp, 17:43 CEST: if Build operates differently, let it be. Pick **one** of these, write it down in your ready file, and keep it for the night:

- **A. The five public TN10 nodes**, as the bot does: `muon-10.kaspa.blue`, `boson-10.kaspa.red`, `electron-10.kaspa.blue`, `neutrino-10.kaspa.stream`, `vector-10.kaspa.green` (wRPC, Borsh, testnet-10). Spread your senders over all five at random. **Claim (measured on TN10):** this afternoon the bot alone pushed about 3,170 tx/s through these nodes at its peak, while you were also sending to them.
- **B. Your own desk node:** kaspad 2.1.0, `--testnet --netsuffix=10 --utxoindex`, pruned (no `--archival`), peers and RPC on loopback only, no tunnel, no public peer port, a watcher that restarts it on the same flags. It must be synced by G1.
- **C. Both:** your node for reads, the public nodes for submits.

Whatever you pick: **never submit to the bot's node**, and **never fire at a dead node** (below).

## Your rates

Send the **Build** column. Never raise your rate mid-step to cover a bot shortfall. At MAX you may go above 2,600, never below. Use as many senders as you need; a fixed number, started once, not respawned in a loop.

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

- **Hold rule:** hold 2,400 if your MAX step was clean; otherwise hold your highest clean step rate (190 if none).
- **Clean step:** you delivered at least 90% of your rate for the whole send window, at least 99% of submitted were seen accepted, p90 submit-to-accept at most 10 s.

## Fees

- Half your lanes at **400**, half at **600** sompi/gram, frozen per step. **Floor 100, cap 600.** (stp asked for double fees at 14:25 CEST; the old pair 200/300, doubled.)
- If the normal fee quote at step start is above 400, sit that step out and log `step-sit-out` with the quote.
- On public nodes: if one node quotes above 400, skip it for a minute and spread over the others.

## Node-dead rule (Kaspa Pulse)

- **Public nodes:** a node that gives about 20 connection or RPC errors in a row is cooled for 30 s and your load moves to the other live nodes. If none is live, wait and count no attempt. Log `node-dead` and `node-back` with the node name.
- **Your own node (B or C):** a sender stops itself when the node's RPC fails for 5 s, the node is not synced, its sink lag is over 60 s, or its virtual DAA score stops for 30 s. It starts again after a fresh health read passes, inside the open step.
- A failed submit is a reject, never "sent".

## Coins

- Build's own wallet and coins. Each sender has its own coins.
- **Work out your need before G1:** transactions × grams per transaction × fee. Example: your column adds up to about 54 million transactions over the run; × 1,000 grams × 500 sompi/gram that is about 270,000 tKAS of fees. Have at least 1.5 times your need ready before G1.
- **Coin-refresh rule (stp, 12:21 CEST):** check every 30 minutes; top up in small, memory-safe batches; never list a whole address in one call (that call once pushed a node to 9.4 GB and it was killed); never re-add a spent or claimed coin; log every refresh. If you cannot keep the buffer, lower your rate and log a `deviation`; do not stop.

## Your miner

- At most **one** miner, one thread, on **your own node only**, paying Build's own address (kept out of git). On at G2, off at END. No miner if you have no node (option A).

## Clock

Brussels is UTC+2. Clocks in git stay in UTC.

- **G1 (20:00 CEST):** stop every desk sender not in this plan. Read your setup: node synced (B, C) or each public node reachable (A, C), coins ready, disk free. Logging starts. A failed read is retried for two minutes and fixed; it does not move T0.
- **G2 (20:15 CEST):** write `FOR-TN10-OPS-ready-1010.txt` (below). stp passes it to the bot. Miner on.
- **One step clock.** One holder process reads one copy of [go/steps-utc.json](../steps-utc.json) as it was when stp sent this prompt. Refuse any step file whose `t0` is not `2026-10-10T18:30:00Z`. Never start a second holder.
- If you open this file after a step has ended, join the open step. Never rerun a finished step.
- If stp has to paste anything, give him **one** PowerShell block that does all of it (senders, loggers, the step clock, and the node if you chose B or C) and then needs nothing more from him. Put everything under `%USERPROFILE%\grok-build\tn10-storm-1010\`.

## Key times

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

## Timeline

<!-- clock:table -->
| Step | Brussels (CEST) | UTC | Bot tx/s | Build tx/s | Combined tx/s |
|---|---|---|---|---|---|
| PREP | until 20:00 | until 18:00 | Re-armed. n2 synced. Coins topped up. No sends. Miner off. | Read this file. Arm your node or nodes, coins and senders. No sends. Miner off. | – |
| G1 | 20:00 | 18:00 | Gate 1: n2 health, coin buffer, the five public nodes reachable. Logging starts. | Gate 1: your node health (or the public nodes), coins, disk. Logging starts. Stop every sender not in this plan. | – |
| G2 | 20:15 | 18:15 | Gate 2, **ready check**: stp confirms Build has started. Miner on. | Gate 2, **ready check**: write `FOR-TN10-OPS-ready-1010.txt`, stp passes it to the bot. Miner on. | – |
| **B0** | 20:30–20:40 | 18:30–18:40 | **T0.** No load. Miner on. | **T0.** No load. Miner on. | 0 |
| X250 | 20:40–20:55, drain to 21:00 | 18:40–18:55, drain to 19:00 | 60 | 190 | 250 |
| C1000 | 21:00–21:15, drain to 21:20 | 19:00–19:15, drain to 19:20 | 250 | 750 | 1,000 |
| C1500 | 21:20–21:35, drain to 21:40 | 19:20–19:35, drain to 19:40 | 375 | 1,125 | 1,500 |
| C2000 | 21:40–21:55, drain to 22:00 | 19:40–19:55, drain to 20:00 | 500 | 1,500 | 2,000 |
| C2500 | 22:00–22:15, drain to 22:20 | 20:00–20:15, drain to 20:20 | 625 | 1,875 | 2,500 |
| **MAX** | 22:20–22:35, drain to 22:40 | 20:20–20:35, drain to 20:40 | 900 | 2,600 (may go above, never below) | 3,500 |
| B1 | 22:40–22:50 | 20:40–20:50 | No load | No load | 0 |
| **HOLD** | 22:50–04:15 Sun | 20:50–02:15 Sun | 800 (see the hold rule) | 2,400 (see the hold rule) | 3,200 |
| DRAIN | 04:15 Sun–04:30 Sun | 02:15 Sun–02:30 Sun | Senders 0 | Senders 0 | 0 |
| **END** | 04:30 Sun | 02:30 Sun | Senders stop. Miner off. Live loggers stop. | Senders stop. Miner off. Live loggers stop. Node stays up. | – |
| COUNT | 04:30 Sun–06:30 Sun | 02:30 Sun–04:30 Sun | Chain count from n2, before pruning | Chain count from your node, before pruning (skip if you have no node) | – |
| PUSH | by 07:30 Sun | by 05:30 Sun | Logs to `logs/bot/` | Logs to `logs/build/`, plus `FOR-TN10-OPS-result-1010.txt` to stp | – |
<!-- /clock:table -->

## Log everything

From G1 to END, even when sending nothing, with the columns in [LOGGING.md](../LOGGING.md): `sec.csv`, `minute.csv`, `rejects.csv`, `host.csv`, `events.csv`, `steps.csv`, `gates.csv`, `ntp.csv`; plus `node.csv`, `miner.csv` and `chain-count.csv` if you run a node; plus `public-nodes.csv` (per minute, per public node: submits ok, rejects, errors) if you use the public nodes. Per-transaction logs and ids stay on the desk.

## Handoff files for the bot

The bot cannot see your screen. stp carries two plain-text files from you to the bot. Formats are in [LOGGING.md](../LOGGING.md#handoff-files-build-to-the-bot).

1. **`FOR-TN10-OPS-ready-1010.txt` at G2 (20:15 CEST):** started yes, option A/B/C, senders, coins ready (tKAS), fee pair, node synced (if any), miner on/off, step file `t0`.
2. **`FOR-TN10-OPS-result-1010.txt` after END (by 06:30 CEST):** one line per step: target, mean submitted, mean accepted, rejects, clean yes/no and why; plus node deaths, restarts, sit-outs and deviations.

## After END

1. **END (04:30 CEST):** senders stop, miner off, live loggers stop. Your node, if any, stays up.
2. **COUNT (04:30 to 06:30 CEST):** if you have a node, write `chain-count.csv` per minute from one hour before T0 to END, before pruning.
3. Write `steps.csv`, `SUMMARY.md` and the result handoff file.
4. **By PUSH (07:30 CEST):** commit your files to `logs/build/` in **STP-KAS/tn10-storm-1010**. Counts only. No force-push. No tags or releases.

## Never

No host IP, port, key, seed, txid or wallet address in the repo. No tunnel. No second miner. No archival. No fee above 600 or below 100. No sending to the bot's node. No firing at a dead node.
