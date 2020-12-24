# Progress tracking

For all dependencies, status can be one of these:
 - POC: proof-of-concept packaging, to be cleaned
 - ITP: cleaned-up happened enough for an ITP to be filed with a proper description
 - NEW: packaging was pushed to salsa, package was uploaded
 - ASK: some specific questions need an answer from the team or from upstream
 - REJECT: more work to be done
 - ACCEPT: package was accepted into the archive

If a specific package has no status set, assume POC.


## New packages

 - crowdsec
 - golang-github-alecaivazis-survey
 - golang-github-antonmedv-expr
 - golang-github-appleboy-gin-jwt
 - golang-github-appleboy-gofight
 - golang-github-denisbrodbeck-machineid
 - golang-github-enescakir-emoji
 - golang-github-facebook-ent
 - golang-github-go-co-op-gocron
 - golang-github-goombaio-namegenerator
 - golang-github-go-openapi-inflect
 - golang-github-hinshun-vt10x
 - golang-github-jamiealquiza-tachymeter
 - golang-github-logrusorgru-grokky
 - golang-github-mohae-deepcopy
 - golang-github-netflix-go-expect
 - golang-github-nxadm-tail
 - golang-github-prometheus-prom2json


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
