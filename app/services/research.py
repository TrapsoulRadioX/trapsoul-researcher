import asyncio
from app.models import ResearchRequest, ResearchResult
from app.services.analytics import analyze
class ResearchOrchestrator:
    def __init__(self,providers): self.providers=providers
    async def run(self,request):
        results=await asyncio.gather(*(p.search(request) for p in self.providers),return_exceptions=True); items=[]; notes=[]
        for p,r in zip(self.providers,results):
            if isinstance(r,Exception): notes.append(f"{p.name}: provider failed safely ({type(r).__name__})")
            else: items.extend(r)
        best={}
        for x in items:
            k=x.title.strip().lower()
            if k not in best or x.score>best[k].score: best[k]=x
        trends=sorted(best.values(),key=lambda x:x.score,reverse=True)[:request.limit]; keys,themes=analyze(trends)
        if not trends: notes.append("No live provider data is configured. Add provider API keys or use local creative tools.")
        return ResearchResult(query=request,trends=trends,keywords=keys,themes=themes,notes=notes)
