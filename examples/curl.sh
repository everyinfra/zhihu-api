#!/usr/bin/env bash
# 知乎 API 的 curl 示例：所有能力都发到同一个地址，只换 action 和 params。
# curl examples for the Zhihu API: every capability uses the same URL; only action and params change.
#
#   export EVERYINFRA_API_KEY=<your API key>
#   bash examples/curl.sh search 咖啡机
#   bash examples/curl.sh content_detail "<answer or article url>"   # search 结果里的 url / the url from a search result
#   bash examples/curl.sh content_comments "<answer or article url>"
#   bash examples/curl.sh profile "<profile url>"                    # search 结果里的 author_url / the author_url from a search result
#   bash examples/curl.sh user_articles "<profile url>"
set -euo pipefail
: "${EVERYINFRA_API_KEY:?Set EVERYINFRA_API_KEY first: https://everyinfra.com/docs#quickstart}"
action=${1:?"usage: bash examples/curl.sh <search|content_detail|content_comments|profile|user_articles> <value>"}
value=${2:?"value: a keyword, a content url or a profile url"}

case "$action" in
  search)                                                      params="{\"keyword\":\"$value\"}" ;;
  content_detail | content_comments | profile | user_articles) params="{\"url\":\"$value\"}" ;;
  *) echo "unknown action: $action (use search, content_detail, content_comments, profile or user_articles)" >&2; exit 2 ;;
esac

curl -sS -X POST https://api.everyinfra.com/api/v1/social \
  -H "Authorization: Bearer $EVERYINFRA_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"platform\":\"zhihu\",\"action\":\"$action\",\"params\":$params}"
echo
