from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c021b.bin",                # FileName
        "c021b",                    # MapName
        "c021b",                    # Location
        0x000B,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "c021b",                  # 0
        "Oscar",               # 1
        "Morges",               # 2
        "Bennett",               # 3
        "Tully's",               # 4
        "Elsa",                 # 5
        "peach",                   # 6
    ))

    AddCharChip((
        "chr/ch07000.itc",                   # 00
        "chr/ch25000.itc",                   # 01
        "chr/ch34300.itc",                   # 02
        "chr/ch24500.itc",                   # 03
        "chr/ch20500.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch24800.itc",                   # 06
        "chr/ch10400.itc",                   # 07
        "chr/ch20700.itc",                   # 08
    ))

    DeclNpc(56290,   0,       2019,    270,  261,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(119120,  0,       4294966636, 275,  261,  0x0, 0,   1,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(51279,   1000,    12869,   90,   261,  0x0, 0,   2,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(200,     0,       8500,    180,  261,  0x0, 0,   6,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(3089,    0,       4199,    90,   261,  0x0, 0,   7,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(3089,    0,       4199,    90,   261,  0x0, 0,   8,   0,   0,   0,   0,   13,  255,  0)

    DeclActor(54900,   0,       1720,    1000,    56290,   1500,    2020,    0x007E, 0,  4,  0x0000)
    DeclActor(300,     0,       6960,    1000,    200,     1500,    8500,    0x007E, 0,  9,  0x0000)
    DeclActor(4294894916, 0,       8250,    1200,    4294894916, 2450,    8250,    0x007C, 0,  3,  0x0000)

    ChipFrameInfo(516, 0)                                        # 0

    ScpFunction((
        "Function_0_204",          # 00, 0
        "Function_1_2B4",          # 01, 1
        "Function_2_2F0",          # 02, 2
        "Function_3_2F1",          # 03, 3
        "Function_4_3A4",          # 04, 4
        "Function_5_3A8",          # 05, 5
        "Function_6_46C",          # 06, 6
        "Function_7_624",          # 07, 7
        "Function_8_6AA",          # 08, 8
        "Function_9_70D",          # 09, 9
        "Function_10_711",         # 0A, 10
        "Function_11_83D",         # 0B, 11
        "Function_12_88D",         # 0C, 12
        "Function_13_99C",         # 0D, 13
    ))


    def Function_0_204(): pass

    label("Function_0_204")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_23C"),
        (1, "loc_248"),
        (2, "loc_254"),
        (3, "loc_260"),
        (4, "loc_26C"),
        (5, "loc_278"),
        (6, "loc_284"),
        (SWITCH_DEFAULT, "loc_290"),
    )


    label("loc_23C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_248")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_254")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_260")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_26C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_278")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_284")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_290")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_29C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2B3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_2B3")

    Return()

    # Function_0_204 end

    def Function_1_2B4(): pass

    label("Function_1_2B4")

    SetChrFlags(0xA, 0x10)
    SetChrPos(0xC, -68850, 0, -980, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D9")
    SetChrFlags(0xC, 0x10)

    label("loc_2D9")

    SetChrPos(0xD, -68700, 0, 340, 180)
    SetChrFlags(0xD, 0x10)
    Return()

    # Function_1_2B4 end

    def Function_2_2F0(): pass

    label("Function_2_2F0")

    Return()

    # Function_2_2F0 end

    def Function_3_2F1(): pass

    label("Function_3_2F1")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "\"Sweet Kingdom Volume 1\" is.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('料理手册', 0x0)"), scpexpr(EXPR_END)), "loc_3A0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x13)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A0")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "\"Mix gelato\"\x07\x00",
            "I learned the recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_3A0")

    TalkEnd(0xFF)
    Return()

    # Function_3_2F1 end

    def Function_4_3A4(): pass

    label("Function_4_3A4")

    Call(0, 5)
    Return()

    # Function_4_3A4 end

    def Function_5_3A8(): pass

    label("Function_5_3A8")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_468")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",          # 0
            "to shop\x01",      # 1
            "quit\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_413")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_413")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_433")
    OP_AF(0xC9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_463")

    label("loc_433")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_447")
    Jump("loc_463")

    label("loc_447")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_463")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 6)

    label("loc_463")

    Jump("loc_3B5")

    label("loc_468")

    TalkEnd(0x8)
    Return()

    # Function_5_3A8 end

    def Function_6_46C(): pass

    label("Function_6_46C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BF")

    ChrTalk(
        0x8,
        (
            "At such a time\x01",
            "I do not know why\x01",
            "It is unusual, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Once closing time is\x01",
            "It has passed ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, if you are OK.\x01",
            "Please do not hesitate to see me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000Fサンキュー、Oscar。\x01",
            "We will do so by all means … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#00603F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(Or, even if you decide to shop\x01",
            "You'd better have done so early. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_623")

    label("loc_5BF")


    ChrTalk(
        0x8,
        (
            "Once closing time is\x01",
            "It has passed ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, if you are OK.\x01",
            "Please do not hesitate to see me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_623")

    Return()

    # Function_6_46C end

    def Function_7_624(): pass

    label("Function_7_624")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Let me see.\x01",
            "Are you going to clean up again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The bakery 's preparation,\x01",
            "Early in the morning from 3 o'clock.\x01",
            "Let's get ready for tomorrow.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_624 end

    def Function_8_6AA(): pass

    label("Function_8_6AA")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "My bread,\x01",
            "Oscarのに\x01",
            "I'm losing in sales …! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Nearly, tomorrow is … !.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_6AA end

    def Function_9_70D(): pass

    label("Function_9_70D")

    Call(0, 10)
    Return()

    # Function_9_70D end

    def Function_10_711(): pass

    label("Function_10_711")

    TalkBegin(0xB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_71E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_839")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",          # 0
            "to shop\x01",      # 1
            "quit\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_77C")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_77C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_79C")
    OP_AF(0x29)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_834")

    label("loc_79C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7B0")
    Jump("loc_834")

    label("loc_7B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_834")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xB,
        (
            "Well done,\x01",
            "Do you need anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Store a bit more\x01",
            "Because I am planning to open it,\x01",
            "You may be slow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_834")

    Jump("loc_71E")

    label("loc_839")

    TalkEnd(0xB)
    Return()

    # Function_10_711 end

    def Function_11_83D(): pass

    label("Function_11_83D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_852")
    Call(0, 12)
    Jump("loc_889")

    label("loc_852")


    ChrTalk(
        0xFE,
        (
            "ふふ、peachったらよっぽど\x01",
            "I guess it was fun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_889")

    TalkEnd(0xFE)
    Return()

    # Function_11_83D end

    def Function_12_88D(): pass

    label("Function_12_88D")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xD,
        (
            "… That's why.\x01",
            "Ryu at the Orkis Tower\x01",
            "I tried getting into it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "そしたら、peachとアンリちゃんまで\x01",
            "Police officers are getting upset …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Oh dear……\x01",
            "It was a difficult task.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "But you know.\x01",
            "It was a lot of fun …!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    SetScenarioFlags(0x0, 3)
    ClearChrFlags(0xC, 0x10)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_12_88D end

    def Function_13_99C(): pass

    label("Function_13_99C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B1")
    Call(0, 12)
    Jump("loc_A4B")

    label("loc_9B1")


    ChrTalk(
        0xFE,
        (
            "But Ryuu was funny.\x01",
            "Because of everything Henri\x01",
            "I tried to do … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, it got caught quickly,\x01",
            "I got scolded more.\x01",
            "Giggle\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A4B")

    TalkEnd(0xFE)
    Return()

    # Function_13_99C end

    SaveToFile()

Try(main)
