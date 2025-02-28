
# UFO Sighting Prediction Web App 🚀

Welcome to the **UFO Sighting Prediction Web App**! This project is a machine learning-based web application that predicts the **country** of a UFO sighting based on input features: `seconds`, `latitude`, and `longitude`.

---

## 🌌 Project Overview

The goal of this project was to combine machine learning with web app development to create an interactive tool for UFO sighting predictions. This was an exciting challenge that helped bridge the gap between data science models and real-world applications.

The **model accuracy** achieved is **96%**, making it a reliable tool for predictions.

---

## 🧰 Features

- **Prediction**: Input UFO sighting details (seconds, latitude, longitude) and get the predicted country.
- **Interactive Web App**: User-friendly interface for easy interaction with the ML model.
- **High Accuracy**: The ML model has been trained to predict UFO sighting countries with precision.

---

## 📂 Project Structure

```
UFO-Sighting-Prediction-WebApp/
├── app/
│   ├── templates/           # HTML files for the web app interface
│   ├── static/              # Static files (CSS, images, etc.)
│   ├── app.py               # Flask app backend
├── model/
│   ├── ufo_model.pkl        # Trained ML model (96% accuracy)
│   ├── preprocessing.py     # Data preprocessing and feature engineering
├── data/
│   ├── ufo_dataset.csv      # UFO sightings dataset
├── README.md                # Project README file
└── requirements.txt         # Python dependencies
```

---

## 🚀 Getting Started

### Prerequisites
To run this project locally, ensure you have the following installed:
- Python 3.8+
- Flask
- Scikit-learn
- Pandas
- Numpy

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/UFO-Sighting-Prediction.git
   cd UFO-Sighting-Prediction
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask app:
   ```bash
   python app.py
   ```

4. Open the app in your browser:
   Navigate to `http://127.0.0.1:5000/`.

---

## 📊 Dataset

The model was trained on a dataset containing UFO sighting data, including:
- **Seconds**: Duration of the sighting.
- **Latitude & Longitude**: Coordinates of the sighting.
- **Country**: The target variable for prediction.

### Data Preprocessing
- Missing values were handled.
- Latitude and longitude were standardized.
- The dataset was split into training and testing sets for model evaluation.

---

## 🧠 Machine Learning Model

The machine learning pipeline includes:
1. **Data Preprocessing**: Feature scaling and encoding.
2. **Model Training**: A classification model was trained using scikit-learn.
3. **Evaluation**: Achieved an accuracy of **96%** on the test set.

---

## 🎨 Web App Features

The web app is built using **Flask**, with:
- **HTML/CSS** for the front-end.
- **Python (Flask)** for the back-end integration with the ML model.

### How to Use the App
1. Enter the UFO sighting details:
   - Duration in seconds.
   - Latitude.
   - Longitude.
2. Click "Predict."
3. The app will display the predicted country of the UFO sighting.

---

## 📚 Lessons Learned

- **Machine Learning to Web App Deployment**: Bridging the gap between ML and web development.
- **Debugging and Problem-Solving**: Tackling issues during development.
- **Model Deployment**: Serving predictions from an ML model in real time.

---

## 🌟 Future Work

- Add more features for prediction, such as weather or time of the sighting.
- Improve the web app design for better user experience.
- Expand the dataset to include more global sightings.

---

## 💻 Technologies Used

- **Programming Languages**: Python, HTML, CSS
- **Frameworks**: Flask
- **Machine Learning**: Scikit-learn
- **Tools**: Pandas, Numpy

---

## 📬 Contact

If you have any questions or suggestions, feel free to reach out:

-
- **Email**: lekanolawale477@gmail.com

---

## 🙌 Acknowledgments

Special thanks to:
- The creators of the UFO dataset.
- Online resources and tutorials that guided this project.
- My determination to never give up during debugging. 😅

```

Let me know if you'd like to adjust the structure or add/remove any sections!
