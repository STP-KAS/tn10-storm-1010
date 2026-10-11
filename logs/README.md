> **Experimental. We are just trying this.** [Disclaimer](../DISCLAIMER.md)

# logs: where the results land

Both sides filled after the 10 Oct run (T0 20:30 CEST). Combined write-up added post-run. PUSH times: [go/README.md](../go/README.md#key-times).

| Folder | Side | Submits to | Who writes it |
|---|---|---|---|
| [bot/](bot/README.md) | Bot run | The five public TN10 nodes (n2 for reads) | TN10 ops and tn ops2 |
| [build/](build/README.md) | Build run | Build's own desk node (public nodes as fallback) | Grok Build |

File names and columns are in [go/LOGGING.md](../go/LOGGING.md). Both folders use the same names, so files can be joined on `minute_utc` and lined up with Kaspa Pulse's count.

The headline, network unique accepted tx/s, is counted once from chain data, never summed across sides. Combined: [`COMBINED.md`](COMBINED.md). Narrative: [`WRITE-UP.md`](WRITE-UP.md).

Live during the run: [bot/SUMMARY.md](bot/SUMMARY.md), every 15 minutes. How to read the run in 5 minutes: [go/LOGGING.md](../go/LOGGING.md#how-to-read-the-run-in-5-minutes).

After the run, once the logs are on GitHub, TN10 ops makes this repo public.

## Method per file

Each per-minute CSV has a method sidecar next to it (`<file>.METHOD.md`), so the CSVs stay plain for parsers: what is counted, which node, how minutes are bucketed, timezone UTC.

| CSV | Counted on | Bucketing | Method |
|---|---|---|---|
| [bot/chain-count.csv](bot/chain-count.csv) (headline) | n2 | n2 receive time (UTC-minute boundary tips) | [METHOD](bot/chain-count.csv.METHOD.md) |
| [bot/recount-1m.csv](bot/recount-1m.csv) | n2 | n2 receive time | [METHOD](bot/recount-1m.csv.METHOD.md) |
| [bot/minute.csv](bot/minute.csv) | bot senders; n2 for network columns | n2 receive time | [METHOD](bot/minute.csv.METHOD.md) |
| [build/chain-count.csv](build/chain-count.csv) | Build's desk node | not stated by Build (open) | [METHOD](build/chain-count.csv.METHOD.md) |
| [build/minute.csv](build/minute.csv) | Build senders; desk node for network columns | not stated by Build (open) | [METHOD](build/minute.csv.METHOD.md) |

Counts only. No txid, key, seed, host IP, port or wallet address.
