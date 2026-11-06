<p align="center">
  <img src="assets/brand/mark.svg" alt="TalkTrack logo" height="112">
</p>

<h1 align="center">TalkTrack</h1>

<p align="center">
  <strong>Turn visual proposals into page-synced presenter notes.</strong><br>
  <sub>An AI skill for design, product and project presentations.</sub>
</p>

<p align="center"><strong>English</strong> | <a href="README_CN.md">简体中文</a></p>

<p align="center">
  <img src="assets/brand/badge-1.svg" alt="type: AI Skill" height="22">
  <img src="assets/brand/badge-2.svg" alt="output: PPTX" height="22">
  <img src="assets/brand/badge-3.svg" alt="notes: Chinese" height="22">
  <img src="assets/brand/badge-4.svg" alt="mode: Page-synced" height="22">
</p>

<p align="center">
  Keep page thumbnails, keywords and Chinese read-aloud notes together.<br>
  Follow pause and page-turn cues to present with a clear rhythm.
</p>

<p align="center"><a href="#quick-start"><strong>Quick Start</strong></a> · <a href="#how-it-works"><strong>How It Works</strong></a> · <a href="#installation"><strong>Installation</strong></a> · <a href="#limitations"><strong>Limitations</strong></a></p>

---

## From visual proposals to a confident delivery

| Page alignment | Read-aloud notes | Speaking rhythm |
| --- | --- | --- |
| Keep original thumbnails and keywords | Develop clear Chinese presenter copy | Add pause and page-turn cues |
| Pages → Companion | Visuals → Spoken narrative | Sequence → Delivery cues |

---

<a id="quick-start"></a>

## Quick Start

Upload a PDF, exported presentation or image-based proposal, then describe your goal:

~~~text
Use TalkTrack to create a page-synced PPTX companion for this proposal, with clear Chinese read-aloud notes.
~~~

For a decision-making audience, ask for decision-briefing mode and a focus on value, choices, risks and next steps. For a professional review, ask for implementation mode and a focus on visible materials, spatial relationships and buildability.

The public product name is **TalkTrack / 顺页讲**. The internal Codex skill ID is **design-report-companion**; it can be invoked as $design-report-companion.

## What You Get

TalkTrack creates a presenter-side companion, intended for reading on an iPad while the original proposal is projected. It helps when a visual deck is ready but the speaker has little preparation time.

| Area | Content | Purpose |
| --- | --- | --- |
| Left | Original page thumbnail, page number and 2–3 keywords | Stay aligned with the projected page |
| Right | A continuous paragraph of large Chinese read-aloud copy | Provide words that can be spoken directly |
| Bottom | Pause, page-turn, continuous-reading or designer-input cues | Control the rhythm |

Every companion page corresponds to the original page number. Current companion copy is **Chinese**; an English README does not imply English narration support.

The usual delivery is one folder and one PPTX:

~~~text
Desktop/
└─ 项目名汇报/
   └─ 01_项目名.pptx
~~~

The name is taken from the source or title page where possible. A different output location can be specified.

## Who It Helps

Designers with a finished proposal but no speaking notes; project leads taking over a presentation; substitute presenters; teams explaining visual proposals to clients and reviewers; and creators developing a spoken narrative from visual project material.

## Inputs and Speaking Modes

Source material can be PDF, exported presentation pages or single/multiple images such as renderings, plans, diagrams, details and references.

| Mode | Typical use | Style |
| --- | --- | --- |
| Direct and steady | Default; limited preparation; substitute speaker | Clear and natural, cautious about unsupported detail |
| Professional implementation | Reviews, materials, details and application pages | Specific about visible objects and confirmed relationships |
| Value narrative | Proposals, branding and cultural/tourism concepts | More story, value, rhythm and memorable ideas |
| Decision briefing | Leadership/client reviews, public presentations, comparisons | Problems, choices, value, risks and next steps |

Without an explicit choice, the default is direct and steady. Implementation pages move toward the professional style. Before generation, the skill recommends a language direction the user can adjust.

<a id="how-it-works"></a>

## How It Works

1. Start calmly: name the project and scope before making strong conclusions.
2. Identify the discipline and the main presentation task.
3. Recognize page roles without forcing every deck into a fixed chapter structure.
4. Keep useful source concepts and turn them into natural spoken language.
5. Ground implementation pages in visible or documented facts.
6. Control repetition across similar pages with pause and page-turn cues.
7. Apply the companion template, verify page counts and generate the final PPTX.

After receiving a file, the skill briefly confirms the output, language direction, narrative approach and factual boundaries before full generation. Naming, folder creation, template application and basic checks are automated. Page-level language, rhythm and professional judgment remain model work.

### Cross-disciplinary use

| Field | Possible emphasis |
| --- | --- |
| Landscape, architecture, interiors | Spatial sequence, circulation, zoning, materials, details, lighting and operation |
| Branding, visual identity, packaging | Meaning, graphic origin, type, color, layout and touchpoint consistency |
| Industrial products | Users, pain points, structure, appearance, materials, interaction and maintenance |
| Sculpture and public art | Site, viewing paths, scale, fabrication and public interaction |
| Cultural/tourism and public projects | Audiences, resources, themes, routes, operation, phasing and decisions |

<a id="installation"></a>

## Installation

1. Download the complete repository with **Code → Download ZIP** and extract it.
2. Ask Codex to inspect the folder, identify your existing skills directory and install the package.
3. For manual installation, copy the folder containing SKILL.md there as **design-report-companion**.
4. Keep the template, preview, references and scripts with the skill.
5. Restart Codex or open a new chat if needed, then invoke TalkTrack / 顺页讲.

Use the existing configured skills directory and avoid duplicates.

## What's Inside

| Item | Purpose |
| --- | --- |
| [SKILL.md](SKILL.md) | Entry point and speaking standard |
| [agents/openai.yaml](agents/openai.yaml) | Skill display information |
| [assets/brand/](assets/brand/) | Logo and icon assets |
| [assets/shunyejiang-template.pptx](assets/shunyejiang-template.pptx) | Companion template |
| [assets/template-preview.jpg](assets/template-preview.jpg) | Template preview |
| [references/](references/) | Writing, tone, planning and automation guidance |
| [scripts/](scripts/) | Generation, rendering and page-plan validation |

Main helpers: build_companion_ppt.py, render_companion_ppt.py, render_companion_pdf.py and validate_page_plan.py.

<a id="limitations"></a>

## Limitations

Concept framing, transitions and summaries can be developed from the source. Specific materials, brands, dimensions, processes, budgets, approvals, client opinions and final decisions must be visible or documented before being stated as project facts.

Implementation pages provide a speaking framework and professional prompts, leaving room for the designer's project knowledge. The companion does not replace professional review or final project wording.

## Updates and Feedback

Development focuses on discipline-specific expression, reliable template output and useful presentation styles. Feedback on unclear materials, details, parameters, costs or decisions informs the relevant rules.

This branding/documentation update preserves the existing behavior, templates and generation scripts.

## About

TalkTrack turns a visual proposal into a page-synced companion the speaker can follow.

[简体中文 documentation](README_CN.md) · [Map2Model](https://github.com/RuiqiWang-LGD/Map2Model) · [Insight-Space](https://github.com/RuiqiWang-LGD/Insight-Space)
