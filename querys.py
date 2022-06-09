query_1 = '''
MATCH (a:Animes)
WHERE a.n_members IS NOT NULL
RETURN a.title AS title, a.link_anime AS link_anime, a.n_members AS n_members
ORDER BY n_members DESC LIMIT 3
'''

query_2 = '''
MATCH (a:Animes)
WHERE a.score IS NOT NULL
RETURN a.title AS title, a.link_anime AS link_anime, a.score AS score
ORDER BY score DESC LIMIT 3
'''

query_3 = '''
MATCH (a1:Animes {title: $title})
WITH a1 UNWIND split(a1.list_genres, ",") AS genre 
MATCH (a2:Animes) 
WHERE lTrim(genre) IN split(a2.list_genres, ",") AND 
a2.title <> a1.title AND 
ABS(a2.score - a1.score) <= 0.1 AND 
(ABS(a2.n_members - a1.n_members)/a2.n_members) <= 0.1 
RETURN DISTINCT(a2.title) AS title, a2.score AS score, 
a2.n_members AS n_members, a2.list_genres AS genres
'''

query_4 = '''
MATCH (a:Animes)
WHERE a.{genre} = 1 AND
a.n_episodes >= $min_episodes AND
a.n_episodes <= $max_episodes AND
a.score IS NOT NULL
RETURN a.title AS title, a.link_anime AS link_anime, 
a.score AS score, a.n_episodes AS n_episodes
ORDER BY score DESC LIMIT $max_results
'''

query_5 = '''
MATCH (p:Profiles)-[r:REVIEW]->(a:Animes)
WHERE a.score IS NOT NULL
RETURN a.title AS title, a.link_anime AS link_anime, 
a.score AS score, ROUND(AVG(r.Overall), 2) AS avg_Overall, COUNT(r) as total
ORDER BY total DESC LIMIT $max_results
'''

query_6 = '''
MATCH (p:Profiles {gender: $gender})-[r:REVIEW]->(a:Animes {title: $title})
WITH p.name AS user, r.Overall AS Overall, r.Character AS Character, r.Enjoyment AS Enjoyment,
r.Animation AS Animation, r.Sound AS Sound, r.Story AS Story
RETURN user, Overall, Character, Enjoyment, Animation, Sound, Story
ORDER BY RAND() LIMIT $max_results
'''

query_7 = '''
MATCH (p:Profiles {name: $name})-[r:REVIEW]->(a:Animes)
RETURN a.title AS title, a.link_anime AS link_anime, a.score AS score,
r.Overall AS Overall, r.Character AS Character, r.Enjoyment AS Enjoyment,
r.Animation AS Animation, r.Sound AS Sound, r.Story AS Story
'''

query_8 = '''
MATCH (p:Profiles)-[r:REVIEW]->(a:Animes {title: $title})
RETURN p.gender AS gender, a.score AS score, ROUND(AVG(r.Overall), 2) AS avg_Overall,
ROUND(AVG(r.Character), 2) AS avg_Character, ROUND(AVG(r.Enjoyment), 2) AS avg_Enjoyment,
ROUND(AVG(r.Animation), 2) AS avg_Animation, ROUND(AVG(r.Sound), 2) AS avg_Sound,
ROUND(AVG(r.Story), 2) AS avg_Story
''' 

query_9 = '''
MATCH (p:Profiles)-[r:REVIEW]->(a:Animes)
WHERE a.{genre} = 1 AND
p.gender = $gender AND
a.score >= $min_score AND
a.score <= $max_score
RETURN a.title AS title, a.score AS score, 
ROUND(AVG(r.Overall), 2) AS avg_Overall, COUNT(r) AS total
ORDER BY total DESC LIMIT $max_results
'''

query_10 = '''
MATCH (a:Animes)<-[r:FAVORITE]-(p:Profiles)
RETURN a.title AS title, COUNT(r) AS inDegree
ORDER BY inDegree DESC LIMIT $max_results
'''

query_11 = '''
MATCH (a1:Animes {title: $title_1})<-[r1:FAVORITE]-(p1:Profiles)-
[r2:FAVORITE]->(a2:Animes {title: $title_2})
WITH COLLECT(DISTINCT(p1.name)) AS p
MATCH (a3:Animes {title: $title_3})<-[r3:FAVORITE]-(p2:Profiles)
WHERE p2.name IN p
RETURN p2.name AS user, p2.gender AS gender, COUNT(*) AS total
'''

query_12 = '''
MATCH (a1:Animes {title: $title})<-[r1:FAVORITE]-
(p:Profiles {gender: $gender})-[r2:FAVORITE]->(a2:Animes)
RETURN a2.title AS title, a2.link_anime AS link_anime, a2.score AS score,
COUNT(r2) AS total
ORDER BY total DESC LIMIT $max_results
'''

query_13 = '''
MATCH (a1:Animes {title: $title}) 
WITH a1 UNWIND split(a1.list_genres, ",") AS genre 
MATCH (a1)<-[r1:FAVORITE]-(p:Profiles)-[r2:FAVORITE]->(a2:Animes) 
WHERE lTrim(genre) IN split(a2.list_genres, ",") AND
ABS(a2.score - a1.score) <= 0.25
RETURN DISTINCT(a2.title) AS title, a2.score AS score, 
a2.list_genres AS list_genres, COUNT(r2) AS total 
ORDER BY total DESC LIMIT $max_results
'''

query_14 = '''
MATCH (a1:Animes {title: $title_1})<-[r1:FAVORITE]-
(p1:Profiles {gender: $gender})-[r2:FAVORITE]->(a2:Animes {title: $title_2})
WITH COLLECT(DISTINCT(p1.name)) AS p
MATCH (a3:Animes)<-[r3:FAVORITE]-(p2:Profiles)
WHERE p2.name IN p AND NOT a3.title IN [$title_1, $title_2]
RETURN a3.title AS title, a3.score AS score, COUNT(r3) AS total
ORDER BY total DESC LIMIT $max_results
'''

query_15 = '''
MATCH (a1:Animes)<-[r1:REVIEW]-(p:Profiles)
-[r2:FAVORITE]->(a2:Animes)
WHERE r1.Overall >= $min_score AND
p.gender = $gender AND
a1.{genre} = 1 AND
a2.{genre} = 1
RETURN a2.title AS title, COUNT(r2) AS total
ORDER BY total DESC LIMIT $max_results
'''
