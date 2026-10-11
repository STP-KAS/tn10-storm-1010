> **Experimental. We are just trying this.** [Disclaimer](../DISCLAIMER.md)

# Write-up — TN10 storm 10–11 Oct 2026

> **Correction, 11 Oct 2026 21:45 CEST.** The first `logs/bot/chain-count.csv` counted 89 minutes twice in the 18:10-02:29Z window: minutes inside a lumped recount row (a boundary block off the final chain merges several minutes into one row) also got a value from the live chain logger, so their transactions were in the lumped row **and** in their own row. Sum 18:10-02:29Z was 38,362,793; corrected **32,299,895** (6,062,898 counted twice). The same minutes were also flagged `complete_minute=yes`, and the 'recount avg' divided lumped rows by 60 instead of by their length. Fixed file: [logs/bot/chain-count.csv](bot/chain-count.csv) (rule: [METHOD](bot/chain-count.csv.METHOD.md)); old file kept as [chain-count.csv.superseded](bot/chain-count.csv.superseded). Step numbers below are recomputed. The 3,000 line is still not met; the earlier 'recount avg above 3,000' for C2500 and MAX was an artifact and is withdrawn. The workbook `run-2026-10-10.xlsx` predates this fix.

Companion to [COMBINED.md](COMBINED.md). Figures from log files only. Clocks: plan/bot **T0 18:30Z / END 02:30Z**; Build SUMMARY **T0 15:00Z / END 23:00Z** (mismatch — align by UTC wall clock).

## What ran

Two private nodes, one miner each, no tunnels:

- **Bot:** public-node submit only; **n2** on the box for reads, coins, chain count, and mining. Scheduler on bot clock from [go/clock.py](../go/clock.py). Fees 400/600 sompi/gram.
- **Build:** own desk node primary (public fallback); fees 200/300. Joined ~**17:28Z** on a different step clock; finished PREP–C1500 as not-run; **skipped C2000** (stale coin list); ran own-clock C2500/MAX before bot T0, then HOLD@1875 from ~19:49Z until 22:45Z, DRAIN to its END 23:00Z.

Live run dir finished **2026-10-11T02:33:22Z** (FINISHED). Bot chain-count covers 17:30Z–02:29Z; recount-1m used as supporting average.

## Per-step peaks and gaps (bot clock)

| Step | Bot submit mean | Network unique median (complete) | What happened |
|---|---:|---:|---|
| X250 | 64.29 | 293.4 (n=7) | Clean bot ramp; Build still on low-rate aborted 2400 HOLD arm. |
| C1000 | 274.06 | 512.0 (n=4) | Bot near target submit; chain coverage thin; freeze coming. |
| C1500 | 0 | 251.1 (n=1) | **Zeroed** by box disk/freeze 21:08–21:29 CEST; public WS stale. |
| C2000 | 544.16 | 1,241.6 (n=6) | Recovered after sdk210 restore; bot clean. |
| C2500 | 673.68 | 2,526.3 (n=7) | Strongest pre-MAX; recount avg 2,513 (corrected; was shown as 3,426). |
| MAX | 916.69 | **2,642.4** (n=9) | Best plan-metric median; last clean bot level **990**. |
| HOLD | 638.74 | 939.1 (n=123) | Long night of WS/RPC stalls, tip rebuilds, coin buffer → 0. |

Build's desk HOLD median network unique **4,032** (175 min) is on **Build's clock and desk count** — useful context, not the plan pass/fail.

## Node-dead / miners

- Bot senders follow the public-node node-dead rule (move off a dead peer; do not die with it). Night notes record many pubMode / WS stall deviations and mass sender TERM/KILL + tip rebuilds (fixes #7–#17).
- Miner briefly OFF when n2 not synced (e.g. timeline 00:12Z, 01:07Z, 02:13Z), then back.
- **END 02:30Z:** timeline `miner OFF: 02:30 UTC end`; `END … senders 0 and stop, miner off`; after-END wrap **senders=0 miner=0**, n2 left running.

## What broke

1. **21:08–21:29 CEST disk/freeze** — box shell dead; disk freefall; C1500 zero; C1000 hurt.
2. **sdk210 accidental delete** during night-watch reclaim — restored from identical 2.1.0 copy; C2000 then ran.
3. **n2 utxoindex removed ~21:58 CEST** (~19:58Z) for disk — n2 restarted without `--utxoindex`; coin refresh/top-up no longer possible; buffer had to carry the night.
4. **HOLD WS/RPC stalls** overnight — mass relaunches; HTTP wrpc/borsh 502 often a false negative while WS submit still worked.
5. **Coin buffer → 0** late night; lane-reuse enabled; tip rebuilds after spent tips / SIGTERM tip-save pollution (KILL -9 only thereafter).
6. **Build clock mismatch / late join / C2000 skipped** — Build T0 15:00Z vs plan 18:30Z; early steps not rerun; HOLD first armed at 2400 then stopped and re-armed at **1875** (not plan 2400).

## Lessons

- One shared UTC clock file must be what both sides actually run; a second T0 makes step labels lie.
- Disk guards must never delete the SDK / sender runtime the storm needs.
- Removing utxoindex mid-run saves disk but ends coin top-ups — size the buffer for the whole HOLD first.
- Plan success = chain unique median on **complete** minutes with ≥10 samples; recount averages and a partner's desk HOLD can exceed 3,000 without passing that bar.
- Public-node endurance overnight is still the hard part (WS stalls, tip pollution, zero coins).

## Pass/fail

**3,000 tx/s plan line: not met.** Best bot-clock complete-minute median: MAX **~2,642** (n=9; corrected 11 Oct). Miners off at END: **confirmed**.
