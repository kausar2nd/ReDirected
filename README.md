# ReDirected: My Personalized URL Shortener  

A simple URL shortener for managing and showcasing my profiles and projects in a fancy way.  

## What is this?  

ReDirected lets me use short, memorable URLs to link to my GitHub, LinkedIn, portfolio, and projects. For example:  
- [k4r.vercel.app/github](https://k4r.vercel.app/github) → My GitHub profile  
- [k4r.vercel.app/portfolio](https://k4r.vercel.app/portfolio) → My Portfolio  

## How It Works  

1. Keywords and URLs are defined in the `database` dictionary in `app.py`.  
2. Visiting a keyword-based URL redirects to the corresponding link.  

Example:  
```python
database = {
    "github": "https://github.com/kausar2nd",
    "portfolio": "https://kausar2nd.github.io/"
}
```
Visiting `k4r.vercel.app/github` redirects to my GitHub profile.  

## How to Set It Up  

1. **Clone the Repository**:  
    ```bash
    git clone https://github.com/kausaraahmed/ReDirected
    cd ReDirected
    ```

2. **Customize Your Links**:  
    - Edit the `database` dictionary in `app.py` to include your own keywords and URLs.  

3. **Run Locally**:  
    ```bash
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    python app.py
    ```
    Access it at `http://127.0.0.1:5000/`.  

4. **Deploy**:  
    - Host it on Vercel (or any other platform supporting Flask apps).  

## Want to Adapt It?  

Feel free to fork this repo and modify the links for your own profiles and projects!  

**Happy Redirecting! 🚀**  