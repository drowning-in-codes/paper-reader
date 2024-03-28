import os, json

from flask import Flask, request, render_template, jsonify
from dotenv import load_dotenv

from werkzeug.exceptions import HTTPException

try:
    from arxiv_api import ArxivParser
except:
    from paper_reader_api.arxiv_api import ArxivParser


load_dotenv()
root_url = os.getenv("ROOT_URL")
app = Flask(__name__, static_url_path=f"/{root_url}/static")


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


@app.errorhandler(Exception)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    if isinstance(e, HTTPException):
        response = e.get_response()
        # replace the body with JSON
        response.data = json.dumps(
            {
                "code": e.code,
                "name": e.name,
                "description": e.description,
            }
        )
        response.content_type = "application/json"
        return response
    return render_template("error.html", e=e), 500


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


@app.route(f"/{root_url}/api/<string:topic>")
def get_papers(topic):
    arxiv_parser = ArxivParser()
    max_results = request.args.get("max_results", 10, type=int)
    start = request.args.get("start", 0, type=int)
    id_list = request.args.get("id_list", None)
    mdata, paper_data_list = arxiv_parser.search(
        all_=topic, max_results=max_results, start=start, id_list=id_list
    )
    return {"metadata": mdata, "paperdata": paper_data_list}


@app.route(f"/{root_url}/result")
def get_page():
    topic = request.args.get("topic", type=str, default="computer science")
    max_results = request.args.get("max_result", 10, type=int)
    if max_results < 0:
        app.logger.error("max_results should be positive")
        return render_template("error.html")
    arxiv_parser = ArxivParser()
    start = request.args.get("start", 0, type=int)
    id_list = request.args.get("id_list", None)
    sort_order = request.args.get("sort_order", "descending", type=str)
    sort_by = request.args.get("sort_by", "relevance", type=str)

    mdata, paper_data_list = arxiv_parser.search(
        all_=topic,
        max_results=max_results,
        start=start,
        id_list=id_list,
        sort_order=sort_order,
        sort_by=sort_by,
    )
    return render_template(
        "paper.html",
        metadata=mdata,
        paperdata=paper_data_list.papers,
        root_url=root_url,
    )
