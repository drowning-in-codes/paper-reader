import os
import sys

from flask import Flask, request, render_template
from .config import SQLALCHEMY_DATABASE_URI
from .arxiv_api import ArxivParser
from .dbmodel import db

app = Flask(__name__)
# WIN = sys.platform.startswith("win")
# if WIN:  # 如果是 Windows 系统，使用三个斜线
#     prefix = "sqlite:///"
# else:  # 否则使用四个斜线
#     prefix = "sqlite:////"
# app.config["SQLALCHEMY_DATABASE_URI"] = prefix + os.path.join(
#     app.root_path, SQLALCHEMY_DATABASE_URI
# )
# initialize the app with the extension
# db.init_app(app)


@app.route("/paper/api/<string:topic>")
def get_papers(topic):
    arxiv_parser = ArxivParser()
    max_results = request.args.get("max_results", 10, type=int)
    start = request.args.get("start", 0, type=int)
    id_list = request.args.get("id_list", None)
    mdata, paper_data_list = arxiv_parser.search(
        all_=topic, max_results=max_results, start=start, id_list=id_list
    )
    return {"metadata": mdata, "paperdata": paper_data_list}


@app.route("/paper/result")
def get_page():
    arxiv_parser = ArxivParser()
    topic = request.args.get("topic", type=str, default="computer science")
    max_results = request.args.get("max_results", 10, type=int)
    start = request.args.get("start", 0, type=int)
    id_list = request.args.get("id_list", None)
    mdata, paper_data_list = arxiv_parser.search(
        all_=topic, max_results=max_results, start=start, id_list=id_list
    )
    return render_template(
        "paper.html", metadata=mdata, paperdata=paper_data_list.papers
    )
