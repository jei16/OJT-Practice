# data
batches = [
    "6A ECQ REG",
    "6A ECQ OBC",
    "6B ECQ REG",
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
            ["Cathedral WindowCathedral W indowCathedral Window", "1", "2", "3", "4"],
        ],
    ],
    [
        "CHOCOLATE",
        [
            ["Cathedral Gelatin", "1", "2", "3", "4"],
            ["Cathedral ChurchCathedral WindowCathedral", "1", "2", "3", "4"],
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
        "PERIMUM CAKES",
        [
            ["Mango Cathedral Cake Cathedral Cake", "1", "2", "3", "4"],
            ["Cathedral Cake", "1", "2", "3", "4"],
            ["Chocolate Caramel Decadence Cake", "2", "1", "2", "3", "4"],
        ],
    ],
    [
        "PREMIUM CAKES",
        [
            ["Mango Cathedral Cake Cathedral Cake", "1", "2", "3", "4"],
            ["Cathedral Cake", "1", "2", "3", "4"],
            ["Chocolate Caramel Decadence Cake", "2", "1", "2", "3", "4"],
        ],
    ],
]


# first row
brdr1_template = "{a:┌^1}{b:─^28}{c:┬^1}"

dynamic_part1 = ""

for batch in range(len(batches)):
    dynamic_part1 += "{d:─^6}{e:┬^1}".format(d="", e="")

formatted_brdr1 = (
    brdr1_template + dynamic_part1 + "{f:─^6}{g:┬^1}{h:─^6}{i:┬^1}{j:─^6}{k:┐^1}"
)
print(formatted_brdr1.format(a="", b="", c="", f="", g="", h="", i="", j="", k=""))

# second row
brdr2_template = "{a:│^1}{b:^28}{c:│^1}"

dynamic_part2 = ""

for batch in range(len(batches)):
    dynamic_part2 += "{d:^6}{e:│^1}".format(d=batches[batch][:-4], e="")

formatted_brdr2 = (
    brdr2_template + dynamic_part2 + "{f:^6}{g:│^1}{h:^6}{i:│^1}{j:^6}{k:│^1}"
)
print(
    formatted_brdr2.format(
        a="",
        b="PRODUCT DESCRIPTION",
        c="",
        f="REG",
        g="",
        h="OBC",
        i="",
        j="TOTAL",
        k="",
    )
)

# third row
brdr2p1_template = "{a:│^1}{b:^28}{c:│^1}"

dynamic_part3 = ""

for batch in range(len(batches)):
    dynamic_part3 += "{d:^6}{e:│^1}".format(d=batches[batch][-3:], e="")

formatted_brdr2p1 = (
    brdr2p1_template + dynamic_part3 + "{f:^6}{g:│^1}{h:^6}{i:│^1}{j:^6}{k:│^1}"
)
print(
    formatted_brdr2p1.format(
        a="", b="", c="", f="TOTAL", g="", h="TOTAL", i="", j="", k=""
    )
)

# fourth row
brdr3_template = "{a:├^1}{b:─^28}{c:┴^1}"

dynamic_part4 = ""

for batch in range(len(batches)):
    dynamic_part4 += "{d:─^6}{e:┴^1}".format(d="", e="")

formatted_brdr3 = (
    brdr3_template + dynamic_part4 + "{f:─^6}{g:┴^1}{h:─^6}{i:┴^1}{j:─^6}{k:┤^1}"
)
print(
    formatted_brdr3.format(
        a="", b="", c="", d="", e="", f="", g="", h="", i="", j="", k=""
    )
)

