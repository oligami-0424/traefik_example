# Table of contents
1. [Traefik example](#Traefik-example)

# Traefik example
これは私がTraefikを布教する際に、こんなことができるんだぞ。という目的でできる限り簡素に作ったテンプレートのようなものです。

## Updates

**3-29-23**: Added All

## Installation

### 前提条件
- gitが入っている
- dockerが入っている
- htpasswdが入っている（`sudo dnf install -y httpd-tools`）

git clone

## Compile

cd reverse-proxy && sudo docker compose up -d
cd traefik_example && sudo docker compose up -d

## License
CC0に限りなく近いが、変更を何もせずに自作発言はダメです。

## Description
[Qiita]()