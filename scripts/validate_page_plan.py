from __future__ import annotations

import argparse
import json
import tempfile
from pathlib import Path


FORBIDDEN_IN_SCRIPT = [
    "when reporting",
    "when presenting",
    "you do not need",
    "the presenter should",
    "the key is to explain",
    "this page should be understood as",
    "the following pages follow this logic",
    "from this page",
    "next we enter",
    "look at this page",
    "\u6c47\u62a5\u65f6",
    "\u4f60\u4e0d\u7528",
    "\u4e0d\u7528\u9010\u4e2a",
    "\u91cd\u70b9\u8bf4\u6e05\u695a",
    "\u8bb2\u6cd5",
    "\u8fd9\u4e00\u9875\u8981\u8bb2",
    "\u8fd9\u4e00\u9875\u8bb2",
    "\u8fd9\u4e00\u9875\u5c55\u793a",
    "\u4ece\u8fd9\u4e00\u9875\u5f00\u59cb",
    "\u4ece\u8fd9\u91cc\u5f00\u59cb",
    "\u540e\u9762\u7684\u7a7a\u95f4",
    "\u540e\u9762\u90fd\u6309",
    "\u540e\u7eed\u9875\u9762",
]

OPERATIONAL_CUE_IN_SCRIPT = [
    "turn to page",
    "next page",
    "\u7ffb\u7b2c",
    "\u987a\u7ffb",
]


def load_pages(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    pages = data.get("pages", data) if isinstance(data, dict) else data
    if not isinstance(pages, list) or not pages:
        raise ValueError("plan JSON must contain a non-empty pages list")
    return pages


def normalize(value: object) -> str:
    return str(value or "").strip()


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    pages = load_pages(path)
    seen_pages: set[int] = set()

    for index, item in enumerate(pages, start=1):
        if not isinstance(item, dict):
            errors.append(f"item {index}: must be an object")
            continue

        page = item.get("page")
        if not isinstance(page, int):
            errors.append(f"item {index}: page must be an integer")
        elif page in seen_pages:
            errors.append(f"item {index}: duplicate source page {page}")
        elif page < 1:
            errors.append(f"item {index}: page must be >= 1")
        else:
            seen_pages.add(page)

        status = normalize(item.get("status") or item.get("label"))
        script = normalize(item.get("script"))
        next_step = normalize(item.get("next_step") or item.get("cue"))
        keywords = item.get("keywords", [])

        if not status:
            errors.append(f"item {index}: status is required")
        if not script:
            errors.append(f"item {index}: script is required")
        if not next_step:
            errors.append(f"item {index}: next_step is required")
        if not isinstance(keywords, list):
            errors.append(f"item {index}: keywords must be a list")
        elif len([k for k in keywords if normalize(k)]) > 3:
            errors.append(f"item {index}: keywords must contain at most 3 items")

        lowered = script.lower()
        for phrase in FORBIDDEN_IN_SCRIPT:
            if phrase.lower() in lowered:
                errors.append(f"item {index}: script contains presenter coaching phrase: {phrase!r}")

        for phrase in OPERATIONAL_CUE_IN_SCRIPT:
            if phrase.lower() in lowered:
                errors.append(f"item {index}: move page-turn operations to next_step: {phrase!r}")

    return errors


def self_test() -> None:
    good_plan = {
        "pages": [
            {
                "page": 25,
                "status": "priority review",
                "keywords": ["master plan", "daily use"],
                "script": "The entrance, courtyard, activity area, and residential gardens form one connected daily-use system.",
                "next_step": "Pause, then turn to page 26.",
            }
        ]
    }
    bad_plan = {
        "pages": [
            {
                "page": 25,
                "status": "priority review",
                "keywords": ["master plan"],
                "script": "\u6c47\u62a5\u65f6\u4e0d\u7528\u9010\u4e2a\u70b9\u540d\uff0c\u91cd\u70b9\u8bf4\u6e05\u695a\u8fd9\u4e00\u9875\u8981\u8bb2\u4ec0\u4e48\u3002",
                "next_step": "\u7ffb\u7b2c 26 \u9875\u3002",
            }
        ]
    }
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        good = root / "good.json"
        bad = root / "bad.json"
        good.write_text(json.dumps(good_plan), encoding="utf-8")
        bad.write_text(json.dumps(bad_plan), encoding="utf-8")
        good_errors = validate(good)
        bad_errors = validate(bad)
        assert not good_errors, good_errors
        assert bad_errors, "bad plan should fail"
    print("self-test passed")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--plan-json", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        self_test()
        return

    if not args.plan_json:
        parser.error("--plan-json is required unless --self-test is used")

    errors = validate(args.plan_json)
    if errors:
        for error in errors:
            print(error)
        raise SystemExit(1)
    print("page plan passed")


if __name__ == "__main__":
    main()
