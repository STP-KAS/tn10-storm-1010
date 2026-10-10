#!/usr/bin/env python3
"""The one place for times. Edit T0 below, run `python3 go/clock.py`, commit.

It rewrites the blocks between <!-- clock:NAME --> and <!-- /clock:NAME -->
in README.md, go/README.md, go/bot/GO-BOT.md and go/build/GO-BUILD.md,
and writes go/steps-utc.json (times, plus the fixed rate targets in TARGETS). Every step is an offset in minutes from T0.
Do not change times by hand anywhere else. Do not run this after a prompt is locked.
"""
import json, re, pathlib
from datetime import datetime, timedelta, timezone

T0 = datetime(2026, 10, 10, 15, 0, tzinfo=timezone.utc)   # <- the only time to edit
LOCAL = timezone(timedelta(hours=2), "CEST")               # Brussels, UTC+2

# id, start, end, drain_end, bot, build   (minutes from T0; None = a point in time)
STEPS = [
    ("PREP", None, -45, None, "Prepare. n2 syncing. No sends. Miner off.", "Start node sync now. Prepare. No sends. Miner off."),
    ("G1", -45, None, None, "First gate on n2. Rehearsal go/no-go.", "Stop every sender not in this plan. First gate on the desk node."),
    ("G2", -30, None, None, "Second gate. Start 1 miner, only if n2 is synced.", "Second gate. Start exactly 1 miner."),
    ("R1", -30, -20, None, "60, only if both gates passed", "0"),
    ("R2", -20, -15, None, "20", "0"),
    ("R3", -15, -10, None, "50", "0"),
    ("R4", -10, -7, None, "60", "0"),
    ("R5", -7, -4, None, "0", "60"),
    ("R6", -4, -1, None, "60", "60"),
    ("R7", -1, 0, None, "0", "0"),
    ("B0", 0, 10, None, "**T0.** No load. Miner on.", "**T0.** No load. Miner on."),
    ("S1", 10, 20, None, "60", "0"),
    ("S2", 20, 30, None, "0", "60"),
    ("S3", 30, 40, None, "60", "60"),
    ("X2", 40, 55, 60, "60 (combined 250)", "190"),
    ("OFF0", 60, 65, None, "Settle, 0. **Miner off.**", "Settle, 0. **Miner off.**"),
    ("OFF", 65, 80, 85, "Miners-off check: 60 (combined 250, same as X2)", "Miners-off check: 190 (same as X2)"),
    ("ON", 85, 90, None, "Settle, 0. **Miner on.**", "Settle, 0. **Miner on.**"),
    ("C1000", 90, 105, 110, "400 (combined 1,000)", "600"),
    ("C1500", 110, 125, 130, "700 (combined 1,500)", "800"),
    ("C2000", 130, 145, 150, "950 (combined 2,000)", "1,050"),
    ("C2500", 150, 165, 170, "1,200 (combined 2,500)", "1,300"),
    ("MAX", 170, 185, 195, "1,600 (combined 3,500)", "1,900, may go above with up to 9 senders, never below"),
    ("B1", 195, 205, None, "No load", "No load"),
    ("HOLD", 205, 465, None, "1,500 (combined 3,200); if not clean at that level, the last clean level, or 30 if none", "1,700; if not clean at that level, the last clean rate, or 250 if none"),
    ("DRAIN", 465, 480, None, "Senders 0", "Senders 0"),
    ("END", 480, None, None, "Miner off. Live loggers stop.", "Miner off. Live loggers stop. Node stays up."),
    ("COUNT", 480, 600, None, "Chain count from n2, before pruning", "Chain count from the desk node, before pruning"),
    ("PUSH", None, 660, None, "Logs to `logs/bot/` in this repo", "Logs to `logs/build/` in this repo"),
]

# Fixed targets in tx/s (stp, 10 Oct 12:05 CEST): step -> (combined, bot, build). B0 is measured and reported, not used for targets.
TARGETS = {"X2": (250, 60, 190), "OFF": (250, 60, 190), "C1000": (1000, 400, 600), "C1500": (1500, 700, 800),
           "C2000": (2000, 950, 1050), "C2500": (2500, 1200, 1300), "MAX": (3500, 1600, 1900), "HOLD": (3200, 1500, 1700)}
SUCCESS_TX_S = 3000   # network unique accepted, step median over >= 10 valid minutes, counted once

def t(m, tz=timezone.utc):
    d = (T0 + timedelta(minutes=m)).astimezone(tz)
    s = d.strftime("%H:%M")
    return s + (" " + d.strftime("%a") if d.date() != T0.astimezone(tz).date() else "")

def span(s, e, dr, tz):
    if s is None: return "until " + t(e, tz)
    if e is None: return t(s, tz)
    out = f"{t(s, tz)}–{t(e, tz)}"
    return out + (f", drain to {t(dr, tz)}" if dr is not None else "")

def table():
    rows = ["| Step | UTC | Brussels (CEST) | Bot | Build |", "|---|---|---|---|---|"]
    for sid, s, e, dr, bot, build in STEPS:
        u, l = span(s, e, dr, timezone.utc), span(s, e, dr, LOCAL)
        if sid == "PUSH": u, l = "by " + t(e), "by " + t(e, LOCAL)
        b = f"**{sid}**" if sid in ("B0", "END") else sid
        rows.append(f"| {b} | {u} | {l} | {bot} | {build} |")
    return "\n".join(rows)

def both(m): return f"{t(m)}Z ({t(m, LOCAL)} Brussels)"

