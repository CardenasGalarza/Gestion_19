mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"alice.dt.control@gmail.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[theme]\n\
base='dark'\n\
primaryColor='#02fbde'\n\
backgroundColor='#00022b'\n\
secondaryBackgroundColor = '#043562'\n\
textColor='#000000'\n\
font = 'sans serif'\n\

[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
