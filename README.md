# Table of contents
1. [Traefik example](#Traefik-example)

# Traefik example
これは私がTraefikを布教する際に、こんなことができるんだぞ。という目的でできる限り簡素に作ったテンプレートのようなものです。
[実際に動いている奴（しばらくは動かす）](https://oligami.ml/traefik_example/)

## Updates

**3-29-23**: Added All

## Installation

### 前提条件
- gitが入っている
- dockerが入っている
- htpasswdが入っている（`sudo dnf install -y httpd-tools`）

git clone https://github.com/oligami-0424/traefik_example.git

## Compile

cd reverse-proxy && sudo docker compose up -d <br>
cd traefik_example && sudo docker compose up -d

## License
CC0に限りなく近いが、変更を何もせずに自作発言はダメです。

## Description
[Qiita](https://qiita.com/oligami/items/616ec6bc4d1d19fdcd30)

## http3
This is http3 enabled.<br>
but [This site](https://http3check.net/?host=oligami.ml) return quick is not supported.<br>
[This site](https://http3check.net/?host=oligami.ml) return http3<br>
[This site](https://http3.is/) is your browser enable http3<br>
If you want more info so read https://github.com/traefik/traefik/issues/8255<br>
About this issue is because `quick go`
