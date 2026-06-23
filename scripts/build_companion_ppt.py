from __future__ import annotations

import argparse
import re
import shutil
import sys
import tempfile
from pathlib import Path

import fitz
from pptx import Presentation

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent
DEFAULT_TEMPLATE = ROOT / "assets" / "shunyejiang-template.pptx"

sys.path.insert(0, str(SCRIPT_DIR))
from render_companion_ppt import load_plan, render  # noqa: E402
from validate_page_plan import validate  # noqa: E402


ILLEGAL_FILENAME_CHARS = r'<>:"/\|?*'


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build one final TalkTrack companion PPTX from a source PDF and an internal page-plan JSON."
    )
    parser.add_argument("--source-pdf", required=True, type=Path, help="Source presentation PDF.")
    parser.add_argument("--plan-json", required=True, type=Path, help="Internal page-plan JSON.")
    parser.add_argument(
        "--output-root",
        type=Path,
        default=None,
        help="Folder where the project report folder will be created. Defaults to the current user's Desktop.",
    )
    parser.add_argument("--project-name", default=None, help="Override the project name inferred from the source file.")
    parser.add_argument("--sequence", default="01", help="Two-digit output sequence number. Defaults to 01.")
    parser.add_argument("--template-pptx", default=DEFAULT_TEMPLATE, type=Path, help="TalkTrack PPT template.")
    parser.add_argument("--total-pages", type=int, default=None, help="Displayed total page count.")
    parser.add_argument("--allow-partial", action="store_true", help="Allow a page plan that covers only part of the source PDF.")
    parser.add_argument("--no-overwrite", action="store_true", help="Fail if the final PPTX already exists.")
    return parser.parse_args()


def sanitize_filename(value: str, fallback: str = "项目") -> str:
    cleaned = "".join(" " if ch in ILLEGAL_FILENAME_CHARS else ch for ch in value)
    cleaned = re.sub(r"\s+", " ", cleaned).strip(" ._-")
    return cleaned or fallback


def infer_project_name(source_pdf: Path) -> str:
    stem = source_pdf.stem
    stem = re.sub(r"\s+", " ", stem).strip()
    stem = re.sub(r"[\s_-]*(20\d{2}[.\-_]?\d{1,2}[.\-_]?\d{1,2}|20\d{6})$", "", stem)
    stem = re.sub(r"[\s_-]*(v|V)\d+(\.\d+)?$", "", stem)
    stem = re.sub(r"[\s_-]*(final|FINAL|正式版|终稿|定稿)$", "", stem)
    return sanitize_filename(stem)


def normalize_sequence(value: str) -> str:
    stripped = str(value).strip()
    if stripped.isdigit():
        return f"{int(stripped):02d}"
    return sanitize_filename(stripped, fallback="01")


def count_pdf_pages(path: Path) -> int:
    with fitz.open(str(path)) as doc:
        return doc.page_count


def default_output_root() -> Path:
    desktop = Path.home() / "Desktop"
    return desktop if desktop.exists() else Path.home()


def validate_inputs(source_pdf: Path, plan_json: Path, template_pptx: Path) -> None:
    missing = [path for path in [source_pdf, plan_json, template_pptx] if not path.exists()]
    if missing:
        joined = "\n".join(str(path) for path in missing)
        raise FileNotFoundError(f"missing required file(s):\n{joined}")

    errors = validate(plan_json)
    if errors:
        joined = "\n".join(f"- {error}" for error in errors)
        raise ValueError(f"page plan validation failed:\n{joined}")


def verify_output(output_pptx: Path, expected_slides: int) -> None:
    prs = Presentation(str(output_pptx))
    actual_slides = len(prs.slides)
    if actual_slides != expected_slides:
        raise ValueError(f"slide count mismatch: expected {expected_slides}, got {actual_slides}")


def verify_page_coverage(pages: list[dict], source_total: int, allow_partial: bool) -> None:
    plan_pages = {item["page"] for item in pages}
    if any(page > source_total for page in plan_pages):
        raise ValueError(f"page plan references pages beyond source page count {source_total}")
    if allow_partial:
        return

    expected_pages = set(range(1, source_total + 1))
    if plan_pages != expected_pages:
        missing = sorted(expected_pages - plan_pages)
        extra = sorted(plan_pages - expected_pages)
        details: list[str] = []
        if missing:
            details.append(f"missing pages: {missing[:20]}{'...' if len(missing) > 20 else ''}")
        if extra:
            details.append(f"extra pages: {extra[:20]}{'...' if len(extra) > 20 else ''}")
        raise ValueError("page plan does not cover the full source PDF; " + "; ".join(details))


def build_companion_ppt(
    source_pdf: Path,
    plan_json: Path,
    output_root: Path,
    project_name: str,
    sequence: str,
    template_pptx: Path,
    displayed_total: int | None,
    overwrite: bool,
    allow_partial: bool,
) -> Path:
    source_pdf = source_pdf.resolve()
    plan_json = plan_json.resolve()
    template_pptx = template_pptx.resolve()
    output_root = output_root.resolve()

    validate_inputs(source_pdf, plan_json, template_pptx)

    project_name = sanitize_filename(project_name)
    sequence = normalize_sequence(sequence)
    final_dir = output_root / f"{project_name}汇报"
    final_path = final_dir / f"{sequence}_{project_name}.pptx"

    if final_path.exists() and not overwrite:
        raise FileExistsError(final_path)

    pages = load_plan(plan_json)
    source_total = count_pdf_pages(source_pdf)
    verify_page_coverage(pages, source_total, allow_partial)

    final_dir.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="talktrack_build_") as tmp:
        tmp_root = Path(tmp)
        tmp_source = tmp_root / "source.pdf"
        tmp_plan = tmp_root / "page_plan.json"
        tmp_output = tmp_root / "companion.pptx"
        shutil.copy2(source_pdf, tmp_source)
        shutil.copy2(plan_json, tmp_plan)
        render(tmp_source, tmp_plan, template_pptx, tmp_output, displayed_total)
        verify_output(tmp_output, len(pages))
        shutil.copy2(tmp_output, final_path)

    verify_output(final_path, len(pages))
    return final_path


def main() -> None:
    args = parse_args()
    source_pdf = args.source_pdf
    project_name = args.project_name or infer_project_name(source_pdf)
    output_root = args.output_root or default_output_root()

    output = build_companion_ppt(
        source_pdf=source_pdf,
        plan_json=args.plan_json,
        output_root=output_root,
        project_name=project_name,
        sequence=args.sequence,
        template_pptx=args.template_pptx,
        displayed_total=args.total_pages,
        overwrite=not args.no_overwrite,
        allow_partial=args.allow_partial,
    )
    print(output)


if __name__ == "__main__":
    main()
