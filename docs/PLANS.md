> **Experimental. We are just trying this.** [Disclaimer](../DISCLAIMER.md)

# Plans, old and new

Back to [README](../README.md).

| Plan | Nodes | Result |
|---|---|---|
| Up to 8 Oct | Box node n0 (+ public nodes for Build) | n0 filled its disk while pruning and was retired. |
| 9 Oct night, 10 Oct take 2 ([tn10-storm-2026-10-09](https://github.com/STP-KAS/tn10-storm-2026-10-09)) | Two nodes on one desk: locus (Build) and keel (bot, via a tunnel) | keel lagged; locus aborted at 03:28, 08:52 and 09:26 CEST. Failed as a test of the plan. |
| 10 Oct 17:00 CEST ([tn10-storm-2026-10-10-plan](https://github.com/STP-KAS/tn10-storm-2026-10-10-plan) shape, refined here) | n2 for the bot (public-node submit from 14:36 CEST), a desk node for Build | Halted by stp at 17:39 CEST: Build had not been started. The bot's S1 row (60 tx/s) was evaluated clean; S3 ran at 60 tx/s and was not evaluated before the halt. [history/2026-10-10-1700-halted.md](../history/2026-10-10-1700-halted.md). |
| 10 Oct public-node test, 14:23 to 16:18 CEST ([tn10-storm-2026-10-10-public-nodes](https://github.com/STP-KAS/tn10-storm-2026-10-10-public-nodes), private) | Bot senders on the five public nodes, n2 for reads | Peak about 3,168 bot tx/s; clean hold about 880 to 985 bot tx/s on 14 senders. Lessons are folded into this plan. |
| **Tonight, T0 20:30 CEST** (this repo) | Bot: five public nodes, n2 for reads. Build: its own desk node, public nodes as fallback | This run. |
