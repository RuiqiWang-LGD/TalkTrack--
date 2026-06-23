from __future__ import annotations

import argparse
import json
import tempfile
from pathlib import Path

import fitz
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
CANVAS_SIZE = (1920, 1080)
THUMB_SIZE = (326, 214)

FONT_REGULAR_CANDIDATES = [
    Path(r"C:/Windows/Fonts/msyh.ttc"),
    Path(r"C:/Windows/Fonts/simsun.ttc"),
]
FONT_BOLD_CANDIDATES = [
    Path(r"C:/Windows/Fonts/msyhbd.ttc"),
    Path(r"C:/Windows/Fonts/simhei.ttf"),
]

COLORS = {
    "paper": (247, 244, 237),
    "sidebar": (16, 17, 14),
    "panel": (255, 255, 251),
    "ink": (0, 0, 0),
    "white": (255, 255, 255),
    "muted": (201, 201, 194),
    "thumb_bg": (25, 25, 22),
}


def first_existing(paths: list[Path]) -> Path | None:
    for path in paths:
        if path.exists():
            return path
    return None


FONT_REGULAR = first_existing(FONT_REGULAR_CANDIDATES)
FONT_BOLD = first_existing(FONT_BOLD_CANDIDATES)


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    path = FONT_BOLD if bold else FONT_REGULAR
    if path is None:
        return ImageFont.load_default()
    return ImageFont.truetype(str(path), size=size)


def load_plan(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    raw_pages = data.get("pages", data) if isinstance(data, dict) else data
    if not isinstance(raw_pages, list) or not raw_pages:
        raise ValueError("plan JSON must contain a non-empty pages list")

    pages = []
    for index, item in enumerate(raw_pages, start=1):
        if not isinstance(item, dict):
            raise ValueError(f"page item {index} must be an object")
        keywords = item.get("keywords", [])
        if isinstance(keywords, str):
            keywords = [part.strip() for part in keywords.replace("，", ",").split(",") if part.strip()]
        keywords = [str(k).strip() for k in keywords if str(k).strip()]
        if len(keywords) > 3:
            keywords = keywords[:2] + [" / ".join(keywords[2:])]

        pages.append(
            {
                "page": int(item.get("page", index)),
                "status": str(item.get("status") or item.get("label") or "顺读"),
                "keywords": keywords[:3],
                "script": str(item.get("script") or "").strip(),
                "next_step": str(item.get("next_step") or item.get("cue") or "").strip(),
            }
        )
    return pages


def make_thumbnail(source_pdf: fitz.Document, page_number: int) -> Image.Image:
    page_index = page_number - 1
    if page_index < 0 or page_index >= source_pdf.page_count:
        raise ValueError(f"source PDF does not contain page {page_number}")

    pix = source_pdf[page_index].get_pixmap(matrix=fitz.Matrix(0.7, 0.7), alpha=False)
    image = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    canvas = Image.new("RGB", THUMB_SIZE, COLORS["thumb_bg"])
    image.thumbnail(THUMB_SIZE, Image.Resampling.LANCZOS)
    x = (THUMB_SIZE[0] - image.width) // 2
    y = (THUMB_SIZE[1] - image.height) // 2
    canvas.paste(image, (x, y))
    return canvas


def text_width(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.ImageFont) -> int:
    if not text:
        return 0
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0]


def wrap_line(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.ImageFont, max_width: int) -> list[str]:
    lines: list[str] = []
    current = ""
    no_line_start = "，。、；：！？)]}）】》"
    for ch in text:
        trial = current + ch
        if current and text_width(draw, trial, fnt) > max_width:
            if ch in no_line_start:
                lines.append(trial)
                current = ""
            else:
                lines.append(current)
                current = ch
        else:
            current = trial
    if current:
        lines.append(current)
    return lines


def wrap_text(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.ImageFont, max_width: int) -> list[str]:
    all_lines: list[str] = []
    paragraphs = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    for paragraph in paragraphs:
        if paragraph == "":
            all_lines.append("")
            continue
        all_lines.extend(wrap_line(draw, paragraph, fnt, max_width))
    return all_lines


def draw_wrapped(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    fnt: ImageFont.ImageFont,
    fill: tuple[int, int, int],
    max_width: int,
    line_gap: int,
    paragraph_gap: int = 16,
) -> int:
    x, y = xy
    for line in wrap_text(draw, text, fnt, max_width):
        if line == "":
            y += paragraph_gap
            continue
        draw.text((x, y), line, font=fnt, fill=fill)
        box = draw.textbbox((x, y), line, font=fnt)
        y += (box[3] - box[1]) + line_gap
    return y


def fitted_main_font(draw: ImageDraw.ImageDraw, text: str, max_width: int, max_height: int) -> ImageFont.ImageFont:
    for size in range(52, 33, -2):
        fnt = font(size, bold=True)
        lines = wrap_text(draw, text, fnt, max_width)
        line_height = size + 12
        height = 0
        for line in lines:
            height += 28 if line == "" else line_height
        if height <= max_height:
            return fnt
    return font(34, bold=True)


