LOAD CSV WITH HEADERS FROM 'file:///data/profiles.csv' AS line
CREATE (:Profiles {name: line.profile, gender: line.gender, 
animes_favorites: line.list_favorites, link_profile: line.link});