#
for items in range(len(itemdetailed) - 1):
    # Item classification
    # fifth row
    brdr4_template = "{a:│^1}{b:<29}"

    dynamic_part5 = ""

    for batch in range(len(batches)):
        dynamic_part5 += "{c:^7}".format(c="")

    formatted_brdr4 = brdr4_template + dynamic_part5 + "{d:^20}{e:│^1}"

    print(formatted_brdr4.format(a="", b=itemdetailed[items][0], d="", e=""))

    # sixth row
    brdr5_template = "{a:├^1}{b:─^28}{c:┬^1}"  # "{d:─^6}{e:┬^1}"

    dynamic_part6 = ""

    for batch in range(len(batches)):
        dynamic_part6 += "{d:─^6}{e:┬^1}".format(d="", e="")

    formatted_brdr5 = (
        brdr5_template + dynamic_part6 + "{f:─^6}{g:┬^1}{h:─^6}{i:┬^1}{j:─^6}{k:┤^1}"
    )

    print(formatted_brdr5.format(a="", b="", c="", f="", g="", h="", i="", j="", k=""))

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
    if len(itemdetailed[-1][-1][q][0]) <= 28:
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
        brdr7 = "{a:├^1}{b:─^28}{c:┼^1}{d:─^6}{e:┼^1}{f:─^6}{g:┼^1}{h:─^6}{i:┼^1}{j:─^6}{k:┤^1}"
        print(
            brdr7.format(
                a="", b="", c="", d="", e="", f="", g="", h="", i="", j="", k=""
            )
        )
    else:
        newDesc = str(itemdetailed[-1][-1][q][0][:27] + "-")
        newDesc2 = str(itemdetailed[-1][-1][q][0][:28])
        transferDesc = str(
            itemdetailed[-1][-1][q][0][27 : len(itemdetailed[-1][-1][q][0]) + 1]
        )
        transferDesc2 = str(
            itemdetailed[-1][-1][q][0][28 : len(itemdetailed[-1][-1][q][0]) + 1]
        )

        if str(itemdetailed[-1][-1][q][0][27]) != " ":
            brdr6 = "{a:│^1}{b:<28}{c:│^1}{d:^6}{e:│^1}{f:^6}{g:│^1}{h:^6}{i:│^1}{j:^6}{k:│^1}"
            print(
                brdr6.format(
                    a="",
                    b=newDesc,
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


# last
if len(itemdetailed[-1][-1][-1][0]) <= 28:
    brdr6last = (
        "{a:│^1}{b:<28}{c:│^1}{d:^6}{e:│^1}{f:^6}{g:│^1}{h:^6}{i:│^1}{j:^6}{k:│^1}"
    )
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
        brdr7last.format(
            a="", b="", c="", d="", e="", f="", g="", h="", i="", j="", k=""
        )
    )
else:
    newDesc = str(itemdetailed[-1][-1][-1][0][:27] + "-")
    newDesc2 = str(itemdetailed[-1][-1][-1][0][:28])
    transferDesc = str(
        itemdetailed[-1][-1][-1][0][27 : len(itemdetailed[-1][-1][-1][0]) + 1]
    )
    transferDesc2 = str(
        itemdetailed[-1][-1][-1][0][28 : len(itemdetailed[-1][-1][-1][0]) + 1]
    )

    if str(itemdetailed[-1][-1][-1][0][27]) != " ":
        brdr6 = (
            "{a:│^1}{b:<28}{c:│^1}{d:^6}{e:│^1}{f:^6}{g:│^1}{h:^6}{i:│^1}{j:^6}{k:│^1}"
        )
        print(
            brdr6.format(
                a="",
                b=newDesc,
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

        brdr6ext = (
            "{a:│^1}{b:<28}{c:│^1}{d:^6}{e:│^1}{f:^6}{g:│^1}{h:^6}{i:│^1}{j:^6}{k:│^1}"
        )
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

        brdr7last = "{a:└^1}{b:─^28}{c:┴^1}{d:─^6}{e:┴^1}{f:─^6}{g:┴^1}{h:─^6}{i:┴^1}{j:─^6}{k:┘^1}"
        print(
            brdr7last.format(
                a="", b="", c="", d="", e="", f="", g="", h="", i="", j="", k=""
            )
        )
    else:
        brdr6 = (
            "{a:│^1}{b:<28}{c:│^1}{d:^6}{e:│^1}{f:^6}{g:│^1}{h:^6}{i:│^1}{j:^6}{k:│^1}"
        )
        print(
            brdr6.format(
                a="",
                b=newDesc2,
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

        brdr6ext = (
            "{a:│^1}{b:<28}{c:│^1}{d:^6}{e:│^1}{f:^6}{g:│^1}{h:^6}{i:│^1}{j:^6}{k:│^1}"
        )
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

        brdr7last = "{a:└^1}{b:─^28}{c:┴^1}{d:─^6}{e:┴^1}{f:─^6}{g:┴^1}{h:─^6}{i:┴^1}{j:─^6}{k:┘^1}"
        print(
            brdr7last.format(
                a="", b="", c="", d="", e="", f="", g="", h="", i="", j="", k=""
            )
        )


#
