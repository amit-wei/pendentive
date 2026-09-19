# State Custody (`ST`)

Holds life state, and serves it.

From `FUN-PL-01` and `FUN-PL-09`. Holds what `FUN-PL-12` derives.

Ten functions, thirty-five requirements and eleven risks. Four of the requirements
are safety requirements that answer those risks. `RSK-ST-001` is the
highest-scored risk in the model and its mitigation is `TBD` (`OPN-023`).

Two known gaps. `OPN-037`: `DEC-044` gives an item a subject, and no requirement
here states it, which `DEC-045` needs to separate the holders of one position.
`OPN-040`: `REQ-ST-019` names a location away from the host, against `DEC-020`,
which gives the carriage to `EX`, and against `MET-005`.
