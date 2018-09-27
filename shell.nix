with import <nixpkgs>{};

let
  smail = (callPackage ./default.nix {});
in ((pkgs.python3.withPackages (ps: [ ps.celery smail ])).override {
  ignoreCollisions = true;
}).env
