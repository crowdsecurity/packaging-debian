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
 - NEW: golang-github-nxadm-tail
 - POC: golang-github-prometheus-prom2json


## Updated packages, GeoIP-oriented mini-stack

 - ACC: golang-github-oschwald-maxminddb-golang
 - ACC: golang-github-oschwald-geoip2-golang


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


## Further tasks

Maybe adopt packages from Alexandre Viau:

 - #940405: golang-github-oschwald-geoip2-golang
 - #940406: golang-github-oschwald-maxminddb-golang

Maybe clean this up some more:

 - golang-github-nxadm-tail: the cmd and vendor exclusion works fine
   for the final binary, but when building from a checkout, files are
   still copied to the build directory. This is strange, but shouldn't
   be an issue for builds from a source package (e.g. on Debian
   buildds). Note: excluding gopaths instead of local directories
   seems to work fine.
