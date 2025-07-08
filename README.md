

# 🎬 Movie Recommendation System

A personalized movie recommendation system built using Python, Streamlit, and machine learning techniques. This application helps users discover movies based on their preferences using collaborative filtering.

🔗 [Live App](https://movierecommendationsystemshravan.streamlit.app/)  
📁 [GitHub Repository](https://github.com/Shravan4598/Movie-Recommendation-System/tree/main)

---

## 🚀 Features

- 🔍 **Top 5 Movie Recommendations** based on selected titles.
- 📊 **Collaborative Filtering** using cosine similarity.
- 🖼️ Fetches **movie posters** using the TMDb API.
- 🧠 Powered by **Scikit-learn**, **Pandas**, and **Numpy**.
- 🖥️ Deployed using **Streamlit** for a clean, interactive UI.

---

## 📊 Dataset

This project uses movie metadata from the [TMDb Movie Metadata Dataset on Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).

---

## 🎥 Demo

![Movie Recommender Demo](https://github.com/Shravan4598/Shravan4598/blob/main/Movie-Recommendation.gif)

---

## 📂 Project Structure

```plaintext
Movie-Recommendation-System/
│
├── app.py                  # Main Streamlit app
├── data/
│   ├── movies.csv          # Movie metadata
│   └── similarity.pkl      # Precomputed similarity matrix
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
````

---

## 🧠 How It Works

1. User selects a movie from the dropdown menu.
2. Cosine similarity is used to find the most similar movies.
3. Top 5 similar movies are recommended.
4. Posters are fetched using TMDb API and displayed on the UI.

---

## 🛠️ Installation

To run this project locally:

```bash
git clone https://github.com/Shravan4598/Movie-Recommendation-System.git
cd Movie-Recommendation-System
pip install -r requirements.txt
streamlit run app.py
```

Make sure you have Python 3.7+ installed.

---

## 📦 Requirements

* Python 3.7+
* Streamlit
* Pandas
* Scikit-learn
* Requests

Install dependencies with:

```bash
pip install -r requirements.txt
```

---

## 🌐 Deployed Version

Explore the deployed web app here:
👉 **[Movie Recommendation System (Streamlit)](https://movierecommendationsystemshravan.streamlit.app/)**

---

## ✨ Credits

* Developed by **[Shravan Kumar Pandey](https://github.com/Shravan4598)**
* Dataset: [TMDb Movie Metadata - Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
* Posters and movie data from [The Movie Database (TMDb)](https://www.themoviedb.org/)

---

## 📃 License

This project is licensed under the [MIT License](LICENSE).

---

⭐ **If you found this project helpful, don't forget to give it a star!**



---
