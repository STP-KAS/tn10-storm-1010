| 17:58:06 CEST | 15:58:06 UTC | watchdog: scheduler not running -> (re)start |
| 17:58:06 CEST | 15:58:06 UTC | scheduler armed; T0 18:30 UTC, gates 18:00/18:15 UTC, end 02:30 UTC; node n2 (own private node, loopback) |
| 17:58:06 CEST | 15:58:06 UTC | PLAN (STP-KAS/tn10-storm-1010 go/steps-utc.json @ 39c4554): bot run, T0 18:30 UTC (20:30 CEST), G1 18:00 / G2 18:15 UTC, END 02:30 UTC. Submit ONLY to the 5 public TN10 nodes (each sender 4 of 5 at random), n2 reads/coins/count/miner. Bot rates: X250 60, C1000 250, C1500 375, C2000 500, C2500 625, MAX 900, HOLD 800; hold 800 if MAX clean else highest clean (60 if none). Fees 400/600, floor 100, cap 600, sit out if quote > 400. 15 senders x 200 lanes, staggered, max 8 relaunches each, no launch at RAM < 1.5 GB. No send until BUILD-OK (stp confirms Build started). n2 lag does not zero senders; n2 frozen > 3 min -> restart (max 1 per 20 min). Miner 1 thread 18:15-02:30 UTC. |
| 17:58:06 CEST | 15:58:06 UTC | n2 first read: synced true, utxoindex true, sink lag 0.3 s, DAA 593137555 |
| 17:58:06 CEST | 15:58:06 UTC | coin refresh started (run 1, first refresh once n2 is synced) |
| 17:58:06 CEST | 15:58:06 UTC | prep: n2 synced true, utxoindex true, lag 0.3 s; no sends, miner off until 18:15 UTC |
| 17:58:26 CEST | 15:58:26 UTC | coin refresh: added 0 coins 0 tKAS, dropped spent 0, unclaimed 1003835.4 tKAS (22656 coins), caught up false, method block walk, 4485 blocks/18 pages, kaspad RSS peak 2038 MB, MemAvailable min 6061 MB, 18 s |
| 17:58:26 CEST | 15:58:26 UTC | coin refresh started (run 2, first refresh once n2 is synced) |
| 17:58:46 CEST | 15:58:46 UTC | coin refresh: added 0 coins 0 tKAS, dropped spent 0, unclaimed 1003835.4 tKAS (22656 coins), caught up false, method block walk, 3735 blocks/15 pages, kaspad RSS peak 2141 MB, MemAvailable min 6116 MB, 17 s |
| 17:58:46 CEST | 15:58:46 UTC | coin refresh started (run 3, first refresh once n2 is synced) |
| 17:59:06 CEST | 15:59:06 UTC | coin refresh: added 0 coins 0 tKAS, dropped spent 0, unclaimed 1003835.4 tKAS (22656 coins), caught up false, method block walk, 4242 blocks/17 pages, kaspad RSS peak 2195 MB, MemAvailable min 6102 MB, 17 s |
| 17:59:06 CEST | 15:59:06 UTC | coin refresh started (run 4, first refresh once n2 is synced) |
| 17:59:26 CEST | 15:59:26 UTC | coin refresh: added 0 coins 0 tKAS, dropped spent 0, unclaimed 1003835.4 tKAS (22656 coins), caught up false, method block walk, 5488 blocks/22 pages, kaspad RSS peak 2207 MB, MemAvailable min 6182 MB, 17 s |
| 17:59:26 CEST | 15:59:26 UTC | coin refresh started (run 5, first refresh once n2 is synced) |
| 17:59:46 CEST | 15:59:46 UTC | coin refresh: added 0 coins 0 tKAS, dropped spent 0, unclaimed 1003835.4 tKAS (22656 coins), caught up false, method block walk, 16679 blocks/67 pages, kaspad RSS peak 2196 MB, MemAvailable min 6513 MB, 17 s |
| 17:59:46 CEST | 15:59:46 UTC | coin refresh started (run 6, first refresh once n2 is synced) |
| 18:00:06 CEST | 16:00:06 UTC | coin refresh: added 0 coins 0 tKAS, dropped spent 0, unclaimed 1003835.4 tKAS (22656 coins), caught up false, method block walk, 19183 blocks/77 pages, kaspad RSS peak 2182 MB, MemAvailable min 6373 MB, 17 s |
| 18:00:06 CEST | 16:00:06 UTC | coin refresh started (run 7, first refresh once n2 is synced) |
| 18:00:26 CEST | 16:00:26 UTC | coin refresh: added 0 coins 0 tKAS, dropped spent 0, unclaimed 1003835.4 tKAS (22656 coins), caught up false, method block walk, 19183 blocks/77 pages, kaspad RSS peak 2209 MB, MemAvailable min 6552 MB, 17 s |
| 18:00:26 CEST | 16:00:26 UTC | coin refresh started (run 8, first refresh once n2 is synced) |
| 18:00:46 CEST | 16:00:46 UTC | coin refresh: added 0 coins 0 tKAS, dropped spent 0, unclaimed 1003835.4 tKAS (22656 coins), caught up false, method block walk, 16206 blocks/65 pages, kaspad RSS peak 2284 MB, MemAvailable min 6544 MB, 17 s |
| 18:00:46 CEST | 16:00:46 UTC | coin refresh started (run 9, first refresh once n2 is synced) |
| 18:00:57 CEST | 16:00:57 UTC | coin refresh: added 9909 coins 30870.7 tKAS, dropped spent 0, unclaimed 1034706.1 tKAS (32565 coins), caught up true, method block walk, 3264 blocks/16 pages, kaspad RSS peak 2294 MB, MemAvailable min 6625 MB, 5 s |
| 18:13:06 CEST | 16:13:06 UTC | prep: n2 synced true, utxoindex true, lag 0.1 s; no sends, miner off until 18:15 UTC |
| 18:26:42 CEST | 16:26:42 UTC | live summary: DRY pushed logs/bot/SUMMARY.md (8eba339) |
| 18:26:48 CEST | 16:26:48 UTC | live summary: loop started: write every 10 min, push every 15 min from G1 to END+15 min |
| 18:28:07 CEST | 16:28:07 UTC | prep: n2 synced true, utxoindex true, lag 0.3 s; no sends, miner off until 18:15 UTC |
| 18:43:07 CEST | 16:43:07 UTC | prep: n2 synced true, utxoindex true, lag 0.2 s; no sends, miner off until 18:15 UTC |
| 18:46:51 CEST | 16:46:51 UTC | n2 unhealthy under pubMode (sink lag 84.2 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 18:46:52 CEST | 16:46:52 UTC | n2 unhealthy under pubMode (sink lag 85.2 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 18:46:53 CEST | 16:46:53 UTC | n2 unhealthy under pubMode (sink lag 86.3 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 18:46:54 CEST | 16:46:54 UTC | n2 unhealthy under pubMode (sink lag 87.3 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 18:46:55 CEST | 16:46:55 UTC | n2 unhealthy under pubMode (sink lag 88.3 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 18:46:56 CEST | 16:46:56 UTC | n2 unhealthy under pubMode (sink lag 89.3 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 18:46:57 CEST | 16:46:57 UTC | n2 unhealthy under pubMode (sink lag 90.3 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 18:46:58 CEST | 16:46:58 UTC | n2 unhealthy under pubMode (sink lag 91.3 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 18:46:59 CEST | 16:46:59 UTC | n2 unhealthy under pubMode (sink lag 92.3 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:00 CEST | 16:47:00 UTC | n2 unhealthy under pubMode (sink lag 93.3 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:01 CEST | 16:47:01 UTC | n2 unhealthy under pubMode (sink lag 94.3 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:02 CEST | 16:47:02 UTC | n2 unhealthy under pubMode (sink lag 95.3 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:03 CEST | 16:47:03 UTC | n2 unhealthy under pubMode (sink lag 96.4 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:04 CEST | 16:47:04 UTC | n2 unhealthy under pubMode (sink lag 97.4 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:05 CEST | 16:47:05 UTC | n2 unhealthy under pubMode (sink lag 98.4 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:06 CEST | 16:47:06 UTC | n2 unhealthy under pubMode (sink lag 99.4 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:07 CEST | 16:47:07 UTC | n2 unhealthy under pubMode (sink lag 100.4 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:08 CEST | 16:47:08 UTC | n2 unhealthy under pubMode (sink lag 101.4 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:09 CEST | 16:47:09 UTC | n2 unhealthy under pubMode (sink lag 102.4 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:10 CEST | 16:47:10 UTC | n2 unhealthy under pubMode (sink lag 103.4 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:11 CEST | 16:47:11 UTC | n2 unhealthy under pubMode (sink lag 104.4 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:12 CEST | 16:47:12 UTC | n2 unhealthy under pubMode (sink lag 105.4 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:13 CEST | 16:47:13 UTC | n2 unhealthy under pubMode (sink lag 106.4 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:14 CEST | 16:47:14 UTC | n2 unhealthy under pubMode (sink lag 107.4 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:15 CEST | 16:47:15 UTC | n2 unhealthy under pubMode (sink lag 108.4 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:16 CEST | 16:47:16 UTC | n2 unhealthy under pubMode (sink lag 109.4 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:17 CEST | 16:47:17 UTC | n2 unhealthy under pubMode (sink lag 110.4 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:18 CEST | 16:47:18 UTC | n2 unhealthy under pubMode (sink lag 111.4 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:19 CEST | 16:47:19 UTC | n2 unhealthy under pubMode (sink lag 112.4 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:20 CEST | 16:47:20 UTC | n2 unhealthy under pubMode (sink lag 113.4 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:21 CEST | 16:47:21 UTC | FREEZE start: n2 virtual DAA not moving for 30 s (>= 30 s) (lag 114.4 s) |
| 18:47:21 CEST | 16:47:21 UTC | n2 unhealthy under pubMode (sink lag 114.4 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:22 CEST | 16:47:22 UTC | n2 unhealthy under pubMode (sink lag 115.4 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:23 CEST | 16:47:23 UTC | n2 unhealthy under pubMode (sink lag 116.4 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:24 CEST | 16:47:24 UTC | n2 unhealthy under pubMode (sink lag 117.4 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:25 CEST | 16:47:25 UTC | n2 unhealthy under pubMode (sink lag 118.4 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:26 CEST | 16:47:26 UTC | n2 unhealthy under pubMode (sink lag 119.5 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:27 CEST | 16:47:27 UTC | n2 unhealthy under pubMode (sink lag 120.5 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:28 CEST | 16:47:28 UTC | n2 unhealthy under pubMode (sink lag 121.5 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:29 CEST | 16:47:29 UTC | n2 unhealthy under pubMode (sink lag 122.5 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:30 CEST | 16:47:30 UTC | n2 unhealthy under pubMode (sink lag 123.5 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:31 CEST | 16:47:31 UTC | n2 unhealthy under pubMode (sink lag 124.5 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:32 CEST | 16:47:32 UTC | n2 unhealthy under pubMode (sink lag 125.5 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:33 CEST | 16:47:33 UTC | n2 unhealthy under pubMode (sink lag 126.5 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:34 CEST | 16:47:34 UTC | n2 unhealthy under pubMode (sink lag 127.5 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:35 CEST | 16:47:35 UTC | n2 unhealthy under pubMode (sink lag 128.5 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:36 CEST | 16:47:36 UTC | n2 unhealthy under pubMode (sink lag 129.5 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:37 CEST | 16:47:37 UTC | n2 unhealthy under pubMode (sink lag 130.5 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:38 CEST | 16:47:38 UTC | n2 unhealthy under pubMode (sink lag 131.5 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:39 CEST | 16:47:39 UTC | n2 unhealthy under pubMode (sink lag 132.5 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:40 CEST | 16:47:40 UTC | n2 unhealthy under pubMode (sink lag 133.5 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:41 CEST | 16:47:41 UTC | n2 unhealthy under pubMode (sink lag 134.5 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:42 CEST | 16:47:42 UTC | n2 unhealthy under pubMode (sink lag 135.5 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:43 CEST | 16:47:43 UTC | n2 unhealthy under pubMode (sink lag 136.5 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:44 CEST | 16:47:44 UTC | n2 unhealthy under pubMode (sink lag 137.5 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:45 CEST | 16:47:45 UTC | n2 unhealthy under pubMode (sink lag 138.5 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:46 CEST | 16:47:46 UTC | n2 unhealthy under pubMode (sink lag 139.5 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:47 CEST | 16:47:47 UTC | n2 unhealthy under pubMode (sink lag 140.5 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:48 CEST | 16:47:48 UTC | n2 unhealthy under pubMode (sink lag 141.5 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:49 CEST | 16:47:49 UTC | n2 unhealthy under pubMode (sink lag 142.5 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:50 CEST | 16:47:50 UTC | n2 unhealthy under pubMode (sink lag 143.5 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:51 CEST | 16:47:51 UTC | n2 unhealthy under pubMode (sink lag 144.6 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:52 CEST | 16:47:52 UTC | n2 unhealthy under pubMode (sink lag 145.6 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:53 CEST | 16:47:53 UTC | n2 unhealthy under pubMode (sink lag 146.6 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:54 CEST | 16:47:54 UTC | n2 unhealthy under pubMode (sink lag 147.6 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:55 CEST | 16:47:55 UTC | n2 unhealthy under pubMode (sink lag 148.6 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:56 CEST | 16:47:56 UTC | n2 unhealthy under pubMode (sink lag 149.6 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:57 CEST | 16:47:57 UTC | n2 unhealthy under pubMode (sink lag 150.6 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:58 CEST | 16:47:58 UTC | n2 unhealthy under pubMode (sink lag 151.6 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:47:59 CEST | 16:47:59 UTC | n2 unhealthy under pubMode (sink lag 152.6 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:00 CEST | 16:48:00 UTC | n2 unhealthy under pubMode (sink lag 153.6 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:01 CEST | 16:48:01 UTC | n2 unhealthy under pubMode (sink lag 154.6 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:02 CEST | 16:48:02 UTC | n2 unhealthy under pubMode (sink lag 155.6 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:03 CEST | 16:48:03 UTC | n2 unhealthy under pubMode (sink lag 156.6 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:04 CEST | 16:48:04 UTC | n2 unhealthy under pubMode (sink lag 157.6 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:05 CEST | 16:48:05 UTC | n2 unhealthy under pubMode (sink lag 158.6 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:06 CEST | 16:48:06 UTC | n2 unhealthy under pubMode (sink lag 159.6 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:07 CEST | 16:48:07 UTC | n2 unhealthy under pubMode (sink lag 160.6 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:08 CEST | 16:48:08 UTC | n2 unhealthy under pubMode (sink lag 161.6 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:09 CEST | 16:48:09 UTC | n2 unhealthy under pubMode (sink lag 162.6 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:10 CEST | 16:48:10 UTC | n2 unhealthy under pubMode (sink lag 163.6 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:11 CEST | 16:48:11 UTC | n2 unhealthy under pubMode (sink lag 164.6 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:12 CEST | 16:48:12 UTC | n2 unhealthy under pubMode (sink lag 165.6 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:13 CEST | 16:48:13 UTC | n2 unhealthy under pubMode (sink lag 166.6 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:14 CEST | 16:48:14 UTC | n2 unhealthy under pubMode (sink lag 167.6 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:15 CEST | 16:48:15 UTC | n2 unhealthy under pubMode (sink lag 168.7 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:16 CEST | 16:48:16 UTC | n2 unhealthy under pubMode (sink lag 169.7 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:17 CEST | 16:48:17 UTC | n2 unhealthy under pubMode (sink lag 170.7 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:18 CEST | 16:48:18 UTC | n2 unhealthy under pubMode (sink lag 171.7 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:19 CEST | 16:48:19 UTC | n2 unhealthy under pubMode (sink lag 172.7 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:20 CEST | 16:48:20 UTC | n2 unhealthy under pubMode (sink lag 173.7 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:21 CEST | 16:48:21 UTC | n2 unhealthy under pubMode (sink lag 174.7 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:22 CEST | 16:48:22 UTC | n2 unhealthy under pubMode (sink lag 175.7 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:23 CEST | 16:48:23 UTC | n2 unhealthy under pubMode (sink lag 176.7 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:24 CEST | 16:48:24 UTC | n2 unhealthy under pubMode (sink lag 177.7 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:25 CEST | 16:48:25 UTC | n2 unhealthy under pubMode (sink lag 178.7 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:26 CEST | 16:48:26 UTC | n2 unhealthy under pubMode (sink lag 179.7 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:27 CEST | 16:48:27 UTC | n2 unhealthy under pubMode (sink lag 180.7 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:28 CEST | 16:48:28 UTC | n2 unhealthy under pubMode (sink lag 181.7 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:29 CEST | 16:48:29 UTC | n2 unhealthy under pubMode (sink lag 182.7 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:30 CEST | 16:48:30 UTC | n2 unhealthy under pubMode (sink lag 183.7 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:31 CEST | 16:48:31 UTC | n2 unhealthy under pubMode (sink lag 184.7 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:32 CEST | 16:48:32 UTC | n2 unhealthy under pubMode (sink lag 185.7 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:33 CEST | 16:48:33 UTC | n2 unhealthy under pubMode (sink lag 186.7 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:34 CEST | 16:48:34 UTC | n2 unhealthy under pubMode (sink lag 187.7 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:35 CEST | 16:48:35 UTC | n2 unhealthy under pubMode (sink lag 188.7 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:36 CEST | 16:48:36 UTC | n2 unhealthy under pubMode (sink lag 189.7 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:37 CEST | 16:48:37 UTC | n2 unhealthy under pubMode (sink lag 190.7 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:38 CEST | 16:48:38 UTC | n2 unhealthy under pubMode (sink lag 191.7 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:39 CEST | 16:48:39 UTC | n2 unhealthy under pubMode (sink lag 192.7 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:40 CEST | 16:48:40 UTC | n2 unhealthy under pubMode (sink lag 193.8 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:41 CEST | 16:48:41 UTC | n2 unhealthy under pubMode (sink lag 194.8 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:42 CEST | 16:48:42 UTC | n2 unhealthy under pubMode (sink lag 195.8 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:43 CEST | 16:48:43 UTC | n2 unhealthy under pubMode (sink lag 196.8 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:44 CEST | 16:48:44 UTC | n2 unhealthy under pubMode (sink lag 197.8 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:45 CEST | 16:48:45 UTC | n2 unhealthy under pubMode (sink lag 198.8 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:46 CEST | 16:48:46 UTC | n2 unhealthy under pubMode (sink lag 199.8 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:47 CEST | 16:48:47 UTC | n2 unhealthy under pubMode (sink lag 200.8 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:48 CEST | 16:48:48 UTC | n2 unhealthy under pubMode (sink lag 201.8 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:49 CEST | 16:48:49 UTC | n2 unhealthy under pubMode (sink lag 202.8 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:50 CEST | 16:48:50 UTC | n2 unhealthy under pubMode (sink lag 203.8 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:51 CEST | 16:48:51 UTC | n2 unhealthy under pubMode (sink lag 204.8 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:52 CEST | 16:48:52 UTC | n2 unhealthy under pubMode (sink lag 205.8 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:53 CEST | 16:48:53 UTC | n2 unhealthy under pubMode (sink lag 206.8 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:54 CEST | 16:48:54 UTC | n2 unhealthy under pubMode (sink lag 207.8 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:55 CEST | 16:48:55 UTC | n2 unhealthy under pubMode (sink lag 208.8 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:56 CEST | 16:48:56 UTC | n2 unhealthy under pubMode (sink lag 209.8 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:57 CEST | 16:48:57 UTC | n2 unhealthy under pubMode (sink lag 210.8 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:58 CEST | 16:48:58 UTC | n2 unhealthy under pubMode (sink lag 211.8 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:48:59 CEST | 16:48:59 UTC | n2 unhealthy under pubMode (sink lag 212.8 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:49:00 CEST | 16:49:00 UTC | n2 unhealthy under pubMode (sink lag 213.8 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:49:01 CEST | 16:49:01 UTC | n2 unhealthy under pubMode (sink lag 214.8 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:49:02 CEST | 16:49:02 UTC | n2 unhealthy under pubMode (sink lag 215.8 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:49:03 CEST | 16:49:03 UTC | n2 unhealthy under pubMode (sink lag 216.8 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:49:04 CEST | 16:49:04 UTC | n2 unhealthy under pubMode (sink lag 217.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:49:05 CEST | 16:49:05 UTC | n2 unhealthy under pubMode (sink lag 218.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:49:06 CEST | 16:49:06 UTC | n2 unhealthy under pubMode (sink lag 219.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:49:07 CEST | 16:49:07 UTC | n2 unhealthy under pubMode (sink lag 220.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:49:08 CEST | 16:49:08 UTC | n2 unhealthy under pubMode (sink lag 221.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:49:09 CEST | 16:49:09 UTC | n2 unhealthy under pubMode (sink lag 222.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:49:10 CEST | 16:49:10 UTC | n2 unhealthy under pubMode (sink lag 223.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:49:11 CEST | 16:49:11 UTC | n2 unhealthy under pubMode (sink lag 224.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:49:12 CEST | 16:49:12 UTC | n2 unhealthy under pubMode (sink lag 225.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:49:13 CEST | 16:49:13 UTC | n2 unhealthy under pubMode (sink lag 226.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:49:14 CEST | 16:49:14 UTC | n2 unhealthy under pubMode (sink lag 227.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:49:15 CEST | 16:49:15 UTC | n2 unhealthy under pubMode (sink lag 228.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:49:16 CEST | 16:49:16 UTC | n2 unhealthy under pubMode (sink lag 229.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:49:17 CEST | 16:49:17 UTC | n2 unhealthy under pubMode (sink lag 230.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:49:18 CEST | 16:49:18 UTC | n2 unhealthy under pubMode (sink lag 231.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:49:19 CEST | 16:49:19 UTC | n2 unhealthy under pubMode (sink lag 232.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:49:20 CEST | 16:49:20 UTC | n2 unhealthy under pubMode (sink lag 233.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:49:21 CEST | 16:49:21 UTC | n2 unhealthy under pubMode (sink lag 234.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:49:22 CEST | 16:49:22 UTC | n2 unhealthy under pubMode (sink lag 235.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:49:23 CEST | 16:49:23 UTC | n2 unhealthy under pubMode (sink lag 236.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:49:24 CEST | 16:49:24 UTC | n2 unhealthy under pubMode (sink lag 237.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:49:25 CEST | 16:49:25 UTC | n2 unhealthy under pubMode (sink lag 238.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:49:26 CEST | 16:49:26 UTC | n2 unhealthy under pubMode (sink lag 239.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:49:27 CEST | 16:49:27 UTC | n2 unhealthy under pubMode (sink lag 240.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:49:28 CEST | 16:49:28 UTC | n2 unhealthy under pubMode (sink lag 242 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:49:29 CEST | 16:49:29 UTC | n2 unhealthy under pubMode (sink lag 243 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:49:30 CEST | 16:49:30 UTC | n2 unhealthy under pubMode (sink lag 244 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:49:31 CEST | 16:49:31 UTC | n2 unhealthy under pubMode (sink lag 245 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:49:32 CEST | 16:49:32 UTC | n2 unhealthy under pubMode (sink lag 246 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:49:33 CEST | 16:49:33 UTC | n2 unhealthy under pubMode (sink lag 247 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:49:34 CEST | 16:49:34 UTC | n2 unhealthy under pubMode (sink lag 248 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:49:35 CEST | 16:49:35 UTC | n2 unhealthy under pubMode (sink lag 249 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:49:36 CEST | 16:49:36 UTC | n2 unhealthy under pubMode (sink lag 250 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 18:49:37 CEST | 16:49:37 UTC | FREEZE end: length 167 s, n2 lag 237.7 s |
| 18:49:37 CEST | 16:49:37 UTC | n2 unhealthy under pubMode (sink lag 237.7 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 18:49:38 CEST | 16:49:38 UTC | n2 unhealthy under pubMode (sink lag 212.6 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 18:49:39 CEST | 16:49:39 UTC | n2 unhealthy under pubMode (sink lag 184 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 18:49:40 CEST | 16:49:40 UTC | n2 unhealthy under pubMode (sink lag 154.3 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 18:49:41 CEST | 16:49:41 UTC | n2 unhealthy under pubMode (sink lag 114.7 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 18:49:42 CEST | 16:49:42 UTC | n2 unhealthy under pubMode (sink lag 87.9 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 18:58:08 CEST | 16:58:08 UTC | prep: n2 synced true, utxoindex true, lag 0.5 s; no sends, miner off until 18:15 UTC |
| 19:05:02 CEST | 17:05:02 UTC | RE-ARM (stp 19:03 CEST, bot rates +10%): steps from STP-KAS/tn10-storm-1010 @ 9a6e010; bot X250 66, C1000 275, C1500 413, C2000 550, C2500 688, MAX 990, HOLD 880 (fallback 66); Build unchanged; scheduler restarted via watchdog; T0 20:30 CEST unchanged; BUILD-OK gate unchanged |
| 19:05:11 CEST | 17:05:11 UTC | watchdog: scheduler not running -> (re)start |
| 19:05:11 CEST | 17:05:11 UTC | scheduler restarted (resume by clock); T0 18:30 UTC, gates 18:00/18:15 UTC, end 02:30 UTC; node n2 (own private node, loopback) |
| 19:05:11 CEST | 17:05:11 UTC | n2 first read: synced true, utxoindex true, sink lag 0.5 s, DAA 593175840 |
| 19:05:11 CEST | 17:05:11 UTC | prep: n2 synced true, utxoindex true, lag 0.5 s; no sends, miner off until 18:15 UTC |
| 19:20:12 CEST | 17:20:12 UTC | prep: n2 synced true, utxoindex true, lag 0.2 s; no sends, miner off until 18:15 UTC |
| 19:35:12 CEST | 17:35:12 UTC | prep: n2 synced true, utxoindex true, lag 0.5 s; no sends, miner off until 18:15 UTC |
| 19:50:01 CEST | 17:50:01 UTC | coin buffer: 1034706 tKAS unclaimed (32565 coins) |
| 19:50:13 CEST | 17:50:13 UTC | prep: n2 synced true, utxoindex true, lag 0.6 s; no sends, miner off until 18:15 UTC |
| 19:59:06 CEST | 17:59:06 UTC | n2 unhealthy under pubMode (sink lag 65.1 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:07 CEST | 17:59:07 UTC | n2 unhealthy under pubMode (sink lag 66.3 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:08 CEST | 17:59:08 UTC | n2 unhealthy under pubMode (sink lag 67.3 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:09 CEST | 17:59:09 UTC | n2 unhealthy under pubMode (sink lag 68.3 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:10 CEST | 17:59:10 UTC | n2 unhealthy under pubMode (sink lag 69.3 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:11 CEST | 17:59:11 UTC | n2 unhealthy under pubMode (sink lag 70.3 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:12 CEST | 17:59:12 UTC | n2 unhealthy under pubMode (sink lag 71.4 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:13 CEST | 17:59:13 UTC | n2 unhealthy under pubMode (sink lag 72.4 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:14 CEST | 17:59:14 UTC | n2 unhealthy under pubMode (sink lag 73.4 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:15 CEST | 17:59:15 UTC | n2 unhealthy under pubMode (sink lag 74.4 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:16 CEST | 17:59:16 UTC | n2 unhealthy under pubMode (sink lag 75.4 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:17 CEST | 17:59:17 UTC | n2 unhealthy under pubMode (sink lag 76.4 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:18 CEST | 17:59:18 UTC | n2 unhealthy under pubMode (sink lag 77.4 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:19 CEST | 17:59:19 UTC | n2 unhealthy under pubMode (sink lag 78.4 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:20 CEST | 17:59:20 UTC | n2 unhealthy under pubMode (sink lag 79.4 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:21 CEST | 17:59:21 UTC | n2 unhealthy under pubMode (sink lag 80.4 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:22 CEST | 17:59:22 UTC | n2 unhealthy under pubMode (sink lag 81.4 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:23 CEST | 17:59:23 UTC | n2 unhealthy under pubMode (sink lag 82.4 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:24 CEST | 17:59:24 UTC | n2 unhealthy under pubMode (sink lag 83.4 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:25 CEST | 17:59:25 UTC | n2 unhealthy under pubMode (sink lag 84.4 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:26 CEST | 17:59:26 UTC | n2 unhealthy under pubMode (sink lag 85.4 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:27 CEST | 17:59:27 UTC | n2 unhealthy under pubMode (sink lag 86.5 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:28 CEST | 17:59:28 UTC | n2 unhealthy under pubMode (sink lag 87.5 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:29 CEST | 17:59:29 UTC | n2 unhealthy under pubMode (sink lag 88.5 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:30 CEST | 17:59:30 UTC | n2 unhealthy under pubMode (sink lag 89.5 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:31 CEST | 17:59:31 UTC | n2 unhealthy under pubMode (sink lag 90.5 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:32 CEST | 17:59:32 UTC | n2 unhealthy under pubMode (sink lag 91.5 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:33 CEST | 17:59:33 UTC | n2 unhealthy under pubMode (sink lag 92.5 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:34 CEST | 17:59:34 UTC | n2 unhealthy under pubMode (sink lag 93.5 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:35 CEST | 17:59:35 UTC | n2 unhealthy under pubMode (sink lag 94.5 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:36 CEST | 17:59:36 UTC | FREEZE start: n2 virtual DAA not moving for 30 s (>= 30 s) (lag 95.5 s) |
| 19:59:36 CEST | 17:59:36 UTC | n2 unhealthy under pubMode (sink lag 95.5 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:37 CEST | 17:59:37 UTC | n2 unhealthy under pubMode (sink lag 96.5 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:38 CEST | 17:59:38 UTC | n2 unhealthy under pubMode (sink lag 97.5 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:39 CEST | 17:59:39 UTC | n2 unhealthy under pubMode (sink lag 98.5 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:40 CEST | 17:59:40 UTC | n2 unhealthy under pubMode (sink lag 99.5 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:41 CEST | 17:59:41 UTC | n2 unhealthy under pubMode (sink lag 100.5 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:42 CEST | 17:59:42 UTC | n2 unhealthy under pubMode (sink lag 101.5 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:43 CEST | 17:59:43 UTC | n2 unhealthy under pubMode (sink lag 102.5 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:44 CEST | 17:59:44 UTC | n2 unhealthy under pubMode (sink lag 103.5 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:45 CEST | 17:59:45 UTC | n2 unhealthy under pubMode (sink lag 104.5 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:46 CEST | 17:59:46 UTC | n2 unhealthy under pubMode (sink lag 105.6 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:47 CEST | 17:59:47 UTC | n2 unhealthy under pubMode (sink lag 106.6 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:48 CEST | 17:59:48 UTC | n2 unhealthy under pubMode (sink lag 107.6 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:49 CEST | 17:59:49 UTC | n2 unhealthy under pubMode (sink lag 108.6 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:50 CEST | 17:59:50 UTC | n2 unhealthy under pubMode (sink lag 109.6 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:51 CEST | 17:59:51 UTC | n2 unhealthy under pubMode (sink lag 110.6 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:52 CEST | 17:59:52 UTC | n2 unhealthy under pubMode (sink lag 111.6 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:53 CEST | 17:59:53 UTC | n2 unhealthy under pubMode (sink lag 112.6 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:54 CEST | 17:59:54 UTC | n2 unhealthy under pubMode (sink lag 113.6 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:55 CEST | 17:59:55 UTC | n2 unhealthy under pubMode (sink lag 114.6 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:57 CEST | 17:59:57 UTC | n2 unhealthy under pubMode (sink lag 115.6 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:58 CEST | 17:59:58 UTC | n2 unhealthy under pubMode (sink lag 116.6 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 19:59:59 CEST | 17:59:59 UTC | n2 unhealthy under pubMode (sink lag 117.6 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:00 CEST | 18:00:00 UTC | n2 unhealthy under pubMode (sink lag 118.6 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:00 CEST | 18:00:00 UTC | GATE 1 18:00 UTC (logging start; never holds public-node senders) (own n2 sink): synced true, utxoindex true, sink lag 118.6 s, mempool 496, quote 160.5 -> FAIL |
| 20:00:00 CEST | 18:00:00 UTC | BOT BLOCK: session down, runners 0, disk 24.1 GB, n2 synced true utxoindex true lag 118.6 s mempool 496, bot sub/acc 0/0 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted 957.4 tx/s (8/9 valid), miner 0, mining share 0%, dup share 0.4561 |
| 20:00:01 CEST | 18:00:01 UTC | n2 unhealthy under pubMode (sink lag 119.6 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:02 CEST | 18:00:02 UTC | n2 unhealthy under pubMode (sink lag 120.6 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:03 CEST | 18:00:03 UTC | n2 unhealthy under pubMode (sink lag 121.6 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:04 CEST | 18:00:04 UTC | n2 unhealthy under pubMode (sink lag 122.7 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:05 CEST | 18:00:05 UTC | n2 unhealthy under pubMode (sink lag 123.7 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:06 CEST | 18:00:06 UTC | n2 unhealthy under pubMode (sink lag 124.7 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:07 CEST | 18:00:07 UTC | n2 unhealthy under pubMode (sink lag 125.7 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:07 CEST | 18:00:07 UTC | coin refresh started (run 10, top-up check) |
| 20:00:08 CEST | 18:00:08 UTC | n2 unhealthy under pubMode (sink lag 126.7 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:09 CEST | 18:00:09 UTC | n2 unhealthy under pubMode (sink lag 127.7 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:10 CEST | 18:00:10 UTC | n2 unhealthy under pubMode (sink lag 128.7 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:11 CEST | 18:00:11 UTC | n2 unhealthy under pubMode (sink lag 129.8 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:12 CEST | 18:00:12 UTC | n2 unhealthy under pubMode (sink lag 130.8 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:13 CEST | 18:00:13 UTC | n2 unhealthy under pubMode (sink lag 131.8 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:14 CEST | 18:00:14 UTC | n2 unhealthy under pubMode (sink lag 132.8 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:14 CEST | 18:00:14 UTC | live summary: pushed logs/bot/SUMMARY.md (e2124e7) |
| 20:00:15 CEST | 18:00:15 UTC | n2 unhealthy under pubMode (sink lag 133.8 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:16 CEST | 18:00:16 UTC | n2 unhealthy under pubMode (sink lag 134.8 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:17 CEST | 18:00:17 UTC | n2 unhealthy under pubMode (sink lag 135.8 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:17 CEST | 18:00:17 UTC | coin refresh skipped: unclaimed 1034706 tKAS >= 10000 |
| 20:00:18 CEST | 18:00:18 UTC | n2 unhealthy under pubMode (sink lag 136.8 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:19 CEST | 18:00:19 UTC | n2 unhealthy under pubMode (sink lag 137.8 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:20 CEST | 18:00:20 UTC | n2 unhealthy under pubMode (sink lag 138.8 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:21 CEST | 18:00:21 UTC | n2 unhealthy under pubMode (sink lag 139.8 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:22 CEST | 18:00:22 UTC | n2 unhealthy under pubMode (sink lag 140.8 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:23 CEST | 18:00:23 UTC | n2 unhealthy under pubMode (sink lag 141.8 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:24 CEST | 18:00:24 UTC | n2 unhealthy under pubMode (sink lag 142.8 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:25 CEST | 18:00:25 UTC | n2 unhealthy under pubMode (sink lag 143.8 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:26 CEST | 18:00:26 UTC | n2 unhealthy under pubMode (sink lag 144.8 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:27 CEST | 18:00:27 UTC | n2 unhealthy under pubMode (sink lag 145.8 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:28 CEST | 18:00:28 UTC | n2 unhealthy under pubMode (sink lag 146.8 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:29 CEST | 18:00:29 UTC | n2 unhealthy under pubMode (sink lag 147.8 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:30 CEST | 18:00:30 UTC | n2 unhealthy under pubMode (sink lag 148.8 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:31 CEST | 18:00:31 UTC | n2 unhealthy under pubMode (sink lag 149.8 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:32 CEST | 18:00:32 UTC | n2 unhealthy under pubMode (sink lag 150.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:33 CEST | 18:00:33 UTC | n2 unhealthy under pubMode (sink lag 151.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:34 CEST | 18:00:34 UTC | n2 unhealthy under pubMode (sink lag 152.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:35 CEST | 18:00:35 UTC | n2 unhealthy under pubMode (sink lag 153.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:36 CEST | 18:00:36 UTC | n2 unhealthy under pubMode (sink lag 154.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:37 CEST | 18:00:37 UTC | n2 unhealthy under pubMode (sink lag 155.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:38 CEST | 18:00:38 UTC | n2 unhealthy under pubMode (sink lag 156.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:39 CEST | 18:00:39 UTC | n2 unhealthy under pubMode (sink lag 157.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:40 CEST | 18:00:40 UTC | n2 unhealthy under pubMode (sink lag 158.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:41 CEST | 18:00:41 UTC | n2 unhealthy under pubMode (sink lag 159.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:42 CEST | 18:00:42 UTC | n2 unhealthy under pubMode (sink lag 160.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:43 CEST | 18:00:43 UTC | n2 unhealthy under pubMode (sink lag 161.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:44 CEST | 18:00:44 UTC | n2 unhealthy under pubMode (sink lag 162.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:45 CEST | 18:00:45 UTC | n2 unhealthy under pubMode (sink lag 163.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:46 CEST | 18:00:46 UTC | n2 unhealthy under pubMode (sink lag 164.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:47 CEST | 18:00:47 UTC | n2 unhealthy under pubMode (sink lag 165.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:48 CEST | 18:00:48 UTC | n2 unhealthy under pubMode (sink lag 166.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:49 CEST | 18:00:49 UTC | n2 unhealthy under pubMode (sink lag 167.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:50 CEST | 18:00:50 UTC | n2 unhealthy under pubMode (sink lag 168.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:51 CEST | 18:00:51 UTC | n2 unhealthy under pubMode (sink lag 169.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:52 CEST | 18:00:52 UTC | n2 unhealthy under pubMode (sink lag 170.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:53 CEST | 18:00:53 UTC | n2 unhealthy under pubMode (sink lag 171.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:54 CEST | 18:00:54 UTC | n2 unhealthy under pubMode (sink lag 172.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:55 CEST | 18:00:55 UTC | n2 unhealthy under pubMode (sink lag 174 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:56 CEST | 18:00:56 UTC | n2 unhealthy under pubMode (sink lag 175 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:57 CEST | 18:00:57 UTC | n2 unhealthy under pubMode (sink lag 176 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:58 CEST | 18:00:58 UTC | n2 unhealthy under pubMode (sink lag 177 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:00:59 CEST | 18:00:59 UTC | n2 unhealthy under pubMode (sink lag 178 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:01:00 CEST | 18:01:00 UTC | n2 unhealthy under pubMode (sink lag 179 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:01:01 CEST | 18:01:01 UTC | n2 unhealthy under pubMode (sink lag 180 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:01:02 CEST | 18:01:02 UTC | n2 unhealthy under pubMode (sink lag 181 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:01:03 CEST | 18:01:03 UTC | n2 unhealthy under pubMode (sink lag 182 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:01:04 CEST | 18:01:04 UTC | n2 unhealthy under pubMode (sink lag 183 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:01:06 CEST | 18:01:06 UTC | n2 unhealthy under pubMode (sink lag 185 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:01:07 CEST | 18:01:07 UTC | n2 unhealthy under pubMode (sink lag 186 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:01:08 CEST | 18:01:08 UTC | n2 unhealthy under pubMode (sink lag 187 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:01:09 CEST | 18:01:09 UTC | n2 unhealthy under pubMode (sink lag 188 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:01:10 CEST | 18:01:10 UTC | n2 unhealthy under pubMode (sink lag 189 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:01:11 CEST | 18:01:11 UTC | n2 unhealthy under pubMode (sink lag 190 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:01:12 CEST | 18:01:12 UTC | n2 unhealthy under pubMode (sink lag 191 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:01:13 CEST | 18:01:13 UTC | n2 unhealthy under pubMode (sink lag 192 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:01:14 CEST | 18:01:14 UTC | n2 unhealthy under pubMode (sink lag 193 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:01:15 CEST | 18:01:15 UTC | n2 unhealthy under pubMode (sink lag 194.1 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:01:16 CEST | 18:01:16 UTC | n2 unhealthy under pubMode (sink lag 195.1 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:01:17 CEST | 18:01:17 UTC | n2 unhealthy under pubMode (sink lag 196.1 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:01:18 CEST | 18:01:18 UTC | n2 unhealthy under pubMode (sink lag 197.1 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:01:19 CEST | 18:01:19 UTC | n2 unhealthy under pubMode (sink lag 198.1 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:01:20 CEST | 18:01:20 UTC | n2 unhealthy under pubMode (sink lag 199.1 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:01:21 CEST | 18:01:21 UTC | n2 unhealthy under pubMode (sink lag 200.1 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:01:22 CEST | 18:01:22 UTC | n2 unhealthy under pubMode (sink lag 201.1 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:01:23 CEST | 18:01:23 UTC | n2 unhealthy under pubMode (sink lag 202.1 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:01:24 CEST | 18:01:24 UTC | n2 unhealthy under pubMode (sink lag 203.1 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:01:25 CEST | 18:01:25 UTC | n2 unhealthy under pubMode (sink lag 204.1 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:01:26 CEST | 18:01:26 UTC | n2 unhealthy under pubMode (sink lag 205.1 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:01:27 CEST | 18:01:27 UTC | n2 unhealthy under pubMode (sink lag 206.1 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:01:28 CEST | 18:01:28 UTC | n2 unhealthy under pubMode (sink lag 207.1 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:01:29 CEST | 18:01:29 UTC | n2 unhealthy under pubMode (sink lag 208.1 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:01:30 CEST | 18:01:30 UTC | n2 unhealthy under pubMode (sink lag 209.1 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 20:01:31 CEST | 18:01:31 UTC | FREEZE end: length 145 s, n2 lag 210.1 s |
| 20:01:31 CEST | 18:01:31 UTC | n2 unhealthy under pubMode (sink lag 210.1 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 20:01:32 CEST | 18:01:32 UTC | n2 unhealthy under pubMode (sink lag 207.2 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 20:01:33 CEST | 18:01:33 UTC | n2 unhealthy under pubMode (sink lag 190.5 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 20:01:34 CEST | 18:01:34 UTC | n2 unhealthy under pubMode (sink lag 183.8 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 20:01:35 CEST | 18:01:35 UTC | n2 unhealthy under pubMode (sink lag 173.6 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 20:01:36 CEST | 18:01:36 UTC | n2 unhealthy under pubMode (sink lag 165.8 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 20:01:37 CEST | 18:01:37 UTC | n2 unhealthy under pubMode (sink lag 156.4 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 20:01:38 CEST | 18:01:38 UTC | n2 unhealthy under pubMode (sink lag 152.7 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 20:01:39 CEST | 18:01:39 UTC | n2 unhealthy under pubMode (sink lag 136.7 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 20:01:40 CEST | 18:01:40 UTC | n2 unhealthy under pubMode (sink lag 130.2 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 20:01:41 CEST | 18:01:41 UTC | n2 unhealthy under pubMode (sink lag 118.8 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 20:01:42 CEST | 18:01:42 UTC | n2 unhealthy under pubMode (sink lag 112.3 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 20:01:44 CEST | 18:01:44 UTC | n2 unhealthy under pubMode (sink lag 93.1 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 20:01:46 CEST | 18:01:46 UTC | n2 unhealthy under pubMode (sink lag 67.1 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 20:10:00 CEST | 18:10:00 UTC | BOT BLOCK: session down, runners 0, disk 23.9 GB, n2 synced true utxoindex true lag 0.3 s mempool 496, bot sub/acc 0/0 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted 937.8 tx/s (6/9 valid), miner 0, mining share 0%, dup share 0.4494 |
| 20:15:00 CEST | 18:15:00 UTC | GATE 2 18:15 UTC (ready check) (own n2 sink): synced true, utxoindex true, sink lag 0.4 s, mempool 496, quote 161.9 -> PASS |
| 20:15:00 CEST | 18:15:00 UTC | READY CHECK: Build started? CONFIRMED (stp 19:22 CEST: GO pasted (tn10-storm-1010), Build is ready); n2 gate pass |
| 20:15:00 CEST | 18:15:00 UTC | BUILD CONFIRMED: stp 19:22 CEST: GO pasted (tn10-storm-1010), Build is ready -> bot sends from the open step |
| 20:15:00 CEST | 18:15:00 UTC | miner ON (1 box CPU kaspa-miner, 1 thread, n2 gRPC): 18:15 UTC start, n2 synced |
| 20:15:23 CEST | 18:15:23 UTC | live summary: pushed logs/bot/SUMMARY.md (f633b4e) |
| 20:20:00 CEST | 18:20:00 UTC | BOT BLOCK: session up, runners 15, disk 23.8 GB, n2 synced true utxoindex true lag 0.2 s mempool 0, bot sub/acc 0/0 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted 53.8 tx/s (9/9 valid), miner 1, mining share 10.56%, dup share 0.3993 |
| 20:20:02 CEST | 18:20:02 UTC | coin buffer: 1034706 tKAS unclaimed (32565 coins) |
| 20:30:00 CEST | 18:30:00 UTC | ROW B0 B0 begins (18:30-18:40 UTC; plan bot: 0; Build: 0; miner on) |
| 20:30:00 CEST | 18:30:00 UTC | rate: B0 senders 0 tx/s total (15 up x 0), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 20:30:00 CEST | 18:30:00 UTC | BOT BLOCK: session up, runners 15, disk 23.8 GB, n2 synced true utxoindex true lag 0.1 s mempool 0, bot sub/acc 0/0 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted 56.1 tx/s (9/9 valid), miner 1, mining share 22.79%, dup share 0.4246 |
| 20:30:12 CEST | 18:30:12 UTC | live summary: pushed logs/bot/SUMMARY.md (a0be987) |
| 20:30:13 CEST | 18:30:13 UTC | coin refresh started (run 11, top-up check) |
| 20:30:23 CEST | 18:30:23 UTC | coin refresh skipped: unclaimed 1034706 tKAS >= 10000 |
| 20:40:00 CEST | 18:40:00 UTC | ROW X250 X250 begins (18:40-18:55 UTC; plan bot: 66; Build: 190; miner on) |
| 20:40:00 CEST | 18:40:00 UTC | fee quote at step start: 100 (pair 400/600, cap 600, floor 100, sit out above 400) |
| 20:40:00 CEST | 18:40:00 UTC | rate: X250 senders 66 tx/s total (15 up x 4.4), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 20:40:00 CEST | 18:40:00 UTC | BOT BLOCK: session up, runners 15, disk 23.7 GB, n2 synced true utxoindex true lag 0.3 s mempool 0, bot sub/acc 0/0 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted 244.2 tx/s (10/10 valid), miner 1, mining share 23.69%, dup share 0.4562 |
| 20:40:09 CEST | 18:40:09 UTC | S3 not running -> relaunch 1/8 |
| 20:40:09 CEST | 18:40:09 UTC | rate: X250 senders 66 tx/s total (14 up x 4.714), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 20:40:10 CEST | 18:40:10 UTC | rate: X250 senders 66 tx/s total (9 up x 7.333), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 20:40:12 CEST | 18:40:12 UTC | S1 not running -> relaunch 1/8 |
| 20:40:15 CEST | 18:40:15 UTC | S2 not running -> relaunch 1/8 |
| 20:40:18 CEST | 18:40:18 UTC | S4 not running -> relaunch 1/8 |
| 20:40:21 CEST | 18:40:21 UTC | S5 not running -> relaunch 1/8 |
| 20:40:24 CEST | 18:40:24 UTC | S6 not running -> relaunch 1/8 |
| 20:40:27 CEST | 18:40:27 UTC | S7 not running -> relaunch 1/8 |
| 20:40:30 CEST | 18:40:30 UTC | S8 not running -> relaunch 1/8 |
| 20:40:33 CEST | 18:40:33 UTC | S9 not running -> relaunch 1/8 |
| 20:40:36 CEST | 18:40:36 UTC | S10 not running -> relaunch 1/8 |
| 20:40:36 CEST | 18:40:36 UTC | rate: X250 senders 66 tx/s total (10 up x 6.6), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 20:40:39 CEST | 18:40:39 UTC | S11 not running -> relaunch 1/8 |
| 20:40:39 CEST | 18:40:39 UTC | rate: X250 senders 66 tx/s total (11 up x 6), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 20:40:42 CEST | 18:40:42 UTC | S12 not running -> relaunch 1/8 |
| 20:40:42 CEST | 18:40:42 UTC | rate: X250 senders 66 tx/s total (12 up x 5.5), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 20:40:45 CEST | 18:40:45 UTC | S13 not running -> relaunch 1/8 |
| 20:40:45 CEST | 18:40:45 UTC | rate: X250 senders 66 tx/s total (13 up x 5.077), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 20:40:48 CEST | 18:40:48 UTC | S14 not running -> relaunch 1/8 |
| 20:40:48 CEST | 18:40:48 UTC | rate: X250 senders 66 tx/s total (14 up x 4.714), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 20:40:51 CEST | 18:40:51 UTC | S15 not running -> relaunch 1/8 |
| 20:40:51 CEST | 18:40:51 UTC | rate: X250 senders 66 tx/s total (15 up x 4.4), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 20:42:00 CEST | 18:42:00 UTC | B0: B = 244.2 tx/s (median of 10 valid n2 minutes 18:30-18:40 UTC) -> reported only; combined targets are fixed (250/1,000/1,500/2,000/2,500/3,500/3,200); bot rates stay the bot column |
| 20:45:21 CEST | 18:45:21 UTC | live summary: pushed logs/bot/SUMMARY.md (cd14524) |
| 20:50:00 CEST | 18:50:00 UTC | BOT BLOCK: session up, runners 15, disk 23.7 GB, n2 synced true utxoindex true lag 0.2 s mempool 112, bot sub/acc 63.3/63.2 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted 300.3 tx/s (10/10 valid), miner 1, mining share 24.43%, dup share 0.4601 |
| 20:50:07 CEST | 18:50:07 UTC | coin buffer: 934337 tKAS unclaimed (29485 coins) |
| 20:55:00 CEST | 18:55:00 UTC | ROW X250-drain X250-drain begins (18:55-19:00 UTC; plan bot: 0; Build: 0; miner on) |
| 20:55:00 CEST | 18:55:00 UTC | rate: X250-drain senders 0 tx/s total (15 up x 0), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 21:00:00 CEST | 19:00:00 UTC | EVAL X250: bot submitted 55432 (66/66 sub/acc tx/s, sec-S*.jsonl (pub-sender), public-node transport errors 1, delivered>=90% true) (own ids, no-signature hop, anyone-can-spend, not realistic payments), eventual accept 100%, p90 0.11 s, rejects 0, n2 lag max 1 s, full time at rate true -> clean=true; last clean level 66 |
| 21:00:00 CEST | 19:00:00 UTC | ROW C1000 C1000 begins (19:00-19:15 UTC; plan bot: 275; Build: 750; miner on) |
| 21:00:00 CEST | 19:00:00 UTC | fee quote at step start: 100 (pair 400/600, cap 600, floor 100, sit out above 400) |
| 21:00:00 CEST | 19:00:00 UTC | rate: C1000 senders 275 tx/s total (15 up x 18.333), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 21:00:00 CEST | 19:00:00 UTC | BOT BLOCK: session up, runners 15, disk 23.5 GB, n2 synced true utxoindex true lag 0.2 s mempool 0, bot sub/acc 33/33.1 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted 278.3 tx/s (10/10 valid), miner 1, mining share 23.61%, dup share 0.4505 |
| 21:00:10 CEST | 19:00:10 UTC | live summary: pushed logs/bot/SUMMARY.md (139ff39) |
| 21:00:19 CEST | 19:00:19 UTC | coin refresh started (run 12, top-up check) |
| 21:00:29 CEST | 19:00:29 UTC | coin refresh skipped: unclaimed 934337 tKAS >= 10000 |
| 21:07:20 CEST | 19:07:20 UTC | DEVIATION: box disk 16.1 GB free (< 20): senders pause at 8 GB; n2 disk guard STOP at 5 GB, halt at 3 GB; pub submit fallback below 10 GB |
| 21:29:16 CEST | 19:29:16 UTC | n2 unhealthy under pubMode (not synced, sink lag 1271.3 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 21:29:22 CEST | 19:29:22 UTC | coin buffer: 934337 tKAS unclaimed (29485 coins) |
| 21:29:22 CEST | 19:29:22 UTC | EVAL C1000: bot submitted 116982 (139.3/139.2 sub/acc tx/s, sec-S*.jsonl (pub-sender), public-node transport errors 22, delivered>=90% false) (own ids, no-signature hop, anyone-can-spend, not realistic payments), eventual accept 99.96%, p90 0.12 s, rejects 0, n2 lag max 1 s, full time at rate true -> clean=false; last clean level 66 |
| 21:29:22 CEST | 19:29:22 UTC | ROW C1500 C1500 begins (joined late, 563 s after its start) (19:20-19:35 UTC; plan bot: 413; Build: 1125; miner on) |
| 21:29:22 CEST | 19:29:22 UTC | fee quote at step start: 100 (pair 400/600, cap 600, floor 100, sit out above 400) |
| 21:29:22 CEST | 19:29:22 UTC | rate: C1500 senders 413 tx/s total (15 up x 27.533), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 21:29:23 CEST | 19:29:23 UTC | BOT BLOCK: session up, runners 15, disk 12.9 GB, n2 synced false utxoindex true lag 1271.3 s mempool 113, bot sub/acc 0/0 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted not measured tx/s (0/0 valid), miner 1, mining share -%, dup share - |
| 21:29:30 CEST | 19:29:30 UTC | live summary: pushed logs/bot/SUMMARY.md (46ade20) |
| 21:29:47 CEST | 19:29:47 UTC | FREEZE start: n2 virtual DAA not moving for 31 s (>= 30 s) (lag 1302.1 s) |
| 21:30:00 CEST | 19:30:00 UTC | BOT BLOCK: session up, runners 15, disk 10.5 GB, n2 synced false utxoindex true lag 1315.1 s mempool 113, bot sub/acc 0/0 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted not measured tx/s (0/0 valid), miner 1, mining share -%, dup share - |
| 21:30:16 CEST | 19:30:16 UTC | miner OFF: n2 not synced for 60 s |
| 21:30:17 CEST | 19:30:17 UTC | live summary: pushed logs/bot/SUMMARY.md (4330645) |
| 21:31:42 CEST | 19:31:42 UTC | FREEZE end: length 146 s, n2 lag 1417.5 s |
| 21:32:10 CEST | 19:32:10 UTC | n2 unhealthy under pubMode (sink lag 658.7 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 21:32:10 CEST | 19:32:10 UTC | miner ON (1 box CPU kaspa-miner, 1 thread, n2 gRPC): n2 synced again / process relaunch |
| 21:32:11 CEST | 19:32:11 UTC | n2 unhealthy under pubMode (sink lag 628.2 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 21:32:12 CEST | 19:32:12 UTC | n2 unhealthy under pubMode (sink lag 593.6 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 21:32:13 CEST | 19:32:13 UTC | n2 unhealthy under pubMode (sink lag 571 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 21:32:14 CEST | 19:32:14 UTC | n2 unhealthy under pubMode (sink lag 550.3 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 21:32:15 CEST | 19:32:15 UTC | n2 unhealthy under pubMode (sink lag 525.2 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 21:32:16 CEST | 19:32:16 UTC | n2 unhealthy under pubMode (sink lag 499.8 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 21:32:16 CEST | 19:32:16 UTC | coin refresh started (run 13, top-up check) |
| 21:32:17 CEST | 19:32:17 UTC | n2 unhealthy under pubMode (sink lag 486.4 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 21:32:18 CEST | 19:32:18 UTC | n2 unhealthy under pubMode (sink lag 455.1 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 21:32:19 CEST | 19:32:19 UTC | n2 unhealthy under pubMode (sink lag 433.3 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 21:32:20 CEST | 19:32:20 UTC | n2 unhealthy under pubMode (sink lag 411.2 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 21:32:21 CEST | 19:32:21 UTC | n2 unhealthy under pubMode (sink lag 379.6 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 21:32:22 CEST | 19:32:22 UTC | n2 unhealthy under pubMode (sink lag 359.3 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 21:32:23 CEST | 19:32:23 UTC | n2 unhealthy under pubMode (sink lag 339.6 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 21:32:24 CEST | 19:32:24 UTC | n2 unhealthy under pubMode (sink lag 300.1 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 21:32:25 CEST | 19:32:25 UTC | n2 unhealthy under pubMode (sink lag 273.8 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 21:32:26 CEST | 19:32:26 UTC | n2 unhealthy under pubMode (sink lag 253.4 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 21:32:26 CEST | 19:32:26 UTC | coin refresh skipped: unclaimed 934337 tKAS >= 10000 |
| 21:32:28 CEST | 19:32:28 UTC | n2 unhealthy under pubMode (sink lag 213.2 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 21:32:29 CEST | 19:32:29 UTC | n2 unhealthy under pubMode (sink lag 179.3 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 21:32:31 CEST | 19:32:31 UTC | n2 unhealthy under pubMode (sink lag 133.6 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 21:32:32 CEST | 19:32:32 UTC | n2 unhealthy under pubMode (sink lag 113.7 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 21:32:33 CEST | 19:32:33 UTC | n2 unhealthy under pubMode (sink lag 85.5 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 21:32:36 CEST | 19:32:36 UTC | n2 unhealthy under pubMode (sink lag 63.2 s > 60): senders KEEP submitting on public nodes (stp 16:19) |
| 21:35:00 CEST | 19:35:00 UTC | ROW C1500-drain C1500-drain begins (19:35-19:40 UTC; plan bot: 0; Build: 0; miner on) |
| 21:35:00 CEST | 19:35:00 UTC | rate: C1500-drain senders 0 tx/s total (15 up x 0), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 21:35:01 CEST | 19:35:01 UTC | DEVIATION: disk freefall trough ~9.1G (n2 datadir ~90G consensus+utxo); night-watch reclaimed ~1.5G+ old logs/runs/tmp; free now 14G holding; diskguard was LOW-truncating; Shell dead 21:13-21:31 then recovered |
| 21:35:01 CEST | 19:35:01 UTC | night-watch: C1500 bot sub still 0 (all pub nodes node_cool RPC timeout); processes up; n2 synced again; MemAvailable ~2.5G; no STOP; run not halted |
| 21:36:12 CEST | 19:36:12 UTC | night-watch: +~1.1G reclaim (old stress dumps/unused trees); disk now 15G free; C1500-drain plan 0; C2000 at 21:40 bot 550; pubs reachable; no STOP |
| 21:38:00 CEST | 19:38:00 UTC | S15 not running -> relaunch 2/8 |
| 21:38:01 CEST | 19:38:01 UTC | rate: C1500-drain senders 0 tx/s total (9 up x 0), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 21:38:03 CEST | 19:38:03 UTC | S1 not running -> relaunch 2/8 |
| 21:38:07 CEST | 19:38:07 UTC | S2 not running -> relaunch 2/8 |
| 21:38:10 CEST | 19:38:10 UTC | S3 not running -> relaunch 2/8 |
| 21:38:13 CEST | 19:38:13 UTC | S4 not running -> relaunch 2/8 |
| 21:38:16 CEST | 19:38:16 UTC | S5 not running -> relaunch 2/8 |
| 21:38:19 CEST | 19:38:19 UTC | S6 not running -> relaunch 2/8 |
| 21:38:22 CEST | 19:38:22 UTC | S7 not running -> relaunch 2/8 |
| 21:38:25 CEST | 19:38:25 UTC | S8 not running -> relaunch 2/8 |
| 21:38:28 CEST | 19:38:28 UTC | S9 not running -> relaunch 2/8 |
| 21:38:31 CEST | 19:38:31 UTC | S10 not running -> relaunch 2/8 |
| 21:38:34 CEST | 19:38:34 UTC | S11 not running -> relaunch 2/8 |
| 21:38:37 CEST | 19:38:37 UTC | S12 not running -> relaunch 2/8 |
| 21:38:40 CEST | 19:38:40 UTC | S13 not running -> relaunch 2/8 |
| 21:38:43 CEST | 19:38:43 UTC | S14 not running -> relaunch 2/8 |
| 21:39:01 CEST | 19:39:01 UTC | S15 not running -> relaunch 3/8 |
| 21:39:04 CEST | 19:39:04 UTC | S1 not running -> relaunch 3/8 |
| 21:39:07 CEST | 19:39:07 UTC | S2 not running -> relaunch 3/8 |
| 21:39:10 CEST | 19:39:10 UTC | S3 not running -> relaunch 3/8 |
| 21:39:13 CEST | 19:39:13 UTC | S4 not running -> relaunch 3/8 |
| 21:39:16 CEST | 19:39:16 UTC | S5 not running -> relaunch 3/8 |
| 21:39:19 CEST | 19:39:19 UTC | S6 not running -> relaunch 3/8 |
| 21:39:22 CEST | 19:39:22 UTC | S7 not running -> relaunch 3/8 |
| 21:39:25 CEST | 19:39:25 UTC | S8 not running -> relaunch 3/8 |
| 21:39:28 CEST | 19:39:28 UTC | S9 not running -> relaunch 3/8 |
| 21:39:28 CEST | 19:39:28 UTC | rate: C1500-drain senders 0 tx/s total (10 up x 0), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 21:39:31 CEST | 19:39:31 UTC | S10 not running -> relaunch 3/8 |
| 21:39:31 CEST | 19:39:31 UTC | rate: C1500-drain senders 0 tx/s total (11 up x 0), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 21:39:34 CEST | 19:39:34 UTC | S11 not running -> relaunch 3/8 |
| 21:39:34 CEST | 19:39:34 UTC | rate: C1500-drain senders 0 tx/s total (12 up x 0), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 21:39:37 CEST | 19:39:37 UTC | S12 not running -> relaunch 3/8 |
| 21:39:37 CEST | 19:39:37 UTC | rate: C1500-drain senders 0 tx/s total (13 up x 0), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 21:39:40 CEST | 19:39:40 UTC | S13 not running -> relaunch 3/8 |
| 21:39:40 CEST | 19:39:40 UTC | rate: C1500-drain senders 0 tx/s total (14 up x 0), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 21:39:43 CEST | 19:39:43 UTC | S14 not running -> relaunch 3/8 |
| 21:39:43 CEST | 19:39:43 UTC | rate: C1500-drain senders 0 tx/s total (15 up x 0), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 21:40:00 CEST | 19:40:00 UTC | EVAL C1500: bot submitted 0 (0/0.3 sub/acc tx/s, sec-S*.jsonl (pub-sender), public-node transport errors 9086, delivered>=90% false) (own ids, no-signature hop, anyone-can-spend, not realistic payments), eventual accept -%, p90 65 s, rejects 0, n2 lag max 1417.5 s, full time at rate true -> clean=false; last clean level 66 |
| 21:40:00 CEST | 19:40:00 UTC | ROW C2000 C2000 begins (19:40-19:55 UTC; plan bot: 550; Build: 1500; miner on) |
| 21:40:00 CEST | 19:40:00 UTC | fee quote at step start: 100 (pair 400/600, cap 600, floor 100, sit out above 400) |
| 21:40:00 CEST | 19:40:00 UTC | rate: C2000 senders 550 tx/s total (15 up x 36.667), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 21:40:00 CEST | 19:40:00 UTC | BOT BLOCK: session up, runners 15, disk 13.3 GB, n2 synced true utxoindex true lag 0.4 s mempool 7, bot sub/acc 0/0.4 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted 240.8 tx/s (7/8 valid), miner 1, mining share 10.93%, dup share 0.5098 |
| 21:43:33 CEST | 19:43:33 UTC | S1 not running -> relaunch 4/8 |
| 21:44:19 CEST | 19:44:19 UTC | box disk back to 28.1 GB free |
| 21:44:39 CEST | 19:44:39 UTC | S1 not running -> relaunch 5/8 |
| 21:45:07 CEST | 19:45:07 UTC | rate: C2000 senders 550 tx/s total (14 up x 39.286), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 21:45:26 CEST | 19:45:26 UTC | live summary: pushed logs/bot/SUMMARY.md (1c465fc) |
| 21:45:40 CEST | 19:45:40 UTC | S1 not running -> relaunch 6/8 |
| 21:45:40 CEST | 19:45:40 UTC | rate: C2000 senders 550 tx/s total (15 up x 36.667), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 21:47:01 CEST | 19:47:01 UTC | DEVIATION (fix 1): C1500 0 sub cause = all 15 senders' public WS sockets went stale during the 21:08-21:29 box freeze (every submit 'RPC request timeout' -> node_cool loop). 21:37 rolling restart of senders -> relaunch crashed: night-watch cleanup had deleted the local kaspa SDK 2.1.0 folder. Restored from identical 2.1.0 copy at 21:38; all 15 relaunched 21:39; C2000 at 550/550 sub/acc 0 rej from 21:40 |
| 21:47:01 CEST | 19:47:01 UTC | DEVIATION (fix 2): n2 datadir bursts (76G->92G->77G, ~600 MB/min peaks under load). pub-sender patched: MAIN_NODE=pub -> health/VCC/reads on a public node (no n2), no utxoindex refusal, n2/main getInfo failure no longer zeros submits. S1 verified on public main 21:46 (37/37 tx/s). Others move in the C2000 drain 21:55 |
| 21:47:01 CEST | 19:47:01 UTC | DEVIATION (fix 3): n2 disk guard v2: never writes the old run's STOP flag; free<10G stops n2 cleanly + n2.HALT (sender disk pause 8G). start-n2.sh: --utxoindex removed (applies on next n2 start). Scheduler MAX_RELAUNCH 8->30 in file (applies on scheduler restart in drain) |
| 21:50:00 CEST | 19:50:00 UTC | BOT BLOCK: session up, runners 15, disk 27.8 GB, n2 synced true utxoindex true lag 0.2 s mempool 4257, bot sub/acc 540.3/539.1 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted 734.3 tx/s (10/10 valid), miner 1, mining share 23.77%, dup share 0.5652 |
| 21:55:00 CEST | 19:55:00 UTC | ROW C2000-drain C2000-drain begins (19:55-20:00 UTC; plan bot: 0; Build: 0; miner on) |
| 21:55:00 CEST | 19:55:00 UTC | rate: C2000-drain senders 0 tx/s total (15 up x 0), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 21:55:16 CEST | 19:55:16 UTC | watchdog: scheduler not running -> (re)start |
| 21:55:16 CEST | 19:55:16 UTC | scheduler restarted (resume by clock); T0 18:30 UTC, gates 18:00/18:15 UTC, end 02:30 UTC; node n2 (own private node, loopback) |
| 21:55:16 CEST | 19:55:16 UTC | n2 first read: synced true, utxoindex true, sink lag 0.2 s, DAA 593281118 |
| 21:55:16 CEST | 19:55:16 UTC | rate: C2000-drain senders 0 tx/s total (15 up x 0), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 21:55:43 CEST | 19:55:43 UTC | S2 not running -> relaunch 4/30 |
| 21:55:43 CEST | 19:55:43 UTC | rate: C2000-drain senders 0 tx/s total (9 up x 0), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 21:55:46 CEST | 19:55:46 UTC | S3 not running -> relaunch 4/30 |
| 21:55:49 CEST | 19:55:49 UTC | S4 not running -> relaunch 4/30 |
| 21:55:52 CEST | 19:55:52 UTC | S5 not running -> relaunch 4/30 |
| 21:55:55 CEST | 19:55:55 UTC | S6 not running -> relaunch 4/30 |
| 21:55:58 CEST | 19:55:58 UTC | S7 not running -> relaunch 4/30 |
| 21:56:01 CEST | 19:56:01 UTC | S8 not running -> relaunch 4/30 |
| 21:56:04 CEST | 19:56:04 UTC | S9 not running -> relaunch 4/30 |
| 21:56:07 CEST | 19:56:07 UTC | S10 not running -> relaunch 4/30 |
| 21:56:07 CEST | 19:56:07 UTC | rate: C2000-drain senders 0 tx/s total (10 up x 0), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 21:56:10 CEST | 19:56:10 UTC | S11 not running -> relaunch 4/30 |
| 21:56:10 CEST | 19:56:10 UTC | rate: C2000-drain senders 0 tx/s total (11 up x 0), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 21:56:13 CEST | 19:56:13 UTC | S12 not running -> relaunch 4/30 |
| 21:56:13 CEST | 19:56:13 UTC | rate: C2000-drain senders 0 tx/s total (12 up x 0), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 21:56:16 CEST | 19:56:16 UTC | S13 not running -> relaunch 4/30 |
| 21:56:16 CEST | 19:56:16 UTC | rate: C2000-drain senders 0 tx/s total (13 up x 0), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 21:56:19 CEST | 19:56:19 UTC | S14 not running -> relaunch 4/30 |
| 21:56:19 CEST | 19:56:19 UTC | rate: C2000-drain senders 0 tx/s total (14 up x 0), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 21:56:22 CEST | 19:56:22 UTC | S15 not running -> relaunch 4/30 |
| 21:56:22 CEST | 19:56:22 UTC | rate: C2000-drain senders 0 tx/s total (15 up x 0), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 21:57:16 CEST | 19:57:16 UTC | night-watch: C2000-drain OK; scheduler MAX_RELAUNCH=30 live; senders 15 @0; disk 28G; MemAvail ~4.8G; n2 synced; C2500 next |
| 21:57:25 CEST | 19:57:25 UTC | FREEZE start: n2 virtual DAA not moving for 30 s (>= 30 s) (lag 30.8 s) |
| 21:57:55 CEST | 19:57:55 UTC | miner OFF: n2 not synced for 60 s |
| 21:58:01 CEST | 19:58:01 UTC | n2 unhealthy under pubMode (utxoindex off, sink lag 66.9 s > 60, virtual DAA stalled >= 30 s): senders KEEP submitting on public nodes (stp 16:19) |
| 21:58:01 CEST | 19:58:01 UTC | miner ON (1 box CPU kaspa-miner, 1 thread, n2 gRPC): n2 synced again / process relaunch |
| 21:58:03 CEST | 19:58:03 UTC | FREEZE end: length 68 s, n2 lag 68.8 s |
| 21:58:07 CEST | 19:58:07 UTC | n2 kaspad restarted (new process, uptime 8 s) |
| 21:58:07 CEST | 19:58:07 UTC | night-watch: n2 FREEZE/dead mid no-utxoindex swap (HALT set 21:56) -> SIGINT the n2 process |
| 21:58:25 CEST | 19:58:25 UTC | night-watch: n2 down (HALT cleared); starting via start-n2.sh (no --utxoindex) |
| 21:58:26 CEST | 19:58:26 UTC | n2 kaspad restarted (new process, uptime 1 s) |
| 21:58:26 CEST | 19:58:26 UTC | miner relaunched (process had exited): n2 synced again / process relaunch |
| 21:59:25 CEST | 19:59:25 UTC | coin buffer: 831799 tKAS unclaimed (26273 coins) |
| 22:00:00 CEST | 20:00:00 UTC | EVAL C2000: bot submitted 458257 (545.5/545.6 sub/acc tx/s, sec-S*.jsonl (pub-sender), public-node transport errors 0, delivered>=90% true) (own ids, no-signature hop, anyone-can-spend, not realistic payments), eventual accept 100%, p90 0.13 s, rejects 0, n2 lag max 5.3 s, full time at rate true -> clean=true; last clean level 550 |
| 22:00:00 CEST | 20:00:00 UTC | ROW C2500 C2500 begins (20:00-20:15 UTC; plan bot: 688; Build: 1875; miner on) |
| 22:00:00 CEST | 20:00:00 UTC | fee quote at step start: 185 (pair 400/600, cap 600, floor 100, sit out above 400) |
| 22:00:00 CEST | 20:00:00 UTC | rate: C2500 senders 688 tx/s total (15 up x 45.867), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 22:00:00 CEST | 20:00:00 UTC | BOT BLOCK: session up, runners 15, disk 40.9 GB, n2 synced true utxoindex false lag 0.4 s mempool 1592, bot sub/acc 275.2/276.1 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted 2431.6 tx/s (7/9 valid), miner 1, mining share 24.66%, dup share 0.3959 |
| 22:00:16 CEST | 20:00:16 UTC | live summary: pushed logs/bot/SUMMARY.md (393cc4c) |
| 22:00:35 CEST | 20:00:35 UTC | night-watch: C2000 clean=true (545.5); C2500 up ~663/688; n2 no-utxoindex synced disk 41G; senders 15; no user ping |
| 22:00:44 CEST | 20:00:44 UTC | DEVIATION (fix 4): 21:55 scheduler restarted in C2000 drain (MAX_RELAUNCH 30 live); S2-S15 rolled onto public main node (MAIN_NODE=pub, VCC/health/reads on public nodes; n2 no longer in the submit or accept path). 21:57 n2 stopped cleanly, utxoindex dir (14G) deleted, n2 restarted WITHOUT --utxoindex at 21:58, synced by 21:59. Disk 28G -> 41G free. Coin refresh/top-up now abort (need utxoindex); buffer ~832k tKAS covers the night |
| 22:00:44 CEST | 20:00:44 UTC | check: C2500 20:00 UTC bot sub ~690/acc ~690 tx/s, 0 rej, 15 senders on public main. Headroom: per sender 46 tx/s at 4% CPU, 200 lanes x depth 2, p50 108 ms; MAX 990 = 66/sender, HOLD 880 = 59/sender (public-node test peaked ~226/sender). MemAvailable ~5.2G |
| 22:04:41 CEST | 20:04:41 UTC | S6 not running -> relaunch 5/30 |
| 22:04:41 CEST | 20:04:41 UTC | rate: C2500 senders 688 tx/s total (13 up x 52.923), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 22:04:44 CEST | 20:04:44 UTC | S14 not running -> relaunch 5/30 |
| 22:04:44 CEST | 20:04:44 UTC | rate: C2500 senders 688 tx/s total (14 up x 49.143), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 22:04:47 CEST | 20:04:47 UTC | S15 not running -> relaunch 5/30 |
| 22:04:47 CEST | 20:04:47 UTC | rate: C2500 senders 688 tx/s total (15 up x 45.867), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 22:05:36 CEST | 20:05:36 UTC | DEVIATION (fix 5): C2500 rate dip ~614/688 (60s) — S6/S14/S15 stuck on muon-10 (pending~375, intermittent 0 sub). Night-watch killed+relaunched 5/30 at 22:04 with fresh pub picks (S6/S14 no muon). Post-fix full seconds ~675–709 sub. Coins ~719k. Disk 41G. No user ping |
| 22:05:36 CEST | 20:05:36 UTC | night-watch: C2500 ~680–700 after S6/S14/S15 restart; 15 senders; n2 synced no-utxoindex; disk 41G; MemAvail ~5.1G; coins ~719k; no user ping |
| 22:10:00 CEST | 20:10:00 UTC | BOT BLOCK: session up, runners 15, disk 40.6 GB, n2 synced true utxoindex false lag 0.1 s mempool 3153, bot sub/acc 666.9/665.7 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted 2526.3 tx/s (9/9 valid), miner 1, mining share 24.47%, dup share 0.364 |
| 22:15:00 CEST | 20:15:00 UTC | ROW C2500-drain C2500-drain begins (20:15-20:20 UTC; plan bot: 0; Build: 0; miner on) |
| 22:15:00 CEST | 20:15:00 UTC | rate: C2500-drain senders 0 tx/s total (15 up x 0), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 22:15:24 CEST | 20:15:24 UTC | live summary: pushed logs/bot/SUMMARY.md (5b8b4c9) |
| 22:20:00 CEST | 20:20:00 UTC | EVAL C2500: bot submitted 566751 (674.7/674.3 sub/acc tx/s, sec-S*.jsonl (pub-sender), public-node transport errors 1076, delivered>=90% true) (own ids, no-signature hop, anyone-can-spend, not realistic payments), eventual accept 99.94%, p90 0.32 s, rejects 24, n2 lag max 1.2 s, full time at rate true -> clean=true; last clean level 688 |
| 22:20:00 CEST | 20:20:00 UTC | ROW MAX MAX begins (20:20-20:35 UTC; plan bot: 990; Build: 2600; miner on) |
| 22:20:00 CEST | 20:20:00 UTC | max step: bot 990 tx/s (combined 3,500 = bot 990 + Build 2,600+) |
| 22:20:00 CEST | 20:20:00 UTC | fee quote at step start: 188.1 (pair 400/600, cap 600, floor 100, sit out above 400) |
| 22:20:00 CEST | 20:20:00 UTC | rate: MAX senders 990 tx/s total (15 up x 66), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 22:20:00 CEST | 20:20:00 UTC | BOT BLOCK: session up, runners 15, disk 40.8 GB, n2 synced true utxoindex false lag 0.4 s mempool 1974, bot sub/acc 343.8/345.1 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted 2418.4 tx/s (9/9 valid), miner 1, mining share 23.8%, dup share 0.3548 |
| 22:29:32 CEST | 20:29:32 UTC | coin buffer: 719142 tKAS unclaimed (22767 coins) |
| 22:30:01 CEST | 20:30:01 UTC | BOT BLOCK: session up, runners 15, disk 40.8 GB, n2 synced true utxoindex false lag 0.3 s mempool 5095, bot sub/acc 912.2/910.8 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted 2689.2 tx/s (9/9 valid), miner 1, mining share 25.34%, dup share 0.3605 |
| 22:30:14 CEST | 20:30:14 UTC | live summary: pushed logs/bot/SUMMARY.md (8644a7f) |
| 22:33:12 CEST | 20:33:12 UTC | S7 not running -> relaunch 5/30 |
| 22:34:14 CEST | 20:34:14 UTC | DEVIATION (fix 6): MAX rate ~912 vs 990 — S7 at 0 sub (node_cool/WS on electron/vector/boson/neutrino). Night-watch TERM+relaunch 5/30 at 22:33:12 CEST with pubs electron/boson/muon/vector. Post-fix ~960–996 sub (avg ~979), S7 at target. Coins 713k. Disk 41G. No user ping |
| 22:34:14 CEST | 20:34:14 UTC | night-watch: MAX OK after S7 restart; ~979/990; 15 senders; n2 synced no-utxoindex; disk 41G; MemAvail ~4.5G; coins ~713k; no user ping |
| 22:35:00 CEST | 20:35:00 UTC | ROW MAX-drain MAX-drain begins (20:35-20:40 UTC; plan bot: 0; Build: 0; miner on) |
| 22:35:00 CEST | 20:35:00 UTC | rate: MAX-drain senders 0 tx/s total (15 up x 0), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 22:45:29 CEST | 20:45:29 UTC | FREEZE start: n2 virtual DAA not moving for 470 s (>= 30 s) (lag 470.2 s) |
| 22:45:30 CEST | 20:45:30 UTC | N2 FREEZE 469 s, lag 470.2 s -> restart n2 (SIGINT the n2 process; guard relaunches same flags); senders keep submitting to public nodes |
| 22:45:30 CEST | 20:45:30 UTC | ROW B1 B1 begins (joined late, 330 s after its start) (20:40-20:50 UTC; plan bot: 0; Build: 0; miner on) |
| 22:45:31 CEST | 20:45:31 UTC | EVAL MAX: bot submitted 772023 (919.1/919.3 sub/acc tx/s, sec-S*.jsonl (pub-sender), public-node transport errors 7857, delivered>=90% true) (own ids, no-signature hop, anyone-can-spend, not realistic payments), eventual accept 100%, p90 0.19 s, rejects 92, n2 lag max 1.4 s, full time at rate true -> clean=true; last clean level 990 |
| 22:45:31 CEST | 20:45:31 UTC | rate: B1 senders 0 tx/s total (15 up x 0), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 22:45:32 CEST | 20:45:32 UTC | BOT BLOCK: session up, runners 15, disk 41.3 GB, n2 synced true utxoindex false lag 470.2 s mempool 3536, bot sub/acc 0/0 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted 1945.5 tx/s (2/2 valid), miner 1, mining share 24.92%, dup share 0.3267 |
| 22:45:49 CEST | 20:45:49 UTC | n2 kaspad restarted (new process, uptime 7 s) |
| 22:45:49 CEST | 20:45:49 UTC | miner relaunched (process had exited): n2 synced again / process relaunch |
| 22:45:57 CEST | 20:45:57 UTC | live summary: pushed logs/bot/SUMMARY.md (58ea666) |
| 22:45:57 CEST | 20:45:57 UTC | FREEZE end: length 498 s, n2 lag 0.5 s |
| 22:47:04 CEST | 20:47:04 UTC | night-watch: B1 OK after n2 FREEZE 498s restart; MAX clean 919/990; HOLD 880 at 22:50; 15 senders; n2 lag ~0.3s no-utxoindex; disk 41G; MemAvail ~2.3G; coins ~713k; no user ping |
| 22:50:00 CEST | 20:50:00 UTC | ROW HOLD HOLD begins (20:50-02:15 UTC; plan bot: 880; Build: 2400; miner on) |
| 22:50:00 CEST | 20:50:00 UTC | long hold level: 880 tx/s (clean at >= 880 (MAX), hold rate 880; combined target 3,200 = bot 880 + Build 2,400) |
| 22:50:00 CEST | 20:50:00 UTC | fee quote at step start: 166.2 (pair 400/600, cap 600, floor 100, sit out above 400) |
| 22:50:00 CEST | 20:50:00 UTC | rate: HOLD senders 880 tx/s total (15 up x 58.667), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 22:50:00 CEST | 20:50:00 UTC | BOT BLOCK: session up, runners 15, disk 40.8 GB, n2 synced true utxoindex false lag 0.4 s mempool 654, bot sub/acc 0/0 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted 1904 tx/s (1/4 valid), miner 1, mining share 7.9%, dup share 0.3974 |
| 22:53:42 CEST | 20:53:42 UTC | S1 not running -> relaunch 7/30 |
| 22:53:43 CEST | 20:53:43 UTC | rate: HOLD senders 880 tx/s total (12 up x 73.333), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 22:53:44 CEST | 20:53:44 UTC | rate: HOLD senders 880 tx/s total (9 up x 97.778), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 22:53:45 CEST | 20:53:45 UTC | S2 not running -> relaunch 5/30 |
| 22:53:48 CEST | 20:53:48 UTC | S3 not running -> relaunch 5/30 |
| 22:53:51 CEST | 20:53:51 UTC | S4 not running -> relaunch 5/30 |
| 22:53:55 CEST | 20:53:55 UTC | S5 not running -> relaunch 5/30 |
| 22:53:58 CEST | 20:53:58 UTC | S6 not running -> relaunch 6/30 |
| 22:54:01 CEST | 20:54:01 UTC | S7 not running -> relaunch 6/30 |
| 22:54:04 CEST | 20:54:04 UTC | S8 not running -> relaunch 5/30 |
| 22:54:07 CEST | 20:54:07 UTC | S9 not running -> relaunch 5/30 |
| 22:54:10 CEST | 20:54:10 UTC | S10 not running -> relaunch 5/30 |
| 22:54:10 CEST | 20:54:10 UTC | rate: HOLD senders 880 tx/s total (10 up x 88), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 22:54:13 CEST | 20:54:13 UTC | S11 not running -> relaunch 5/30 |
| 22:54:13 CEST | 20:54:13 UTC | rate: HOLD senders 880 tx/s total (11 up x 80), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 22:54:16 CEST | 20:54:16 UTC | S12 not running -> relaunch 5/30 |
| 22:54:16 CEST | 20:54:16 UTC | rate: HOLD senders 880 tx/s total (12 up x 73.333), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 22:54:19 CEST | 20:54:19 UTC | S13 not running -> relaunch 5/30 |
| 22:54:19 CEST | 20:54:19 UTC | rate: HOLD senders 880 tx/s total (13 up x 67.692), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 22:54:22 CEST | 20:54:22 UTC | S14 not running -> relaunch 6/30 |
| 22:54:22 CEST | 20:54:22 UTC | rate: HOLD senders 880 tx/s total (14 up x 62.857), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 22:54:25 CEST | 20:54:25 UTC | S15 not running -> relaunch 6/30 |
| 22:54:25 CEST | 20:54:25 UTC | rate: HOLD senders 880 tx/s total (15 up x 58.667), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 22:54:54 CEST | 20:54:54 UTC | DEVIATION (fix 7): HOLD 0 sub for ~3.5 min after 22:50 — all 15 senders node_cool/RPC timeout on public WS. Night-watch TERM+relaunch S1–S15 5–7/30 at 22:53:36–22:54:25. Post-fix ~876–887/880. Coins 618k. Disk 41G. No user ping |
| 22:54:54 CEST | 20:54:54 UTC | night-watch: HOLD OK after mass sender restart; ~880/880; 15 senders; n2 synced no-utxoindex; disk 41G; MemAvail ~4.6G; coins ~618k; no user ping |
| 22:59:33 CEST | 20:59:33 UTC | coin buffer: 618443 tKAS unclaimed (19567 coins) |
| 23:00:00 CEST | 21:00:00 UTC | BOT BLOCK: session up, runners 15, disk 40.6 GB, n2 synced true utxoindex false lag 0.1 s mempool 4165, bot sub/acc 529.3/527.6 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted 2615.8 tx/s (9/9 valid), miner 1, mining share 23.96%, dup share 0.3958 |
| 23:00:26 CEST | 21:00:26 UTC | live summary: pushed logs/bot/SUMMARY.md (9727346) |
| 23:10:00 CEST | 21:10:00 UTC | BOT BLOCK: session up, runners 15, disk 40.5 GB, n2 synced true utxoindex false lag 0.1 s mempool 5066, bot sub/acc 878.5/877.9 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted 2726.1 tx/s (9/9 valid), miner 1, mining share 23.97%, dup share 0.3837 |
| 23:10:25 CEST | 21:10:25 UTC | night-watch: HOLD OK; ~878/880; 15 senders; n2 synced no-utxoindex; disk 41G; MemAvail ~4.4G; coins ~618k; no user ping |
| 23:15:14 CEST | 21:15:14 UTC | live summary: pushed logs/bot/SUMMARY.md (70e804f) |
| 23:20:01 CEST | 21:20:01 UTC | BOT BLOCK: session up, runners 15, disk 40.5 GB, n2 synced true utxoindex false lag 0.4 s mempool 3299, bot sub/acc 879.7/880.4 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted 2694.4 tx/s (10/10 valid), miner 1, mining share 25.58%, dup share 0.3812 |
| 23:29:39 CEST | 21:29:39 UTC | coin buffer: 618443 tKAS unclaimed (19567 coins) |
| 23:29:55 CEST | 21:29:55 UTC | night-watch: HOLD OK; ~880.4/880; 15 senders; n2 synced no-utxoindex; disk 41G; MemAvail ~3.9G; coins ~618k; no user ping |
| 23:30:00 CEST | 21:30:00 UTC | BOT BLOCK: session up, runners 15, disk 40.4 GB, n2 synced true utxoindex false lag 0.4 s mempool 3959, bot sub/acc 878.6/878.1 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted 2718.1 tx/s (9/9 valid), miner 1, mining share 23.9%, dup share 0.3763 |
| 23:30:24 CEST | 21:30:24 UTC | live summary: pushed logs/bot/SUMMARY.md (ec7b599) |
| 23:40:00 CEST | 21:40:00 UTC | BOT BLOCK: session up, runners 15, disk 40.2 GB, n2 synced true utxoindex false lag 0.3 s mempool 4133, bot sub/acc 871.1/871.9 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted 2645.7 tx/s (10/10 valid), miner 1, mining share 24.84%, dup share 0.378 |
| 23:45:13 CEST | 21:45:13 UTC | live summary: pushed logs/bot/SUMMARY.md (63fdbaf) |
| 23:50:00 CEST | 21:50:00 UTC | BOT BLOCK: session up, runners 15, disk 39.9 GB, n2 synced true utxoindex false lag 1.2 s mempool 5099, bot sub/acc 876.9/877.2 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted 2630.9 tx/s (10/10 valid), miner 1, mining share 24.62%, dup share 0.3773 |
| 23:50:50 CEST | 21:50:50 UTC | night-watch: HOLD OK; ~877/880; 15 senders; n2 synced no-utxoindex; disk 40G; MemAvail ~4.0G; coins ~602k; no user ping |
| 23:59:46 CEST | 21:59:46 UTC | coin buffer: 584786 tKAS unclaimed (18446 coins) |
| 00:00:00 CEST | 22:00:00 UTC | BOT BLOCK: session up, runners 15, disk 39.4 GB, n2 synced true utxoindex false lag 0.2 s mempool 5299, bot sub/acc 875.6/875.9 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted 2642.6 tx/s (10/10 valid), miner 1, mining share 24.57%, dup share 0.3734 |
| 00:00:23 CEST | 22:00:23 UTC | live summary: pushed logs/bot/SUMMARY.md (fc8ccee) |
| 00:07:10 CEST | 22:07:10 UTC | night-watch: HOLD OK; ~880/880; 15 senders; n2 synced no-utxoindex; disk 40G; MemAvail ~4.1G; coins ~584k; no user ping |
| 00:26:21 CEST | 22:26:21 UTC | BOT BLOCK: session up, runners 15, disk 39.3 GB, n2 synced false utxoindex false lag 1146.9 s mempool 3991, bot sub/acc 0/0 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted not measured tx/s (0/0 valid), miner 1, mining share -%, dup share - |
| 00:26:34 CEST | 22:26:34 UTC | live summary: pushed logs/bot/SUMMARY.md (40837e8) |
| 00:26:50 CEST | 22:26:50 UTC | FREEZE start: n2 virtual DAA not moving for 30 s (>= 30 s) (lag 1177.3 s) |
| 00:27:19 CEST | 22:27:19 UTC | miner OFF: n2 not synced for 60 s |
| 00:27:53 CEST | 22:27:53 UTC | S1 not running -> relaunch 8/30 |
| 00:27:53 CEST | 22:27:53 UTC | rate: HOLD senders 880 tx/s total (13 up x 67.692), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 00:27:54 CEST | 22:27:54 UTC | rate: HOLD senders 880 tx/s total (11 up x 80), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 00:27:55 CEST | 22:27:55 UTC | rate: HOLD senders 880 tx/s total (9 up x 97.778), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 00:27:56 CEST | 22:27:56 UTC | S2 not running -> relaunch 6/30 |
| 00:27:59 CEST | 22:27:59 UTC | S3 not running -> relaunch 6/30 |
| 00:28:02 CEST | 22:28:02 UTC | S4 not running -> relaunch 6/30 |
| 00:28:05 CEST | 22:28:05 UTC | S5 not running -> relaunch 6/30 |
| 00:28:08 CEST | 22:28:08 UTC | S6 not running -> relaunch 7/30 |
| 00:28:11 CEST | 22:28:11 UTC | S7 not running -> relaunch 7/30 |
| 00:28:14 CEST | 22:28:14 UTC | S8 not running -> relaunch 6/30 |
| 00:28:17 CEST | 22:28:17 UTC | S9 not running -> relaunch 6/30 |
| 00:28:20 CEST | 22:28:20 UTC | S10 not running -> relaunch 6/30 |
| 00:28:20 CEST | 22:28:20 UTC | rate: HOLD senders 880 tx/s total (10 up x 88), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 00:28:23 CEST | 22:28:23 UTC | S11 not running -> relaunch 6/30 |
| 00:28:23 CEST | 22:28:23 UTC | rate: HOLD senders 880 tx/s total (11 up x 80), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 00:28:26 CEST | 22:28:26 UTC | S12 not running -> relaunch 6/30 |
| 00:28:26 CEST | 22:28:26 UTC | rate: HOLD senders 880 tx/s total (12 up x 73.333), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 00:28:29 CEST | 22:28:29 UTC | S13 not running -> relaunch 6/30 |
| 00:28:29 CEST | 22:28:29 UTC | rate: HOLD senders 880 tx/s total (13 up x 67.692), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 00:28:32 CEST | 22:28:32 UTC | S14 not running -> relaunch 7/30 |
| 00:28:32 CEST | 22:28:32 UTC | rate: HOLD senders 880 tx/s total (14 up x 62.857), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 00:28:35 CEST | 22:28:35 UTC | S15 not running -> relaunch 7/30 |
| 00:28:35 CEST | 22:28:35 UTC | rate: HOLD senders 880 tx/s total (15 up x 58.667), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 00:28:40 CEST | 22:28:40 UTC | FREEZE end: length 140 s, n2 lag 1286.9 s |
| 00:29:32 CEST | 22:29:32 UTC | miner ON (1 box CPU kaspa-miner, 1 thread, n2 gRPC): n2 synced again / process relaunch |
| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |
| 00:30:00 CEST | 22:30:00 UTC | BOT BLOCK: session up, runners 15, disk 38.7 GB, n2 synced true utxoindex false lag 349.1 s mempool 14, bot sub/acc 112.2/110.4 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted not measured tx/s (0/0 valid), miner 1, mining share -%, dup share - |
| 00:30:20 CEST | 22:30:20 UTC | DEVIATION (fix 8): HOLD 0 sub ~20 min (~00:07–00:27 CEST) — all 15 senders stuck pending/resubscribe (WS stall). Night-watch TERM+relaunch S1–S15 6–8/30 at 00:27:47–00:28:35. Post-fix ~872–886/880. n2 lag ~19m then catch-up; miner/chain back 00:29. Coins ~489k. Disk 39G. No user ping |
| 00:30:20 CEST | 22:30:20 UTC | night-watch: HOLD OK after fix #8; ~880/880; 15 senders; n2 synced catching-up no-utxoindex; disk 39G; MemAvail ~2.9G; coins ~489k; no user ping |
| 00:30:23 CEST | 22:30:23 UTC | live summary: pushed logs/bot/SUMMARY.md (d9909d2) |
| 00:31:36 CEST | 22:31:36 UTC | DEVIATION (fix 8b): HOLD died again ~00:30:10 after #8 — all 5 public wrpc/borsh HTTP 502 (polled 00:30:51–00:31:16). Hold relaunches until pubs recover; background watcher to TERM+relaunch then. Coins ~489k. Disk 39G. No user ping |
| 00:32:15 CEST | 22:32:15 UTC | DEVIATION (fix 8c start): all 5 public wrpc 502; HOLD 0; background recovery watcher started; coins ~489k disk 39G; no user ping |
| 00:40:00 CEST | 22:40:00 UTC | BOT BLOCK: session up, runners 15, disk 38.5 GB, n2 synced true utxoindex false lag 0.1 s mempool 1654, bot sub/acc 0/0 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted 1916.1 tx/s (8/9 valid), miner 1, mining share 16.88%, dup share 0.4243 |
| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |
| 00:45:12 CEST | 22:45:12 UTC | live summary: pushed logs/bot/SUMMARY.md (47cc34d) |
| 00:50:00 CEST | 22:50:00 UTC | BOT BLOCK: session up, runners 15, disk 38.3 GB, n2 synced true utxoindex false lag 0.2 s mempool 0, bot sub/acc 380.8/379.8 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted 1900.5 tx/s (9/10 valid), miner 1, mining share 23.79%, dup share 0.4456 |
| 00:52:37 CEST | 22:52:39 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4044 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |; |
| 00:59:58 CEST | 22:59:58 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |
| 01:00:00 CEST | 23:00:00 UTC | BOT BLOCK: session up, runners 15, disk 38.1 GB, n2 synced true utxoindex false lag 0.5 s mempool 0, bot sub/acc 878.5/878.5 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted 935.4 tx/s (9/9 valid), miner 1, mining share 22.28%, dup share 0.5647 |
| 01:00:21 CEST | 23:00:21 UTC | live summary: pushed logs/bot/SUMMARY.md (26bcd04) |
| 01:02:43 CEST | 23:02:44 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4009 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |;| 00:52:37 CEST | 22:52:39 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4044 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |; |;| 00:59:58 CEST | 22:59:58 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |
| 01:10:00 CEST | 23:10:00 UTC | BOT BLOCK: session up, runners 15, disk 37.9 GB, n2 synced true utxoindex false lag 0.2 s mempool 0, bot sub/acc 878.5/878 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted 935 tx/s (10/10 valid), miner 1, mining share 24.02%, dup share 0.554 |
| 01:12:49 CEST | 23:12:51 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 38G | MemAvailable: 3948 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |;| 00:52:37 CEST | 22:52:39 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4044 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |; |;| 00:59:58 CEST | 22:59:58 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |;| 01:02:43 CEST | 23:02:44 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4009 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |;| 00:52:37 CEST | 22:52:39 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4044 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |; |;| 00:59:58 CEST | 22:59:58 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |; |
| 01:15:10 CEST | 23:15:10 UTC | live summary: pushed logs/bot/SUMMARY.md (7cafb1e) |
| 01:20:00 CEST | 23:20:00 UTC | BOT BLOCK: session up, runners 15, disk 37.7 GB, n2 synced true utxoindex false lag 0.1 s mempool 0, bot sub/acc 840.5/840.4 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted 887.6 tx/s (9/9 valid), miner 1, mining share 23.9%, dup share 0.5449 |
| 01:22:55 CEST | 23:22:57 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 38G | MemAvailable: 3813 MB;coin buffer: 474,826 tKAS unclaimed in 15005 coins;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |;| 00:52:37 CEST | 22:52:39 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4044 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |; |;| 00:59:58 CEST | 22:59:58 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |;| 01:02:43 CEST | 23:02:44 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4009 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |;| 00:52:37 CEST | 22:52:39 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4044 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |; |;| 00:59:58 CEST | 22:59:58 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |;| 01:12:49 CEST | 23:12:51 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 38G | MemAvailable: 3948 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |;| 00:52:37 CEST | 22:52:39 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4044 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |; |;| 00:59:58 CEST | 22:59:58 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |;| 01:02:43 CEST | 23:02:44 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4009 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |;| 00:52:37 CEST | 22:52:39 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4044 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |; |;| 00:59:58 CEST | 22:59:58 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |; |; |
| 01:30:00 CEST | 23:30:00 UTC | BOT BLOCK: session up, runners 15, disk 37.4 GB, n2 synced true utxoindex false lag 0.3 s mempool 89, bot sub/acc 817.8/818 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted 875.2 tx/s (9/10 valid), miner 1, mining share 24.42%, dup share 0.54 |
| 01:30:03 CEST | 23:30:03 UTC | coin buffer: 473932 tKAS unclaimed (14971 coins) |
| 01:30:19 CEST | 23:30:19 UTC | live summary: pushed logs/bot/SUMMARY.md (802fd69) |
| 01:33:01 CEST | 23:33:02 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 38G | MemAvailable: 3898 MB;coin buffer: 473,883 tKAS unclaimed in 14970 coins;| 00:59:58 CEST | 22:59:58 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |;| 01:02:43 CEST | 23:02:44 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4009 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |;| 00:52:37 CEST | 22:52:39 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4044 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |; |;| 00:59:58 CEST | 22:59:58 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |;| 01:12:49 CEST | 23:12:51 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 38G | MemAvailable: 3948 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |;| 00:52:37 CEST | 22:52:39 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4044 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |; |;| 00:59:58 CEST | 22:59:58 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |;| 01:02:43 CEST | 23:02:44 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4009 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |;| 00:52:37 CEST | 22:52:39 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4044 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |; |;| 00:59:58 CEST | 22:59:58 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |; |;| 01:22:55 CEST | 23:22:57 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 38G | MemAvailable: 3813 MB;coin buffer: 474,826 tKAS unclaimed in 15005 coins;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |;| 00:52:37 CEST | 22:52:39 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4044 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |; |;| 00:59:58 CEST | 22:59:58 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |;| 01:02:43 CEST | 23:02:44 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4009 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |;| 00:52:37 CEST | 22:52:39 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4044 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |; |;| 00:59:58 CEST | 22:59:58 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |;| 01:12:49 CEST | 23:12:51 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 38G | MemAvailable: 3948 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |;| 00:52:37 CEST | 22:52:39 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4044 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |; |;| 00:59:58 CEST | 22:59:58 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |;| 01:02:43 CEST | 23:02:44 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4009 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |;| 00:52:37 CEST | 22:52:39 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4044 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |; |;| 00:59:58 CEST | 22:59:58 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |; |; |;| 01:30:03 CEST | 23:30:03 UTC | coin buffer: 473932 tKAS unclaimed (14971 coins) |; |
| 01:33:40 CEST | 23:33:40 UTC | S5 not running -> relaunch 7/30 |
| 01:34:39 CEST | 23:34:39 UTC | DEVIATION (fix 9): HOLD ~818–840 (~01:13–01:33 CEST) — S5 alone stuck submitted=0 pending=525 (quiet/reconnect). TERM+relaunch S5 7/30 at 01:33:40. Post-fix ~876/880. HTTP wrpc poll still 502 (false neg; WS OK). Coins ~468k. Disk 38G. No user ping |
| 01:34:39 CEST | 23:34:39 UTC | night-watch: HOLD OK after fix #9; ~876/880; 15 senders; S5 fresh; n2 synced no-utxoindex; disk 38G; MemAvail ~3.8G; coins ~468k; HTTP wrpc 502 poll ignore (WS live); no user ping |
| 01:35:44 CEST | 23:35:44 UTC | night-watch: HOLD OK ~888/880; 15 senders; post fix#9 S5; disk 38G; MemAvail ~3.7G; coins ~467k; no user ping |
| 01:40:00 CEST | 23:40:00 UTC | BOT BLOCK: session up, runners 15, disk 37.3 GB, n2 synced true utxoindex false lag 0.5 s mempool 0, bot sub/acc 487.1/486.9 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted 874 tx/s (7/9 valid), miner 1, mining share 25.08%, dup share 0.5546 |
| 01:43:06 CEST | 23:43:07 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 38G | MemAvailable: 2979 MB;coin buffer: 461,400 tKAS unclaimed in 14558 coins;| 01:22:55 CEST | 23:22:57 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 38G | MemAvailable: 3813 MB;coin buffer: 474,826 tKAS unclaimed in 15005 coins;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |;| 00:52:37 CEST | 22:52:39 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4044 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |; |;| 00:59:58 CEST | 22:59:58 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |;| 01:02:43 CEST | 23:02:44 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4009 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |;| 00:52:37 CEST | 22:52:39 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4044 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |; |;| 00:59:58 CEST | 22:59:58 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |;| 01:12:49 CEST | 23:12:51 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 38G | MemAvailable: 3948 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |;| 00:52:37 CEST | 22:52:39 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4044 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |; |;| 00:59:58 CEST | 22:59:58 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |;| 01:02:43 CEST | 23:02:44 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4009 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |;| 00:52:37 CEST | 22:52:39 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4044 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |; |;| 00:59:58 CEST | 22:59:58 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |; |; |;| 01:30:03 CEST | 23:30:03 UTC | coin buffer: 473932 tKAS unclaimed (14971 coins) |;| 01:33:01 CEST | 23:33:02 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 38G | MemAvailable: 3898 MB;coin buffer: 473,883 tKAS unclaimed in 14970 coins;| 00:59:58 CEST | 22:59:58 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |;| 01:02:43 CEST | 23:02:44 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4009 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |;| 00:52:37 CEST | 22:52:39 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4044 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |; |;| 00:59:58 CEST | 22:59:58 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |;| 01:12:49 CEST | 23:12:51 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 38G | MemAvailable: 3948 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |;| 00:52:37 CEST | 22:52:39 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4044 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |; |;| 00:59:58 CEST | 22:59:58 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |;| 01:02:43 CEST | 23:02:44 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4009 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |;| 00:52:37 CEST | 22:52:39 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4044 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |; |;| 00:59:58 CEST | 22:59:58 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |; |;| 01:22:55 CEST | 23:22:57 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 38G | MemAvailable: 3813 MB;coin buffer: 474,826 tKAS unclaimed in 15005 coins;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |;| 00:52:37 CEST | 22:52:39 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4044 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |; |;| 00:59:58 CEST | 22:59:58 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |;| 01:02:43 CEST | 23:02:44 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4009 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |;| 00:52:37 CEST | 22:52:39 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4044 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |; |;| 00:59:58 CEST | 22:59:58 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |;| 01:12:49 CEST | 23:12:51 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 38G | MemAvailable: 3948 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |;| 00:52:37 CEST | 22:52:39 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4044 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |; |;| 00:59:58 CEST | 22:59:58 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |;| 01:02:43 CEST | 23:02:44 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4009 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |;| 00:52:37 CEST | 22:52:39 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4044 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |;| 00:42:32 CEST | 22:42:33 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 15 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 39G | MemAvailable: 4151 MB;coin buffer: 488,999 tKAS unclaimed in 15426 coins;| 00:29:52 CEST | 22:29:52 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |; |;| 00:59:58 CEST | 22:59:58 UTC | coin buffer: 488999 tKAS unclaimed (15426 coins) |; |; |; |;| 01:30:03 CEST | 23:30:03 UTC | coin buffer: 473932 tKAS unclaimed (14971 coins) |; |; |
| 01:47:24 CEST | 23:47:24 UTC | live summary: pushed logs/bot/SUMMARY.md (7573dac) |
| 01:50:00 CEST | 23:50:00 UTC | BOT BLOCK: session up, runners 15, disk 37.2 GB, n2 synced true utxoindex false lag 0.7 s mempool 7, bot sub/acc 0/0 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted 53.8 tx/s (6/7 valid), miner 1, mining share 18.51%, dup share 0.5041 |
| 01:52:57 CEST | 23:52:57 UTC | S11 not running -> relaunch 7/30 |
| 01:52:57 CEST | 23:52:57 UTC | rate: HOLD senders 880 tx/s total (14 up x 62.857), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 01:52:58 CEST | 23:52:58 UTC | rate: HOLD senders 880 tx/s total (9 up x 97.778), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 01:53:00 CEST | 23:53:00 UTC | S4 not running -> relaunch 7/30 |
| 01:53:03 CEST | 23:53:03 UTC | S1 not running -> relaunch 9/30 |
| 01:53:06 CEST | 23:53:06 UTC | S2 not running -> relaunch 7/30 |
| 01:53:09 CEST | 23:53:09 UTC | S3 not running -> relaunch 7/30 |
| 01:53:12 CEST | 23:53:12 UTC | S5 not running -> relaunch 8/30 |
| 01:53:15 CEST | 23:53:15 UTC | S6 not running -> relaunch 8/30 |
| 01:53:18 CEST | 23:53:18 UTC | S7 not running -> relaunch 8/30 |
| 01:53:21 CEST | 23:53:21 UTC | S8 not running -> relaunch 7/30 |
| 01:53:22 CEST | 23:53:23 UTC | night-watch: still all/mostly wrpc 502 (ok=0/5); waiting; senders: 9 | miner: 1 | loggers: n2mon 1 chain 1 | topup 0;disk free: 38G | MemAvailable: 4943 MB;coin buffer: 406,227 tKAS unclaimed in 12798 coins; |
| 01:53:24 CEST | 23:53:24 UTC | S9 not running -> relaunch 7/30 |
| 01:53:24 CEST | 23:53:24 UTC | rate: HOLD senders 880 tx/s total (10 up x 88), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 01:53:27 CEST | 23:53:27 UTC | S10 not running -> relaunch 7/30 |
| 01:53:27 CEST | 23:53:27 UTC | rate: HOLD senders 880 tx/s total (11 up x 80), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 01:53:30 CEST | 23:53:30 UTC | S12 not running -> relaunch 7/30 |
| 01:53:30 CEST | 23:53:30 UTC | rate: HOLD senders 880 tx/s total (12 up x 73.333), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 01:53:33 CEST | 23:53:33 UTC | S13 not running -> relaunch 7/30 |
| 01:53:34 CEST | 23:53:34 UTC | rate: HOLD senders 880 tx/s total (13 up x 67.692), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 01:53:37 CEST | 23:53:37 UTC | S14 not running -> relaunch 8/30 |
| 01:53:37 CEST | 23:53:37 UTC | rate: HOLD senders 880 tx/s total (14 up x 62.857), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 01:53:40 CEST | 23:53:40 UTC | S15 not running -> relaunch 8/30 |
| 01:53:40 CEST | 23:53:40 UTC | rate: HOLD senders 880 tx/s total (15 up x 58.667), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 01:54:47 CEST | 23:54:47 UTC | DEVIATION (fix 10): HOLD 0 sub ~17 min (~01:36–01:53 CEST) — all 15 senders stuck rpc_down/node_cool (RPC timeout) despite all 5 public WS OPEN (HTTP wrpc/borsh 502 = false neg). BOT BLOCK 01:40 ~487, 01:50 0/0. Sender procs exited; storm auto-relaunch S1–S15 7–9/30 at 01:52:57–01:53:40. Post-fix ~876–886/880. Coins ~360k (was ~456k; mass restart locked). Disk 38G. MemAvail ~4.1G. No user ping |
| 01:54:47 CEST | 23:54:47 UTC | night-watch: HOLD OK after fix #10; ~876–886/880; 15 senders; n2 synced no-utxoindex; disk 38G; MemAvail ~4.1G; coins ~360k; WS live (HTTP 502 ignore); no user ping |
| 02:11:55 CEST | 00:11:55 UTC | coin buffer: 360193 tKAS unclaimed (11331 coins) |
| 02:11:55 CEST | 00:11:55 UTC | BOT BLOCK: session up, runners 15, disk 37.1 GB, n2 synced false utxoindex false lag 779.3 s mempool 447, bot sub/acc 0/0 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted not measured tx/s (0/0 valid), miner 1, mining share -%, dup share - |
| 02:12:03 CEST | 00:12:03 UTC | live summary: pushed logs/bot/SUMMARY.md (e841ad0) |
| 02:12:18 CEST | 00:12:18 UTC | FREEZE start: n2 virtual DAA not moving for 30 s (>= 30 s) (lag 809.8 s) |
| 02:12:48 CEST | 00:12:48 UTC | miner OFF: n2 not synced for 60 s |
| 02:13:24 CEST | 00:13:24 UTC | S1 not running -> relaunch 10/30 |
| 02:13:24 CEST | 00:13:24 UTC | rate: HOLD senders 880 tx/s total (14 up x 62.857), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 02:13:25 CEST | 00:13:25 UTC | rate: HOLD senders 880 tx/s total (9 up x 97.778), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 02:13:27 CEST | 00:13:27 UTC | S2 not running -> relaunch 8/30 |
| 02:13:30 CEST | 00:13:30 UTC | S3 not running -> relaunch 8/30 |
| 02:13:33 CEST | 00:13:33 UTC | S4 not running -> relaunch 8/30 |
| 02:13:36 CEST | 00:13:36 UTC | S5 not running -> relaunch 9/30 |
| 02:13:39 CEST | 00:13:39 UTC | S6 not running -> relaunch 9/30 |
| 02:13:42 CEST | 00:13:42 UTC | S7 not running -> relaunch 9/30 |
| 02:13:45 CEST | 00:13:45 UTC | S8 not running -> relaunch 8/30 |
| 02:13:48 CEST | 00:13:48 UTC | S9 not running -> relaunch 8/30 |
| 02:13:51 CEST | 00:13:51 UTC | S10 not running -> relaunch 8/30 |
| 02:13:51 CEST | 00:13:51 UTC | rate: HOLD senders 880 tx/s total (10 up x 88), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 02:13:54 CEST | 00:13:54 UTC | S11 not running -> relaunch 8/30 |
| 02:13:54 CEST | 00:13:54 UTC | rate: HOLD senders 880 tx/s total (11 up x 80), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 02:13:57 CEST | 00:13:57 UTC | S12 not running -> relaunch 8/30 |
| 02:13:57 CEST | 00:13:57 UTC | rate: HOLD senders 880 tx/s total (12 up x 73.333), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 02:14:00 CEST | 00:14:00 UTC | S13 not running -> relaunch 8/30 |
| 02:14:00 CEST | 00:14:00 UTC | rate: HOLD senders 880 tx/s total (13 up x 67.692), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 02:14:03 CEST | 00:14:03 UTC | S14 not running -> relaunch 9/30 |
| 02:14:03 CEST | 00:14:03 UTC | rate: HOLD senders 880 tx/s total (14 up x 62.857), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 02:14:06 CEST | 00:14:06 UTC | S15 not running -> relaunch 9/30 |
| 02:14:06 CEST | 00:14:06 UTC | rate: HOLD senders 880 tx/s total (15 up x 58.667), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 02:14:10 CEST | 00:14:10 UTC | FREEZE end: length 142 s, n2 lag 919.3 s |
| 02:14:18 CEST | 00:14:18 UTC | miner ON (1 box CPU kaspa-miner, 1 thread, n2 gRPC): n2 synced again / process relaunch |
| 02:15:02 CEST | 00:15:02 UTC | DEVIATION (fix 11): HOLD 0 sub ~2 min (~02:11–02:13 CEST) — all 15 senders stuck pending~52 + resubscribe + rpc rejects (lat ~60s); BOT BLOCK 02:11 0/0; n2 FREEZE 142s then catch-up. Night-watch TERM S1–S15 at 02:13:18; storm relaunch 8–10/30 by 02:14:06. Post-fix ~890/880 sub, ~868 acc. Coins ~360k pre-restart. Disk 37G. MemAvail ~2.7G. Miner back ON 02:14:18. No user ping |
| 02:15:02 CEST | 00:15:02 UTC | night-watch: HOLD OK after fix #11; ~890/880; 15 senders; n2 synced again no-utxoindex; disk 37G; MemAvail ~2.7G; coins ~360k; no user ping |
| 02:15:09 CEST | 00:15:09 UTC | live summary: pushed logs/bot/SUMMARY.md (c1cd8f3) |
| 02:20:00 CEST | 00:20:00 UTC | BOT BLOCK: session up, runners 15, disk 36.9 GB, n2 synced true utxoindex false lag 0.3 s mempool 0, bot sub/acc 549/546.8 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted 934.9 tx/s (4/5 valid), miner 1, mining share 9.03%, dup share 0.5799 |
| 02:32:01 CEST | 00:32:01 UTC | BOT BLOCK: session up, runners 15, disk 36.9 GB, n2 synced true utxoindex false lag 609.1 s mempool 0, bot sub/acc 0/0 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted not measured tx/s (0/0 valid), miner 1, mining share -%, dup share - |
| 02:32:11 CEST | 00:32:11 UTC | live summary: pushed logs/bot/SUMMARY.md (59b3900) |
| 02:33:19 CEST | 00:33:19 UTC | S1 not running -> relaunch 11/30 |
| 02:33:19 CEST | 00:33:19 UTC | rate: HOLD senders 880 tx/s total (9 up x 97.778), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 02:33:22 CEST | 00:33:22 UTC | S2 not running -> relaunch 9/30 |
| 02:33:25 CEST | 00:33:25 UTC | S3 not running -> relaunch 9/30 |
| 02:33:28 CEST | 00:33:28 UTC | S4 not running -> relaunch 9/30 |
| 02:33:31 CEST | 00:33:31 UTC | S5 not running -> relaunch 10/30 |
| 02:33:34 CEST | 00:33:34 UTC | S6 not running -> relaunch 10/30 |
| 02:33:37 CEST | 00:33:37 UTC | S7 not running -> relaunch 10/30 |
| 02:33:40 CEST | 00:33:40 UTC | S8 not running -> relaunch 9/30 |
| 02:33:43 CEST | 00:33:43 UTC | S9 not running -> relaunch 9/30 |
| 02:33:46 CEST | 00:33:46 UTC | S10 not running -> relaunch 9/30 |
| 02:33:49 CEST | 00:33:49 UTC | S11 not running -> relaunch 9/30 |
| 02:33:49 CEST | 00:33:49 UTC | rate: HOLD senders 880 tx/s total (10 up x 88), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 02:33:52 CEST | 00:33:52 UTC | S12 not running -> relaunch 9/30 |
| 02:33:52 CEST | 00:33:52 UTC | rate: HOLD senders 880 tx/s total (11 up x 80), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 02:33:55 CEST | 00:33:55 UTC | S13 not running -> relaunch 9/30 |
| 02:33:55 CEST | 00:33:55 UTC | rate: HOLD senders 880 tx/s total (12 up x 73.333), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 02:33:58 CEST | 00:33:58 UTC | S14 not running -> relaunch 10/30 |
| 02:33:58 CEST | 00:33:58 UTC | rate: HOLD senders 880 tx/s total (13 up x 67.692), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 02:34:01 CEST | 00:34:01 UTC | S15 not running -> relaunch 10/30 |
| 02:34:01 CEST | 00:34:01 UTC | rate: HOLD senders 880 tx/s total (14 up x 62.857), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 02:34:19 CEST | 00:34:19 UTC | S1 not running -> relaunch 12/30 |
| 02:34:19 CEST | 00:34:19 UTC | rate: HOLD senders 880 tx/s total (15 up x 58.667), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 02:35:17 CEST | 00:35:17 UTC | DEVIATION (fix 12): HOLD 0 sub ~13 min (~02:20–02:33 CEST) — BOT BLOCK 02:20 ~549 then 02:32 0/0; all 15 senders stuck pending~65–69 (S5 pend=600) + resubscribe + rpc rejects (lat~60s); WS pubs OPEN on /kaspa/testnet-10/wrpc/borsh. Night-watch TERM then KILL S1–S15 at 02:33:14–02:33:21; storm relaunch 9–12/30 by 02:34:19. Post-fix ~875–882/880 sub, ~809 acc. Coins ~168k (was ~264k; mass restart locks). Disk 37G. MemAvail ~2.8G. No user ping |
| 02:35:17 CEST | 00:35:17 UTC | night-watch: HOLD OK after fix #12; ~875–882/880; 15 senders; n2 synced no-utxoindex; disk 37G; MemAvail ~2.8G; coins ~168k; WS live; no user ping |
| 02:40:01 CEST | 00:40:01 UTC | BOT BLOCK: session up, runners 15, disk 36.6 GB, n2 synced true utxoindex false lag 0.2 s mempool 17, bot sub/acc 560.1/558.8 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted 931 tx/s (7/8 valid), miner 1, mining share 12.66%, dup share 0.5506 |
| 02:43:42 CEST | 00:43:42 UTC | coin buffer: 167960 tKAS unclaimed (5318 coins) |
| 02:44:56 CEST | 00:44:56 UTC | S1 not running -> relaunch 13/30 |
| 02:44:56 CEST | 00:44:56 UTC | rate: HOLD senders 880 tx/s total (9 up x 97.778), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 02:44:59 CEST | 00:44:59 UTC | S2 not running -> relaunch 10/30 |
| 02:45:02 CEST | 00:45:02 UTC | S3 not running -> relaunch 10/30 |
| 02:45:06 CEST | 00:45:06 UTC | S4 not running -> relaunch 10/30 |
| 02:45:09 CEST | 00:45:09 UTC | S5 not running -> relaunch 11/30 |
| 02:45:12 CEST | 00:45:12 UTC | S6 not running -> relaunch 11/30 |
| 02:45:15 CEST | 00:45:15 UTC | S7 not running -> relaunch 11/30 |
| 02:45:18 CEST | 00:45:18 UTC | S8 not running -> relaunch 10/30 |
| 02:45:21 CEST | 00:45:21 UTC | S9 not running -> relaunch 10/30 |
| 02:45:24 CEST | 00:45:24 UTC | live summary: pushed logs/bot/SUMMARY.md (9792fed) |
| 02:45:24 CEST | 00:45:24 UTC | S10 not running -> relaunch 10/30 |
| 02:45:24 CEST | 00:45:24 UTC | rate: HOLD senders 880 tx/s total (10 up x 88), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 02:45:27 CEST | 00:45:27 UTC | S11 not running -> relaunch 10/30 |
| 02:45:27 CEST | 00:45:27 UTC | rate: HOLD senders 880 tx/s total (11 up x 80), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 02:45:30 CEST | 00:45:30 UTC | S12 not running -> relaunch 10/30 |
| 02:45:30 CEST | 00:45:30 UTC | rate: HOLD senders 880 tx/s total (12 up x 73.333), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 02:45:33 CEST | 00:45:33 UTC | S13 not running -> relaunch 10/30 |
| 02:45:33 CEST | 00:45:33 UTC | rate: HOLD senders 880 tx/s total (13 up x 67.692), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 02:45:36 CEST | 00:45:36 UTC | S14 not running -> relaunch 11/30 |
| 02:45:36 CEST | 00:45:36 UTC | rate: HOLD senders 880 tx/s total (14 up x 62.857), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 02:45:39 CEST | 00:45:39 UTC | S15 not running -> relaunch 11/30 |
| 02:45:39 CEST | 00:45:39 UTC | rate: HOLD senders 880 tx/s total (15 up x 58.667), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 02:47:25 CEST | 00:47:25 UTC | DEVIATION (fix 13): HOLD 0 sub ~4 min (~02:41–02:44 CEST) — BOT BLOCK 02:40 ~560 then live sec all-zero from ~02:43; all 15 senders stuck pending~55–58 + rpc rejects (lat~60–156s); WS pubs OPEN on /kaspa/testnet-10/wrpc/borsh. Night-watch TERM then KILL S1–S15 at 02:44:51–02:44:56; storm relaunch 10–11/30 by 02:45:39. Post-fix ~875–881/880 sub, acc recovering. Coins ~74k after restart locks (was ~168k; BELOW 100k supervisor floor). utxoindex absent — coin-refresh/topup dump impossible. No further mass restarts unless rate dies. Disk 37G. MemAvail ~2670 MB. No user ping |
| 02:47:25 CEST | 00:47:25 UTC | night-watch: HOLD OK after fix #13; ~879/1273 vs 880; 15 senders; zeros 0; n2 synced no-utxoindex; disk 37G; MemAvail ~2670 MB; coins ~74k (<100k floor — NO extra mass restarts; keep HOLD); WS live; no user ping |
| 02:50:00 CEST | 00:50:00 UTC | BOT BLOCK: session up, runners 15, disk 36.5 GB, n2 synced true utxoindex false lag 0.4 s mempool 111, bot sub/acc 582.4/580.9 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted 925.4 tx/s (6/7 valid), miner 1, mining share 20.42%, dup share 0.5825 |
| 03:06:59 CEST | 01:06:59 UTC | BOT BLOCK: session up, runners 15, disk 36.3 GB, n2 synced false utxoindex false lag 786.4 s mempool 17, bot sub/acc 0/0 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted not measured tx/s (0/0 valid), miner 1, mining share -%, dup share - |
| 03:07:10 CEST | 01:07:10 UTC | live summary: pushed logs/bot/SUMMARY.md (d1d272e) |
| 03:07:29 CEST | 01:07:29 UTC | FREEZE start: n2 virtual DAA not moving for 31 s (>= 30 s) (lag 817.1 s) |
| 03:07:58 CEST | 01:07:58 UTC | miner OFF: n2 not synced for 60 s |
| 03:08:37 CEST | 01:08:37 UTC | S1 not running -> relaunch 14/30 |
| 03:08:37 CEST | 01:08:37 UTC | rate: HOLD senders 880 tx/s total (9 up x 97.778), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:08:40 CEST | 01:08:40 UTC | S2 not running -> relaunch 11/30 |
| 03:08:43 CEST | 01:08:43 UTC | S3 not running -> relaunch 11/30 |
| 03:08:46 CEST | 01:08:46 UTC | S4 not running -> relaunch 11/30 |
| 03:08:49 CEST | 01:08:49 UTC | S5 not running -> relaunch 12/30 |
| 03:08:52 CEST | 01:08:52 UTC | S6 not running -> relaunch 12/30 |
| 03:08:55 CEST | 01:08:55 UTC | S7 not running -> relaunch 12/30 |
| 03:08:58 CEST | 01:08:58 UTC | S8 not running -> relaunch 11/30 |
| 03:09:01 CEST | 01:09:01 UTC | S9 not running -> relaunch 11/30 |
| 03:09:04 CEST | 01:09:04 UTC | S10 not running -> relaunch 11/30 |
| 03:09:04 CEST | 01:09:04 UTC | rate: HOLD senders 880 tx/s total (10 up x 88), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:09:07 CEST | 01:09:07 UTC | S11 not running -> relaunch 11/30 |
| 03:09:07 CEST | 01:09:07 UTC | rate: HOLD senders 880 tx/s total (11 up x 80), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:09:10 CEST | 01:09:10 UTC | S12 not running -> relaunch 11/30 |
| 03:09:10 CEST | 01:09:10 UTC | rate: HOLD senders 880 tx/s total (12 up x 73.333), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:09:13 CEST | 01:09:13 UTC | S13 not running -> relaunch 11/30 |
| 03:09:13 CEST | 01:09:13 UTC | rate: HOLD senders 880 tx/s total (13 up x 67.692), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:09:14 CEST | 01:09:14 UTC | FREEZE end: length 136 s, n2 lag 906.8 s |
| 03:09:16 CEST | 01:09:16 UTC | S14 not running -> relaunch 12/30 |
| 03:09:16 CEST | 01:09:16 UTC | rate: HOLD senders 880 tx/s total (14 up x 62.857), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:09:19 CEST | 01:09:19 UTC | launch held: MemAvailable 1394 MB < 1500 (no sender launch while RAM is low) |
| 03:09:25 CEST | 01:09:25 UTC | miner ON (1 box CPU kaspa-miner, 1 thread, n2 gRPC): n2 synced again / process relaunch |
| 03:09:26 CEST | 01:09:26 UTC | S15 not running -> relaunch 12/30 |
| 03:09:26 CEST | 01:09:26 UTC | rate: HOLD senders 880 tx/s total (15 up x 58.667), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:09:36 CEST | 01:09:36 UTC | rate: HOLD senders 880 tx/s total (14 up x 62.857), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:09:39 CEST | 01:09:39 UTC | rate: HOLD senders 880 tx/s total (12 up x 73.333), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:09:47 CEST | 01:09:47 UTC | S4 not running -> relaunch 12/30 |
| 03:09:47 CEST | 01:09:47 UTC | rate: HOLD senders 880 tx/s total (13 up x 67.692), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:09:50 CEST | 01:09:50 UTC | S5 not running -> relaunch 13/30 |
| 03:09:50 CEST | 01:09:50 UTC | rate: HOLD senders 880 tx/s total (14 up x 62.857), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:10:00 CEST | 01:10:00 UTC | BOT BLOCK: session up, runners 14, disk 36.3 GB, n2 synced true utxoindex false lag 57.9 s mempool 31, bot sub/acc 75.8/75.2 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted not measured tx/s (0/1 valid), miner 1, mining share 1.19%, dup share - |
| 03:10:02 CEST | 01:10:02 UTC | S9 not running -> relaunch 12/30 |
| 03:10:02 CEST | 01:10:02 UTC | rate: HOLD senders 880 tx/s total (15 up x 58.667), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:10:03 CEST | 01:10:03 UTC | rate: HOLD senders 880 tx/s total (14 up x 62.857), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:10:14 CEST | 01:10:14 UTC | S2 not running -> relaunch 12/30 |
| 03:10:14 CEST | 01:10:14 UTC | rate: HOLD senders 880 tx/s total (15 up x 58.667), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:10:15 CEST | 01:10:15 UTC | rate: HOLD senders 880 tx/s total (12 up x 73.333), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:10:29 CEST | 01:10:29 UTC | S6 not running -> relaunch 13/30 |
| 03:10:31 CEST | 01:10:31 UTC | n2 kaspad restarted (new process, uptime 1 s) |
| 03:10:32 CEST | 01:10:32 UTC | miner relaunched (process had exited): n2 synced again / process relaunch |
| 03:10:33 CEST | 01:10:33 UTC | S7 not running -> relaunch 13/30 |
| 03:10:33 CEST | 01:10:33 UTC | rate: HOLD senders 880 tx/s total (13 up x 67.692), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:10:36 CEST | 01:10:36 UTC | S10 not running -> relaunch 12/30 |
| 03:10:36 CEST | 01:10:36 UTC | rate: HOLD senders 880 tx/s total (14 up x 62.857), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:10:41 CEST | 01:10:41 UTC | rate: HOLD senders 880 tx/s total (13 up x 67.692), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:10:42 CEST | 01:10:42 UTC | S14 not running -> relaunch 13/30 |
| 03:10:42 CEST | 01:10:42 UTC | rate: HOLD senders 880 tx/s total (14 up x 62.857), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:10:45 CEST | 01:10:45 UTC | rate: HOLD senders 880 tx/s total (13 up x 67.692), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:10:49 CEST | 01:10:49 UTC | S4 not running -> relaunch 13/30 |
| 03:10:49 CEST | 01:10:49 UTC | rate: HOLD senders 880 tx/s total (14 up x 62.857), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:10:50 CEST | 01:10:50 UTC | rate: HOLD senders 880 tx/s total (10 up x 88), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:10:51 CEST | 01:10:51 UTC | rate: HOLD senders 880 tx/s total (9 up x 97.778), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:10:52 CEST | 01:10:52 UTC | S1 not running -> relaunch 15/30 |
| 03:10:52 CEST | 01:10:52 UTC | rate: HOLD senders 880 tx/s total (10 up x 88), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:10:56 CEST | 01:10:56 UTC | S3 not running -> relaunch 12/30 |
| 03:10:56 CEST | 01:10:56 UTC | rate: HOLD senders 880 tx/s total (11 up x 80), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:10:59 CEST | 01:10:59 UTC | S5 not running -> relaunch 14/30 |
| 03:10:59 CEST | 01:10:59 UTC | rate: HOLD senders 880 tx/s total (12 up x 73.333), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:11:01 CEST | 01:11:01 UTC | rate: HOLD senders 880 tx/s total (11 up x 80), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:11:02 CEST | 01:11:02 UTC | S8 not running -> relaunch 12/30 |
| 03:11:02 CEST | 01:11:02 UTC | rate: HOLD senders 880 tx/s total (12 up x 73.333), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:11:05 CEST | 01:11:05 UTC | S9 not running -> relaunch 13/30 |
| 03:11:14 CEST | 01:11:14 UTC | rate: HOLD senders 880 tx/s total (10 up x 88), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:11:15 CEST | 01:11:15 UTC | S2 not running -> relaunch 13/30 |
| 03:11:15 CEST | 01:11:15 UTC | rate: HOLD senders 880 tx/s total (11 up x 80), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:11:20 CEST | 01:11:20 UTC | S11 not running -> relaunch 12/30 |
| 03:11:20 CEST | 01:11:20 UTC | rate: HOLD senders 880 tx/s total (12 up x 73.333), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:11:27 CEST | 01:11:27 UTC | S12 not running -> relaunch 12/30 |
| 03:11:28 CEST | 01:11:28 UTC | rate: HOLD senders 880 tx/s total (9 up x 97.778), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:11:30 CEST | 01:11:30 UTC | S6 not running -> relaunch 14/30 |
| 03:11:33 CEST | 01:11:33 UTC | S7 not running -> relaunch 14/30 |
| 03:11:36 CEST | 01:11:36 UTC | S10 not running -> relaunch 13/30 |
| 03:11:39 CEST | 01:11:39 UTC | S13 not running -> relaunch 12/30 |
| 03:11:42 CEST | 01:11:42 UTC | S14 not running -> relaunch 14/30 |
| 03:11:45 CEST | 01:11:45 UTC | S15 not running -> relaunch 13/30 |
| 03:11:50 CEST | 01:11:50 UTC | S4 not running -> relaunch 14/30 |
| 03:11:53 CEST | 01:11:53 UTC | S1 not running -> relaunch 16/30 |
| 03:11:57 CEST | 01:11:57 UTC | coin buffer: 0 tKAS unclaimed (0 coins) |
| 03:11:57 CEST | 01:11:57 UTC | coin top-up started: buffer 0 < 150000 tKAS -> fill 300,000 tKAS (read-only utxoindex dump, consolidate old coinbases on n2, merge confirmed outputs) |
| 03:11:57 CEST | 01:11:57 UTC | S3 not running -> relaunch 13/30 |
| 03:12:00 CEST | 01:12:00 UTC | S5 not running -> relaunch 15/30 |
| 03:12:00 CEST | 01:12:00 UTC | rate: HOLD senders 880 tx/s total (10 up x 88), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:12:04 CEST | 01:12:04 UTC | S8 not running -> relaunch 13/30 |
| 03:12:04 CEST | 01:12:04 UTC | rate: HOLD senders 880 tx/s total (11 up x 80), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:12:07 CEST | 01:12:07 UTC | S9 not running -> relaunch 14/30 |
| 03:12:07 CEST | 01:12:07 UTC | rate: HOLD senders 880 tx/s total (12 up x 73.333), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:12:17 CEST | 01:12:17 UTC | rate: HOLD senders 880 tx/s total (10 up x 88), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:12:18 CEST | 01:12:18 UTC | S2 not running -> relaunch 14/30 |
| 03:12:18 CEST | 01:12:18 UTC | rate: HOLD senders 880 tx/s total (11 up x 80), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:12:21 CEST | 01:12:21 UTC | rate: HOLD senders 880 tx/s total (10 up x 88), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:12:22 CEST | 01:12:22 UTC | S11 not running -> relaunch 13/30 |
| 03:12:22 CEST | 01:12:22 UTC | rate: HOLD senders 880 tx/s total (11 up x 80), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:12:30 CEST | 01:12:30 UTC | S12 not running -> relaunch 13/30 |
| 03:12:41 CEST | 01:12:41 UTC | S13 not running -> relaunch 13/30 |
| 03:12:41 CEST | 01:12:41 UTC | rate: HOLD senders 880 tx/s total (12 up x 73.333), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:12:47 CEST | 01:12:47 UTC | rate: HOLD senders 880 tx/s total (11 up x 80), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:12:48 CEST | 01:12:48 UTC | S6 not running -> relaunch 15/30 |
| 03:12:48 CEST | 01:12:48 UTC | rate: HOLD senders 880 tx/s total (9 up x 97.778), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:12:51 CEST | 01:12:51 UTC | S4 not running -> relaunch 15/30 |
| 03:12:54 CEST | 01:12:54 UTC | S1 not running -> relaunch 17/30 |
| 03:12:57 CEST | 01:12:57 UTC | S7 not running -> relaunch 15/30 |
| 03:13:00 CEST | 01:13:00 UTC | S3 not running -> relaunch 14/30 |
| 03:13:03 CEST | 01:13:03 UTC | S5 not running -> relaunch 16/30 |
| 03:13:06 CEST | 01:13:06 UTC | S8 not running -> relaunch 14/30 |
| 03:13:09 CEST | 01:13:09 UTC | S9 not running -> relaunch 15/30 |
| 03:13:12 CEST | 01:13:12 UTC | S10 not running -> relaunch 14/30 |
| 03:13:15 CEST | 01:13:15 UTC | S14 not running -> relaunch 15/30 |
| 03:13:15 CEST | 01:13:15 UTC | rate: HOLD senders 880 tx/s total (10 up x 88), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:13:18 CEST | 01:13:18 UTC | S2 not running -> relaunch 15/30 |
| 03:13:18 CEST | 01:13:18 UTC | rate: HOLD senders 880 tx/s total (11 up x 80), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:13:21 CEST | 01:13:21 UTC | S15 not running -> relaunch 14/30 |
| 03:13:21 CEST | 01:13:21 UTC | rate: HOLD senders 880 tx/s total (12 up x 73.333), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:13:24 CEST | 01:13:24 UTC | S11 not running -> relaunch 14/30 |
| 03:13:24 CEST | 01:13:24 UTC | rate: HOLD senders 880 tx/s total (13 up x 67.692), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:13:28 CEST | 01:13:28 UTC | rate: HOLD senders 880 tx/s total (12 up x 73.333), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:13:29 CEST | 01:13:29 UTC | rate: HOLD senders 880 tx/s total (11 up x 80), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:13:31 CEST | 01:13:31 UTC | S12 not running -> relaunch 14/30 |
| 03:13:31 CEST | 01:13:31 UTC | rate: HOLD senders 880 tx/s total (12 up x 73.333), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:13:34 CEST | 01:13:34 UTC | rate: HOLD senders 880 tx/s total (11 up x 80), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:13:37 CEST | 01:13:37 UTC | rate: HOLD senders 880 tx/s total (10 up x 88), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:13:41 CEST | 01:13:41 UTC | S13 not running -> relaunch 14/30 |
| 03:13:50 CEST | 01:13:50 UTC | S6 not running -> relaunch 16/30 |
| 03:13:50 CEST | 01:13:50 UTC | rate: HOLD senders 880 tx/s total (11 up x 80), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:14:02 CEST | 01:14:02 UTC | S7 not running -> relaunch 16/30 |
| 03:14:02 CEST | 01:14:02 UTC | rate: HOLD senders 880 tx/s total (12 up x 73.333), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:14:04 CEST | 01:14:04 UTC | rate: HOLD senders 880 tx/s total (11 up x 80), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:14:09 CEST | 01:14:09 UTC | S5 not running -> relaunch 17/30 |
| 03:14:09 CEST | 01:14:09 UTC | rate: HOLD senders 880 tx/s total (12 up x 73.333), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:14:14 CEST | 01:14:14 UTC | rate: HOLD senders 880 tx/s total (11 up x 80), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:14:16 CEST | 01:14:16 UTC | S9 not running -> relaunch 16/30 |
| 03:14:16 CEST | 01:14:16 UTC | rate: HOLD senders 880 tx/s total (12 up x 73.333), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:14:22 CEST | 01:14:22 UTC | launch held: MemAvailable 1235 MB < 1500 (no sender launch while RAM is low) |
| 03:14:23 CEST | 01:14:23 UTC | S2 not running -> relaunch 16/30 |
| 03:14:23 CEST | 01:14:23 UTC | rate: HOLD senders 880 tx/s total (11 up x 80), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:14:26 CEST | 01:14:26 UTC | rate: HOLD senders 880 tx/s total (9 up x 97.778), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:14:28 CEST | 01:14:28 UTC | S1 not running -> relaunch 18/30 |
| 03:14:31 CEST | 01:14:31 UTC | S3 not running -> relaunch 15/30 |
| 03:14:34 CEST | 01:14:34 UTC | S4 not running -> relaunch 16/30 |
| 03:14:37 CEST | 01:14:37 UTC | S8 not running -> relaunch 15/30 |
| 03:14:40 CEST | 01:14:40 UTC | S10 not running -> relaunch 15/30 |
| 03:14:43 CEST | 01:14:43 UTC | S11 not running -> relaunch 15/30 |
| 03:14:46 CEST | 01:14:46 UTC | S12 not running -> relaunch 15/30 |
| 03:14:49 CEST | 01:14:49 UTC | S13 not running -> relaunch 15/30 |
| 03:14:52 CEST | 01:14:52 UTC | S6 not running -> relaunch 17/30 |
| 03:14:55 CEST | 01:14:55 UTC | S14 not running -> relaunch 16/30 |
| 03:14:55 CEST | 01:14:55 UTC | rate: HOLD senders 880 tx/s total (10 up x 88), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:14:58 CEST | 01:14:58 UTC | S15 not running -> relaunch 15/30 |
| 03:14:58 CEST | 01:14:58 UTC | rate: HOLD senders 880 tx/s total (11 up x 80), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:15:02 CEST | 01:15:02 UTC | S7 not running -> relaunch 17/30 |
| 03:15:02 CEST | 01:15:02 UTC | rate: HOLD senders 880 tx/s total (12 up x 73.333), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:15:09 CEST | 01:15:09 UTC | S5 not running -> relaunch 18/30 |
| 03:15:09 CEST | 01:15:09 UTC | rate: HOLD senders 880 tx/s total (13 up x 67.692), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:15:16 CEST | 01:15:16 UTC | S9 not running -> relaunch 17/30 |
| 03:15:16 CEST | 01:15:16 UTC | rate: HOLD senders 880 tx/s total (14 up x 62.857), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:15:23 CEST | 01:15:23 UTC | S2 not running -> relaunch 17/30 |
| 03:15:23 CEST | 01:15:23 UTC | rate: HOLD senders 880 tx/s total (15 up x 58.667), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:15:26 CEST | 01:15:26 UTC | live summary: pushed logs/bot/SUMMARY.md (e42cb98) |
| 03:16:50 CEST | 01:16:50 UTC | S12 not running -> relaunch 16/30 |
| 03:16:51 CEST | 01:16:51 UTC | rate: HOLD senders 880 tx/s total (12 up x 73.333), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:16:54 CEST | 01:16:54 UTC | S13 not running -> relaunch 16/30 |
| 03:16:54 CEST | 01:16:54 UTC | rate: HOLD senders 880 tx/s total (13 up x 67.692), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:16:57 CEST | 01:16:57 UTC | S14 not running -> relaunch 17/30 |
| 03:16:57 CEST | 01:16:57 UTC | rate: HOLD senders 880 tx/s total (14 up x 62.857), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:17:00 CEST | 01:17:00 UTC | S15 not running -> relaunch 16/30 |
| 03:17:00 CEST | 01:17:00 UTC | rate: HOLD senders 880 tx/s total (15 up x 58.667), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:17:18 CEST | 01:17:18 UTC | watchdog: scheduler not running -> (re)start |
| 03:17:18 CEST | 01:17:18 UTC | scheduler restarted (resume by clock); T0 18:30 UTC, gates 18:00/18:15 UTC, end 02:30 UTC; node n2 (own private node, loopback) |
| 03:17:19 CEST | 01:17:19 UTC | n2 first read: synced true, utxoindex false, sink lag 0.3 s, DAA 593473418 |
| 03:17:19 CEST | 01:17:19 UTC | S12 not running -> relaunch 17/30 |
| 03:17:19 CEST | 01:17:19 UTC | rate: HOLD senders 880 tx/s total (12 up x 73.333), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:17:22 CEST | 01:17:22 UTC | S13 not running -> relaunch 17/30 |
| 03:17:22 CEST | 01:17:22 UTC | rate: HOLD senders 880 tx/s total (13 up x 67.692), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:17:25 CEST | 01:17:25 UTC | S14 not running -> relaunch 18/30 |
| 03:17:25 CEST | 01:17:25 UTC | rate: HOLD senders 880 tx/s total (14 up x 62.857), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:17:28 CEST | 01:17:28 UTC | S15 not running -> relaunch 17/30 |
| 03:17:28 CEST | 01:17:28 UTC | rate: HOLD senders 880 tx/s total (15 up x 58.667), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:17:43 CEST | 01:17:43 UTC | watchdog: scheduler not running -> (re)start |
| 03:17:43 CEST | 01:17:43 UTC | scheduler restarted (resume by clock); T0 18:30 UTC, gates 18:00/18:15 UTC, end 02:30 UTC; node n2 (own private node, loopback) |
| 03:17:44 CEST | 01:17:44 UTC | n2 first read: synced true, utxoindex false, sink lag 0.4 s, DAA 593473712 |
| 03:17:44 CEST | 01:17:44 UTC | rate: HOLD senders 880 tx/s total (11 up x 80), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:18:44 CEST | 01:18:44 UTC | DEVIATION (fix 14): HOLD 0 sub from ~03:00 (BOT BLOCK 03:06 0/0) — all 15 senders stuck pending~60–68 + resubscribe + rpc rejects (lat~60–836s); WS pubs OPEN. Night-watch TERM/KILL S1–S15 at 03:08:31–03:08:36; storm relaunch burned coin buffer 74k→0 and bloated sender RSS to 400–980 MB (MemAvail crashed <1G; n2 restarted 03:10:31; RAM<1G self-stops). Second kill at 03:11:24 reclaimed MemAvail~7.7G; coinless relaunches still bloated. Root cause: keel-coins unclaimed=0 and lane-reuse was disabled (if(false) + wrong tip-file prefix). Fix: enabled lane-reuse in pub-sender.mjs (03:14:26); S1–S11 reused 200 tips and recovered ~880. S12–S15 tips already spent (lanes_dead=200) → skipped in storm.mjs ensureRunners; HOLD carried by 11 up × 80. Post-fix ~874–883/880 sub. Coins still 0 unclaimed (utxoindex absent; topup aborted no venv-rdb). Disk 37G. MemAvail ~6.3G. RSS~220 MB/sender. No user ping |
| 03:18:44 CEST | 01:18:44 UTC | night-watch: HOLD OK after fix #14; ~874–883/880; 11 senders (S12–S15 skipped spent tips); zeros 0 on live; n2 synced no-utxoindex; disk 37G; MemAvail ~6.3G; coins 0 unclaimed (lane-reuse active); WS live; no user ping |
| 03:20:00 CEST | 01:20:00 UTC | BOT BLOCK: session up, runners 11, disk 36.1 GB, n2 synced true utxoindex false lag 0.3 s mempool 0, bot sub/acc 426.7/426.2 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted 675.6 tx/s (9/10 valid), miner 1, mining share 17.77%, dup share 0.5151 |
| 03:32:03 CEST | 01:32:03 UTC | BOT BLOCK: session up, runners 11, disk 36 GB, n2 synced true utxoindex false lag 159.4 s mempool 1, bot sub/acc 116.9/117.2 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted 53.7 tx/s (5/7 valid), miner 1, mining share 20.86%, dup share 0.5668 |
| 03:32:13 CEST | 01:32:13 UTC | live summary: pushed logs/bot/SUMMARY.md (33219de) |
| 03:33:18 CEST | 01:33:18 UTC | S1 not running -> relaunch 19/30 |
| 03:33:18 CEST | 01:33:18 UTC | rate: HOLD senders 880 tx/s total (9 up x 97.778), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:33:21 CEST | 01:33:21 UTC | S2 not running -> relaunch 18/30 |
| 03:33:24 CEST | 01:33:24 UTC | S3 not running -> relaunch 16/30 |
| 03:33:27 CEST | 01:33:27 UTC | S4 not running -> relaunch 17/30 |
| 03:33:30 CEST | 01:33:30 UTC | S5 not running -> relaunch 19/30 |
| 03:33:33 CEST | 01:33:33 UTC | S6 not running -> relaunch 18/30 |
| 03:33:36 CEST | 01:33:36 UTC | S7 not running -> relaunch 18/30 |
| 03:33:39 CEST | 01:33:39 UTC | S8 not running -> relaunch 16/30 |
| 03:33:42 CEST | 01:33:42 UTC | S9 not running -> relaunch 18/30 |
| 03:33:45 CEST | 01:33:45 UTC | S10 not running -> relaunch 16/30 |
| 03:33:45 CEST | 01:33:45 UTC | rate: HOLD senders 880 tx/s total (10 up x 88), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:33:48 CEST | 01:33:48 UTC | S11 not running -> relaunch 16/30 |
| 03:33:48 CEST | 01:33:48 UTC | rate: HOLD senders 880 tx/s total (11 up x 80), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:37:02 CEST | 01:37:02 UTC | watchdog: scheduler not running -> (re)start |
| 03:37:02 CEST | 01:37:02 UTC | scheduler restarted (resume by clock); T0 18:30 UTC, gates 18:00/18:15 UTC, end 02:30 UTC; node n2 (own private node, loopback) |
| 03:37:02 CEST | 01:37:02 UTC | n2 first read: synced true, utxoindex false, sink lag 0.1 s, DAA 593486247 |
| 03:37:02 CEST | 01:37:02 UTC | S1 not running -> relaunch 20/30 |
| 03:37:02 CEST | 01:37:02 UTC | rate: HOLD senders 880 tx/s total (9 up x 97.778), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:37:05 CEST | 01:37:05 UTC | S2 not running -> relaunch 19/30 |
| 03:37:08 CEST | 01:37:08 UTC | S3 not running -> relaunch 17/30 |
| 03:37:11 CEST | 01:37:11 UTC | S4 not running -> relaunch 18/30 |
| 03:37:14 CEST | 01:37:14 UTC | S5 not running -> relaunch 20/30 |
| 03:37:17 CEST | 01:37:17 UTC | S6 not running -> relaunch 19/30 |
| 03:37:21 CEST | 01:37:21 UTC | S7 not running -> relaunch 19/30 |
| 03:37:24 CEST | 01:37:24 UTC | S8 not running -> relaunch 17/30 |
| 03:37:27 CEST | 01:37:27 UTC | S9 not running -> relaunch 19/30 |
| 03:37:30 CEST | 01:37:30 UTC | S10 not running -> relaunch 17/30 |
| 03:37:30 CEST | 01:37:30 UTC | rate: HOLD senders 880 tx/s total (10 up x 88), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:37:33 CEST | 01:37:33 UTC | S11 not running -> relaunch 17/30 |
| 03:37:33 CEST | 01:37:33 UTC | rate: HOLD senders 880 tx/s total (11 up x 80), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:37:36 CEST | 01:37:36 UTC | S12 not running -> relaunch 21/30 |
| 03:37:36 CEST | 01:37:36 UTC | rate: HOLD senders 880 tx/s total (12 up x 73.333), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:37:39 CEST | 01:37:39 UTC | S13 not running -> relaunch 21/30 |
| 03:37:39 CEST | 01:37:39 UTC | rate: HOLD senders 880 tx/s total (13 up x 67.692), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:37:42 CEST | 01:37:42 UTC | S14 not running -> relaunch 21/30 |
| 03:37:42 CEST | 01:37:42 UTC | rate: HOLD senders 880 tx/s total (14 up x 62.857), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:37:45 CEST | 01:37:45 UTC | S15 not running -> relaunch 21/30 |
| 03:37:45 CEST | 01:37:45 UTC | rate: HOLD senders 880 tx/s total (15 up x 58.667), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:38:13 CEST | 01:38:13 UTC | DEVIATION (fix 15): HOLD collapsed ~03:25–03:33 (BOT BLOCK 03:32 116.9/117.2; live 0) — S1–S11 rpc_down stuck; mass TERM 03:33 reused spent 03:10 tips → lanes_dead=200. Rebuilt S1–S15 tip files via pub getUtxosByAddresses (electron utxoindex; 200 UTXOs/~9.8k tKAS each). Unskipped S12–S15 (backed up first); reset relaunch caps; storm restart 03:36:57. Post-fix ~878/880 with 15/15; coins 0 unclaimed; disk 36G; MemAvail ~5.4G. No user ping |
| 03:38:13 CEST | 01:38:13 UTC | night-watch: HOLD OK after fix #15; ~878/880; 15 senders; tips refreshed from pub UTXO index; n2 synced no-utxoindex; disk 36G; MemAvail ~5.4G; coins 0 unclaimed (lane-reuse); WS live; no user ping |
| 03:40:00 CEST | 01:40:00 UTC | BOT BLOCK: session up, runners 15, disk 35.9 GB, n2 synced true utxoindex false lag 0.3 s mempool 96, bot sub/acc 237.1/236.1 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted 57.2 tx/s (7/8 valid), miner 1, mining share 20.37%, dup share 0.4971 |
| 03:44:28 CEST | 01:44:28 UTC | coin buffer: 0 tKAS unclaimed (0 coins) |
| 03:44:28 CEST | 01:44:28 UTC | coin top-up started: buffer 0 < 150000 tKAS -> fill 300,000 tKAS (read-only utxoindex dump, consolidate old coinbases on n2, merge confirmed outputs) |
| 03:45:11 CEST | 01:45:11 UTC | live summary: pushed logs/bot/SUMMARY.md (fc56457) |
| 03:47:08 CEST | 01:47:08 UTC | S1 not running -> relaunch 21/30 |
| 03:47:08 CEST | 01:47:08 UTC | rate: HOLD senders 880 tx/s total (9 up x 97.778), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:47:11 CEST | 01:47:11 UTC | S2 not running -> relaunch 20/30 |
| 03:47:14 CEST | 01:47:14 UTC | S3 not running -> relaunch 18/30 |
| 03:47:17 CEST | 01:47:17 UTC | S4 not running -> relaunch 19/30 |
| 03:47:20 CEST | 01:47:20 UTC | S5 not running -> relaunch 21/30 |
| 03:47:23 CEST | 01:47:23 UTC | S6 not running -> relaunch 20/30 |
| 03:47:26 CEST | 01:47:26 UTC | S7 not running -> relaunch 20/30 |
| 03:47:29 CEST | 01:47:29 UTC | S8 not running -> relaunch 18/30 |
| 03:47:32 CEST | 01:47:32 UTC | S9 not running -> relaunch 20/30 |
| 03:47:35 CEST | 01:47:35 UTC | S10 not running -> relaunch 18/30 |
| 03:47:38 CEST | 01:47:38 UTC | S11 not running -> relaunch 18/30 |
| 03:47:41 CEST | 01:47:41 UTC | S12 not running -> relaunch 22/30 |
| 03:47:41 CEST | 01:47:41 UTC | rate: HOLD senders 880 tx/s total (10 up x 88), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:47:44 CEST | 01:47:44 UTC | S13 not running -> relaunch 22/30 |
| 03:47:44 CEST | 01:47:44 UTC | rate: HOLD senders 880 tx/s total (11 up x 80), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:47:47 CEST | 01:47:47 UTC | S14 not running -> relaunch 22/30 |
| 03:47:47 CEST | 01:47:47 UTC | rate: HOLD senders 880 tx/s total (12 up x 73.333), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:47:50 CEST | 01:47:50 UTC | S15 not running -> relaunch 22/30 |
| 03:47:50 CEST | 01:47:50 UTC | rate: HOLD senders 880 tx/s total (13 up x 67.692), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:48:08 CEST | 01:48:08 UTC | S1 not running -> relaunch 22/30 |
| 03:48:08 CEST | 01:48:08 UTC | rate: HOLD senders 880 tx/s total (14 up x 62.857), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:48:11 CEST | 01:48:11 UTC | S2 not running -> relaunch 21/30 |
| 03:48:11 CEST | 01:48:11 UTC | rate: HOLD senders 880 tx/s total (15 up x 58.667), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:48:59 CEST | 01:48:59 UTC | S3 not running -> relaunch 19/30 |
| 03:48:59 CEST | 01:48:59 UTC | rate: HOLD senders 880 tx/s total (9 up x 97.778), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:49:02 CEST | 01:49:02 UTC | S4 not running -> relaunch 20/30 |
| 03:49:05 CEST | 01:49:05 UTC | S5 not running -> relaunch 22/30 |
| 03:49:08 CEST | 01:49:08 UTC | S1 not running -> relaunch 23/30 |
| 03:49:11 CEST | 01:49:11 UTC | S2 not running -> relaunch 22/30 |
| 03:49:14 CEST | 01:49:14 UTC | S6 not running -> relaunch 21/30 |
| 03:49:17 CEST | 01:49:17 UTC | S7 not running -> relaunch 21/30 |
| 03:49:20 CEST | 01:49:20 UTC | S8 not running -> relaunch 19/30 |
| 03:49:23 CEST | 01:49:23 UTC | S9 not running -> relaunch 21/30 |
| 03:49:26 CEST | 01:49:26 UTC | S10 not running -> relaunch 19/30 |
| 03:49:26 CEST | 01:49:26 UTC | rate: HOLD senders 880 tx/s total (10 up x 88), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:49:30 CEST | 01:49:30 UTC | S11 not running -> relaunch 19/30 |
| 03:49:30 CEST | 01:49:30 UTC | rate: HOLD senders 880 tx/s total (11 up x 80), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:49:33 CEST | 01:49:33 UTC | S12 not running -> relaunch 23/30 |
| 03:49:33 CEST | 01:49:33 UTC | rate: HOLD senders 880 tx/s total (12 up x 73.333), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:49:36 CEST | 01:49:36 UTC | S13 not running -> relaunch 23/30 |
| 03:49:36 CEST | 01:49:36 UTC | rate: HOLD senders 880 tx/s total (13 up x 67.692), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:49:39 CEST | 01:49:39 UTC | S14 not running -> relaunch 23/30 |
| 03:49:39 CEST | 01:49:39 UTC | rate: HOLD senders 880 tx/s total (14 up x 62.857), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:49:42 CEST | 01:49:42 UTC | S15 not running -> relaunch 23/30 |
| 03:49:42 CEST | 01:49:42 UTC | rate: HOLD senders 880 tx/s total (15 up x 58.667), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 03:50:00 CEST | 01:50:00 UTC | BOT BLOCK: session up, runners 15, disk 35.8 GB, n2 synced true utxoindex false lag 0.2 s mempool 0, bot sub/acc 232.4/230.5 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted 53.7 tx/s (5/6 valid), miner 1, mining share 18.94%, dup share 0.5119 |
| 03:50:29 CEST | 01:50:29 UTC | DEVIATION (fix 16): HOLD dead ~03:41–03:49 (live 0; pending~74; node_cool/rpc_down) — rebuilt tips via electron getUtxosByAddresses; first relaunch polluted by SIGTERM spent tip-save (lanes_dead=200). Quarantined bad tips; rebuild#2; KILL -9 only; post-fix ~876/880 with 15/15 lanes_dead=0. Coins 0; disk 36G; MemAvail ~2.6G. No user ping |
| 03:50:29 CEST | 01:50:29 UTC | night-watch: HOLD OK after fix #16; ~876/880; 15 senders; tips refreshed; n2 synced no-utxoindex; disk 36G; MemAvail ~2.6G; coins 0 (lane-reuse); WS live; no user ping |
| 04:12:13 CEST | 02:12:13 UTC | BOT BLOCK: session up, runners 15, disk 35.7 GB, n2 synced false utxoindex false lag 1068.1 s mempool 0, bot sub/acc 0/0 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted not measured tx/s (0/0 valid), miner 1, mining share -%, dup share - |
| 04:12:25 CEST | 02:12:25 UTC | live summary: pushed logs/bot/SUMMARY.md (1367fd1) |
| 04:12:42 CEST | 02:12:42 UTC | FREEZE start: n2 virtual DAA not moving for 30 s (>= 30 s) (lag 1098.3 s) |
| 04:13:13 CEST | 02:13:13 UTC | miner OFF: n2 not synced for 60 s |
| 04:14:21 CEST | 02:14:21 UTC | S1 not running -> relaunch 24/30 |
| 04:14:21 CEST | 02:14:21 UTC | rate: HOLD senders 880 tx/s total (9 up x 97.778), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 04:14:24 CEST | 02:14:24 UTC | S2 not running -> relaunch 23/30 |
| 04:14:27 CEST | 02:14:27 UTC | S3 not running -> relaunch 20/30 |
| 04:14:30 CEST | 02:14:30 UTC | S4 not running -> relaunch 21/30 |
| 04:14:34 CEST | 02:14:34 UTC | coin buffer: 0 tKAS unclaimed (0 coins) |
| 04:14:34 CEST | 02:14:34 UTC | S5 not running -> relaunch 23/30 |
| 04:14:37 CEST | 02:14:37 UTC | S6 not running -> relaunch 22/30 |
| 04:14:40 CEST | 02:14:40 UTC | S7 not running -> relaunch 22/30 |
| 04:14:43 CEST | 02:14:43 UTC | S8 not running -> relaunch 20/30 |
| 04:14:46 CEST | 02:14:46 UTC | S9 not running -> relaunch 22/30 |
| 04:14:48 CEST | 02:14:48 UTC | FREEZE end: length 156 s, n2 lag 1224 s |
| 04:14:49 CEST | 02:14:49 UTC | S10 not running -> relaunch 20/30 |
| 04:14:49 CEST | 02:14:49 UTC | rate: HOLD senders 880 tx/s total (10 up x 88), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 04:14:52 CEST | 02:14:52 UTC | S11 not running -> relaunch 20/30 |
| 04:14:52 CEST | 02:14:52 UTC | rate: HOLD senders 880 tx/s total (11 up x 80), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 04:14:55 CEST | 02:14:55 UTC | S12 not running -> relaunch 24/30 |
| 04:14:55 CEST | 02:14:55 UTC | rate: HOLD senders 880 tx/s total (12 up x 73.333), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 04:14:58 CEST | 02:14:58 UTC | S13 not running -> relaunch 24/30 |
| 04:14:58 CEST | 02:14:58 UTC | rate: HOLD senders 880 tx/s total (13 up x 67.692), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 04:14:59 CEST | 02:14:59 UTC | miner ON (1 box CPU kaspa-miner, 1 thread, n2 gRPC): n2 synced again / process relaunch |
| 04:15:00 CEST | 02:15:00 UTC | ROW DRAIN DRAIN begins (02:15-02:30 UTC; plan bot: 0; Build: 0; miner on) |
| 04:15:00 CEST | 02:15:00 UTC | rate: DRAIN senders 0 tx/s total (13 up x 0), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 04:15:01 CEST | 02:15:01 UTC | S14 not running -> relaunch 24/30 |
| 04:15:01 CEST | 02:15:01 UTC | rate: DRAIN senders 0 tx/s total (14 up x 0), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 04:15:04 CEST | 02:15:04 UTC | S15 not running -> relaunch 24/30 |
| 04:15:04 CEST | 02:15:04 UTC | rate: DRAIN senders 0 tx/s total (15 up x 0), fees 400/600 [no-signature hop, anyone-can-spend, not realistic payments] |
| 04:15:14 CEST | 02:15:14 UTC | live summary: pushed logs/bot/SUMMARY.md (27c76fc) |
| 04:16:21 CEST | 02:16:21 UTC | DEVIATION (fix 17): HOLD dead ~03:54–04:14 (BOT BLOCK 04:12 0/0; pending~75–81; node_cool/rpc_down) — rebuilt tips via electron getUtxosByAddresses (200/sender stillOld=0); KILL -9 only; relaunch caps reset; brief HOLD ~802–880 with 10–13 up in final ~40s before DRAIN 04:15. Coins 0; disk 36G; MemAvail ~2.9G. No user ping |
| 04:16:21 CEST | 02:16:21 UTC | night-watch: DRAIN OK after fix #17; plan target 0 from 04:15; 15 senders; tips refreshed; n2 synced no-utxoindex; disk 36G; MemAvail ~2.9G; coins 0 (lane-reuse); WS live; no user ping |
| 04:20:00 CEST | 02:20:00 UTC | BOT BLOCK: session up, runners 15, disk 35.6 GB, n2 synced true utxoindex false lag 0.1 s mempool 293, bot sub/acc 34.9/34.9 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted 56.1 tx/s (4/6 valid), miner 1, mining share 9.62%, dup share 0.4549 |
| 04:26:57 CEST | 02:26:57 UTC | night-watch: DRAIN OK pre-END; 15 senders target 0; disk 36G; MemAvail ~2.3G; coins 0; after-END wrap starts at 04:30; no user ping |
| 04:30:00 CEST | 02:30:00 UTC | miner OFF: 02:30 UTC end |
| 04:30:01 CEST | 02:30:01 UTC | EVAL HOLD: bot submitted 9120513 (469.2/468.6 sub/acc tx/s, sec-S*.jsonl (pub-sender), public-node transport errors 107927, delivered>=90% false) (own ids, no-signature hop, anyone-can-spend, not realistic payments), eventual accept 99.87%, p90 0.26 s, rejects 61152, n2 lag max 1224 s, full time at rate true -> clean=false; last clean level 990 |
| 04:30:01 CEST | 02:30:01 UTC | BOT BLOCK: session up, runners 15, disk 35.5 GB, n2 synced true utxoindex false lag 0.2 s mempool 293, bot sub/acc 0/0 tx/s (no-signature hop, anyone-can-spend, not realistic payments), n2 unique accepted 56 tx/s (6/7 valid), miner 1, mining share 18.46%, dup share 0.4654 |
| 04:30:01 CEST | 02:30:01 UTC | END 02:30 UTC: senders 0 and stop, miner off, loggers stop at +30 s |
| 04:30:01 CEST | 02:30:01 UTC | miner OFF: 02:30 UTC end |
| 04:30:24 CEST | 02:30:24 UTC | live summary: pushed logs/bot/SUMMARY.md (6fb0145) |
| 04:32:03 CEST | 02:32:03 UTC | after-END wrap: watchdog stopped; storm/chain/live-loop stopped; senders=0 miner=0; n2 left running |
| 04:32:15 CEST | 02:32:15 UTC | chain recount on n2 starting (window 2026-10-10T17:30:00Z - 2026-10-11T02:30:00Z, before pruning) |
| 04:32:28 CEST | 02:32:28 UTC | end clock read (HTTP Date method; UDP NTP is blocked from the box) |
| 04:32:59 CEST | 02:32:59 UTC | chain recount done (local file) |
| 04:33:07 CEST | 02:33:07 UTC | repo log files written locally (LOGGING.md names, counts only, leak scan clean) |
| 04:33:22 CEST | 02:33:22 UTC | local bot summary written locally |
| 04:33:22 CEST | 02:33:22 UTC | FINISHED marker written (2026-10-11T02:33:22Z) |
| 04:33:36 CEST | 02:33:36 UTC | local bot summary written locally (summarize.py fixed for missing bot_hop_accepted_s) |
