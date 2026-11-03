"""Generates IA2 (User Story Map MVP) and FA3 (Epics & User Stories) HTML from one data source,
so that every User Story Map task has exactly one User Story.

Usage:  python3 build.py   (then run: python3 export_pdf.py)
"""
from html import escape
from pathlib import Path

HERE = Path(__file__).parent

# ---------------------------------------------------------------------------
# Epics (one Epic = scope of one future BDD Feature File)
# ---------------------------------------------------------------------------
EPICS = {
    "E1": ("Location Management", "Owner", "manage Locations",
           "I can represent the sites of my EV Charging Network in the system"),
    "E2": ("Charger Management", "Owner", "manage the Chargers of each Location",
           "Customers can charge their vehicles with AC or DC"),
    "E3": ("Price Management", "Owner", "manage the Price List of each Location",
           "Charging Sessions are billed correctly and I can react to market changes"),
    "E4": ("Charger Status Management", "Owner", "manage the Charger Status",
           "only usable Chargers are offered to Customers"),
    "E5": ("Network Status", "Owner / Customer", "view the Network Status at any time",
           "I know the current Price Lists and which Chargers are available"),
    "E6": ("Customer Account Management", "Customer", "register and manage my Customer Account",
           "I can use the EV Charging Network"),
    "E7": ("Top-Up", "Customer", "top up my Customer Account in advance",
           "I have enough Balance to charge (prepaid system)"),
    "E8": ("Charging Session", "Customer", "charge my vehicle at a Charger",
           "my vehicle has enough energy and the Charging Cost is billed automatically"),
    "E9": ("Transaction History", "Customer / Owner", "view the Transaction History of a Customer Account",
           "Top-Ups, Charging Costs and the Balance are transparent"),
}

# ---------------------------------------------------------------------------
# User Story Maps: persona -> list of activities -> list of steps -> tasks
# task = (task title, epic id, "so that" value)
# ---------------------------------------------------------------------------
MAPS = {
    "Owner": [
        ("Network Setup", [
            ("manage Locations",
             [("create Location", "E1", "a new site of my EV Charging Network is available in the system"),
              ("read Locations", "E1", "I have an overview of all my Locations")],
             [("update Location", "E1", "Location data stays correct"),
              ("delete Location", "E1", "closed sites are removed from the EV Charging Network")]),
            ("manage Chargers",
             [("create Charger", "E2", "a new AC or DC Charger can be used at a Location"),
              ("read Chargers", "E2", "I know which Chargers exist at each Location")],
             [("update Charger", "E2", "Charger data (e.g. Charging Mode) stays correct"),
              ("delete Charger", "E2", "removed Chargers are no longer offered")]),
        ]),
        ("Pricing", [
            ("manage Price Lists",
             [("create Price List", "E3", "Charging Sessions at a Location can be billed"),
              ("read Price List", "E3", "I know the currently valid Prices of a Location"),
              ("update Price List", "E3", "new Prices apply to Charging Sessions started afterwards")],
             []),
        ]),
        ("Network Operation", [
            ("manage Charger Status",
             [("set Charger Out of Order", "E4", "a defective Charger cannot be used"),
              ("set Charger Available", "E4", "a repaired Charger can be used again")],
             []),
            ("view Network Status",
             [("read Network Status", "E5", "I see Price Lists and Charger Status of all Locations")],
             [("filter Network Status by Location", "E5", "I can quickly check one Location")]),
        ]),
        ("Account Monitoring", [
            ("view Customer Accounts",
             [("read Customer Accounts", "E6", "I know who is registered in my EV Charging Network")],
             [("deactivate Customer Account", "E6", "misused Customer Accounts can be blocked")]),
            ("view Transaction History",
             [("read Transaction History of a Customer", "E9", "I can check Top-Ups, Charging Costs and Balance of a Customer")],
             [("filter Transaction History by period", "E9", "I can analyse a specific time range")]),
        ]),
    ],
    "Customer": [
        ("Onboarding", [
            ("register",
             [("create Customer Account", "E6", "I can use the EV Charging Network"),
              ("read Customer Account", "E6", "I can check my registered data")],
             [("update Customer Account", "E6", "my data stays up to date"),
              ("delete Customer Account", "E6", "my data is removed when I stop using the service")]),
        ]),
        ("Account Funding", [
            ("top up Customer Account",
             [("top up Customer Account", "E7", "I have enough Balance to start a Charging Session"),
              ("read Balance", "E7", "I know how much money is left")],
             []),
        ]),
        ("Charging", [
            ("find Charger",
             [("read Network Status", "E5", "I can find an Available Charger and its Prices")],
             [("filter Network Status by Location", "E5", "I only see Chargers near me"),
              ("filter Network Status by Charging Mode", "E5", "I only see AC or DC Chargers")]),
            ("charge vehicle",
             [("start Charging Session", "E8", "my vehicle is charged at the Prices valid at the start"),
              ("end Charging Session", "E8", "the Charging Cost is calculated and deducted from my Balance")],
             [("read running Charging Session", "E8", "I see Charged Energy and Charging Duration so far")]),
        ]),
        ("Account Review", [
            ("view Transaction History",
             [("read Transaction History", "E9", "I can check all my Top-Ups, Charging Sessions and my Balance")],
             [("filter Transaction History by period", "E9", "I can review a specific month")]),
        ]),
    ],
}

