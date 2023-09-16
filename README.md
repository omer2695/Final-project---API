# Final Project – API Service for Business Property Scoring

I designed a REST API service that calculates potential scores for business properties by consuming data from various sources and utilizing a decision tree model in Python.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)


### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher
- Flask
- scikit-learn

### Installation

To install and set up the project locally, follow these steps:
   ```shell
   git clone https://github.com/yourusername/business-property-scoring.git
   ```

1. Navigate to the project directory:
```shell
   cd business-property-scoring
   ```
2. Install the required dependencies:
```shell
   pip install -r requirements.txt
```

3. Run the API service:
```shell
   python main.py
```

## Usage
To use the API service, send POST requests to the following endpoint:

/predict: Endpoint for making predictions. Send a POST request with JSON data containing property information to receive a score prediction.
Example JSON request:
```shell
{
  "areaCategory": 1,
  "Floor": 0,
  "Storage": 0,
  "publicTransport": 1,
  "publicParking": 1
}
```

## Example JSON response:

```shell
{
  "prediction": 1
}
```

| prediction  | predictionStatus |
| ------------- | ------------- |
| 0  | bad  |
| 1  | good  |
| 2  | very good  |


## Project Structure
The project is structured as follows:

- data_preprocessing.py: Module for loading and preprocessing the dataset.
- model.py: Module for building and training the decision tree model.
- Rest_Api.py: Main file for the REST API service using Flask.
- main.py: Script to run the API service.
- dataset.csv: Dataset file (if applicable).
- requirements.txt: List of required Python packages.











   
