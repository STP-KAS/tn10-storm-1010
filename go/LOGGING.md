> **Experimental. We are just trying this.** [Disclaimer](../DISCLAIMER.md)

# LOGGING: log everything that can be found

Both sides log the same files, with the same columns, so the bot's minutes, Build's minutes and Kaspa Pulse's minutes line up row by row. Plan: [go/README.md](README.md). Prompts: [bot run](bot-run/GO-BOT-RUN.md), [build run](build-run/GO-BUILD-RUN.md).

## Format, both sides

- CSV, UTF-8, comma, one header row, LF line ends.
- Time in UTC, ISO 8601 with `Z`. Seconds: `2026-10-10T18:30:05Z`. Minutes: `2026-10-10T18:30Z` (the same as Kaspa Pulse's CSV). Reports to stp give CEST first, UTC second.
- `side` is `bot` or `build`. `step` is the step id from the [timeline](README.md#timeline): `G1`, `G2`, `B0`, `X250`, `C1000`, `C1500`, `C2000`, `C2500`, `MAX`, `B1`, `HOLD`, `DRAIN`, `COUNT`; a drain after a step is `<step>-drain`.
- An empty cell means **not measured**. Never write 0 for not measured.
- Log the clock offset at the start and at the end (`ntp.csv`).
- **Counts only in git.** No txid, key, seed, host IP, port or wallet address. The public node names (`muon-10.kaspa.blue` and so on) are allowed. Per-transaction logs and ids stay on the machine that made them.
- Logging runs from G1 to END, even when a side sends nothing. The COUNT file runs after.

## Files

| File | Rate | Columns |
|---|---|---|
| `sec.csv` | every second | `utc, side, step, target_tx_s, senders_live, sent, submit_ok, rejects, node_accepted, mempool_size, sink_lag_s, synced, utxoindex, virtual_daa_score, sink_blue_score, feerate_quote, fee_low, fee_high, node_state` |
| `minute.csv` | every minute | `minute_utc, side, step, target_tx_s, sent, submit_ok, rejects, node_accepted, network_unique_accepted, blocks, tx_per_block, our_mined_blocks, mempool_max, sink_lag_max_s, synced_all_minute, cpu_pct_max, ram_free_gb_min, disk_free_gb_min, node_state` |
| `public-nodes.csv` | every minute, per public node | `minute_utc, side, node, submit_ok, rejects, errors, cooled_s, quote_skip` |
| `rejects.csv` | every second with a reject | `utc, side, step, reason, count` (`fee-too-low`, `mempool-full`, `orphan`, `double-spend`, `mass`, `rpc-timeout`, `rpc-closed`, `other`) |
| `miner.csv` | every 10 s | `utc, side, miner_state, threads, hashrate_hs, blocks_found, blocks_accepted, blocks_rejected` |
| `host.csv` | every 10 s | `utc, side, cpu_pct, kaspad_cpu_pct, ram_free_gb, kaspad_rss_gb, disk_free_gb, datadir_gb, net_in_kbs, net_out_kbs, peers_out, senders_up` |
| `node.csv` | every 10 s | `utc, side, synced, utxoindex, sink_lag_s, virtual_daa_score, sink_blue_score, header_count, block_count, mempool_size, kaspad_uptime_s, pruning_point_changed` |
| `events.csv` | each event | `utc, side, step, event, detail` |
| `steps.csv` | each step | `step, side, start_utc, end_utc, target_tx_s, mean_sent, mean_submit_ok, mean_node_accepted, rejects, zero_seconds, fee_low, fee_high, clean, reason` |
| `gates.csv` | each gate read | `utc, side, gate, synced, utxoindex, sink_lag_s, result` |
| `ntp.csv` | start and end | `utc, side, when, offset_ms, source` |
| `chain-count.csv` | COUNT, per minute from one hour before T0 to END | `minute_utc, side, network_unique_accepted, accepted_tx_per_s, blocks, our_mined_blocks, complete_minute` |
| `confirm.csv` | each step | `step, side, fee_tier, n, p50_s, p90_s, max_s` |
| `SUMMARY.md` | once | Counts per step, what broke, what was done |

A side without its own node (Build option A) leaves the node columns empty and skips `node.csv`, `miner.csv` and `chain-count.csv`.

### Events

One `events.csv` row for each: `gate`, `build-confirmed`, `build-not-confirmed` (each minute without it, from G2), `step-start`, `step-end`, `step-sit-out` (the quote), `sender-start`, `sender-relaunch` (count so far), `sender-pause`, `sender-stop`, **`node-dead`**, **`node-back`** (both with the node name), `node-quote-skip`, `node-lag`, `node-restart`, `miner-on`, `miner-off`, `coin-refresh` (coins and tKAS added, unclaimed after, memory low point), `disk-guard`, `halt`, `deviation` (what and why).

### Words used

- **sent**: the sender called submit. **submit_ok**: the node took it. A failed submit is a reject, never sent-and-ok.
- **node_accepted**: own transactions seen accepted on the virtual chain of the node the side reads.
- **network_unique_accepted**: every accepted transaction in that minute on the virtual chain, each id once, all senders. This is the headline. It is never added across sides; the two sides' counts of the same network are a check on each other.
- **node_state**: `ok`, `lag` (sink lag over 60 s), `dead` (RPC down or not accepting), `syncing`.

### Counting rule (lesson of 17:21 CEST)

Count `sent`, `submit_ok` and `node_accepted` from the senders' own per-second records. If a sender keeps no per-transaction file, the step counts still come from its per-second file. A step that shows 0 sent while the senders logged sends is a counting bug: fix it and re-count, and log the fix as a `deviation`.

## Node-dead rule (Kaspa Pulse's fix)

- **Per public node:** about 20 connection or RPC errors in a row cools that node for 30 s; the load moves to the sender's other live nodes. No live node: wait, count no attempt.
- **Own node used for submits:** stop when RPC fails for 5 s, `synced` is false, sink lag is over 60 s, or the virtual DAA score is still for 30 s.
- A reader node (the bot's n2) that lags does not stop the senders; its lag is logged.
- While a sender has no live node, its `sent` is 0. The sender starts again only after a fresh read passes, and writes `node-back`.

## Handoff files, Build to the bot

The bot cannot see Build's screen. Build writes these two plain-text files; stp pastes them to the bot. `key: value`, one per line, CEST times.

**`FOR-TN10-OPS-ready-1010.txt`** (at G2, 20:15 CEST):

```
build_started: yes
written_cest: 20:14
option: A | B | C            (A public nodes, B own node, C own node for reads + public nodes for submits)
senders: <n>
coins_ready_tkas: <n>
fee_pair: 400/600
own_node_synced: yes | no | none
miner: on | off | none
step_file_t0: 2026-10-10T18:30:00Z
notes: <anything the bot should know>
```

**`FOR-TN10-OPS-result-1010.txt`** (after END, by 06:30 CEST):

```
step, target_tx_s, mean_sent, mean_submit_ok, mean_accepted, rejects, clean, reason
B0, 0, ...
X250, 190, ...
...
HOLD, 2400, ...
events: node deaths (node, CEST from–to), restarts, sit-outs, deviations
hold_rate_used: <n> (why)
```

## After the run

1. COUNT, the two hours after END: `chain-count.csv` from the own node, before pruning.
2. `steps.csv` and `SUMMARY.md`.
3. Copy the files to `logs/bot/` or `logs/build/` in this repo. Keep raw per-transaction logs and ids local.
