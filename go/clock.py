#!/usr/bin/env python3
"""The one place for times. Edit T0 below, run `python3 go/clock.py`, commit.

It rewrites the blocks between <!-- clock:NAME --> and <!-- /clock:NAME -->
in README.md, go/README.md, go/bot/GO-BOT.md and go/build/GO-BUILD.md,
and writes go/steps-utc.json. Every step is an offset in minutes from T0.
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
    ("X2", 40, 55, 60, "2×, bot 60", "2×, fallback 190, or the scaled rate"),
    ("OFF0", 60, 65, None, "Settle, 0. **Miner off.**", "Settle, 0. **Miner off.**"),
    ("OFF", 65, 80, 85, "Miners-off check, same rate as X2", "Miners-off check, same rate as X2"),
    ("ON", 85, 90, None, "Settle, 0. **Miner on.**", "Settle, 0. **Miner on.**"),
    ("C1000", 90, 105, 110, "bot 120", "1,000 − bot (fallback 880)"),
    ("C1500", 110, 125, 130, "bot 240", "1,500 − bot (fallback 1,260)"),
    ("C2000", 130, 145, 150, "bot 480", "2,000 − bot (fallback 1,520)"),
    ("C2500", 150, 165, 170, "bot 960", "2,500 − bot (fallback 1,540)"),
    ("MAX", 170, 185, 195, "The bot's own max", "Uncapped, up to 9 senders"),
    ("B1", 195, 205, None, "No load", "No load"),
    ("HOLD", 205, 465, None, "Last clean level, or 30 if none", "Last clean rate, or 250 if none"),
    ("DRAIN", 465, 480, None, "Senders 0", "Senders 0"),
    ("END", 480, None, None, "Miner off. Live loggers stop.", "Miner off. Live loggers stop. Node stays up."),
    ("COUNT", 480, 600, None, "Chain count from n2, before pruning", "Chain count from the desk node, before pruning"),
    ("PUSH", None, 660, None, "Logs to `logs/bot/` in this repo", "Logs to `logs/build/` in this repo"),
]

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

BLOCKS = {"table": table(), "key": key(), "header": header()}

root = pathlib.Path(__file__).resolve().parent.parent
for f in ["README.md", "go/README.md", "go/bot/GO-BOT.md", "go/build/GO-BUILD.md"]:
    p = root / f; s = p.read_text()
    for name, body in BLOCKS.items():
        s = re.sub(rf"(<!-- clock:{name} -->\n)(?:.*?\n)?(<!-- /clock:{name} -->)", lambda m: m.group(1) + body + "\n" + m.group(2), s, flags=re.S)
    p.write_text(s)

steps = []
for sid, s, e, dr, bot, build in STEPS:
    iso = lambda m: None if m is None else (T0 + timedelta(minutes=m)).strftime("%Y-%m-%dT%H:%M:%SZ")
    steps.append({"step": sid, "start": iso(s), "end": iso(e), "drain_end": iso(dr), "bot": bot, "build": build})
(root / "go/steps-utc.json").write_text(json.dumps({"t0": T0.strftime("%Y-%m-%dT%H:%M:%SZ"), "end": (T0 + timedelta(minutes=480)).strftime("%Y-%m-%dT%H:%M:%SZ"), "steps": steps}, indent=1, ensure_ascii=False) + "\n")
print("T0", T0.isoformat())
