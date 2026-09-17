# The Hardest Letters — Companion Tools

Companion code for *The Hardest Letters: What It Really Took to Print a Page*, a middle-grade illustrated booklet about movable type printing in Renaissance Venice — and, four hundred years later, hot-metal Linotype composition.

These tools let a reader do what a real print shop had to do: figure out how many pieces of each letter a font needs, based on real text, real production settings, and real physics.

**Try it right now, no download needed:** [estrong-type.github.io/hardest-letters-tools/printers-bill.html](https://estrong-type.github.io/hardest-letters-tools/printers-bill.html)

---

## What's in this repository

### `printers-bill.html`
A self-contained web app — open it in any browser, or use the live link above. Paste in your own text, or load one of three built-in samples (the U.S. Constitution, an excerpt of *King Lear* in its original 1623 First Folio spelling, or the opening chapter of *Alice's Adventures in Wonderland*), then describe a print shop: how many sheets it prints a day, how many days pass before distributed type becomes available again, how much safety buffer to build in against a bad week. The tool casts a full two-case bill — capitals and lowercase counted separately, exactly the way a real shop's type was actually stored — and estimates the total weight of lead-tin-antimony type metal the shop would need to own.

### `printers_bill.py`
The same tool, as a Python script meant to be read and typed in by hand — in the spirit of the book itself, where a compositor built every line one piece at a time. Requires only Python 3 and its standard library; no installation needed beyond that. Open the file, read the comments, and change the settings at the top to experiment.

```bash
python3 printers_bill.py
```

### `quarto-imposition.svg` / `quarto-imposition.png`
A diagram of how a quarto sheet was actually imposed for printing — eight pages per sheet, four to a side, two of them upside down on purpose, folding into correct reading order. Referenced in Chapter Ten.

---

## A note on the sample texts

The Constitution, *King Lear*, and *Alice's Adventures in Wonderland* are all in the public domain. The *Lear* excerpt is transcribed in its original First Folio spelling on purpose — "vs" for "us," "haue" for "have" — since older orthography measurably changes a text's letter-frequency profile, which is itself part of the lesson.

## About the book

*The Hardest Letters* traces the real engineering, economic, and typographic problems behind printing a page — from a Venetian punchcutter's workshop in 1490 to a twentieth-century Linotype composing room to the thousands of free fonts sitting on an ordinary laptop today.
