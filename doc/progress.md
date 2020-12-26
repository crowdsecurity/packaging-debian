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
 - NEW: golang-github-appleboy-gofight
 - ASK: golang-github-denisbrodbeck-machineid
    + Maybe can be replaced by a direct read from `/etc/machine-id` in
      the `crowdsec` package, e.g. through a Debian-specific patch.
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
    + ASK the Debian Go Team:
       - Shipping `patterns*` through `DH_GOLANG_INSTALL_EXTRA` does
         the job for the test suite, but should test data also be
         shipped in the final binary?
       - Data point: there are a number of similar things in existing
         packages.
 - NEW: golang-github-mohae-deepcopy
 - POC: golang-github-netflix-go-expect
 - POC: golang-github-nxadm-tail
 - POC: golang-github-prometheus-prom2json


## Updated packages, apparently easy


 - POC: golang-github-oschwald-maxminddb-golang
 - POC: golang-github-oschwald-geoip2-golang
 - POC: syncthing [see below, no actual work besides communication]

For this set of packages:
 - The first two needs new upstream versions for `crowdsec` to have
   all required features; Alexandre Viau has been contacted but
   hasn't answered yet.
 - `syncthing` only needs to be checked through `ratt` and probably
   doesn't deserve an upload on its own. It could be nice to send a
   heads-up to its maintainers anyway, just to be on the safe side.


## Updated packages, not so easy/work to be done

 - POC: golang-github-gin-gonic-gin
    + DEP: golang-github-go-playground-validator
 - ASK: golang-github-go-playground-assert
    + go.mod has: github.com/go-playground/assert/v2
 - POC: golang-github-go-playground-locales
    + This one is unversioned.
 - POC: golang-github-go-playground-universal-translator
    + This one is unversioned.
 - ASK: golang-github-go-playground-validator
    + go.mod has: github.com/go-playground/validator/v10
    + golang-gopkg-go-playground-validator.v8-dev exists
       - Should be investigated: remove it, replace it, let it be?
       - Check dependencies
       - Maybe throw ratt at it, trying to rebuild dependencies
         against the new package (that could temporarily provide the
         old one)
    + Possible collision but different hosting sites, so not an issue.
    + DEP: golang-github-go-playground-assert
    + DEP: golang-github-go-playground-locales
    + DEP: golang-github-go-playground-universal-translator
    + DEP: golang-github-leodido-go-urn-dev
 - NEW: golang-github-leodido-go-urn

**XXX:** Build the whole dependency tree, and account for new packages
to be introduced. Shengjing Zhu is aware of the will to update these
packages, and also spotted the need for new packages. `ratt ` will be
more useful here than it will be for the previous set of packages.

Using a prospective binary for `golang-github-gin-gonic-gin` (needing
more work, e.g. the source repack wasn't looked at), and feeing it to
`ratt` with a `sid` schroot configuration pointing at the custom
`devel-gin` repository containing the new dependencies, 35 packages
were determined as needing a rebuild. Only 3 failed, and RC bug
reports seem to exist for each of them:

 - consul 1.0.7~dfsg1-5
    + #964873 (FTBFS; supposed to be fixed, apparently not).
    + A clean build of consul_1.8.6+dfsg1-1.dsc.log in cowbuilder
      looks good.
 - rkt 1.30.0+dfsg1-9
    + #964871
    + Reproduced in a clean cowbuilder.
 - singularity-container 3.5.2+ds1-1
    + Not updated in a 1+ year
    + Several grave security bugs
    + TODO: Unfiled FTBFS bug (reproduced in a clean cowbuilder).

Further tasks:

 - reproduce the FTBFS in a clean sid chroot (without any custom
   repository), and open/update/reopen as needed.
 - rerun `ratt` once `golang-github-gin-gonic-gin` has been cleaned up
   (even if all the new dependencies aren't cleaned up), to ensure
   repacking the source tarball doesn't trigger other side effects.
