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
