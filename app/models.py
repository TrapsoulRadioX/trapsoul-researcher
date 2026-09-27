from datetime import datetime, timezone
from typing import Literal
from pydantic import BaseModel, Field

Genre = Literal["Hip Hop","R&B","Trap Soul","Soul","Pop","Afrobeats","Unknown"]

class ResearchRequest(BaseModel):
    genre: Genre = "R&B"
    market: str = "US"
    seed: str = ""
    days: int = Field(default=30, ge=1, le=365)
    limit: int = Field(default=20, ge=1, le=50)

class TrendItem(BaseModel):
    title: str
    score: float = Field(ge=0, le=100)
    source: str
    url: str | None = None
    observed_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    evidence: dict = Field(default_factory=dict)
    confidence: Literal["high","medium","low"] = "medium"
    tags: list[str] = Field(default_factory=list)

class ResearchResult(BaseModel):
    query: ResearchRequest
    generated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    trends: list[TrendItem]
    keywords: list[dict]
    themes: list[dict]
    notes: list[str] = Field(default_factory=list)

class TitleRequest(BaseModel):
    genre: Genre = "R&B"; mood: str = "late night"; themes: list[str] = ["love"]; market: str = "US"; count: int = Field(default=20,ge=1,le=100)

class LyricsConceptRequest(BaseModel):
    title: str; genre: Genre = "R&B"; mood: str = "dark romantic"; themes: list[str] = ["heartbreak"]

class SEORequest(BaseModel):
    title: str; artist: str = ""; genre: Genre = "R&B"; market: str = "US"; themes: list[str] = []
    platform: Literal["YouTube","Spotify","TikTok","Instagram"] = "YouTube"
