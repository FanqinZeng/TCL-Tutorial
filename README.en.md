# Tcl Everyday Workshop

[中文](README.md) · [Learning guide](docs/TEACHING.md)

Small scripts, useful results. An original, practical Tcl curriculum with **18 full lessons, 54 exercises, six independent projects, real browser Tcl, SVG explanations and six captioned demonstrations**.

Repository: [FanqinZeng/TCL-Tutorial](https://github.com/FanqinZeng/TCL-Tutorial). Pages target: [fanqinzeng.github.io/TCL-Tutorial/](https://fanqinzeng.github.io/TCL-Tutorial/) (verify deployment in Actions).

## Choose a route

- First programming experience: lessons 1–18 in order. Predict, run, change one input, explain what happened.
- Experience in another language: focus on 3, 6, 8 and 10–15: substitution, Tcl lists, records, procedures, scope, and TclOO.
- VLSI: review lists, dictionaries, procedures and files, then lessons 16–18 and projects E/F. All tool models are explicitly educational.

## Complete curriculum overview

1. Output and scripts — create an event notice.
2. Variables and calculation — calculate a shopping total.
3. Quotes, braces and brackets — understand substitution.
4. Conditional decisions — compare shopping plans.
5. Repetition — process measurement rows.
6. Lists — maintain a registration list, including names with spaces.
7. Strings — normalize contact text.
8. Dictionaries and arrays — represent sample records.
9. Regular expressions — extract simple log fields.
10. Procedures and parameters — make reusable fee tools.
11. File I/O — summarize experiment records.
12. Errors and debugging — explain missing files and invalid input.
13. Scope and namespaces — organize related tools.
14. Modules and arguments — configure a report entry point.
15. TclOO — maintain a measurement instrument's state.
16. Tcl and EDA — distinguish language commands from tool extensions.
17. Constraints and reports — inspect a simplified teaching model.
18. Analysis summaries — combine parsing, validation and reporting.

Independent projects: registration cleaner; household expense summary; measurement statistics; context-aware log diagnosis; teaching path report filter; configurable reporting pipeline. Each has starter code, layered hints, a full reference implementation, and varied, empty and invalid verification cases.

Main lesson prose is Chinese. The English homepage, guide and curriculum overview are complete; the language control clearly opens that overview rather than pretending to translate the lesson body.

## Run locally

```sh
git clone https://github.com/FanqinZeng/TCL-Tutorial.git
cd TCL-Tutorial
python3 scripts/serve.py
# http://127.0.0.1:8765/
```

Use HTTP; do not open index.html directly. The browser lab needs no local Tcl or Node installation and loads no external CDN. Native practice requires **Tcl 8.6+** (TclOO). File examples write to their working directory; practice in a separate directory. The verifier creates temporary working directories.

```sh
python3 scripts/build.py
python3 scripts/check.py --all
python3 tests/integrity.py
node tests/runtime.mjs
```

## Runtime and limits

Every run creates a fresh Web Worker, genuine Wacl Tcl 8.6.6 interpreter and virtual in-memory filesystem. Execution times out after five seconds; stop cancels it. Result views display actual final variables and files. Optional execution records use real Tcl observation, capped at 120 events. Diagrams are labeled illustrations. Local native validation also covers Tcl 9.0.4.

Browser drafts, manually marked reading and recent location can be exported/imported. There is no login, remote database, tracking or ranking. EDA and slack examples are teaching models, not commercial EDA, real STA, Calibre or GDS generation.

## Contribute and attribution

Edit `lessons/*.json` and `projects/*.json`, then regenerate Markdown, Tcl artifacts and `site/course.json`. See [CONTRIBUTING](CONTRIBUTING.md), [runtime](docs/RUNTIME.md), [deployment](docs/DEPLOYMENT.md) and [accessibility](docs/ACCESSIBILITY.md).

Original code, prose and artwork: MIT, FanqinZeng. Third-party components keep their licenses: [notices](THIRD_PARTY_NOTICES.md). Language semantics are checked against the [official Tcl 8.6 manual](https://www.tcl-lang.org/man/tcl8.6/TclCmd/contents.htm).
