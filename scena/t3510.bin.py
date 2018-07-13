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
        "Function_5_B08",          # 05, 5
        "Function_6_BDD",          # 06, 6
        "Function_7_122E",         # 07, 7
        "Function_8_1232",         # 08, 8
        "Function_9_1825",         # 09, 9
        "Function_10_1829",        # 0A, 10
        "Function_11_1ED5",        # 0B, 11
        "Function_12_1F4F",        # 0C, 12
        "Function_13_2016",        # 0D, 13
        "Function_14_20F0",        # 0E, 14
        "Function_15_21B3",        # 0F, 15
        "Function_16_224D",        # 10, 16
        "Function_17_22C6",        # 11, 17
        "Function_18_23DE",        # 12, 18
        "Function_19_2558",        # 13, 19
        "Function_20_273E",        # 14, 20
        "Function_21_27F7",        # 15, 21
        "Function_22_3276",        # 16, 22
        "Function_23_34C7",        # 17, 23
        "Function_24_3633",        # 18, 24
        "Function_25_373A",        # 19, 25
        "Function_26_42C3",        # 1A, 26
        "Function_27_4830",        # 1B, 27
        "Function_28_51C3",        # 1C, 28
        "Function_29_5385",        # 1D, 29
        "Function_30_54B8",        # 1E, 30
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_932")

    ChrTalk(
        0xFE,
        (
            "Go around the places where the packages\x01",
            "were mistakenly sent and exchange them\x01",
            "with the correct ones.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It'll be alright going first to Mainz,\x01",
            "then St. Ursula Hospital and finally to\x01",
            "the Residential Street private house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As for that private house address,\x01",
            "it's written on the slip, so check\x01",
            "it again when going there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Sorry for the bother. I'm counting on you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_9DC")

    label("loc_932")


    ChrTalk(
        0xFE,
        (
            "It'll be alright going first to Mainz,\x01",
            "then St. Ursula Hospital and finally to\x01",
            "the Residential Street private house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Sorry for the bother. I'm counting on you.\x02",
    )

    CloseMessageWindow()

    label("loc_9DC")

    Jump("loc_B04")

    label("loc_9E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A98")

    ChrTalk(
        0xFE,
        "Thank you for your hard work, you were a big help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, then I must report to the boss...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I mean, to the president, that everything ended all right.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_B04")

    label("loc_A98")


    ChrTalk(
        0xFE,
        "Thank you for your hard work, you were a big help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'll count on you if something comes up again.\x02",
    )

    CloseMessageWindow()

    label("loc_B04")

    TalkEnd(0xFE)
    Return()

    # Function_4_75D end

    def Function_5_B08(): pass

    label("Function_5_B08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B4B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 6)), scpexpr(EXPR_END)), "loc_B47")
    Call(0, 28)
    Jump("loc_B4A")

    label("loc_B47")

    Call(0, 27)

    label("loc_B4A")

    Return()

    label("loc_B4B")

    TalkBegin(0x12)

    ChrTalk(
        0xFE,
        (
            "Cheating out medical goods in\x01",
            "Crossbell at such a time...\x01",
            "Totally unforgivable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You guys, catch the\x01",
            "culprit in a way or another!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x12)
    Return()

    # Function_5_B08 end

    def Function_6_BDD(): pass

    label("Function_6_BDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 6)), scpexpr(EXPR_END)), "loc_C1C")
    Call(0, 28)
    Jump("loc_C1F")

    label("loc_C1C")

    Call(0, 27)

    label("loc_C1F")

    Return()

    label("loc_C20")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_CC7")

    ChrTalk(
        0xA,
        (
            "The police came just moments ago. It seems they \x01",
            "are searching for jaegers' traces at the landing field.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I'm sorry, but don't go past here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_122A")

    label("loc_CC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_CD5")
    Jump("loc_122A")

    label("loc_CD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_CE3")
    Jump("loc_122A")

    label("loc_CE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_10BE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_EDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E0D")

    ChrTalk(
        0xFE,
        (
            "You have safely taken back\x01",
            "the medical goods, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just before, a call came from St. Ursula\x01",
            "about them receiving the packages.\x01",
            "I could finally rest assured too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I must be more careful and\x01",
            "check so that such a thing\x01",
            "doesn't happen in the future.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_ED9")

    label("loc_E0D")


    ChrTalk(
        0xFE,
        (
            "Just before, a call came from St. Ursula\x01",
            "about them receiving the packages.\x01",
            "I could finally rest assured too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I must be more careful and\x01",
            "check so that such a thing\x01",
            "doesn't happen in the future.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ED9")

    Jump("loc_10B9")

    label("loc_EDE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_1039")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FC5")

    ChrTalk(
        0xFE,
        (
            "...In the end, they got away\x01",
            "with the medical goods, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, it's not your fault you know.\x01",
            "It's all my bad since I was carelessly deceived.\x02",
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
    Jump("loc_1034")

    label("loc_FC5")


    ChrTalk(
        0xFE,
        (
            "...In the end, they got away\x01",
            "with the medical goods, eh?\x02",
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

    label("loc_1034")

    Jump("loc_10B9")

    label("loc_1039")


    ChrTalk(
        0xFE,
        (
            "To think I was deceived by forged documents...\x01",
            "Dammit, it's my responsibility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I must contact St.\x01",
            "Ursula later too...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10B9")

    Jump("loc_122A")

    label("loc_10BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_122A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11A4")

    ChrTalk(
        0xFE,
        (
            "I've become very acquainted at the\x01",
            "airport with the Capua Express guys too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a private enterprise shipping company,\x01",
            "it seems their business has been blooming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Man, prospects are bright.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_122A")

    label("loc_11A4")


    ChrTalk(
        0xFE,
        (
            "As a private enterprise shipping company,\x01",
            "the Capua Express business seems\x01",
            "to be quite blooming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Man, prospects are bright.\x02",
    )

    CloseMessageWindow()

    label("loc_122A")

    TalkEnd(0xFE)
    Return()

    # Function_6_BDD end

    def Function_7_122E(): pass

    label("Function_7_122E")

    Call(0, 8)
    Return()

    # Function_7_122E end

    def Function_8_1232(): pass

    label("Function_8_1232")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1409")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1366")

    ChrTalk(
        0x8,
        (
            "After the jaegers and the monsters loitering in the city\x01",
            "went away, I tried to get back to my post for now, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In a situation where airmail can't run at all,\x01",
            "I wonder what should we do in the future...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wonder if we'll be able to\x01",
            "get back our daily lives...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1404")

    label("loc_1366")


    ChrTalk(
        0x8,
        (
            "In a situation where airmail can't run at all,\x01",
            "I wonder what should we do in the future...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wonder if we'll be able to\x01",
            "get back our daily lives...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1404")

    Jump("loc_1821")

    label("loc_1409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_15E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_153C")

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
            "They gathered donation money, goods\x01",
            "and showed a presence of mind in\x01",
            "restoration works relatively early stages.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As a Crossbell citizen, I would really\x01",
            "like to express them my gratitude.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15DF")

    label("loc_153C")


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
            "As a Crossbell citizen, I would really\x01",
            "like to express them my gratitude.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15DF")

    Jump("loc_1821")

    label("loc_15E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1821")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_173B")

    ChrTalk(
        0x8,
        (
            "After the independence was advocated,\x01",
            "it appears the visitors too are feeling\x01",
            "the anxiety in Crossbell state of things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In practice, we saw even\x01",
            "persons cancelling their\x01",
            "planned trips, although a few.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It can be reasonable, but from\x01",
            "the point of view of the Crossbell\x01",
            "citizens, it's also a little sad.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1821")

    label("loc_173B")


    ChrTalk(
        0x8,
        (
            "After the independence was advocated,\x01",
            "it appears the visitors too are feeling\x01",
            "the anxiety in Crossbell state of things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It can be reasonable, but from\x01",
            "the point of view of the Crossbell\x01",
            "citizens, it's also a little sad.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1821")

    TalkEnd(0x8)
    Return()

    # Function_8_1232 end

    def Function_9_1825(): pass

    label("Function_9_1825")

    Call(0, 10)
    Return()

    # Function_9_1825 end

    def Function_10_1829(): pass

    label("Function_10_1829")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1A2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19C7")

    ChrTalk(
        0x9,
        (
            "After the independence declaration has been carried out, \x01",
            "this airport has become the interception point against\x01",
            "the two major powers' invasion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It appears that the jaegers who\x01",
            "raided the city before were working\x01",
            "as the President's private corps.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...I don't know what to say.\x01",
            "What about our hearts that believed the President's\x01",
            "words and supported the independence...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A29")

    label("loc_19C7")


    ChrTalk(
        0x9,
        (
            "What about our hearts that believed the President's\x01",
            "words and supported the independence...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A29")

    Jump("loc_1ED1")

    label("loc_1A2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1C6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B8C")

    ChrTalk(
        0x9,
        (
            "It's been whispered with seeming\x01",
            "truth that the Crossbell raid incident\x01",
            "was an Empire plot intrigue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "There're no positive proofs, but...\x01",
            "It's also said that where\x01",
            "there's smoke, there's fire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If we consider the Empire doings until now,\x01",
            "the possibility that's true is high...\x01",
            "You can only think it like that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C65")

    label("loc_1B8C")


    ChrTalk(
        0x9,
        (
            "It's been whispered with seeming\x01",
            "truth that the Crossbell raid incident\x01",
            "was an Empire plot intrigue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "There're no positive proofs, but,\x01",
            "the possibility that's true is high...\x01",
            "You can only think it like that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C65")

    Jump("loc_1ED1")

    label("loc_1C6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1ED1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DE0")

    ChrTalk(
        0x9,
        (
            "This is the immigration and emigration notice reception.\x01",
            "We also take in custody your hand baggages.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you want to deliver packages abroad,\x01",
            "why don't trying requesting the persons of\x01",
            "the "Capua Express" who are right here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It seems they are quite popular and they quickly deliver\x01",
            "packages even more than the common air transports.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1ED1")

    label("loc_1DE0")


    ChrTalk(
        0x9,
        (
            "If you want to deliver packages abroad,\x01",
            "why don't trying requesting the persons of\x01",
            "the "Capua Express" who are right here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It seems they are quite popular and they quickly deliver\x01",
            "packages even more than the common air transports.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ED1")

    TalkEnd(0x9)
    Return()

    # Function_10_1829 end

    def Function_11_1ED5(): pass

    label("Function_11_1ED5")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Ooh, look, look!\x01",
            "You can see the airship taking off!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Honey, you look too!\x01",
            "It sure is something exciting!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_1ED5 end

    def Function_12_1F4F(): pass

    label("Function_12_1F4F")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "*sigh*, boys...\x01",
            "No matter the age, they're always children.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, to make such a big thing fly in\x01",
            "the sky, the technology must be amazing.\x01",
            "I have to frankly agree in that regard.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_1F4F end

    def Function_13_2016(): pass

    label("Function_13_2016")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Oh, that green-colored airship seems\x01",
            "to be different from a passenger one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From the looks it appears to be an old type\x01",
            "of high-speed cruiser from Reinford...\x01",
            "Could it be just some noble's property...?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_2016 end

    def Function_14_20F0(): pass

    label("Function_14_20F0")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "The city restoration is generally over,\x01",
            "so I thought to go abroad with all my\x01",
            "family for some time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In Remiferia, where my parents'\x01",
            "home is located, I'm sure it'll\x01",
            "be safe, yes.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_20F0 end

    def Function_15_21B3(): pass

    label("Function_15_21B3")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "*sigh*, I was surprised by this\x01",
            "sudden trip back home, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What my husband says holds true.\x01",
            "Recently it's somehow become dangerous...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_21B3 end

    def Function_16_224D(): pass

    label("Function_16_224D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I'm gonna ride an airshiiip.\x01",
            "Ehehe, I can't waaait.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll have to take lots of\x01",
            "photos from up the skies.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_224D end

    def Function_17_22C6(): pass

    label("Function_17_22C6")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2359")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Welcome to the Independent State of Crossbell!\x01",
            "For your stay and lodging, \x01",
            "come to "Hotel Millennium!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23C5")

    label("loc_2359")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Welcome to the Autonomous State of Crossbell!\x01",
            "For your stay and lodging, \x01",
            "come to "Hotel Millennium!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23C5")

    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_17_22C6 end

    def Function_18_23DE(): pass

    label("Function_18_23DE")

    EventBegin(0x1)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2488")

    ChrTalk(
        0xA,
        (
            "The police came just moments ago. It seems they \x01",
            "are searching for jaegers' traces at the landing field.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I'm sorry, but don't go past here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2509")

    label("loc_2488")

    TurnDirection(0xA, 0x0, 500)

    ChrTalk(
        0xA,
        (
            "Halt there...\x01",
            "The boarding entrance is there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Since you can't enter without\x01",
            "having a ticket, please be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2509")

    Sleep(50)
    SetChrPos(0x0, 960, 0, 5140, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_254A")
    TurnDirection(0xA, 0x12, 0)
    Jump("loc_2551")

    label("loc_254A")

    OP_93(0xA, 0xB4, 0x0)

    label("loc_2551")

    OP_4C(0xA, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_18_23DE end

    def Function_19_2558(): pass

    label("Function_19_2558")

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

    # Function_19_2558 end

    def Function_20_273E(): pass

    label("Function_20_273E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_27F6")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_276C")
    Sleep(500)
    Jump("loc_27B4")

    label("loc_276C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2783")
    Sleep(1000)
    Jump("loc_27B4")

    label("loc_2783")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_279A")
    Sleep(1500)
    Jump("loc_27B4")

    label("loc_279A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_27B1")
    Sleep(2000)
    Jump("loc_27B4")

    label("loc_27B1")

    Sleep(2500)

    label("loc_27B4")

    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(810, 0, 80, 0)
    Jump("Function_20_273E")

    label("loc_27F6")

    Return()

    # Function_20_273E end

    def Function_21_27F7(): pass

    label("Function_21_27F7")

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
            "#6P#10102FThe Liberl Kingdom high-speed cruiser,\x01",
            "the "Arseille"...\x02\x03",
            "#10109F*sigh*...\x01",
            "As I thought, it's an amazing airship...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#6PIt's the world's fastest airship with which\x01",
            "ZCF made a name for themselves...\x02\x03",
            "#00100FIt seems it still keeps itself away from the others\x01",
            "by continuing to improve on its own records.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00309FSo that's the flagship the\x01",
            "Liberl princess came ridin' in.\x02\x03",
            "#00302FPrincess Klaudia, was she?\x01",
            "She seems to be an august person...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        (
            "#00004F#5PTo be precise, she's not a "princess",\x01",
            "but the "crown princess".\x02\x03",
            "#00000FIn other words, it means that she's\x01",
            "the next Liberl Kingdom queen in line.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00305FAah, I see.\x02\x03",
            "#00301F...No way that we were\x01",
            "called by her in person, huh?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#5P#00106FU-Uhhm.\x01",
            "We can't really know.\x02\x03",
            "#00108FAlthough I think that if\x01",
            "I asked Bell, I could know\x01",
            "her highness schedule...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x105, 0x13, 500)

    def lambda_2DD5():

        label("loc_2DD5")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_2DD5")

    QueueWorkItem2(0x105, 2, lambda_2DD5)

    ChrTalk(
        0x105,
        (
            "#11P#10302FHu hu...\x01",
            "It seems that won't be necessary.\x02",
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
            "──I'm sorry to have made you wait.\x01",
            "You're the ladies and gentlemen from the SSS, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_2EFD():

        label("loc_2EFD")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_2EFD")

    QueueWorkItem2(0x101, 2, lambda_2EFD)
    Sleep(50)

    def lambda_2F12():

        label("loc_2F12")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_2F12")

    QueueWorkItem2(0x104, 2, lambda_2F12)
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

    def lambda_2F7D():
        OP_95(0xFE, -4300, 5000, 10000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2F7D)
    WaitChrThread(0x13, 1)

    def lambda_2F9B():
        OP_95(0xFE, 1000, 5000, 11000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2F9B)
    WaitChrThread(0x13, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x105, 0x2)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00011FAh──\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10101F!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FI-It's really...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00305FOoh, you're the miss who the\x01",
            "ladies were kicking a fuss for...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#07105F#5P...?\x02\x03",
            "#07104FOh, please forgive me.\x01",
            "You were at the unveiling ceremony too?\x02",
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
            "──I'm sorry for the\x01",
            "late introduction.\x02\x03",
            "Liberl Royal Army, Royal Elite\x01",
            "Guards, Captain Julia Schwarz.\x02\x03",
            "By order of Her Highness Klaudia,\x01",
            "allow me to guide you all to the\x01",
            ""Arseille" now.\x02\x03",
            "Please follow me.\x02",
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

    # Function_21_27F7 end

    def Function_22_3276(): pass

    label("Function_22_3276")

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
            "#00000FExcuse us, are you from\x01",
            "the "Capua Express"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Yeah, I am...\x01",
            "Who're you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FCrossbell Police,\x01",
            "Special Support Section.\x02\x03",
            "We saw your request and\x01",
            "came to inquire about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Ooh, you're them then!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Man, thanks.\x01",
            "I'm totally in a bind here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "It's a job that's gonna require a tiny bit of time...\x01",
            "Will you accept it?\x02",
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

    # Function_22_3276 end

    def Function_23_34C7(): pass

    label("Function_23_34C7")

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
        (
            "Oh, could it be\x01",
            "that you're free?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "It's a job that's gonna require a tiny bit of time...\x01",
            "Will you accept it?\x02",
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

    # Function_23_34C7 end

    def Function_24_3633(): pass

    label("Function_24_3633")

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
            "[Quit]\x01",        # 1
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
        (0, "loc_3693"),
        (1, "loc_369B"),
        (SWITCH_DEFAULT, "loc_3739"),
    )


    label("loc_3693")

    Call(0, 25)
    Jump("loc_3739")

    label("loc_369B")


    ChrTalk(
        0x101,
        (
            "#00006FI'm sorry, we\x01",
            "aren't free now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Oh, is that so?\x01",
            "Oh, man...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Then, if you free yourselves,\x01",
            "come talk to me again, eh!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x175, 4)
    Jump("loc_3739")

    label("loc_3739")

    Return()

    # Function_24_3633 end

    def Function_25_373A(): pass

    label("Function_25_373A")


    ChrTalk(
        0x101,
        "#00000FYes, please leave it to us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FIf I'm correct, the request was about\x01",
            "misdelivered packages or something...\x02",
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
            "We fly all over the continent\x01",
            "delivering packages to all\x01",
            "kind of places, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "This time, we made a blunder with\x01",
            "the packages delivered here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "It appears the destinations were\x01",
            "reverted and a few packages were\x01",
            "delivered to the wrong places.\x02",
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
            "#00206FI think it doesn't happen many\x01",
            "times to mistake slips, but...\x02",
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
            "Such a thing has happened\x01",
            "some times until now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "At worst, she affixes letters\x01",
            "from her friends instead of\x01",
            "the sales slips...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FAhaha...\x01",
            "Your president seems\x01",
            "to be a careless person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Well, I respect her though.\x01",
            "She took us in when we\x01",
            "had nowhere to go...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "...*cough*, sorry.\x01",
            "I strayed from the subject.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "In short, I want to ask you to redeliver\x01",
            "the packages that were wrongly delivered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "After they're received at the autonomous state,\x01",
            "they're always entrusted to a local shipping\x01",
            "company, but we aren't familiar with the place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FI see, I understand\x01",
            "the situation.\x02\x03",
            "#10302FWere you able to grasp the whereabouts\x01",
            "of the misdelivered packages?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Uhhm, according to what I\x01",
            "could confirm, let's see...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "A package addressed to St. Ursula was\x01",
            "delivered to the "Der Ziegel" Inn in Mainz..\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Then, it seems that a package meant\x01",
            "for a private house in Residential Street\x01",
            "in the city went to St. Ursula Hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "I want you to go around those places, \x01",
            "recover the misdelivered packages and\x01",
            "deliver the intended goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "...And so,\x01",
            "take these.\x02",
        )
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
            "originally should've been\x01",
            "delivered to "Der Ziegel".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FAs for this slip, it is the one that\x01",
            "originally should have been attached to\x01",
            "the package delivered to the hospital...\x02",
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
            "First of all, deliver this small \x01",
            "package to the "Der Ziegel" Inn\x01",
            "or whatever it's called.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Because the package addressed to\x01",
            "St. Ursula Hospital should be there,\x01",
            "you take that and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "...Somehow, saying it myself\x01",
            "I don't get it anymore.\x02",
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
            "#00003FI-In any case...\x01",
            "It's all right to exchange\x01",
            "the packages in order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Yes, well, exactly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "I'm sorry that's a bother,\x01",
            "but I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYes, understood.\x02\x03",
            "#00000F...Then, let's go to the\x01",
            "Mainz "Der Ziegel" Inn\x01",
            "at once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FOh man, seems it's gonna\x01",
            "be quite the painstakin' job.\x02",
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
            "Quest [Redelivering the Misdeliveries]\x07\x00",
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

    # Function_25_373A end

    def Function_26_42C3(): pass

    label("Function_26_42C3")

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
            "Ooh, it seems you've properly delivered\x01",
            "the packages to the correct destinations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Maaan, what a help you've been.\x01",
            "Really, thanks a bunch, Support Section.\x02",
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
            "That miss...\x01",
            "Isn't her face color somehow bad?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#1S*mumble mumble*...\x01",
            "We spoke to a spirit...\x02",
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
        "#10309FHu hu, it seems it was quite the shock.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FI understand how she feels...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FWell, in time she'll calm down.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FE-Ehhm...\x01",
            "That being the case,\x01",
            "please don't mind it.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x11, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x11,
        (
            "Really?\x01",
            "Well, alright...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Then, I'll be\x01",
            "leaving now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "If something comes up again,\x01",
            "I'll be counting on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, whenever you want.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FWe will look forward to it.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4767")
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

    label("loc_4767")

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
            "Quest [Redelivering the Misdeliveries]\x07\x00",
            " completed!\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4818")
    EventEnd(0x5)
    NewScene("c0000", 103, 0, 0)
    IdleLoop()
    Jump("loc_482F")

    label("loc_4818")

    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 6600, 0, -5000, 0)
    EventEnd(0x5)

    label("loc_482F")

    Return()

    # Function_26_42C3 end

    def Function_27_4830(): pass

    label("Function_27_4830")

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
        "*sigh*, what should I do...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If I had been more careful,\x01",
            "such a thing would've never...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FExcuse us...\x01",
            "Has something happened?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_49A6():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_49A6)
    Sleep(10)

    def lambda_49B6():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_49B6)
    WaitChrThread(0xA, 2)
    Sleep(500)

    ChrTalk(
        0x12,
        (
            "Ooh, you're the Special Support Section...\x01",
            "Actually, something troublesome happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Today, the plan was to deliver \x01",
            "medical goods from Remiferia \x01",
            "to St. Ursula Hospital, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "It appears that some guy\x01",
            "cheated out those.\x02",
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
        "#00105FHe cheated out medical goods...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yeah... Just some time ago,\x01",
            "a man who said to be from a\x01",
            "shipping company came here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "He used a plausible reason, saying that\x01",
            "he took the goods transport instead of\x01",
            "the Rhymes Shipping that couldn't come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "He didn't seem a person who\x01",
            "was lying at all, so I readily\x01",
            "handed over the packages.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "However, I too didn't remember a letter of proxy \x01",
            "like that having been sent anywhere else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "So, I noticed that the goods had been\x01",
            "cheated out while talking about this and that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FHmm... The point is, that letter\x01",
            "of proxy was a counterfeit, is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10301FIn any case, that's quite an ill-\x01",
            "conditioned man cheating out medical\x01",
            "goods in such a time of crisis.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108FAlthough there're a lot of injured people\x01",
            "from that raid incident hospitalized...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FThat's because medical goods like\x01",
            "those would sell well in the black market\x01",
            "fetchin' quite an amount of mira.\x02\x03",
            "#00301FBasically a sly looter with\x01",
            "mira as his purpose, hm?\x02",
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
        "Still, what a problem it is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "At St. Ursula Hospital\x01",
            "are currently waiting\x01",
            "for the goods, and yet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yeah, it's totally my fault...\x01",
            "If I had at least checked\x01",
            "with the Rhymes Shipping...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0xA, 500)

    ChrTalk(
        0x12,
        (
            "No... It's not your fault.\x01",
            "No matter how you look at it, the one at\x01",
            "fault is the guy who cheated out the packages.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x12, 0x101, 500)

    ChrTalk(
        0x12,
        (
            "Oh, right... Couldn't you\x01",
            "search for the culprit who\x01",
            "cheated out the medical goods?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "I'd like you to catch him in a way\x01",
            "or another, even for the sake of\x01",
            "St. Ursula Hospital patients.\x02",
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

    # Function_27_4830 end

    def Function_28_51C3(): pass

    label("Function_28_51C3")

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
            "The culprit who cheated out the medical goods...\x01",
            "Won't you search for him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "I'd like you to catch him in a way\x01",
            "or another, even for the sake of\x01",
            "St. Ursula Hospital patients.\x02",
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

    # Function_28_51C3 end

    def Function_29_5385(): pass

    label("Function_29_5385")

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
            "Quit\x01",        # 1
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
        (0, "loc_53E1"),
        (1, "loc_53E9"),
        (SWITCH_DEFAULT, "loc_54B7"),
    )


    label("loc_53E1")

    Call(0, 30)
    Jump("loc_54B7")

    label("loc_53E9")


    ChrTalk(
        0x101,
        (
            "#00003FI'm sorry...\x01",
            "We've got some pressing business now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I-I see...\x01",
            "Then it can't be helped...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "If you can find the time,\x01",
            "speak to me again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "I can only count on you all.\x01",
            "Please.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19B, 6)
    Jump("loc_54B7")

    label("loc_54B7")

    Return()

    # Function_29_5385 end

    def Function_30_54B8(): pass

    label("Function_30_54B8")


    ChrTalk(
        0x101,
        (
            "#00003F...It seems that not much time \x01",
            "has passed since the incident yet...\x01",
            "If we hurry, we could make it in time.\x02\x03",
            "#00000FPlease leave it to us for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Ooh...I owe you one!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FHowever, it seems our opponent\x01",
            "has already finished his job...\x01",
            "It seems we should really hurry up.\x02\x03",
            "#00101FWasn't there any clue that\x01",
            "indicate the culprit destination?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Let's see...\x01",
            "I didn't see him,\x01",
            "so I couldn't say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Now that I think about it...\x01",
            "It seems that man was driving\x01",
            "a Reinford made black wagon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Even by his appearance he looked like\x01",
            "a well-dressed Imperial, so maybe...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301FIt's very likely he's trying to\x01",
            "escape towards the Empire\x01",
            "region like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103FIf that's the case, by\x01",
            "now he could be arriving\x01",
            "nearby Bellguard Gate.\x02\x03",
            "#10101FI think it would be better to chase him\x01",
            "by getting information about the wagon\x01",
            "along the way, just in case...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306FWell, it seems we can't do\x01",
            "this at leisure, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FIn any case...\x01",
            "Let's try chasing him.\x02\x03",
            "#00001FMr. Billy, Mr. Ricardo, please\x01",
            "wait here for us to contact you.\x02",
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
        "We're counting on you, everyone!\x02",
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
            "Quest [Medical Supplies Investigation]\x07\x00",
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

    # Function_30_54B8 end

    SaveToFile()

Try(main)
