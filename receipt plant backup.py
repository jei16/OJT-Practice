a = [
    ["PRODUCT DESCRIPTION", "6A ECQ", "REG", "OBC", "TOTAL"],
    ["", "REG", "TOTAL", "TOTAL", ""],
]

#
brdr1 = "{a:┌^1}{b:─^28}{c:┬^1}{d:─^6}{e:┬^1}{f:─^6}{g:┬^1}{h:─^6}{i:┬^1}{j:─^6}{k:┐^1}"
print(brdr1.format(a="", b="", c="", d="", e="", f="", g="", h="", i="", j="", k=""))

#
brdr2 = "{a:│^1}{b:^28}{c:│^1}{d:^6}{e:│^1}{f:^6}{g:│^1}{h:^6}{i:│^1}{j:^6}{k:│^1}"
for b in a:
    print(
        brdr2.format(
            a="", b=b[0], c="", d=b[1], e="", f=b[2], g="", h=b[3], i="", j=b[4], k=""
        )
    )

#
brdr3 = "{a:├^1}{b:─^28}{c:┴^1}{d:─^6}{e:┴^1}{f:─^6}{g:┴^1}{h:─^6}{i:┴^1}{j:─^6}{k:┤^1}"
print(brdr3.format(a="", b="", c="", d="", e="", f="", g="", h="", i="", j="", k=""))

#
brdr4 = "{a:│^1}{b:<56}{c:│^1}"
print(brdr4.format(a="", b="GELATIN/SALAD", c=""))

#
brdr5 = "{a:├^1}{b:─^28}{c:┬^1}{d:─^6}{e:┬^1}{f:─^6}{g:┬^1}{h:─^6}{i:┬^1}{j:─^6}{k:┤^1}"
print(brdr5.format(a="", b="", c="", d="", e="", f="", g="", h="", i="", j="", k=""))

#default
brdr6 = "{a:│^1}{b:<28}{c:│^1}{d:^6}{e:│^1}{f:^6}{g:│^1}{h:^6}{i:│^1}{j:^6}{k:│^1}"
print(
    brdr6.format(
        a="", b="Cathedral Window", c="", d="888", e="", f="22", g="", h="", i="", j="", k=""
    )
)

#looping
brdr7 = "{a:├^1}{b:─<28}{c:┼^1}{d:─^6}{e:┼^1}{f:─^6}{g:┼^1}{h:─^6}{i:┼^1}{j:─^6}{k:┤^1}"
print(brdr7.format(a="", b="", c="", d="", e="", f="", g="", h="", i="", j="", k=""))

#looping
brdr8 = "{a:│^1}{b:<28}{c:│^1}{d:^6}{e:│^1}{f:^6}{g:│^1}{h:^6}{i:│^1}{j:^6}{k:│^1}"
print(
    brdr8.format(
        a="", b="Cathedral Window", c="", d="888", e="", f="22", g="", h="", i="", j="", k=""
    )
)

#default
brdr4loop1 = "{a:├^1}{b:─^28}{c:┴^1}{d:─^6}{e:┴^1}{f:─^6}{g:┴^1}{h:─^6}{i:┴^1}{j:─^6}{k:┤^1}"
print(brdr4loop1.format(a="", b="", c="", d="", e="", f="", g="", h="", i="", j="", k=""))

#
brdr4loop2 = "{a:│^1}{b:<56}{c:│^1}"
print(brdr4loop2.format(a="", b="GELATIN/SALAD", c=""))


#
brdr4loop3 = "{a:├^1}{b:─^28}{c:┬^1}{d:─^6}{e:┬^1}{f:─^6}{g:┬^1}{h:─^6}{i:┬^1}{j:─^6}{k:┤^1}"
print(brdr4loop3.format(a="", b="", c="", d="", e="", f="", g="", h="", i="", j="", k=""))

#
brdr6loop = "{a:│^1}{b:<28}{c:│^1}{d:^6}{e:│^1}{f:^6}{g:│^1}{h:^6}{i:│^1}{j:^6}{k:│^1}"
print(
    brdr6loop.format(
        a="", b="Cathedral Window", c="", d="888", e="", f="22", g="", h="", i="", j="", k=""
    )
)

#default
brdrlast = "{a:└^1}{b:─^28}{c:┴^1}{d:─^6}{e:┴^1}{f:─^6}{g:┴^1}{h:─^6}{i:┴^1}{j:─^6}{k:┘^1}"
print(brdrlast.format(a="", b="", c="", d="", e="", f="", g="", h="", i="", j="", k=""))