HEAD = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>{title}</title>
<link rel="stylesheet" href="../style.css"></head><body>
"""


def build_maps() -> str:
    out = [HEAD.format(title="User Story Map MVP – Group 1")]
    for persona, activities in MAPS.items():
        steps = [s for _, ss in activities for s in ss]
        n = len(steps)
        out.append('<section class="map">')
        out.append(f'<div class="map-title">User Story Map “EV Charging Network” – Persona: {persona}'
                   f' &nbsp;·&nbsp; Group 1</div>')
        out.append(f'<div class="grid" style="grid-template-columns: repeat({n}, 1fr)">')
        # Activities row (blue) – each activity spans its steps
        for act, ss in activities:
            out.append(f'<div class="card activity" style="grid-column: span {len(ss)}">{escape(act)}</div>')
        # Steps row (yellow) = Backbone / narrative flow
        for step, *_ in steps:
            out.append(f'<div class="card step">{escape(step)}</div>')
        for lane, idx in (("MVP", 1), ("Backlog", 2)):
            out.append(f'<div class="lane">{lane}</div>')
            for s in steps:
                tasks = s[idx]
                cards = "".join(f'<div class="card">{escape(t[0])}</div>' for t in tasks) or \
                        '<div class="card empty"></div>'
                out.append(f'<div class="cell">{cards}</div>')
        out.append('</div>')
        out.append('<div class="legend">Legend:<span style="border:2px solid #3d8fd9"></span>Activity'
                   '<span style="border:2px solid #f2c21b"></span>Step Task (Backbone / narrative flow)'
                   '<span style="border:1px solid #aaa"></span>Detail Task (→ User Story)</div>')
        out.append('</section>')
    out.append("</body></html>")
    return "\n".join(out)


def build_epics() -> str:
    # collect stories per epic, in map order
    per_epic = {e: [] for e in EPICS}
    for persona, activities in MAPS.items():
        for _, steps in activities:
            for step, mvp, backlog in steps:
                for prio, tasks in (("MVP", mvp), ("Backlog", backlog)):
                    for title, epic, value in tasks:
                        per_epic[epic].append((persona, title, value, prio))

    out = [HEAD.format(title="Epics & User Stories – Group 1")]
    out.append('<header class="doc"><h1>FA3 – Epics &amp; User Stories “EV Charging Network”</h1>'
               '<div class="meta">Requirements Engineering Project · Group 1 · Version 1.0 (draft) · '
               'based on IA2 User Story Map MVP</div></header>')
    out.append('<p class="note">Each Epic is derived from the narrative flow (Backbone) of the User Story Map and '
               'represents the scope of one future BDD Feature File. Each User Story corresponds to exactly one '
               'task of the User Story Map. Format: <em>As &lt;user&gt; I want &lt;function&gt; so that '
               '&lt;value&gt;</em>. All terms follow the Glossary (FA1).</p>')

    us_no = 0
    for eid, (name, user, function, value) in EPICS.items():
        out.append('<div class="epic"><div class="epic-head">'
                   f'<span class="id">{eid}</span><strong>{escape(name)}</strong>'
                   f'<span class="story">As {escape(user)}, I want to {escape(function)}, '
                   f'so that {escape(value)}.</span></div>')
        out.append('<table><tr><th style="width:9%">ID</th><th>User Story</th>'
                   '<th style="width:11%">Priority</th></tr>')
        for persona, title, val, prio in per_epic[eid]:
            us_no += 1
            out.append(f'<tr><td>US{us_no:02d}</td><td>As {persona}, I want to {escape(title)}, '
                       f'so that {escape(val)}.</td>'
                       f'<td><span class="badge {prio.lower()}">{prio}</span></td></tr>')
        out.append('</table></div>')
    out.append("</body></html>")
    return "\n".join(out)


if __name__ == "__main__":
    (HERE / "IA2_User-Story-Map-MVP" / "User-Story-Mapping-MVP_Group1.html").write_text(build_maps(), "utf-8")
    (HERE / "FA3_Epics-User-Stories" / "Epics-UserStories_Group1.html").write_text(build_epics(), "utf-8")
    print("HTML generated.")
