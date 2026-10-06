# Python Syllabus

This syllabus is designed to build a strong understanding of **Python itself** before moving to FastAPI.

I already have experience with:

- JavaScript
- TypeScript
- Node.js
- Java
- Spring Boot

Generic programming concepts should therefore move quickly.

The focus should be on Python-specific behaviour and runtime concepts.

---

# Priority Levels

## Priority 1 — Understand Deeply

Fundamental to reasoning correctly about Python.

## Priority 2 — Understand Practically

Important for real Python development but does not require extreme depth.

## Priority 3 — Learn Later

Useful advanced material that should not block FastAPI.

---

# Phase 1 — Environment and Python Execution

**Priority: 1**

Cover:

- Python installation
- Python versions
- Python interpreter
- REPL
- Running `.py` files
- CPython
- Source code execution
- Compilation to bytecode
- Python virtual machine conceptually
- Statements vs expressions
- Runtime execution
- Namespaces
- Stack frames at a high level

Environment:

- `uv`
- Virtual environments
- Dependency installation basics

Goal:

Understand what happens between writing a Python file and Python executing it.

Do not go into CPython C source.

---

# Phase 2 — Names, Objects and References

**Priority: 1**

Cover deeply:

- Everything in Python is an object
- Variables are names
- Names reference objects
- Assignment
- Reassignment
- Identity
- Value
- Type
- `id()`
- `is`
- `==`
- Aliasing
- Shared references
- Mutable objects
- Immutable objects
- Mutation vs reassignment
- Passing objects to functions

Compare where useful with JavaScript object references and Java references.

## Copying

Cover:

- Assignment vs copying
- Shallow copy
- Deep copy
- `copy.copy`
- `copy.deepcopy`

---

# Phase 3 — Core Data Types

**Priority: 2**

Move quickly through syntax.

## Numbers

- `int`
- `float`
- Arithmetic
- `/`
- `//`
- `%`
- `**`
- Numeric conversion
- Python integer behaviour

## Strings

- Strings
- Immutability
- Indexing
- Slicing
- String methods
- f-strings

## Booleans

- `True`
- `False`
- Truthy values
- Falsy values
- `and`
- `or`
- `not`
- Short-circuit behaviour

Focus on behaviour that differs from JavaScript or Java.

---

# Phase 4 — Collections

**Priority: 1**

## Lists

- Creating lists
- Indexing
- Slicing
- Mutability
- Common methods
- References inside lists
- Copying lists

## Tuples

- Tuple syntax
- Immutability
- Packing
- Unpacking
- Single-element tuples
- Practical use cases

## Dictionaries

- Keys
- Values
- Access
- Mutation
- Iteration
- `.keys()`
- `.values()`
- `.items()`
- Dictionary ordering
- Hashability

## Sets

- Sets
- Uniqueness
- Membership
- Set operations
- Hashability

Understand deeply:

- Mutable vs immutable
- Hashable vs unhashable
- Why dictionary keys must be hashable
- Why sets provide efficient membership checks

Compare with JavaScript `Array`, `Object`, `Map`, `Set` and Java collections where useful.

---

# Phase 5 — Pythonic Syntax and Control Flow

**Priority: 2**

Move quickly through:

- `if`
- `elif`
- `else`
- `for`
- `while`
- `break`
- `continue`

Focus more on:

- Chained comparisons
- Conditional expressions
- `range`
- Iterating directly over collections
- `enumerate`
- `zip`
- `any`
- `all`

## Slicing

Cover:

```python
values[start:stop:step]
```

Include:

- Negative indexing
- Reverse slicing

## Packing and Unpacking

Cover:

```python
a, b = values
```

```python
first, *middle, last = values
```

## Comprehensions

- List comprehensions
- Dictionary comprehensions
- Set comprehensions
- Conditions
- Nested comprehensions

Focus on readability and Pythonic usage.

---

# Phase 6 — Functions

**Priority: 1**

Do not teach what a function is.

Focus on how **Python functions work**.

Cover:

- Functions are objects
- Assigning functions to names
- Passing functions
- Returning functions
- Function attributes
- Multiple return values

## Arguments

Cover deeply:

- Positional arguments
- Keyword arguments
- Default arguments
- Positional-only arguments
- Keyword-only arguments
- `*args`
- `**kwargs`
- Argument unpacking

Compare with JavaScript rest/spread syntax where useful, but explain the differences clearly.

## Mutable Default Arguments

Understand this deeply:

```python
def add(item, items=[]):
    items.append(item)
    return items
```

Understand why the same default object can survive across calls.

---

# Phase 7 — Scope and Closures

**Priority: 1**

