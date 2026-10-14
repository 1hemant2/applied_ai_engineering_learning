# Python learning notes

Last updated: 14 October 2026 (India time)
Companion tracker: python-learning-progress.md

These are notes from actual discussions. Topics not yet discussed are not presented as completed learning.

## 1. Python setup and uv

### Question: What does “zsh: command not found: uv” mean?

The terminal shell, zsh, could not locate an executable called uv.
Usually uv is not installed; it may also be installed but absent from PATH.
PATH is the list of directories the shell searches for executable commands.

Observed user output:

```text
python --version
Python 3.14.7

uv --version
zsh: command not found: uv
```

Python is available through the user's python command. The displayed version is user-reported.
uv installation is not confirmed.

### Question: Is uv equivalent to npm, which manages Node packages?

Yes, as a starting comparison. Both manage project dependencies.
uv also manages Python virtual environments and can manage Python versions.
Python runs the code; uv manages the packages and environment used to run it.

| Node.js / npm | Python / uv | Meaning |
|---|---|---|
| node | python | Language runtime |
| npm init | uv init | Initialise project metadata |
| npm install express | uv add fastapi | Add a dependency; examples use different frameworks |
| package.json | pyproject.toml | Project metadata and declared dependencies; not identical formats |
| package-lock.json | uv.lock | Resolved dependency versions |
| node app.js | uv run python app.py | Run the program; uv selects the project environment |

### What is a virtual environment?

Each Python project can have its own environment containing its installed packages.
One project can use a different FastAPI version from another without changing the other's packages.

A .venv directory is commonly used for this environment. It is not a direct equivalent of node_modules: it also contains environment-specific executables and Python environment configuration.
This distinction is a reference clarification; it has not been assessed yet.

### Installation command provided

Official macOS/Linux installer:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Close and reopen the terminal after installation, then check:

```bash
uv --version
```

