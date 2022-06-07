MATCH (p:Profiles) SET p.borrar = replace(p.animes_favorites, "[", "")
MATCH (p:Profiles) SET p.borrar2 = replace(p.borrar, "]", "")
MATCH (p:Profiles) SET p.string_array = split(p.borrar2, ",")
MATCH (p:Profiles) REMOVE p.borrar
MATCH (p:Profiles) REMOVE p.borrar2
MATCH (p:Profiles) WITH p UNWIND p.string_array AS uid MATCH(a:Animes {uid_anime: toInteger(lTrim(uid))})
MERGE (p)-[r:FAVORITE]->(a);