Cover:

- Namespace
- Local scope
- Enclosing scope
- Global scope
- Built-in scope
- LEGB
- `global`
- `nonlocal`

## Closures

Cover:

- Nested functions
- Captured variables
- Returning inner functions
- Closure state
- Function objects and closures

Compare heavily with JavaScript closures because the conceptual foundation is already familiar.

Focus on Python-specific differences such as `nonlocal` and LEGB.

---

# Phase 8 — Modules, Packages and Imports

**Priority: 1**

Cover:

- Modules
- Packages
- `import`
- `from ... import`
- Aliases
- `__init__.py`
- `__name__`
- `__main__`

Understand what happens when Python executes:

```python
import module
```

Cover:

- Module execution
- Module objects
- Module caching
- `sys.modules`
- Import search path
- `sys.path`
- Absolute imports
- Relative imports
- Circular imports

Compare with JavaScript / Node.js module loading when useful, while explaining the differences.

---

# Phase 9 — Exceptions

**Priority: 2**

Move quickly through basic syntax:

```python
try:
    ...
except SomeError:
    ...
else:
    ...
finally:
    ...
```

Focus more on:

- Exception hierarchy
- Multiple exception types
- `raise`
- Custom exceptions
- Exception propagation
- Exception chaining
- `raise ... from ...`

Compare with JavaScript and Java exception behaviour where useful.

---

# Phase 10 — Python OOP

**Priority: 1**

I already understand OOP.

Focus on Python-specific behaviour.

Cover:

- Classes
- Instances
- Classes are objects
- `self`
- `__init__`
- Instance attributes
- Class attributes
- Instance methods

Understand:

- Attribute lookup
- Method binding

Then:

- `@classmethod`
- `@staticmethod`
- `@property`
- Inheritance
- Composition
- Overriding
- `super()`
- MRO at a practical level

Compare primarily with Java classes, and JavaScript prototype/class behaviour where useful.

---

# Phase 11 — Python Data Model and Dunder Methods

**Priority: 1**

Understand how Python objects participate in language behaviour.

Cover important methods:

- `__init__`
- `__str__`
- `__repr__`
- `__eq__`
- `__hash__`
- `__len__`
- `__getitem__`
- `__setitem__`
- `__contains__`
- `__iter__`
- `__next__`
- `__call__`

The goal is not to memorise dunder methods.

The goal is to understand Python's data model.

---

# Phase 12 — Dataclasses

**Priority: 2**

Cover:

- `@dataclass`
- Fields
- Generated `__init__`
- Generated `__repr__`
- Equality
- Defaults
- `default_factory`
- Frozen dataclasses
- Ordering
- `__post_init__`

Compare with Java DTOs, records, or simple model classes where useful.

---

# Phase 13 — Iterables and Iterators

**Priority: 1**

Cover deeply:

- Iterable
- Iterator
- Iterator protocol
- `iter()`
- `next()`
- `StopIteration`

Understand conceptually how:

```python
for item in values:
    ...
```

works internally.

Build one custom iterator to understand the protocol.

Do not spend excessive time building custom iterators afterwards.

---

# Phase 14 — Generators

**Priority: 1**

Cover:

- Generator functions
- `yield`
- Generator objects
- Pausing execution
- Resuming execution
- Generator state
- Lazy evaluation
- Generator expressions
- `yield from`

Understand why generators are useful and how they preserve execution state.

---

# Phase 15 — Decorators

**Priority: 1**

Build understanding progressively:

```text
Functions are objects
↓
Functions can be passed around
↓
Functions can return functions
↓
Closures
↓
Function wrapping
↓
Decorator
↓
@decorator syntax
```

Cover:

- Basic decorators
- Wrapper functions
- `*args`
- `**kwargs`
- `functools.wraps`
- Decorators with arguments
- Multiple decorators
- Decorator execution timing

After this phase:

```python
@app.get("/users")
def get_users():
    ...
```

should not feel magical.

---

# Phase 16 — Context Managers

**Priority: 1**

Cover:

- Resource management
- `with`
- `__enter__`
- `__exit__`

Understand why:

```python
with open("data.txt") as file:
    ...
```

works.

Then cover:

- Custom context managers
- `contextlib`
- `@contextmanager`

---

# Phase 17 — Type Hints

**Priority: 1**

First establish:

> Python remains dynamically typed when annotations are used.

Cover:

- Function annotations
- Variable annotations
- Return annotations
- `list[str]`
- `dict[str, int]`
- Union syntax
- `None`
- Optional values
- `Literal`
- Type aliases

Then:

- Generics
- `TypeVar`
- `Protocol`
- `TypedDict`

