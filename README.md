# 🎬 Movie Recommendation System

## 📌 Overview

This project is a **Movie Recommendation System** that suggests movies similar to the one selected by the user. It helps users discover new movies based on their interests, reducing the effort of searching through large collections.

The system uses techniques from Machine Learning to analyze movie genres and recommend similar content.

---

## 🚀 Features

* Recommend movies based on similarity
* Simple and interactive user interface
* Netflix-style UI design
* Fast and efficient recommendations
* Beginner-friendly implementation

---

## 🧠 How It Works

1. The dataset contains movie titles and their genres
2. Genres are converted into numerical form using TF-IDF
3. Cosine similarity is used to measure similarity between movies
4. Based on similarity, the system recommends top matching movies

---

## 📂 Project Structure

```
movie-recommendation-system/
│── main.py              # Builds similarity model
│── app.py               # Streamlit web app
│── movies.csv           # Dataset
│── similarity.pkl       # Saved similarity matrix
│── movies.pkl           # Saved dataset
│── requirements.txt     # Dependencies
│── README.md            # Documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Train the Model

```
python main.py
```

### 4️⃣ Run the Application

```
streamlit run app.py
```

---

## 🌐 Usage

* Select a movie from the dropdown
* Click on **Recommend**
* View similar movie suggestions

---

## 📊 Example

**Input:** Inception
**Output:** Interstellar, The Matrix, Tenet, etc.

---

## ⚠️ Limitations

* Recommendations are based only on genre
* No personalization based on user history
* Uses a synthetic dataset

---

## 🚀 Future Improvements

* Use real-world datasets (IMDb, TMDB)
* Add user-based collaborative filtering
* Include ratings and reviews
* Add movie posters and trailers
* Deploy the app online

---

## 🛠️ Tech Stack

* Python
* Pandas
* Scikit-learn
* Streamlit
* Joblib

---

## 👨‍💻 Author

**Pratyush Jaiswal**</br>
**25BAI11065**

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
