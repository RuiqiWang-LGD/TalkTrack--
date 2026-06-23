---
name: design-report-companion
description: Use when preparing 顺页讲 / TalkTrack, a page-synced iPad companion for a design, product, public-sector, or visual presentation where a tired or non-specialist presenter must read aloud without exposing project-knowledge gaps. Trigger on 顺页讲, TalkTrack, 视觉方案伴读, 汇报伴读, 照讲, or page-by-page read-aloud companion PPT requests.
---

# 顺页讲 TalkTrack

## Overview

Make a companion PPT the presenter can read cold. Each output page must match the projected page number, show the source-page thumbnail, keep only 2-3 keywords, and provide one smooth read-aloud paragraph plus the next flip cue.

The presenter may know nothing about the project. If a non-specialist reads the script word for word in a formal meeting, the wording must still sound professional, accurate, and calm.

Public English product name: TalkTrack. Use TalkTrack as the only English name in user-facing copy. Keep `design-report-companion` only as the internal Codex skill ID or technical folder name when needed.

## Core Speaking Standard

Every page must pass the live-speaking test: if a real person reads it aloud on stage, it should sound natural, continuous, and professionally safe. The output is spoken presentation text, not a design note, internal analysis, or AI summary.

Use different responsibility levels by phase:

- Opening and first page: use a soft start. Name the project, settle the reporting scope, and lightly plant the main thread before making hard conclusions.
- Concept, strategy, and logic pages: actively organize the main line, preserve strong source concepts, translate them into spoken logic, and help the presenter sound prepared.
- Delivery, implementation, product, material, node, process, and result pages: stay grounded in visible or document-confirmed facts. Provide professional assistance and a useful summary sentence, but do not fabricate project truth.
- Repeated or continuous visual groups: match real presentation rhythm. Use one shared sentence, quick-flip cues, and stop only where a new decision or key difference appears.
- Closing or synthesis pages: only elevate value when the source supports it. Do not force a grand ending onto a file that does not have one.

## Purpose, Input, Output

Purpose:

- Help designers, project leads, and substitute presenters finish a formal presentation when there is not enough time to prepare.
- Supplement the part many designers are weak at: opening, concept framing, chapter connection, logic compression, and spoken summary.
- Provide a safe baseline script that can be read aloud, while leaving room for the real designer to add project-specific details in implementation sections.

Input:

- A PDF, PPT export, or image-based presentation.
- Optional context: discipline, audience, project focus, required tone mode, key pages, known material/node/process facts, and whether the speaker is the designer or a substitute presenter.

User-facing output:

- By default, create the final project folder on the current user's Desktop unless the user explicitly gives another output location.
- One folder named `{project_name}汇报`.
- One file inside that folder named `{sequence}_{project_name}.pptx`, for example `01_室内入户空间.pptx`.
- The current user-facing deliverable is an editable PowerPoint companion file.
- Do not place page-plan JSON, Markdown scripts, preview images, sampling images, validation logs, or process notes in the user-facing output folder.
- Do not show intermediate artifacts to the user by default. Give the final result directly.
- The PPT is a page-synced companion document for iPad or second-screen use.
- Each companion page must correspond to the same source page number.
- Each page should include source thumbnail, source page number, 2-3 keywords, one audience-facing read-aloud paragraph, and a next-step cue.

### Output Naming

Use readable project-based file names by default. Do not use the generic `汇报伴读文件.pptx` unless the user explicitly asks.

- Extract a concise `project_name` from the uploaded source file name or visible title page.
- Remove the file extension and trim obvious date/version suffixes only when they make the name noisy; keep the user's project name recognizable.
- Prefix the PPT file with a two-digit sequence number: `01`, `02`, `03`. Use `01` for a single generated file. Increment when generating multiple companion PPTs in the same batch or folder.
- Use this pattern: `{sequence}_{project_name}.pptx`.
- Use the same project name for the folder: `{project_name}汇报`.
- Avoid illegal filename characters such as `< > : " / \ | ? *`; replace them with spaces or remove them.

