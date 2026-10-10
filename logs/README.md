> **Experimental. We are just trying this.** [Disclaimer](../DISCLAIMER.md)

# logs: where the results land

Empty until the run (T0 20:30 CEST, 10 Oct 2026). Each side drops its files here after the chain count, by the PUSH time in [go/README.md](../go/README.md#key-times).

| Folder | Side | Submits to | Who writes it |
|---|---|---|---|
| [bot/](bot/README.md) | Bot run | The five public TN10 nodes (n2 for reads) | TN10 ops and tn ops2 |
| [build/](build/README.md) | Build run | Public nodes or Build's own node, as Build chose | Grok Build |

File names and columns are in [go/LOGGING.md](../go/LOGGING.md). Both folders use the same names, so files can be joined on `minute_utc` and lined up with Kaspa Pulse's count.

The headline, network unique accepted tx/s, is counted once from chain data, never summed across sides. A combined page, `COMBINED.md`, is written here after both folders are filled.

Counts only. No txid, key, seed, host IP, port or wallet address.
