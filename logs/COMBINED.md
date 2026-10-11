> **Experimental. We are just trying this.** [Disclaimer](../DISCLAIMER.md)

# Combined results — TN10 storm 10–11 Oct 2026

Back to [logs/](README.md) · narrative: [WRITE-UP.md](WRITE-UP.md) · bot detail: [docs/RESULTS.md](../docs/RESULTS.md) · history: [history/MASTER.md](../history/MASTER.md)

**Clocks.** Plan / bot clock ([go/clock.py](../go/clock.py)): **T0 2026-10-10T18:30:00Z**, **END 2026-10-11T02:30:00Z**, HOLD through 02:15Z. Build's SUMMARY used a **different clock** (T0 15:00Z, END 23:00Z) and joined ~17:28Z. Tables below use **UTC wall clock** for alignment. Do not add bot + Build submit as network unique.

**Success line.** Network unique accepted ≥ **3,000 tx/s**, median of a step's **complete** chain-count minutes (`complete_minute=yes`), ≥10 valid minutes, counted once. **Not met** on that metric (best: MAX **2,644.9**, n=12).

**Sources.** Bot: [logs/bot/steps.csv](bot/steps.csv), [chain-count.csv](bot/chain-count.csv), [recount-1m.csv](bot/recount-1m.csv), [SUMMARY.md](bot/SUMMARY.md). Build: [logs/build/steps.csv](build/steps.csv), [minute.csv](build/minute.csv), [SUMMARY.md](build/SUMMARY.md).

## Per-step table (bot clock windows)

Network unique = median of `accepted_tx_per_s` on bot [chain-count.csv](bot/chain-count.csv) where `complete_minute=yes`, window `[start, end)`. Recount avg = mean of `unique_accepted_s` on [recount-1m.csv](bot/recount-1m.csv) in the same window (supporting; thinner coverage on freeze gaps). Bot submit = `mean_submit_ok` from [bot/steps.csv](bot/steps.csv). Build submit = mean of `submit_ok/60` from [build/minute.csv](build/minute.csv) over the **same UTC window** (Build's own step name may differ because of its clock).

| Step | Window UTC | Combined target | Bot submit mean | Build submit mean (UTC-overlap) | Network unique median (complete) | Recount avg | 3000 line? | Notes |
|---|---|---:|---:|---:|---:|---:|---|---|
| X250 | 18:40–18:55 | 256 | 64.29 | 174.1 (n=15) | **293.6** (n=11) | 402.3 (n=11) | no | Bot clean. Build still on aborted first HOLD arm (label 2400, low submit). Build's own-clock C2500/MAX were earlier (17:31–18:15Z). |
| C1000 | 19:00–19:15 | 1,025 | 274.06 | 172.5 (n=15) | **512.0** (n=6) | 1,194.9 (n=6) | no (n&lt;10) | Bot unclean (lag). Disk/freeze approaching. Complete minutes thin. |
| C1500 | 19:20–19:35 | 1,538 | 0 | 163.5 (n=15) | **245.9** (n=2) | 1,506.2 (n=2) | no (n&lt;10) | Bot zeroed by 21:08–21:29 CEST box freeze (stale public WS). |
| C2000 | 19:40–19:55 | 2,050 | 544.16 | 1,193.0 (n=9) | **796.5** (n=11) | 2,093.2 (n=10) | no | Bot clean after sdk210 restore. Build re-armed HOLD at 1875 from ~19:49Z (partial window; earlier minutes still ~177 on 2400 arm). Build skipped own-clock C2000 (stale coin list). |
| C2500 | 20:00–20:15 | 2,563 | 673.68 | 1,754.1 (n=15) | **2,526.3** (n=11) | 3,426.4 (n=11) | no | Bot clean. Build on HOLD@1875. Recount avg &gt;3000 (supporting only). |
| MAX | 20:20–20:35 | 3,590 | 916.69 | 1,617.0 (n=15) | **2,644.9** (n=12) | 3,271.5 (n=12) | **no** | Best plan-metric median. Bot clean (last clean level 990). Recount avg &gt;3000 (supporting). |
| HOLD | 20:50–02:15 | 3,280 | 638.74 | 1,529.0 (n=129; Build ended 23:00Z) | **936.5** (n=177) | 2,145.3 (n=173) | no | Bot unclean (WS/RPC stalls, coin buffer). Build HOLD own-clock median network unique **4,032** over 175 min on desk count (see below) — not the plan clock. |

Peak complete-minute on bot chain-count (any time in file): **2,765.7** tx/s at 21:55Z. MAX-window peak complete: **2,734.7** at 20:26Z.

### Reconciliation with docs/RESULTS.md

Earlier [docs/RESULTS.md](../docs/RESULTS.md) used slightly different chain medians / n (closer to all minutes with a rate, e.g. X250 298.3 n=15, MAX 2,642.4 n=15). **This page prefers `complete_minute=yes`**, which matches the plan's "valid complete minutes" rule. Recount averages agree with RESULTS (within rounding).

## Build on its own clock (do not mix into plan pass/fail)

From [logs/build/SUMMARY.md](build/SUMMARY.md) / [steps.csv](build/steps.csv):

| Build step | Build window UTC | Build target | Build submit (steps mean / SUMMARY median) | Build network unique median | Notes |
|---|---|---:|---:|---|---|
| C2500 | 17:31–17:50 (SUMMARY eval 17:40–17:44) | 1,875 | mean 1,949 / med 1,778 | 2,505 (5 min) | Before bot T0. Window shorter than 10 min. |
| MAX | 17:50–18:15 (SUMMARY eval 17:55–18:04) | 2,600 | mean 2,687 / med 875 | 1,726 (10 min) | Before bot T0. steps.csv marked clean; SUMMARY says minute median under target — not clean. |
| HOLD | 19:49–22:45 | 1,875 (not 2,400) | mean 1,718 / med 1,722 | **4,032** (n=175) | 138/175 min ≥3000 on Build's desk count. First 2400 arm aborted; coin list refreshed. |
| DRAIN | 22:45–23:00 | 0 | 0 | 2,155 | Build END 23:00Z (its clock). |

## Headline

| | |
|---|---|
| Plan success line (3,000) | **Not met** — bot-clock complete-minute median, ≥10 valid minutes |
| Best plan-metric step | MAX **2,644.9** (n=12 complete) |
| Supporting recount | C2500 avg **3,426.4** (n=11); MAX avg **3,271.5** (n=12) — thinner freeze-gap coverage |
| Build HOLD (desk count, Build clock) | median **4,032** over 175 complete minutes |
| Miners at END | **Off** at 02:30Z; after-END wrap senders=0 miner=0 (bot timeline) |
| Bot last clean level | 990 (MAX) |