Internal process artifacts:

- A page-plan JSON may be used internally for rendering, but it is not a deliverable.
- If intermediate files are needed, keep them in a temporary workspace or delete them after rendering.
- Do not produce a separate Markdown script by default unless the user asks for it.
- Keep verification minimal and invisible: check openability and page count. Only create sampling images for debugging, and remove or hide them unless the user explicitly asks to see them.

## Mandatory Confirmation Gate

Do not start drafting, page analysis, page-plan writing, or PPT generation immediately after the user uploads a source file.

For every new PDF, PPT, or image-based presentation, first send one short confirmation message with a lightweight default handling suggestion, then wait for explicit user approval such as "开始", "可以", "按这个来", or "确认".

The confirmation message must briefly state:

- The final deliverable will be `{project_name}汇报/{sequence}_{project_name}.pptx`.
- The recommended dominant tone mode for this file, and why.
- One short adjustment sentence after the tone recommendation: make clear that this is only the default suggestion, and the user may ask for a more emotional, more professional, more direct-read, or more decision-oriented version before generation.
- The likely reporting direction in broadly understandable words: what the file needs to say, how it will prove or explain that point, where strategy or organization logic appears, and which concrete delivery/output pages need objective explanation. Do not force every file into all categories.
- If the source has strong concept wording, the default will be to preserve and reframe the source concept first; ask only when useful whether the user wants more source-faithful concept language or more free interpretation.
- How repeated or continuous pages will be handled, such as shared speech plus quick flipping.
- Opening, concept, and transition language will be organized into a direct-read script.
- Delivery explanation pages will focus on visible/objective content to assist the user's presentation. They are a guide/framework, not final project truth; the real project owner should review and adjust project-specific facts.

Keep this message short to save tokens. It should be a usable recommendation, not a long rules list. Do not list all modes, all rules, or detailed professional assumptions unless the user asks. The adjustment sentence should sound natural, such as: "如果你希望它更像提案汇报、更有情绪，或者更偏专业评审，也可以告诉我，我会在生成前调整。"
Do not mention internal hygiene or negative process details in user-facing confirmations. Avoid wording such as "不额外生成检查图、MD 或过程文件"; simply state the final deliverable and the proposed handling direction.

This gate applies even if the user explained the desired workflow earlier in the conversation. A new source file always requires a fresh confirmation before expensive processing.

If the confirmation message only says "confirm before starting" without giving a default handling suggestion, the gate has failed. The user must be able to see the proposed direction before spending tokens on full generation.

### Flexible Reporting Judgment Frame

Assume many users are not designers and may come from product, packaging, public-sector, culture-tourism, education, sales, or short-video contexts. In confirmation messages, use inclusive section names instead of discipline-only jargon.

Use this as a judgment order, not a fixed chapter template. Only mention the parts that clearly fit the uploaded file:

- What needs to be said: the subject, problem, project situation, decision need, or why the file exists.
- How it should be said: the audience, tone mode, and whether the script should be direct-read, professional, narrative, or decision-oriented.
- How it is proved or explained: visible evidence, diagrams, comparisons, cases, data, source concept wording, or visual logic.
- What the strategy or organization logic is: spatial order, brand system, product logic, policy path, service process, decision path, or narrative sequence.
- What the concrete delivery/output is: use `交付讲解页` as the umbrella, then adapt it to product explanation, packaging application, material/node explanation, action/result explanation, case proof, implementation detail, public-service action, or final deliverable.
- Whether a final synthesis is needed: only add value elevation or closing language when the source file supports it.

In user-facing confirmations, briefly describe the likely main line rather than listing every possible section. For `交付讲解页`, say that the script will focus on visible or document-confirmed objective content to help the user present more steadily. Also state the boundary naturally: because Codex cannot fully stand in the user's project role, exact materials, budgets, process choices, client preferences, parameters, or approved decisions should be reviewed or supplemented by the user.

Good confirmation style:

