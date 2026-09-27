# Provider matrix

| Provider | Purpose | Required key | Reliability |
|---|---|---:|---|
| YouTube Data API v3 | Video discovery/metadata | Yes | High |
| Spotify Web API | Catalog lookup | Yes | High |
| Google Ads API | Keyword ideas/historical metrics | Yes | High |
| Google Trends/pytrends | Search-interest signals | No | Best effort |
| Local creative engine | Titles/concepts/SEO | No | High |

Every live result should retain source and observation timestamp. Generated ideas are not evidence of a trend.
