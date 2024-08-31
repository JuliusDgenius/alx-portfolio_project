{pkgs}: {
  deps = [
    pkgs.sqlite-interactive
    pkgs.saw-tools
    pkgs.python312Packages.pycodestyle
    pkgs.tree
    pkgs.neovim
  ];
}
