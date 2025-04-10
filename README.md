# cloud-gaming-latency-prediction
This repository contains a latency prediction model for cloud gaming networks, utilizing machine learning techniques to analyze and predict network latency based on real-world dataset measurements.

#📊 Dataset
The dataset used in this project is from IEEE Dataport and contains network delay measurements between 189 players and 9 servers across multiple regions: North America, South America, Europe, and East Asia. The cleaned data can be found in data/processed/main_dataset_cleaned.csv.

#🚀 Running the Project
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