Source: [Official uv installation documentation](https://docs.astral.sh/uv/getting-started/installation/)

Status: command provided; successful installation not yet reported.

## 2. Important learning decisions

- Learn just enough Python to begin FastAPI and DSA.
- Aim for 5–7 focused days, but allow extra time when understanding needs it.
- Cover one topic at a time, followed by a practical assessment.
- Mark completed only after reviewing demonstrated understanding.
- Begin familiar DSA problems once collections and functions are ready.
- After readiness: one Python DSA question per day, with most time on FastAPI and Applied AI systems.

## 3. Mistakes and corrections

No learner coding mistakes reviewed yet.
The missing uv command is a setup issue, not a failed Python concept assessment.

## 4. Future note format

Append a section after each meaningful discussion:

- Date and topic.
- Learner's important question.
- Explanation and a small example when useful.
- Submitted task and reviewed result.
- Mistake or misconception and its correction, if any.
- GO / NO-GO and what still needs practice.

Keep explanations here and current progress in the companion tracker.
Record useful commands without secrets, credentials, or private company code.


## 5. pip versus uv (11 October 2026)

Question: pip also manages Python packages, so what is different about uv?

pip primarily installs and uninstalls packages in a Python environment. uv includes package installation plus project dependency declarations, lockfiles, virtual environment management and Python version management. Both can install packages from PyPI. uv is a separate tool, not a wrapper around pip.

- pip example: `python -m pip install fastapi` installs FastAPI into the selected Python environment.
- uv project example: `uv add fastapi` declares FastAPI in pyproject.toml, updates uv.lock and installs it into the project environment.
- `uv pip install fastapi` provides a pip-style installation interface, but does not declare the dependency in pyproject.toml like uv add does.

For our learning project, use uv's project commands consistently. Recognise pip commands when reading tutorials. No need to install the same dependency using both tools.

Sources:
- https://pip.pypa.io/en/stable/
- https://docs.astral.sh/uv/guides/projects/
- https://docs.astral.sh/uv/getting-started/features/

Assessment status: explained, not tested. Setup remains in progress.

## 6. Runtime and environment checks (11 October 2026)

- Asked which tool executes `print("Hello")`: learner correctly answered Python.
- Asked whether `uv add fastapi` in Project A makes it available in Project B: learner correctly expected separation, but linked it to sibling folders and global installation.
- Correction: package availability depends on the Python environment used, not folder relationships. Separate project environments isolate packages. Installing into a global Python environment does not normally expose packages to isolated virtual environments. Environments can explicitly opt into system packages, but that is outside our current workflow.
- Concept check: GO for basic runtime/package separation, with environment-versus-folder correction explained. Whole setup topic remains incomplete; uv installation and practical project task are pending.

## 7. uv installation and PATH resolved (11 October 2026)

- Installer placed uv and uvx in `/Users/hemant/.local/bin`.
- Current zsh session initially still reported command not found.
- `source "$HOME/.local/bin/env"` loaded the installer-created shell configuration into the current shell. `$HOME` expands to the home directory; this configuration adds the installation directory to PATH. It does not reinstall uv.
- PATH lists directories searched for executable commands.
- User confirmed working output: `uv 0.13.0 (4ecd0eff2 2026-10-09 aarch64-apple-darwin)`.
- Installation substep complete. Entire setup topic awaits practical project exercise.

Next exercise: in a personal workspace, run `uv init python-learning`, enter that directory, edit main.py to print `Hello, Hemant`, then run `uv run python main.py`. Share code/output and explain the purpose of pyproject.toml and .venv.

## 8. First project and successful execution (11 October 2026)

- Learner chose existing `applied_ai_engineering/python_core` folder, rather than a new python-learning folder.
- Ran `uv init` in it; output: `Initialized project python-core`.
- Ran `uv run python src/python_core/__init__.py`; output: `Hello, Hemant`.
- Practical execution substep: GO. Full source has not been reviewed.
- The observed file is __init__.py. It can be executed directly but normally marks/initialises a regular Python package. Future standalone exercises should use separate .py files; explain imports/packages later.
- Remaining concept check: pyproject.toml contains project metadata and dependency declarations; .venv contains the isolated Python environment and installed packages. Ask learner to explain this distinction before full setup GO.

## 9. .venv, .env and project metadata (11 October 2026)

- Asked whether .venv is like .env. Explained: .venv is a directory containing the Python environment and installed packages; .env is a text file for application configuration such as database URLs and API keys.
- Learner correctly answered that installed FastAPI goes in .venv.
- Asked what pyproject.toml is for. It declares project metadata, Python requirements and dependencies; roughly equivalent to package.json.
- uv.lock records exact resolved dependency versions, roughly like package-lock.json.
- Learner asked if .venv is like node_modules. Yes for installed package storage, but it also includes isolated Python environment setup. Normally exclude .venv from Git; other developers recreate it from declared dependencies and the lockfile.
- Learner asked to proceed. Setup: GO based on successful installation/run and basic concept checks. Dependency installation is explained but not yet practised.

## 10. Variables and basic types — next lesson

Planned scope: assignment without let/const or Java declarations; int, float, str, bool, None; dynamic typing (names can be rebound to different object types); type(); explicit int/float/str conversion; f-strings. Python does not implicitly concatenate strings and integers using +.

Task: create basics.py with name (str), experience_years (int), learning_python (bool), daily_hours (float), project_name (None); print each value and its type; convert string "45" to int and add 15; print a greeting with an f-string. Prediction check: x = 10; x = "10"; explain final type and whether x + 5 works. Review before GO.

## 11. Variables and basic types assessment (11 October 2026)

- First submission correctly assigned name, experience, daily_hours, is_learning and project, and formatted them with an f-string. Initially omitted type printing and conversion task; requested those remaining parts.
- Correctly predicted x = 10; x = "10"; x + 5 causes runtime TypeError because x refers to a string.
- Follow-up printed str, int, float, bool and NoneType correctly. `num = "45"; print(int(num) + 15)` produced 60.
- Result: GO. Variables/basic types complete (2/11 overall).
- Python does not require trailing semicolons; None has type NoneType. int(num) returns an integer and does not change the original num string.

## 12. Conditions and loops — next lesson

Scope: colon and indentation define blocks; if/elif/else; and/or/not; for iterates values; range stop is exclusive; enumerate yields index/value pairs; while and +=.
Task: print 1–10 with even/odd labels using for/range/if; sum 1–10; enumerate ["Python", "FastAPI", "DSA"] starting at 1; while countdown 3 to 1; if/elif/else classify score 75 using >=80 Excellent, >=50 Pass, otherwise Retry. Predict list(range(2, 8, 2)). Review before GO.

## 13. Conditions and loops assessment (11 October 2026)

- Predicted list(range(2, 8, 2)) as 2, 4, 6; exact displayed list is [2, 4, 6]. Stop is exclusive.
- Even/odd loop, while countdown and score classification were correct.
- Initially printed sum instead of total. Output was <built-in function sum> because sum is a built-in name. Corrected print(total) produced 55.
- Initially printed only languages, then indices starting at 0. Explained enumerate defaults to 0 and start=1 produces requested numbering.
- Correctly predicted enumerate(["A", "B"], start=5) output: 5 A / 6 B.
- Initially shared truncated output; later complete run confirmed the programme continued. Exact cause of truncation was not established. When output and pasted source differ, save the file and use cat loop.py to inspect what actually runs.
- Result: GO, 3/11 complete. Logical operators were explained but not separately tested.

## 14. Lists — next lesson

Lists are ordered, mutable collections, roughly like JS arrays / Java ArrayList. Cover zero-based and negative indexing, exclusive-stop slicing, append, pop, len, membership and iteration. append/pop modify the list; slices produce a new shallow list (reference/copy depth comes later).
Task with nums = [10, 20, 30, 40, 50]: print first and last, slice [20, 30, 40], append 60, replace 20 with 25, pop and print removed last value, print length, check membership of 30, and loop over remaining items. Predict nums[1:4] and nums[-2] for the original list before changes.

## 15. Lists submission and Python conversion syntax (11 October 2026)

- Correctly used nums[1:4], append(60), nums[1] = 25, pop(), len(), membership and iteration. Reported output matched these operations.
- Incorrect first statement: print("0th: " + (str)nums[0]). Python conversion is a function call str(nums[0]), not Java-style (str)value casting.
- Incorrect second statement: print("last: + " (str)nums[0]). Missing valid concatenation/call structure and used index 0 for last. Correct target is nums[-1], formatted with str() or an f-string.
- Explain SyntaxError occurs while parsing the file before execution. A file containing these syntax errors cannot run later lines in the same execution; later output must be from a version excluding/fixing them or a separate execution.
- Remaining list task: first/last printing and directly printing remaining list. Await revised source/output before GO.
- New learner preference: all future coding tasks must be paste-ready code blocks with commented questions, starter data and TODOs.
- Learner also requested adding a topic to syllabus/tracker, but did not specify its name. Ask for clarification, then place it in the appropriate order. Do not invent the requested topic.

## 16. Added scope to syllabus (11 October 2026)

Learner clarified the requested new topic: how Python handles scopes. It was not explicit in the original syllabus. Added immediately after functions, before comprehensions; checklist now 12 topics, with 3 passed.

Planned scope: LEGB name lookup (Local, Enclosing, Global, Built-in), function-local names, module-global names, if/for/while not creating separate scopes, shadowing built-ins (connecting to earlier sum issue), reading versus assigning globals, UnboundLocalError, global and nonlocal. Comprehensions have their own scope; explain that distinction during the following comprehension lesson.

Short preview: `if True: message = "Hello"` at module level leaves message available after the if block. Unlike JS let/const, if/for/while blocks do not create a separate variable scope. Scope lesson itself is not completed; finish collections first.

## 17. Lists final check — GO (11 October 2026)

Learner submitted correct code:
```python
nums = [10, 25, 30, 40, 50]
print(f"first: {nums[0]} last: {nums[-1]}")
print(nums)
print(len(nums))
```
Expected output: first: 10 last: 50; [10, 25, 30, 40, 50]; 5. Final output not submitted; reviewed code is sufficient. Lists GO. Overall checklist remains 3/12 because tuples, dictionaries and sets are part of the same collections topic.

## 18. Tuples — next lesson

Tuples are ordered collections whose item slots cannot be changed. They support indexing, negative indices, slicing, len, iteration and unpacking; no append/pop or item assignment. A tuple may contain mutable objects, whose contents can still change; discuss during mutability. A singleton tuple needs a trailing comma: (42,); (42) is int.
Task: profile = ("Hemant", 2, "Python"); print first/last and length; unpack to name/experience/language; format a sentence; create one-item tuple containing "FastAPI" and print type; predict profile[1] = 3 and explain why.

## 19. Tuple use cases and assessment — GO (11 October 2026)

- Learner asked why tuples instead of lists. Explained fixed groups such as coordinates/dimensions, and tuples as dictionary keys when all contents are hashable. Lists cannot be dictionary keys.
- Clarified nested mutability: a tuple's slots cannot change, but an inner list can be modified.
- Submitted correct indexing, tuple unpacking and f-string, and framework = ("FastApi",). Correctly predicted item assignment TypeError.
- Initially omitted len(profile) and printing whole tuple/type. Supplied correction lines; no rerun submitted.
- Correctly answered that framework = ("FastApi") has string type without the comma.
- Result: GO for tuple fundamentals, based on demonstrated core understanding. Overall remains 3/12 until dictionaries and sets are completed.

## 20. Dictionaries — next lesson

A dict maps unique hashable keys to values, roughly like a JS Map / Java HashMap. Python dicts preserve insertion order. d[key] raises KeyError for absent keys; d.get(key, default) returns a fallback (None if omitted). d[key] = value adds or updates a key. key in d checks keys. d.items() yields key/value pairs; del d[key] removes a key.
Task: learner = {"name": "Hemant", "experience": 2}; print name, change experience to 3, add language Python, get city with fallback Unknown, check language key, iterate items, print len, delete experience and print dict. Prediction: learner["city"] versus learner.get("city").

## 21. Dictionaries assessment — GO (11 October 2026)

- Correct code for key access, update, adding a key, get fallback, membership, items iteration, len and deletion. Deletion output omitted; explained that del does not print and provided print(learner) for inspection.
- Initially predicted absent-key direct access as TypeError. Corrected to KeyError. Follow-up correctly identified data["missing"] as KeyError and data["count"] + "1" as TypeError (incompatible int and str).
- Initial error stack included node:internal and Node.js v26.1.0: Python source was being run by Node. Running uv run python dictionaries.py resolved this. Editor runner choice was not independently inspected.
- Python run output confirmed name Hemant, fallback unknown, True membership, three key/value pairs with experience 3, and length 3.
- Result: Dictionaries GO. Overall 3/12 until sets complete.

## 22. Sets — next lesson

Sets contain unique hashable values, support membership and add/discard/remove, do not support indexing and do not guarantee iteration order. Empty set is set(); {} is an empty dict. discard of absent element does nothing; remove raises KeyError. Operators: | union, & intersection, - difference.
Task: numbers = [1,2,2,3,3,4]; create set, print len, check 3, add 5, discard 2, discard absent 99; a={1,2,3}, b={3,4,5}; print union/intersection/a-b; create empty set and print type. Predictions: type({}) and a[0].

## 23. Sets assessment and built-in shadowing — GO (11 October 2026)

- Initial code used set = set(), which created an instance then shadowed the built-in class. Later set() raised runtime TypeError: set object is not callable. Earlier lines had executed, so this was not a compile/parse-time error.
- Renamed variable unique_num and used set(numbers) directly. Correct add/discard, membership, union/intersection/difference and empty-set creation.
- Follow-up still used print(set), displaying <class 'set'> rather than stored values; explained print(unique_num).
- Correctly explained set is the built-in class, whereas unique_num holds the created set.
- Correct predictions: {} is dict; indexing a set raises TypeError; discard missing value does nothing.
- Initial set/length print statements were omitted; supplied corrections. No final rerun required for core concept GO.
- Sets GO; collections complete. Overall 4/12 passed.

## 24. Object references and mutability — next lesson

Names refer to objects. Assignment does not copy. list/dict/set are mutable; int/float/str/bool/None/tuple are immutable (tuple contents can include mutable objects). Mutation changes an object; rebinding changes which object a name refers to. == compares values; is compares identity. Use is None for None checks, not is for numeric/string equality. list.copy() creates a shallow copy; nested mutable objects remain shared.

Prediction task before running: A a=[1,2]; b=a; b.append(3); print(a,b,a is b). B x=10; y=x; y+=5; print(x,y). C a=[1,2]; b=a.copy(); b.append(3); print(a,b,a==b,a is b). D a=[[1,2],[3,4]]; b=a.copy(); b[0].append(99); print(a,b,a is b,a[0] is b[0]). Ask for explanations and outputs; do not advance without demonstrated understanding.

## 25. References and mutability assessment — GO (12 October 2026)

All four predictions correct: A both lists [1,2,3] and identity True; B integers 10 and 15; C original [1,2], copy [1,2,3], equality False and identity False; D both nested lists reflect 99, outer identity False and inner identity True. Predictions and reasons reviewed; no execution output supplied, predictions sufficient for this assessment.

Clarified C wording: .copy() is not general copying by value; it creates a new outer list and copies references to the same elements. append changes only the new outer list. Shared immutable integers cannot be mutated. Learner already correctly understood this shallow-copy behaviour in D.

Result: GO; overall 5/12.

## 26. Functions and arguments — next lesson

Initial scope: def, indentation, return versus print, implicit None return, positional and keyword arguments, defaults and required arguments before default arguments. Defaults are evaluated at definition time; mutable-default pitfall will follow after initial function tasks and before full topic GO.

Task: add(a,b) returns sum; greet(name,language="Python") returns formatted greeting; count_even(numbers) loops to return even count; invoke greet positionally and by keyword. Predict function show_message(): print("Hello"); result=show_message(); print(result) as Hello then None.

## 27. Functions: return versus print corrected (12 October 2026)

- Submitted correct add(a,b), greet(name,language="Python") and count_even(numbers).
- Java greet call used positional arguments, although keyword call requested. Explained greet(name="Hemant", language="Java"); await learner demonstration.
- Initially thought show_message printing Hello returned/stored Hello. Explained a function without return returns None, while print displays text.
- Correctly predicted double(5) with only print produces 10 and Answer: None. Then correctly rewrote double(number): return number * 2; res=double(5); print(res).
- Basic return understanding GO. Entire functions topic pending mutable-default assessment and keyword-call demonstration.

## 28. Mutable default arguments — next lesson

Default argument expressions are evaluated when def executes, rather than fresh for each call. A default list is reused by calls that omit the argument. Example add_item(item, items=[]): items.append(item); return items. Separate printed calls add_item("A"), add_item("B") show ["A"] then ["A", "B"].

Safe pattern: items=None; if items is None: items=[]; then append and return. Only allocate when omitted/None, preserving explicitly provided lists (even empty lists).

Task: predict calls add_tag("python"), add_tag("fastapi") with tags=[]; rewrite using None; show independent default calls; supply existing=["backend"] using keyword tags=existing and explain existing changes. This also checks keyword argument syntax.

## 29. Functions and mutable defaults — GO (12 October 2026)

- Correctly predicted default-list accumulation and explained defaults evaluated at function definition, not on each call. Exact output is ['python'] then ['python', 'fastapi'].
- Submitted safe tags=None function creating [] only when None; used == None, which works for this case, but advised idiomatic is None.
- Correct explanation that passing existing lets function append to same list object.
- Keyword requirement initially missed; final correct call add_tag_safe(tags=existing, tag="python") demonstrated named parameters in reverse order. Expected existing ['backend', 'python']; no output supplied for final call.
- Functions and arguments GO; overall 6/12.

## 30. Scope — initial lesson

LEGB lookup: Local, Enclosing function, Global module, Built-in. Function parameters/assigned names are local unless declared global/nonlocal. Local names can shadow globals without changing them. if/for/while do not create separate scopes. Assignment anywhere in a function normally makes the name local throughout that function; reading before local binding raises UnboundLocalError. Reading a global without local assignment works. Global/nonlocal will follow after initial assessment.

Paste-ready prediction tasks: global language Python, local language Java -> prints Java then Python; global score=10 read inside function -> 10; if block assigns message Ready -> accessible afterward; function reading count then assigning count=2 -> UnboundLocalError despite outer count=1. Consider cases separately. Explain static local-name classification.

## 31. Scope assessment and corrections — GO (12 October 2026)

- Initial local shadowing and global read predictions correct. Initially predicted if-block assignment unavailable; corrected: if/for/while do not introduce scopes. Correctly predicted loop last=20 and recognised function-local status inaccessible outside.
- Understood reading count before local assignment fails; corrected error spelling to UnboundLocalError. Distinction: missing name lookup -> NameError; unbound function-local name -> UnboundLocalError.
- Requested slower explanation of local/nonlocal. Used nested functions: inner local score=9 leaves outer score=5; nonlocal score updates enclosing score to 9. Learner correctly explained using existing enclosing variable.
- Correctly predicted nonlocal with module score=100 -> outer 9, module 100; global version -> outer 5, module 9. Clarified nearest enclosing function binding versus module binding.
- Correct append prediction ['Python']; explained mutation needs no global declaration because it does not rebind items.
- Final correct prediction: function items=["Python"] leaves module items=["Java"] unchanged because local assignment.
- Result: scope GO. Overall 7/12.

## 32. Comprehensions — next lesson

List comprehension [expression for item in iterable if condition] is a concise way to build a new list, comparable to JS map/filter. Dict comprehension {key_expression: value_expression for item in iterable}. In Python 3, comprehension loop variables do not leak into surrounding scope, unlike normal for loops.
Task: nums=[1,2,3,4,5,6]; squares; evens; squares of evens; word_lengths from words=["Python","API","backend"]; predict x=99; values=[x*2 for x in [1,2,3]]; print(values); print(x). Sorting/lambda follow this assessment.

## 33. Comprehensions assessment — GO (12 October 2026)

Correct squares, even filter, squared evens and word-length dict comprehensions. Correctly predicted values=[2,4,6] and outer x remaining 99; understood comprehension loop variable scope. Omitted printing evenSquare/wordLenMap; code correct, no extra printing assessment needed. Suggested snake_case naming as convention (even_squares, word_lengths).

Comprehensions GO; combined checklist item still pending sorting/lambda. Overall remains 7/12.

## 34. Sorting and lambda — next lesson

sorted(iterable) returns a new sorted list without changing original; list.sort() mutates list and returns None. reverse=True means descending. key=function computes each item's comparison value, e.g. key=len or key=lambda user: user["age"]. Python key functions differ from JS comparator callbacks: return a sort key, not an a/b comparison. Lambda is an anonymous function limited to a single expression, whose value is returned.

Task: sorted nums ascending/descending and show original; words sorted by length using key=len; users sorted by experience using lambda; define lambda double; predict result of nums.sort() and original list.

## 35. Sorting and lambda assessment — GO (13 October 2026)

- Ascending sorted, descending reverse=True, key=len correct initially. User sort by experience omitted reverse=True; clarified descending. Standalone unused lambda unnecessary.
- Explained Python key extracts one value per item (e.g. experience), unlike JS two-item comparator returning ordering result.
- Initially confused .sort() with sorted(). Corrected: sorted returns new list preserving original; list.sort modifies list and returns None.
- Follow-up lambda had erroneous comma after lambda and lowercase true; corrected key=lambda product: product["price"], reverse=True. Numeric predicted output had typo [4,2,2]; clarified sorting preserves values.
- Final independent check correct: sorted(words, key=lambda word: len(word), reverse=True). Correct predictions for numbers=[9,1,5]: original unchanged, ordered=[1,5,9].
- Result: combined comprehensions/sorting/lambda topic GO. Overall 8/12.

## 36. Type hints — next lesson

Annotations describe intended types for readers/tools; Python does not automatically enforce or convert them. Syntax name: str, def f(a: int) -> int; collections list[int], dict[str,int]; str | None allows None, with =None separately specifying default; -> None for no useful returned value. Frameworks such as FastAPI/Pydantic may inspect annotations for validation, separate from Python itself.

Task: annotated add(a,b); count_even(numbers:list[int])->int; word_lengths(words:list[str])->dict[str,int]; greet(name:str,prefix:str|None=None)->str with None fallback; predict annotated label:int="hello" print(label) and explain annotations versus runtime validation.

## 37. Type hints assessment — GO (13 October 2026)

- Correct annotated add and count_even, and prediction that value:int="hello" prints hello without automatic runtime rejection.
- word_lengths initially used wl:dict[str,int] without assignment, then accessed wl. Explained annotation alone does not initialise; causes UnboundLocalError here.
- Correct final rewrite initialises wl:dict[str,int]={}, iterates words, assigns lengths and returns wl. Included test call for ["Python","API"]; no execution output supplied, code sufficient.
- Correct greet(name:str,prefix:None|str=None)->str handles None and custom prefix. None|str is valid. Unused fullName:str annotation should be removed.
- Result: GO, 9/12 overall.

## 38. Classes and objects — next lesson

Class defines objects with attributes/methods. __init__ initialises newly created instance; self is explicit current-instance parameter, analogous to this (conventional name, not keyword). Calling user.method() automatically passes user as self. Assign instance state using self.name; local name alone does not store an attribute. __init__ -> None.

Task: class Task with __init__(title:str) storing self.title and self.completed=False; complete(self)->None sets completed True; describe(self)->str formats title/completed. Create two tasks, complete only first, print both descriptions and confirm independent state. Basic inheritance/super follows this exercise.

## 39. Classes and inheritance assessment — GO (13 October 2026)

- Asked if __init__ is like constructor and why self supplied. Explained object created first then initialised, explicit self analogous to implicit Java this; Python supplies it automatically.
- Correct Task with instance title/completed, complete and describe; initially extra Learn prefix corrected. Understood completing task1 doesn't affect separate task2.
- Correct PriorityTask(Task), super().__init__(title), own priority and inherited complete. Initially used super.title/super.completed and string priority despite int annotation. Corrected self attribute access and integer 1.
- Correctly explained parent initialiser acts on same PriorityTask instance, not separate parent object. Clarified inheritance declared by class header; super calls inherited implementation.
- Final full code and output reviewed: Learn Python completed True, Build API completed False, PriorityTask Build API completed True priority 1.
- Classes GO, overall 10/12.

## 40. Exceptions — next lesson

try runs potentially failing code; except catches matching exception; as error binds exception object; raise creates/propagates an error and stops normal execution of current function until handled. Catch specific types, not a bare except. int("abc") raises ValueError.

Task: parse_age(text:str)->int converts with int(), raises ValueError("Age cannot be negative") for negative result, returns valid age. Loop test strings ["25","abc","-3"], call inside try, print age on success, catch ValueError as error and print useful error; print Finished after loop. Predict return after unconditional raise unreachable. Modules/imports follow exceptions assessment.

## 41. Exceptions assessment — GO (13 October 2026)

Correct parse_age converting int, raising ValueError for negative, and returning valid age. Correct try/except ValueError inside loop so failed input doesn't skip later values; Finished after loop. Correct reject prediction: raise interrupts function and return 10 is not reached. Code reviewed, no output supplied; sufficient for GO. Whole checklist remains 10/12 while modules/imports pending.

## 42. Modules and imports — next lesson

A .py file can be imported as a module. import age_utils uses age_utils.parse_age; from age_utils import parse_age binds function name directly. Use module name without .py. Module's top-level code executes on initial import; functions' bodies execute when called. __name__ is __main__ when directly run, module name when imported. Guard if __name__ == "__main__": prevents script/demo code running on import.

Task: place parse_age in age_utils.py, demo print(parse_age("30")) behind main guard; app.py imports function, tests ["25","abc","-3"] with per-input try/except. Run uv run python app.py and uv run python age_utils.py. Explain whether 30 appears when running app.py and why.

## 43. Modules/imports and main guard — GO (13 October 2026)

Requested clarification of top-level execution and __name__. Explained direct starter file labelled __main__, imported module labelled age_utils; guard skips demo when imported. Learner correctly explained app is main so imported age_utils demo does not run.

Correct two-file code with from age_utils import parse_age and guarded print(parse_age("30")). Filename in message initially age_util.py but import age_utils; flagged mismatch. Actual commands succeeded, confirming intended import available. Outputs app.py: 25, invalid-literal error for abc, negative-age error; age_utils.py: 30.

Exceptions/modules/imports GO, overall 11/12.

## 44. JSON — next lesson

JSON is a text format, not a Python dict. json.dumps(object) serialises to str, json.loads(text) parses to Python values. Like JS JSON.stringify/parse. JSON object->dict, array->list, true/false->True/False, null->None. JSON keys are strings. Invalid JSON raises json.JSONDecodeError. Python JSON module is standard library, no uv add needed.

Task: user={"name":"Hemant","learning":True,"project":None}; dumps and print text/type; loads and print value/type; access restored name; catch JSONDecodeError for '{"name": "Hemant",}' (trailing comma). Prediction json.loads('{"active": true, "score": null}') types bool and NoneType. Async follows this assessment.

## 45. JSON assessment — GO (13 October 2026)

- Correct serialisation dumps to str, parsing loads to dict, and restored name access.
- Initially used dumps on malformed JSON string; explained this serialises the string itself rather than parsing contents. Corrected to loads and catch JSONDecodeError.
- Initially predicted values true/None when type output requested; clarified bool and NoneType.
- Correct independent check: loads('{"count":3}'), access count, add 2, print (expected 5). No final execution output submitted; code reviewed sufficient.
- JSON GO, combined final topic still pending async; overall 11/12.

## 46. Async/await — next lesson

async def defines coroutine function. Calling it returns coroutine object without immediately running its body, unlike JS async invocation. await runs/awaits coroutine and gets result; suspension while waiting allows event loop to run other scheduled tasks. Does not automatically parallelise code or make CPU work faster. asyncio.run(main()) is script entry point; frameworks run loop themselves. Sequential awaits remain sequential; concurrent scheduling later. await asyncio.sleep non-blocking versus time.sleep blocking current thread/event loop.

Task: async fetch_message(name:str)->str awaits asyncio.sleep(1), returns greeting. async main awaits function, stores/prints result; entry guard asyncio.run(main()). Predict sequential two calls with one-second sleep ~2 seconds. Explain why time.sleep(1) in async function blocks other tasks on that loop thread.

## 47. Async and Node.js comparison — GO (14 October 2026)

- Requested comparison with Node event loop and threads. Explained shared cooperative event-loop idea; Python async function call creates a coroutine without starting body, unlike JS async call which starts immediately until await. create_task schedules on loop, does not create thread. Python supports threads/processes; typical asyncio loop tasks run on one thread.
- Correct fetch_message async function waits asyncio.sleep(1), returns greeting; main awaits, stores/prints; asyncio.run inside main guard. Code reviewed; no execution output provided.
- Correct answers: call without await returns coroutine; time.sleep blocks thread and tasks on same loop cannot progress.
- Predicted sequential two awaits about 2 seconds, initially explained thread slept twice. Corrected: only coroutine suspended, not thread; second await starts after first completes.
- Final explicit understanding: other scheduled task can run because only current coroutine is suspended.
- Result: async and final combined topic GO. 12/12 completed. Readiness gates 2/3: language GO, async GO, DSA pending.

## 48. Final DSA readiness — next task

Two Sum in Python using dict, returning distinct indices with expected O(n) time and O(n) space. Define no-pair result []. Tests [2,7,11,15],9; [3,2,4],6; [3,3],6; [1,2,3],10. Explain why same element not reused; print results and analyse complexity. Then Group Anagrams. Remaining standard-library DSA helpers learned alongside problems, not new prerequisites.

## 49. Two Sum assessment — GO (14 October 2026)

Submitted correct dict solution: check hm.get(target-ele)==None, store ele->index if absent, otherwise return current and earlier index. Reverse output index order is valid. Expected O(n) time and O(n) space correct. Suggested complement not in hm as clearer membership test; None comparison works because stored values are integer indices.

Initial explanation that single traversal prevents same-index reuse incomplete. Explained lookup-before-insertion means only earlier indices exist. Learner correctly explained [3], target 6 yields [] and inserting first could yield same index twice. Two Sum GO; no execution output submitted, code reviewed sufficient. DSA gate still pending Group Anagrams.

## 50. Group Anagrams — next task

Use dict grouping words by canonical sorted-character signature. sorted("eat") returns ['a','e','t']; tuple(sorted(word)) is hashable when characters are strings, so can be dict key (list can't). Alternative "".join(sorted(word)) gives "aet". Dict values hold lists of words; list(groups.values()) returns list of those lists. Preserve duplicate words. Tests ["eat","tea","tan","ate","nat","bat"], [""], ["a","a"], []. Explain why signatures agree for anagrams and time complexity in n words/k max length.

## 51. Group Anagrams and final readiness — GO (14 October 2026)

- Initial implementation used sorted(word), a list, as dict key; runtime TypeError unhashable list. Explained joined string key or hashable tuple.
- Also corrected missing group initialisation and dictionary iteration: hm.items() needed for key/value unpacking.
- Final implementation uses "".join(sorted(word)), initialises absent key with [], appends originals, iterates items and returns groups. Handles empty input/string and duplicate words by code review; no final output provided.
- Correct complexity O(n*k log k) for sorting signatures.
- Initially explained abb/ab different because different words; clarified character counts, not word identity. Final independent check correctly identified abb/bab -> abb and matching sorted signatures.
- Group Anagrams GO. 12/12 syllabus topics and 3/3 readiness gates passed. Begin FastAPI; continue DSA practice in Python.

## 52. FastAPI transition

Separate project planned beside python_core: from applied_ai_engineering run uv init fastapi-learning; cd fastapi-learning; uv add "fastapi[standard]". Installation not yet confirmed. First endpoint lesson next; development command uv run fastapi dev main.py. Sources: https://fastapi.tiangolo.com/fastapi-cli/ and https://fastapi.tiangolo.com/tutorial/first-steps/ .
