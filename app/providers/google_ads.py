from app.providers.base import Provider
class GoogleAdsProvider(Provider):
    name="google-ads"
    async def search(self,request):
        # Adapter boundary for KeywordPlanIdeaService.
        # Kept optional so the core app works without an Ads account.
        return []
