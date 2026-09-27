from app.models import TrendItem
from app.services.analytics import analyze
def test_analyze():
 x=[TrendItem(title="Midnight Love",score=90,source="test"),TrendItem(title="Late Night Love",score=80,source="test")]
 keys,themes=analyze(x);assert keys and themes
