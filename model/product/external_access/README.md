# External Access (`EX`)

The only route between the platform and an external service, in both directions. It
holds the connections and their credentials, carries each call, and records each call.

From `FUN-PL-08`, `FUN-PL-02`, `FUN-PL-15`, `FUN-PL-13`, `FUN-PL-11` and `FUN-PL-01`.

It carries and does not decide. `DEC-123`, which restates `DEC-107`, keeps the check on
an act with Actuation: this system checks no authority over a call that it carries, and
carries a call only from Actuation, Ingestion, Interaction and Agent Runtime
(`DEC-140`), and a copy only from State Custody, Agent Definition and Authorization (`REQ-EX-020`, `REQ-EX-031`). Every part that opens a
connection off the host or holds a credential is here (`DEC-124`). The model provider is
an external service, and this system carries each call to it. Each operation that an
agent can call is a declared act in Actuation. A tool that the provider runs for a call
is refused unless the provider's connection names it as one that only reads, which
needs an answer of the user (`DEC-137`).

A connection is a declaration (`DEC-125`): the service, the account, the scopes, whether
the account can pay or send in the name of the user, whether its use is metered and its
cost, and the tools of its service that only read. An agent declares it. The credential comes from the user
only, and the consent of the user at the service is the answer. A credential with no
connection, or wider than its connection, is refused. The removal of a connection needs
an answer and revokes the credential where the service allows it. Because this system
holds a declaration, it refuses by position on the acts that it holds, as each holder
does.

A connection is metered until the user answers that it is not (`DEC-126`). At the
limit of the month, each metered call is refused except the messages of Interaction and
the calls to a model of the agent that speaks to the user and the agent that receives the
work that this system raises. A call is never repeated (`DEC-129`): the caller learns that it returned no
result and decides.

A session that an agent drives, such as a browser, is signed in here and never sends in
the name of the user (`DEC-127`). How is `OPN-093`, and the lean is a session that only
reads. The holders decide when to make a copy, and this system carries it, encrypts it
and keeps it for a period (`DEC-128`). The user holds the key.

Open against this system: `OPN-093`, `OPN-094` (whether the connections survive the loss
of the host). `RSK-EX-017` is open on `OPN-093`.
