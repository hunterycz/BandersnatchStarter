# imports
from sklearn.ensemble import RandomForestClassifier
import joblib
from datetime import datetime


class Machine:

    def __init__(self, df):
        '''
        Initialize the Machine object. Creates a model using sklearn
        RandomForestClassifier() class.

        Parameter(s):
        df: A Pandas DataFrame
        '''

        # save df to the self.dataframe
        self.dataframe = df

        # split columns into target and features
        target = df['Rarity']
        features = df.drop(columns=['Rarity'])

        # instantiate a RandomForestClassifier()
        # and save it to self.model
        self.model = RandomForestClassifier(
            max_features=3,
            n_estimators=200
        )

        # fit the model to the target and feature data sets
        self.model.fit(features, target)

        # save the time the model was created
        self.datetime = datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")

        # save what type of model was used
        self.model_type = "Random Forest Classifier"

    def __call__(self, feature_basis):
        '''
        Uses the model either from the 'model.joblib' file
        or the model instantiated in the init method and returns
        the prediction and the confidence (e.g. estimated probability).

        Parameter(s):
            feature_basis: A Pandas DataFrame with the data to
                           to make a prediction and get the confidence'
        '''
        # get prediction array from the model
        prediction = self.model.predict(feature_basis)

        # save the biggest confidence percent to variable 'confidence'
        confidence = self.model.predict_proba(feature_basis).max()

        # return both the prediction and confidence
        return prediction, confidence

    def save(self, filepath):
        '''
        Saves the model and created a 'model.joblib' file
        in the Bandersnatchstarter directory for future use.

        Parameter(s):
            filepath: A string of the location where to save
                      the model using the joblib library
        '''

        # use the dump() function to save the self.model
        # to the Bandersnatchstarter directory
        joblib.dump(self.model, filepath)

    @staticmethod
    def open(filepath):
        '''
        Opens and returns the model from the saved filepath.

        Parameter(s):
            filepath: A string of the location where to save
                      the model using the joblib library
        '''

        # use the load() to open the model in the filepath
        # indicted and save to variable self.model
        model = joblib.load(filepath)

        # return Machine.model
        return model

    def info(self):
        '''
        Returns the name of the model in a string with
        the date and time of when the model was created.
        '''

        return f"Base Model: {self.model_type}<br>\
                 Timestamp: {str(self.datetime)}"
