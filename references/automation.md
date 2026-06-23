# Automation Rules

Use automation for deterministic packaging work. Do not use automation to replace presentation judgment.

## What Scripts Should Do

Use `scripts/build_companion_ppt.py` for normal user delivery. It should:

- infer or accept `project_name`;
- create `{project_name}汇报` on the current user's Desktop by default, unless the user explicitly gives another output root;
- output `{sequence}_{project_name}.pptx`;
- keep page-plan JSON, thumbnails, logs, and temporary copies outside the user-facing output folder;
- validate the page-plan JSON before rendering;
- apply `assets/shunyejiang-template.pptx`;
- verify that the generated PPTX opens and that slide count matches the page plan;
- require the page plan to cover every source PDF page for normal delivery;
- preserve template background, typography, layout, and colors, except for the required centering correction of the main read-aloud text box;
- keep the main read-aloud text box centered in the right white content panel.

Standard command:

```powershell
python scripts/build_companion_ppt.py --source-pdf "D:/path/source.pdf" --plan-json "D:/path/page-plan.json" --project-name "项目名" --sequence 01
```

Use `--output-root "D:/path/output-root"` only when the user asks for a non-Desktop location.

The builder internally calls `scripts/render_companion_ppt.py`. The low-level renderer is for template debugging or development work only.

Use `--allow-partial` only for confirmed chapter tests, page-range tests, or partial internal trials. Do not use it for normal user delivery.

## What Scripts Should Not Do

Do not automate these decisions:

- whether to start generation before the user confirms;
- dominant tone mode;
- first-page soft-start wording;
- concept-page source fidelity;
- discipline core judgment;
- repeated-page grouping;
- whether a delivery page needs user supplementation;
- final read-aloud script quality.

These decisions decide whether the result sounds like a real person presenting. They must stay in model reasoning and page-plan writing.

## Output Hygiene

The final user-facing folder should contain only the final editable PPTX unless the user explicitly asks for extra materials.

Do not place these files in the final output folder:

- page-plan JSON;
- Markdown scripts;
- preview images;
- sampling images;
- validation logs;
- temporary thumbnails;
- extracted page images.

If debugging requires any of those files, put them in a temporary workspace or clearly separate maintenance folder, then remove or hide them before normal user delivery.

## Verification

Before saying the file is ready, run at least:

1. page-plan validation;
2. PPT openability check;
3. slide-count match against the page plan.

For template changes, also visually inspect at least one generated slide and confirm the background, fonts, text size, and thumbnail placement still follow the approved template.
