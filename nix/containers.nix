{ pkgs, ... }:

with import <nixpkgs> {};

let

  smail = (callPackage ../default.nix {});

  py = ((pkgs.python3.withPackages (ps: [ ps.celery smail ])).override {
    ignoreCollisions = true;
  });
  
  smail-cfg = ''
  '';

in rec {

  networking.firewall.allowedTCPPorts = [ 8080 ];

  services.postfix.enable = true;

  users.users.smail = {
    isNormalUser = true;
  };

  systemd.services.smail-front = {
    enable =  true;
    environment = {};
    description = "Start smail-front.";
    wantedBy = [ "default.target" ];
    serviceConfig = {
      User = "smail";
      ExecStart = "${py}/bin/smail -l 0.0.0.0 -p 8080 --start";
    };
  };

}
