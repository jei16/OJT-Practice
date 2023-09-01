a = [
    ["PRODUCT DESCRIPTION", "6A ECQ", "REG", "OBC", "TOTAL"],
    ["", "REG", "TOTAL", "TOTAL", ""],
]

itemdetailed = [
    [
        "GELATIN/SALAD",
        [
            [
                "Cathedral Gelatin Cathedral GelatinCathedral",
                "1",
                "2",
                "3",
                "4",
            ],
            ["Cathedral Church", "1", "2", "3", "4"],
            ["Cathedral WindowCathedral WindowCathedral Window", "1", "2", "3", "4"],
        ],
    ],
    [
        "CHOCOLATE",
        [
            ["Cathedral Gelatin", "1", "2", "3", "4"],
            ["Cathedral Church", "1", "2", "3", "4"],
            ["Cathedral Window", "1", "2", "3", "4"],
        ],
    ],
    [
        "CHEESE",
        [
            ["Cathedral Gelatin", "1", "2", "3", "4"],
            ["Cathedral Church", "1", "2", "3", "4"],
            ["Cathedral Window", "1", "2", "3", "4"],
            ["Cathedral Gelatin", "1", "2", "3", "4"],
        ],
    ],
    [
        "STRAWBERRY",
        [
            ["Mango", "1", "2", "3", "4"],
            ["Cathedral Cake", "1", "2", "3", "4"],
            ["Cathedral 2", "1", "2", "3", "4"],
        ],
    ],
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
for items in range(len(itemdetailed) - 1):
    # Item classification
    brdr4 = "{a:│^1}{b:<56}{c:│^1}"
    print(brdr4.format(a="", b=itemdetailed[items][0], c=""))

    #
    brdr5 = (
        "{a:├^1}{b:─^28}{c:┬^1}{d:─^6}{e:┬^1}{f:─^6}{g:┬^1}{h:─^6}{i:┬^1}{j:─^6}{k:┤^1}"
    )
    print(
        brdr5.format(a="", b="", c="", d="", e="", f="", g="", h="", i="", j="", k="")
    )

    # Item Details
    for y in range(len(itemdetailed[items][1]) - 1):
        if len(itemdetailed[items][1][y][0]) <= 28:
            brdr6 = "{a:│^1}{b:<28}{c:│^1}{d:^6}{e:│^1}{f:^6}{g:│^1}{h:^6}{i:│^1}{j:^6}{k:│^1}"
            print(
                brdr6.format(
                    a="",
                    b=itemdetailed[items][1][y][0],
                    c="",
                    d=itemdetailed[items][1][y][1],
                    e="",
                    f=itemdetailed[items][1][y][2],
                    g="",
                    h=itemdetailed[items][1][y][3],
                    i="",
                    j=itemdetailed[items][1][y][4],
                    k="",
                )
            )

            brdr7 = "{a:├^1}{b:─^28}{c:┼^1}{d:─^6}{e:┼^1}{f:─^6}{g:┼^1}{h:─^6}{i:┼^1}{j:─^6}{k:┤^1}"
            print(
                brdr7.format(
                    a="", b="", c="", d="", e="", f="", g="", h="", i="", j="", k=""
                )
            )
        else:
            newDesc = str(itemdetailed[items][1][y][0][:27] + "-")
            newDesc2 = str(itemdetailed[items][1][y][0][:28])
            transferDesc = str(
                itemdetailed[items][1][y][0][27 : len(itemdetailed[items][1][y][0]) + 1]
            )
            transferDesc2 = str(
                itemdetailed[items][1][y][0][28 : len(itemdetailed[items][1][y][0]) + 1]
            )

            if str(itemdetailed[items][1][y][0][27]) != " ":
                brdr6 = "{a:│^1}{b:<28}{c:│^1}{d:^6}{e:│^1}{f:^6}{g:│^1}{h:^6}{i:│^1}{j:^6}{k:│^1}"
                print(
                    brdr6.format(
                        a="",
                        b=newDesc,
                        c="",
                        d=itemdetailed[items][1][y][1],
                        e="",
                        f=itemdetailed[items][1][y][2],
                        g="",
                        h=itemdetailed[items][1][y][3],
                        i="",
                        j=itemdetailed[items][1][y][4],
                        k="",
                    )
                )

                brdr6ext = "{a:│^1}{b:<28}{c:│^1}{d:^6}{e:│^1}{f:^6}{g:│^1}{h:^6}{i:│^1}{j:^6}{k:│^1}"
                print(
                    brdr6ext.format(
                        a="",
                        b=transferDesc,
                        c="",
                        d="",
                        e="",
                        f="",
                        g="",
                        h="",
                        i="",
                        j="",
                        k="",
                    )
                )

                brdr7 = "{a:├^1}{b:─^28}{c:┼^1}{d:─^6}{e:┼^1}{f:─^6}{g:┼^1}{h:─^6}{i:┼^1}{j:─^6}{k:┤^1}"
                print(
                    brdr7.format(
                        a="", b="", c="", d="", e="", f="", g="", h="", i="", j="", k=""
                    )
                )
            else:
                brdr6 = "{a:│^1}{b:<28}{c:│^1}{d:^6}{e:│^1}{f:^6}{g:│^1}{h:^6}{i:│^1}{j:^6}{k:│^1}"
                print(
                    brdr6.format(
                        a="",
                        b=newDesc2,
                        c="",
                        d=itemdetailed[items][1][y][1],
                        e="",
                        f=itemdetailed[items][1][y][2],
                        g="",
                        h=itemdetailed[items][1][y][3],
                        i="",
                        j=itemdetailed[items][1][y][4],
                        k="",
                    )
                )

                brdr6ext = "{a:│^1}{b:<28}{c:│^1}{d:^6}{e:│^1}{f:^6}{g:│^1}{h:^6}{i:│^1}{j:^6}{k:│^1}"
                print(
                    brdr6ext.format(
                        a="",
                        b=transferDesc2,
                        c="",
                        d="",
                        e="",
                        f="",
                        g="",
                        h="",
                        i="",
                        j="",
                        k="",
                    )
                )

                brdr7 = "{a:├^1}{b:─^28}{c:┼^1}{d:─^6}{e:┼^1}{f:─^6}{g:┼^1}{h:─^6}{i:┼^1}{j:─^6}{k:┤^1}"
                print(
                    brdr7.format(
                        a="", b="", c="", d="", e="", f="", g="", h="", i="", j="", k=""
                    )
                )

    if len(itemdetailed[items][-1][-1][0]) <= 28:
        brdr6lasts = (
            "{a:│^1}{b:<28}{c:│^1}{d:^6}{e:│^1}{f:^6}{g:│^1}{h:^6}{i:│^1}{j:^6}{k:│^1}"
        )
        print(
            brdr6lasts.format(
                a="",
                b=itemdetailed[items][-1][-1][0],
                c="",
                d=itemdetailed[items][-1][-1][1],
                e="",
                f=itemdetailed[items][-1][-1][2],
                g="",
                h=itemdetailed[items][-1][-1][3],
                i="",
                j=itemdetailed[items][-1][-1][4],
                k="",
            )
        )
        brdr3 = "{a:├^1}{b:─^28}{c:┴^1}{d:─^6}{e:┴^1}{f:─^6}{g:┴^1}{h:─^6}{i:┴^1}{j:─^6}{k:┤^1}"
        print(
            brdr3.format(
                a="", b="", c="", d="", e="", f="", g="", h="", i="", j="", k=""
            )
        )
    else:
        newDesc = str(itemdetailed[items][-1][-1][0][:27] + "-")
        newDesc2 = str(itemdetailed[items][-1][-1][0][:28])
        transferDesc = str(
            itemdetailed[items][-1][-1][0][27 : len(itemdetailed[items][-1][-1][0]) + 1]
        )
        transferDesc2 = str(
            itemdetailed[items][-1][-1][0][28 : len(itemdetailed[items][-1][-1][0]) + 1]
        )

        if itemdetailed[items][-1][-1][0][27] != " ":
            brdr6 = "{a:│^1}{b:<28}{c:│^1}{d:^6}{e:│^1}{f:^6}{g:│^1}{h:^6}{i:│^1}{j:^6}{k:│^1}"
            print(
                brdr6.format(
                    a="",
                    b=newDesc,
                    c="",
                    d=itemdetailed[items][1][-1][1],
                    e="",
                    f=itemdetailed[items][1][-1][2],
                    g="",
                    h=itemdetailed[items][1][-1][3],
                    i="",
                    j=itemdetailed[items][1][-1][4],
                    k="",
                )
            )

            brdr6ext = "{a:│^1}{b:<28}{c:│^1}{d:^6}{e:│^1}{f:^6}{g:│^1}{h:^6}{i:│^1}{j:^6}{k:│^1}"
            print(
                brdr6ext.format(
                    a="",
                    b=transferDesc,
                    c="",
                    d="",
                    e="",
                    f="",
                    g="",
                    h="",
                    i="",
                    j="",
                    k="",
                )
            )

            brdr3 = "{a:├^1}{b:─^28}{c:┴^1}{d:─^6}{e:┴^1}{f:─^6}{g:┴^1}{h:─^6}{i:┴^1}{j:─^6}{k:┤^1}"
            print(
                brdr3.format(
                    a="", b="", c="", d="", e="", f="", g="", h="", i="", j="", k=""
                )
            )
        else:
            brdr6 = "{a:│^1}{b:<28}{c:│^1}{d:^6}{e:│^1}{f:^6}{g:│^1}{h:^6}{i:│^1}{j:^6}{k:│^1}"
            print(
                brdr6.format(
                    a="",
                    b=newDesc2,
                    c="",
                    d=itemdetailed[items][1][-1][1],
                    e="",
                    f=itemdetailed[items][1][-1][2],
                    g="",
                    h=itemdetailed[items][1][-1][3],
                    i="",
                    j=itemdetailed[items][1][-1][4],
                    k="",
                )
            )

            brdr6ext = "{a:│^1}{b:<28}{c:│^1}{d:^6}{e:│^1}{f:^6}{g:│^1}{h:^6}{i:│^1}{j:^6}{k:│^1}"
            print(
                brdr6ext.format(
                    a="",
                    b=transferDesc2,
                    c="",
                    d="",
                    e="",
                    f="",
                    g="",
                    h="",
                    i="",
                    j="",
                    k="",
                )
            )

            brdr3 = "{a:├^1}{b:─^28}{c:┴^1}{d:─^6}{e:┴^1}{f:─^6}{g:┴^1}{h:─^6}{i:┴^1}{j:─^6}{k:┤^1}"
            print(
                brdr3.format(
                    a="", b="", c="", d="", e="", f="", g="", h="", i="", j="", k=""
                )
            )


# Last Table
brdr4last = "{a:│^1}{b:<56}{c:│^1}"
print(brdr4last.format(a="", b=itemdetailed[-1][0], c=""))

brdr5 = "{a:├^1}{b:─^28}{c:┬^1}{d:─^6}{e:┬^1}{f:─^6}{g:┬^1}{h:─^6}{i:┬^1}{j:─^6}{k:┤^1}"
print(brdr5.format(a="", b="", c="", d="", e="", f="", g="", h="", i="", j="", k=""))

for q in range(len(itemdetailed[-1][-1]) - 1):
    brdr6lasts = (
        "{a:│^1}{b:<28}{c:│^1}{d:^6}{e:│^1}{f:^6}{g:│^1}{h:^6}{i:│^1}{j:^6}{k:│^1}"
    )
    print(
        brdr6lasts.format(
            a="",
            b=itemdetailed[-1][-1][q][0],
            c="",
            d=itemdetailed[-1][-1][q][1],
            e="",
            f=itemdetailed[-1][-1][q][2],
            g="",
            h=itemdetailed[-1][-1][q][3],
            i="",
            j=itemdetailed[-1][-1][q][4],
            k="",
        )
    )
    brdr7 = (
        "{a:├^1}{b:─^28}{c:┼^1}{d:─^6}{e:┼^1}{f:─^6}{g:┼^1}{h:─^6}{i:┼^1}{j:─^6}{k:┤^1}"
    )
    print(
        brdr7.format(a="", b="", c="", d="", e="", f="", g="", h="", i="", j="", k="")
    )

# last

brdr6last = "{a:│^1}{b:<28}{c:│^1}{d:^6}{e:│^1}{f:^6}{g:│^1}{h:^6}{i:│^1}{j:^6}{k:│^1}"
print(
    brdr6last.format(
        a="",
        b=itemdetailed[-1][-1][-1][0],
        c="",
        d=itemdetailed[-1][-1][-1][1],
        e="",
        f=itemdetailed[-1][-1][-1][2],
        g="",
        h=itemdetailed[-1][-1][-1][3],
        i="",
        j=itemdetailed[-1][-1][-1][4],
        k="",
    )
)

brdr7last = (
    "{a:└^1}{b:─^28}{c:┴^1}{d:─^6}{e:┴^1}{f:─^6}{g:┴^1}{h:─^6}{i:┴^1}{j:─^6}{k:┘^1}"
)

print(
    brdr7last.format(a="", b="", c="", d="", e="", f="", g="", h="", i="", j="", k="")
)

#
