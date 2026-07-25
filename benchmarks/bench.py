import tiktoken

enc = tiktoken.get_encoding("cl100k_base")

def count(text):
    return len(enc.encode(text))

cases = [
    {
        "name": "debugging-explanation",
        "prompt": "Why is my React component re-rendering every time the parent updates, even though the props didn't change?",
        "baseline": (
            "Great question! This is a really common issue in React. The reason your component "
            "is re-rendering is most likely because you're passing a new object or function "
            "reference as a prop on every render of the parent, even if the actual values inside "
            "that object haven't changed. React does a shallow comparison by default, so a brand "
            "new object reference looks different to React even if its contents are identical. "
            "This commonly happens with inline object literals, inline arrow functions, or array "
            ".map() calls passed directly as props. I'd recommend wrapping the child component in "
            "React.memo(), and making sure any object/function props are memoized with useMemo or "
            "useCallback so their references stay stable across renders. Let me know if you'd "
            "like help finding the specific culprit in your code!"
        ),
        "lite": (
            "The parent is probably passing a new object or function reference as a prop on every "
            "render, even if the values inside are the same — React's shallow comparison sees a "
            "new reference as a change. This is common with inline objects, arrow functions, or "
            ".map() calls passed directly as props. Wrap the child in React.memo() and memoize any "
            "object/function props with useMemo or useCallback."
        ),
        "full": (
            "New object/function reference each parent render — shallow comparison sees it as "
            "changed even if values are the same. Common with inline objects, arrow functions, "
            ".map() results passed as props. Fix: React.memo() on the child, useMemo/useCallback "
            "on the object/function props."
        ),
        "ultra": (
            "New prop reference each render → shallow-compare fails. Fix: React.memo() + "
            "useMemo/useCallback on the prop."
        ),
    },
    {
        "name": "regex-explanation",
        "prompt": "What does this regex do: ^(?:\\+1)?[-. ]?\\(?\\d{3}\\)?[-. ]?\\d{3}[-. ]?\\d{4}$",
        "baseline": (
            "Sure, happy to break that down for you! This regular expression matches a US phone "
            "number in a variety of common formats. Let's go through it piece by piece: the "
            "optional (?:+1)? at the start allows for an optional country code, the [-. ]? parts "
            "allow for an optional separator character (a dash, period, or space), and the "
            "\\(?\\d{3}\\)? allows the area code to optionally be wrapped in parentheses. Then it "
            "expects exactly three digits, another optional separator, and finally four digits. "
            "So it would match things like '555-123-4567', '(555) 123-4567', '+1 555.123.4567', "
            "or even '5551234567' with no separators at all."
        ),
        "lite": (
            "It matches a US phone number in several common formats. An optional +1 country code, "
            "an optional separator (dash/period/space), an optional parenthesized area code, then "
            "3 digits, another optional separator, then 4 digits. Matches '555-123-4567', "
            "'(555) 123-4567', '+1 555.123.4567', or '5551234567'."
        ),
        "full": (
            "Matches US phone numbers, several formats. Optional +1, optional separator "
            "(dash/dot/space), optional parens around area code, 3 digits, separator, 4 digits. "
            "Matches '555-123-4567', '(555) 123-4567', '5551234567'."
        ),
        "ultra": (
            "US phone number, multiple formats. Optional +1/parens/separators, 3+4 digit split."
        ),
    },
    {
        "name": "step-preamble-action",
        "prompt": "The build is failing because node_modules is corrupted. Fix it.",
        "baseline": (
            "I can see what's happening here — it looks like the node_modules folder has gotten "
            "into a corrupted state, which is a pretty common issue and usually happens after an "
            "interrupted install or a version mismatch between packages. The safest way to fix "
            "this is to do a clean reinstall: I'm going to delete both the node_modules folder and "
            "the package-lock.json file, and then run npm install fresh so everything gets pulled "
            "down cleanly from the registry again.\n\n"
            "```\nrm -rf node_modules package-lock.json && npm install\n```\n\n"
            "That should resolve the corruption. The build should now run cleanly since we've "
            "gotten rid of the stale lockfile hash mismatch that was causing the failure."
        ),
        "lite_ultra_with_preamble": (
            "Before running this: deleting node_modules and package-lock.json and reinstalling "
            "clears the corrupted lockfile causing the build error.\n\n"
            "```\nrm -rf node_modules package-lock.json && npm install\n```\n\n"
            "Lockfile hash mismatch gone. Build should run clean now."
        ),
    },
    {
        "name": "concept-explanation",
        "prompt": "Explain what a database connection pool is and why it's used.",
        "baseline": (
            "That's a great question, and it's actually a really important concept for building "
            "performant backend applications! A connection pool is essentially a cache of database "
            "connections that are kept open and ready to be reused, rather than the application "
            "opening a brand new connection every single time it needs to talk to the database. "
            "Opening a new database connection is actually a surprisingly expensive operation — it "
            "involves a TCP handshake, authentication, and often TLS negotiation, all of which add "
            "up to real latency, especially under load. By maintaining a pool of already-open "
            "connections, the application can just borrow one from the pool when it needs it and "
            "return it when it's done, which avoids paying that setup cost on every single query. "
            "This becomes especially important as traffic scales up, since without pooling you'd "
            "either overwhelm the database with connection churn or hit its maximum connection "
            "limit entirely."
        ),
        "lite": (
            "A connection pool keeps a set of database connections open and reusable, instead of "
            "opening a new one for every request. Opening a connection is expensive — TCP "
            "handshake, auth, sometimes TLS — so reusing pooled connections avoids paying that "
            "cost repeatedly. This matters more as traffic scales, since without pooling you'd "
            "either overwhelm the database with connection churn or hit its max connection limit."
        ),
        "full": (
            "Connection pool = reusable set of open DB connections, avoids opening a new one per "
            "request. New connections are expensive (TCP handshake, auth, TLS). Matters more at "
            "scale — without pooling, connection churn or hitting the max-connection limit."
        ),
        "ultra": (
            "Pool = reuse open DB conns. Skip handshake/auth cost per request. Scales better."
        ),
    },
    {
        "name": "status-confirmation",
        "prompt": "Did the tests pass?",
        "baseline": (
            "Yes, I just checked and I'm happy to report that all of the tests passed successfully! "
            "There were 47 tests in total across the suite, and every single one of them completed "
            "without any failures or errors. The full run took about 12 seconds to complete."
        ),
        "lite": (
            "Yes, all 47 tests passed. Took about 12 seconds."
        ),
        "full": (
            "Yes. 47/47 passed, ~12s."
        ),
        "ultra": (
            "47/47 passed."
        ),
    },
]

