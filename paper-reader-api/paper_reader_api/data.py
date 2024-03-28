from typing import Optional
from dataclasses import dataclass
import json


@dataclass
class MetaData:
    """metadata of results"""

    updated_time: str
    total_result: int
    items: int

    def to_json(self):
        return json.dumps(self.__dict__, ensure_ascii=False)


@dataclass
class AuthorData:
    """data of author"""

    name: str
    affiliation: Optional[str]

    def to_json(self):
        return json.dumps(self.__dict__, ensure_ascii=False)


@dataclass
class PaperData:
    """data of paper"""

    paper_id: str
    updated: str
    published: str
    title: str
    summary: str
    author: AuthorData
    doi: Optional[str]
    category: list[str]
    pdf_link: str

    def to_json(self):
        return json.dumps(
            self.__dict__,
            default=lambda o: o.__dict__,
            ensure_ascii=False,
            encoding="utf-8",
            skipkeys=True,
        )


@dataclass
class PaperDataList:
    papers: list[PaperData]

    def to_json(self):
        return json.dumps([paper.to_json() for paper in self.papers])
