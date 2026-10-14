# Python learning checkpoint

Last updated: 14 October 2026 (India time)
Learner: Hemant
Goal: Learn enough Python to start FastAPI and DSA, then deepen Python through an Applied AI project.
Target: 5–7 focused days; flexible, including 2–3 weeks if needed.
Background: Experienced with JavaScript/Node.js and Java. Use comparisons where they help.

## Current checkpoint — start here

- Assessed completion: **12/12 topics passed**.
- Current topic: FastAPI project setup — Python foundations complete, all readiness gates GO.
- All 12 minimum Python topics GO. All three readiness gates passed: language, async and DSA.
- Exceptions/modules/imports GO: two-file code, main guard explanation and both execution outputs reviewed.
- Classes GO: Task and PriorityTask code/output reviewed, instance state, inheritance, override, self and super understood.
- Type hints GO: parameter/return/collection/optional annotations demonstrated; runtime non-enforcement understood; annotation-only uninitialised dict fixed.
- Comprehensions, sorting/lambda GO: lambda key/reverse syntax and sorted() preserving original correctly demonstrated; sort() return None understood.
- Scope GO: local/global shadowing, no if/for block scope, NameError versus UnboundLocalError, nonlocal/global and mutation versus rebinding reviewed.
- Functions/arguments GO: def, return, positional/keyword calls, defaults, mutable-default pitfall and reference mutation assessed.
- References/mutability GO: all four predictions and reasons correct, including nested shallow-copy identity. Clarified that copy() copies element references rather than deeply copying by value.
- Collections GO: lists, tuples, dictionaries and sets assessed.
- Conditions and loops: GO. Reviewed even/odd, accumulator, enumerate, while countdown and if/elif/else; learner correctly predicted enumerate starting at 5.
- Variables/basic types: GO. Learner demonstrated five basic types, type(), f-string formatting, int conversion, and correctly predicted mixed string/int TypeError. Actual exercise filename: basic.py.
- Python setup and uv: GO. Installed tools, initialised project, ran a Python file, and correctly identified installed package location. Dependency installation will be practised when needed.
- Python command works: user reported `python --version` → `Python 3.14.7`. This is reported output, not independently verified.
- Initial uv command was not found. Installation and PATH setup are now confirmed on macOS (aarch64).
- Explained Python versus uv, uv's rough equivalence to npm, and pip versus uv (see learning notes section 5).
- User confirmed `uv --version` → `uv 0.13.0 (4ecd0eff2 2026-10-09 aarch64-apple-darwin)` after sourcing the installer environment file.
- Actual learning project: `applied_ai_engineering/python_core`; user ran `uv init`, which reported project name `python-core`.
- Practical run succeeded: `uv run python src/python_core/__init__.py` → `Hello, Hemant` (user-reported output).
- Lists final code reviewed as correct: first/last f-string using [0]/[-1], print(nums), len(nums). No final output submitted; code is sufficient for this small check. Lists GO.
- Tuples GO: indexing, unpacking, singleton tuple and immutability prediction correct; removing singleton comma correctly identified as str. len/type print lines were omitted initially and supplied as corrections; no rerun submitted, core understanding demonstrated.
- Dictionaries GO: code/output reviewed for access, update, add, get, membership, iteration, length; deletion code submitted without printed result. Correctly distinguished missing-key KeyError from int/string TypeError in follow-up.
- Sets GO: conversion, membership, add/discard, union/intersection/difference and empty-set type demonstrated. Correctly explained set class versus stored set instance. Initial length/value print requirements omitted and supplied as corrections; final rerun not required for core concept GO.
- Function tasks: add, greet, count_even and double correct. print/return misunderstanding corrected; keyword call now demonstrated as add_tag_safe(tags=existing, tag="python"). Mutable-default reuse correctly predicted and safe None-default function submitted; advised is None instead of == None.
- Comprehensions GO: squares, even filter, even squares, word-length dict all correct; predicted [2,4,6] and unchanged outer x=99. Full execution output not submitted; code review sufficient.
- Exceptions GO: parse_age converts strings, raises ValueError for negatives, per-input try/except handles failures and continues, reject prediction correct. Submitted code reviewed; no execution output provided.
- JSON GO: dumps/loads and dict access correct; initially used dumps for invalid JSON and predicted values instead of type names. Corrected loads, JSONDecodeError handling, and parsed count + 2.
- Async GO: correct coroutine/await/run code, blocking sleep explanation, and sequential timing. Initially said asyncio.sleep sleeps the thread; corrected and explicitly confirmed only coroutine suspends and other scheduled tasks can run.
- Two Sum GO: correct one-pass dict solution and expected O(n) time/O(n) space. Initially attributed distinct indices to one traversal; corrected and independently explained check-before-insertion prevents same-index reuse for [3], target 6. Returned reverse index order is valid. No execution output submitted; code reviewed.
- Group Anagrams GO: corrected sorted-list unhashable key to joined string, initialised groups, used items iteration. Correct O(n*k log k) analysis and final explanation abb/bab share canonical key. Submitted code reviewed; final execution output not provided.
- Next action: start separate fastapi-learning project beside python_core with uv init and uv add "fastapi[standard]". First GET endpoint then task API with POST/validation/in-memory store. Maintain Python DSA practice alongside building.
- Added explicit variable scope/name lookup topic immediately after functions and before comprehensions. Total checklist is now 12 topics; all 12 passed.
- `__init__.py` can run as a file, but normally marks/initialises a regular Python package; use a separate exercise file for future tasks. Modules/imports have since been assessed; package details can be deepened while building.
- Concept checks: correctly identified Python as the runtime and expected project package separation. Explained that environment choice, not sibling folder placement, controls isolation.
- First Python execution succeeded. Learner correctly identified .venv as the installed package location; explained pyproject.toml, uv.lock and .env distinctions. Dependency installation has not been demonstrated yet and can be practised later.