def key():
    return "\n".join([
        "| What | UTC | Brussels (CEST) |", "|---|---|---|",
        f"| First gate G1 | {t(-45)} | {t(-45, LOCAL)} |",
        f"| Second gate G2, miners on, rehearsal | {t(-30)} | {t(-30, LOCAL)} |",
        f"| **T0** (B0 starts) | **{t(0)}** | **{t(0, LOCAL)}** |",
        f"| Miners off (OFF0 to ON) | {t(60)}–{t(85)} | {t(60, LOCAL)}–{t(85, LOCAL)} |",
        f"| End (END), miners off | {t(480)} | {t(480, LOCAL)} |",
        f"| Chain count (COUNT) | {t(480)}–{t(600)} | {t(480, LOCAL)}–{t(600, LOCAL)} |",
        f"| Logs pushed (PUSH) | by {t(660)} | by {t(660, LOCAL)} |",
        f"| Suggested window for Kaspa Pulse's counter | {t(-35)}–{t(485)} | {t(-35, LOCAL)}–{t(485, LOCAL)} |",
    ])

def header():
    return (f"T0 is **{T0:%Y-%m-%dT%H:%M:%SZ} ({t(0, LOCAL)} Brussels)**. End is **{both(480)}**. "
            f"Gates G1 {t(-45)}Z and G2 {t(-30)}Z. Every time is in [Key times](#key-times) and the [Timeline](#timeline). "
            "Do not send or mine before the row that says so. Do not move T0.")

def targets():
    rows = ["| Step | UTC | Brussels (CEST) | Combined target | Bot | Build |", "|---|---|---|---|---|---|"]
    for sid, s, e, dr, bot, build in STEPS:
        if sid not in TARGETS: continue
        c, b, d = TARGETS[sid]
        rows.append(f"| {sid} | {t(s)}–{t(e)} | {t(s, LOCAL)}–{t(e, LOCAL)} | {c:,} | {b:,} | {d:,} |")
    return "\n".join([
        "**Changed 10 Oct 2026, 12:05 CEST, by stp:** \"make sure that bot and Build go over 3,000 tx/s, share the load.\" "
        "The goal is now **over 3,000 tx/s combined**, with the load shared between the two sides. "
        "The scaled rule, combined = (multiplier − 1) × B, is dropped. Friday's B was about 55 to 59 tx/s, so scaling would have shrunk "
        "every step (the 2,500 step to about 1,700) and the run could never reach 3,000. "
        "**The combined targets are now fixed.** B0 is still measured and reported, but it no longer sets any rate. "
        "Times, rows, gates, fees, the node-dead rule, the miners and logging are unchanged. Only the rates changed.",
        "",
        "Rates in tx/s, send window only (drains are 0). S1, S2, S3 and the rehearsal keep their rates from the timeline table.",
        "",
        *rows,
        "",
        "- **MAX:** Build may go above 1,900 (up to 9 senders), never below its share.",
        "- **HOLD:** each side holds its HOLD rate only if it was clean at that rate or higher at MAX. If not, it holds its last clean rate "
        "(bot: or 30 if none; Build: or 250 if none). Neither side raises its rate mid-step to cover the other's shortfall.",
        f"- **Success line:** network unique accepted ≥ **{SUCCESS_TX_S:,} tx/s**, as the median of a step's valid minutes, over at least 10 valid minutes "
        "(a valid minute is a complete minute in the chain count). The headline is counted once from chain data, never summed across the two nodes. "
        "Report the signed shape (Build) and the no-signature hop shape (bot) separately.",
        "",
        "**Not sure / open for debate: n2's disk at 2,000+ tx/s.** On this same box, the old pruned node n0 grew 2 to 3 GB a minute under sustained "
        "load of about 2,000 tx/s or more and filled its disk. n2 has the same disk, and it also runs the UTXO index. So n2 may hit its disk guard "
        "during MAX or the long hold. If it does, the bot's senders stop (logged as `disk-guard` and `node-dead`) and Build carries on alone. "
        "Then the combined rate can fall below 3,000. We have not measured n2's growth at these rates yet.",
    ])

BLOCKS = {"table": table(), "key": key(), "header": header(), "targets": targets()}

root = pathlib.Path(__file__).resolve().parent.parent
for f in ["README.md", "go/README.md", "go/bot/GO-BOT.md", "go/build/GO-BUILD.md"]:
    p = root / f; s = p.read_text()
    for name, body in BLOCKS.items():
        s = re.sub(rf"(<!-- clock:{name} -->\n)(?:.*?\n)?(<!-- /clock:{name} -->)", lambda m: m.group(1) + body + "\n" + m.group(2), s, flags=re.S)
    p.write_text(s)

steps = []
for sid, s, e, dr, bot, build in STEPS:
    iso = lambda m: None if m is None else (T0 + timedelta(minutes=m)).strftime("%Y-%m-%dT%H:%M:%SZ")
    row = {"step": sid, "start": iso(s), "end": iso(e), "drain_end": iso(dr), "bot": bot, "build": build}
    if sid in TARGETS: row.update(dict(zip(("combined_tx_s", "bot_tx_s", "build_tx_s"), TARGETS[sid])))
    steps.append(row)
(root / "go/steps-utc.json").write_text(json.dumps({"t0": T0.strftime("%Y-%m-%dT%H:%M:%SZ"), "end": (T0 + timedelta(minutes=480)).strftime("%Y-%m-%dT%H:%M:%SZ"), "success_network_unique_accepted_tx_s": SUCCESS_TX_S, "targets_note": "Fixed combined targets (stp, 10 Oct 12:05 CEST). B0 is measured and reported, not used for targets.", "steps": steps}, indent=1, ensure_ascii=False) + "\n")
print("T0", T0.isoformat())
