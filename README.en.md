<p align="center">
  <img src="docs/assets/readme-banner.svg" alt="Tcl Everyday Workshop — small scripts, useful results" width="100%">
</p>

<h1 align="center">Tcl Everyday Workshop</h1>

<p align="center">
  <strong>Turn everyday data into useful results, one short Tcl script at a time.</strong>
</p>

<p align="center">
  <a href="https://fanqinzeng.github.io/TCL-Tutorial/">Open the workshop</a> ·
  <a href="https://fanqinzeng.github.io/TCL-Tutorial/#lesson/1">First lesson</a> ·
  <a href="docs/TEACHING.md#english-learning-guide">Learning guide</a> ·
  <a href="README.md">中文</a>
</p>

<p align="center">
  <a href="https://github.com/FanqinZeng/TCL-Tutorial/actions/workflows/checks.yml"><img src="https://github.com/FanqinZeng/TCL-Tutorial/actions/workflows/checks.yml/badge.svg" alt="Workshop verification"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-17776b" alt="MIT license"></a>
  <a href="docs/RUNTIME.md"><img src="https://img.shields.io/badge/Tcl-8.6%2B-DA8E56" alt="Tcl 8.6 or later for native practice"></a>
</p>

Clean a registration list, summarize measurements, inspect logs, or build a report pipeline. This original, task-driven course starts with recognizable problems and grows into reusable automation tools. Run **real Tcl directly in your browser**, then take the same examples into local practice.

| Complete lessons | Runnable examples | Hands-on exercises | Applied projects |
| :---: | :---: | :---: | :---: |
| **18** | **55** | **54** | **6** |

Six units also include **24 original SVG explanations** and **six one-minute demonstrations** with Chinese captions and transcripts. Main lesson prose is **Chinese**; the English website home, learning guide, and curriculum overview provide a complete orientation.

## Start with a small, useful task

