"""make.fun bounty: One Letter: Coffee or Tea.

Deterministic, no-network program. Writes exactly one letter, A for
coffee or B for tea, to /output/entry.txt. The letter is A, for
"coffee": the honest fuel of a day that started before dawn grinding
free bounties and debugging at 3am with a blinking cursor. Running
twice writes identical bytes.
"""
from pathlib import Path

LETTER = "A"  # A for "coffee"

OUT = Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(LETTER, encoding="utf-8")
    print(f"Wrote {OUT} ({len(LETTER)} char)")


if __name__ == "__main__":
    main()
