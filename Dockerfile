FROM php7.4-cli
WORKDIR /usr/src/pmm-parser
COPY . .
CMD ["php", "./index.php"]