> **Experimental. We are just trying this.** [Disclaimer](../DISCLAIMER.md)

# Combined results — TN10 storm 10–11 Oct 2026

> **Correction, 11 Oct 2026 21:45 CEST.** The first `logs/bot/chain-count.csv` counted 89 minutes twice in the 18:10-02:29Z window: minutes inside a lumped recount row (a boundary block off the final chain merges several minutes into one row) also got a value from the live chain logger, so their transactions were in the lumped row **and** in their own row. Sum 18:10-02:29Z was 38,362,793; corrected **32,299,895** (6,062,898 counted twice). The same minutes were also flagged `complete_minute=yes`, and the 'recount avg' divided lumped rows by 60 instead of by their length. Fixed file: [logs/bot/chain-count.csv](bot/chain-count.csv) (rule: [METHOD](bot/chain-count.csv.METHOD.md)); old file kept as [chain-count.csv.superseded](bot/chain-count.csv.superseded). Step numbers below are recomputed. The 3,000 line is still not met; the earlier 'recount avg above 3,000' for C2500 and MAX was an artifact and is withdrawn. The workbook `run-2026-10-10.xlsx` predates this fix.

Back to [logs/](README.md) · narrative: [WRITE-UP.md](WRITE-UP.md) · bot detail: [docs/RESULTS.md](../docs/RESULTS.md) · history: [history/MASTER.md](../history/MASTER.md)

**Clocks.** Plan / bot clock ([go/clock.py](../go/clock.py)): **T0 2026-10-10T18:30:00Z**, **END 2026-10-11T02:30:00Z**, HOLD through 02:15Z. Build's SUMMARY used a **different clock** (T0 15:00Z, END 23:00Z) and joined ~17:28Z. Tables below use **UTC wall clock** for alignment. Do not add bot + Build submit as network unique.

**Success line.** Network unique accepted ≥ **3,000 tx/s**, median of a step's **complete** chain-count minutes (`complete_minute=yes`), ≥10 valid minutes, counted once. **Not met** on that metric (best: MAX **2,642.4**, n=9; no step reached 10 complete minutes except HOLD).

**Sources.** Bot: [logs/bot/steps.csv](bot/steps.csv), [chain-count.csv](bot/chain-count.csv), [recount-1m.csv](bot/recount-1m.csv), [SUMMARY.md](bot/SUMMARY.md). Build: [logs/build/steps.csv](build/steps.csv), [minute.csv](build/minute.csv), [SUMMARY.md](build/SUMMARY.md).

## Per-step table (bot clock windows)

Network unique = median of `accepted_tx_per_s` on bot [chain-count.csv](bot/chain-count.csv) where `complete_minute=yes`, window `[start, end)`. Recount avg = total `unique_accepted` of the [recount-1m.csv](bot/recount-1m.csv) rows whose whole span lies in the window, divided by the minutes they cover (supporting; corrected 11 Oct: lumped rows were divided by 60 before). Bot submit = `mean_submit_ok` from [bot/steps.csv](bot/steps.csv). Build submit = mean of `submit_ok/60` from [build/minute.csv](build/minute.csv) over the **same UTC window** (Build's own step name may differ because of its clock).

| Step | Window UTC | Combined target | Bot submit mean | Build submit mean (UTC-overlap) | Network unique median (complete) | Recount avg | 3000 line? | Notes |
|---|---|---:|---:|---:|---:|---:|---|---|
| X250 | 18:40–18:55 | 256 | 64.29 | 174.1 (n=15) | **293.4** (n=7) | 295.0 (15 min) | no | Bot clean. Build still on aborted first HOLD arm (label 2400, low submit). Build's own-clock C2500/MAX were earlier (17:31–18:15Z). |
| C1000 | 19:00–19:15 | 1,025 | 274.06 | 172.5 (n=15) | **512.0** (n=4) | 513.6 (7 min) | no (n&lt;10) | Bot unclean (lag). Disk/freeze approaching. Complete minutes thin. |
| C1500 | 19:20–19:35 | 1,538 | 0 | 163.5 (n=15) | **251.1** (n=1) | 1,004.2 (3 min) | no (n&lt;10) | Bot zeroed by 21:08–21:29 CEST box freeze (stale public WS). |
| C2000 | 19:40–19:55 | 2,050 | 544.16 | 1,193.0 (n=9) | **1,241.6** (n=6) | 1,395.5 (15 min) | no | Bot clean after sdk210 restore. Build re-armed HOLD at 1875 from ~19:49Z (partial window; earlier minutes still ~177 on 2400 arm). Build skipped own-clock C2000 (stale coin list). |
| C2500 | 20:00–20:15 | 2,563 | 673.68 | 1,754.1 (n=15) | **2,526.3** (n=7) | 2,512.7 (15 min) | no | Bot clean. Build on HOLD@1875. (Recount avg was shown as 3,426.4: counting artifact, corrected.) |
| MAX | 20:20–20:35 | 3,590 | 916.69 | 1,617.0 (n=15) | **2,642.4** (n=9) | 2,617.2 (15 min) | **no** | Best step median, but under 10 complete minutes. Bot clean (last clean level 990). (Recount avg was shown as 3,271.5: counting artifact, corrected.) |
| HOLD | 20:50–02:15 | 3,280 | 638.74 | 1,529.0 (n=129; Build ended 23:00Z) | **939.1** (n=123) | 1,142.0 (325 min) | no | Bot unclean (WS/RPC stalls, coin buffer). Build HOLD own-clock median network unique **4,032** over 175 min on desk count (see below) — not the plan clock. |

Peak complete-minute on bot chain-count (any time in file): **2,765.7** tx/s at 21:55Z. MAX-window peak complete: **2,734.7** at 20:26Z.

### Reconciliation with docs/RESULTS.md

Earlier [docs/RESULTS.md](../docs/RESULTS.md) used slightly different chain medians / n (closer to all minutes with a rate, e.g. X250 298.3 n=15, MAX 2,642.4 n=15). **This page prefers `complete_minute=yes`**, which matches the plan's "valid complete minutes" rule. Recount averages agree with RESULTS (within rounding). Both pages corrected on 11 Oct (see the correction note at the top).

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
| Best plan-metric step | MAX **2,642.4** (n=9 complete; under the 10-minute rule) |
| Supporting recount | C2500 avg **2,512.7**; MAX avg **2,617.2** (15 min each; corrected 11 Oct, were 3,426.4 / 3,271.5) |
| Build HOLD (desk count, Build clock) | median **4,032** over 175 complete minutes |
| Miners at END | **Off** at 02:30Z; after-END wrap senders=0 miner=0 (bot timeline) |
| Bot last clean level | 990 (MAX) |

