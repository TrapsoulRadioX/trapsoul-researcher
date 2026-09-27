import httpx
from datetime import datetime, timezone
from app.models import ResearchRequest, TrendItem
from app.providers.base import Provider

class YouTubeProvider(Provider):
    name="youtube"
    endpoint="https://www.googleapis.com/youtube/v3/search"
    def __init__(self,api_key,timeout=15): self.api_key,self.timeout=api_key,timeout
    async def search(self,request):
        if not self.api_key: return []
        q=" ".join(x for x in [request.genre,request.seed] if x).strip() or request.genre
        params={"part":"snippet","q":q,"type":"video","maxResults":min(request.limit,50),"regionCode":request.market,"key":self.api_key}
        async with httpx.AsyncClient(timeout=self.timeout) as c:
            r=await c.get(self.endpoint,params=params); r.raise_for_status(); data=r.json()
        now=datetime.now(timezone.utc)
        return [TrendItem(title=i["snippet"]["title"],score=max(1,100-n*3),source="YouTube Data API",url=f"https://www.youtube.com/watch?v={i['id']['videoId']}",observed_at=now,evidence={"channel":i["snippet"].get("channelTitle"),"published_at":i["snippet"].get("publishedAt")},confidence="high",tags=[request.genre]) for n,i in enumerate(data.get("items",[])) if i.get("id",{}).get("videoId")]
