# Third-party components

Original course text, tasks, data, diagrams and website code are independently authored under MIT. No teaching text, questions, artwork or page layout from the two reviewed teaching repositories is included.

- **Wacl**, ecky-l, 2017 distribution: [upstream](https://github.com/ecky-l/wacl), [original archive](https://ecky-l.github.io/wacl/releases/wacl.zip). BSD-3-Clause; full text `site/vendor/WACL-LICENSE`. `wacl.wasm`, `wacl-library.data`, `wacl-custom.data` copied unmodified. One Worker compatibility patch in `wacl.js`: guard `delete window.Module` with `typeof window !== "undefined"`. We call the native exported Tcl C API, not the upstream string-concatenating Eval wrapper.
- **Tcl 8.6.6** and bundled Tcl library: copyrights retained in runtime; full primary Tcl terms `site/vendor/TCL-LICENSE`. Wacl also contains tDOM, rl_json and selected Tcllib extensions; embedded package copyright notices remain intact. These extensions are not used as curriculum dependencies. Their upstream source and terms are available in Wacl's `ext/` directory.
- **RequireJS 2.3.7**, James Burke and contributors: MIT, copyright and upstream license URL preserved in `site/vendor/require.js`. Source distribution: https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.7/require.min.js . The deployed site uses the local copy, not this CDN.

Runtime asset hashes are recorded in `site/vendor/SHA256.json`. There are no downloaded stock illustrations, icon libraries or external web fonts. SVGs and the favicon are original. Videos are generated from original demonstration scripts with real native Tcl output. System fonts are used for layout; no font files are redistributed.

The course cites the [Tcl 8.6 official manual](https://www.tcl-lang.org/man/tcl8.6/TclCmd/contents.htm) to verify semantics; its prose is not reproduced as course chapters.
