LOAD CSV WITH HEADERS FROM 'file:///data/reviews.csv' AS line
MATCH (p:Profiles {name: line.profile}), (a:Animes {uid_anime: toInteger(line.anime_uid)})
CREATE (p)-[:REVIEW {Overall: toInteger(line.Overall), Story: toInteger(line.Story), 
Animation: toInteger(line.Animation), Sound: toInteger(line.Sound), Character: toInteger(line.Character), 
Enjoyment: toInteger(line.Enjoyment)}]->(a);