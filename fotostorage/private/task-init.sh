#!/usr/bin/env bash

rnddir() {
  tr -dc 'a-zA-Z0-9_\-' </dev/urandom | fold -w 10 | head -n 1
}

new_dir="/var/www/html/$(rnddir)"
mkdir -- "$new_dir"
chown www-data:www-data -- "$new_dir"
cd /tmp
mv -- flag.jpg "$new_dir/F1@g.jpg"
unzip cats.zip || exit

cd /var/www/html
for file in $(ls -1 /tmp); do
  new_dir="$(rnddir)"
  mkdir -- "$new_dir"
  mv -- "/tmp/$file" "$new_dir/$(rnddir).jpg"
  chown -R www-data:www-data -- "$new_dir"
done
