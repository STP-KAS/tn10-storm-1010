> **Experimental. We are just trying this.** [Disclaimer](../DISCLAIMER.md)

# Tonight's results

Back to [README](../README.md).

**Filled after END (04:30 Sun CEST / 02:30 Sun UTC) and the chain recount (~04:33 CEST).** Combined page: [`logs/COMBINED.md`](../logs/COMBINED.md), narrative [`logs/WRITE-UP.md`](../logs/WRITE-UP.md). Build logs are in [`logs/build/`](../logs/build/README.md). Network unique below prefers bot `chain-count.csv` with `complete_minute=yes` (plan rule); recount averages stay as supporting.

Sources: [`logs/bot/`](../logs/bot/README.md), [`logs/bot/run-2026-10-10.xlsx`](../logs/bot/run-2026-10-10.xlsx), [`logs/bot/SUMMARY.md`](../logs/bot/SUMMARY.md), [`logs/bot/timeline.md`](../logs/bot/timeline.md), [`logs/bot/night-notes.md`](../logs/bot/night-notes.md), [`logs/bot/recount-1m.csv`](../logs/bot/recount-1m.csv), [`logs/build/SUMMARY.md`](../logs/build/SUMMARY.md). How to read them: [go/LOGGING.md](../go/LOGGING.md#how-to-read-the-run-in-5-minutes).

## Headline

| Step | Combined target | Network unique (complete_minute=yes median, tx/s) | Network unique (recount avg, tx/s) | Bot submit / n2-accepted mean (steps.csv) | Build submit mean (UTC-overlap, minute.csv/60) | Clean (bot) | Label |
|---|---:|---:|---:|---|---|---|---|
| X250 | 256 | **293.6** (n=11) | 402.3 (n=11) | 64.29 / 64.22 | 174.1 (aborted 2400 HOLD arm) | yes | Claim (measured on TN10) |
| C1000 | 1,025 | **512.0** (n=6) | 1,194.9 (n=6) | 274.06 / 273.58 | 172.5 | no | Claim (measured on TN10); disk/freeze |
| C1500 | 1,538 | **245.9** (n=2) | 1,506.2 (n=2) | 0 / 0.69 | 163.5 | no | Claim (measured on TN10); zeroed by 21:08 freeze |
| C2000 | 2,050 | **796.5** (n=11) | 2,093.2 (n=10) | 544.16 / 543.69 | 1,193 (re-arm 1875 mid-window; Build skipped own C2000) | yes | Claim (measured on TN10) |
| C2500 | 2,563 | **2,526.3** (n=11) | 3,426.4 (n=11) | 673.68 / 672.51 | 1,754.1 (Build HOLD@1875) | yes | Claim (measured on TN10) |
| MAX | 3,590 | **2,644.9** (n=12) | **3,271.5** (n=12) | **916.69 / 915.38** | 1,617.0 (Build HOLD@1875) | yes | Claim (measured on TN10) |
| HOLD | 3,280 | **936.5** (n=177) | 2,145.3 (n=173) | 638.74 / 637.93 | 1,529 (Build ended 23:00Z; own-clock HOLD med unique **4,032**/175) | no | Claim (measured on TN10); many WS/RPC stalls |

- **Success line (3,000 tx/s network unique accepted):** plan metric = median of a step's **complete** minutes (`complete_minute=yes`), ≥10 valid minutes. **Not met** (best: MAX **2,644.9**, n=12). Post-run recount averages for C2500 (~3,426) and MAX (~3,272) exceed 3,000 but with thinner freeze-gap coverage — supporting only, not the plan pass/fail.
- **Combined vs goal:** network unique is the whole network (bot + Build + others), counted once. Build submit figures are in the table and in [`logs/COMBINED.md`](../logs/COMBINED.md); do not add bot+Build submit as a substitute for network unique. Build's own clock was T0 15:00Z (joined ~17:28Z).
- **Bot last clean level:** 990 (MAX). HOLD unclean; mean includes long dead periods overnight. Miners off at END 02:30Z (timeline).

## What went wrong (short)

From [`logs/bot/night-notes.md`](../logs/bot/night-notes.md) / timeline:

1. **21:08–21:29 CEST disk/freeze** zeroed C1500 (and hurt C1000). Box shell dead; disk freefall toward ~9G; senders' public WS went stale (`node_cool` / RPC timeout).
2. **sdk210 accidental delete** during night-watch reclaim — restored from identical 2.1.0 copy; relaunches then worked for C2000.
3. **n2 utxoindex removed ~21:58 CEST** (datadir bursts; ~14G reclaimed). n2 restarted without `--utxoindex`. Coin refresh/top-up no longer possible; buffer had to carry the night.
4. **HOLD WS/RPC stalls** overnight — fixes **#7–#17** (mass sender TERM/KILL + tip rebuilds via public-node `getUtxosByAddresses`). HTTP wrpc/borsh 502 was a false negative; WS submit often still worked.
5. **Coin buffer → 0** late night; **lane-reuse** enabled in `pub-sender.mjs` (correct `pub-chains-P2WP1010*` prefix). Tip rebuilds after spent tips / SIGTERM tip-save pollution (KILL -9 only thereafter).

## Workbook

[`logs/bot/run-2026-10-10.xlsx`](../logs/bot/run-2026-10-10.xlsx) — Summary sheet (EVAL + network), one sheet per main CSV, charts for submitted vs accepted and network unique over time.
