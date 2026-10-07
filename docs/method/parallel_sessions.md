# Parallel sessions

Two sessions may work at the same time, each on a different system, in one checkout.

- **Each session states which system it owns**, in one line where the other session
  reads it. Check whether the other session wrote its line.
- **The sessions find and reach each other** through the agent tooling (in Claude
  Code: `ListAgents`, then `SendMessage`). Say before you edit a shared file. Keep
  messages rare and short.
- **A session's system directory is its own.** A change that the other session's
  system needs is an `OPN-` row or a message, not an edit.
- **Shared files** (`model/registers/*.csv`, the `product_*.csv` files,
  `compartments.csv`): re-read just before editing, append or make small edits only,
  and take the next free identifier at the moment of writing.
- **A shared decision is settled before either session writes rows on it.**
- **A cascade** (a supersession) touches rows everywhere. Tell the other session first.
- **Commits:** stage by path, never everything. If the validator fails on the other
  session's rows, message it and wait. Don't fix its rows.
- **Close-out:** the session that closes last updates the top-level README and the
  shared session state. The session that closes first leaves a short note for it.
