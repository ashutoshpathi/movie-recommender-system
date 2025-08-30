# 🎬 Movie Recommendation System  

This project is a simple **content-based movie recommender** built with **Python** and **Streamlit**.  
It suggests movies similar to the one you select, using a precomputed similarity matrix and poster data from **The Movie Database (TMDB) API**.  

---

## 🚀 Features  
- Pick a movie from the dropdown and get 5 similar recommendations.  
- Movie posters and titles displayed side-by-side in a clean UI.  
- Powered by cosine similarity on movie metadata.  
- Interactive web app built with Streamlit.  

---

## 🛠️ Tech Stack  
- **Python** (pandas, pickle, requests)  
- **Streamlit** for the UI  
- **TMDB API** for fetching movie posters  

---

## 📂 Data Files  
This project needs two pickle files that are too large for GitHub. Download them here:  

- [📥 movies.pkl](https://drive.google.com/file/d/1IbVRD9dU1yH9QPc7afyi2EsG8e9lKNrE/view?usp=sharing)  
- [📥 similarity.pkl.gz](https://drive.google.com/file/d/1Zt0vXYNOgN_IyRmOGv3S813LKy1U7mZJ/view?usp=sharing)  

After downloading, place them in the project’s root directory (same folder as `app.py`).  

--- 

## 🔑 Note
You’ll need a TMDB API key. Store it in a .env file as:
TMDB_API_KEY=your_api_key_here

Install dependencies:
pip install -r requirements.txt

Run the app:
streamlit run app.py


---

## ▶️ Run Locally  
Clone the repo:  
```bash
git clone https://github.com/ashutoshpathi/movie-recommendation-system.git
cd movie-recommendation-system

