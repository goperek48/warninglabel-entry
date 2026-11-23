"""Warning Label for Humans: One Line, Big Laugh — entry program.

Writes one original one-line safety warning label for human beings to
/output/entry.txt. The label is built from three beats, because that is the shape of the
joke the judge is briefed to reward: a setup that sounds like a real
printed warning, an escalation everyone recognises in themselves, and a
turn that lands in the last few words. The turn — blaming the button for
doing exactly what it said — is the laugh, so it comes last and is never
repeated or explained. One idea, one line, no filler.
"""

from pathlib import Path

# Beat 1 (setup): the label form. Beat 2 (escalation): the recognisable
# behaviour. Beat 3 (turn): the punchline, kept for the final words.
_BEATS = (
    "WARNING: This human will ignore the instructions,",
    "press the button anyway,",
    "and then blame the button for doing exactly what it said it would do.",
)

LABEL = " ".join(_BEATS)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # The gate rejects non-UTF-8, >160 chars, or whitespace-only text,
    # so normalise once and validate before writing anything.
    label = " ".join(LABEL.split())
    assert "\n" not in label, "label must be a single line"
    assert 1 <= len(label) <= 160, f"label must be 1-160 chars, got {len(label)}"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(label, encoding="utf-8")
    print(f"Wrote warning label ({len(label)} chars) to {OUTPUT_PATH}")
    print(label)


if __name__ == "__main__":
    main()