| Your starting point | Suggested route | Open your first lesson |
| --- | --- | --- |
| **New to programming** | Follow 01–18. Predict an output, run the script, change one input, explain the result. | [01 · Output and scripts →](https://fanqinzeng.github.io/TCL-Tutorial/#lesson/1) |
| **Know another language** | Focus on 03, 06, 08, and 10–15: substitution, lists, records, procedures, scope, and TclOO. | [03 · Tcl substitution →](https://fanqinzeng.github.io/TCL-Tutorial/#lesson/3) |
| **Learning VLSI scripting** | Review lists, dictionaries, procedures, and files, then study 16–18 and projects E/F. | [16 · Tcl and EDA tools →](https://fanqinzeng.github.io/TCL-Tutorial/#lesson/16) |

Every lesson is freely accessible. Follow a route or open the problem you want to solve.

## A notebook and a real Tcl workbench

[![Actual workshop homepage](docs/screenshots/home.jpg)](https://fanqinzeng.github.io/TCL-Tutorial/)

| Change the input, inspect the result | Turn a teaching report into information |
| :---: | :---: |
| [![Variables lesson with the live Tcl workbench](docs/screenshots/lesson-02.jpg)](https://fanqinzeng.github.io/TCL-Tutorial/#lesson/2) | [![VLSI constraints and report lesson](docs/screenshots/lesson-17.jpg)](https://fanqinzeng.github.io/TCL-Tutorial/#lesson/17) |
| [Open lesson 02 →](https://fanqinzeng.github.io/TCL-Tutorial/#lesson/2) | [Open lesson 17 →](https://fanqinzeng.github.io/TCL-Tutorial/#lesson/17) |

Screenshots show the actual website. The workbench displays real output, final variables, and virtual files. Original diagrams explain the concepts, and folded hints let you reveal help one step at a time.

- **Run and check:** edit examples, attempt exercises, and validate output plus lesson-specific behavior.
- **Inspect and explore:** compare changed inputs, observe command execution, and download generated files.
- **Keep your place:** browser-local drafts and reading records can be exported and imported.
- **Watch and try:** [six short demonstrations](https://fanqinzeng.github.io/TCL-Tutorial/#videos) show verified code and results, with captions and transcripts.

## Six units, eighteen lessons

The links below open repository teaching notes. For the runnable version, use the [online curriculum](https://fanqinzeng.github.io/TCL-Tutorial/#course).

| Unit | Lessons | What you will make |
| --- | --- | --- |
| **01 · First useful scripts** | [01 Output](lessons/01/README.md) · [02 Variables](lessons/02/README.md) · [03 Quotes, braces, brackets](lessons/03/README.md) | Notices, shopping totals, message templates |
| **02 · Decisions and repetition** | [04 Conditions](lessons/04/README.md) · [05 Loops](lessons/05/README.md) · [06 Lists](lessons/06/README.md) | Budget decisions, batch calculations, registration lists |
| **03 · Text and records** | [07 Strings](lessons/07/README.md) · [08 Dictionaries and arrays](lessons/08/README.md) · [09 Regular expressions](lessons/09/README.md) | Clean text, structured records, simple log parsers |
| **04 · Reusable scripts** | [10 Procedures](lessons/10/README.md) · [11 Files](lessons/11/README.md) · [12 Errors](lessons/12/README.md) | Reusable calculations and reliable file summaries |
| **05 · Project organization** | [13 Scope and namespaces](lessons/13/README.md) · [14 Modules and arguments](lessons/14/README.md) · [15 TclOO](lessons/15/README.md) | Organized tools and objects with independent state |
| **06 · VLSI applications** | [16 Tcl and EDA](lessons/16/README.md) · [17 Constraints and reports](lessons/17/README.md) · [18 Analysis summaries](lessons/18/README.md) | Teaching path analysis and report workflows |

Each lesson includes a problem, learning goals, an original diagram, at least three examples with expected output, three exercises, layered hints, reference solutions, comprehension questions, common mistakes, and a quick reference.

## Combine your tools into a project

| Project | Your finished tool | Practice |
| --- | --- | --- |
| [**A · Registration cleaner**](projects/A/README.md) | Normalize, deduplicate, and sort a list of names | Lists, strings, procedures |
| [**B · Household expense summary**](projects/B/README.md) | Summarize categories using integer cents and report invalid records | Dictionaries, validation, errors |
| [**C · Measurement statistics**](projects/C/README.md) | Calculate min, max, mean, and out-of-range measurements | Numeric data and boundary cases |
| [**D · Log diagnosis**](projects/D/README.md) | Count warnings and errors while keeping nearby context | Text parsing and line numbers |
| [**E · Teaching path report filter**](projects/E/README.md) | Find negative slack and sort the most severe paths first | Report parsing and educational VLSI models |
| [**F · Configurable report pipeline**](projects/F/README.md) | Load trusted configuration and generate summaries and error records | Modules, files, arguments, reusable workflows |

Each project provides starter code, layered hints, a complete reference implementation, and verification with varied, empty, or invalid inputs. [Open the project workbench →](https://fanqinzeng.github.io/TCL-Tutorial/#projects)

## Bring the workshop to your computer

```sh
git clone https://github.com/FanqinZeng/TCL-Tutorial.git
cd TCL-Tutorial
python3 scripts/serve.py
```

Open **[http://127.0.0.1:8765/](http://127.0.0.1:8765/)**. The browser lab needs no local Tcl, Node, or npm installation; its runtime is included in the repository. Serve the site over HTTP so the runtime can load.

For native practice, install **Tcl 8.6+**, then try:

```sh
tclsh examples/01/01.tcl
python3 scripts/check.py --all
```

File and argument examples use the matching fixtures in `data/`. Native file examples write to their working directory; use a separate practice directory, or let the verifier create a temporary one. The system Tcl 8.5 on some Macs does not support the course's TclOO examples.

<details>
<summary><strong>For contributors: source files, generation, and validation</strong></summary>

Edit `lessons/*.json` and `projects/*.json`, then regenerate the teaching notes, Tcl artifacts, and website data:

```sh
python3 scripts/build.py
python3 scripts/check.py --all
python3 tests/integrity.py
node tests/runtime.mjs
```

Node 18+ is required only for the development tests. The repository also runs native Tcl and browser-runtime checks in GitHub Actions.

```text
lessons/*.json       Canonical lesson content
projects/*.json      Canonical project content
lessons/NN/          Generated teaching notes
examples/            Runnable Tcl examples
exercises/           Exercise starters
solutions/           Reference solutions
data/                Original input fixtures
site/                Static website, WASM runtime, and media
docs/                Teaching, runtime, deployment, and QA notes
scripts/             Generation, validation, preview, and media tools
tests/               Content integrity and real WASM regression tests
.github/workflows/   Verification and GitHub Pages deployment
```

See [contributing](CONTRIBUTING.md), [content schema](docs/CONTENT_SCHEMA.md), [deployment](docs/DEPLOYMENT.md), [accessibility](docs/ACCESSIBILITY.md), and [verification records](docs/QA.md).

</details>

## Runtime and scope

The browser uses **genuine Tcl 8.6.6 through Wacl WebAssembly**. Every run creates a fresh Worker, interpreter, and in-memory filesystem; execution is stopped after five seconds. Optional execution records show observed calls after execution. See [runtime details](docs/RUNTIME.md) for limits and supported behavior.

Drafts and reading records stay in the current browser, with manual export/import. The website works without an account and has no server-side database or telemetry. Native Tcl and browser Tcl are both covered by the [documented verification](docs/QA.md).

VLSI examples use explicitly labeled **educational models** for design objects, constraints, and path reports. They do not connect to commercial EDA tools or perform real STA, Calibre checks, or GDS generation.

## License and references

Original course text, code, data, and SVG artwork are available under the [MIT license](LICENSE). Third-party runtime components retain their own licenses; see [third-party notices](THIRD_PARTY_NOTICES.md).

Language rules follow the [official Tcl 8.6 command reference](https://www.tcl-lang.org/man/tcl8.6/TclCmd/contents.htm). Lessons, exercises, datasets, and the workshop interface are independently designed.

<p align="center">
  <a href="https://fanqinzeng.github.io/TCL-Tutorial/#lesson/1"><strong>Make your first useful script →</strong></a>
</p>
