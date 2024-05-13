import requests
from dagster import asset, multi_asset, AssetOut
import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

@asset
def hackernews_stories():
    df = pd.read_csv("hackernews_stories.csv")
    if len(df) > 0:
        df = df[df.type == "story"]
        df = df[~df.title.isna()]
    return df


@multi_asset(outs={"training_data": AssetOut(), "test_data": AssetOut()})
def training_test_data(hackernews_stories):
    X = hackernews_stories.title
    y = hackernews_stories.descendants
    # Split the dataset to reserve 20% of records as the test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    return (X_train, y_train), (X_test, y_test)


@multi_asset(
    outs={"tfidf_vectorizer": AssetOut(), "transformed_training_data": AssetOut()}
)
def transformed_train_data(training_data):
    X_train, y_train = training_data
    # Initiate and fit the tokenizer on the training data and transform the training dataset
    vectorizer = TfidfVectorizer()
    transformed_X_train = vectorizer.fit_transform(X_train)
    transformed_X_train = transformed_X_train.toarray()
    y_train = y_train.fillna(0)
    transformed_y_train = np.array(y_train)
    return vectorizer, (transformed_X_train, transformed_y_train)


@asset
def transformed_test_data(test_data, tfidf_vectorizer):
    X_test, y_test = test_data
    # Use the fitted tokenizer to transform the test dataset
    transformed_X_test = tfidf_vectorizer.transform(X_test)
    y_test = y_test.fillna(0)
    transformed_y_test = np.array(y_test)
    return transformed_X_test, transformed_y_test


@asset
def linear_regression_model(transformed_training_data):
    transformed_X_train, transformed_y_train = transformed_training_data
    # Train Linear Regression model
    model = LinearRegression()
    model.fit(transformed_X_train, transformed_y_train)
    return model


@asset
def model_test_set_score(transformed_test_data, linear_regression_model):
    transformed_X_test, transformed_y_test = transformed_test_data
    # Use the test set data to get a score of the Linear Regression model
    score = linear_regression_model.score(transformed_X_test, transformed_y_test)
    return score


@asset
def latest_stories():
    df = pd.read_csv("latest_stories.csv")
    if len(df) > 0:
        df = df[df.type == "story"]
        df = df[~df.title.isna()]
    return df


@asset
def latest_story_data(latest_stories, tfidf_vectorizer):
    inference_x = latest_stories.title
    # Transform the new story titles using the existing vectorizer
    inference_x = tfidf_vectorizer.transform(inference_x)
    return inference_x


@asset
def latest_story_comment_predictions(linear_regression_model, latest_story_data):
    return linear_regression_model.predict(latest_story_data)