mkdir -p ~ /.streamlit

echo "[server]
headless = True
port = $port
enableCORS = False
" > /.streamlit/config.toml