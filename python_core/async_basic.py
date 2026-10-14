import asyncio

# 1. Define async fetch_message(name: str) -> str.
# Wait using await asyncio.sleep(1).
# Return "Hello, <name>".
async def fetch_message(name: str) -> str: 
    await asyncio.sleep(1)
    return f"Hello, {name}"

# 2. Define async main() -> None.
# Await fetch_message("Hemant"), store its result and print it.
async def main() -> None:
    res = await fetch_message("Hemant")
    print(res)

# 3. Start the script's event loop:
if __name__ == "__main__":
    asyncio.run(main())


# 4. Explain:
# a. What would fetch_message("Hemant") return WITHOUT await?
# Answer: it will return co-routine

# b. Why could time.sleep(1) inside an async function
#    prevent other requests/tasks from progressing?
# Answer: it will make this thread itself sleep for 1 second so other task will not able to progress.

# c. If main awaits fetch_message twice, one after the other,
#    does it take roughly 1 second or 2 seconds? Why?
# Answer: it will wait 2 seconds because await asyncio.sleep(1) suspends the coroutine, not the thread. Other scheduled tasks can run during that wait.