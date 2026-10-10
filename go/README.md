> **Experimental. We are just trying this.** [Disclaimer](../DISCLAIMER.md)

# go: goals, timeline and rules

Thank you, Kaspa Pulse ([@gokugalax](https://x.com/gokugalax)). Three of today's rules are his fixes from Friday night ([credits](../credits/KASPA-PULSE.md)).

This page is the shared rule book. The two prompts are [bot/GO-BOT.md](bot/GO-BOT.md) and [build/GO-BUILD.md](build/GO-BUILD.md). Each prompt carries the same timeline, so each side can run from its own prompt alone. Logging is [LOGGING.md](LOGGING.md).

Base: TN10 ops' plan, [tn10-private @ 517fb43](https://github.com/STP-KAS/tn10-private/tree/517fb43). The clock, gates, rates and fees below are the same. If this page and that plan disagree on a number, tell stp; do not pick one silently.

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

**n2 is not ready.** At 11:27 CEST (09:27 UTC) it was still in initial sync: about 1.16M of about 6.3M headers, about 260 headers/s, 0 blocks (TN10 ops, 10 Oct). It may not be synced by the 12:15Z and 12:30Z gates, and maybe not by T0. If so, the bot's rehearsal is **not run**, and the bot joins the first send row that opens after n2 is synced. T0 does not move. Every gap is logged.

Build's desk node is new too. Build starts its sync **now**, hours before T0.

## Timeline

Rates are tx/s. "Drain" means senders 0 and the row's logging continues.

| Step id | UTC | Brussels | Bot | Build |
|---|---|---|---|---|
| PREP | until 12:15 | until 14:15 | Prepare. n2 syncing. No sends. Miner off. | Prepare. Desk node syncing. No sends. Miner off. |
| G1 | 12:15 | 14:15 | First gate on n2. Rehearsal go/no-go. | Stop every sender not in this plan. First gate on the desk node. |
| G2 | 12:30 | 14:30 | Second gate. Start 1 miner, only if n2 is synced. | Second gate. Start exactly 1 miner. |
| R1 | 12:30–12:40 | 14:30–14:40 | 60, only if both gates passed | 0 |
| R2 | 12:40–12:45 | 14:40–14:45 | 20 | 0 |
| R3 | 12:45–12:50 | 14:45–14:50 | 50 | 0 |
| R4 | 12:50–12:53 | 14:50–14:53 | 60 | 0 |
| R5 | 12:53–12:56 | 14:53–14:56 | 0 | 60 |
| R6 | 12:56–12:59 | 14:56–14:59 | 60 | 60 |
| R7 | 12:59–13:00 | 14:59–15:00 | 0 | 0 |
| **B0** | **13:00–13:10** | **15:00–15:10** | **T0.** No load. Miner on. | No load. Miner on. |
| S1 | 13:10–13:20 | 15:10–15:20 | 60 | 0 |
| S2 | 13:20–13:30 | 15:20–15:30 | 0 | 60 |
| S3 | 13:30–13:40 | 15:30–15:40 | 60 | 60 |
| X2 | 13:40–13:55, drain to 14:00 | 15:40–15:55, drain to 16:00 | 2×, bot 60 | 2×, fallback 190, or the scaled rate |
| OFF0 | 14:00–14:05 | 16:00–16:05 | Settle, 0. **Miner off.** | Settle, 0. **Miner off.** |
| OFF | 14:05–14:20, drain to 14:25 | 16:05–16:20, drain to 16:25 | Miners-off check, same rate as X2 | Miners-off check, same rate as X2 |
| ON | 14:25–14:30 | 16:25–16:30 | Settle, 0. **Miner on.** | Settle, 0. **Miner on.** |
| C1000 | 14:30–14:45, drain to 14:50 | 16:30–16:45, drain to 16:50 | bot 120 | 1,000 − bot (fallback 880) |
| C1500 | 14:50–15:05, drain to 15:10 | 16:50–17:05, drain to 17:10 | bot 240 | 1,500 − bot (fallback 1,260) |
| C2000 | 15:10–15:25, drain to 15:30 | 17:10–17:25, drain to 17:30 | bot 480 | 2,000 − bot (fallback 1,520) |
| C2500 | 15:30–15:45, drain to 15:50 | 17:30–17:45, drain to 17:50 | bot 960 | 2,500 − bot (fallback 1,540) |
| MAX | 15:50–16:05, drain to 16:15 | 17:50–18:05, drain to 18:15 | The bot's own max | Uncapped, up to 9 senders |
| B1 | 16:15–16:25 | 18:15–18:25 | No load | No load |
| HOLD | 16:25–20:45 | 18:25–22:45 | Last clean level, or 30 if none | Last clean rate, or 250 if none |
| DRAIN | 20:45–21:00 | 22:45–23:00 | Senders 0 | Senders 0 |
| END | 21:00 | 23:00 | Miner off. Live loggers stop. | Miner off. Live loggers stop. |
| COUNT | 21:00–23:00 | 23:00–01:00 | Chain count from n2 | Chain count from the desk node |
| PUSH | by 23:59 | by 01:59 Sun | Logs to [logs/bot/](../logs/bot/README.md) | Logs to [logs/build/](../logs/build/README.md) |

**B and the combined targets** (from tn10-private). B is this run's own B0, 13:00–13:10Z, with no load, on each side's own node. Do not reuse an old baseline (66 or 67). If 50 ≤ B ≤ 200, combined = (multiplier − 1) × B, and the 2× step is capped at 250. Otherwise the combined targets are 250, 1,000, 1,500, 2,000 and 2,500. The bot column is the bot's send rate. Build sends combined minus that column.

## Gates

- **G1 at 12:15Z and G2 at 12:30Z.** Each side reads its own node: synced, UTXO index on, sink lag ≤ 60 s. Sink lag = UTC now minus the timestamp of the node's sink. The other side's lag is not your gate.
- A read that errors because the node is down is retried for two minutes. A lag above 60 s is a failed gate.
- A failed gate: write **not run** for the rehearsal, keep senders at 0 until T0, and do not move T0.
- **Live gate, every second while sending:** the same health rule. A sender that fails it stops. See the node-dead rule below.

## Fees

Pair 200 and 300 sompi/gram. Half the lanes at 200, half at 300, frozen for the step from the node's quote. Cap 600, floor 200. If the node's quote is above 200, do not send that step: sit it out and log the quote.

## Miners

- **One miner per side, no more.** One thread. On that side's own node only.
- Bot: one box-CPU kaspa-miner, one thread, on n2's loopback gRPC, user agent `stp grok bot`, paying the bot's own address (kept out of git). It starts at 12:30Z only if n2 is synced; otherwise it starts when n2 is synced.
- Build: one miner on the desk node, one thread, paying Build's own address (kept out of git).
- **Both miners off 14:00–14:25Z** (16:00–16:25 CEST) for the miners-off check. Both back on at 14:25Z. Both off at 21:00Z.
- No public mining endpoint. The box's old stratum stays stopped.

## Kaspa Pulse's three fixes

1. **Node-dead rule.** A sender stops by itself, and logs a `node-dead` event, when its node stops accepting or its sink lag passes 60 s. It never fires at a dead node. A failed submit is a reject, never "sent". It starts again only after a fresh health read passes, inside the open row. (Friday from 01:28Z the sent column read about 1 million a minute at a dead locus.)
2. **Chain count right after the end.** Both nodes are pruned. The COUNT row runs 21:00–23:00Z, before older blocks are pruned: per minute, network unique accepted tx, blocks, and our mined blocks, from 12:00Z to 21:00Z.
3. **T0 to Kaspa Pulse a few hours ahead.** A to-do for **stp**, not for the bots. Suggested window for his counter: 12:25Z to 21:05Z (14:25–23:05 CEST).

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

- Send Kaspa Pulse T0 13:00Z and the suggested counting window, a few hours ahead.
- Decide on his ask for the actual miner payout address, privately. It never goes in this repo.
- Send GO-BOT.md and GO-BUILD.md about an hour before T0.