Compare with TypeScript's type system.

Pay special attention to the fact that TypeScript types are primarily compile-time concepts, while Python annotations are runtime-accessible objects unless evaluation behaviour changes them.

Understand:

- Runtime behaviour of annotations
- Static checking
- Runtime inspection
- Why frameworks can inspect annotations

---

# Phase 18 — Async Python

**Priority: 1**

Use JavaScript and Node.js knowledge heavily here.

Start with:

- Sequential execution
- Concurrency
- Parallelism

Then cover:

- `async def`
- Coroutine functions
- Coroutine objects
- `await`
- Event loop
- Tasks
- Cooperative scheduling

Cover:

- `asyncio.run`
- `asyncio.create_task`
- `asyncio.gather`
- Task cancellation basics
- Async exception behaviour

Then:

- Async context managers
- Async iterators
- Async generators

Compare:

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

Clearly explain where these analogies break down.

---

# Phase 19 — Threads, Processes and the GIL

**Priority: 1**

## Threads

Cover:

- Python threads
- Shared memory
- Race conditions
- Locks
- I/O-bound workloads

## Processes

Cover:

- Multiprocessing
- Separate memory
- CPU-bound workloads
- Parallelism

## GIL

Understand practically:

- What the GIL is
- Why CPython has it
- What it affects
- What it does not affect
- Why threads remain useful for I/O
- Why multiprocessing is useful for CPU-heavy work
- Where async fits

Compare where useful with Node.js worker threads/event loop and Java threading.

---

# Phase 20 — Memory Management

**Priority: 1**

Cover:

- Object lifetime
- References
- Reference counting
- `del`
- Garbage collection
- Cyclic references
- Garbage collector basics

Understand why:

```python
del x
```

removes a name/reference and does not necessarily immediately destroy the underlying object.

Compare with JavaScript and Java garbage-collected runtimes where helpful.

---

# Phase 21 — Python Internals

**Priority: 2**

Connect earlier concepts.

Cover:

- CPython
- Bytecode
- `dis`
- Code objects
- Function objects
- Stack frames
- Call stack
- Namespaces
- Module objects

Use small runtime experiments.

The objective is not to become a CPython contributor.

The objective is to understand why Python behaves the way it does.

---

# Phase 22 — Packaging and Environment Management

**Priority: 2**

Cover:

- Virtual environments
- `uv`
- Dependencies
- Development dependencies
- `pyproject.toml`
- Package structure
- Dependency locking
- Installing packages
- Local packages
- Editable installs

Compare conceptually with `npm`, `package.json`, Gradle or Maven where helpful.

---

# Phase 23 — Testing

**Priority: 2**

Do not teach testing theory from scratch.

Focus on Python tooling.

Cover:

- `assert`
- `pytest`
- Test discovery
- Fixtures
- Parameterisation
- Mocking
- Monkeypatching basics
- Testing exceptions

Compare with familiar JavaScript or Java testing concepts when helpful.

Advanced framework testing can be learned later inside the FastAPI repository.

---

# Phase 24 — Performance Fundamentals

**Priority: 2**

Cover practical concepts:

- Complexity of lists
- Dictionaries
- Sets
- Membership lookup
- List vs generator memory usage
- Lazy evaluation
- `timeit`
- Profiling basics
- Common Python performance mistakes

Do not prematurely optimise.

---

# Phase 25 — Advanced Python

**Priority: 3**

These topics can be learned after the core path:

- Descriptors
- Metaclasses
- `__slots__`
- Advanced MRO
- Multiple inheritance details
- Advanced reflection
- Dynamic attribute handling
- Advanced monkey patching
- Advanced generator behaviour
- Advanced async internals
- CPython implementation details
- C extensions

These topics should **not block FastAPI**.

---

# FastAPI Readiness Check

Before moving to FastAPI, verify that I understand:

- Python execution model
- Names and objects
- References
- Identity
- `is` vs `==`
- Mutability
- Hashability
- Collections
- Function argument behaviour
- Mutable default arguments
- `*args`
- `**kwargs`
- LEGB
- Closures
- Modules and imports
- Python OOP
- Method binding
- `self`
- Python data model
- Iterables
- Iterators
- Generators
- Decorators
- Context managers
- Type annotations
- Dynamic typing
- Coroutines
- `async`
- `await`
- Event loop
- Tasks
- Threads
- Processes
- GIL
- Basic memory management

Then provide:

```text
FASTAPI READINESS: GO
```

or:

```text
FASTAPI READINESS: NO-GO
```

A NO-GO should only identify meaningful gaps.

Advanced Python topics should not block the transition to FastAPI.
