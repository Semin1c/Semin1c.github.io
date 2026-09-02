# Portfolio index

The landing page at [semin1c.github.io](https://semin1c.github.io) — a single
self-contained `index.html` with the project charts base64-embedded, so there
are no asset paths to break.

`build_index.py` regenerates it. Project titles, findings, stat lines and repo
links live in the `PROJECTS` list at the top of that file; edit there and re-run:

```bash
python3 build_index.py .
```

The page links out to the project repositories, so their content is always
current. The summary text on this page is not pulled from them automatically —
if a project's headline finding changes, update `PROJECTS` and rebuild.
