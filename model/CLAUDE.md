# model/

Before you write or change a row, read:

- `model_conventions.md`: what makes a row valid.
- `../docs/method/writing_rows.md`: what makes a valid row good.
- `../docs/method/decomposition.md`: the procedure for a system.

What bites in this folder:

- **Edit a CSV through a script, by identifier.** Never by hand, and never by
  regenerating a shared file whole.
- **Read the successor.** Many decisions are superseded. The row that a search finds
  first is often the retired one; `superseded_by` names the one that stands.
- **A new bare "shall report" row** at system level must be listed in its system's
  "give Self-Observation each fact" row (`MET-027`), or the validator fails.
- **Run `uv run python model/validate_model.py`** after every change.
