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

The dataset is generated for academic use and contains simulated maintenance work-order records. It does not contain real customer, employee, technician, property, or asset data. The notebook uses the repository's deterministic generator to create the CSV with a fixed random seed when the file is not already present.

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

## Bias Awareness

Poor data cleaning can introduce bias by changing which records remain in the analysis or by masking differences between groups. For example, deleting every row with a missing value could remove some asset types or priority levels more often than others if documentation quality is uneven. Imputation can also reduce natural variation and make the data appear more complete than it really is. This project therefore preserves the raw dataset, documents each cleaning rule, uses transparent transformations, and treats the cleaning logic as dataset-specific assumptions rather than universal rules.

## Future Integration Reflections

### How the workflow would change for machine learning

For a machine-learning extension, I would separate features from the prediction target, create leakage-safe train/validation/test splits, fit preprocessing only on training data, compare multiple baseline models, tune only on training/validation data, and reserve the final test set for one locked evaluation. I would also exclude post-outcome fields such as `resolution_hours` from intake-time prediction because they are not available when a work order is first created.

### How I would prepare the data for a neural network

For a neural-network workflow, I would encode categorical variables numerically, scale continuous variables where appropriate, handle missing values consistently, and create fixed train/validation/test tensors or arrays. I would also monitor class imbalance, use suitable loss functions and evaluation metrics, and keep the preprocessing pipeline reproducible so training and inference use the same transformations.

### How agentic automation could build on this workflow

An agentic maintenance system could use this data workflow as one stage in a larger human-in-the-loop process. A future agent could gather an incoming maintenance description, validate required information, call classification or priority models, retrieve relevant asset context, summarize the evidence, and route the request to a qualified person for review or action. High-consequence decisions should remain subject to explicit human approval rather than being made autonomously.

## Development History

This repository is a focused, rubric-compliant extraction of the first stage of a larger maintenance-intelligence capstone. The original work was developed iteratively in the broader [maintenance-ml-priority-prediction](https://github.com/peymangraph/maintenance-ml-priority-prediction) repository, which contains the extended statistical analysis, applied machine learning, NLP, and integration work. This dedicated repository keeps the Project 1 submission concise while preserving a direct link to the broader engineering history.

The submission repository itself also includes multiple commits and an additional `feature/data-workflow` branch to demonstrate version-controlled development for this module.

## Submission Files

- `data_workflow.ipynb`
- `module_summary.pdf`
- `requirements.txt`
- `README.md`
- dataset CSV used by the notebook

## Related Project

This repository is the focused Programming Foundations submission. The broader maintenance-intelligence capstone continues in [maintenance-ml-priority-prediction](https://github.com/peymangraph/maintenance-ml-priority-prediction), which contains later statistical analysis, machine learning, NLP, and integration work.
