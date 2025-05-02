# Crop and Fertilizer Recommendation System

This project uses Machine Learning to recommend suitable crops and fertilizers based on soil and environmental conditions.

## Datasets
- `crop.csv`: Contains soil nutrients (N, P, K), temperature, humidity, pH, and rainfall, with the target crop label.
- `fertilizer.csv`: Contains temperature, humidity, moisture, soil type, crop type, and nutrient levels, with recommended fertilizer.

##  Features
### Crop Recommendation
- Inputs: N, P, K, temperature, humidity, pH, rainfall
- Output: Best-suited crop
- Model: Random Forest Classifier

### Fertilizer Recommendation
- Inputs: Crop type, soil type, N, P, K levels
- Output: Recommended fertilizer
- Logic: Rule-based or ML model (depending on data)

##  Basic EDA
- `head()`, `tail()`, `describe()`, `isnull()`, `dtypes`, `unique()` values

##  Tech Stack
- Python (pandas, scikit-learn, matplotlib/seaborn for EDA)
- Jupyter Notebook or VS Code

##  How to Run
1. Place `crop.csv` and `fertilizer.csv` in your working directory.
2. Run the scripts for EDA and model training.
3. Input your soil/environment data to get recommendations.

##  Future Work
- building model 

---

