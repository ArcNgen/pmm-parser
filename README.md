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