def draw_page(item: dict, total: int, out_index: int, thumbnail: Image.Image) -> Image.Image:
    img = Image.new("RGB", CANVAS_SIZE, COLORS["paper"])
    draw = ImageDraw.Draw(img)

    draw.rectangle((0, 0, 430, 1080), fill=COLORS["sidebar"])
    draw.rectangle((500, 191, 1845, 878), fill=COLORS["panel"])

    draw.text((52, 34), f"{out_index:02d}", font=font(82, True), fill=COLORS["white"])
    draw.text((154, 78), f"/ {total}", font=font(30, True), fill=COLORS["muted"])

    draw.ellipse((62, 171, 82, 191), fill=COLORS["white"])
    draw.text((88, 163), item["status"], font=font(32, True), fill=COLORS["white"])

    img.paste(thumbnail, (52, 260))

    keyword_y = [536, 616, 695]
    for i, keyword in enumerate(item["keywords"][:3]):
        y = keyword_y[i]
        draw.ellipse((62, y, 82, y + 20), fill=COLORS["white"])
        draw.text((102, y - 8), keyword, font=font(34, True), fill=COLORS["white"])

    draw.text((47, 938), f"iPad 第 {out_index} 页", font=font(31, True), fill=COLORS["white"])
    draw.text((47, 993), f"对应大屏第 {item['page']} 页", font=font(31, True), fill=COLORS["white"])

    main_box = (541, 334, 1765, 735)
    main_font = fitted_main_font(draw, item["script"], main_box[2] - main_box[0], main_box[3] - main_box[1])
    draw_wrapped(
        draw,
        (main_box[0], main_box[1]),
        item["script"],
        main_font,
        COLORS["ink"],
        main_box[2] - main_box[0],
        line_gap=14,
        paragraph_gap=52,
    )

    draw_wrapped(
        draw,
        (528, 976),
        item["next_step"],
        font(38, True),
        COLORS["ink"],
        1200,
        line_gap=8,
        paragraph_gap=8,
    )
    return img


def assemble_pdf(image_paths: list[Path], output_pdf: Path) -> None:
    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    doc = fitz.open()
    try:
        for image_path in image_paths:
            page = doc.new_page(width=CANVAS_SIZE[0], height=CANVAS_SIZE[1])
            page.insert_image(fitz.Rect(0, 0, *CANVAS_SIZE), filename=str(image_path))
        doc.save(output_pdf)
    finally:
        doc.close()


def render(input_pdf: Path, plan_json: Path, output_pdf: Path, preview_dir: Path | None = None) -> list[Path]:
    pages = load_plan(plan_json)
    image_paths: list[Path] = []
    with tempfile.TemporaryDirectory() as td:
        work_dir = Path(td)
        source = fitz.open(input_pdf)
        try:
            for index, item in enumerate(pages, start=1):
                thumbnail = make_thumbnail(source, item["page"])
                image = draw_page(item, len(pages), index, thumbnail)
                image_path = work_dir / f"page_{index:03d}.jpg"
                image.save(image_path, quality=92, optimize=True)
                image_paths.append(image_path)
                if preview_dir and index in {1, min(5, len(pages)), min(12, len(pages)), len(pages)}:
                    preview_dir.mkdir(parents=True, exist_ok=True)
                    image.save(preview_dir / f"preview_{index:03d}.png")
            assemble_pdf(image_paths, output_pdf)
        finally:
            source.close()
    return image_paths


def self_test() -> None:
    with tempfile.TemporaryDirectory() as td:
        plan = Path(td) / "plan.json"
        plan.write_text(
            json.dumps(
                {
                    "pages": [
                        {
                            "page": 1,
                            "status": "开场停留",
                            "keywords": ["一", "二", "三", "四"],
                            "script": "第一句\n\n第二句",
                            "next_step": "翻第 2 页",
                        }
                    ]
                },
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )
        pages = load_plan(plan)
        assert pages[0]["page"] == 1
        assert pages[0]["keywords"] == ["一", "二", "三 / 四"]
        test_img = Image.new("RGB", THUMB_SIZE, COLORS["thumb_bg"])
        out = draw_page(pages[0], 1, 1, test_img)
        assert out.size == CANVAS_SIZE
        header_contract = {
            "page": 25,
            "status": "status",
            "keywords": ["a", "b", "c"],
            "script": "script",
            "next_step": "next",
        }
        header_out = draw_page(header_contract, 29, 1, test_img)
        actual_header = header_out.crop((0, 0, 235, 130))

        def header_reference(label: str) -> Image.Image:
            ref = Image.new("RGB", (235, 130), COLORS["sidebar"])
            ref_draw = ImageDraw.Draw(ref)
            ref_draw.text((52, 34), label, font=font(82, True), fill=COLORS["white"])
            ref_draw.text((154, 78), "/ 29", font=font(30, True), fill=COLORS["muted"])
            return ref

        def image_delta(left: Image.Image, right: Image.Image) -> int:
            return sum(abs(a - b) for a, b in zip(left.tobytes(), right.tobytes()))

        assert image_delta(actual_header, header_reference("01")) < image_delta(actual_header, header_reference("25"))
        draw = ImageDraw.Draw(out)
        wrapped = wrap_line(draw, "这是一个很长的句子，需要测试，标点不要跑到行首。", font(34, True), 210)
        assert all(not line.startswith(("，", "。", "、")) for line in wrapped)
    print("self-test passed")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-pdf", type=Path)
    parser.add_argument("--plan-json", type=Path)
    parser.add_argument("--output-pdf", type=Path)
    parser.add_argument("--preview-dir", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        self_test()
        return

    if not args.input_pdf or not args.plan_json or not args.output_pdf:
        parser.error("--input-pdf, --plan-json, and --output-pdf are required unless --self-test is used")

    render(args.input_pdf, args.plan_json, args.output_pdf, args.preview_dir)
    print(args.output_pdf)


if __name__ == "__main__":
    main()
