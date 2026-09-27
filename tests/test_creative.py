from app.services.creative import titles,lyric_concept,seo
def test_titles_unique():
 x=titles("R&B","late night",["love"],30);assert len(x)==30 and len(set(x))==30
def test_concept():
 x=lyric_concept("After Hours","R&B","dark",["love"]);assert "structure" in x and "copyrighted lyrics" in x["copyright_note"]
def test_seo():
 x=seo("After Hours","","R&B","US",["love"],"YouTube");assert x["title"] and "#RnB" in x["hashtags"]
