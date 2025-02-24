from flask import Flask, redirect

app = Flask(__name__)

database = {
    "github": "https://github.com/kausar2nd",
    "linkedin": "https://www.linkedin.com/in/kausar2nd/",
    "portfolio": "https://kausar2nd.github.io/",
    "alteruse": "https://alteruse.jobair-hossain.info/",
    "schedulumos": "https://cpuscheduler.vercel.app/",
    "schedulumos-gh": "https://github.com/kausar2nd/ScheduLumos",
}


@app.route("/")
def home():
    return 'Welcome to ReDirected! To know more about the project, visit: "https://github.com/kausar2nd/ReDirected"'


@app.route("/<keyword>")
def redirect_to_user_url(keyword):
    link = database.get(keyword)

    if link:
        return redirect(link)
    else:
        return "URL not found", 404


if __name__ == "__main__":
    app.run(debug=True)
