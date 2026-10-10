> **Experimental. We are just trying this.** [Disclaimer](../DISCLAIMER.md)

# logs: where the results land

Empty until the run. Each side drops its files here after the chain count, by the PUSH time in [go/README.md](../go/README.md#key-times).

| Folder | Side | Node | Who writes it |
|---|---|---|---|
| [bot/](bot/README.md) | Bot | n2, on the box | TN10 ops and tn ops2 |
| [build/](build/README.md) | Build | Build's desk node | Grok Build |

File names and columns are in [go/LOGGING.md](../go/LOGGING.md). Both folders use the same names, so files can be joined on `minute_utc`, and lined up with Kaspa Pulse's count.

The headline, network unique accepted tx/s, is counted once from chain data. Each side's `chain-count.csv` is a count of the same network; the two are a check on each other, never a sum.

A combined page, `COMBINED.md`, is written here after both folders are filled.

Counts only. No txid, key, seed, host, IP, port or address.
