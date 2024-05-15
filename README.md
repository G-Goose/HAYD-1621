## Project Overview
The backend repository of How Are You Doing (hayd-1621) supports the emotion detection web application. It handles image analysis using the ResNet50 deep learning model, interacts with Google Big Query for data storage, and provides API endpoints for the frontend.

## Setup Instructions
1. Clone the repository:

> git clone git@github.com:G-Goose/HAYD-1621.git

2. Install dependencies:

> pip install -r /path/to/requirements.txt

3. Run the application:

> make run_api

See make file for options to dockerize and deploy the backend to Google Cloud.

3. Set up environment variables for Google Big Query access.

## API Endpoints
- **/upload_your_nice_face**: Receives images for mood analysis and returns the top or top two corresponding moods
- **/save_to_bq**: Saves the integer value of the mood to the Google Big Query Dataset
- **/fetch_mood_board**: Fetches the mood history from Big Query

## Connection to Big Query
Ensure you have the appropriate credentials and environment variables set for Google Big Query to store and retrieve mood data.

## Model Information
The backend uses the ResNet50 model pre-trained on facial datasets for emotion detection.

## Technologies Used
- FastAPI for the API
- TensorFlow for the deep learning model
- Google Big Query

## Contributing
Contributions to improve the backend are encouraged. Please fork the repository and submit pull requests with your proposed changes.
