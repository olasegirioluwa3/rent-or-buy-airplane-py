import pandas as pd
from pycaret.classification import *

# Step 1: Load your data
dataset = pd.read_csv('fullraw.csv')

# Step 2: Initialize PyCaret Setup
clf = setup(data=dataset, target='timestamp')

# Step 3: Compare Models and Select the Best One
best_model = compare_models()

# Step 4: Create a Specific Model (if desired)
decision_tree = create_model('dt')

# Step 5: Tune the Model (if desired)
tuned_decision_tree = tune_model(decision_tree)

# Step 6: Evaluate the Model
evaluate_model(tuned_decision_tree)

# Step 7: Make Predictions on New Data
new_data = pd.read_csv('new_data.csv')
predictions = predict_model(tuned_decision_tree, data=new_data)

# You can save the trained model and deploy it to production as needed.
save_model(tuned_decision_tree, 'your_model_name')

