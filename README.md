# AI Programming Foundations Project

This repository contains my AI Programming Foundations capstone module submission. It implements a reproducible Python data workflow using a synthetic CMMS maintenance work-order dataset and covers ingestion, cleaning, exploratory analysis, visualization, interpretation, and reproducibility.

The broader continuation of this maintenance-intelligence project is maintained in the related repository: [maintenance-ml-priority-prediction](https://github.com/peymangraph/maintenance-ml-priority-prediction).

## What I Built

- A reproducible Jupyter Notebook data workflow
- Reusable data-cleaning functions with docstrings
- Exploratory data analysis functions
- At least three labeled Matplotlib/Seaborn visualizations
- A written academic summary with citations

## Dataset

**Dataset:** Synthetic CMMS Maintenance Work Orders

The dataset is generated for academic use and contains simulated maintenance work-order records. It does not contain real customer, employee, technician, property, or asset data.

## How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/peymangraph/ai-programming-foundations-project.git
cd ai-programming-foundations-project
```

2. Create and activate a Python environment.

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Open Jupyter Notebook or JupyterLab:

```bash
jupyter notebook
```

or

```bash
jupyter lab
```

5. Open `data_workflow.ipynb` and run all cells from top to bottom.

## Reproducibility

The project uses a documented dependency file and Git version control. To regenerate the dependency snapshot from the active project environment, use:

```bash
pip freeze > requirements.txt
```

## Submission Files

- `data_workflow.ipynb`
- `module_summary.pdf`
- `requirements.txt`
- `README.md`
- dataset CSV used by the notebook

## Related Project

This repository is the focused Programming Foundations submission. The broader maintenance-intelligence capstone continues in [maintenance-ml-priority-prediction](https://github.com/peymangraph/maintenance-ml-priority-prediction), which contains later statistical analysis, machine learning, NLP, and integration work.
