# IPL Score Prediction

## Overview
This project uses data from IPL matches from 2008 till 2017 to predict the scores of matches. It leverages machine learning techniques to analyze factors like venue, batting team, bowling team, batsman, and bowler, integrating these into a predictive model that outputs the likely total score for a given set of match conditions.

## How It Works

### Data Handling
- **Data Loading**: The project begins by loading the IPL dataset from a CSV file into a Pandas DataFrame.
- **Initial Visualization**: It visualizes the distribution of total scores in the dataset using a histogram to understand the typical score ranges and their frequency.
- **Feature Selection and Cleaning**: Unnecessary features such as specific match details that don't contribute to score prediction (e.g., date, wickets, overs) are dropped to streamline the model.

### Feature Engineering
- **Label Encoding**: Categorical variables like `venue`, `batting_team`, `bowling_team`, `batsman`, and `bowler` are transformed into numerical formats using Label Encoding. This process converts each category into a unique integer.
- **Feature Scaling**: All features are scaled using MinMaxScaler to ensure that the model is not biased towards variables with higher magnitude.

### Model Building
- **Neural Network Architecture**: The model is constructed using TensorFlow's Keras library. It consists of a sequence of densely connected layers, specifically designed to process the input features and predict the output score.
- **Model Training**: The neural network is trained on the processed data, learning to map the relationship between match conditions and final scores.

### Prediction
- **Score Prediction Function**: This function takes user inputs for match conditions, preprocesses them in the same way as the training data, and then uses the trained model to predict the score.
- **Accuracy Checking**: The model's accuracy is evaluated using the Mean Absolute Error (MAE) metric on the test set, providing an indication of how close the predictions are to the actual scores.

### Interactive GUI
- **User Interface**: Using IPython widgets, a simple GUI is provided for users to select match conditions from dropdown menus. The GUI includes interactive elements that let users input their own conditions and receive score predictions.

### Code Modules
This project is divided into several modules, each handling a specific aspect of the application:
- `app.py`: This is the main executable script that launches the user interface for the application. It integrates all other components and provides an interactive GUI for users to input match conditions and receive score predictions.
- `data_preparation.py`: Handles the initial loading, cleaning, and preliminary preprocessing of the IPL dataset. This module prepares the data by removing unnecessary columns and resolving any inconsistencies.
- `ipl_data.csv`: The dataset file containing historical data from IPL matches. It includes various features such as match venue, teams, players involved, scores, and other relevant match details.
- `model.py`: Contains the definition and training of the machine learning model. This module uses TensorFlow to construct a neural network that learns to predict the total score of a match based on the processed input features.
- `preprocessing.py`: Focuses on preparing the data for modeling. This includes scaling numerical features and encoding categorical features using techniques like MinMaxScaler and LabelEncoder, respectively.
- `requirements.txt`: A text file listing all the dependencies needed to run the project. This ensures that anyone setting up the project can install the necessary Python packages easily.
