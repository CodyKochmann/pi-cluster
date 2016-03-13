function allow {
  sudo ufw allow $@
}

allow 22 
allow 53/tcp
allow 80/tcp
allow 443

