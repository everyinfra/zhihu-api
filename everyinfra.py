"""EveryInfra 最小客户端：一次调用就是一个 POST /api/v1/social；出错时打印错误码和处理建议后退出。

Minimal EveryInfra client: one POST per call; on errors it prints the code and next steps, then exits.
文档 / Docs: https://everyinfra.com/docs
"""
import csv
import json
import os
import sys

import requests

API = "https://api.everyinfra.com"


def _key():
    key = os.environ.get("EVERYINFRA_API_KEY")
    if not key:
        sys.exit("先设置环境变量 EVERYINFRA_API_KEY（Set EVERYINFRA_API_KEY first）: https://everyinfra.com/docs#quickstart")
    return key


def call(action, params, platform="zhihu", timeout=180):
    """调一次能力，返回响应 JSON。Call one capability and return the response body."""
    r = requests.post(
        f"{API}/api/v1/social",
        json={"platform": platform, "action": action, "params": params},
        headers={"Authorization": f"Bearer {_key()}"},
        timeout=timeout,
    )
    data = r.json()
    if r.status_code >= 400:
        err = data.get("error", {})
        steps = " ".join(err.get("next_steps") or [])
        sys.exit(f"HTTP {r.status_code} {err.get('code')}: {err.get('message')} {steps}".strip())
    return data


def rows_of(data):
    """列表能力的 results 是数组；content_detail、profile 这类详情能力是一个对象，这里统一成数组。"""
    res = data.get("results")
    if isinstance(res, dict):
        return [res]
    return res or []


def fetch(action, params, max_pages=1):
    """按 next_page_token 翻页，最多 max_pages 页；每页算一次调用。Follow next_page_token for up to max_pages pages."""
    rows, charged, page_params = [], 0.0, dict(params)
    for _ in range(max_pages):
        data = call(action, page_params)
        rows += rows_of(data)
        charged += data.get("billing", {}).get("charged_usd") or 0
        token = data.get("next_page_token")
        if not token:
            break
        page_params = {**params, "page_token": token}
    return rows, charged


def _cell(value):
    """CSV 单元格：简单列表用分号连起来，嵌套的（比如评论里的楼中楼）存成 JSON 字符串。"""
    if isinstance(value, list) and not any(isinstance(v, (dict, list)) for v in value):
        return ";".join(map(str, value))
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False)
    return value


def save(rows, path):
    """存成 .json 或 .csv（CSV 用 UTF-8 BOM，Excel 直接打开不乱码）。Write rows to .json or .csv."""
    if path.endswith(".json"):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(rows, f, ensure_ascii=False, indent=2)
        return
    keys = []
    for row in rows:
        keys += [k for k in row if k not in keys]
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=keys, extrasaction="ignore")
        w.writeheader()
        for row in rows:
            w.writerow({k: _cell(v) for k, v in row.items()})


def report(rows, charged, out):
    print(f"{len(rows)} rows, charged ${charged:.6f}", file=sys.stderr)
    if out:
        save(rows, out)
        print(f"saved to {out}", file=sys.stderr)
    else:
        print(json.dumps(rows[:3], ensure_ascii=False, indent=2))
