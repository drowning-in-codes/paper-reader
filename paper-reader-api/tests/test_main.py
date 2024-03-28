import json
from dataclasses import dataclass
from flask import jsonify
from typing import Optional
from paper_reader_api.data import MetaData, AuthorData, PaperData, PaperDataList


def test_get_papers():

    pdatalist = PaperDataList(papers=[])
    pdata = PaperData(
        paper_id="arXiv:2106.00001",
        updated="adss",
        published="published",
        title="title",
        summary="summary",
        author=AuthorData(name="author_name", affiliation="affiliation"),
        doi="None",
        category=["cats"],
        pdf_link="ad",
    )
    pdatalist.papers.append(pdata)
    print(pdatalist.to_json())
