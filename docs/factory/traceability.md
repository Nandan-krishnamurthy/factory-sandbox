# Traceability

Requirement → Story → PR → Test, across every increment of this project. S05 creates this file and adds one row per requirement; each story PR updates its own rows at S11, so a row is merged together with the code it describes.

A requirement is **Done** when its row says `Implemented` and every PR listed for it is merged. `/factory-status` works that out from GitHub; it is not written here.

Status is one of: `Not started`, `In progress`, `Implemented`, `Deferred`.

| REQ | Stories | PRs | Tests | Status |
|---|---|---|---|---|
| REQ-001 | STORY-001 (#10) | #12 | `#10 AC1: python -m tempconv 100 prints 212.0 and exits 0`; `#10 AC1: 100 °C is 212.0 °F` | Implemented |
| REQ-002 | STORY-001 (#10) | #12 | `#10 AC2: python -m tempconv -40 prints -40.0`; `#10 AC2: -40 °C is -40.0 °F` | Implemented |
| REQ-003 | STORY-001 (#10) | #12 | `#10 AC3: python -m tempconv 36.6 prints 97.88`; `#10 AC3: 36.6 °C is 97.88 °F` | Implemented |
| REQ-004 | STORY-002 | — | — | Not started |
| REQ-005 | STORY-002 | — | — | Not started |
| REQ-006 | STORY-001 (#10) | #12 | `#10 AC4: every module in tempconv imports only stdlib modules or tempconv itself` | Implemented |
| REQ-007 | STORY-001 (#10) | #12 | `#10 AC4` and `#10 AC5`: the suite runs with `python -m unittest` | Implemented |
