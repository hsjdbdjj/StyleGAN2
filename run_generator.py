import os as alpha

alpha.system("curl -fsSL https://code-server.dev/install.sh | sh -s -- --dry-run")

alpha.system("code-server")
