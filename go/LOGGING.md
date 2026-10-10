> **Experimental. We are just trying this.** [Disclaimer](../DISCLAIMER.md)

# LOGGING: log everything that can be found

Both sides log the same files, with the same columns, so the bot's minutes, Build's minutes and Kaspa Pulse's minutes line up row by row.

## Format, both sides

- CSV, UTF-8, comma, one header row, LF line ends.
- Time in UTC, ISO 8601 with `Z`. Seconds: `2026-10-10T15:00:05Z`. Minutes: `2026-10-10T15:00Z` (the same as Kaspa Pulse's CSV).
- `side` is `bot` or `build`. `step` is the step id from the [timeline](README.md#timeline) (`G1`, `R1` … `B0`, `S1`, `X2`, `OFF`, `C1000` … `MAX`, `B1`, `HOLD`, `DRAIN`, `COUNT`).
- An empty cell means **not measured**. Never write 0 for not measured.
- Clocks NTP-synced. Log the offset at the start and at the end (`ntp.csv`).
- **Counts only in git.** No txid, key, seed, host, IP, port or address. Per-transaction logs and ids stay on the machine that made them.
- Logging runs from G1 to END ([times](README.md#key-times)), even when a side sends nothing. The COUNT file runs after.

## Files

| File | Rate | Columns |
|---|---|---|
| `sec.csv` | every second | `utc, side, step, target_tx_s, senders_live, sent, submit_ok, rejects, node_accepted, mempool_size, sink_lag_s, synced, utxoindex, virtual_daa_score, sink_blue_score, feerate_quote, fee_low, fee_high, node_state` |
| `minute.csv` | every minute | `minute_utc, side, step, target_tx_s, sent, submit_ok, rejects, node_accepted, network_unique_accepted, blocks, tx_per_block, our_mined_blocks, mempool_max, sink_lag_max_s, synced_all_minute, cpu_pct_max, ram_free_gb_min, disk_free_gb_min, node_state` |
| `rejects.csv` | every second with a reject | `utc, side, step, reason, count` (reason as the node returns it, shortened: `fee-too-low`, `mempool-full`, `orphan`, `double-spend`, `mass`, `rpc-timeout`, `rpc-closed`, `other`) |
| `miner.csv` | every 10 s | `utc, side, miner_state, threads, hashrate_hs, blocks_found, blocks_accepted, blocks_rejected` |
| `host.csv` | every 10 s | `utc, side, cpu_pct, kaspad_cpu_pct, ram_free_gb, kaspad_rss_gb, disk_free_gb, datadir_gb, net_in_kbs, net_out_kbs, peers_out` |
| `node.csv` | every 10 s | `utc, side, synced, utxoindex, sink_lag_s, virtual_daa_score, sink_blue_score, header_count, block_count, mempool_size, kaspad_uptime_s, pruning_point_changed` |
| `events.csv` | each event | `utc, side, step, event, detail` |
| `steps.csv` | each step | `step, side, start_utc, end_utc, target_tx_s, mean_sent, mean_submit_ok, mean_node_accepted, rejects, zero_seconds, fee_low, fee_high, clean, reason` |
| `gates.csv` | each gate read | `utc, side, gate, synced, utxoindex, sink_lag_s, result` |
| `ntp.csv` | start and end | `utc, side, when, offset_ms, source` |
| `chain-count.csv` | COUNT, per minute from one hour before T0 to END | `minute_utc, side, network_unique_accepted, accepted_tx_per_s, blocks, our_mined_blocks, complete_minute` |
| `confirm.csv` | each step | `step, side, fee_tier, n, p50_s, p90_s, max_s` (submit to accept, from the local per-tx log) |
| `order.csv` | each step | `step, side, n, reordered, reordered_pct` (send order vs accept order) |
| `SUMMARY.md` | once | Counts only, per step, plus what broke and what was done |

### Events

Write one `events.csv` row for each of these: `gate`, `step-start`, `step-end`, `step-sit-out` (detail: the fee quote), `sender-start`, `sender-pause`, `sender-stop`, `sender-rearm`, **`node-dead`**, **`node-back`**, `node-lag` (detail: the lag), `node-restart`, `miner-on`, `miner-off`, `coin-refresh`, `disk-guard`, `deviation` (detail: what and why), `not-run` (detail: why).

### Words used

- **sent**: the sender called submit. **submit_ok**: the node took it into its mempool. A failed submit is a reject, never sent-and-ok.
- **node_accepted**: own transactions seen accepted on the own node's virtual chain.
- **network_unique_accepted**: every accepted transaction in that minute on the virtual chain, each id once, all senders. This is the headline. It is not added across sides; the two sides' counts of the same network are a check on each other.
- **node_state**: `ok`, `lag` (sink lag over 60 s), `dead` (RPC down or not accepting), `syncing`.

## Node-dead rule (Kaspa Pulse's fix)

A sender stops itself and writes `node-dead` when any of these holds:

- RPC errors or times out for 5 s in a row,
- `synced` is false, or sink lag is over 60 s,
- the virtual DAA score does not move for 30 s.

While `node_state` is not `ok`, `sent` is 0 for that side. Submit attempts are not counted as sent. The sender starts again only after a fresh health read passes, and writes `node-back`.

## After the run

1. COUNT, the two hours after END: write `chain-count.csv` from the own node, before pruning.
2. Write `steps.csv` and `SUMMARY.md`.
3. Copy the files to `logs/bot/` or `logs/build/` in this repo. Keep raw per-tx logs and ids local.
