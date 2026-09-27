from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import FileResponse
from app.config import settings
from app.models import ResearchRequest,TitleRequest,LyricsConceptRequest,SEORequest
from app.providers.youtube import YouTubeProvider
from app.providers.spotify import SpotifyProvider
from app.providers.google_trends import GoogleTrendsProvider
from app.providers.google_ads import GoogleAdsProvider
from app.services.research import ResearchOrchestrator
from app.services.creative import titles,lyric_concept,seo
s=settings()
app=FastAPI(title=s["app_name"],version="1.0.0",description="Hip Hop & R&B research and creative intelligence API")
providers=[YouTubeProvider(s["youtube_api_key"],s["request_timeout"]),SpotifyProvider(s["spotify_client_id"],s["spotify_client_secret"],s["request_timeout"]),GoogleTrendsProvider(),GoogleAdsProvider()]
researcher=ResearchOrchestrator(providers)
@app.get("/api/health")
async def health(): return {"status":"ok","app":s["app_name"],"version":"1.0.0"}
@app.post("/api/research")
async def research(req:ResearchRequest): return await researcher.run(req)
@app.post("/api/titles")
async def make_titles(req:TitleRequest): return {"titles":titles(req.genre,req.mood,req.themes,req.count)}
@app.post("/api/lyrics/concept")
async def make_concept(req:LyricsConceptRequest): return lyric_concept(req.title,req.genre,req.mood,req.themes)
@app.post("/api/seo")
async def make_seo(req:SEORequest): return seo(req.title,req.artist,req.genre,req.market,req.themes,req.platform)
@app.get("/api/trends")
async def trends(genre:str="R&B",market:str="US",seed:str="",days:int=30,limit:int=20): return await researcher.run(ResearchRequest(genre=genre,market=market,seed=seed,days=days,limit=limit))
@app.get("/")
async def dashboard(): return FileResponse(Path(__file__).parent/"static"/"index.html")
