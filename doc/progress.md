# Progress tracking

For all dependencies, status can be one of these:
 - POC: proof-of-concept packaging, to be cleaned
 - DEP: depends on other packages
 - ITP: cleaned-up happened enough for an ITP to be filed with a proper description
 - NEW: packaging was pushed to salsa, package was uploaded
 - ASK: some specific questions need an answer from the team or from upstream
 - REJ: more work to be done
 - ACC: package was accepted into the archive

If a specific package has no status set, assume POC.


## New packages

 - POC: crowdsec
 - DEP: golang-github-alecaivazis-survey
    + golang-github-hinshun-vt10x
    + golang-github-netflix-go-expect
 - NEW: golang-github-antonmedv-expr
 - DEP: golang-github-appleboy-gin-jwt
    + Updated golang-github-gin-gonic-gin (see below)
 - ITP: golang-github-appleboy-gofight
 - ASK: golang-github-denisbrodbeck-machineid
    + Maybe can be replaced by a direct read from `/etc/machine-id` in
      the `crowdsec` package, e.g. through a Debian-specific patch.
 - POC: golang-github-enescakir-emoji
 - POC: golang-github-facebook-ent
 - POC: golang-github-go-co-op-gocron
 - POC: golang-github-goombaio-namegenerator
 - POC: golang-github-go-openapi-inflect
 - POC: golang-github-hinshun-vt10x
 - POC: golang-github-jamiealquiza-tachymeter
 - POC: golang-github-logrusorgru-grokky
 - POC: golang-github-mohae-deepcopy
 - POC: golang-github-netflix-go-expect
 - POC: golang-github-nxadm-tail
 - POC: golang-github-prometheus-prom2json


## Updated packages, apparently easy


 - golang-github-oschwald-maxminddb-golang
 - golang-github-oschwald-geoip2-golang
 - syncthing

For this set of packages:
 - The first two needs new upstream versions for `crowdsec` to have
   all required features; Alexandre Viau has been contacted but
   hasn't answered yet.
 - `syncthing` only needs to be checked through `ratt` and probably
   doesn't deserve an upload on its own. It could be nice to send a
   heads-up to its maintainers anyway, just to be on the safe side.


## Updated packages, not so easy/work to be done

 - golang-github-gin-gonic-gin
 - golang-github-go-playground-assert
 - golang-github-go-playground-locales
 - golang-github-go-playground-universal-translator
 - golang-github-go-playground-validator
 - golang-github-leodido-go-urn

**XXX:** Build the whole dependency tree, and account for new packages
to be introduced. Shengjing Zhu is aware of the will to update these
packages, and also spotted the need for new packages. `ratt ` will be
more useful here than it will be for the previous set of packages.
