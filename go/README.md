> **Experimental. We are just trying this.** [Disclaimer](../DISCLAIMER.md)

# go: goals, timeline and rules

Thank you, Kaspa Pulse ([@gokugalax](https://x.com/gokugalax)). Three of today's rules are his fixes from Friday night ([credits](../credits/KASPA-PULSE.md)).

This page is the shared rule book. The two prompts are [bot/GO-BOT.md](bot/GO-BOT.md) and [build/GO-BUILD.md](build/GO-BUILD.md). Each prompt carries the same timeline, so each side can run from its own prompt alone. Logging is [LOGGING.md](LOGGING.md).

Base: TN10 ops' plan, [tn10-private @ 517fb43](https://github.com/STP-KAS/tn10-private/tree/517fb43). The step shape, gates, rates and fees below are the same. **The clock is 2 hours later** than that commit (T0 15:00Z, not 13:00Z), relayed by TN10 ops at 11:32 CEST, pending stp's confirmation. If this page and that plan disagree on a number, tell stp; do not pick one silently.

## Goals

1. **Headline:** network unique accepted tx/s, counted once from chain data. Never add the bot's accepted count to Build's.
2. Run the same 8-hour shape as Friday: rehearsal, B0, one side then the other, both, the ramp, miners-off, max, B1, long hold, drain.
3. Each side on its own private, non-archival node. Show that a dead or lagging node no longer spoils the run.
4. **Log everything that can be found** ([LOGGING.md](LOGGING.md)), on both sides, in one format.
5. Count the chain right after the end, before pruning drops the blocks.
6. Put sent next to accepted, per minute, so Kaspa Pulse's count lines up with ours.

## The two nodes

| Side | Node | Kind | Owner |
|---|---|---|---|
| Bot | **n2**, on the box | kaspad 2.1.0, testnet-10, pruned (not archival), UTXO index on, loopback only, no tunnel, no inbound peers | TN10 ops |
| Build | New node on the desk | kaspad 2.1.0, testnet-10, pruned (not archival), UTXO index on, loopback only, no tunnel, no inbound peers | Grok Build |

**n2 is not ready.** At 11:27 CEST (09:27 UTC) it was still in initial sync: about 1.16M of about 6.3M headers, about 260 headers/s, 0 blocks (TN10 ops, 10 Oct). It may not be synced by the gates (G1, G2), and maybe not by T0. If so, the bot's rehearsal is **not run**, and the bot joins the first send row that opens after n2 is synced. T0 does not move. Every gap is logged.

Build's desk node is new too. Build starts its sync **now**, hours before T0.

## Key times

All times come from [clock.py](clock.py) (one T0, every step an offset). To change the clock, edit T0 there and run `python3 go/clock.py`; it rewrites these tables, the two prompts, the front page and [steps-utc.json](steps-utc.json). Do not change times by hand.

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

## Timeline

Rates are tx/s. "Drain" means senders 0 and the row's logging continues.

<!-- clock:table -->
| Step | UTC | Brussels (CEST) | Bot | Build |
|---|---|---|---|---|
| PREP | until 14:15 | until 16:15 | Prepare. n2 syncing. No sends. Miner off. | Start node sync now. Prepare. No sends. Miner off. |
| G1 | 14:15 | 16:15 | First gate on n2. Rehearsal go/no-go. | Stop every sender not in this plan. First gate on the desk node. |
| G2 | 14:30 | 16:30 | Second gate. Start 1 miner, only if n2 is synced. | Second gate. Start exactly 1 miner. |
| R1 | 14:30–14:40 | 16:30–16:40 | 60, only if both gates passed | 0 |
| R2 | 14:40–14:45 | 16:40–16:45 | 20 | 0 |
| R3 | 14:45–14:50 | 16:45–16:50 | 50 | 0 |
| R4 | 14:50–14:53 | 16:50–16:53 | 60 | 0 |
| R5 | 14:53–14:56 | 16:53–16:56 | 0 | 60 |
| R6 | 14:56–14:59 | 16:56–16:59 | 60 | 60 |
| R7 | 14:59–15:00 | 16:59–17:00 | 0 | 0 |
| **B0** | 15:00–15:10 | 17:00–17:10 | **T0.** No load. Miner on. | **T0.** No load. Miner on. |
| S1 | 15:10–15:20 | 17:10–17:20 | 60 | 0 |
| S2 | 15:20–15:30 | 17:20–17:30 | 0 | 60 |
| S3 | 15:30–15:40 | 17:30–17:40 | 60 | 60 |
| X2 | 15:40–15:55, drain to 16:00 | 17:40–17:55, drain to 18:00 | 2×, bot 60 | 2×, fallback 190, or the scaled rate |
| OFF0 | 16:00–16:05 | 18:00–18:05 | Settle, 0. **Miner off.** | Settle, 0. **Miner off.** |
| OFF | 16:05–16:20, drain to 16:25 | 18:05–18:20, drain to 18:25 | Miners-off check, same rate as X2 | Miners-off check, same rate as X2 |
| ON | 16:25–16:30 | 18:25–18:30 | Settle, 0. **Miner on.** | Settle, 0. **Miner on.** |
| C1000 | 16:30–16:45, drain to 16:50 | 18:30–18:45, drain to 18:50 | bot 120 | 1,000 − bot (fallback 880) |
| C1500 | 16:50–17:05, drain to 17:10 | 18:50–19:05, drain to 19:10 | bot 240 | 1,500 − bot (fallback 1,260) |
| C2000 | 17:10–17:25, drain to 17:30 | 19:10–19:25, drain to 19:30 | bot 480 | 2,000 − bot (fallback 1,520) |
| C2500 | 17:30–17:45, drain to 17:50 | 19:30–19:45, drain to 19:50 | bot 960 | 2,500 − bot (fallback 1,540) |
| MAX | 17:50–18:05, drain to 18:15 | 19:50–20:05, drain to 20:15 | The bot's own max | Uncapped, up to 9 senders |
| B1 | 18:15–18:25 | 20:15–20:25 | No load | No load |
| HOLD | 18:25–22:45 | 20:25–00:45 Sun | Last clean level, or 30 if none | Last clean rate, or 250 if none |
| DRAIN | 22:45–23:00 | 00:45 Sun–01:00 Sun | Senders 0 | Senders 0 |
| **END** | 23:00 | 01:00 Sun | Miner off. Live loggers stop. | Miner off. Live loggers stop. Node stays up. |
| COUNT | 23:00–01:00 Sun | 01:00 Sun–03:00 Sun | Chain count from n2, before pruning | Chain count from the desk node, before pruning |
| PUSH | by 02:00 Sun | by 04:00 Sun | Logs to `logs/bot/` in this repo | Logs to `logs/build/` in this repo |
<!-- /clock:table -->

**B and the combined targets** (from tn10-private). B is this run's own B0 (the first ten minutes from T0), with no load, on each side's own node. Do not reuse an old baseline (66 or 67). If 50 ≤ B ≤ 200, combined = (multiplier − 1) × B, and the 2× step is capped at 250. Otherwise the combined targets are 250, 1,000, 1,500, 2,000 and 2,500. The bot column is the bot's send rate. Build sends combined minus that column.

## Gates

- **G1 and G2** (see [Key times](#key-times)). Each side reads its own node: synced, UTXO index on, sink lag ≤ 60 s. Sink lag = UTC now minus the timestamp of the node's sink. The other side's lag is not your gate.
- A read that errors because the node is down is retried for two minutes. A lag above 60 s is a failed gate.
- A failed gate: write **not run** for the rehearsal, keep senders at 0 until T0, and do not move T0.
- **Live gate, every second while sending:** the same health rule. A sender that fails it stops. See the node-dead rule below.

## Fees

Pair 200 and 300 sompi/gram. Half the lanes at 200, half at 300, frozen for the step from the node's quote. Cap 600, floor 200. If the node's quote is above 200, do not send that step: sit it out and log the quote.

## Miners

- **One miner per side, no more.** One thread. On that side's own node only.
- Bot: one box-CPU kaspa-miner, one thread, on n2's loopback gRPC, user agent `stp grok bot`, paying the bot's own address (kept out of git). It starts at G2 only if n2 is synced; otherwise it starts when n2 is synced.
- Build: one miner on the desk node, one thread, paying Build's own address (kept out of git).
- **Both miners off from OFF0 to ON** (see [Key times](#key-times)) for the miners-off check. Both back on at ON. Both off at END.
- No public mining endpoint. The box's old stratum stays stopped.

## Kaspa Pulse's three fixes

1. **Node-dead rule.** A sender stops by itself, and logs a `node-dead` event, when its node stops accepting or its sink lag passes 60 s. It never fires at a dead node. A failed submit is a reject, never "sent". It starts again only after a fresh health read passes, inside the open row. (Friday from 01:28Z the sent column read about 1 million a minute at a dead locus.)
2. **Chain count right after the end.** Both nodes are pruned. The COUNT row runs in the two hours after END, before older blocks are pruned: per minute, network unique accepted tx, blocks, and our mined blocks, from one hour before T0 to END.
3. **T0 to Kaspa Pulse a few hours ahead.** A to-do for **stp**, not for the bots. Suggested window for his counter: in [Key times](#key-times).

## Keep going, but fix first

stp: "If there are issues, keep going. First try to resolve the problem."

- A problem is fixed first: restart the node on the same flags, re-arm a sender, refresh coins, free disk. Log what broke and what was done.
- Then keep going: join the open row. Never rerun a finished row. Never end the run early. Never move T0.
- Do not stop at the first risk. Find a way that stays inside the rules.
- "Keep going" never breaks a rule: no shared node, no tunnel, no second miner, no archival switch, no public peer port, no fee above the cap, no sending at a dead or lagging node.
- Every gap and every deviation goes in `events.csv` with the time and the reason.

## Lock rule

- stp sends each prompt about an hour before T0. **Once stp sends a prompt, it is locked.** No one edits it after that.
- Sending is not the start. Sending means: **be ready by T0**, and follow the clock without stp watching.
- A fix after the lock goes in the deviations list in `events.csv`, not in the prompt.
- The run log writes the SHA of the commit that holds the sent prompt.

## stp's to-do

- Send Kaspa Pulse T0 and the suggested counting window ([Key times](#key-times)), a few hours ahead.
- Decide on his ask for the actual miner payout address, privately. It never goes in this repo.
- Send GO-BOT.md and GO-BUILD.md about an hour before T0.
