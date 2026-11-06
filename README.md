# Cloud Gaming Latency Prediction

[![DOI](https://img.shields.io/badge/DOI-10.1109%2FICAICCIT64383.2024.10912118-blue)](https://doi.org/10.1109/ICAICCIT64383.2024.10912118)
[![IEEE](https://img.shields.io/badge/IEEE-ICAICCIT%202024-00629B)](https://doi.org/10.1109/ICAICCIT64383.2024.10912118)

This repository contains a latency prediction model for cloud gaming networks, utilizing machine learning techniques to analyze and predict network latency based on real-world dataset measurements.

# 📄 Publication
This project is associated with the following peer-reviewed IEEE conference paper:

> J. Tanveer, S. K. Abbas, M. Z. Hasan, M. Z. Hussain, A. Khalid, **A. Ahmad**, M. A. Yaqub, S. H. Chuhan, M. Mustafa and Z. Ali, "Advancing Cloud Gaming: Addressing Latency Challenges through Research and Innovative Solutions," *2024 2nd International Conference on Advances in Computation, Communication and Information Technology (ICAICCIT)*, 2024, pp. 1284–1289, doi: [10.1109/ICAICCIT64383.2024.10912118](https://doi.org/10.1109/ICAICCIT64383.2024.10912118).

- IEEE Xplore: https://doi.org/10.1109/ICAICCIT64383.2024.10912118
- ResearchGate: https://www.researchgate.net/publication/389839371

<details>
<summary>BibTeX</summary>

```bibtex
@inproceedings{tanveer2024advancing,
  title     = {Advancing Cloud Gaming: Addressing Latency Challenges through Research and Innovative Solutions},
  author    = {Tanveer, Jahanzaib and Abbas, Syed Khizar and Hasan, Muhammad Zulkifl and Hussain, Muhammad Zunnurain and Khalid, Aqsa and Ahmad, Atique and Yaqub, Muhammad Atif and Chuhan, Saad Hussain and Mustafa, Muzammil and Ali, Zafar},
  booktitle = {2024 2nd International Conference on Advances in Computation, Communication and Information Technology (ICAICCIT)},
  pages     = {1284--1289},
  year      = {2024},
  doi       = {10.1109/ICAICCIT64383.2024.10912118}
}
```
</details>

# 📊 Dataset
The dataset used in this project is from IEEE Dataport and contains network delay measurements between 189 players and 9 servers across multiple regions: North America, South America, Europe, and East Asia. The cleaned data can be found in data/processed/main_dataset_cleaned.csv.

# 🚀 Running the Project
1. Preprocess Data
Run the preprocessing steps to clean and prepare the dataset:
```
python src/preprocess.py
```
2. Train Models
Train the models (Linear Regression, Random Forest, Gradient Boosting):
```
python src/train.py
```
3. Evaluate Models
Evaluate model performance and visualize the results:
```
python src/evaluate.py
```
4. Run the Entire Pipeline
To run the full pipeline from preprocessing to evaluation, simply run:
```
python src/main.py
```