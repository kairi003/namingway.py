# Enter your discord token
TOKEN=

# rewrite Dockerfile with your token
sed -e "s/_TOKEN_/${TOKEN}/g" Dockerfile-TEMPLATE > Dockerfile

# initiate container
docker-compose up -d