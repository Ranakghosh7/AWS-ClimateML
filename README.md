# SmartPredict

SmartPredict is a Python script (`main.py`) that trains a machine learning model to predict a target variable from a dataset.  
It uses the Random Forest Regressor from `scikit-learn` and evaluates performance with R² and Mean Absolute Error (MAE).  
Feature importance is saved automatically to a CSV file for analysis.  

I developed this project after completing the IBM Python for AI and Development course to apply my learning to practical problems and demonstrate skills in data preprocessing, model training, evaluation, and feature analysis.  

To use it:  
1. Place your dataset CSV in the same folder as `main.py` with the target column specified.  
2. Run `python main.py`.  
3. The model will train, evaluate, and generate `feature_importance.csv`.  

Requirements: Python 3.x, `pandas`, and `scikit-learn` (`pip install pandas scikit-learn`).  

Created by [Ranak Ghosh](https://github.com/Ranakghosh7).  