## Teaching and assessment rules

1. Explain one topic briefly with Python-specific details and useful JS/Java comparisons.
2. Give a small coding task or explanation task. For coding exercises, provide a paste-ready Python code block with questions as comments, starter data and TODOs; do not include solutions before the learner attempts them.
3. Review actual code/output/reasoning and give GO or NO-GO.
4. On NO-GO, explain the gap differently and give a fresh task.
5. Move on after GO. Allow a direct assessment when the learner already knows a topic.
6. Record important questions, answers, mistakes, and examples in python-learning-notes.md.
7. Update this checkpoint after each reviewed task or meaningful discussion.
8. Use demonstrated readiness rather than the calendar. Keep the focus on building.
9. Exercises should be written by the learner; do not give their solution before an attempt unless requested.

## Readiness checklist

Only mark a box when the topic's task is passed.

| Done | Topic | Planned day | Status / evidence |
|---|---|---|---|
| [x] | Python setup and uv: environments, dependencies, running files | 1 | GO: tools installed, project initialised, file ran, package location understood; dependency command explained |
| [x] | Variables and basic types: int, float, str, bool, None, dynamic typing | 1 | GO: code/output and TypeError prediction reviewed |
| [x] | Conditions and loops: if, elif, for, while, range, enumerate | 1 | GO: code/output reviewed; range and enumerate predictions correct |
| [x] | Lists, tuples, dictionaries, sets: indexing, slicing, iteration, operations | 2 | GO: all four collections reviewed |
| [x] | Object references and mutability: identity, copying, mutable/immutable | 2 | GO: four predictions and explanations reviewed |
| [x] | Functions and arguments: def, return, positional/keyword/defaults; mutable defaults | 3 | GO: reviewed functions, mutable-default rewrite and keyword call |
| [x] | Variable scope and name lookup: LEGB, block scope, shadowing, global/nonlocal, UnboundLocalError | 3 | GO: corrected block scope misconception; global/nonlocal and mutation/rebinding predictions passed |
| [x] | Comprehensions, sorting and lambda: list/dict comprehensions, sorted, key | 3 | GO: reviewed comprehension code and corrected sorting/lambda tasks |
| [x] | Type hints: list[int], dict[str, int], None, optional values | 4 | GO: annotated functions/collections, optional prefix and initialisation correction reviewed |
| [x] | Classes and objects: self, __init__, attributes, basic inheritance | 4 | GO: Task/PriorityTask code and full execution output correct |
| [x] | Exceptions, modules and imports: try, except, raise, multiple files | 4 | GO: parse_age, per-input try/except, two-file imports and main guard; both runs verified |
| [x] | Basic JSON and async/await: serialisation, coroutines, blocking/non-blocking I/O | 5 | GO: JSON tasks and async code/explanations reviewed |

