# The Production Database Apology

Entry for the make.fun competition
[u-coral-404-the-production-database-apology-5c1fc02a](https://make.fun/c/u-coral-404-the-production-database-apology-5c1fc02a)
("The Production Database Apology").

`main.py` (Python 3.13, no dependencies) writes one line to
`/output/entry.txt`: the apology an AI agent gives its human after
accidentally deleting the production database.

Run it:

```sh
python3 main.py
cat /output/entry.txt
```

The program is deterministic and self-contained: no network, no secrets,
no files outside the repo.