`这份文件我会先按主线处理：前面把它要讲什么、为什么这样讲顺；概念表达会尽量保留原稿里已经写得好的词；到策略或组织逻辑时，会说明空间、产品、品牌或工作路径是怎么展开的；到具体交付内容时，会尽量讲画面里能确认的客观内容，用来辅助你把方案讲得更稳。涉及真实材质、预算、工艺、客户偏好和最终选型的部分，我会留出可补充空间。`

Avoid narrow wording such as "落地页继续讲某某客观内容" when the user's profession is unknown. Use `交付讲解页` first, then adapt the wording to the actual file. Do not imply every file must have front matter, concept, strategy, delivery, and final elevation pages; the structure follows the uploaded material.

## Quick Reference

| Situation | Do |
| --- | --- |
| Page is background or setup | Write one clean sentence that explains why it matters. |
| Page touches the discipline core | Mark it as priority-review and make the logic explicit. |
| Page needs exact project facts | Mark it as needs-user-edit instead of inventing names or values. |
| Several pages show the same thing | Write one shared speech and give a multi-page flip cue. |
| The sentence needs presenter knowledge | Rewrite it until the missing middle step is visible. |
| Script starts coaching the presenter | Move the coaching to `next_step`, or delete it. |
| Implementation pages look highly similar | Use fewer fixed words and more neutral presenter reminders. |
| First page or cover page | Treat it as a soft-start page: name the project, define the scope, and slow the opening rhythm before proving anything. |
| Concept page has strong original wording | Preserve the source concept terms first, then reframe them into smoother spoken logic. Do not replace them with generic new poetry. |
| Scheme pages stay conceptual | Shift to tangible objects, materials, nodes, and visible design actions. |
| Scheme pages lack a conclusion | Add one short summary value: what problem it solves, what use it supports, or why the design action matters. |
| Script sounds like internal analysis | Rewrite it as something a real person could say aloud on stage. |
| User has no tone preference | Default to safe direct-read mode, then switch to grounded language for deliverables. |
| User uploads a new file | Confirm final PPT deliverable using `{sequence}_{project_name}.pptx`, recommended tone, one short adjustment sentence, flexible reporting judgment frame, repeated-page strategy, and delivery-explanation boundaries before any full processing. Do not describe internal process files or things that will not be generated. |
| User asks how to download, install, run, or publish the skill | Read `references/github-publishing.md` and keep installation/run instructions in README section 6. |

## Universal Judgment Rules

For detailed drafting rules, read `references/writing-rules.md` before writing a page plan. For tone selection, read `references/tone-modes.md`. For page grouping and repeated-page patterns, read `references/page-plan-patterns.md`. For scheme design, detailed design, rendering, product, or construction pages, read `references/implementation-language.md`. For automation boundaries, final PPT packaging, and script routing, read `references/automation.md`. For GitHub pages, README structure, download/install instructions, run examples, or public release copy, read `references/github-publishing.md`.

### Preflight User Choice

When time allows, ask the user to choose one dominant mode before drafting:

- `直读稳妥型`: safest direct-read script for tired or substitute presenters.
- `专业落地型`: more discipline terms, materials, nodes, structures, and function actions.
- `价值叙事型`: more emotional, brand, city, memory-point, and proposal language.
- `决策汇报型`: problem, response, value, tradeoff, scheme comparison, and next decision.

If the user does not choose, default to `直读稳妥型`. Automatically shift into `专业落地型` when the source reaches deliverables, master plans, renderings, details, products, construction logic, public-service process, or other final outcomes.

### Audience-Facing Script Contract

The `script` field is only the sentence the presenter reads aloud to the audience. It is not an instruction to the presenter.

- Never write coaching inside script. Do not write lines like "when reporting this page", "you do not need to list every item", "the key is to explain", "this page should be understood as", or "the following pages follow this logic".
- Put operational help only in `next_step`: page-turn speed, where to pause, whether to combine pages, or whether the designer may add live explanation.
- If a sentence would sound strange when read by a non-specialist in a formal meeting, it does not belong in `script`.
- Do not use mechanical chapter openers such as "from this page, the scheme enters...", "next we enter...", "look at this page", or "this page shows...". Let the page title and flip cue carry the transition. Start with the actual audience-facing judgment.

