from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t3510.bin",                # FileName
        "t3510",                    # MapName
        "t3510",                    # Location
        0x005C,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\x01',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 92, 0, 2, 0, 3],
    )

    BuildStringList((
        "t3510",                  # 0
        "Receptionist Marcana",   # 1
        "Receptionist Thomas",    # 2
        "Ricardo",                # 3
        "Tourist",                # 4
        "Tourist",                # 5
        "Tourist",                # 6
        "Citizen",                # 7
        "Citizen",                # 8
        "Boy",                    # 9
        "Freight Employee Aaron", # 10
        "Billy",                  # 11
        "Female Officer",         # 12
        "Airship",                # 13
        "Policeman",              # 14
        "Policeman",              # 15
        "Grace",                  # 16
        "Reins",                  # 17
        "Reporter Noticia",       # 18
        "Reporter",               # 19
        "Reporter",               # 20
        "Reporter",               # 21
        "Reporter",               # 22
    ))

    AddCharChip((
        "chr/ch10500.itc",                   # 00
        "chr/ch23600.itc",                   # 01
        "chr/ch26000.itc",                   # 02
        "chr/ch28200.itc",                   # 03
        "chr/ch28100.itc",                   # 04
        "chr/ch22000.itc",                   # 05
        "chr/ch22100.itc",                   # 06
        "chr/ch21800.itc",                   # 07
        "chr/ch20200.itc",                   # 08
        "chr/ch20302.itc",                   # 09
        "chr/ch34202.itc",                   # 0A
    ))

    DeclNpc(4294957076, 150,     2849,    90,   261,  0x0, 0,   3,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(4294958946, 150,     6730,    135,  261,  0x0, 0,   4,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(6679,    0,       5530,    180,  261,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(4294955996, 5000,    4760,    270,  389,  0x0, 0,   5,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(4294956567, 5000,    5769,    225,  389,  0x0, 0,   6,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(4294966257, 5000,    13960,   315,  389,  0x0, 0,   7,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(4294961617, 0,       4294964757, 225,  389,  0x0, 0,   8,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(4294956977, 5199,    8109,    45,   389,  0x0, 0,   9,   0,   255, 255, 0,   15,  255,  0)
    DeclNpc(4294958427, 5199,    10039,   225,  389,  0x0, 0,   10,  0,   255, 255, 0,   16,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 18,  0.25999999046325684,   7.989999771118164,     0.0,                   36.0,                  [0.1666666716337204,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    0.0,                   -0.04333333298563957,  -3.994999885559082,    -0.0,                  1.0])

    DeclActor(4294958606, 0,       2530,    1000,    4294957076, 1600,    2850,    0x007E, 0,  7,  0x0000)
    DeclActor(4294960086, 0,       5680,    1000,    4294958946, 1600,    6730,    0x007E, 0,  9,  0x0000)
    DeclActor(4294959706, 0,       4294964856, 1200,    4294959706, 1500,    4294964856, 0x007C, 0,  17, 0x0000)

    ChipFrameInfo(1136, 0)                                       # 0

    ScpFunction((
        "Function_0_470",          # 00, 0
        "Function_1_520",          # 01, 1
        "Function_2_56D",          # 02, 2
        "Function_3_6EA",          # 03, 3
        "Function_4_75D",          # 04, 4
        "Function_5_B13",          # 05, 5
        "Function_6_BD7",          # 06, 6
        "Function_7_11FE",         # 07, 7
        "Function_8_1202",         # 08, 8
        "Function_9_17CB",         # 09, 9
        "Function_10_17CF",        # 0A, 10
        "Function_11_1E2B",        # 0B, 11
        "Function_12_1E9F",        # 0C, 12
        "Function_13_1F4F",        # 0D, 13
        "Function_14_2016",        # 0E, 14
        "Function_15_20DC",        # 0F, 15
        "Function_16_217B",        # 10, 16
        "Function_17_21F7",        # 11, 17
        "Function_18_22DD",        # 12, 18
        "Function_19_245A",        # 13, 19
        "Function_20_2640",        # 14, 20
        "Function_21_26F9",        # 15, 21
        "Function_22_3114",        # 16, 22
        "Function_23_3366",        # 17, 23
        "Function_24_34BF",        # 18, 24
        "Function_25_35CB",        # 19, 25
        "Function_26_40DD",        # 1A, 26
        "Function_27_4666",        # 1B, 27
        "Function_28_4F60",        # 1C, 28
        "Function_29_50F7",        # 1D, 29
        "Function_30_524A",        # 1E, 30
    ))


    def Function_0_470(): pass

    label("Function_0_470")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_4A8"),
        (1, "loc_4B4"),
        (2, "loc_4C0"),
        (3, "loc_4CC"),
        (4, "loc_4D8"),
        (5, "loc_4E4"),
        (6, "loc_4F0"),
        (SWITCH_DEFAULT, "loc_4FC"),
    )


    label("loc_4A8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_508")

    label("loc_4B4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_508")

    label("loc_4C0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_508")

    label("loc_4CC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_508")

    label("loc_4D8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_508")

    label("loc_4E4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_508")

    label("loc_4F0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_508")

    label("loc_4FC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_508")

    label("loc_508")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_51F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_508")

    label("loc_51F")

    Return()

    # Function_0_470 end

    def Function_1_520(): pass

    label("Function_1_520")

    SetMapObjFlags(0x0, 0x2000000)
    SetMapObjFlags(0x2, 0x2000000)
    SetMapObjFlags(0x5, 0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_546")
    ClearMapObjFlags(0x5, 0x2000000)
    Jump("loc_555")

    label("loc_546")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_555")
    ClearMapObjFlags(0x5, 0x2000000)

    label("loc_555")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56C")
    ClearMapObjFlags(0x0, 0x2000000)

    label("loc_56C")

    Return()

    # Function_1_520 end

    def Function_2_56D(): pass

    label("Function_2_56D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_594")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 6600, 0, -3500, 180)

    label("loc_594")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5D5")
    SetChrPos(0x8, 0, 0, -5500, 90)
    SetChrPos(0x9, 1500, 0, -5500, 270)
    SetChrPos(0xA, 340, 0, 6490, 180)
    Jump("loc_6A7")

    label("loc_5D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5E3")
    Jump("loc_6A7")

    label("loc_5E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5F1")
    Jump("loc_6A7")

    label("loc_5F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_66E")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0xF, 0x9)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    SetChrChipByIndex(0x10, 0xA)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_669")
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 5480, 0, 5530, 90)
    TurnDirection(0xA, 0x12, 0)

    label("loc_669")

    Jump("loc_6A7")

    label("loc_66E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_67C")
    Jump("loc_6A7")

    label("loc_67C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_69E")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xB, 0x10)
    Jump("loc_6A7")

    label("loc_69E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6A7")

    label("loc_6A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_6BE")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 4)
    Event(0, 19)
    Jump("loc_6E9")

    label("loc_6BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_6D5")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x0, 4)
    Event(0, 21)
    Jump("loc_6E9")

    label("loc_6D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_6E9")
    ClearScenarioFlags(0x22, 2)
    SetMapFlags(0x10000000)
    Event(0, 26)

    label("loc_6E9")

    Return()

    # Function_2_56D end

    def Function_3_6EA(): pass

    label("Function_3_6EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_6FE")
    OP_24(0x86)
    ClearScenarioFlags(0x0, 4)
    Jump("loc_71A")

    label("loc_6FE")

    SoundDistance(0x86, 0x16D0, 0x0, 0x259E, 0x1388, 0x30D40, 0x64, 0x0)

    label("loc_71A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_72B")
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)

    label("loc_72B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_745")
    ModifyEventFlags(0, 0, 0x80)
    ClearMapObjFlags(0x3, 0x10)
    ClearMapObjFlags(0x4, 0x10)

    label("loc_745")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_75C")
    ClearMapObjFlags(0x0, 0x4)

    label("loc_75C")

    Return()

    # Function_3_6EA end

    def Function_4_75D(): pass

    label("Function_4_75D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x175, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_795")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x175, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_791")
    Call(0, 22)
    Return()

    label("loc_791")

    Call(0, 23)
    Return()

    label("loc_795")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_92E")

    ChrTalk(
        0xFE,
        (
            "Visit the places the packages\x01",
            "were mistakenly sent and exchange\x01",
            "them for the correct ones.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It'll be alright if you go first to Mainz,\x01",
            "then St. Ursula Hospital and finally to\x01",
            "the Residential Street private house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As for that private house address,\x01",
            "it's written on the slip, so\x01",
            "double-check it when you get there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sorry for the bother.\x01",
            "I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_9DC")

    label("loc_92E")


    ChrTalk(
        0xFE,
        (
            "It'll be alright if you go first to Mainz,\x01",
            "then St. Ursula Hospital and finally to\x01",
            "the Residential Street private house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sorry for the bother.\x01",
            "I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9DC")

    Jump("loc_B0F")

    label("loc_9E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A9D")

    ChrTalk(
        0xFE,
        (
            "Thank you for your hard\x01",
            "work. You were a big\x01",
            "help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, then I've got to\x01",
            "report to the boss...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I mean, to the president,\x01",
            "that everything ended all\x01",
            "right.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_B0F")

    label("loc_A9D")


    ChrTalk(
        0xFE,
        (
            "Thank you for your hard\x01",
            "work. You were a big\x01",
            "help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We'll be counting on you\x01",
            "if we need your help\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B0F")

    TalkEnd(0xFE)
    Return()

    # Function_4_75D end

    def Function_5_B13(): pass

    label("Function_5_B13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 6)), scpexpr(EXPR_END)), "loc_B52")
    Call(0, 28)
    Jump("loc_B55")

    label("loc_B52")

    Call(0, 27)

    label("loc_B55")

    Return()

    label("loc_B56")

    TalkBegin(0x12)

    ChrTalk(
        0xFE,
        (
            "Stealing medical goods in\x01",
            "Crossbell at a time like\x01",
            "this... Totally unforgivable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Guys, catch that thief\x01",
            "for me!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x12)
    Return()

    # Function_5_B13 end

    def Function_6_BD7(): pass

    label("Function_6_BD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 6)), scpexpr(EXPR_END)), "loc_C16")
    Call(0, 28)
    Jump("loc_C19")

    label("loc_C16")

    Call(0, 27)

    label("loc_C19")

    Return()

    label("loc_C1A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_CD2")

    ChrTalk(
        0xA,
        (
            "The police came just moments ago. It seems\x01",
            "they're searching for clues regarding the\x01",
            "jaegers at the landing field.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm sorry, but please\x01",
            "don't go past here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11FA")

    label("loc_CD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_CE0")
    Jump("loc_11FA")

    label("loc_CE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_CEE")
    Jump("loc_11FA")

    label("loc_CEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_10AC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_EAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E02")

    ChrTalk(
        0xFE,
        (
            "You've safely recovered\x01",
            "the medical supplies for\x01",
            "us, haven't you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Earlier, St. Ursula called and\x01",
            "said they received the packages.\x01",
            "I could finally relax.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I must be more careful\x01",
            "to make sure nothing\x01",
            "like that happens again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_EA8")

    label("loc_E02")


    ChrTalk(
        0xFE,
        (
            "Earlier, St. Ursula called and\x01",
            "said they received the packages.\x01",
            "I could finally relax.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I must be more careful\x01",
            "to make sure nothing\x01",
            "like that happens again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EA8")

    Jump("loc_10A7")

    label("loc_EAD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_1022")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FA2")

    ChrTalk(
        0xFE,
        (
            "...In the end, they got\x01",
            "away with the medical\x01",
            "supplies, didn't they.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, it's not your fault you\x01",
            "know. It's all my fault since\x01",
            "I was carelessly deceived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I must be more careful\x01",
            "and check next time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_101D")

    label("loc_FA2")


    ChrTalk(
        0xFE,
        (
            "...In the end, they got\x01",
            "away with the medical\x01",
            "supplies, didn't they.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I must be more careful\x01",
            "and check next time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_101D")

    Jump("loc_10A7")

    label("loc_1022")


    ChrTalk(
        0xFE,
        (
            "To think I was deceived by\x01",
            "forged documents... Dammit,\x01",
            "it's my responsibility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got to contact St.\x01",
            "Ursula later too...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10A7")

    Jump("loc_11FA")

    label("loc_10AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_11FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1189")

    ChrTalk(
        0xFE,
        (
            "I've become rather acquainted\x01",
            "with the Capua Express guys\x01",
            "at this airport too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a private shipping\x01",
            "company, it seems their\x01",
            "business has been booming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man, prospects are\x01",
            "bright.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_11FA")

    label("loc_1189")


    ChrTalk(
        0xFE,
        (
            "As a private shipping\x01",
            "company, Capua Express'\x01",
            "business seems to be booming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man, prospects are\x01",
            "bright.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11FA")

    TalkEnd(0xFE)
    Return()

    # Function_6_BD7 end

    def Function_7_11FE(): pass

    label("Function_7_11FE")

    Call(0, 8)
    Return()

    # Function_7_11FE end

    def Function_8_1202(): pass

    label("Function_8_1202")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_13CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1325")

    ChrTalk(
        0x8,
        (
            "After the jaegers and monsters\x01",
            "wandering the city left, I tried\x01",
            "to return to my post, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In a situation where airmail\x01",
            "can't be delivered, I wonder what\x01",
            "we should do going forward...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wonder if we'll be\x01",
            "able to get back to our\x01",
            "daily lives...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13C8")

    label("loc_1325")


    ChrTalk(
        0x8,
        (
            "In a situation where airmail\x01",
            "can't be delivered, I wonder what\x01",
            "we should do going forward...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wonder if we'll be\x01",
            "able to get back to our\x01",
            "daily lives...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13C8")

    Jump("loc_17C7")

    label("loc_13CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_15B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1508")

    ChrTalk(
        0x8,
        (
            "Liberl and Remiferia are\x01",
            "greatly supporting the\x01",
            "restoration of Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They gathered donation money, goods and\x01",
            "showed presence of mind in the restoration\x01",
            "work at a relatively early stage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As a Crossbell citizen, I\x01",
            "would really like to express\x01",
            "my gratitude to them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15AE")

    label("loc_1508")


    ChrTalk(
        0x8,
        (
            "Liberl and Remiferia are\x01",
            "greatly supporting the\x01",
            "restoration of Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As a Crossbell citizen, I\x01",
            "would really like to express\x01",
            "my gratitude to them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15AE")

    Jump("loc_17C7")

    label("loc_15B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_17C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16F3")

    ChrTalk(
        0x8,
        (
            "After independence was proposed, it\x01",
            "appears visitors are feeling anxious\x01",
            "about the state of Crossbell as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Although there weren't\x01",
            "many, we saw some people\x01",
            "cancel their planned trips.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That's reasonable, but from the\x01",
            "Crossbell citizens' point of\x01",
            "view, it's also a little sad.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17C7")

    label("loc_16F3")


    ChrTalk(
        0x8,
        (
            "After independence was proposed, it\x01",
            "appears visitors are feeling anxious\x01",
            "about the state of Crossbell as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That's reasonable, but from the\x01",
            "Crossbell citizens' point of\x01",
            "view, it's also a little sad.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17C7")

    TalkEnd(0x8)
    Return()

    # Function_8_1202 end

    def Function_9_17CB(): pass

    label("Function_9_17CB")

    Call(0, 10)
    Return()

    # Function_9_17CB end

    def Function_10_17CF(): pass

    label("Function_10_17CF")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_199B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1940")

    ChrTalk(
        0x9,
        (
            "After independence was declared, this\x01",
            "airport has become the interception point\x01",
            "against the major powers' invasion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It appears the jaegers who attacked\x01",
            "the city before were working as the\x01",
            "President's private army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...I don't know what to say. What about\x01",
            "our hearts that believed the President\x01",
            "and supported independence...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1996")

    label("loc_1940")


    ChrTalk(
        0x9,
        (
            "What about our hearts that\x01",
            "believed the President and\x01",
            "supported independence...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1996")

    Jump("loc_1E27")

    label("loc_199B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1BC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AEF")

    ChrTalk(
        0x9,
        (
            "The rumor going around that the\x01",
            "attack on Crossbell was a plot\x01",
            "by the Empire seems to be true.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "There's no positive proof, but...\x01",
            "It's also been said that where\x01",
            "there's smoke, there's fire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If we consider the Empire's actions\x01",
            "up to now, it's likely to be true...\x01",
            "That's the only way to think of it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1BBD")

    label("loc_1AEF")


    ChrTalk(
        0x9,
        (
            "The rumor going around that the\x01",
            "attack on Crossbell was a plot\x01",
            "by the Empire seems to be true.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "There're no positive proof, but\x01",
            "it's highly likely to be true...\x01",
            "That's the only way to think of it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BBD")

    Jump("loc_1E27")

    label("loc_1BC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1E27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D3A")

    ChrTalk(
        0x9,
        (
            "This is the immigration and emigration\x01",
            "notice reception desk. We can also\x01",
            "store your hand luggage for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you want to deliver packages abroad, why\x01",
            "not make a request with the "Capua Express"\x01",
            "representative standing right over there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "They seem to be quite popular and\x01",
            "deliver packages even more quickly\x01",
            "than common air transports.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E27")

    label("loc_1D3A")


    ChrTalk(
        0x9,
        (
            "If you want to deliver packages abroad, why\x01",
            "not make a request with the "Capua Express"\x01",
            "representative standing right over there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "They seem to be quite popular and\x01",
            "deliver packages even more quickly\x01",
            "than common air transports.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E27")

    TalkEnd(0x9)
    Return()

    # Function_10_17CF end

    def Function_11_1E2B(): pass

    label("Function_11_1E2B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Ooh, look, look! You can\x01",
            "see the airship taking\x01",
            "off!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Honey, you come too!\x01",
            "It's certainly exciting!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_1E2B end

    def Function_12_1E9F(): pass

    label("Function_12_1E9F")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "*sigh*, boys... No\x01",
            "matter the age, they're\x01",
            "always children.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, the technology to make\x01",
            "something so big fly must be amazing.\x01",
            "I have agree in that regard.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_1E9F end

    def Function_13_1F4F(): pass

    label("Function_13_1F4F")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Oh, that green airship\x01",
            "seems doesn't seem like\x01",
            "it's an airliner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From look of it, it appears to be an\x01",
            "old high-speed cruiser from Reinford...\x01",
            "Could just be some noble's property...?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_1F4F end

    def Function_14_2016(): pass

    label("Function_14_2016")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "The city restoration is largely\x01",
            "complete, so I thought I'd head out of\x01",
            "state with my whole family for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In Remiferia, where my\x01",
            "parents' home is, I'm\x01",
            "sure it'll be safe, yes.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_2016 end

    def Function_15_20DC(): pass

    label("Function_15_20DC")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "*sigh*, I was surprised\x01",
            "by this sudden trip back\x01",
            "home, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What my husband says is\x01",
            "true. It's become dangerous\x01",
            "recently for some reason...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_20DC end

    def Function_16_217B(): pass

    label("Function_16_217B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I'm gonna ride an\x01",
            "airshiiip. Ehehe, I\x01",
            "can't waaait.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll have to take lots\x01",
            "of photos from up in the\x01",
            "skies.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_217B end

    def Function_17_21F7(): pass

    label("Function_17_21F7")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_227A")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Welcome to the Independent State\x01",
            "of Crossbell! For lodging, come\x01",
            "to Hotel Millennium!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22C4")

    label("loc_227A")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Welcome to Crossbell\x01",
            "State! For lodging, come\x01",
            "to Hotel Millennium!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22C4")

    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_17_21F7 end

    def Function_18_22DD(): pass

    label("Function_18_22DD")

    EventBegin(0x1)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2398")

    ChrTalk(
        0xA,
        (
            "The police came just moments ago. It seems\x01",
            "they're searching for clues regarding the\x01",
            "jaegers at the landing field.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm sorry, but please\x01",
            "don't go past here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_240B")

    label("loc_2398")

    TurnDirection(0xA, 0x0, 500)

    ChrTalk(
        0xA,
        (
            "Whoops... The boarding\x01",
            "entrance is there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "You can't enter without\x01",
            "a ticket, so please be\x01",
            "careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_240B")

    Sleep(50)
    SetChrPos(0x0, 960, 0, 5140, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_244C")
    TurnDirection(0xA, 0x12, 0)
    Jump("loc_2453")

    label("loc_244C")

    OP_93(0xA, 0xB4, 0x0)

    label("loc_2453")

    OP_4C(0xA, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_18_22DD end

    def Function_19_245A(): pass

    label("Function_19_245A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch06000.itc", 0x1E)
    LoadChrToIndex("apl/ch50314.itc", 0x1F)
    LoadChrToIndex("chr/ch47900.itc", 0x20)
    LoadChrToIndex("chr/ch27400.itc", 0x21)
    LoadChrToIndex("chr/ch27800.itc", 0x22)
    LoadChrToIndex("chr/ch27900.itc", 0x23)
    LoadChrToIndex("chr/ch27600.itc", 0x24)
    LoadEffect(0x0, "event/eva02_00.eff")
    SetChrChipByIndex(0x17, 0x1E)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x1F)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetChrChipByIndex(0x19, 0x20)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x21)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x22)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1C, 0x23)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1D, 0x24)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetMapObjFlags(0x5, 0x1000)
    ClearMapObjFlags(0x5, 0x4)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0x17, -1450, 5000, 13350, 0)
    SetChrPos(0x18, -900, 5000, 13950, 0)
    SetChrPos(0x19, 3000, 5000, 13450, 0)
    SetChrPos(0x1A, 1150, 5000, 13950, 0)
    SetChrPos(0x1B, -3150, 5000, 13350, 45)
    SetChrPos(0x1C, 1550, 5000, 12500, 0)
    SetChrPos(0x1D, 4700, 5000, 13000, 0)
    BeginChrThread(0x18, 3, 0, 20)
    OP_68(1000, 8000, 13250, 0)
    MoveCamera(315, 15, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(37800, 0)
    OP_68(1000, 6000, 13250, 5000)
    SetCameraDistance(35800, 5000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 5)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_19_245A end

    def Function_20_2640(): pass

    label("Function_20_2640")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_26F8")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_266E")
    Sleep(500)
    Jump("loc_26B6")

    label("loc_266E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2685")
    Sleep(1000)
    Jump("loc_26B6")

    label("loc_2685")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_269C")
    Sleep(1500)
    Jump("loc_26B6")

    label("loc_269C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_26B3")
    Sleep(2000)
    Jump("loc_26B6")

    label("loc_26B3")

    Sleep(2500)

    label("loc_26B6")

    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(810, 0, 80, 0)
    Jump("Function_20_2640")

    label("loc_26F8")

    Return()

    # Function_20_2640 end

    def Function_21_26F9(): pass

    label("Function_21_26F9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch11200.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x20)
    LoadChrToIndex("chr/ch02902.itc", 0x22)
    LoadChrToIndex("apl/ch51212.itc", 0x24)
    LoadChrToIndex("chr/ch30000.itc", 0x25)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07100.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x1)
    SetChrChipByIndex(0x109, 0x22)
    SetChrSubChip(0x109, 0x2)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrPos(0x101, 3000, 5000, 11400, 0)
    SetChrPos(0x102, 2700, 5100, 13000, 90)
    SetChrPos(0x104, 4500, 5000, 10600, 0)
    SetChrPos(0x109, 4800, 5100, 12300, 270)
    SetChrPos(0x105, 3300, 5000, 10100, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x13, 0x1E)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, -8300, 5000, 6700, 90)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0x15, 0x25)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, -4300, 0, -6800, 45)
    BeginChrThread(0x15, 0, 0, 0)
    SetChrChipByIndex(0x16, 0x25)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, -3700, 0, 6600, 180)
    BeginChrThread(0x16, 0, 0, 0)
    ClearChrFlags(0x14, 0x80)
    OP_78(0x5, 0x14)
    OP_49()
    SetChrPos(0x14, -7700, 0, 29900, 270)
    OP_D5(0x14, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    ClearMapObjFlags(0x5, 0x4)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    OP_11(0xE4, 0xA9, 0x9D, 0x32, 0xBE, 0x0)
    OP_68(0, 2000, 0, 0)
    MoveCamera(330, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(30000, 0)
    OP_68(0, 7500, 0, 9000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)
    Fade(500)
    OP_68(4300, 6500, 12000, 0)
    MoveCamera(330, 20, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(22000, 0)
    SetCameraDistance(20500, 2000)
    OP_6F(0x79)

    ChrTalk(
        0x109,
        (
            "#6P#10102FLiberl Kingdom's high\x01",
            "speed cruiser, the\x01",
            "Arseille...\x02\x03",
            "#10109F*sigh*... It really is\x01",
            "an amazing ship...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#6PIt's the world's fastest\x01",
            "airship. It really put ZCF on\x01",
            "the map.\x02\x03",
            "#00100FBecause they keep improving\x01",
            "their own speed records, no\x01",
            "one else has even come close.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00309FSo that's the flagship\x01",
            "the Liberl princess came\x01",
            "ridin' in on.\x02\x03",
            "#00302FPrincess Klaudia, was\x01",
            "she? She seems very\x01",
            "esteemed.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        (
            "#00004F#5PTo be precise, she's not\x01",
            "a "princess", but a\x01",
            ""crown princess".\x02\x03",
            "#00000FIn other words, the next\x01",
            "queen of Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00305FAah, I see.\x02\x03",
            "#00301F...Could she be the one\x01",
            "who called us here?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#5P#00106FH-Hmm. We really don't\x01",
            "know.\x02\x03",
            "#00108FI think Bell would know\x01",
            "Her Highness' schedule.\x01",
            "Maybe I should ask her.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x105, 0x13, 500)

    def lambda_2C77():

        label("loc_2C77")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_2C77")

    QueueWorkItem2(0x105, 2, lambda_2C77)

    ChrTalk(
        0x105,
        (
            "#11P#10302FHaha... It seems that\x01",
            "won't be necessary.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    ChrTalk(
        0x101,
        "#5P#00005FHuh.\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    ClearChrFlags(0x13, 0x80)

    NpcTalk(
        0x13,
        "Calm Voice",
        (
            "─I've kept you waiting. You are\x01",
            "the ladies and gentlemen of the\x01",
            "Special Support Section, correct?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_2DA7():

        label("loc_2DA7")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_2DA7")

    QueueWorkItem2(0x101, 2, lambda_2DA7)
    Sleep(50)

    def lambda_2DBC():

        label("loc_2DBC")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_2DBC")

    QueueWorkItem2(0x104, 2, lambda_2DBC)
    Sleep(100)
    SetChrSubChip(0x109, 0x1)
    Sleep(300)
    Fade(500)
    OP_68(-7500, 6100, 7000, 0)
    MoveCamera(336, 19, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20500, 0)
    OP_68(1800, 6100, 11300, 5500)
    MoveCamera(321, 19, 0, 5500)

    def lambda_2E27():
        OP_95(0xFE, -4300, 5000, 10000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2E27)
    WaitChrThread(0x13, 1)

    def lambda_2E45():
        OP_95(0xFE, 1000, 5000, 11000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2E45)
    WaitChrThread(0x13, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x105, 0x2)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00011FAh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10101F!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FI-I knew it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00305FOh, you're the young\x01",
            "lady that caused the\x01",
            "fuss earlier...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#07105F#5P...?\x02\x03",
            "#07104FI do apologize for that. I\x01",
            "take it you were at the\x01",
            "unveiling ceremony as well?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(20000, 300)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    OP_6F(0x79)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x13,
        (
            "─But where are my manners. Captain\x01",
            "Julia Schwartz of the Liberl Royal\x01",
            "Guard, at your service.\x02\x03",
            "By order of Her Highness Klaudia,\x01",
            "allow me to guide you to the\x01",
            "Arseille.\x02\x03",
            "Please, follow me.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    SetCameraDistance(20500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(500)
    SetScenarioFlags(0x22, 1)
    NewScene("t3520", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_21_26F9 end

    def Function_22_3114(): pass

    label("Function_22_3114")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(6860, 1250, -5300, 0)
    MoveCamera(315, 27, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(36000, 0)
    SetChrPos(0x101, 6000, 0, -4790, 0)
    SetChrPos(0x102, 7200, 0, -4850, 0)
    SetChrPos(0x103, 5430, 0, -5620, 0)
    SetChrPos(0x104, 6910, 0, -5920, 0)
    SetChrPos(0x109, 7600, 0, -6670, 0)
    SetChrPos(0x105, 6280, 0, -6960, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x11, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FExcuse us, are you with\x01",
            "the Capua Express?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Yeah, that's right.\x01",
            "...And you are?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FCrossbell Police,\x01",
            "Special Support Section.\x02\x03",
            "We saw your request and\x01",
            "came to ask about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Ohh, you're them then!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Man, thanks. We're in a\x01",
            "total bind here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "It's a job that's gonna\x01",
            "require a tiny bit of\x01",
            "time... Will you accept?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 24)
    OP_4C(0x11, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 6600, 0, -5000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_22_3114 end

    def Function_23_3366(): pass

    label("Function_23_3366")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(6860, 1250, -5300, 0)
    MoveCamera(315, 27, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(36000, 0)
    SetChrPos(0x101, 6000, 0, -4790, 0)
    SetChrPos(0x102, 7200, 0, -4850, 0)
    SetChrPos(0x103, 5430, 0, -5620, 0)
    SetChrPos(0x104, 6910, 0, -5920, 0)
    SetChrPos(0x109, 7600, 0, -6670, 0)
    SetChrPos(0x105, 6280, 0, -6960, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x11, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x11,
        "Oh, are you free?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "It's a job that's gonna\x01",
            "require a tiny bit of\x01",
            "time... Will you accept?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 24)
    OP_4C(0x11, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 6600, 0, -5000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_23_3366 end

    def Function_24_34BF(): pass

    label("Function_24_34BF")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Accept]\x01",      # 0
            "[Cancel]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3521"),
        (1, "loc_3529"),
        (SWITCH_DEFAULT, "loc_35CA"),
    )


    label("loc_3521")

    Call(0, 25)
    Jump("loc_35CA")

    label("loc_3529")


    ChrTalk(
        0x101,
        (
            "#00006FSorry, our hands are\x01",
            "full right now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Oh, really? Oh, man...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Then, come speak with me\x01",
            "again when you're free,\x01",
            "alright?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x175, 4)
    Jump("loc_35CA")

    label("loc_35CA")

    Return()

    # Function_24_34BF end

    def Function_25_35CB(): pass

    label("Function_25_35CB")


    ChrTalk(
        0x101,
        (
            "#00000FYes, please leave it to\x01",
            "us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FThe request was about\x01",
            "misdelivered packages or\x01",
            "something, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Yeah, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "We fly to all sorts of places\x01",
            "across the continent delivering\x01",
            "our customers' packages, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "This time, we made a\x01",
            "mistake with some packages\x01",
            "we delivered here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "It looks like the addresses got\x01",
            "switched and we delivered several\x01",
            "packages to the wrong addresses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FMy... That's terrible.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206FI don't think address\x01",
            "label mistakes happen\x01",
            "that often, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Weeell, our president is\x01",
            "a scatterbrain, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "This sort of thing has\x01",
            "happened many times\x01",
            "before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "At worst, she affixes letters\x01",
            "from her friends instead of\x01",
            "the address labels...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FAhaha... Your president\x01",
            "seems to be careless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Well, I respect her though.\x01",
            "She took us in when we had\x01",
            "nowhere to go...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "...*ahem*, sorry. I got\x01",
            "off-track.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "In short, I want to ask you\x01",
            "to redeliver the packages\x01",
            "that were wrongly delivered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "After our packages are received in-state, they're\x01",
            "left with a local shipping company for the rest of\x01",
            "the trip, because we aren't familiar with the place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FI see, I understand the\x01",
            "situation.\x02\x03",
            "#10302FDo you know where the\x01",
            "misdelivered packages\x01",
            "are?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Umm, according to what I\x01",
            "could confirm, let's\x01",
            "see...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "A package addressed to St.\x01",
            "Ursula was delivered to the\x01",
            "Der Ziegel Inn in Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Then, it seems a package meant for a\x01",
            "house on Residential Street in the\x01",
            "city went to St. Ursula Hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "I want you to visit those addresses,\x01",
            "recover the misdelivered packages\x01",
            "and deliver the intended ones.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "...And so, take these.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x331),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x331, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x332),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x332, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00000FThis is the package that\x01",
            "was supposed to go to\x01",
            "Der Ziegel, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FAnd this address label was\x01",
            "supposed to have been on\x01",
            "the hospital's package.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Yeah, that's it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "First, deliver this package\x01",
            "to the Der Ziegel Inn or\x01",
            "whatever it's called.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "The package intended for St.\x01",
            "Ursula Hospital should be\x01",
            "there, so take that and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "...Somehow, saying it\x01",
            "myself I don't get it\x01",
            "anymore.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00003FI-In any case... It's\x01",
            "all right to exchange\x01",
            "the packages in order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Yes, exactly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "I'm sorry it's a pain,\x01",
            "but we're counting on\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FAlright, understood.\x02\x03",
            "#00000F...In that case, let's\x01",
            "head to the Der Ziegel\x01",
            "Inn in Mainz right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FOh man, this one looks\x01",
            "pretty tough.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [Redelivering the\x01",
            "Misdeliveries]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x175, 5)
    OP_29(0x85, 0x1, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4C(0x11, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 6600, 0, -5000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_25_35CB end

    def Function_26_40DD(): pass

    label("Function_26_40DD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(6860, 2500, -5300, 0)
    MoveCamera(315, 27, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(36000, 0)
    SetChrPos(0x101, 6000, 0, -4790, 0)
    SetChrPos(0x102, 7200, 0, -4850, 0)
    SetChrPos(0x103, 5430, 0, -5620, 0)
    SetChrPos(0x104, 6910, 0, -5920, 0)
    SetChrPos(0x109, 7600, 0, -6670, 0)
    SetChrPos(0x105, 6280, 0, -6960, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x11, 0xFF)
    OP_68(6860, 1250, -5300, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x11,
        (
            "Oh, it seems you've properly\x01",
            "delivered the packages to\x01",
            "the correct destinations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Maaan, what a help you've\x01",
            "been. Really, thanks a\x01",
            "bunch, Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYou're welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "By the way...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x11,
        (
            "That young lady... Does\x01",
            "she look unwell to you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#1S*mumble mumble*... To\x01",
            "think we spoke to a\x01",
            "spirit...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x105,
        (
            "#10309FHehe, looks like she\x01",
            "took quite the shock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FI understand how she\x01",
            "feels...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FWell, she'll settle down\x01",
            "before long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FUmm... That's how it is,\x01",
            "so please don't worry\x01",
            "about it.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x11, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x11,
        "Really? Well, alright...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "I'll excuse myself,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "If something comes up\x01",
            "again, we'll be counting\x01",
            "on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, let us know\x01",
            "anytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FWe'll be looking forward\x01",
            "to it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_459D")
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00000F...Alright, then let's hurry\x01",
            "to the derailment site on\x01",
            "West Crossbell Highway.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_459D")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_57(0x0)
    OP_5A()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [Redelivering the\x01",
            "Misdeliveries]\x07\x00\x01",
            "completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x85, 0x1, 0x5)
    OP_29(0x85, 0x1, 0x6)
    OP_29(0x85, 0x4, 0x10)
    SubItemNumber(0x332, 1)
    OP_4C(0x11, 0xFF)
    ClearMapFlags(0x10000000)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_464E")
    EventEnd(0x5)
    NewScene("c0000", 103, 0, 0)
    IdleLoop()
    Jump("loc_4665")

    label("loc_464E")

    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 6600, 0, -5000, 0)
    EventEnd(0x5)

    label("loc_4665")

    Return()

    # Function_26_40DD end

    def Function_27_4666(): pass

    label("Function_27_4666")

    EventBegin(0x0)
    Fade(500)
    OP_68(5810, 1250, 4500, 0)
    MoveCamera(315, 27, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(32500, 0)
    SetChrPos(0x101, 5480, 0, 4000, 0)
    SetChrPos(0x102, 6680, 0, 4000, 0)
    SetChrPos(0x104, 5480, 0, 2800, 0)
    SetChrPos(0x103, 6580, 0, 2800, 0)
    SetChrPos(0x105, 5480, 0, 1600, 0)
    SetChrPos(0x109, 6680, 0, 1600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x12, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_0D()

    ChrTalk(
        0x12,
        (
            "*sigh*, what should I\x01",
            "do...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If I had been more\x01",
            "careful, such a thing\x01",
            "would've never...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FExcuse us... Has\x01",
            "something happened?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_47DC():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_47DC)
    Sleep(10)

    def lambda_47EC():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_47EC)
    WaitChrThread(0xA, 2)
    Sleep(500)

    ChrTalk(
        0x12,
        (
            "Oh, you're the Special Support\x01",
            "Section... Actually, something\x01",
            "troublesome has happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "The plan was to deliver medical\x01",
            "supplies from Remiferia to St.\x01",
            "Ursula Hospital today, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "It appears that some guy\x01",
            "cheated us out of them.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#00105FHe stole medical\x01",
            "supplies!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yeah... Not long ago, a man\x01",
            "saying he was from a\x01",
            "shipping company came here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "He gave a plausible reason, saying that\x01",
            "he was taking over the delivery for\x01",
            "Rhymes Shipping that couldn't make it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It didn't seem like he was\x01",
            "lying at all, so I readily\x01",
            "handed over the packages.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "However, I don't remember\x01",
            "seeing an authorization\x01",
            "like that anywhere else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "And while talking about this\x01",
            "and that, I realized we'd been\x01",
            "cheated out of the goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FHmm... In short, that\x01",
            "authorization was a\x01",
            "counterfeit, is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10301FBut, you'd have to be one nasty\x01",
            "fellow to steal medical supplies\x01",
            "in this time of crisis.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108FThey say there are lot\x01",
            "of hospitalized attack\x01",
            "victims...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FThat's because medical supplies\x01",
            "like those would fetch a fair\x01",
            "bit of mira on the black market.\x02\x03",
            "#00301FIt's probably a sly opportunist\x01",
            "after some mira.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101FH-How horrible...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Still, this is a\x01",
            "problem...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "St. Ursula says they're\x01",
            "waiting for the goods to\x01",
            "arrive even now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yeah, it's totally my fault...\x01",
            "If I had at least checked with\x01",
            "Rhymes Shipping...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0xA, 500)

    ChrTalk(
        0x12,
        (
            "No... It's not your fault. No matter how\x01",
            "you look at it, the one at fault is the\x01",
            "guy who cheated us out of the packages.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x12, 0x101, 500)

    ChrTalk(
        0x12,
        (
            "Oh, right... Couldn't\x01",
            "you guys look for the\x01",
            "thief?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "For the patients at St.\x01",
            "Ursula too, I'd like to\x01",
            "catch him somehow or other.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 29)
    OP_4C(0x12, 0xFF)
    OP_4C(0xA, 0xFF)
    TurnDirection(0x12, 0xA, 0)
    TurnDirection(0xA, 0x12, 0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 6080, 0, 4000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_27_4666 end

    def Function_28_4F60(): pass

    label("Function_28_4F60")

    EventBegin(0x0)
    Fade(500)
    OP_68(5810, 1250, 4500, 0)
    MoveCamera(315, 27, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(32500, 0)
    SetChrPos(0x101, 5480, 0, 4000, 0)
    SetChrPos(0x102, 6680, 0, 4000, 0)
    SetChrPos(0x104, 5480, 0, 2800, 0)
    SetChrPos(0x103, 6580, 0, 2800, 0)
    SetChrPos(0x105, 5480, 0, 1600, 0)
    SetChrPos(0x109, 6680, 0, 1600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x12, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_93(0x12, 0xB4, 0x0)
    OP_93(0xA, 0xB4, 0x0)
    OP_0D()

    ChrTalk(
        0x12,
        (
            "The medical supplies\x01",
            "thief... Can't you look\x01",
            "for him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "For the patients at St.\x01",
            "Ursula too, I'd like to\x01",
            "catch him somehow or other.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 29)
    OP_4C(0x12, 0xFF)
    OP_4C(0xA, 0xFF)
    TurnDirection(0x12, 0xA, 0)
    TurnDirection(0xA, 0x12, 0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 6080, 0, 4000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_28_4F60 end

    def Function_29_50F7(): pass

    label("Function_29_50F7")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Accept\x01",      # 0
            "Cancel\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5155"),
        (1, "loc_515D"),
        (SWITCH_DEFAULT, "loc_5249"),
    )


    label("loc_5155")

    Call(0, 30)
    Jump("loc_5249")

    label("loc_515D")


    ChrTalk(
        0x101,
        (
            "#00003FI'm sorry... We've got\x01",
            "business we can't get\x01",
            "away from right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I-I see... Then it can't\x01",
            "be helped...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Speak with me again if\x01",
            "you manage to find the\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "You're the only ones I\x01",
            "can count on. Please.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19B, 6)
    Jump("loc_5249")

    label("loc_5249")

    Return()

    # Function_29_50F7 end

    def Function_30_524A(): pass

    label("Function_30_524A")


    ChrTalk(
        0x101,
        (
            "#00003F...It seems that not much time has\x01",
            "passed since the incident yet... If\x01",
            "we hurry, we could make it in time.\x02\x03",
            "#00000FPlease leave it to us for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Ohh...I owe you one!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FHowever, it seems our opponent has\x01",
            "already finished his job... It\x01",
            "seems we should really hurry up.\x02\x03",
            "#00101FWasn't there any clue that could\x01",
            "indicate the culprit's\x01",
            "destination?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Let's see... I didn't\x01",
            "see him, so I couldn't\x01",
            "say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Now that I think about it... It\x01",
            "seems that man was driving a\x01",
            "Reinford-made black transport.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Just going by appearance, he\x01",
            "seemed like a well-dressed\x01",
            "imperial, so maybe...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301FThen it's likely he's\x01",
            "trying to escape to the\x01",
            "Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103FIf that's the case, he might be\x01",
            "approaching Bellguard Gate by now.\x02\x03",
            "#10101FI think it's best to chase him by\x01",
            "getting information about the transport\x01",
            "along the way, just in case...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306FWell, it seems we can't\x01",
            "take our time, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FIn any case... Let's try\x01",
            "chasing after him.\x02\x03",
            "#00001FBilly, Ricardo. Please\x01",
            "wait here for us to\x01",
            "contact you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "Yeah, got it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We're counting on you,\x01",
            "everyone!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [Medical Supplies\x01",
            "Investigation]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x93, 0x4, 0x2)
    OP_29(0x93, 0x1, 0x0)
    Return()

    # Function_30_524A end

    SaveToFile()

Try(main)
