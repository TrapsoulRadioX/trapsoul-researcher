import re
from collections import Counter
STOP=set("the a an and or of to in on for with my your you me i is are was be this that from new music song official video ft feat remix edit".split())
def tokens(text): return [x.lower() for x in re.findall(r"[a-zA-Z][a-zA-Z'-]{2,}",text) if x.lower() not in STOP]
def analyze(items):
    counts=Counter(t for item in items for t in tokens(item.title))
    keys=[{"keyword":k,"frequency":v,"opportunity_score":round(min(100,20+v*12),1)} for k,v in counts.most_common(25)]
    groups={"romance":["love","heart","baby","kiss","relationship","miss"],"nightlife":["night","midnight","after","late","club"],"money":["money","cash","rich","bag","million"],"confidence":["boss","queen","king","flex","power"],"pain":["sad","hurt","alone","tears","broken","pain"],"street":["street","hood","city","block","trap"]}
    themes=[]
    for name,words in groups.items():
        hits=sum(counts[w] for w in words)
        if hits: themes.append({"theme":name,"signals":hits,"score":min(100,20+hits*15)})
    return keys,sorted(themes,key=lambda x:x["score"],reverse=True)