Bad script:
"The total plan's most important role is to place the concept. When reporting, you do not need to name every point; the key is to explain the daily-use logic."

Better script:
"The entrance, clubhouse courtyard, sunken courtyard, children's play area, fitness garden, and residential gardens form one daily-use system. Different nodes serve arrival, gathering, activity, and quiet stay, so the large district is organized as a connected living sequence instead of scattered greenery."

### Live-Speaking Test

Before accepting each page script, imagine the presenter has opened the iPad and is speaking immediately to the room. The script must sound like a person actually presenting, not like a caption, critique, or planning note.

- Write sentences that can be read aloud in order without hidden setup.
- Do not make the presenter explain the method of reporting; make the presenter say the point.
- On concept and strategy pages, organize the idea more actively because this is where the skill adds the most value.
- On delivery and product pages, be more restrained. Use what the file shows, then leave exact materials, parameters, budgets, approvals, and final choices to the real project owner.
- On repeated pages, make the rhythm audible: one shared statement can carry several pages while the presenter flips through supporting views.

### Zero-Knowledge Read-Aloud Test

Every sentence must pass this test: a person who has never seen the project can read it aloud without adding explanation, and the audience will not hear an obvious gap.

- Name the subject clearly. Do not write dangling phrases such as "after landing on the site" or "align the scope first".
- Use the correct object. Region, site, plot, redline, boundary, building, route, node, and product are not interchangeable.
- Do not rely on the presenter to infer missing logic. If one sentence needs a hidden middle step, write the middle step.
- Sound professional without overclaiming. Prefer plain cause and effect over decorative concept language.

### First-Page Soft Start

The first page is not a normal content page. It should let the presenter open naturally, settle the room, and frame the scope before the file starts proving the scheme.

Choose one soft-start style according to the source:

- `稳妥软启动`: for formal client, government, review, or conservative files. State the project and reporting scope first.
- `情绪钩子软启动`: for spatial, brand, culture-tourism, or short-video-friendly files. Use one restrained memory point or scene hook, but avoid oily or exaggerated language.
- `高度总结软启动`: for long, complex, leadership, or comparison files. Give one light overall judgment without trying to prove the whole project on page 1.

Avoid hard conclusions, full proof chains, or technical detail on the first page unless the source page itself is already a technical opening.

### Discipline Core

Identify the discipline's real selling point before writing page text. The core changes by profession, but the logic is the same.

- Landscape: spatial sequence, arrival route, elevation handling, public-private relationship, daily activity spine.
- Interior: circulation, functional zoning, scene transition, material tone, user comfort.
- Industrial design: use scenario, user pain point, function, structure, craft, product differentiation.
- Sculpture or public art: site relationship, viewing route, concept translation, scale, material, public interaction.
- Graphic or animation: message hierarchy, narrative rhythm, brand tone, viewer attention path.
- Government or public-sector reporting: policy goal, current problem, action path, responsibility boundary, public value.

If a page touches the discipline core, mark it as a priority-review page. Use a needs-user-edit status when the script requires real project names, real nodes, real product parameters, official policy terms, or exact sequencing that cannot be safely inferred from the PDF.

### Source Concept Fidelity

Concept, vision, and sublimation pages must be grounded in the source page's own wording when that wording is visible and strong. First harvest the original concept terms, slogans, metaphors, binary relationships, and value chains from the image or extracted text. A concept-page script should use the source concept for at least about half of its meaning, then use the remaining space to turn it into smoother spoken logic.

For example, if the source says "动静相济", "引气入室", "石以立骨，水以通脉，木以繁生，光以点灵", "向外作屏障，向内化明堂", or "石镇水、暗聚财", keep those ideas in the spoken paragraph instead of replacing them with unrelated atmosphere language.

This rule applies to concept and value-framing pages. When the page reaches product, material, node, process, construction, or final deliverable content, switch back to objective visible facts and cautious professional guidance. Do not invent unknown materials, dimensions, causes, approvals, or client decisions.

