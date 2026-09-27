import random
PATTERNS={"R&B":["After {noun}","{adj} Without You","2AM {noun}","No Reply","Still On My Mind","Love After Dark","Too Close To Leave","Velvet {noun}"],"Hip Hop":["{noun} Season","No {noun}, No Peace","Pressure Made Me","{noun} Talk","Late Night Run","From Nothing","Cold City","Still Outside"],"Trap Soul":["Midnight {noun}","Love Ain't {noun}","Ghost In My Phone","After Hours","Slow Burn","No Sleep In {place}","Heart On Ice","Dark Room"]}
WORDS={"noun":["Love","Money","Feelings","Pressure","Dreams","Memories","Silence","Secrets","Vibes"],"adj":["Cold","Lost","Closer","Broken","Toxic","Honest"],"place":["LA","NYC","Miami","The City"]}
def titles(genre,mood,themes,count):
    pats=PATTERNS.get(genre,PATTERNS["R&B"]); rng=random.Random(f"{genre}|{mood}|{themes}|{count}"); out=[]
    for _ in range(count*5):
        p=rng.choice(pats)
        for k,v in WORDS.items(): p=p.replace("{"+k+"}",rng.choice(v))
        if p not in out: out.append(p)
        if len(out)>=count: break
    return out
def lyric_concept(title,genre,mood,themes):
    return {"title":title,"genre":genre,"mood":mood,"themes":themes,"structure":["Intro","Verse 1","Pre-Chorus","Chorus","Verse 2","Bridge","Final Chorus","Outro"],"concept":f"An original {genre} narrative about {', '.join(themes)}. The protagonist processes desire, memory and self-respect around '{title}'.","hook_direction":"Use a short memorable central phrase and repeat the emotional image rather than copying an existing lyric.","verse_prompts":["Set the scene with concrete sensory details.","Introduce the conflict and what the narrator wants.","Raise the stakes with a specific choice.","Resolve or deliberately leave the emotional tension open."],"copyright_note":"Concept and prompts only; do not reproduce or imitate copyrighted lyrics."}
def seo(title,artist,genre,market,themes,platform):
    base=" ".join([title,genre,"music"]+themes); tags=["#RnB" if genre=="R&B" else "#HipHop","#NewMusic","#TrapSoul","#UrbanMusic"]+["#"+''.join(w.title() for w in x.split()) for x in themes[:4]]
    if platform=="YouTube": head=f"{title} | {genre} {market} | Official Audio"; desc=f"{title} — a {genre} release built around {', '.join(themes) or 'late-night atmosphere'}. Keywords: {base}."
    elif platform=="TikTok": head=f"{title} — {genre} sound"; desc=f"Original {genre} sound: {title}. {', '.join(themes)}"
    else: head=f"{title} — {genre}"; desc=f"{title}. {genre} for listeners into {', '.join(themes) or 'modern urban music'}."
    return {"title":head[:100],"description":desc,"hashtags":list(dict.fromkeys(tags)),"keyword_string":base,"note":"Generated SEO ideas are not guarantees of ranking or trend status."}
