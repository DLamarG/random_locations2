./db/setup.sh
docker inspect  -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' locations_db > api/db_ip_addr
./api/start_api.sh
./frontend/start_frontend.sh