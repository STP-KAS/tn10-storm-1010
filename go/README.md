> **Experimental. We are just trying this.** [Disclaimer](../DISCLAIMER.md)

# go: the shared rule book for the bot run and the build run

Thank you, Kaspa Pulse ([@gokugalax](https://x.com/gokugalax)). The node-dead rule, the chain count right after the end, and sending him T0 ahead are his fixes ([credits](../credits/KASPA-PULSE.md)).

This page is the rule book. The two prompts are [bot-run/GO-BOT-RUN.md](bot-run/GO-BOT-RUN.md) and [build-run/GO-BUILD-RUN.md](build-run/GO-BUILD-RUN.md). Each prompt carries the same timeline and the same rates, so each side can run from its own prompt alone. Logging is [LOGGING.md](LOGGING.md). If two files here disagree on a number, the numbers in [clock.py](clock.py) win; tell stp, do not pick one silently.

**Written 10 Oct 2026, 17:43 CEST, by stp's order:** "rewrite completely, change name: bot/build run … keep what is good, cut what is bad, with everything you learned from the run … start 20h30."

## Goals

1. **Headline:** network unique accepted tx/s, counted once from chain data. Target: **over 3,000 tx/s combined**, held, with the load shared 25% bot / 75% Build (stp, 10 Oct 12:05 and 12:11 CEST).
2. A short ramp to MAX, then a **long hold** to see whether 3,200 combined lasts for hours.
3. Show that a failing node no longer spoils the run: the bot keeps its submit path off its own node, and every sender backs off a failing node instead of firing at it.
4. **Log everything** ([LOGGING.md](LOGGING.md)) on both sides, in one format, and count the chain right after END, before pruning.

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

Rates are tx/s, per side, in the send window only. "Drain" means senders 0 while logging goes on. The same steps, machine-readable in UTC: [steps-utc.json](steps-utc.json).

<!-- clock:table -->
| Step | Brussels (CEST) | UTC | Bot tx/s | Build tx/s | Combined tx/s |
|---|---|---|---|---|---|
| PREP | until 20:00 | until 18:00 | Re-armed. n2 synced. Coins topped up. No sends. Miner off. | Read this file. Desk node synced with UTXO index, coins, senders, public fallback. No sends. Miner off. | – |
| G1 | 20:00 | 18:00 | Gate 1: n2 health, coin buffer, the five public nodes reachable. Logging starts. | Gate 1: desk node health, RAM >= 4 GB free, public fallback reachable, coins, disk. Logging starts. Stop every sender not in this plan. | – |
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
| COUNT | 04:30 Sun–06:30 Sun | 02:30 Sun–04:30 Sun | Chain count from n2, before pruning | Chain count from your desk node, before pruning | – |
| PUSH | by 07:30 Sun | by 05:30 Sun | Logs to `logs/bot/` | Logs to `logs/build/`, plus `FOR-TN10-OPS-result-1010.txt` to stp | – |
<!-- /clock:table -->

## Targets

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

- **MAX:** Build may go above 2,600, never below. The bot sends 900.
- **Hold rule:** each side holds its HOLD rate if its MAX step was clean. If not, it holds its highest clean step rate from the ramp (bot: 60 if none; Build: 190 if none). Neither side raises its rate mid-step to cover the other's shortfall.
- **Clean step:** the side delivered at least 90% of its rate for the whole send window, at least 99% of its submitted transactions were seen accepted, and the p90 submit-to-accept time stayed at or under 10 s.
- **B0 and B1** are measured and reported. They do not set any rate.

## Who sends where

| Side | Submits to | Reads (health, accepted, coins, count) | Miner |
|---|---|---|---|
| Bot | **Only** the five public TN10 nodes: `muon-10.kaspa.blue`, `boson-10.kaspa.red`, `electron-10.kaspa.blue`, `neutrino-10.kaspa.stream`, `vector-10.kaspa.green` | n2, its own private pruned node (kaspad 2.1.0, UTXO index on, loopback only) | 1 thread, on n2 |
| Build | **Its own desk node (primary)**; the same five public nodes **only as fallback** when its node lags, freezes, unsyncs, dies, or desk RAM gets tight | Its own desk node | At most 1 thread, on its own node |

stp, 14:36 CEST, for the bot: "Skip your node. Only use public nodes. For now and the 17:00 test. More space, more runners." stp, 18:18 CEST, for Build: its own desk node is primary for its 75% share; the public nodes are its fallback only. Build moves the affected senders to the public nodes when its node has a sink lag over 60 s, a virtual DAA stall of 30 s, is not synced, or dies, and moves back after 2 minutes of good health. It keeps at least 4 GB RAM free on the desk. So the load on the public nodes is mostly the bot's 25%.

## Gates

- **G1, 20:00 CEST (18:00 UTC).** Each side reads its own setup: node synced (if it has one), UTXO index on, sink lag at or under 60 s, coins ready, disk free, the public nodes reachable. Logging starts. A failed read is retried for two minutes and logged. **A failed G1 never blocks the public-node senders** (lesson of 16:15 CEST, when n2's freeze failed the gate and the scheduler held the senders at 0).
- **G2, 20:15 CEST (18:15 UTC), the ready check.** Both sides started and armed. **Build started?** Build writes `FOR-TN10-OPS-ready-1010.txt` (format in [LOGGING.md](LOGGING.md#handoff-files-build-to-the-bot)) and stp passes it to the bot, or stp tells the bot "Build started". Miners on.
- **If Build is not confirmed at G2:** the bot tells stp at once. T0 does not move. The bot does not send until stp confirms Build or tells it to go alone; then it joins the open step. Every minute without that confirmation is logged as `build-not-confirmed`.

## Fees

- Both sides: **half the lanes at 400, half at 600 sompi/gram**, frozen for the step. **Floor 100** (never lower), **cap 600**.
- Why 400/600: stp asked for double fees at 14:25 CEST in the public-node test ("scale and use double fees"). The old pair was 200/300; doubled, it is 400/600. **Claim (measured on TN10):** at 400 the public-node test ran with zero rejects in its clean phase, and n2's normal fee quote read 100 at every step start the bot logged (16:30 to 17:40 CEST).
- **Sit-out:** if the normal fee quote at step start is above 400, that side sits the step out and logs `step-sit-out` with the quote.
- **Per public node:** if one public node quotes above 400 (vector-10 has quoted higher than the others before), skip that node for a minute and spread its load over the others. Log `node-quote-skip`.

## Node-dead rule (Kaspa Pulse), per node

- A sender **never fires at a dead node.** A node is dead for a sender when it gives about 20 connection or RPC errors in a row, or fails health reads for 5 s. The sender cools that node for 30 s and moves its lanes to its other live nodes. If none is live, it waits and counts no attempt. Log `node-dead` and `node-back` per node.
- A failed submit is a reject, never "sent".
- **For the bot, n2 lagging or not synced does not zero the senders** (stp, 16:19 CEST). n2 is only the bot's reader. If n2 freezes (virtual DAA still for over 3 minutes and sink lag over 3 minutes), the bot restarts n2 on the same flags, at most once per 20 minutes, and logs it. That is what fixed the 15:57 CEST freeze.
- **Build's own node:** never fire at it when its RPC fails for 5 s, it is not synced, its sink lag is over 60 s, or its virtual DAA score stops for 30 s. The affected senders move to the public fallback (`node-fallback`) and come back after 2 minutes of good health (`node-back`). If the desk node is not synced with the UTXO index by G2, Build starts on the public nodes and moves to its node when it is synced.

## Coins

- **Never list a whole address in one call.** On 2 Oct one `getUtxosByAddresses` call for the bot address pushed n0 to 9.4 GB and it was OOM-killed.
- **Bot method (Claim, measured on TN10):** read n2's UTXO index through a **read-only secondary RocksDB instance** (it does not touch the running node; about 3 s and under 200 MB for 1.8 million entries), pick old coinbase coins, consolidate them on n2 into about 49 tKAS outputs back to the bot, and add only outputs that a fresh read shows confirmed. Every coin goes through the claim ledger (claim file created exclusively, then an append-only used list), so nothing is spent twice. Today: 1,000,000 tKAS at 14:10 CEST, 250,000 at 15:13 CEST, about 138,000 at 17:40 CEST (cut short by the halt), and a further fill before G1.
- **Coin-refresh rule (stp, 12:21 CEST), both sides:** check the buffer every 30 minutes from G1 to END. Keep at least 1.5 times the remaining need unclaimed. Top up in small, memory-safe batches when it runs low. Never re-add a spent or claimed coin. Log every refresh. If the buffer cannot be kept, lower the rate and log a `deviation`; do not stop.
- **Watch memory:** abort a fill or refresh if free memory on the machine falls below 1.5 GB.

## Disk

- The bot's box shares one disk. n2's guard writes STOP at **5 GB** free and stops n2 cleanly at **3 GB** free. Bot senders pause at **8 GB** free.
- **Claim (measured on TN10):** in the public-node test, free disk on the box fell about 2 GB an hour (29 to 26.2 GB in about 90 minutes) with combined loads up to about 3,000 tx/s. **Not sure / open for debate:** whether 3,200 combined for 5 hours 25 minutes stays at that pace. If it does, the box ends near 10 GB free, above the 8 GB pause.

## Miners

- One miner per side at most, one thread, on that side's own node. On at G2, off at END.
- No miners-off check tonight (cut, see below).

## What we kept and what we cut

| | What | Why |
|---|---|---|
| Kept | B0 baseline at T0, no load | It tells us the network's own rate before our load. |
| Kept | The fixed combined targets and the 25/75 split | stp's order (12:05 and 12:11 CEST). They reach past 3,000. |
| Kept | The ramp 250 → 1,000 → 1,500 → 2,000 → 2,500 → MAX 3,500, 15-minute steps with 5-minute drains | Fixed steps, not one blast (Kaspa Pulse's method). Drains separate the steps in the count. |
| Kept | MAX, B1, long hold, final drain | The hold is the real test of "over 3,000". |
| Kept | Node-dead rule, chain count right after END, one logging format | Kaspa Pulse's fixes; they worked. |
| Kept | The bot's coin fill from n2's UTXO index through a read-only secondary RocksDB | Measured safe today: no memory spike on n2. |
| Cut | The rehearsal rows (R1 to R7) | It never ran today (G1 failed at 16:15 CEST) and it tied the senders to a gate. The bot already measured 60 tx/s clean on the public nodes (17:10–17:20 CEST). |
| Cut | The one-side-alone controls (S1, S2, S3) | Each side already counts its own accepted transactions by id, so "alone" rows add 30 minutes without changing a rate. |
| Cut | The miners-off check (OFF0, OFF, ON) | 25 minutes at 250 tx/s. A side question at low load; it does not test the 3,000 goal. Can come back in a later run. |
| Cut | "Bot sends only to n2" and the n2-lag stop for the bot | stp moved the bot to the public nodes (14:36 CEST). n2 froze at its tip at 15:57 CEST; a lagging reader must not zero the senders. |
| Cut | Gates that hold the senders at 0 | The 16:15 CEST gate failed during the n2 freeze and locked the senders, though the public nodes were fine. |
| Cut | Fee pair 200/300 with a sit-out above 200 | Replaced by 400/600 (stp's double fees, 14:25 CEST). |
| Changed | Gates: G1 20:00 and G2 20:15 CEST, with an explicit **Build started?** check | The 17:00 CEST run was halted at 17:39 CEST because Build had not been started. |
| Changed | End 04:30 CEST, eight hours after T0 | Same eight-hour length as Friday's plan, so the runs compare. The time freed by the cuts goes into a longer hold (5 h 25 min instead of 4 h 20 min). |

## Lessons from today, built in

| What happened (Claim, measured on TN10) | What the plan does now |
|---|---|
| n2's tip froze at about 15:57 CEST under the public-node test; a restart at 16:19 CEST fixed it | n2 is a reader only. A freeze of over 3 minutes triggers a restart on the same flags (at most once per 20 minutes). The senders keep going. |
| The public-node launcher spawned twice, senders piled up past 20, the rate collapsed from about 2,850 to about 200 tx/s, and the out-of-memory killer took n2 at about 14:51 CEST | One scheduler, locked. A fixed number of senders (15). Launches staggered. At most one relaunch per sender per minute, a relaunch limit per sender, and no launch while free memory is under 1.5 GB. |
| Each relaunch claimed fresh coins for every lane; the coin list ran to 0 unclaimed at about 15:10 CEST | Fewer lanes per sender and the relaunch limit. A coin buffer check every 30 minutes, with a top-up. |
| The step evaluation counted 0 submitted for the public-node senders (they keep no per-transaction file) | The evaluation counts from the senders' per-second files. |
| After a kill, a watchdog started senders again | A halt stops the watchdog first, then the scheduler, then the senders with a hard kill. |
| boson, electron and neutrino often refused connections when many senders booted at once | Staggered launches. Each sender holds four of the five nodes, picked at random, and moves its lanes off a node that fails. **Not sure / open for debate:** why those three refused. |
| Build was not started at 17:00 CEST | The ready check at G2 and the handoff file. |
| Build pushed over 3,000 tx/s into blocks from the desk last week (**Claim**) | Build's own desk node is primary for its 75% share. |
| On 9 Oct keel and locus lagged and froze about every 10 minutes; locus died at about 03:28 CEST Sat (**Claim**) | Build's senders move to the public fallback when the desk node lags or freezes, and back after 2 minutes healthy. |
| Node B likely crashed when the desk's 32 GB ran out while building its UTXO index on 9 Oct (**Not sure / open for debate**) | Keep at least 4 GB RAM free on the desk; if memory gets tight, move senders to the fallback instead of crashing the node. |

## Keep going, but fix first

stp: "If there are issues, keep going. First try to resolve the problem."

- Fix first: restart a node on the same flags, re-arm a sender, refresh coins, free disk. Log what broke and what was done.
- Then keep going: join the open step. Never rerun a finished step. Never end early. Never move T0.
- Keep going never breaks a rule: no tunnel, no second miner, no archival switch, no public peer port, no fee above the cap or below the floor, no firing at a dead node.
- Every gap and deviation goes in `events.csv` with the time and the reason.

## Lock rule

- stp sends each prompt before G2. **Once sent, it is locked.** A fix after that goes in `events.csv` as a `deviation`, not in the prompt.
- Sending is not the start. It means: be ready by G2 and follow the clock without stp watching.
- The run log records the commit SHA of the prompt that was sent.

## stp's to-do

- Paste [GO-BUILD-RUN.md](build-run/GO-BUILD-RUN.md) into Grok Build **well before 20:15 CEST**, and pass Build's `FOR-TN10-OPS-ready-1010.txt` to the bot (or tell the bot "Build started").
- Send Kaspa Pulse T0 and the suggested counting window ([Key times](#key-times)).
- After the run, pass Build's `FOR-TN10-OPS-result-1010.txt` to the bot.
