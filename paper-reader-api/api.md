# 搜索论文
> http://export.arxiv.org/api/{method_name}?{parameters}

|       |                |                        |              |              |
| ----- | -------------- | ---------------------- | ------------ | ------------ |
| query |                |                        |              |              |
|       | **parameters** | **type**               | **defaults** | **required** |
|       | `search_query` | string                 | None         | No           |
|       | `id_list`      | comma-delimited string | None         | No           |
|       | `start`        | int                    | 0            | No           |
|       | `max_results`  | int                    | 10           | No           |

`search_query`是一个字符串,里面包含查询论文的信息,包括标题,作者等并使用逻辑符号表示关系

```
prefix  explanation
ti  Title
au  Author
abs Abstract
co  Comment
jr  Journal Reference
cat Subject Category
rn  Report Number
id  Id (use id_list instead)
all All of the above
```

```
AND``OR``ANDNOT
```

同时使用`+`表示url中的宫格.此外的id_list,start,max_results用于额外挑选.



### 返回响应

返回的是xml.

其中论文喜喜包括title,id,published,updated

The `<title>` element contains the title of the article returned

The `<id>` element contains a url that resolves to the abstract page for that article

The `<published>` tag contains the date in which the `first` version of this article was submitted and processed. The `<updated>` element contains the date on which the retrieved article was submitted and processed.



此外还有summary,author和category.

The `<summary>` element contains the abstract for the article



The `<category>` element is used to describe either an arXiv, ACM, or MSC classification

The `<category>` element has two attributes, `scheme`, which is the categorization scheme, and `term` which is the term used in the categorization.



links

For each entry, there are up to three `<link>` elements, distinguished by their `rel` and `title` attributes
