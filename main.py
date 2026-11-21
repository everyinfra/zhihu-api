"""知乎 API 示例（Zhihu API in Python）。

  python main.py search 咖啡机 --out results.csv                # 按关键词搜内容 / search content
  python main.py detail "<回答或文章链接>" --out detail.json    # 回答或文章详情 / content detail
  python main.py comments "<回答或文章链接>" --out comments.csv # 评论 / comments
  python main.py user "<作者主页链接>"                          # 作者主页 / author profile
  python main.py articles "<作者主页链接>" --out articles.csv   # 作者的文章 / an author's articles
"""
import argparse

from everyinfra import fetch, report

SORTS = ["general", "upvote_count_descending", "time_descending"]


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search", help="按关键词搜内容 / search content by keyword")
    s.add_argument("keyword")
    s.add_argument("--sort", choices=SORTS, help="排序 / sort order")
    d = sub.add_parser("detail", help="回答或文章详情 / one answer or article")
    d.add_argument("url")
    c = sub.add_parser("comments", help="回答或文章的评论 / comments")
    c.add_argument("url")
    u = sub.add_parser("user", help="作者主页 / author profile")
    u.add_argument("url")
    ar = sub.add_parser("articles", help="作者的文章 / an author's articles")
    ar.add_argument("url")
    for x in (s, d, c, u, ar):
        x.add_argument("--out", help="存成 .csv 或 .json / write .csv or .json")
    a = p.parse_args()

    if a.cmd == "search":
        params = {"keyword": a.keyword, **({"sort": a.sort} if a.sort else {})}
        rows, charged = fetch("search", params)
    elif a.cmd == "detail":
        rows, charged = fetch("content_detail", {"url": a.url})
    elif a.cmd == "comments":
        rows, charged = fetch("content_comments", {"url": a.url})
    elif a.cmd == "user":
        rows, charged = fetch("profile", {"url": a.url})
    else:
        rows, charged = fetch("user_articles", {"url": a.url})
    report(rows, charged, a.out)


if __name__ == "__main__":
    main()
