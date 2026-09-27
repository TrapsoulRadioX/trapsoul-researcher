from datetime import datetime, timezone
from app.models import ResearchRequest, TrendItem
from app.providers.base import Provider

class GoogleTrendsProvider(Provider):
    name="google-trends"
    async def search(self,request):
        try: from pytrends.request import TrendReq
        except ImportError: return []
        term=request.seed.strip() or request.genre
        try:
            py=TrendReq(hl="en-US",tz=0); py.build_payload([term],timeframe=f"today {min(request.days,90)}-d",geo=request.market if len(request.market)==2 else "US")
            data=py.related_queries().get(term,{})
            rows=data.get("rising") if data else None
            if rows is None: return []
            now=datetime.now(timezone.utc)
            return [TrendItem(title=str(row[term]),score=min(100,float(row.get("value",0))),source="Google Trends / pytrends",observed_at=now,evidence={"type":"rising"},confidence="low",tags=[request.genre,"search"]) for _,row in rows.head(request.limit).iterrows()]
        except Exception: return []
