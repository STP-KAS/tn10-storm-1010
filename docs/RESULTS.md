> **Experimental. We are just trying this.** [Disclaimer](../DISCLAIMER.md)

# Tonight's results

Back to [README](../README.md).

**Filled after END (04:30 Sun CEST / 02:30 Sun UTC) and the chain recount (~04:33 CEST).** Bot-side wrap on the box. Build numbers were not present on the box at wrap time — leave blank.

Sources: [`logs/bot/`](../logs/bot/README.md), [`logs/bot/run-2026-10-10.xlsx`](../logs/bot/run-2026-10-10.xlsx), [`logs/bot/SUMMARY.md`](../logs/bot/SUMMARY.md), [`logs/bot/timeline.md`](../logs/bot/timeline.md), [`logs/bot/night-notes.md`](../logs/bot/night-notes.md), [`logs/bot/recount-1m.csv`](../logs/bot/recount-1m.csv). How to read them: [go/LOGGING.md](../go/LOGGING.md#how-to-read-the-run-in-5-minutes).

## Headline

| Step | Combined target | Network unique (chain-1m valid median, tx/s) | Network unique (recount avg, tx/s) | Bot submitted / accepted | Build | Clean | Label |
|---|---:|---:|---:|---|---|---|---|
| X250 | 256 | 298.3 (n=15) | 402.3 (n=11) | 66.0 / 66.0 | — | yes | Claim (measured on TN10) |
| C1000 | 1,025 | 512.0 (n=8) | 1,194.9 (n=6) | 139.3 / 139.2 | — | no | Claim (measured on TN10); disk/freeze |
| C1500 | 1,538 | 245.9 (n=2) | 1,506.2 (n=2) | 0 / 0.3 | — | no | Claim (measured on TN10); zeroed by 21:08 freeze |
| C2000 | 2,050 | 796.5 (n=15) | 2,093.2 (n=10) | 545.5 / 545.6 | — | yes | Claim (measured on TN10) |
| C2500 | 2,563 | 2,526.3 (n=15) | 3,426.4 (n=11) | 674.7 / 674.3 | — | yes | Claim (measured on TN10) |
| MAX | 3,590 | **2,642.4** (n=15) | **3,271.5** (n=12) | **919.1 / 919.3** | — | yes | Claim (measured on TN10) |
| HOLD | 3,280 | 938.7 (n=212) | 2,145.3 (n=173) | 469.2 / 468.6 | — | no | Claim (measured on TN10); many WS/RPC stalls |

- **Success line (3,000 tx/s network unique accepted):** plan metric = median of a step's valid minutes, ≥10 valid minutes. **Not met** on that metric (best: MAX ~2,642). Post-run recount averages for C2500 (~3,426) and MAX (~3,272) exceed 3,000 but with fewer boundary-sink minutes (merged/missing minutes during freezes) — treat as supporting, not the plan pass/fail.
- **Combined vs goal:** network unique is the whole network (bot + Build + others). Build column unknown on this wrap; do not add bot+Build submit rates as a substitute.
- **Bot last clean level:** 990 (MAX). HOLD unclean; average includes long dead periods overnight.

## What went wrong (short)

From [`logs/bot/night-notes.md`](../logs/bot/night-notes.md) / timeline:

1. **21:08–21:29 CEST disk/freeze** zeroed C1500 (and hurt C1000). Box shell dead; disk freefall toward ~9G; senders' public WS went stale (`node_cool` / RPC timeout).
2. **sdk210 accidental delete** during night-watch reclaim — restored from identical 2.1.0 copy; relaunches then worked for C2000.
3. **n2 utxoindex removed ~21:58 CEST** (datadir bursts; ~14G reclaimed). n2 restarted without `--utxoindex`. Coin refresh/top-up no longer possible; buffer had to carry the night.
4. **HOLD WS/RPC stalls** overnight — fixes **#7–#17** (mass sender TERM/KILL + tip rebuilds via public-node `getUtxosByAddresses`). HTTP wrpc/borsh 502 was a false negative; WS submit often still worked.
5. **Coin buffer → 0** late night; **lane-reuse** enabled in `pub-sender.mjs` (correct `pub-chains-P2WP1010*` prefix). Tip rebuilds after spent tips / SIGTERM tip-save pollution (KILL -9 only thereafter).

## Workbook

[`logs/bot/run-2026-10-10.xlsx`](../logs/bot/run-2026-10-10.xlsx) — Summary sheet (EVAL + network), one sheet per main CSV, charts for submitted vs accepted and network unique over time.