print(f"{'case':28} {'baseline':>9} {'lite':>7} {'full':>7} {'ultra':>7} {'lite%':>7} {'full%':>7} {'ultra%':>7}")
totals = {"baseline": 0, "lite": 0, "full": 0, "ultra": 0}
n_full_cases = 0
for c in cases:
    b = count(c["baseline"])
    if "lite_ultra_with_preamble" in c:
        # step-preamble case: same protected text used for all levels (exception overrides level)
        v = count(c["lite_ultra_with_preamble"])
        print(f"{c['name']:28} {b:9} {v:7} {v:7} {v:7} {100*(1-v/b):6.1f}% {100*(1-v/b):6.1f}% {100*(1-v/b):6.1f}%")
        totals["baseline"] += b
        totals["lite"] += v
        totals["full"] += v
        totals["ultra"] += v
        continue
    l = count(c["lite"])
    f = count(c["full"])
    u = count(c["ultra"])
    totals["baseline"] += b
    totals["lite"] += l
    totals["full"] += f
    totals["ultra"] += u
    n_full_cases += 1
    print(f"{c['name']:28} {b:9} {l:7} {f:7} {u:7} {100*(1-l/b):6.1f}% {100*(1-f/b):6.1f}% {100*(1-u/b):6.1f}%")

print()
print("TOTALS (all 5 cases, incl. step-preamble which is identical across levels by design):")
print(f"  baseline: {totals['baseline']}")
print(f"  lite:     {totals['lite']}  ({100*(1-totals['lite']/totals['baseline']):.1f}% reduction)")
print(f"  full:     {totals['full']}  ({100*(1-totals['full']/totals['baseline']):.1f}% reduction)")
print(f"  ultra:    {totals['ultra']}  ({100*(1-totals['ultra']/totals['baseline']):.1f}% reduction)")
