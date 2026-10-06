# Python Core

`python-core` is my structured repository for understanding **Python deeply as a programming language** before moving to frameworks such as FastAPI.

I am already a software developer with professional experience in:

- JavaScript
- TypeScript
- Node.js
- Java
- Spring Boot
- Backend development

This repository is therefore **not a beginner programming course**.

The goal is to understand what is unique about Python, how Python behaves at runtime, and why Python code works the way it does.

Where useful, Python concepts should be compared with **JavaScript, TypeScript, Node.js, or Java** to make differences easier to understand.

---

## Goal

By the end of this repository, I should be able to:

- Read Python code confidently
- Write idiomatic Python
- Debug Python-specific behaviour
- Understand Python's object and reference model
- Understand Python's execution model
- Understand functions as first-class objects
- Understand closures
- Understand decorators rather than treating them as magic
- Understand iterators and generators
- Understand modules and imports
- Understand Python's object model
- Understand type annotations
- Understand asynchronous Python
- Understand threads, processes and the GIL
- Understand practical Python memory behaviour
- Reason about Python code rather than memorising syntax

The objective is **not to learn every obscure Python feature before moving forward**.

The objective is to build a strong enough mental model that frameworks such as FastAPI make sense naturally.

---

## Existing Programming Background

I already understand general programming concepts from JavaScript, TypeScript, Node.js and Java.

These include:

- Variables
- Conditions
- Loops
- Functions
- Closures
- Classes
- Objects
- Inheritance
- Exceptions
- Collections
- APIs
- Backend development
- Asynchronous programming
- Promises
- Event-driven systems
- Unit testing

When these concepts appear in Python, the focus should be on:

- Python syntax
- Python-specific behaviour
- Differences from JavaScript / TypeScript
- Differences from Java
- Differences from Node.js runtime behaviour
- Python conventions
- Python's runtime model
- Common Python mistakes

---

## Repository Files

### `AGENTS.md`

Contains instructions for AI agents teaching from this repository.

Any agent should read this file before starting or continuing a lesson.

---

### `PYTHON_SYLLABUS.md`

Contains the ordered learning roadmap for Python.

The syllabus focuses on understanding Python itself rather than backend frameworks.

---

### `PROGRESS.md`

Tracks learning progress.

Suggested statuses:

```text
⬜ Not Started
🟡 Learning
🟠 Needs Practice
✅ Completed
```

A topic should only be marked complete after its important Python-specific behaviour is understood.

---

## Repository Structure

Directories should be created gradually as topics are learned.

```text
python-core/
│
├── 01_execution_model/
├── 02_objects_and_references/
├── 03_data_types/
├── 04_collections/
├── 05_pythonic_syntax/
├── 06_functions/
├── 07_scope_and_closures/
├── 08_modules_and_imports/
├── 09_exceptions/
├── 10_oop/
├── 11_python_data_model/
├── 12_dataclasses/
├── 13_iterators/
├── 14_generators/
├── 15_decorators/
├── 16_context_managers/
├── 17_typing/
├── 18_async/
├── 19_concurrency_and_gil/
├── 20_memory_management/
├── 21_internals/
├── 22_packaging/
├── 23_testing/
├── 24_performance/
│
├── AGENTS.md
├── PYTHON_SYLLABUS.md
├── PROGRESS.md
└── README.md
```

A topic directory may contain:

```text
README.md
examples.py
exercises.py
experiments.py
```

Only create files when they are useful for learning.

---

## Learning Style

The general learning loop is:

```text
Concept
↓
Python mental model
↓
Compare with JavaScript / TypeScript / Node.js / Java when useful
↓
Small example
↓
Predict behaviour
↓
My answer
↓
Explanation
↓
Exercise
↓
Review
↓
GO / NO-GO
```

The main question should be:

> Why does Python behave this way?

rather than:

> What syntax should I memorise?

---

## Useful Comparisons

Examples of comparisons that may help:

```text
JavaScript object references
vs
Python names and objects
```

```text
JavaScript closures
vs
Python closures + LEGB + nonlocal
```

```text
Java classes
vs
Python classes and method binding
```

```text
TypeScript types
vs
Python type annotations
```

```text
JavaScript Promise
vs
Python coroutine
```

```text
Node.js event loop
vs
Python asyncio event loop
```

```text
Promise.all()
vs
asyncio.gather()
```

Comparisons should only be used when they improve understanding.

---

## What This Repository Should Avoid

Do not spend significant time explaining generic concepts such as:

```python
if condition:
    ...
```

or:

```python
for item in items:
    ...
```

Instead, move quickly to Python-specific behaviour:

```python
for index, user in enumerate(users):
    print(index, user)

for key, value in data.items():
    print(key, value)
```

and explain:

- Iterables
- Unpacking
- `enumerate`
- Dictionary iteration
- Pythonic conventions

---

## FastAPI

FastAPI will be learned in a **separate repository**.

This repository should remain focused on Python itself.

Before starting FastAPI, I should understand:

- Python execution model
- Objects and references
- Mutability
- Identity vs equality
- Collections
- Functions
- Argument behaviour
- Scope and LEGB
- Closures
- Modules and imports
- Python OOP
- Python data model
- Iterators
- Generators
- Decorators
- Context managers
- Type hints
- Async Python
- Coroutines
- Event loop
- Threads
- Processes
- GIL
- Basic memory management

---

## Why Learn Python Before FastAPI?

When I eventually see:

```python
@app.get("/users")
async def get_users() -> list[User]:
    ...
```

I should already understand:

- `get_users` is a function object
- What `async def` means
- What calling an async function returns
- What `await` does
- What the event loop does
- What `list[User]` represents
- How annotations work
- What `@app.get(...)` means
- How decorators work
- How Python can inspect function signatures

At that point, I should be learning **FastAPI**, not Python fundamentals at the same time.

---

## FastAPI Readiness

Once the required concepts are understood:

```text
FASTAPI READINESS: GO
```

If important gaps remain:

```text
FASTAPI READINESS: NO-GO
```

Advanced or obscure Python topics should not block progress.

---

## Final Objective

The purpose of `python-core` is not:

> Learn enough Python syntax to build an API.

It is:

> Understand Python well enough that frameworks and libraries built on top of it make sense rather than feel like magic.

My existing experience with JavaScript, TypeScript, Node.js and Java should be used to accelerate the process without skipping important Python-specific behaviour.