# Nursing Research Toolkit

Open-source helper scripts and templates for nursing and clinical research workflows.

This repository is designed for researchers who need simple, reproducible tools for common nursing research tasks, including scale scoring, Delphi expert consultation summaries, and evidence-synthesis screening logs.

## Why this project exists

Many clinical nursing projects rely on repeated manual work in spreadsheets: calculating total and domain scores, summarising Delphi panel ratings, and documenting evidence-synthesis decisions. This toolkit provides small, transparent Python utilities and example files that make these workflows easier to inspect, reproduce, and adapt.

## Current features

- **Scale scoring**: calculate total scores and domain scores from a JSON configuration file.
- **Delphi consultation summary**: calculate mean, standard deviation, coefficient of variation, median, interquartile range, and item-level content validity index.
- **Evidence-synthesis screening log**: summarise include/exclude decisions and reasons.
- **Example data**: uses simulated demonstration data only.

## Who may find it useful

- Nursing researchers
- ICU and oncology nursing teams
- Graduate students preparing Delphi studies, scale-development studies, or scoping reviews
- Clinical research assistants who need auditable data-processing scripts

## Important privacy note

This repository does **not** include patient-identifiable information, hospital internal data, ethics documents, or real clinical datasets. Example files are synthetic and are provided only to demonstrate the workflow.

## Installation

```bash
git clone https://github.com/a1279034731-png/nursing-research-toolkit.git
cd nursing-research-toolkit
pip install -e .
```

If the repository has not yet been renamed, replace the clone URL with the current repository URL.

## Quick examples

### 1. Score a scale dataset

```bash
python -m nursing_research_toolkit.scale_scoring \
  --data examples/sample_scale_data.csv \
  --config examples/scale_config.json \
  --output examples/scored_scale_data.csv
```

### 2. Summarise Delphi expert ratings

```bash
python -m nursing_research_toolkit.delphi \
  --data examples/sample_delphi_panel.csv \
  --output examples/delphi_summary.csv
```

### 3. Summarise screening decisions

```bash
python -m nursing_research_toolkit.evidence \
  --data examples/sample_screening_log.csv \
  --output examples/screening_summary.csv
```

## Repository structure

```text
.
├── src/nursing_research_toolkit/
│   ├── scale_scoring.py
│   ├── delphi.py
│   └── evidence.py
├── examples/
├── tests/
├── docs/
└── README.md
```

## Roadmap

- Add Cronbach's alpha calculation for scale reliability testing.
- Add Kendall's W summary for Delphi consensus assessment.
- Add PRISMA-ScR screening-flow utilities.
- Add bilingual documentation for Chinese nursing researchers.

## Disclaimer

This project is for research workflow support and education. It is not a medical device, not clinical decision-support software, and should not be used to make patient-care decisions.

## License

MIT License. See `LICENSE` for details.
