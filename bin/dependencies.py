#!/usr/bin/python3
#
# Do interesting things with dependencies.

import os
import re
import sys

from debian import deb822


def build_dependencies(upload_dir):
    os.chdir(upload_dir)
    existing_dsc = [x for x in os.listdir('.')
                    if x.endswith('.dsc')]
    uploaded_dsc = [x for x in existing_dsc
                    if os.path.exists(re.sub(r'\.dsc$', '_amd64.ftp-master.upload', x))]

    sources = []
    build_deps = []
    for dsc in uploaded_dsc:
        # Should be a single paragraph, but...
        for pkg in deb822.Dsc.iter_paragraphs(open(dsc)):
            # print(pkg['Source'])
            # print(pkg['Build-Depends'])
            # print()
            sources.append(pkg['Source'])
            for bd in pkg['Build-Depends'].split(', '):
                bd = re.sub(r' \(.*\)', '', bd)
                #print(pkg['Source'], '->', bd)
                build_deps.append((pkg['Source'], bd))

    accepted = [
        "golang-github-oschwald-geoip2-golang",
        "golang-github-oschwald-maxminddb-golang",
        "golang-github-antonmedv-expr",
        "golang-github-go-playground-locales",
        "golang-github-enescakir-emoji",
        "golang-github-go-playground-assert-v2",
        "golang-github-appleboy-gofight",
        "golang-github-go-playground-validator-v10",
        "golang-github-jamiealquiza-tachymeter",
        "golang-github-leodido-go-urn",
        "golang-github-logrusorgru-grokky",
        "golang-github-mohae-deepcopy",
        "golang-github-go-playground-universal-translator",
        "golang-github-alecaivazis-survey",
        "golang-github-go-co-op-gocron",
        "golang-github-hinshun-vt10x",
        "golang-github-netflix-go-expect",
        "golang-github-nxadm-tail",
    ]

    rebuild_1 = [
        "golang-github-enescakir-emoji",
        "golang-github-antonmedv-expr",
        "golang-github-jamiealquiza-tachymeter",
        "golang-github-logrusorgru-grokky",
        "golang-github-mohae-deepcopy",
        "golang-github-appleboy-gofight",
        "golang-github-go-playground-locales",
        "golang-github-go-playground-assert-v2",
        "golang-github-leodido-go-urn",
        "golang-github-netflix-go-expect",
        "golang-github-go-co-op-gocron",
        "golang-github-nxadm-tail",
    ]

    rebuild_2 = [
        "golang-github-go-playground-universal-translator",
        "golang-github-hinshun-vt10x",
    ]

    rebuild_3 = [
        "golang-github-go-playground-validator-v10",
    ]

    binaries = ['%s-dev' % x for x in sources]
    print('digraph {')
    print('  rankdir=LR;')
    print('  node[shape=box];')
    for (x, y) in build_deps:
        if y in binaries:
            print('  "%s" -> "%s"' % (x, re.sub(r'-dev$', '', y)))
    for x in sources:
        if x in rebuild_1 + rebuild_2 + rebuild_3:
            print('  "%s" [fillcolor=green,style=filled];' % x)
        elif x in accepted:
            print('  "%s" [fillcolor=orange,style=filled];' % x)
        else:
            print('  "%s" [fillcolor=red,style=filled];' % x)
    print('}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("E: Usage: %s path/with/uploads" % sys.argv[0])
        sys.exit(1)
    build_dependencies(sys.argv[1])
