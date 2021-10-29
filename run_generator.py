mkdir -p ~/.local/lib ~/.local/bin
curl -fL https://github.com/cdr/code-server/releases/download/v$VERSION/code-server-$VERSION-linux-amd64.tar.gz \
  | tar -C ~/.local/lib -xz
mv ~/.local/lib/code-server-$VERSION-linux-amd64 ~/.local/lib/code-server-$VERSION
ln -s ~/.local/lib/code-server-$VERSION/bin/code-server ~/.local/bin/code-server
PATH="~/.local/bin:$PATH"
