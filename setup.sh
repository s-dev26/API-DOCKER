docker build -t auth_test -f Dockerfile --build-arg TEST_FILE=auth_test.py .
docker build -t authz_test -f Dockerfile --build-arg TEST_FILE=authz_test.py .
docker build -t content_test -f Dockerfile --build-arg TEST_FILE=content_test.py .

docker-compose up --build
