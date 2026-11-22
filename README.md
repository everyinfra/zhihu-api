# Zhihu API（知乎 API）

[English](#english) · [中文](#中文)

## English

This repo reads public Zhihu data with Python or curl. You can search content by keyword, read an answer or article with its comments, and look up an author's profile and articles. You need one EveryInfra API key. You do not need a Zhihu account or cookie. The same API also works as an MCP tool in Claude and Cursor. Billing is per call: these 5 capabilities cost $0.56 to $0.79 per 1,000 calls. Failed calls and empty results are not charged. The EveryInfra Zhihu API has 17 capabilities; 16 are available now. All are listed on the platform page: <https://everyinfra.com/en/zhihu-api?utm_source=github&utm_medium=example_repo&utm_campaign=zhihu-api>

### Quick start

```bash
git clone https://github.com/everyinfra/zhihu-api.git
cd zhihu-api
pip install -r requirements.txt
export EVERYINFRA_API_KEY=<your API key>
python main.py search 咖啡机 --out results.csv
python main.py detail "<answer or article url>" --out detail.json
python main.py comments "<answer or article url>" --out comments.csv
python main.py user "<profile url>"
python main.py articles "<profile url>" --out articles.csv
```

- For `detail` and `comments`, pass an answer or article link: use the `url` of a `search` row whose `type` is answer or article. Question page links do not work.
- For `user` and `articles`, pass the author's profile link from the `author_url` field of a `search` result.
- In this test run, `user` returned only the answer count and the article count.
- Without `--out`, the command prints the first 3 rows as JSON. With `--out`, it saves a .csv or .json file. The CSV has a BOM, so Excel opens it without garbled text.
- Register at everyinfra.com, then create the API key in the console. Steps: <https://everyinfra.com/en/docs?utm_source=github&utm_medium=example_repo&utm_campaign=zhihu-api#quickstart>

### curl

```bash
curl -X POST https://api.everyinfra.com/api/v1/social \
  -H "Authorization: Bearer $EVERYINFRA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"platform":"zhihu","action":"search","params":{"keyword":"咖啡机"}}'
```

All capabilities use the same URL. Change `action` and `params` to call another one. Examples for `content_detail`, `content_comments`, `profile`, and `user_articles` are in [examples/curl.sh](examples/curl.sh).

### Claude and Cursor (MCP)

The remote MCP URL is <https://api.everyinfra.com/mcp>. Add the `Authorization: Bearer` header with your API key. EveryInfra runs the server, so you install no local program.

Claude Code:

```bash
claude mcp add --transport http everyinfra https://api.everyinfra.com/mcp --header "Authorization: Bearer <API Key>"
```

Cursor and other clients that read `mcp.json` ([examples/mcp.json](examples/mcp.json)):

```json
{
  "mcpServers": {
    "everyinfra": {
      "url": "https://api.everyinfra.com/mcp",
      "headers": {
        "Authorization": "Bearer <API Key>"
      }
    }
  }
}
```

Custom connectors in Claude on the web and desktop, and ChatGPT, accept only a URL. Enter <https://api.everyinfra.com/mcp/all>, sign in to EveryInfra when asked, and allow access. You do not need to enter a key. Full steps: <https://everyinfra.com/en/mcp-server?utm_source=github&utm_medium=example_repo&utm_campaign=zhihu-api>

### Price

| `action` | Per 1,000 calls |
|---|---|
| `search` | $0.79 |
| `content_detail` | $0.56 |
| `content_comments` | $0.56 |
| `profile` | $0.56 |
| `user_articles` | $0.56 |

- Billing is per call, about $0.00056 to $0.00079 each. Failed calls, empty results, parameter errors, and authentication failures are not charged.
- A new account gets a $1 trial allowance, valid for 24 hours. No credit card is needed. How to claim it: <https://everyinfra.com/en/pricing?utm_source=github&utm_medium=example_repo&utm_campaign=zhihu-api>
- Prices for the other 11 available Zhihu capabilities are on the platform page: <https://everyinfra.com/en/zhihu-api?utm_source=github&utm_medium=example_repo&utm_campaign=zhihu-api>

### Fields

The fields of each capability are documented on the English pages linked below.

- `search`: <https://everyinfra.com/en/zhihu-api/search?utm_source=github&utm_medium=example_repo&utm_campaign=zhihu-api>
- `content_detail`: <https://everyinfra.com/en/zhihu-api/content_detail?utm_source=github&utm_medium=example_repo&utm_campaign=zhihu-api>
- `content_comments`: <https://everyinfra.com/en/zhihu-api/content_comments?utm_source=github&utm_medium=example_repo&utm_campaign=zhihu-api>
- `profile`: <https://everyinfra.com/en/zhihu-api/profile?utm_source=github&utm_medium=example_repo&utm_campaign=zhihu-api>
- `user_articles`: <https://everyinfra.com/en/zhihu-api/user_articles?utm_source=github&utm_medium=example_repo&utm_campaign=zhihu-api>

### FAQ

**Do I need a Zhihu account or cookie to call the API?**

No. Send the `Authorization: Bearer` header with your API key. The request body holds `platform`, `action`, and the capability parameters. You do not scan a QR code, keep a login session, or open a browser.

**How much does it cost? Are failed calls charged? Is there a free allowance?**

Billing is per call, from $0.56 per 1,000 calls. Failed calls, empty results, parameter errors, and authentication failures are not charged. A new account gets a $1 trial allowance, valid for 24 hours. No credit card is needed. How to claim it: <https://everyinfra.com/en/pricing?utm_source=github&utm_medium=example_repo&utm_campaign=zhihu-api>

**Can I connect the Zhihu API to Claude or Cursor?**

Yes. The remote MCP URL is <https://api.everyinfra.com/mcp>. Add the `Authorization: Bearer` header with your API key. You install no local program. Setup for Claude, Cursor, ChatGPT, and Claude Code: <https://everyinfra.com/en/mcp-server?utm_source=github&utm_medium=example_repo&utm_campaign=zhihu-api>.

**What legal points apply when I use Zhihu data?**

The EveryInfra Terms of Service require you to make sure your use of the data follows applicable law and the terms of the relevant platform. Do not use the data for anything illegal or anything that violates privacy or intellectual property rights. Do not use bulk scraping for harassment, fraud, or other abuse. When you use personal information such as nicknames and avatars, keep only the fields your business needs.

**Which Zhihu data can I get?**

The EveryInfra Zhihu API has 17 capabilities; 16 are available now:

- keyword search
- content detail
- content comments
- comment replies
- profile or object details
- user articles
- trending list
- answers to a question
- user answers
- user pins
- account search
- column search
- scholar search
- salt search
- topic search
- ebook search

Parameters and return fields for each capability are on the platform page: <https://everyinfra.com/en/zhihu-api?utm_source=github&utm_medium=example_repo&utm_campaign=zhihu-api>

### Tested

Before release, we ran the 5 commands in Quick start against the live API with this repo's code.

| Command | Time (Singapore, UTC+8) | Rows | Charged |
|---|---|---|---|
| `python main.py search 咖啡机 --out results.csv` | 2026-11-21 09:32 | 20 | $0.000792 |
| `python main.py detail "<answer or article url>" --out detail.json` | 2026-11-21 09:32 | 1 | $0.000556 |
| `python main.py comments "<answer or article url>" --out comments.csv` | 2026-11-21 09:32 | 20 | $0.000556 |
| `python main.py user "<profile url>"` | 2026-11-21 09:32 | 1 | $0.000556 |
| `python main.py articles "<profile url>" --out articles.csv` | 2026-11-21 09:33 | 20 | $0.000556 |

## 中文

本仓库用 Python 或 curl 读知乎公开数据：按关键词搜内容，读回答或文章的详情和评论，查作者主页和他写的文章。只需一把 EveryInfra API Key，不用知乎账号和 Cookie，也能作为 MCP 工具接进 Claude、Cursor。按调用次数计费，这 5 个能力每千次 $0.56 到 $0.79，失败和空结果不收费。知乎共 17 个能力，其中 16 个现在可用：<https://everyinfra.com/zhihu-api?utm_source=github&utm_medium=example_repo&utm_campaign=zhihu-api>

### 快速开始

```bash
git clone https://github.com/everyinfra/zhihu-api.git
cd zhihu-api
pip install -r requirements.txt
export EVERYINFRA_API_KEY=<你的 API Key>
python main.py search 咖啡机 --out results.csv
python main.py detail "<回答或文章链接>" --out detail.json
python main.py comments "<回答或文章链接>" --out comments.csv
python main.py user "<作者主页链接>"
python main.py articles "<作者主页链接>" --out articles.csv
```

- `detail` 和 `comments` 传回答或文章链接：用 `search` 结果里 `type` 为 answer 或 article 的那一行的 `url`，问题页链接不能用。
- `user` 和 `articles` 传作者主页链接，用 `search` 结果里的 `author_url`。
- 这次实测 `user` 只返回了回答数和文章数。
- 不加 `--out` 时打印前 3 条 JSON；加 `--out` 存成 .csv 或 .json。CSV 带 BOM，Excel 直接打开不乱码。
- API Key 在 everyinfra.com 注册后到控制台创建，步骤见 <https://everyinfra.com/docs?utm_source=github&utm_medium=example_repo&utm_campaign=zhihu-api#quickstart>

### 用 curl 调

```bash
curl -X POST https://api.everyinfra.com/api/v1/social \
  -H "Authorization: Bearer $EVERYINFRA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"platform":"zhihu","action":"search","params":{"keyword":"咖啡机"}}'
```

所有能力都发到同一个地址，换 `action` 和 `params` 就行；`content_detail`、`content_comments`、`profile`、`user_articles` 的写法见 [examples/curl.sh](examples/curl.sh)。

### 接进 Claude、Cursor（MCP）

远程 MCP 地址是 <https://api.everyinfra.com/mcp>，请求头加 `Authorization: Bearer` 和 API Key；服务器由 EveryInfra 运行，不用装本地程序。

Claude Code：

```bash
claude mcp add --transport http everyinfra https://api.everyinfra.com/mcp --header "Authorization: Bearer <API Key>"
```

Cursor 等读 `mcp.json` 的客户端（[examples/mcp.json](examples/mcp.json)）：

```json
{
  "mcpServers": {
    "everyinfra": {
      "url": "https://api.everyinfra.com/mcp",
      "headers": {
        "Authorization": "Bearer <API Key>"
      }
    }
  }
}
```

Claude 网页版和桌面版的自定义连接器、ChatGPT 只能填网址：填 <https://api.everyinfra.com/mcp/all>，连接时登录 EveryInfra 并允许，不用填 Key。完整步骤见 <https://everyinfra.com/mcp-server?utm_source=github&utm_medium=example_repo&utm_campaign=zhihu-api>

### 价格

| 能力 | `action` | 每千次 |
|---|---|---|
| 关键词搜索 | `search` | $0.79 |
| 内容详情 | `content_detail` | $0.56 |
| 内容评论 | `content_comments` | $0.56 |
| 主页或对象详情 | `profile` | $0.56 |
| 用户文章 | `user_articles` | $0.56 |

- 按调用次数计费，每次约 $0.00056 到 $0.00079；失败、空结果、参数错误和鉴权失败都不收费。
- 新账号有 $1 试用额度，24 小时内有效，不用信用卡，领取方式见 <https://everyinfra.com/pricing?utm_source=github&utm_medium=example_repo&utm_campaign=zhihu-api>
- 知乎其他 11 个可用能力的单价见平台页 <https://everyinfra.com/zhihu-api?utm_source=github&utm_medium=example_repo&utm_campaign=zhihu-api>

### 返回字段

下面是这 5 个能力实测返回的字段，含义取自接口文档每条说明的第一句，完整说明在每张表下面的链接里。

#### `search`（关键词搜索）

| 字段 | 含义 |
|---|---|
| `id` | 该记录在原平台上的唯一标识。 |
| `type` | 内容类型（answer 回答 / article 文章 / video 视频；hot_list 上是 question 问题；user_pins 是 pin 想法；column_search 是 column 专栏；salt_search 是盐选商品类型，如 paid_column_chapter 付费专栏的一篇；scholar_search 是 paper 论文；ebook_search 是 publication 整本书 / publication_chapter 书里的一章）。 |
| `url` | 该记录在原平台上的可访问链接。 |
| `title` | 标题。 |
| `text` | 正文内容，已去除 HTML 标签，全文返回、不截断（个别平台的列表结果本身只有摘要，以该平台的字段说明为准）。 |
| `like_count` | 点赞数。 |
| `comment_count` | 评论数。 |
| `posted_at` | 发布时间，ISO 8601 格式、UTC 时区（如 2026-08-07T12:34:56+00:00）。 |
| `platform` | 数据来源平台标识，与请求里的 platform 一致（如 xiaohongshu、tiktok）。 |
| `author_id` | 作者在原平台的唯一 ID。 |
| `author_name` | 作者昵称（显示名）。 |
| `author_url` | 作者主页链接。 |
| `author_avatar_url` | 作者头像链接；评论类结果里是评论者的头像。 |
| `author_follower_count` | 作者粉丝数。 |
| `author_bio` | 作者简介。 |
| `collect_count` | 收藏数。 |
| `author_verification_label` | 认证说明。 |

完整参数和字段：<https://everyinfra.com/zhihu-api/search?utm_source=github&utm_medium=example_repo&utm_campaign=zhihu-api>

#### `content_detail`（内容详情）

| 字段 | 含义 |
|---|---|
| `id` | 该记录在原平台上的唯一标识。 |
| `type` | 内容类型（answer 回答 / article 文章 / video 视频；hot_list 上是 question 问题；user_pins 是 pin 想法；column_search 是 column 专栏；salt_search 是盐选商品类型，如 paid_column_chapter 付费专栏的一篇；scholar_search 是 paper 论文；ebook_search 是 publication 整本书 / publication_chapter 书里的一章）。 |
| `url` | 该记录在原平台上的可访问链接。 |
| `title` | 标题。 |
| `text` | 正文内容，已去除 HTML 标签，全文返回、不截断（个别平台的列表结果本身只有摘要，以该平台的字段说明为准）。 |
| `like_count` | 点赞数。 |
| `comment_count` | 评论数。 |
| `collect_count` | 收藏数。 |
| `posted_at` | 发布时间，ISO 8601 格式、UTC 时区（如 2026-08-07T12:34:56+00:00）。 |
| `platform` | 数据来源平台标识，与请求里的 platform 一致（如 xiaohongshu、tiktok）。 |
| `author_id` | 作者在原平台的唯一 ID。 |
| `author_name` | 作者昵称（显示名）。 |
| `author_url` | 作者主页链接。 |
| `author_avatar_url` | 作者头像链接；评论类结果里是评论者的头像。 |
| `author_bio` | 作者简介。 |
| `author_verified` | 作者是否认证。 |
| `author_verification_label` | 认证说明。 |

完整参数和字段：<https://everyinfra.com/zhihu-api/content_detail?utm_source=github&utm_medium=example_repo&utm_campaign=zhihu-api>

#### `content_comments`（内容评论）

| 字段 | 含义 |
|---|---|
| `id` | 该记录在原平台上的唯一标识。 |
| `text` | 正文内容，已去除 HTML 标签，全文返回、不截断（个别平台的列表结果本身只有摘要，以该平台的字段说明为准）。 |
| `like_count` | 点赞数。 |
| `posted_at` | 发布时间，ISO 8601 格式、UTC 时区（如 2026-08-07T12:34:56+00:00）。 |
| `reply_count` | 回复数，通常用于评论的子回复。 |
| `author_id` | 作者在原平台的唯一 ID。 |
| `author_name` | 作者昵称（显示名）。 |
| `author_avatar_url` | 作者头像链接；评论类结果里是评论者的头像。 |
| `platform` | 数据来源平台标识，与请求里的 platform 一致（如 xiaohongshu、tiktok）。 |

完整参数和字段：<https://everyinfra.com/zhihu-api/content_comments?utm_source=github&utm_medium=example_repo&utm_campaign=zhihu-api>

#### `profile`（主页或对象详情）

| 字段 | 含义 |
|---|---|
| `answer_count` | 回答数：profile、user_search 是这个账号写过的回答总数；hot_list 是这个问题下的回答数。 |
| `article_count` | 文章数：profile、user_search 是这个账号的文章总数；column_search 是这个专栏收录的文章数。 |
| `platform` | 数据来源平台标识，与请求里的 platform 一致（如 xiaohongshu、tiktok）。 |

完整参数和字段：<https://everyinfra.com/zhihu-api/profile?utm_source=github&utm_medium=example_repo&utm_campaign=zhihu-api>

#### `user_articles`（用户文章）

| 字段 | 含义 |
|---|---|
| `id` | 该记录在原平台上的唯一标识。 |
| `url` | 该记录在原平台上的可访问链接。 |
| `title` | 标题。 |
| `text` | 正文内容，已去除 HTML 标签，全文返回、不截断（个别平台的列表结果本身只有摘要，以该平台的字段说明为准）。 |
| `like_count` | 点赞数。 |
| `comment_count` | 评论数。 |
| `collect_count` | 收藏数。 |
| `posted_at` | 发布时间，ISO 8601 格式、UTC 时区（如 2026-08-07T12:34:56+00:00）。 |
| `cover_image_url` | 封面图。 |
| `platform` | 数据来源平台标识，与请求里的 platform 一致（如 xiaohongshu、tiktok）。 |
| `author_id` | 作者在原平台的唯一 ID。 |
| `author_name` | 作者昵称（显示名）。 |
| `author_url` | 作者主页链接。 |
| `author_avatar_url` | 作者头像链接；评论类结果里是评论者的头像。 |
| `author_bio` | 作者简介。 |
| `author_verified` | 作者是否认证。 |
| `author_verification_label` | 认证说明。 |

完整参数和字段：<https://everyinfra.com/zhihu-api/user_articles?utm_source=github&utm_medium=example_repo&utm_campaign=zhihu-api>

### 常见问题

**调用时要不要提供知乎账号或 Cookie？**

不用，请求头带 `Authorization: Bearer` 和 API Key 就能调，请求体写 `platform`、`action` 和能力参数。不用扫码、维护登录状态，也不用开浏览器。

**怎么收费？失败了收不收钱？有免费额度吗？**

按调用次数计费，每千次 $0.56 起。失败、空结果、参数错误和鉴权失败都不收费。新账号有 $1 试用额度，24 小时内有效，不用信用卡，领取方式见定价页 <https://everyinfra.com/pricing?utm_source=github&utm_medium=example_repo&utm_campaign=zhihu-api>

**能把知乎接口接进 Claude、Cursor 吗？**

能，远程 MCP 地址是 <https://api.everyinfra.com/mcp>，请求头加 `Authorization: Bearer` 和 API Key，不用装本地程序。Claude、Cursor、ChatGPT、Claude Code 配置见 <https://everyinfra.com/mcp-server?utm_source=github&utm_medium=example_repo&utm_campaign=zhihu-api>。

**用知乎数据要注意哪些合规问题？**

EveryInfra 服务条款要求你自行确保数据用法符合适用法律和相关平台条款，禁止用于违法、侵犯隐私或知识产权，或批量抓取用于骚扰、欺诈等恶意用途。用到昵称、头像等个人信息时，只留业务用得上的字段。

**可以拿到知乎的哪些数据？**

知乎有 17 个能力，其中 16 个现在可用：关键词搜索、内容详情、内容评论、评论回复、主页或对象详情、用户文章、热榜、问题下的回答、用户回答、用户想法、账号搜索、专栏搜索、学术论文搜索、盐选搜索、话题搜索、电子书搜索。每个能力的参数和返回字段见平台页 <https://everyinfra.com/zhihu-api?utm_source=github&utm_medium=example_repo&utm_campaign=zhihu-api>

### 实测记录

发布前用本仓的代码对线上接口跑过一遍，命令就是「快速开始」里的 5 条。

| 命令 | 时间（新加坡时间） | 返回条数 | 扣费 |
|---|---|---|---|
| `python main.py search 咖啡机 --out results.csv` | 2026-11-21 09:32 | 20 | $0.000792 |
| `python main.py detail "<回答或文章链接>" --out detail.json` | 2026-11-21 09:32 | 1 | $0.000556 |
| `python main.py comments "<回答或文章链接>" --out comments.csv` | 2026-11-21 09:32 | 20 | $0.000556 |
| `python main.py user "<作者主页链接>"` | 2026-11-21 09:32 | 1 | $0.000556 |
| `python main.py articles "<作者主页链接>" --out articles.csv` | 2026-11-21 09:33 | 20 | $0.000556 |

`content_detail` 返回的一条（正文截到 60 字，作者字段没放进来）：

```json
{
  "id": "114770929599",
  "type": "answer",
  "title": "为什么不建议买一千左右的咖啡机?",
  "text": "当你弄懂了咖啡制作原理，千元的咖啡机肯定不会买，要买千元以下的、300元左右就行了。\n咖啡机二个重要零件：过滤网、水泵。…",
  "like_count": 148,
  "comment_count": 202,
  "collect_count": 150,
  "posted_at": "2025-03-02T23:48:04+00:00"
}
```

## License

MIT
