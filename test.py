import pandas as pd
import joblib
import os

# load the model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, 'model', 'trained_model.pkl')
model = joblib.load(model_path)


print(f"Model loaded successfully!")
print(f"Type 'exit' to exit prediction testing!\n")

while True:
    review = input(f"Enter review text:\n")
    if review.lower() == 'exit':
        print(f"Disconnecting...")
        break

    

    # create a dataframe from input
    user_input = pd.DataFrame([{
        'review': review
    }])

    # predict sentiment
    prediction = model.predict(user_input)[0]
    print(f"Predicted category: {prediction}\n" + "-" * 30)