## DSA tools — learn as needed

Start familiar DSA problems once collections and functions are understood.

| Tool | Purpose | Status |
|---|---|---|
| list | Arrays, stacks, two pointers | List fundamentals GO; specific DSA patterns practised as needed |
| dict, set | Hashing and lookups | GO: collection tasks; dict applied in Two Sum and Group Anagrams |
| Counter, defaultdict | Frequency maps, grouping | Not assessed |
| deque | Queues, BFS, sliding windows | Not assessed |
| heapq | Heap problems | Not assessed |
| bisect | Binary search helpers | Not assessed |
| sorted, lambda | Custom sorting | GO: sorting exercises; sorted also used in Group Anagrams |
| functools.cache | Memoisation and DP | Not assessed |

Python traps to assess: mutable defaults, list aliasing, // division (including negative values), recursion depth, and complexity of common collection operations.

## Practical milestones

- [ ] Day 1–2: frequency counter and Two Sum in Python — Two Sum GO; standalone frequency counter not assessed.
- [ ] Day 3: Group Anagrams and one BFS problem in Python — Group Anagrams GO; BFS pending.
- [x] Day 4: small application split across multiple files — age_utils.py and app.py completed and run.
- [ ] Day 5: understand basic async/await; start a FastAPI task API with GET, POST, Pydantic validation and in-memory storage.
- [ ] Day 6–7: practise DSA, test API endpoints, fix observed gaps.
- [ ] Move into the Applied AI project; one DSA problem per day, most learning time on building.

## GO / NO-GO before FastAPI

**3/3 passed.**

| Gate | Required evidence | Result |
|---|---|---|
| DSA readiness | Implement Two Sum and Group Anagrams using dictionaries | GO: both implementations and explanations reviewed |
| Python language readiness | Small class, type hints, exceptions, and a function imported from another file | GO: Task/PriorityTask, annotated functions, parse_age and two-file import reviewed |
| Async understanding | Explain async/await and why blocking operations inside async functions cause problems | GO: coroutine/await code and blocking-versus-suspending explanation correct |

## Postponed topics

Learn when the project requires them: decorator implementation, generators/yield, context managers, advanced OOP/inheritance, metaclasses/descriptors, advanced asyncio, threading/multiprocessing, advanced internals, packaging/distribution.
Pick up *args, **kwargs, Pydantic, pytest and dependency injection while building FastAPI.

## Assessment log

| Date | Topic/task | Outcome | Gap / next step |
|---|---|---|---|
| 2026-10-11 | Setup discussion | No assessment yet | Project initialised and file ran; environment explanation pending |

## How to resume in a new chat

Ask the assistant to read **python-learning-progress.md** and **python-learning-notes.md** before continuing.
Use the current files as authoritative; do not reconstruct progress from memory.
Resume from “Current checkpoint”, check outstanding task evidence, and continue the explain → task → review loop.
When editing these files, update the same saved files rather than creating a new copy each session.


| 2026-10-11 | Python setup and uv | GO | Move to variables/basic types; practise dependency installation later |

Assessment: 2026-10-11 — Variables/basic types GO; five types correctly printed, int("45") + 15 produced 60, string/int TypeError correctly predicted.

Assessment: 2026-10-11 — Conditions/loops GO after corrections. enumerate(["A", "B"], start=5) correctly predicted as 5 A / 6 B.

Scope update: 2026-10-11 — Learner requested Python scopes. Added as topic 7 immediately after functions; total readiness topics 12. Existing completion preserved (3/12).

Assessment: 2026-10-11 — Sets and collections GO (4/12); runtime error from shadowing set corrected and understood.

Tracker correction: 2026-10-14 — Fixed stale exceptions/modules/imports checkbox and status to GO; aligned assessed collection/sorting helper rows and completed multi-file milestone. Verified 12 checked readiness rows. Additional DSA helpers, BFS and FastAPI milestones remain pending as intended.
