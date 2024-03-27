import requests
from typing import Optional


class ArxivParser:
    Ascending = "ascending"
    Descending = "descending"

    Relevance = "relevance"
    LastUpdatedDate =  "lastUpdatedDate"
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
        author: Optional[str] = None,
        abstract: Optional[str] = None,
        comment: Optional[str] = None,
        jr: Optional[str] = None,
        cat: Optional[str] = None,
        rn: Optional[str] = None,
        title: Optional[str] = None,
    ):
        search_query = "all:{all_}".format(all_=all_)
        params = {
            search_query: search_query,
            id_list: id_list,
            start: start,
            max_results: max_results,
            sortBy: Descending,
            sortOrder:
        }
        res = requests.get(self.root_url.format(method_name="query"), params=params)
        print(res.url)
        print(res.content)


if __name__ == "__main__":
    parser = ArxivParser()
    parser.search("computer")
