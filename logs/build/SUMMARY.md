# Build storm 1010

Prompt sha: a755dfe. T0 2026-10-10T15:00:00Z. End 2026-10-10T23:00:00Z. Miner off at END. Node left running.

Joined at 17:28Z. Finished rows PREP through C1500 were logged not-run and were not rerun. C2000 was not sent: the saved coin list was stale and that window was nearly closed.

Fees were the pair 200 and 300 sompi/gram. The desk quote stayed at or under 200 on the rows that sent, so there was no sit-out.

## Chain count

540 complete minutes, 2026-10-10T14:00Z through 2026-10-10T22:59Z, from this desk node's virtual chain.

| | |
|---|---|
| Network unique accepted | 49,246,307 |
| Our chain blocks | 23,189 |

The COUNT step-end figure of 23,764 chain blocks includes the 10 minute lead-in used to resolve mergesets. The table is the file total.

## Steps

Build submit is this side's `submit_ok` per minute, divided by 60. Network unique is the chain count for the same minutes, each id once. A valid minute is a complete chain-count minute.

| Step | Window (UTC) | Target | Build submit median | Network unique median | Rejects | Clock clean |
|---|---|---|---|---|---|---|
| C2500 | 17:40–17:44, 5 min | 1,875 | 1,778 | 2,505 | 0 | yes |
| MAX | 17:55–18:04, 10 min | 2,600 | 875 | 1,726 | 0 | yes, see below |
| B1 | 18:15–18:25, 10 min | 0 | 0 | 106 | 0 | no |
| HOLD | 19:50–22:44, 175 min | 1,875 | 1,722 | 4,032 | 0 | no |
| DRAIN | 22:45–22:59, 15 min | 0 | 0 | 2,155 | 0 | no |

C2500 submit over those five minutes was 535,431. The window is shorter than 10 minutes.

MAX submit over those ten minutes was 525,568. `steps.csv` marks MAX clean because the per-loop mean treated a slow loop as one second. The minute submit median is 875, which is under 2,600 and outside the 5% band. MAX was not clean. HOLD used 1,875 from C2500, which is the last rate that had been held near its target. The earlier HOLD label of 2,400 is superseded in `events.csv`.

HOLD full minutes: submit min 1,444, max 1,844, total submit 18,050,020, rejects 0. That is outside the 5% band around 1,875, so the step is not clean. Network unique min 2,098, max 4,618. 138 of the 175 minutes were at or above 3,000 tx/s. The median of the 175 complete minutes is 4,032 tx/s.

The 19:49Z minute is partial: the 1,875 arm started at 19:49:21Z. `minute.csv` has no 22:59Z row. The clock stopped at 23:00Z before that flush. `chain-count.csv` has 22:59Z: 131,130 accepts, 2,185.50 tx/s.

## Headline

The success line is network unique accepted at or above 3,000 tx/s, the median of a step's valid minutes, over at least 10 valid minutes, counted once. HOLD's median is 4,032 tx/s over 175 complete minutes.

## What broke, and what was done

- A false G1 step-start and a false PUSH step-start were corrected before any send.
- The first HOLD arm was labelled 2,400 and was spending coins already used by C2500 and MAX. It was stopped. The coin list was refreshed from the desk node. HOLD was armed again at 1,875.
- The sec row at 19:46:12Z replayed older sender logs. That row and its orphan reject row were cleared. Minutes 19:43Z through 19:46Z were not flushed.
- `confirm.csv` and `order.csv` have a row per step and empty measurements. Confirmation latency and send-versus-accept order were not measured.

Per-transaction logs stayed on the desk.
