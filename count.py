from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
  fname = "README.md"
  c = 0
  with open(fname, 'r') as f:
      for line in f:
          c += 1

  return render_template("index.html", variable=c)

if __name__ == "__main__":
  app.run()