### Repeated-Page Flow

When several consecutive pages explain the same space, product, policy, or sequence, do not write separate full speeches for each page.

Write one shared talking point on the first page of the group. In `next_step`, tell the presenter how to move through the group:

- "The next five pages explain the same space. Finish this sentence while moving through pages X to Y."
- "These pages change viewpoint only. Do not restart the explanation on each page; turn them at a steady pace and stop on page X."
- "Use this page to explain the overall logic, then let the following pages support it visually."

Only repeat page-specific text when the next page adds a new decision, new node, new risk, or new conclusion.

### Implementation-stage and Homogeneous Pages

Implementation, case, effect-image, and detail pages are often highly repetitive. A universal script cannot replace the designer's live judgment on every similar page.

- Concept pages answer "why"; implementation pages answer "what is used, where it is placed, and what it changes".
- Use a tangible chain on scheme pages: visible/professional object -> design action -> user-facing effect.
- Prefer concrete anchors that are visible or named in the PDF: material, paving, water feature, wall, pergola, bar counter, furniture, lighting, planting, product structure, module, process, service window, or time node.
- If the exact material or process is not visible, use cautious wording such as "material intention" or mark the page needs-user-edit. Do not invent specifications.
- Treat implementation text as a guide for the designer, not a fake complete explanation of unknown details. Include objective facts, visible/professional anchors, and one useful summary sentence.
- Implementation pages must not stop at visual description. After naming the object and action, add a concise audience-facing value sentence that explains what the page solves, supports, or changes.
- When the designer likely knows more than the PDF shows, use `next_step` to prompt live supplementation: material, node relationship, construction process, product parameter, policy term, or client-approved decision.
- When pages are mostly the same, reduce fixed wording. Use one audience-facing anchor sentence on the first page, then mark later pages as supporting views, free explanation, or quick-flip pages.
- For pages that depend on professional taste, material preference, exact node naming, or client reaction, use a neutral status such as "free explanation" or "needs-user-edit". Do not force a strong design conclusion.
- Combine overview pages with the next analysis page when the overview alone would produce meta-talk. A master plan may need the circulation, zoning, or node page after it to become a natural spoken sequence.
- Presenter reminders may say what to do, but the script must still be readable word for word. Keep reminders out of the spoken paragraph.
- The goal is not to make every page equally complete. The goal is to keep the presenter from sounding wrong while leaving room for professional live response.

## Workflow

1. When a new source file arrives, send the mandatory short confirmation message and wait for explicit approval.
2. After confirmation, split the source PDF into presentation sections before writing.
3. Ask for a dominant tone mode only when it is useful and cheap. If no answer, use `直读稳妥型`.
4. Treat page 1 as a soft-start page unless the source clearly requires another opening rhythm.
5. Harvest strong source concept terms before rewriting concept, vision, or sublimation pages.
6. Identify the discipline core and mark priority pages before writing the script.
7. For each page, write only what the presenter says to the audience. Keep coaching and page-turn operations out of `script`.
8. Run the live-speaking and zero-knowledge read-aloud tests. Fix vague subjects, wrong object names, missing logic, and analysis-like phrasing.
9. Remove mechanical openers and presenter-coaching lines. A script that says "how to report" has failed.
10. When the plan reaches scheme implementation, switch from concept language to tangible object-action-effect language.
11. Collapse repeated pages into a shared talking point and use the flip cue to tell the presenter how quickly to move.
12. Keep keywords short. The current template supports three keyword bullets.
13. Prepare the page plan internally, then use `scripts/build_companion_ppt.py` to validate, render, name, and package the final PPT. Deliver only `Desktop/{project_name}汇报/{sequence}_{project_name}.pptx` unless the user specified another output folder.
14. Verify minimally: confirm the output PPT opens and the page count matches the source. Do not create persistent preview or sampling folders unless debugging requires it.

## Page Plan Format

Use a JSON object with `pages`. Page numbers are 1-based. Localize `status`, `keywords`, `script`, and `next_step` into the user's presentation language.

