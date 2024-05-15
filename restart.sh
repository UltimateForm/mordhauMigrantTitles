docker stop mh-rcon-migrant-titles
docker rm mh-rcon-migrant-titles
docker build . -t mh-rcon-migrant-titles-img
docker run -d --rm --name mh-rcon-migrant-titles mh-rcon-migrant-titles-img
