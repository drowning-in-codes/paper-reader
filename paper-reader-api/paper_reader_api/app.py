from .arxiv_api import ArxivParser
from flask import Flask, jsonify, request
from dataclasses import asdict

app = Flask(__name__)


@app.route("/paper/<string:topic>")
def get_papers(topic):
    arxiv_parser = ArxivParser()
    max_results = request.args.get("max_results", 10, type=int)
    start = request.args.get("start", 0, type=int)
    id_list = request.args.get("id_list", None)
    mdata, paper_data_list = arxiv_parser.search(
        all_=topic, max_results=max_results, start=start, id_list=id_list
    )

    return {"metadata": mdata, "paperdata": paper_data_list}
