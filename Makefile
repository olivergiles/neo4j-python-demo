.PHONEY: run_db
run_db:
		docker run \
    --restart always \
    --publish=7474:7474 --publish=7687:7687 \
    --volume=${HOME}/neo4j/data:/data \
		--env NEO4J_AUTH=neo4j/your_password \
    neo4j:4.4.9
