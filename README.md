# PMM data processor 

## Text data parser 

Setup first image for parsing text files. 

```bash
git init
touch README.md
touch Dockerfile
```

Edit **Dockerfile**

```docker
FROM php7.4-cli
WORKDIR /usr/src/pmm-parser
COPY . .
CMD ["php", "./index.php"]
```
In terminal
```docker
docker images
docker rmi pmm-test-cli:latest
docker build -t pmm-test-cli .
docker images
docker run -it --rm --name pmm-test pmm-test-cli
```