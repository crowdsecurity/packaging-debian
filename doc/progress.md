# Progress tracking

For all dependencies, status can be one of these:
 - POC: proof-of-concept packaging, to be cleaned
 - DEP: depends on other packages
 - ITP: cleaned-up happened enough for an ITP to be filed with a proper description
 - NEW: packaging was pushed to salsa, package was uploaded
 - ASK: some specific questions need an answer from the team or from upstream
 - REJ: more work to be done
 - ACC: package was accepted into the archive
 - SKP: skip!

If a specific package has no status set, assume POC.


## New packages

 - POC: crowdsec
 - DEP: golang-github-alecaivazis-survey
    + golang-github-hinshun-vt10x
    + golang-github-netflix-go-expect
 - NEW: golang-github-antonmedv-expr
 - DEP: golang-github-appleboy-gin-jwt
    + Updated golang-github-gin-gonic-gin (see below)
 - NEW: golang-github-appleboy-gofight
 - SKP: golang-github-denisbrodbeck-machineid
    + Local override, to maintain through a Debian-specific patch.
 - NEW: golang-github-enescakir-emoji
 - POC: golang-github-facebook-ent
 - POC: golang-github-go-co-op-gocron
 - POC: golang-github-goombaio-namegenerator
 - ASK: golang-github-go-openapi-inflect
    + Strange tag situation upstream:
       - https://github.com/go-openapi/inflect/issues/2
    + Close to no metadata, leading to no meaningful descriptions,
      which is a blocker for a proper ITP:
       - https://github.com/go-openapi/inflect/issues/3
 - DEP: golang-github-hinshun-vt10x
    + golang-github-netflix-go-expect
 - NEW: golang-github-jamiealquiza-tachymeter
 - NEW: golang-github-logrusorgru-grokky
 - NEW: golang-github-mohae-deepcopy
 - POC: golang-github-netflix-go-expect
 - POC: golang-github-nxadm-tail
 - POC: golang-github-prometheus-prom2json


## Updated packages, GeoIP-oriented mini-stack


 - ASK: golang-github-oschwald-maxminddb-golang
 - ASK: golang-github-oschwald-geoip2-golang

For this set of packages:
 - New upstream versions are needed for `crowdsec` to have all
   required features.
 - Only reverse dependency: `syncthing` is fine.
 - Review was requested on the list:
     https://lists.debian.org/debian-go/2020/12/msg00060.html


## Updated packages, golang-github-gin-gonic-gin stack

 - ASK: golang-github-gin-gonic-gin
    + DEP: golang-github-go-playground-validator(-v10)
    + Review requested on the list:
        https://lists.debian.org/debian-go/2020/12/msg00059.html
 - NEW: golang-github-go-playground-assert(-v2)
    + go.mod has: github.com/go-playground/assert/v2
 - NEW: golang-github-go-playground-locales
    + This one is unversioned.
 - NEW: golang-github-go-playground-universal-translator
    + This one is unversioned.
    + DEP: golang-github-go-playground-locales
 - NEW: golang-github-go-playground-validator(-v10)
    + go.mod has: github.com/go-playground/validator/v10
    + golang-gopkg-go-playground-validator.v8-dev exists
       - Should be investigated: remove it, replace it, let it be?
    + DEP: golang-github-go-playground-assert(-v2)
    + DEP: golang-github-go-playground-locales
    + DEP: golang-github-go-playground-universal-translator
    + DEP: golang-github-leodido-go-urn-dev
 - NEW: golang-github-leodido-go-urn
