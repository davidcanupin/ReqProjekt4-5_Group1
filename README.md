# REQEP – EV Charging Network (Gruppe 1)

Requirements Engineering Project, FH Technikum Wien, 3. Semester.
Wir entwickeln im BDD-Stil eine Software für das Ladenetzwerk „EV Charging Network“.

> **Alle Abgaben sind auf Englisch!** Diese README ist auf Deutsch, die Dokumente selbst sind auf Englisch.

---

## 📅 Aktuell: Block 1 „Define the Story“

**Abgabe: Sonntag, 15.11.2026, 18:00 Uhr (Moodle)**

| Aufgabe | Was | Punkte | Datei zum Abgeben |
|---|---|---|---|
| **FA1** Glossary | Einheitliche Begriffe + Definition + Synonyme aus dem Kundentext | 5 | `Block1_Define-the-Story/FA1_Glossary/Glossary-Group1.pdf` |
| **IA2** User Story Map MVP | Eine Map pro Persona (Owner, Customer): Activities → Steps → Tasks, aufgeteilt in MVP / Backlog | 15 | `Block1_Define-the-Story/IA2_User-Story-Map-MVP/User-Story-Mapping-MVP_Group1.pdf` |
| **FA3** Epics & User Stories | Epics aus dem Backbone, **eine User Story pro Task** der Map | 10 | `Block1_Define-the-Story/FA3_Epics-User-Stories/Epics-UserStories_Group1.pdf` |

### ✅ To-do fürs Team (vor der Abgabe)

- [ ] **Alle** lesen die Customer Needs „EV Charging Network“ (Moodle → Course Organization)
- [ ] Glossar gemeinsam durchgehen und euch auf die Begriffe einigen.
      Besonders wichtig, weil diese Namen später im Java-Code landen:
      - **Location** (statt Station/Site)
      - **Charger** (statt Charging Point/EVSE)
      - **Customer Account**, **Top-Up**, **Charging Session**, **Transaction History**
- [ ] User Story Map prüfen: Fehlen Tasks? Ist die MVP/Backlog-Aufteilung sinnvoll?
- [ ] User Stories prüfen: Ist das „so that …“ jeweils sinnvoll?
- [ ] PDFs neu erzeugen (siehe unten) und eine Person lädt sie in Moodle hoch

---

## 🛠 Was ihr installieren müsst

### Für Block 1 (jetzt)

| Tool | Wofür | Download / Check |
|---|---|---|
| **Git** | Repo klonen, Änderungen pushen | macOS: `git --version` (wird sonst automatisch installiert) · Windows: https://git-scm.com/download/win |
| **Python 3** | Erzeugt Story Map + User Stories aus `build.py` | https://www.python.org/downloads/ · Check: `python3 --version` (Windows: `py --version`) |
| **Google Chrome** oder **Microsoft Edge** | Wandelt das HTML in PDF um | ist meistens schon installiert |
| *(optional)* **Miro**-Account | In den Folien wird das Template „User Story Mapping Framework“ empfohlen | https://miro.com |

### Für Block 2 (bis zur nächsten Einheit am 17.11. vorbereiten)

Laut Self-Study soll die IntelliJ-BDD-Umgebung **schon zur nächsten Einheit funktionieren**:

1. **IntelliJ IDEA** in der neuesten Version installieren: https://www.jetbrains.com/idea/download
   (als Studierende bekommt ihr die Ultimate-Version gratis: https://www.jetbrains.com/student/, die Community-Version reicht aber auch)
2. In IntelliJ unter *Settings → Plugins* diese zwei Plugins installieren:
   - **Cucumber for Java**
   - **Gherkin**
3. Testprojekt anlegen: *New Project → Generators → Maven Archetype*
   - **JDK:** neueste Oracle OpenJDK (kann direkt im Dialog heruntergeladen werden)
   - **Catalog:** Maven Central
   - **Archetype:** `io.cucumber:cucumber-archetype`
4. Warten, bis Maven fertig gebaut hat
5. `src/test/resources/org/example/example.feature` ausführen. Das muss **ohne Fehler** laufen.
6. *(für FA5 später)* **Modelio** für das UML-Klassendiagramm: https://www.modelio.org

---

## 🚀 Erste Schritte

1. **Einladung annehmen:** Mail von GitHub öffnen oder https://github.com/davidcanupin/ReqProjekt_Group1/invitations aufrufen
2. **Repo klonen:**
   ```bash
   git clone https://github.com/davidcanupin/ReqProjekt_Group1.git
   cd ReqProjekt_Group1
   ```
3. **Vor jeder Änderung den aktuellen Stand holen:**
   ```bash
   git pull
   ```

## ✏️ Dokumente bearbeiten

| Was ändern? | Welche Datei bearbeiten? |
|---|---|
| Glossar | `Block1_Define-the-Story/FA1_Glossary/Glossary-Group1.html` (einfach im Editor bearbeiten) |
| Story Map **und** User Stories | `Block1_Define-the-Story/build.py`, Bereich `EPICS` und `MAPS` |

Story Map und User Stories werden **beide aus `build.py` erzeugt**. Ein neuer Task in der Map bekommt dadurch automatisch eine User Story, und die zwei Dokumente können nicht auseinanderlaufen. **Bitte die generierten HTML-Dateien nicht von Hand ändern**, sonst werden die Änderungen beim nächsten Build überschrieben.

Ein Task in `build.py` sieht so aus:
```python
("create Charger", "E2", "a new AC or DC Charger can be used at a Location"),
#  ^ Task-Name        ^ Epic   ^ "so that ..." der User Story
```

### PDFs neu erzeugen

```bash
cd Block1_Define-the-Story
python3 build.py        # Story Map + User Stories (HTML) neu erzeugen
python3 export_pdf.py   # alle 3 PDFs erzeugen
```
Unter Windows statt `python3` einfach `py` verwenden.
Wenn kein Chrome/Edge gefunden wird, die HTML-Datei im Browser öffnen und über *Drucken → Als PDF speichern* exportieren. Die Story Map dabei im **Querformat** drucken.

### Änderungen hochladen

```bash
git add .
git commit -m "Glossary: add term XY"
git push
```

---

## 📁 Struktur

```
ReqProjekt_Group1/
├── README.md
└── Block1_Define-the-Story/
    ├── style.css                    # gemeinsames Layout aller Dokumente
    ├── build.py                     # Daten: Epics, Story Map, User Stories
    ├── export_pdf.py                # HTML → PDF
    ├── FA1_Glossary/
    ├── IA2_User-Story-Map-MVP/
    └── FA3_Epics-User-Stories/
```

## ℹ️ Infos

- **Moodle-Kurs:** https://moodle.technikum-wien.at/course/view.php?id=34987
- **Lehrende:** Robert Jonas, Julia Jakoubek
- **KI-Nutzung:** Laut Moodle ist KI bei beurteilten Leistungen verboten, außer es wird ausdrücklich erlaubt. Bitte vor der Abgabe abklären.
- Folien und Unterlagen aus Moodle **nicht ins Repo legen**, weil die Weitergabe laut Copyright-Hinweis verboten ist.
