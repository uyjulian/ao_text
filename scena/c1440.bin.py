from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c1440.bin",                # FileName
        "c1440",                    # MapName
        "c1440",                    # Location
        0x0031,                     # MapIndex
        "ed7101",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 49, 0, 1, 0, 2],
    )

    BuildStringList((
        "c1440",                  # 0
        "Ashley",             # 1
        "Jingo",                 # 2
        "Dino",               # 3
        "Koki",                 # 4
        "Van",                 # 5
        "Ruze",                   # 6
    ))

    AddCharChip((
        "chr/ch09200.itc",                   # 00
        "chr/ch23900.itc",                   # 01
        "chr/ch06800.itc",                   # 02
        "chr/ch23000.itc",                   # 03
        "chr/ch24700.itc",                   # 04
        "chr/ch30800.itc",                   # 05
    ))

    DeclNpc(4294964437, 0,       13750,   0,    261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(5670,    29,      8649,    225,  261,  0x0, 0,   1,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(0,       0,       15090,   225,  389,  0x0, 0,   2,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(2000,    0,       15090,   0,    389,  0x0, 0,   5,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(9640,    0,       850,     180,  389,  0x0, 0,   3,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(10279,   0,       4294966746, 315,  389,  0x0, 0,   4,   0,   0,   0,   0,   13,  255,  0)

    DeclEvent(0x0000, 0, 21,  9.899999618530273,     14.0,                  -0.5,                  16.0,                  [0.25,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -2.4749999046325684,   -7.0,                  0.10000000149011612,   1.0])

    DeclActor(4590,    0,       7540,    1000,    5670,    1500,    8650,    0x007E, 0,  6,  0x0000)
    DeclActor(4294916276, 0,       6820,    1200,    4294916276, 1150,    6820,    0x007C, 0,  3,  0x0000)

    ChipFrameInfo(596, 0)                                        # 0

    ScpFunction((
        "Function_0_254",          # 00, 0
        "Function_1_304",          # 01, 1
        "Function_2_4F2",          # 02, 2
        "Function_3_5BB",          # 03, 3
        "Function_4_672",          # 04, 4
        "Function_5_26B9",         # 05, 5
        "Function_6_2935",         # 06, 6
        "Function_7_2939",         # 07, 7
        "Function_8_3BCC",         # 08, 8
        "Function_9_3EBF",         # 09, 9
        "Function_10_3F0F",        # 0A, 10
        "Function_11_417D",        # 0B, 11
        "Function_12_41D5",        # 0C, 12
        "Function_13_4245",        # 0D, 13
        "Function_14_42A1",        # 0E, 14
        "Function_15_441D",        # 0F, 15
        "Function_16_45C2",        # 10, 16
        "Function_17_4985",        # 11, 17
        "Function_18_4E60",        # 12, 18
        "Function_19_5B79",        # 13, 19
        "Function_20_5EAB",        # 14, 20
        "Function_21_6738",        # 15, 21
    ))


    def Function_0_254(): pass

    label("Function_0_254")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_28C"),
        (1, "loc_298"),
        (2, "loc_2A4"),
        (3, "loc_2B0"),
        (4, "loc_2BC"),
        (5, "loc_2C8"),
        (6, "loc_2D4"),
        (SWITCH_DEFAULT, "loc_2E0"),
    )


    label("loc_28C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_298")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2A4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2B0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2BC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2C8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2D4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2E0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_303")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_303")

    Return()

    # Function_0_254 end

    def Function_1_304(): pass

    label("Function_1_304")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_312")
    Jump("loc_4DB")

    label("loc_312")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_320")
    Jump("loc_4DB")

    label("loc_320")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_32E")
    Jump("loc_4DB")

    label("loc_32E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_34B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_346")
    SetChrFlags(0x8, 0x10)

    label("loc_346")

    Jump("loc_4DB")

    label("loc_34B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_359")
    Jump("loc_4DB")

    label("loc_359")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3A7")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xC, -2960, 20, 8530, 315)
    SetChrPos(0xD, -3010, 30, 7170, 315)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A2")
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xD, 0x10)

    label("loc_3A2")

    Jump("loc_4DB")

    label("loc_3A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_441")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x8, -2240, 20, 13000, 225)
    SetChrPos(0xB, -2630, 20, 11000, 0)
    SetChrPos(0xA, -3850, 0, 11830, 45)
    SetChrFlags(0xB, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_406")
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x8, 0x10)

    label("loc_406")

    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xC, 4930, 0, 4600, 315)
    SetChrPos(0xD, 5930, 0, 4600, 315)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xD, 0x10)
    Jump("loc_4DB")

    label("loc_441")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_454")
    SetChrFlags(0x8, 0x80)
    Jump("loc_4DB")

    label("loc_454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_491")
    SetChrPos(0x8, 1750, 30, 10220, 135)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47D")
    SetChrFlags(0x8, 0x10)

    label("loc_47D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48C")
    SetChrFlags(0x9, 0x10)

    label("loc_48C")

    Jump("loc_4DB")

    label("loc_491")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_49F")
    Jump("loc_4DB")

    label("loc_49F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4AD")
    Jump("loc_4DB")

    label("loc_4AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4BB")
    Jump("loc_4DB")

    label("loc_4BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x138, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D6")
    SetMapFlags(0x10000000)
    Event(0, 16)

    label("loc_4D6")

    SetChrFlags(0x8, 0x10)

    label("loc_4DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F1")
    SetMapFlags(0x10000000)
    Event(0, 17)

    label("loc_4F1")

    Return()

    # Function_1_304 end

    def Function_2_4F2(): pass

    label("Function_2_4F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_505")
    OP_1B(0x0, 0x0, 0x13)

    label("loc_505")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_51E")
    OP_10(0x0, 0x0)
    OP_10(0x3, 0x1)
    Jump("loc_524")

    label("loc_51E")

    OP_10(0x0, 0x1)
    OP_10(0x3, 0x0)

    label("loc_524")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 7)), scpexpr(EXPR_END)), "loc_532")
    ModifyEventFlags(0, 0, 0x80)

    label("loc_532")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_57B")
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_57B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5BA")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)

    label("loc_5BA")

    Return()

    # Function_2_4F2 end

    def Function_3_5BB(): pass

    label("Function_3_5BB")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is \"exciting family lunch\".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('料理手册', 0x0)"), scpexpr(EXPR_END)), "loc_66E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0xE)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66E")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "\"Leisure Lunch Box\"\x07\x00",
            "I learned the recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_66E")

    TalkEnd(0xFF)
    Return()

    # Function_3_5BB end

    def Function_4_672(): pass

    label("Function_4_672")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_693")
    Call(0, 18)
    Return()

    label("loc_693")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A5")
    Call(0, 20)
    Return()

    label("loc_6A5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_811")

    ChrTalk(
        0xFE,
        (
            "At the same time as President's detention,\x01",
            "Such a \"big tree\"\x01",
            "That is not to appear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The barrier disappeared and vigilance to the two major powers also\x01",
            "When it is time to … …\x01",
            "It is a terrible difficult ground, here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Kuku … … It has become interesting, is not it?\x01",
            "If this is the case, as a weapon merchant,\x01",
            "Let's be involved with dirt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FHey, hey, hey.\x01",
            "…… I will ask for more convenience.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_8BE")

    label("loc_811")


    ChrTalk(
        0xFE,
        (
            "As warning against two major powers is increasing now,\x01",
            "It seems that demand will increase for my job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Kuku … … It has become interesting, is not it?\x01",
            "If this is the case, as a weapon merchant,\x01",
            "Let's be involved with dirt.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8BE")

    Jump("loc_26B5")

    label("loc_8C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_CAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C15")

    ChrTalk(
        0xFE,
        "Oh, are you guys here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Kuku …. It's been a long time.\x01",
            "It seems surprisingly healthy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FAshleyさん、お久しぶりです。\x02\x03",
            "#00012F… or so, in this situation\x01",
            "It does not seem to work at all.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A2B")

    ChrTalk(
        0x10A,
        (
            "#00600FShe has the police underground activity\x01",
            "I was being supported.\x02\x03",
            "#00603FEven if you are predicting possible situations\x01",
            "There is no mystery.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A90")

    label("loc_A2B")


    ChrTalk(
        0xFE,
        "Well, it is a situation that I was feeling.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Dudley's Underground Activity\x01",
            "Because I am helping, is it natural?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A90")


    ChrTalk(
        0x102,
        "#00105FWell, was that so ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FTo the private sector as it is\x01",
            "It seems there are collaborators.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FWell, if you are an underground organization partner\x01",
            "I guess you are accustomed to business as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's it, that's it.\x01",
            "Thanks to you I'm making money.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… In preparation for an emergency,\x01",
            "It is preparing variously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I pulled it out from the back of the warehouse\x01",
            "There are plenty of good stuff as it is.\x01",
            "必要ならJingoと交渉しな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BE, 4)
    Jump("loc_CA6")

    label("loc_C15")


    ChrTalk(
        0xFE,
        (
            "In preparation for an emergency,\x01",
            "It is preparing variously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I pulled it out from the back of the warehouse\x01",
            "There are plenty of good stuff as it is.\x01",
            "必要ならJingoと交渉しな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CA6")

    Jump("loc_26B5")

    label("loc_CAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_EFC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E3D")

    ChrTalk(
        0xFE,
        (
            "Is the crossbell independent?\x01",
            "Huh, that banker too\x01",
            "I made a big decision.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Kuku, red hair.\x01",
            "If you are aware of it?\x01",
            "It smells like the battlefield comes near.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F…… Indeed.\x01",
            "I do not think that the two major powers are still silent … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Kuku, a blood as a weapon merchant\x01",
            "It all came.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I thought of leaving the crossbell,\x01",
            "If so, Tocoton\x01",
            "I suppose you will get involved.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EF7")

    label("loc_E3D")


    ChrTalk(
        0xFE,
        (
            "The smell approaching the battlefield ……\x01",
            "Kuku, a blood as a weapon merchant\x01",
            "I caught hold of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I thought of leaving the crossbell,\x01",
            "If so, Tocoton\x01",
            "I suppose you will get involved.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EF7")

    Jump("loc_26B5")

    label("loc_EFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1582")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14D2")
    OP_4B(0xFE, 0xFF)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(
        0xFE,
        "Oh, the Special Affairs Division?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although it was a raid incident during this time … …\x01",
            "How are you watching?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F……I agree.\x02\x03",
            "#00001FThe part that I still do not understand\x01",
            "Although it is a place like that … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FHowever, it caused the incident\x01",
            "Being \"Red constellation\"\x01",
            "It is an undeniable fact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FThen the employer,\x01",
            "That is, with the imperial government's deposit\x01",
            "It may be natural to think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, already among citizens\x01",
            "It seems that similar rumors are spreading.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Around where the guys quickly withdrew\x01",
            "Although it is indescribable … …\x01",
            "Huh, oh well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FThat's right,\x01",
            "With Wald who turned into a devil in the vicinity\x01",
            "I heard that they met.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, after all too\x01",
            "Did you make a mistake in Wald?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He was made a hard time … …\x01",
            "You seem to have used the strange medicine of the example.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A medicine to become such a monster\x01",
            "I wonder where I got it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108FThat is also the case ….\x02\x03",
            "#10106FThe investigation is continuing,\x01",
            "The route you still get\x01",
            "It is not clear …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ha, you guys like that too.\x01",
            "All I do not understand at all\x01",
            "I am getting sick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, after that incident\x01",
            "Because the security problem of the autonomous province recurred,\x01",
            "It became not to be a business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The long-standing Old Town is also\x01",
            "It has become such a thing ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    ChrTalk(
        0xFE,
        (
            "……gradually,\x01",
            "It might be a time of leaving here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FAshleyさん……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10303F…… Well, it may be useless.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FIf you are\x01",
            "I wonder if there are many shades … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, I have not decided yet.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Jingoのこともあるし、\x01",
            "I have to decide how to shake it.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    OP_4C(0xFE, 0xFF)
    SetScenarioFlags(0x18D, 6)
    Jump("loc_157D")

    label("loc_14D2")


    ChrTalk(
        0xFE,
        (
            "… …. Soon, I will crossbell\x01",
            "It may be a time of departure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All I do not understand\x01",
            "It's a shaku ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Jingoのこともあるし、\x01",
            "I have to decide how to shake it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_157D")

    Jump("loc_26B5")

    label("loc_1582")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1636")

    ChrTalk(
        0xFE,
        (
            "You know, with those noisy guys\x01",
            "If you are going to set up a job,\x01",
            "Take care of yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think that I know,\x01",
            "I am prepared for half-heartedness\x01",
            "It is punchy to be crushed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26B5")

    label("loc_1636")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_16DE")

    ChrTalk(
        0xFE,
        (
            "Since the trade meeting,\x01",
            "Somewhat to crossbell\x01",
            "I'm getting hard to flow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anything on the back and the two major powers regulate\x01",
            "It's a story that I started getting on,\x01",
            "I want you to be cavern.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26B5")

    label("loc_16DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_18D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1823")

    ChrTalk(
        0xFE,
        (
            "By the way yesterday, at an example trade meeting\x01",
            "The remnants of the rampaged \"anti-immigration policyism\"\x01",
            "You seem to have been caught.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the train involving the black moon\x01",
            "It is a story that there was a riot,\x01",
            "I wonder if I could not do it a little more quietly.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_17F0")

    ChrTalk(
        0x101,
        (
            "#00012F（流石はAshleyさん、\x01",
            "Ears are early. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_181B")

    label("loc_17F0")


    ChrTalk(
        0x101,
        "#00005F(Is there such a thing ……)\x02",
    )

    CloseMessageWindow()

    label("loc_181B")

    SetScenarioFlags(0x0, 0)
    Jump("loc_18D1")

    label("loc_1823")


    ChrTalk(
        0xFE,
        (
            "Yesterday, I was rampant at an example trade meeting\x01",
            "The remnants of \"anti-immigration policyism\"\x01",
            "You seem to have been caught.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the train involving the black moon\x01",
            "It is a story that there was a riot,\x01",
            "I wonder if I could not do it a little more quietly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18D1")

    Jump("loc_26B5")

    label("loc_18D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_196D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18F1")
    Call(0, 10)
    Jump("loc_1968")

    label("loc_18F1")


    ChrTalk(
        0xFE,
        (
            "Even so,\x01",
            "Today is something strange and lively.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whew ……\x01",
            "Since when have you been with Gakincho\x01",
            "Have you been hanging out?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1968")

    Jump("loc_26B5")

    label("loc_196D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_197B")
    Jump("loc_26B5")

    label("loc_197B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_19F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1996")
    Call(0, 5)
    Jump("loc_19EE")

    label("loc_1996")


    ChrTalk(
        0xFE,
        (
            "by the way,\x01",
            "Did you move it yourself?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whew ……\x01",
            "I am too old to attend.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19EE")

    Jump("loc_26B5")

    label("loc_19F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1C43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 2)), scpexpr(EXPR_END)), "loc_1BB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B57")

    ChrTalk(
        0xFE,
        (
            "Because there was a noisy person on the store\x01",
            "Blow off from here\x01",
            "I thought of doing it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There are also holes in the roof\x01",
            "Jingoに任せたのさ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FWell, as expected the firing in the city\x01",
            "I can not miss it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Huh, so you probably did not do it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Even then, that blond hair,\x01",
            "It seems like you have seen somewhere … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, it may be due to mind.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BB4")

    label("loc_1B57")


    ChrTalk(
        0xFE,
        (
            "…… Even then, that blond hair,\x01",
            "It seems like you have seen somewhere … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, it may be due to mind.\x02",
    )

    CloseMessageWindow()

    label("loc_1BB4")

    Jump("loc_1C3E")

    label("loc_1BB9")


    ChrTalk(
        0xFE,
        (
            "Each country's VIP\x01",
            "A couple bases, or …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Honestly I can not read what happens,\x01",
            "Just being involved in something\x01",
            "I want to wish for Kamen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C3E")

    Jump("loc_26B5")

    label("loc_1C43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1F18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E6D")
    OP_4B(0xFE, 0xFF)

    ChrTalk(
        0xFE,
        "Oh, it is redheaded.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Apparently to the support department\x01",
            "You seem to have returned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FOh, thanks, sir.\x02\x03",
            "#00306FEven so ……\x01",
            "As usual it is a queen smell store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ha, it was bad.\x01",
            "I am unfortunate I am a small business\x01",
            "I can not afford to care about the upper side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "By the way Anta, in the back street … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Oh, I guess that's OK.\x01",
            "When I thrust my neck poorly,\x01",
            "It only makes me more troubled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F(… …. Ha, this looks like\x01",
            "The relationship between me and \"red constellation\" is also\x01",
            "I guess the examination is going on all the time. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F(To what extent is it?\x01",
            "You probably know … …)\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xFE, 0xFF)
    SetScenarioFlags(0x14D, 4)
    Jump("loc_1F13")

    label("loc_1E6D")


    ChrTalk(
        0xFE,
        (
            "But because of the trade meeting\x01",
            "The police officers who do not usually watch today\x01",
            "It looks like he is on business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whew ……\x01",
            "If you want to come to the shop\x01",
            "It sounds annoying to treat.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F13")

    Jump("loc_26B5")

    label("loc_1F18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2389")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2285")
    OP_4B(0xFE, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Come to think of it …\x01",
            "What's with Tibiko and Redhead?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FChi, Chibiko and redhead …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FAh……\x01",
            "Tio and Randy.\x02\x03",
            "#00003FThe two still have\x01",
            "There was another job left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes, it is\x01",
            "It is likely to be a while later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Indeed, indeed\x01",
            "I do not know who Tibiko is … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The one with red hair is mostly,\x01",
            "Even in the rehabilitation training of the guard\x01",
            "Is it a place to go out?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FHow, why is that … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302FIt is not Date to fluffy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, as I do this business\x01",
            "That sticky point is attached.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "HM………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FAshleyさん？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh … no, nothing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, anyway for work\x01",
            "It is more than anything else if you are giving sacrifice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tentatively, you too\x01",
            "Not to be late for that man\x01",
            "You should at best train at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FWell, yeah.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xFE, 0xFF)
    SetScenarioFlags(0x137, 6)
    Jump("loc_2384")

    label("loc_2285")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_234B")

    ChrTalk(
        0xFE,
        (
            "Oh, no more from me\x01",
            "Even if I try to draw something\x01",
            "It's useless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do not say uncertain things,\x01",
            "There is also Mr. in-law.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, at the very least\x01",
            "Try chasing with your own power.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2384")

    label("loc_234B")


    ChrTalk(
        0xFE,
        (
            "Well, at the very least\x01",
            "Try chasing with your own power.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2384")

    Jump("loc_26B5")

    label("loc_2389")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_26B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2639")
    OP_4B(0xFE, 0xFF)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x0, 500)

    ChrTalk(
        0xFE,
        "Oh, the Special Affairs Division?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although I did not see it for a while\x01",
            "It's been a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009Fmy mother……\x01",
            "long time no see.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 500)

    ChrTalk(
        0xFE,
        (
            "Huh, I heard about rumors\x01",
            "No way that you do not get it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What kind of wind blowing,\x01",
            "Wadi Hemisphere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FWell, there is something I think.\x02\x03",
            "#10302FNext time around Trinity\x01",
            "I'll let you talk to the knob.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Huh, whatever.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So?\x01",
            "Is there something for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it is a release from Rubache\x01",
            "Handling as usual#2RMackerel#I have heard it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F(Did you do such a thing ……)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FNo, especially today.\x01",
            "I'm sorry to disturb you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's right.\x01",
            "Well, properly\x01",
            "You are going to look at the items of the store, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x0, 0x0)
    OP_4C(0xFE, 0xFF)
    SetScenarioFlags(0x137, 5)
    Jump("loc_26B5")

    label("loc_2639")

    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(
        0xFE,
        (
            "But Wadi, you surely\x01",
            "I will enter the Special Affairs Support Division.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now, within close range\x01",
            "Is not it snowing?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x0, 0x0)

    label("loc_26B5")

    TalkEnd(0xFE)
    Return()

    # Function_4_672 end

    def Function_5_26B9(): pass

    label("Function_5_26B9")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    TurnDirection(0x8, 0x9, 0)

    ChrTalk(
        0x8,
        (
            "おう、Jingo。\x01",
            "The grenades brought in yesterday\x01",
            "Do you remember where you went to?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Certainly around here\x01",
            "I suppose I should have put it … …\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 0)

    ChrTalk(
        0x9,
        "Mom, do you remember me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That's where I got in the way\x01",
            "Later that mom himself to the underground warehouse\x01",
            "You guys moved it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "Oh, was that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "サンクス、Jingo。\x01",
            "As much as I should have is my daughter.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F(With the exception of grenades,\x01",
            "It is an ordinary conversation … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F(As usual,\x01",
            "This mother and daughter is out of the standard. )\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2912")
    OP_4C(0x9, 0xFF)

    label("loc_2912")

    OP_4C(0x8, 0xFF)
    OP_93(0x8, 0x87, 0x0)
    OP_93(0x9, 0xE1, 0x0)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    Return()

    # Function_5_26B9 end

    def Function_6_2935(): pass

    label("Function_6_2935")

    Call(0, 7)
    Return()

    # Function_6_2935 end

    def Function_7_2939(): pass

    label("Function_7_2939")

    TalkBegin(0x9)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2950")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BC8")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",                # 0
            "交換する(装備)\x01",          # 1
            "交換する(クオーツ)\x01",      # 2
            "交換する(その他)\x01",        # 3
            "quit\x01",                  # 4
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_29DE")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_29DE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29FE")
    OP_AF(0x8C)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3BC3")

    label("loc_29FE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A1E")
    OP_AF(0x96)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3BC3")

    label("loc_2A1E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ABB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2A6A")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetItemNumber('沐浴阳光的阿尼艾丝14卷', 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AF(0xA3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetItemNumber('沐浴阳光的阿尼艾丝14卷', 0x0)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2A65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2A62")
    ClearScenarioFlags(0x0, 1)

    label("loc_2A62")

    SetScenarioFlags(0x189, 5)

    label("loc_2A65")

    Jump("loc_2AAC")

    label("loc_2A6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2A7A")
    OP_AF(0xA2)
    Jump("loc_2AAC")

    label("loc_2A7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2A8A")
    OP_AF(0xA1)
    Jump("loc_2AAC")

    label("loc_2A8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2A9A")
    OP_AF(0xA1)
    Jump("loc_2AAC")

    label("loc_2A9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2AAA")
    OP_AF(0xA0)
    Jump("loc_2AAC")

    label("loc_2AAA")

    OP_AF(0xA0)

    label("loc_2AAC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3BC3")

    label("loc_2ABB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2ACF")
    Jump("loc_3BC3")

    label("loc_2ACF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BC3")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2F76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 5)), scpexpr(EXPR_END)), "loc_2C9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C30")

    ChrTalk(
        0x9,
        (
            "Oh……\x01",
            "After all the Kagemalg Goods\x01",
            "I'm innocent with Iki!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, there was Katana in the warehouse.\x01",
            "If you do have that, it's pat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "VanとRuzeにもこれ着せて、\x01",
            "Chamber of Love.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FThis, the category of children's play\x01",
            "Because it exceeds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FKagemalu's character also\x01",
            "It is delicately curved and transmitted.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C98")

    label("loc_2C30")


    ChrTalk(
        0x9,
        (
            "After all the Kagemalg Goods\x01",
            "I'm innocent with Iki!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "VanとRuzeにもこれ着せて、\x01",
            "Chamber of Love.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C98")

    Jump("loc_2F71")

    label("loc_2C9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D88")

    ChrTalk(
        0x9,
        "Do you know cats, or macaques?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FMeguro cat … ….?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FDid you mean …\x01",
            "Is it about \"Kagemal\"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "That.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Jingo、それのフク探してんだ。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "It is perfect to collect a lot.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x189, 6)
    Jump("loc_2F71")

    label("loc_2D88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EE2")

    ChrTalk(
        0x9,
        "Customer, did not you see that tree?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's awesome.\x01",
            "Even though I am tearing apricate tree,\x01",
            "How many gates are there?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00006F(I'm really thrilled … …)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106F(As usual noisy child … …)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2F71")

    label("loc_2EE2")


    ChrTalk(
        0x9,
        (
            "By that, I will end the tree,\x01",
            "How many gates are there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Nishishi …\x01",
            "Even though there are many tanks of empire\x01",
            "It might be Muzukashi.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F71")

    Jump("loc_3BC3")

    label("loc_2F76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3117")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30D3")

    ChrTalk(
        0x9,
        "Oh, the customer?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Outside it sounds like adzuki.\x01",
            "Please buy something for your protection.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you kick out the endless Yoroi out of town,\x01",
            "I wonder if I burst grenades.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00006F(I guess it is probably not for protecting … …)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3112")

    label("loc_30D3")


    ChrTalk(
        0x9,
        (
            "Outside it sounds like adzuki.\x01",
            "Please buy something for your protection.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3112")

    Jump("loc_3BC3")

    label("loc_3117")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3189")

    ChrTalk(
        0x9,
        (
            "Consult with Mama, Cross Bell\x01",
            "It will be left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Customers, something\x01",
            "If you want a monkey you want, say it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BC3")

    label("loc_3189")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_321C")

    ChrTalk(
        0x9,
        (
            "As usual, everyone\x01",
            "I guess I am busy with reconstruction work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I will make it for honor but,\x01",
            "ママとJingoもちょこちょこ\x01",
            "You are helping.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BC3")

    label("loc_321C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3384")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3317")

    ChrTalk(
        0x9,
        "Fuwa - Ah, Nemenem ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yesterday evening a sudden job entered,\x01",
            "I was scratching moms and warehouses\x01",
            "It's been a while since sleeping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "But, Mama also ordered such a sudden order,\x01",
            "I took over well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That customer,\x01",
            "Was I such a friend with Mama?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_337F")

    label("loc_3317")


    ChrTalk(
        0x9,
        (
            "But, Mama also ordered such a sudden order,\x01",
            "I took over well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That customer,\x01",
            "Was I such a friend with Mama?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_337F")

    Jump("loc_3BC3")

    label("loc_3384")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3408")

    ChrTalk(
        0x9,
        "Mum, I do not think so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If it does not matter any more, more\x01",
            "Those who have fallen away\x01",
            "I'm feeling refreshed though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BC3")

    label("loc_3408")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3486")
    OP_93(0x9, 0x10E, 0x0)

    ChrTalk(
        0x9,
        "But they are not disciplined.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Before I saw my mother's tension,\x01",
            "You forgot to completely forget it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BC3")

    label("loc_3486")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3501")

    ChrTalk(
        0x9,
        (
            "Yo, customers.\x01",
            "These things are\x01",
            "I do not have to worry about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Because there are nice spots today,\x01",
            "Please exchange.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BC3")

    label("loc_3501")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_35EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35A6")

    ChrTalk(
        0x9,
        "I'm going for a drink if it is mama.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Today I will inventory inventory from the morning\x01",
            "Because I was busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "A little for a reward\x01",
            "It's getting hooked.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_35E7")

    label("loc_35A6")


    ChrTalk(
        0x9,
        (
            "Mom, it is tough for customers of the shop,\x01",
            "I'm sweet tootto tonight for myself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35E7")

    Jump("loc_3BC3")

    label("loc_35EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_366C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3607")
    Call(0, 5)
    Jump("loc_3667")

    label("loc_3607")

    TurnDirection(0x9, 0x0, 0)

    ChrTalk(
        0x9,
        "Mom, I forgot sometime.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Nishishi …\x01",
            "やっぱ、Jingoがいねえとダメだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3667")

    Jump("loc_3BC3")

    label("loc_366C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_37C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 2)), scpexpr(EXPR_END)), "loc_36F4")

    ChrTalk(
        0x9,
        (
            "Those kimpetsu,\x01",
            "I fell from the roof\x01",
            "I was fine with Wari.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "A little more strongly\x01",
            "I wish I should have kicked it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37C3")

    label("loc_36F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3781")

    ChrTalk(
        0x9,
        (
            "In the morning it was rare to shut down the store,\x01",
            "I have seen the unveiling ceremony with Mom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That building,\x01",
            "I'm really stupid.\x01",
            "Jingoもビックリしたぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_37C3")

    label("loc_3781")


    ChrTalk(
        0x9,
        (
            "That building,\x01",
            "I'm really stupid.\x01",
            "Jingoもビックリしたぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37C3")

    Jump("loc_3BC3")

    label("loc_37C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_390C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3899")

    ChrTalk(
        0x9,
        (
            "New sister no-chan\x01",
            "I came from reading this book, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If I told you not to go like usual,\x01",
            "Even homework put another book.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Somehow I can not care less … -.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3907")

    label("loc_3899")


    ChrTalk(
        0x9,
        (
            "That sister no-chan,\x01",
            "Somehow I can not care less … -.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, I have a lot of trouble ……\x01",
            "I read this book.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3907")

    Jump("loc_3BC3")

    label("loc_390C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3B06")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3927")
    Call(0, 8)
    Jump("loc_3B01")

    label("loc_3927")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A95")

    ChrTalk(
        0x9,
        (
            "Rainy Yarrow, Hairstyle Gimmering\x01",
            "Untitled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Shoot a conductive cannon\x01",
            "I wonder if it will clear if the rain clouds are evaporated?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FLet me see……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F(Yup,\x01",
            "What is this child … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F(Yeah … a little\x01",
            "There is no way to tsukkomi. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3B01")

    label("loc_3A95")


    ChrTalk(
        0x9,
        (
            "Rainy Yarrow, Hairstyle Gimmering\x01",
            "Untitled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "With a guiding bomb\x01",
            "I wonder if I will blow up the rain clouds?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B01")

    Jump("loc_3BC3")

    label("loc_3B06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3BC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B21")
    Call(0, 8)
    Jump("loc_3BC3")

    label("loc_3B21")


    ChrTalk(
        0x9,
        (
            "I think that I know,\x01",
            "What can you do with customers?\x01",
            "Just swapping exchange.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Accessories to quartz for medicine ……\x01",
            "I also have other items available in the text\x01",
            "Watch it if you like.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BC3")

    Jump("loc_2950")

    label("loc_3BC8")

    TalkEnd(0x9)
    Return()

    # Function_7_2939 end

    def Function_8_3BCC(): pass

    label("Function_8_3BCC")


    ChrTalk(
        0x9,
        "Oh, customers, it's been a long time ago.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Buki is not selling, but,\x01",
            "Should I exchange something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Before the stuff for Ippan\x01",
            "I do not have enough.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C82")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_3C82")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3CA8")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_3CA8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3CCE")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_3CCE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3CF4")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_3CF4")

    Sleep(1000)

    ChrTalk(
        0x101,
        "#00006FOh, it is still a noisy remark.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FUm, I really wanted this shop\x01",
            "Is it okay to use it …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FWell, well, the items on the table are\x01",
            "It looks like it's not illegal … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHuff, to some extent\x01",
            "Is not there a problem?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Oh, later.\x01",
            "Recently I've been doing extensive things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's like an egg-on-goby sauce\x01",
            "Would you like me to bring it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "As it is\x01",
            "I will exchange it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FI knew.\x01",
            "I will let you use it again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x137, 7)
    Return()

    # Function_8_3BCC end

    def Function_9_3EBF(): pass

    label("Function_9_3EBF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3ED4")
    Call(0, 10)
    Jump("loc_3F0B")

    label("loc_3ED4")


    ChrTalk(
        0xFE,
        (
            "Ju, 100 thousand mirrors ……\x01",
            "I have never seen such a thing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F0B")

    TalkEnd(0xFE)
    Return()

    # Function_9_3EBF end

    def Function_10_3F0F(): pass

    label("Function_10_3F0F")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0x8,
        (
            "Oh, what you are talking about\x01",
            "That's about Enigma.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Huh, put it like this in my ears\x01",
            "It will be a quick change to a communication device.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Well, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well, police and fighter ……\x01",
            "You used it even after that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "ちなみにAshleyさん。\x01",
            "If I buy it properly\x01",
            "How long is it to be a monkey?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm? Well basics\x01",
            "It's made to order.\x01",
            "Is there a minimum of 100,000 mirrors?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If it is a wake-onary item in our place\x01",
            "A little flexible, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Perhaps,\x01",
            "Do you want guys?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Ju, 100,000 ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Yes, 1 million chocolates 100,000 pieces …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hahaha, you guys\x01",
            "I guess it's quite a nice reaction.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x16E, 5)
    Return()

    # Function_10_3F0F end

    def Function_11_417D(): pass

    label("Function_11_417D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4192")
    Call(0, 10)
    Jump("loc_41D1")

    label("loc_4192")


    ChrTalk(
        0xFE,
        (
            "1 Mirachocho 100 thousand pieces …\x01",
            "Jun, how much is 100,000 pieces?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41D1")

    TalkEnd(0xFE)
    Return()

    # Function_11_417D end

    def Function_12_41D5(): pass

    label("Function_12_41D5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4235")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41F3")
    Call(0, 14)
    Jump("loc_4230")

    label("loc_41F3")


    ChrTalk(
        0xFE,
        (
            "くっそー、Jingoの母ちゃん、\x01",
            "As usual I'm okay.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4230")

    Jump("loc_4241")

    label("loc_4235")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4241")
    Call(0, 15)

    label("loc_4241")

    TalkEnd(0xFE)
    Return()

    # Function_12_41D5 end

    def Function_13_4245(): pass

    label("Function_13_4245")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4291")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4263")
    Call(0, 14)
    Jump("loc_428C")

    label("loc_4263")


    ChrTalk(
        0xFE,
        (
            "Couscous……\x01",
            "It's also a strategy shoot.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_428C")

    Jump("loc_429D")

    label("loc_4291")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_429D")
    Call(0, 15)

    label("loc_429D")

    TalkEnd(0xFE)
    Return()

    # Function_13_4245 end

    def Function_14_42A1(): pass

    label("Function_14_42A1")

    OP_4B(0x8, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xC,
        (
            "Wow, this is a conductive gun.\x01",
            "It is cool.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "ねえねえ、Van。\x01",
            "I wonder if I can bake Niku?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well, is not it a casual win?\x01",
            "Hee hee, try this secretly next time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "…… Hey, gokincho.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xC, 0)

    ChrTalk(
        0x8,
        (
            "That monkey,\x01",
            "Do not touch it on your own. (Guilli)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Oh, oh ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Couscous……\x01",
            "Jingoちゃんのお母さん、\x01",
            "You have power.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    OP_93(0x8, 0x0, 0x0)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x10)
    OP_4C(0x8, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_14_42A1 end

    def Function_15_441D(): pass

    label("Function_15_441D")

    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_452C")

    ChrTalk(
        0xC,
        (
            "よお、Jingo。\x01",
            "I came to see you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Please kindly bless me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Oh, my godfather.\x01",
            "Mira 's are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hiakha, I had it\x01",
            "I used it yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Couscous……\x01",
            "I ate a lot, Niku.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Haa, as usual\x01",
            "There is no planning ability, sorry.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_45B5")

    label("loc_452C")


    ChrTalk(
        0xC,
        (
            "Gothak is good.\x01",
            "恵んでくれよ、Jingo。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "What? I'm sorry but\x01",
            "Do not expect it to be healthy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Couscous……\x01",
            "Jingoちゃんのオニー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45B5")

    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_15_441D end

    def Function_16_45C2(): pass

    label("Function_16_45C2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x10000000)
    OP_68(0, 1100, 12800, 0)
    MoveCamera(50, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, -600, 0, 1800, 0)
    SetChrPos(0x102, 600, 0, 1800, 0)
    SetChrPos(0x109, 900, 0, 700, 0)
    SetChrPos(0x105, -900, 0, 700, 0)
    OP_68(0, 1100, 2800, 6000)
    MoveCamera(45, 19, 0, 6000)
    SetCameraDistance(18500, 6000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#12P#00001FWell, as usual\x01",
            "I guess it's a suspicious store ……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#6P#00108F相変わらずJingoちゃんが\x01",
            "You are doing a store number ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10103FThere are several in the crossbell city\x01",
            "It is one of the dark brokers.\x02\x03",
            "#10101FWe are dealing with weapons ammunition\x01",
            "I have been rumored by the guard, but … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FWell, in those stores\x01",
            "I am still conscientious.\x02\x03",
            "#10300FMy husband is a pretty girls guy.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_47E5():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_47E5)
    Sleep(50)

    def lambda_47F5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_47F5)
    Sleep(50)
    TurnDirection(0x102, 0x105, 500)

    ChrTalk(
        0x101,
        (
            "#5P#00003FI see that …\x02\x03",
            "#00001FAnyway, if you have a business\x01",
            "Will you do it quickly?\x02",
        )
    )

    CloseMessageWindow()
    Sound(814, 0, 100, 0)
    SetChrName("")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※ At the exchange shop \"Ninevali\"\x01",
            "Instead of consuming certain items\x01",
            "Items with high scarcity value are available.\x02\x03",
            "※カウンターにいるJingoに話しかけて\x01",
            "If you select \"Replace\"\x01",
            "A menu is displayed and you can exchange.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 0, 0, 1000, 0)
    SetScenarioFlags(0x138, 4)
    EventEnd(0x5)
    Return()

    # Function_16_45C2 end

    def Function_17_4985(): pass

    label("Function_17_4985")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x10000000)
    SetChrPos(0x101, -600, 0, 1800, 0)
    SetChrPos(0x102, 600, 0, 1800, 0)
    SetChrPos(0x109, 900, 0, 700, 0)
    SetChrPos(0x105, -900, 0, 700, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x138, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D3F")
    OP_68(0, 1100, 12800, 0)
    MoveCamera(50, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    OP_68(0, 1100, 2800, 6000)
    MoveCamera(45, 19, 0, 6000)
    SetCameraDistance(18500, 6000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#12P#00001FWell, as usual\x01",
            "I guess it's a suspicious store ……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#6P#00108F相変わらずJingoちゃんが\x01",
            "You are doing a store number ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10103FThere are several in the crossbell city\x01",
            "It is one of the dark brokers.\x02\x03",
            "#10101FWe are dealing with weapons ammunition\x01",
            "I have been rumored by the guard, but … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FWell, in those stores\x01",
            "I am still conscientious.\x02\x03",
            "#10300FMy husband is a pretty girls guy.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4BB2():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4BB2)
    Sleep(50)

    def lambda_4BC2():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4BC2)
    Sleep(50)
    TurnDirection(0x102, 0x105, 500)

    ChrTalk(
        0x101,
        (
            "#5P#00003FI see that …\x02\x03",
            "#00001FとにかくAshleyさんに\x01",
            "Let's ask about the example man.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(814, 0, 100, 0)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※ At the exchange shop \"Ninevali\"\x01",
            "Instead of consuming certain items\x01",
            "Items with high scarcity value are available.\x02\x03",
            "※カウンターにいるJingoに話しかけて\x01",
            "If you select \"Replace\"\x01",
            "A menu is displayed and you can exchange.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_4E46")

    label("loc_4D3F")

    OP_68(0, 1100, 2800, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#12P#00006FWell, after all\x01",
            "I guess it's a suspicious store ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00106FWell, no matter how many times you come\x01",
            "I do not get used to it ……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#11P#00101Fとりあえず、Ashleyさんに\x01",
            "Let's ask about the example man.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()

    label("loc_4E46")

    SetChrPos(0x0, 0, 0, 1000, 0)
    SetScenarioFlags(0x138, 5)
    SetScenarioFlags(0x128, 3)
    EventEnd(0x5)
    Return()

    # Function_17_4985 end

    def Function_18_4E60(): pass

    label("Function_18_4E60")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    Fade(500)
    OP_68(-2860, 1000, 12800, 0)
    MoveCamera(37, 22, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, -3100, 20, 11800, 0)
    SetChrPos(0x102, -4400, 20, 11000, 45)
    SetChrPos(0x109, -2900, 20, 10800, 0)
    SetChrPos(0x105, -1700, 20, 12000, 315)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x8, 0xB4, 0x1F4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5188")

    ChrTalk(
        0x8,
        "#5POh, the Special Affairs Division?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAlthough I did not see it for a while\x01",
            "It's been a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012Fmy mother……\x01",
            "long time no see.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#5PHuh, I heard about rumors\x01",
            "No way that you do not get it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWhat kind of wind blowing,\x01",
            "Wadi Hemisphere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FWell, there is something I think.\x02\x03",
            "#10302FNext time around Trinity\x01",
            "I'll let you talk to the knob.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PHuh, whatever.\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#5PSo?\x01",
            "Is there something for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIf it is a release from Rubache\x01",
            "Handling as usual#2RMackerel#I have heard it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00006F(Did you do such a thing ……)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103F実は、Ashleyさんに\x01",
            "I have something to ask.\x02\x03",
            "#00100FTo you as a former weapon merchant.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x137, 5)
    Jump("loc_5228")

    label("loc_5188")


    ChrTalk(
        0x8,
        "#5PIs it a Special Affairs Division?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PIs there something for me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103Fはい、実はAshleyさんに\x01",
            "I have something to ask.\x02\x03",
            "#00100FTo you as a former weapon merchant.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5228")

    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#5PHmm, what is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PTsao in earnest\x01",
            "About the matter that started moving?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FDo you know as expected?\x02\x03",
            "#00001FPerhaps, with that\x01",
            "I think that it is another matter … …\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_64(0x8)

    ChrTalk(
        0x8,
        "#5PEye#4RCough#…… Redhead's Fortune#6RBad luck#Or\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FHave you accepted it?\x02\x03",
            "A man belonging to a back society\x01",
            "I do not think he will make a mistake ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIf it was a target\x01",
            "I have some idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PBut in this situation now\x01",
            "If it comes to the crossbell … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P…………………………………….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00108FLet me see……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305FOh, so much\x01",
            "Do you recognize it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PWell then …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PJust my imagination\x01",
            "If it was the worst case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIt is the opponent who can bear the hands of you\x01",
            "I guess there is no mistake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00101FTo that extent ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10101FOr, are you still a hunter?\x01",
            "Is it per terrorist?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PHuh, well then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIf that man,\x01",
            "Once, I also have a relationship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PI will not go talking.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10107FBut, it is …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FAnyhow, as a hunter\x01",
            "If it is a terrorist it can not be neglected.\x02\x03",
            "#00003FAlthough it is a crossbell,\x01",
            "There are laws to punish terrorist acts.\x02\x03",
            "#00013FEven with minimal information alone\x01",
            "Would you like to be taught?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00108FLloyd …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PHehe, not bad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P── Were you brother of Guy?\x01",
            "You started to have good eyes.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00005FAshleyさん、\x01",
            "My older brother and acquaintance …! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PNow also around Dudley\x01",
            "Sometimes I show my face ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PBack then, to the old city kun\x01",
            "A rigorous investigator who is carrying legs\x01",
            "It was about a guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PI lost an interesting man.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00008F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PExcept that idiot\x01",
            "I will answer this only.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PMy worst sort of idea is\x01",
            "It is not a terrorist.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHowever, it seems like a cannibal tiger\x01",
            "It is a dangerous man though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10108FHin eating tiger ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306FWhew ……\x01",
            "Is not it the worst partner?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWell, whether that man or not\x01",
            "It was not decided yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThe man that you saw was\x01",
            "I wonder who was alone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PUsually, if you are a subordinate\x01",
            "I suppose I should accompany it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FWell, is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00101FAnd then …\x01",
            "Is it still a military official?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PHuh, this far.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PMore than this is our power\x01",
            "You have to go close.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00006F……I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00104FThank you for the information.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_93(0x8, 0x0, 0x0)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, -2860, 20, 11750, 180)
    SetScenarioFlags(0x128, 4)
    OP_1B(0x0, 0x0, 0x13)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_18_4E60 end

    def Function_19_5B79(): pass

    label("Function_19_5B79")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(300, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    SetChrFlags(0x0, 0x8)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    OP_68(0, 1200, 500, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20000, 0)
    Sleep(500)
    OP_68(5100, 1200, 8100, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_93(0x9, 0xB4, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x9,
        "#5PMum, I do not think so.\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x13B, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#11PThat's right Mom, the stuff that came yesterday,\x01",
            "Do not unwind the load?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x87, 0x0)

    ChrTalk(
        0x8,
        (
            "Oh, this weather is OK.\x01",
            "There is no hurry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "……それよりJingo。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When you got out into town yesterday,\x01",
            "Did not you see a strange person?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PHen you?\x01",
            "There were lots of such things?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWakaba of vacation look or something\x01",
            "I bought a lot of bread\x01",
            "Sister Nyu-chan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PThat wadi is too stupid.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "If so, I do not mind.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_68(-2860, 1200, 13750, 3500)
    MoveCamera(15, 26, 0, 3500)
    OP_6F(0x79)
    OP_64(0x8)
    Sleep(500)

    ChrTalk(
        0x8,
        "#5P(…, well, are you worrying too much?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P(If I thought that he came\x01",
            "I guess I have my daughter as well. )\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    ClearChrFlags(0x0, 0x8)
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    SetScenarioFlags(0x22, 0)
    NewScene("c1400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_19_5B79 end

    def Function_20_5EAB(): pass

    label("Function_20_5EAB")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    Fade(500)
    OP_68(-2860, 1000, 12800, 0)
    MoveCamera(37, 22, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, -3100, 20, 11800, 0)
    SetChrPos(0x102, -4400, 20, 11000, 45)
    SetChrPos(0x103, -3700, 20, 10500, 0)
    SetChrPos(0x109, -2600, 20, 10800, 0)
    SetChrPos(0x105, -1900, 20, 12000, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x8, 0xB4, 0x1F4)

    ChrTalk(
        0x8,
        "#5PGee\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P… … As expected,\x01",
            "Have you arrived quickly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FThat means …\x01",
            "Would you like Randy here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5POh, I got in touch with you last night.\x01",
            "I got a spot early in the morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWhen you come in\x01",
            "I was asked to cut the sashimi\x01",
            "I do not have obligation to that extent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10309FAhaha, indeed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00101FSo then … Randy\x01",
            "What did you order?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00201FIs it still a driving-type rifle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PNo, such a true\x01",
            "It was not a shimmer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PBurst bullets and armor riders,\x01",
            "Not to mention grenades,\x01",
            "Up to old-style ammunition with explosive … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PStocks that were in store\x01",
            "I bought it for washing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAnd it was flowing in the darkness\x01",
            "It is unregistered \"Enigma 嘦\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FI see……\x02\x03",
            "#00008F… … It's truly amply prepared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00206FYeah …… With no enrolled enigma\x01",
            "I also do not know the number.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FBut the body of the heavy weapon#4R噵 噵#Is\x01",
            "Did not you purchase it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5POh, my stuff is as powerful as it is\x01",
            "A power formula · pyrotechnic rifle\x01",
            "I intended to handle it … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PTo the next president of \"red constellation\"\x01",
            "You seem to have not liked it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00011FAshleyさん……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00106FDid you know ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHa, obviously.\x01",
            "Because Kocota information is a life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PApparently let the old nest blow a foam\x01",
            "I suppose I intended to … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P\"Red war demon#8ROgre Rosso#\"When\x01",
            "Blooded#8RBladder#Speaking of \"Charlie\"\x01",
            "It is genuine creatures.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYou're like an odd former hunter\x01",
            "It will definitely return.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00201F…… I will not let it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00013FTo prevent it\x01",
            "We are going to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHuff, from a little while ago\x01",
            "It is always in this condition.\x02\x03",
            "#10302FIt seems like waste even if provoking?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PWhew, it seems so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWell, that young creature fights\x01",
            "I have not heard of that, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PEven if the number of customers is reduced, it is boring.\x01",
            "You will at best help him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10101FYes……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00103FThank you for the information.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_93(0x8, 0x0, 0x0)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, -2860, 20, 11750, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x165, 6)
    OP_29(0xAA, 0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_20_5EAB end

    def Function_21_6738(): pass

    label("Function_21_6738")

    EventBegin(0x1)
    OP_4B(0x9, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_67F8")

    ChrTalk(
        0x9,
        "Are you planning to enter the warehouse?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hmm……\x01",
            "Well, as long as you are a customer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Do not bother me.\x01",
            "I do not know if I die.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F…… O, Thank you very much.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x189, 7)
    ModifyEventFlags(0, 0, 0x80)
    Jump("loc_6901")

    label("loc_67F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6891")

    ChrTalk(
        0x9,
        (
            "…… Hey, customer.\x01",
            "Jingoの目はごまかせねえかんな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "There is an underground warehouse,\x01",
            "It is not a campaign except for going out.\x01",
            "If you are shopping, do it here!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6901")

    label("loc_6891")


    ChrTalk(
        0x9,
        (
            "Hey, customers?\x01",
            "Jingoのハナシ聞いてたか？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The underground warehouse is getting stuck! It is!\x01",
            "If you are shopping, do it here! It is!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6901")

    Sleep(50)
    SetChrPos(0x0, 9940, 0, 11910, 180)
    OP_4C(0x9, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_21_6738 end

    SaveToFile()

Try(main)
