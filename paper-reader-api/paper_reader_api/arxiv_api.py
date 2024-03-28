from datetime import datetime
from typing import Optional
from .data import MetaData, AuthorData, PaperData, PaperDataList
import requests
import xml
import xml.etree.ElementTree as ET


def parse_xml(xml_str: str) -> tuple[MetaData, PaperDataList]:
    root: xml.etree.ElementTree.Element = ET.fromstring(xml_str)
    namespaces = {
        "atom": "http://www.w3.org/2005/Atom",
        "meta": "http://a9.com/-/spec/opensearch/1.1/",
        "arxiv": "http://arxiv.org/schemas/atom",
    }
    updated_time = root.find("atom:updated", namespaces).text
    # 解析时间字符串为datetime对象
    dt = datetime.fromisoformat(updated_time)
    # 将时间对象格式化为人类可读格式
    formatted_time = dt.strftime("%Y年%m月%d日 %H:%M:%S")
    total_result = root.find("meta:totalResults", namespaces).text
    items = root.find("meta:itemsPerPage", namespaces).text
    mdata = MetaData(
        updated_time=formatted_time,
        total_result=int(total_result),
        items=int(items),
    )
    pdatalist = PaperDataList(papers=[])
    for entry in root.findall("atom:entry", namespaces):
        paper_id = entry.find("atom:id", namespaces).text
        updated = entry.find("atom:updated", namespaces).text
        published = entry.find("atom:published", namespaces).text
        title = entry.find("atom:title", namespaces).text
        summary = entry.find("atom:summary", namespaces).text
        author_name = (
            entry.find("atom:author", namespaces).find("atom:name", namespaces).text
        )
        affiliation_element = entry.find("atom:author", namespaces).find(
            "arxiv:affiliation", namespaces
        )
        affiliation = (
            affiliation_element.text if affiliation_element is not None else None
        )
        categories = entry.findall("atom:category", namespaces)
        cats = []
        for category in categories:
            category = category.attrib["term"]
            cats.append(category)
        pdf_link = entry.find("atom:link[@title='pdf']", namespaces).attrib["href"]
        doi = entry.find("atom:link[@title='doi']", namespaces)
        doi = doi.attrib["href"] if doi is not None else None
        pdata = PaperData(
            paper_id=paper_id,
            updated=updated,
            published=published,
            title=title,
            summary=summary,
            author=AuthorData(name=author_name, affiliation=affiliation),
            doi=doi,
            category=cats,
            pdf_link=pdf_link,
        )

        pdatalist.papers.append(pdata)
    return mdata, pdatalist


class ArxivParser:
    Ascending = "ascending"
    Descending = "descending"

    Relevance = "relevance"
    LastUpdatedDate = "lastUpdatedDate"
    SubmittedDate = "submittedDate"

    def __init__(self, url: Optional[str] = None):
        if url is None:
            self.root_url = "http://export.arxiv.org/api/{method_name}"
        else:
            self.root_url = url

    def search(
        self,
        all_: str,
        id_list: Optional[list[str]] = None,
        start: int = 0,
        max_results: int = 10,
        # author: Optional[str] = None,
        # abstract: Optional[str] = None,
        # comment: Optional[str] = None,
        # jr: Optional[str] = None,
        # cat: Optional[str] = None,
        # rn: Optional[str] = None,
        # title: Optional[str] = None,
    ):
        search_query = "all:{all_}".format(all_=all_)
        params = {
            "search_query": search_query,
            "id_list": id_list,
            "start": start,
            "max_results": max_results,
            "sortOrder": ArxivParser.Descending,
            "sortBy": ArxivParser.Relevance,
        }
        res = requests.get(self.root_url.format(method_name="query"), params=params)
        mdata, pdatalist = parse_xml(res.text)
        return mdata, pdatalist
