import base64, httpx
from datetime import datetime, timezone
from app.models import ResearchRequest, TrendItem
from app.providers.base import Provider

class SpotifyProvider(Provider):
    name="spotify"
    def __init__(self,client_id,client_secret,timeout=15): self.client_id,self.client_secret,self.timeout=client_id,client_secret,timeout
    async def search(self,request):
        if not self.client_id or not self.client_secret: return []
        basic=base64.b64encode(f"{self.client_id}:{self.client_secret}".encode()).decode()
        async with httpx.AsyncClient(timeout=self.timeout) as c:
            a=await c.post("https://accounts.spotify.com/api/token",headers={"Authorization":f"Basic {basic}"},data={"grant_type":"client_credentials"}); a.raise_for_status()
            token=a.json()["access_token"]; q=" ".join(x for x in [request.genre,request.seed] if x).strip() or request.genre
            r=await c.get("https://api.spotify.com/v1/search",headers={"Authorization":f"Bearer {token}"},params={"q":q,"type":"track","limit":min(request.limit,10)}); r.raise_for_status(); data=r.json()
        now=datetime.now(timezone.utc); items=data.get("tracks",{}).get("items",[])
        return [TrendItem(title=f"{x['name']} — {', '.join(a['name'] for a in x['artists'])}",score=max(1,100-n*5),source="Spotify Web API",url=x.get("external_urls",{}).get("spotify"),observed_at=now,evidence={"album":x.get("album",{}).get("name")},confidence="medium",tags=[request.genre]) for n,x in enumerate(items)]
