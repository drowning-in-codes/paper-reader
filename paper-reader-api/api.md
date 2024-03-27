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