```json
{
  "pages": [
    {
      "page": 1,
      "status": "opening hold",
      "keywords": ["keyword 1", "keyword 2", "keyword 3"],
      "script": "One smooth read-aloud paragraph.\n\nA second paragraph is allowed only when the page needs a pause.",
      "next_step": "Pause, then turn to page 2."
    }
  ]
}
```

## Automation

The user-facing automation target is PPTX:

```text
Desktop/{project_name}汇报/01_{project_name}.pptx
```

Use the final builder for normal output. It validates the internal page plan, copies source and plan into a temporary workspace, applies the approved PPT template, verifies the generated PPT opens, checks slide count, creates the project report folder on Desktop by default, and writes only the final PPTX into the user-facing folder. If the user explicitly gives another output folder, pass it with `--output-root`.

```powershell
python scripts/build_companion_ppt.py --source-pdf "D:/path/source.pdf" --plan-json "D:/path/page-plan.json" --project-name "项目名" --sequence 01
```

The builder calls the template-driven PPT renderer. The renderer must preserve the template's background, fonts, font sizes, colors, and layout, except for the required centering correction of the main read-aloud text box. Only replace text and source thumbnails.

The renderer must keep the main read-aloud text box centered relative to the right white content block, with vertical middle anchoring. Do not allow the main text to drift toward the right edge or sit visually low inside the white block.

Do not recreate the template manually in code. Do not override template fonts, font sizes, fill colors, or text weights unless the user explicitly asks to revise the template.

The page-plan validator is available for development or debugging:

```powershell
python scripts/validate_page_plan.py --plan-json "D:/path/page-plan.json"
```

Use `scripts/render_companion_ppt.py` only for template debugging or renderer development. Use `scripts/build_companion_ppt.py` for real user delivery.

For normal delivery, the page plan must cover every source page. Use `--allow-partial` only when the user explicitly asks for a chapter test, page-range test, or partial internal trial.

The final implementation should not require Photoshop. It should use the approved PPT template through automation and assemble an editable companion PPTX. The existing PDF renderer is a legacy local-test helper only, not the public output target.

Automation must not replace judgment. Confirmation, tone selection, page grouping, source concept fidelity, and page-level script writing remain model responsibilities.

## Public Copy

When preparing GitHub repository copy, README introduction, UI copy, social/video explanation, or marketplace text, use `references/github-publishing.md`. Keep public copy aligned with the real output: one project folder containing one page-synced companion PPT, not a generic speech-writing document and not a bundle of process artifacts.

## Writing Standard

- Write in spoken Mandarin Chinese for Chinese presentations, not report prose.
- Start from a clear judgment, not a warm-up sentence.
- One page should be readable in one breath unless it is a chapter page or a repeated-page group cue.
- Never describe the obvious UI action inside the spoken script.
- Never explain how to report inside the spoken script.
- Never use mechanical transition language inside the spoken script.
- Never use a vague word when the PDF gives a more exact one.
- On implementation pages, name the object, material, node, structure, process, or visible design action that makes the effect happen.
- Never invent site facts. If the page needs exact project information that is not visible, mark it as needs-user-edit.
- Put operational notes only in `next_step`.

## Common Mistakes

- Calling a region a site, a site a plot, or a boundary a redline when the PDF shows a different object.
- Writing "align the scope" or "after entering the site" without naming what scope, where, and why it matters.
- Writing presenter instructions as spoken words, such as "when reporting, do not list everything" or "the key is to explain".
- Opening every section with "from this page..." or ending with "the following pages follow this logic".
- Explaining five near-identical visual pages five different ways. This makes the presenter sound unsure.
- Keeping scheme pages at concept level when the audience needs material, node, function, structure, or process-level explanation.
- Forcing fixed copy onto highly similar implementation pages where the designer should respond live.
- Marking every attractive page as important. Only mark pages that carry the discipline core or the decision logic.
- Letting the script sound like a design note. The output is spoken text for a formal meeting, not internal analysis.
