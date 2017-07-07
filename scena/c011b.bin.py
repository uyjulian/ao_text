from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c011b.bin",                # FileName
        "c011b",                    # MapName
        "c011b",                    # Location
        0x0009,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 9, 0, 2, 0, 3],
    )

    BuildStringList((
        "c011b",                  # 0
        "Sergey Manager",           # 1
        "Zeit",               # 2
        "Keya",                 # 3
        "Charlie",             # 4
        "Dudley investigator",         # 5
        "Citizen",                   # 6
        "Citizen",                   # 7
        "Citizen",                   # 8
        "Citizen",                   # 9
        "Citizen",                   # 10
        "Policeman",                   # 11
        "Dishes",                   # 12
        "Dishes",                   # 13
        "Dishes",                   # 14
        "Dishes",                   # 15
        "Dishes",                   # 16
        "Dishes",                   # 17
        "Dishes",                   # 18
        "Dishes",                   # 19
        "Dishes",                   # 20
        "Dishes",                   # 21
        "Dishes",                   # 22
        "Dishes",                   # 23
        "Dishes",                   # 24
        "Dishes",                   # 25
        "Dishes",                   # 26
        "Dishes",                   # 27
        "Dishes",                   # 28
        "Dishes",                   # 29
        "Dishes",                   # 30
        "Chair",                   # 31
        "Chair",                   # 32
        "Chair",                   # 33
        "Chair",                   # 34
        "Chair",                   # 35
        "Chair",                   # 36
        "Chair",                   # 37
        "Chair",                   # 38
    ))

    AddCharChip((
        "chr/ch02500.itc",                   # 00
        "chr/ch02502.itc",                   # 01
        "chr/ch08200.itc",                   # 02
        "chr/ch08202.itc",                   # 03
        "chr/ch02707.itc",                   # 04
        "chr/ch02708.itc",                   # 05
        "chr/ch02702.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   4,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   2,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(170000,  0,       63560,   1500,    170000,  1500,    63560,   0x007C, 0,  7,  0x0000)
    DeclActor(16960,   850,     10840,   2000,    16960,   1300,    10840,   0x007C, 0,  25, 0x0000)

    ChipFrameInfo(1512, 0)                                       # 0

    ScpFunction((
        "Function_0_5E8",          # 00, 0
        "Function_1_698",          # 01, 1
        "Function_2_6B4",          # 02, 2
        "Function_3_7DE",          # 03, 3
        "Function_4_83F",          # 04, 4
        "Function_5_994",          # 05, 5
        "Function_6_B4A",          # 06, 6
        "Function_7_DCF",          # 07, 7
        "Function_8_E10",          # 08, 8
        "Function_9_2E85",         # 09, 9
        "Function_10_2F14",        # 0A, 10
        "Function_11_4986",        # 0B, 11
        "Function_12_49B4",        # 0C, 12
        "Function_13_4A05",        # 0D, 13
        "Function_14_4A56",        # 0E, 14
        "Function_15_4AAE",        # 0F, 15
        "Function_16_4AF8",        # 10, 16
        "Function_17_4B1E",        # 11, 17
        "Function_18_5426",        # 12, 18
        "Function_19_5463",        # 13, 19
        "Function_20_673B",        # 14, 20
        "Function_21_8A44",        # 15, 21
        "Function_22_8AB4",        # 16, 22
        "Function_23_9DA3",        # 17, 23
        "Function_24_ADCA",        # 18, 24
        "Function_25_B8DB",        # 19, 25
        "Function_26_BFC4",        # 1A, 26
    ))


    def Function_0_5E8(): pass

    label("Function_0_5E8")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_620"),
        (1, "loc_62C"),
        (2, "loc_638"),
        (3, "loc_644"),
        (4, "loc_650"),
        (5, "loc_65C"),
        (6, "loc_668"),
        (SWITCH_DEFAULT, "loc_674"),
    )


    label("loc_620")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_680")

    label("loc_62C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_680")

    label("loc_638")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_680")

    label("loc_644")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_680")

    label("loc_650")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_680")

    label("loc_65C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_680")

    label("loc_668")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_680")

    label("loc_674")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_680")

    label("loc_680")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_697")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_680")

    label("loc_697")

    Return()

    # Function_0_5E8 end

    def Function_1_698(): pass

    label("Function_1_698")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6B3")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_1_698")

    label("loc_6B3")

    Return()

    # Function_1_698 end

    def Function_2_6B4(): pass

    label("Function_2_6B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_72E")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 14400, 850, 12500, 0)
    BeginChrThread(0x8, 0, 0, 0)
    ClearChrFlags(0x8, 0x40)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrPos(0xA, 5570, 150, 6230, 180)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x5)
    SetChrPos(0x9, 2880, 0, 1750, 225)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0x9, 0x40)

    label("loc_72E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_742")
    ClearScenarioFlags(0x22, 0)
    Event(0, 8)
    Jump("loc_7DD")

    label("loc_742")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_756")
    ClearScenarioFlags(0x22, 1)
    Event(0, 10)
    Jump("loc_7DD")

    label("loc_756")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_76A")
    ClearScenarioFlags(0x22, 2)
    Event(0, 17)
    Jump("loc_7DD")

    label("loc_76A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_77E")
    ClearScenarioFlags(0x22, 3)
    Event(0, 19)
    Jump("loc_7DD")

    label("loc_77E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_792")
    ClearScenarioFlags(0x22, 4)
    Event(0, 20)
    Jump("loc_7DD")

    label("loc_792")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_7A9")
    ClearScenarioFlags(0x22, 5)
    SetScenarioFlags(0x0, 4)
    Event(0, 22)
    Jump("loc_7DD")

    label("loc_7A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_7BD")
    ClearScenarioFlags(0x22, 6)
    Event(0, 23)
    Jump("loc_7DD")

    label("loc_7BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 7)), scpexpr(EXPR_END)), "loc_7CE")
    ClearScenarioFlags(0x22, 7)
    Jump("loc_7DD")

    label("loc_7CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 0)), scpexpr(EXPR_END)), "loc_7DD")
    ClearScenarioFlags(0x23, 0)
    Event(0, 24)

    label("loc_7DD")

    Return()

    # Function_2_6B4 end

    def Function_3_7DE(): pass

    label("Function_3_7DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_7F3")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x203), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 4)

    label("loc_7F3")

    SetMapObjFlags(0x19, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_816")
    SetMapObjFrame(0xFF, "asihuki", 0x0, 0x1)
    Jump("loc_825")

    label("loc_816")

    SetMapObjFrame(0xFF, "asihuki", 0x1, 0x1)

    label("loc_825")

    ClearMapObjFlags(0x6, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_83E")
    SetMapObjFlags(0x6, 0x10)
    OP_65(0x0, 0x1)

    label("loc_83E")

    Return()

    # Function_3_7DE end

    def Function_4_83F(): pass

    label("Function_4_83F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_91C")

    ChrTalk(
        0x8,
        (
            "#01000FI got information on terrorists\x01",
            "Contact the mayor and the guard.\x02\x03",
            "Dudley, our folks\x01",
            "I ordered a talisman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00603FWell, please leave it to me.\x02\x03",
            "#00601F… …. Come on, you guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_990")

    label("loc_91C")


    ChrTalk(
        0x8,
        (
            "#01000FAt the Geo Front\x01",
            "I do not know what happened,\x01",
            "At best, be careful.\x02\x03",
            "Dudley, our folks\x01",
            "I ordered a talisman.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_990")

    TalkEnd(0xFE)
    Return()

    # Function_4_83F end

    def Function_5_994(): pass

    label("Function_5_994")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ADC")

    ChrTalk(
        0xA,
        (
            "#01100FEveryone, please tell me.\x02\x03",
            "#01109FWell, please be careful of Dudley too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#00603FSo let's stop byhand … …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#01105FHmm?\x02",
    )

    CloseMessageWindow()
    OP_63(0x10A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x10A,
        (
            "#00606F…… Yeah, that's enough!\x01",
            "You guys are going quickly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F(Well, truly Dadley also\x01",
            "  Keyaには敵わないか。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_B46")

    label("loc_ADC")


    ChrTalk(
        0xA,
        (
            "#01109FEveryone, please tell me.\x02\x03",
            "Well, please be careful of Dudley too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#00603F(Exactly … …)\x02",
    )

    CloseMessageWindow()

    label("loc_B46")

    TalkEnd(0xFE)
    Return()

    # Function_5_994 end

    def Function_6_B4A(): pass

    label("Function_6_B4A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DAA")

    ChrTalk(
        0x9,
        "#01200FGururururu …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00603FHun, it is as great a wolf as ever.\x02\x03",
            "#00600FBut above being a police dog\x01",
            "You may borrow that power.\x01",
            "Prepare to be ready at any time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01200F……won.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C4B")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_C4B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C7F")
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_C7F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CB3")
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_CB3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CE7")
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_CE7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D1B")
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_D1B")

    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#00306F(Might be great,\x01",
            "You can not tell anyone else … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(Hehe, Mr. Dudley's\x01",
            "I guess it is a way of encouragement. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_DCB")

    label("loc_DAA")


    ChrTalk(
        0x9,
        "#01200FGurururu …… won.\x02",
    )

    CloseMessageWindow()

    label("loc_DCB")

    TalkEnd(0xFE)
    Return()

    # Function_6_B4A end

    def Function_7_DCF(): pass

    label("Function_7_DCF")

    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00000FThis is the room of Tio.\x01",
            "Let's stop entering.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_7_DCF end

    def Function_8_E10(): pass

    label("Function_8_E10")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis120.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis124.itp")
    CreatePortrait(3, 176, 36, 304, 164, 0, 0, 512, 256, 0, 0, 128, 128, 0xFFFFFF, 0x0, "c_vis239.itp")
    OP_68(14100, 1750, 12300, 0)
    MoveCamera(40, 17, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(22000, 0)
    OP_90(0x101, 1700, 850, 14100, 180)
    OP_90(0x102, 600, 4850, 14400, 180)
    OP_90(0x153, 1700, 4850, 15400, 180)
    OP_90(0x109, 600, 4850, 15700, 180)
    OP_90(0x105, 1700, 4850, 16700, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x153, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 14100, 850, 12300, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x9, 0x5)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, 13100, 850, 9300, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SoundLoad(98)
    SoundLoad(2668)
    ClearMapObjFlags(0x19, 0x4)
    SetMapObjFlags(0x19, 0x1000)
    OP_70(0x19, 0x32)
    SetCameraDistance(24000, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x8,
        (
            "#01003F#11PHmm, Hm …\x02\x03",
            "#01000FThat's right.\x01",
            "It will come back soon ──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(3054, 255, 80, 0)

    ChrTalk(
        0x9,
        "#01200F#12Pwon.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x8, 0x10E, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#01005F#11P…… Oops.\x01",
            "I just came back.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x101,
        "Voice of Lloyd",
        "I'm home.\x02",
    )

    CloseMessageWindow()
    OP_68(4100, 1750, 10400, 2500)
    SetCameraDistance(25000, 2500)
    Sleep(1000)
    OP_90(0x101, 1700, 4850, 14100, 180)
    BeginChrThread(0x101, 3, 0, 9)

    def lambda_1141():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1141)
    Sleep(400)

    def lambda_1155():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1155)
    Sleep(600)

    def lambda_1169():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x153, 2, lambda_1169)
    Sleep(400)

    def lambda_117D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_117D)
    Sleep(600)

    def lambda_1191():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_1191)
    WaitChrThread(0x101, 0)

    def lambda_11A6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_11A6)
    WaitChrThread(0x102, 0)

    def lambda_11B7():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_11B7)
    WaitChrThread(0x153, 0)

    def lambda_11C8():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x153, 2, lambda_11C8)
    WaitChrThread(0x109, 0)

    def lambda_11D9():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_11D9)
    WaitChrThread(0x105, 0)

    def lambda_11EA():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_11EA)

    ChrTalk(
        0x153,
        "#5P#01110FColloquium, I'm home.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105FOh, are you communicating?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#01004F#12PNo, no problem.\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x0, 0x1F4)
    Sleep(300)
    Sound(838, 0, 100, 0)
    SetMapObjFlags(0x19, 0x4)
    Sleep(500)
    OP_93(0x8, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#01002F#6PSky, barely\x01",
            "Try starting the terminal there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FHuh, yes … ….?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FFrom the police headquarters\x01",
            "Do you have a contact?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01003F#6PYou can tell by starting it.\x02\x03",
            "#01001FHere, with newcomers\x01",
            "Keyaもこっちに来い。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#5P#01100FHmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10105FYes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FThere seems to be something.\x02",
    )

    CloseMessageWindow()

    def lambda_13BA():
        OP_97(0x101, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_13BA)
    Sleep(250)

    def lambda_13D7():
        OP_97(0x153, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 0, lambda_13D7)
    Sleep(250)

    def lambda_13F4():
        OP_97(0x102, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_13F4)
    Sleep(250)

    def lambda_1411():
        OP_97(0x109, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1411)
    Sleep(100)
    Fade(1000)
    OP_68(16300, 1750, 10200, 0)
    MoveCamera(13, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    EndChrThread(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    EndChrThread(0x153, 0xFF)
    SetChrSubChip(0x153, 0x0)
    EndChrThread(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    EndChrThread(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrPos(0x101, 16300, 850, 10200, 45)
    SetChrPos(0x102, 14800, 850, 9500, 45)
    SetChrPos(0x153, 15250, 850, 8500, 45)
    SetChrPos(0x109, 16200, 850, 7400, 0)
    SetChrPos(0x105, 17200, 850, 7800, 0)
    SetChrPos(0x8, 14200, 850, 11900, 135)
    SetChrPos(0x9, 13100, 850, 8900, 45)
    OP_68(16800, 1750, 10700, 2000)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#5P#00001FEr …\x02",
    )

    CloseMessageWindow()
    Sound(836, 0, 100, 0)
    Sleep(1200)
    StopBGM(0xBB8)
    Sound(72, 0, 100, 0)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(500)
    OP_CB(0x3, 0x1, 0x3E8, 0x0, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0x0, 0x17700, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0xFA, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sound(1021, 0, 100, 0)
    OP_CB(0x3, 0x0, 0x0, 0x0, 0xFA, 0x0)
    OP_CB(0x3, 0x1, 0x3E8, 0x3E8, 0xFA, 0x0)
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0xFA, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    Sleep(300)

    AnonymousTalk(
        0x101,
        "#00005FIt is! It is!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        "#00105FTio!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x153,
        "#01109FOh, Tio!\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7515", 0)
    Sleep(500)
    SetMessageWindowPos(-1, 150, -1, -1)
    OP_C9(0x0, 0x80000000)
    SetChrName("Tio")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2668V#40W……Good evening.\x01",
            "It is long time no see.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xA6C)
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x101,
        (
            "#00002FTio……！\x01",
            "Why on earth …?\x02\x03",
            "Possibly to crossbell\x01",
            "Are you coming home! Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x3, 0x8, 0x100, 0x0, 0x180, 0x80)
    OP_0D()
    Sound(2273, 255, 100, 0)
    Sleep(800)
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("Tio")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30W…… Still in Leman Autonomous Region\x01",
            "I am in the Institute of the Epstein Foundation.\x02\x03",
            "There is more to go home than planned\x01",
            "Because it seems to be a little late ……\x02\x03",
            "Say a selfish line\x01",
            "I used it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x101,
        "#00000FI see……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00109FTioちゃん……\x01",
            "I'm glad to see your face.\x02\x03",
            "#00105FOh, but it's a power net\x01",
            "In the network outside autonomous province\x01",
            "I can not connect it … ….?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x3, 0x8, 0x80, 0x0, 0x100, 0x80)
    OP_0D()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("Tio")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Yes, if you do not connect by wired\x01",
            "We can not process huge amounts of information.\x02\x03",
            "But now, between the Foundation and IBC\x01",
            "Experiments on remote connection are under way.\x02\x03",
            "Well, a powerful radio booster\x01",
            "Between Les Autonomous state and Crossbell autonomous state\x01",
            "About ten units are installed, but …\x02\x03",
            "That is why\x01",
            "That's why I can send it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x102,
        "#00102FWas it so……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        "#00004FThe progress of technology is amazing ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x153,
        (
            "#01110Fねえねえ、Tio！\x02\x03",
            "I told you I will be late\x01",
            "When are you coming back?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("Tio")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "At the end of the month or at the beginning of next month\x01",
            "I think that I can return to there.\x02\x03",
            "In the meantime,\x01",
            "この通信で溜めたKeya分で\x01",
            "I will do my best.\x02\x03",
            "だからKeya、\x01",
            "Please show me your face better.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x153,
        (
            "#01109FErr …… Well!\x02\x03",
            "#01110Fほらほら、Zeitも\x01",
            "Tioに顔を見せてあげてー。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x9,
        "#01200FUluru …… Won.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("Tio")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Yes, it's okay.\x01",
            "Because I am doing fine.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x101,
        "#00002Fmy mother……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00104FHuhu …… In the power net\x01",
            "There are also such benefits.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x3, 0x8, 0x180, 0x0, 0x200, 0x80)
    OP_0D()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("Tio")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "By the way, Randy also\x01",
            "I heard that he has not returned yet …\x02\x03",
            "Noel and Mr. Wasi\x01",
            "You seem to have participated already, are not you?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x101,
        (
            "#00000FOh, just starting today\x01",
            "I have my job started.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x109,
        (
            "#10102FHehu ……\x01",
            "Tioちゃん、お久しぶり！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x105,
        (
            "#10302FHello.\x01",
            "I'm getting in the way.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x3, 0x8, 0x80, 0x0, 0x100, 0x80)
    OP_0D()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("Tio")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Whatching\x01",
            "Both of you two years ago.\x02\x03",
            "Anyway, Mr. Noel\x01",
            "I am convinced that I have been seconded … …\x02\x03",
            "Waji-san is there\x01",
            "It is a mysterious sight.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x105,
        "#10309FAhaha, I think so too.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x109,
        (
            "#10106FAlready……\x01",
            "It's not a laughing thing.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00004FWell, well somehow for now\x01",
            "I will get on with this one.\x02\x03",
            "#00002FだけどTio……\x01",
            "Please come back soon!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00102Fええ、Tioちゃんがいないと\x01",
            "It is not a real support department.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x153,
        "#01109FYes!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x3, 0x8, 0x100, 0x0, 0x180, 0x80)
    OP_0D()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("Tio")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "So I can return early in the case …\x01",
            "I will try hard as well.\x02\x03",
            "Actually Jonah, too, for this communication\x01",
            "I thought about calling … ….\x02\x03",
            "It seems that it was continued all night\x01",
            "I did not get up even if I called.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x101,
        (
            "#00000FReally……\x01",
            "He seems to be doing his best.\x02\x03",
            "#00006FWell, damages given to the Foundation\x01",
            "It seems to be regaining it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00104FDo not strain too much\x01",
            "Take care.\x02\x03",
            "#00100FもちろんTioちゃんも\x01",
            "Do not push yourself?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x3, 0x8, 0x80, 0x0, 0x100, 0x80)
    OP_0D()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("Tio")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Yes, I understand.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(839, 0, 90, 0)
    Sleep(400)
    Sound(839, 0, 90, 0)
    Sleep(600)
    Sound(2274, 255, 50, 0)
    Fade(250)
    OP_CB(0x3, 0x8, 0x180, 0x0, 0x200, 0x80)
    OP_0D()
    Sleep(1500)
    Sound(2676, 255, 100, 0)
    Fade(250)
    OP_CB(0x3, 0x8, 0x0, 0x80, 0x80, 0x100)
    OP_0D()
    Sleep(1200)
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("Tio")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……Excuse me.\x01",
            "It looks like time is about to come.\x02\x03",
            "Impossibly to make a line for experiments\x01",
            "Because I am using it … ….\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x101,
        "#00001FI see……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00106FI would like to talk more\x01",
            "so sorry……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x8,
        (
            "#01004FWell, there are opportunities again.\x02\x03",
            "#01002FTio、そちらの予定が付いたら\x01",
            "Please contact me again.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x3, 0x8, 0x80, 0x0, 0x100, 0x80)
    OP_0D()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("Tio")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "OK.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 4)), scpexpr(EXPR_END)), "loc_2571")

    AnonymousTalk(
        0x101,
        (
            "#00004F……じゃあな、Tio。\x02\x03",
            "#00002FWhen you come back this time\x01",
            "Because I will keep promises at that time.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x3, 0x8, 0x80, 0x80, 0x100, 0x100)
    OP_0D()
    Sound(2275, 255, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("Tio")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Yes……\x01",
            "I am looking forward to it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x153,
        "#01111FYakseoku ~?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00104FI do not care what it is ….\x01",
            "Well, that would be nice.\x02\x03",
            "#00102FTioちゃん。\x01",
            "Please contact me again.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x3, 0x8, 0x80, 0x0, 0x100, 0x80)
    OP_0D()

    AnonymousTalk(
        0x109,
        (
            "#10109FTake care!\x01",
            "Beware of the body!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_2607")

    label("loc_2571")


    AnonymousTalk(
        0x101,
        (
            "#00002Fじゃあな、Tio。\x01",
            "Take care of yourself.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00102FIf it is ok\x01",
            "Please contact me again.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x109,
        "#10109FTioちゃん、元気でね！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2607")


    AnonymousTalk(
        0x105,
        "#10302FAdios, good night.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x9,
        "#01200FGuru …… Won.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x153,
        "#01110Fまたね〜、Tio！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x3, 0x8, 0x100, 0x0, 0x180, 0x80)
    OP_0D()
    Sound(2276, 255, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("Tio")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Well, see you then.\x01",
            "good night.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(1021, 0, 50, 0)
    Sound(939, 0, 50, 0)
    OP_CB(0x3, 0x0, 0x0, 0x17700, 0xFA, 0x0)
    OP_CB(0x3, 0x1, 0x3E8, 0x0, 0xFA, 0x0)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0xFA, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    Sleep(500)
    OP_24(0x3AB)
    Sound(73, 0, 100, 0)
    OP_68(16300, 1750, 10200, 2000)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0x153,
        "#6P#01106FI disappeared …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008FAh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00104F…… If you look at your face\x01",
            "I wanted to meet you more and more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10302FHuh, it's youth.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10109FHuh, the support department\x01",
            "You really are on good terms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FHello, it's not too bad at first\x01",
            "It was a relationship though.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#00000FThat's right, the section chief.\x01",
            "I'm sorry to be late.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_28C0():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_28C0)
    Sleep(50)

    def lambda_28D0():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_28D0)
    Sleep(50)

    def lambda_28E0():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_28E0)
    Sleep(50)

    def lambda_28F0():
        TurnDirection(0x153, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x153, 0, lambda_28F0)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x153, 0)

    ChrTalk(
        0x8,
        (
            "#01004FWell, that's good.\x02\x03",
            "#01000FFor today's report\x01",
            "As I will tell you later … …\x02\x03",
            "What's going on for dinner?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#11P#00011FWell, yes, I forgot!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#6P#00108FBy the way, with this member\x01",
            "I have not decided the duty yet …\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2A2E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2A2E)
    Sleep(100)

    def lambda_2A3E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x153, 2, lambda_2A3E)
    WaitChrThread(0x109, 2)

    ChrTalk(
        0x109,
        (
            "#6P#10105FThat's right, the Special Affairs Support Division\x01",
            "The meal is on course, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10305FWhat is it?\x02\x03",
            "#10306F……HM.\x01",
            "A little Mendozai dear.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12B, 3)), scpexpr(EXPR_END)), "loc_2BCF")

    ChrTalk(
        0x101,
        (
            "#00003FSince Wazi also entered the support section\x01",
            "It will be shared properly.\x02\x03",
            "#00000FIt seems to be possible to cook surprisingly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FWell, you can do it so much.\x02\x03",
            "#10300FBecause it is troublesome because of Abbas\x01",
            "Though there were many things to make.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CDB")

    label("loc_2BCF")


    ChrTalk(
        0x101,
        (
            "#00003FSince Wazi also entered the support section\x01",
            "It will be shared properly.\x02\x03",
            "#00000FI also got a new cookbook,\x01",
            "I will teach you when I'm not good at it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FIt's nice, but,\x01",
            "I can cook so much.\x02\x03",
            "#10309FBecause it is troublesome because of Abbas\x01",
            "Though there were many things to make.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CDB")


    ChrTalk(
        0x101,
        (
            "#00013FEh, if it's the case\x01",
            "Do not complain!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00109FHehe, well well today\x01",
            "Shall we try it all together?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10102FWell then, quickly\x01",
            "What looks good looks good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#6P#01109FKeyaも手伝うー！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01006F… …. Good luck.\x01",
            "I suppose I should wait while taking a dose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#6P#01203FGuru …… Won.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(24000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(1000)
    Sound(13, 0, 100, 0)
    Sleep(4000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(2000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    RemoveParty(0x52, 0xFF)
    OP_CC(0x1, 0xFF, 0x0)
    OP_32(0xFF, 0xFE, 0x0)
    SetScenarioFlags(0x22, 1)
    NewScene("c0120", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_8_E10 end

    def Function_9_2E85(): pass

    label("Function_9_2E85")


    def lambda_2E8A():
        OP_97(0x101, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2E8A)
    Sleep(200)

    def lambda_2EA7():
        OP_97(0x102, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2EA7)
    Sleep(200)

    def lambda_2EC4():
        OP_97(0x153, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 0, lambda_2EC4)
    Sleep(200)

    def lambda_2EE1():
        OP_97(0x109, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2EE1)
    Sleep(200)

    def lambda_2EFE():
        OP_97(0x105, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2EFE)
    Return()

    # Function_9_2E85 end

    def Function_10_2F14(): pass

    label("Function_10_2F14")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch03400.itc", 0x1E)
    LoadChrToIndex("apl/ch51201.itc", 0x1F)
    LoadChrToIndex("apl/ch50091.itc", 0x20)
    LoadChrToIndex("chr/ch02710.itc", 0x21)
    SoundLoad(3942)
    SoundLoad(3943)
    SoundLoad(3944)
    SoundLoad(3945)
    SoundLoad(3946)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04601.itp")
    SetChrPos(0x101, 1200, 0, -2000, 0)
    SetChrPos(0x102, 300, 0, -1800, 0)
    SetChrPos(0x104, 2700, 0, 5000, 90)
    SetChrPos(0x109, 1200, 0, -2300, 0)
    SetChrPos(0x105, 300, 0, -2100, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xB, 0x1F)
    SetChrSubChip(0xB, 0x3)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xB, 0x2)
    SetChrFlags(0xB, 0x20)
    SetChrPos(0xB, 5300, 150, 6250, 180)
    OP_52(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 0x6)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 900, 0, -3000, 0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 700, 0, -2500, 0)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x13, 0x20)
    SetChrSubChip(0x13, 0x1D)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 5300, 330, 4600, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    OP_68(5300, 900, 6250, 0)
    MoveCamera(50, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    SetCameraDistance(24000, 3000)
    StopBGM(0xFA0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_68(4000, 1000, 5250, 2500)
    MoveCamera(40, 19, 0, 2500)
    BeginChrThread(0x104, 3, 0, 11)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#12P#00011FI mean …!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 3)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x105, 3)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        "#6P#00105FRandy's cousin#4Rcousin#of……\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7561", 0)
    SetChrSubChip(0xB, 0x4)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xB,
        (
            "#11P#04609F#3942V#30WEh, thank you.\x01",
            "Charlie・オルランドでーす。\x02\x03",
            "#04602F#3943VI guess it was late.\x01",
            "I was tired of waiting.\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF67)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#6P#00301F#30W……you……\x02\x03",
            "What on earth did you come to …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11P#04605FOh, I'm sorry, Randy elder brother.\x02\x03",
            "#04606FTo cute cute Itoko after 2 years\x01",
            "Is not she a bit nervous?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303F#30WPlease answer, okay ….\x01",
            "I came to see what it was.\x02\x03",
            "#00311FNo, what did you do here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#11P#04604FHehu ……\x02",
    )

    CloseMessageWindow()
    Fade(800)
    SetCameraDistance(22800, 800)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_6F(0x79)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0xB,
        (
            "#3944V#40W── It's lukewarm, Randy's older brother#2RHiud#.\x02\x03",
            "#3945V#30WAfter setting up an interpersonal trap\x01",
            "It was minced at the moment I entered?\x02\x03",
            "#3946VSince when\x01",
            "I got through to it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xF6A)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_C9(0x1, 0x80000000)

    ChrTalk(
        0x104,
        "#6P#00311F#30W…………………………………….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00101FOh, you …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#N#10107FSuddenly what … …!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0xB,
        (
            "#11P#04612FHuh, you do not have to worry\x01",
            "There is no trap or anything.\x02\x03",
            "#04602FRandy if I was alone\x01",
            "Such play was also ant.\x02\x03",
            "#04604FUnless it is \"during the war\"\x01",
            "Because ordinary people do not want to involve them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00110FWell …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#01105F#6P#NBarking ……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#6P#N#10306FFuu …\x01",
            "This is an extreme child again.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#12P#00003F── You.\x01",
            "Charlieといったか。\x02\x03",
            "#00001Fagain……\x01",
            "It is Lloyd · Bannings of support section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11P#04602FThanks.\x02\x03",
            "#04609FIs not that a while ago?\x01",
            "Just chew your earlobe ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006F…… Anyway it is.\x02\x03",
            "#00013FThis is a crossbar police section\x01",
            "Even that sofa where you sit is\x01",
            "Burden by public expense#2RFake#I was something.\x02\x03",
            "It's a trap but I get involved …\x01",
            "An inadvertent remark in front of a child\x01",
            "Should we hold back?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11P#04612FHaha, I'm sorry.\x02\x03",
            "#04611FBecause I felt nostalgic\x01",
            "brother#2RHiud#I'm hanging out with Jarrett ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306F…… Hun.\x01",
            "Are you a Tama who knows me?\x02\x03",
            "#00301FOita, with your uncle's use\x01",
            "I wonder if you came to call me?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_3994():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3994)
    Sleep(50)

    def lambda_39A4():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_39A4)
    Sleep(50)

    def lambda_39B4():
        TurnDirection(0x109, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_39B4)
    Sleep(50)

    def lambda_39C4():
        TurnDirection(0x105, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_39C4)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        "#12P#00005FHuh……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00101Fthat's……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#11P#04604FHuh, you got the correct answer.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(4000, 800, 5250, 800)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xB, 0x2)
    ClearChrFlags(0xB, 0x20)
    Sound(802, 0, 100, 0)
    OP_9D(0xB, 0x14B4, 0x1E, 0x157C, 0x1F4, 0xBB8)
    OP_93(0xB, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#04602F#11PDaddy was saying that, right?\x01",
            "I have a story.\x02\x03",
            "I will be busy from tomorrow,\x01",
            "How about per tonight.\x02\x03",
            "#04605FOh, may I refuse it separately?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FHappy, if you refuse\x01",
            "means#4R噵 噵#You do not choose it, do you?\x02\x03",
            "#00311FIt is a prospect.\x01",
            "…… your way of doing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#04609F#11PHeh.\x01",
            "It seems that the situation has returned.\x02\x03",
            "#04602FDad is \"Neue-Blanc\"\x01",
            "I do it first, what do you do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00304FHuh, that would be nice.\x02",
    )

    CloseMessageWindow()
    OP_68(4100, 800, 5360, 1000)
    BeginChrThread(0xA, 3, 0, 16)
    Sleep(150)
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#5P#00300FEveryone is bad\x01",
            "Dinner is without me ─\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x79)
    WaitChrThread(0xA, 3)

    ChrTalk(
        0xA,
        (
            "#6P#01101FHey Hey, Randy.\x02\x03",
            "This older sister,\x01",
            "Probably a bad person?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_3D4A():
        TurnDirection(0x104, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3D4A)
    Sleep(50)

    def lambda_3D5A():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3D5A)
    Sleep(50)

    def lambda_3D6A():
        TurnDirection(0x102, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3D6A)
    Sleep(50)

    def lambda_3D7A():
        TurnDirection(0x109, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3D7A)
    Sleep(50)

    def lambda_3D8A():
        TurnDirection(0x105, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3D8A)
    Sleep(50)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        "#11P#00011Fちょ、Keya……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00107FKeyaちゃん、下がって……！\x02",
    )

    CloseMessageWindow()
    OP_68(3920, 800, 5320, 1000)
    MoveCamera(42, 20, 0, 1000)
    OP_6E(400, 1000)
    SetCameraDistance(24000, 1000)

    def lambda_3E2B():
        OP_95(0xFE, 1400, 0, 5500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3E2B)
    Sleep(300)

    def lambda_3E48():
        OP_95(0xFE, 1800, 0, 4300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3E48)
    WaitChrThread(0x102, 1)

    def lambda_3E66():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3E66)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0xA, 500)

    def lambda_3E7E():
        OP_96(0xFE, 0x1F4, 0x0, 0x13EC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3E7E)

    def lambda_3E98():
        OP_96(0xFE, 0x384, 0x0, 0xF3C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3E98)

    def lambda_3EB2():
        OP_96(0xFE, 0x3E8, 0x0, 0x12C0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3EB2)
    Sleep(300)

    def lambda_3ECF():
        OP_95(0xFE, 1300, 0, 2700, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3ECF)
    Sleep(300)

    def lambda_3EEC():
        OP_95(0xFE, 2200, 0, 2500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3EEC)
    WaitChrThread(0x101, 1)

    def lambda_3F0A():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3F0A)

    ChrTalk(
        0xB,
        (
            "#04606F#11PBad people are terrible.\x02\x03",
            "#04605FI wonder what that child! Is it?\x01",
            "It's not cute! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#6P#01105FHmm?\x02",
    )

    CloseMessageWindow()

    def lambda_3F8A():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3F8A)
    Sleep(100)

    def lambda_3F9A():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3F9A)

    def lambda_3FA7():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_3FA7)
    WaitChrThread(0x104, 2)
    Sleep(150)

    ChrTalk(
        0x104,
        (
            "#6P#00303FIt is a baby custody in my house.\x02\x03",
            "#00312F#30W──If you give out your hands, will you kill it?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x32, 0x0, 0xBB8, 0x96)

    ChrTalk(
        0x101,
        "#6P#00013F……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00108FWell …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#04612F#11PHaha, I understand.\x02\x03",
            "#04602FAt least this building\x01",
            "I will stop blowing up.\x02\x03",
            "#04609FOh, it's a joke, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10106F(What a conversation ……)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10308F(This is bad for your heart.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#5P#00304F─ ─ Well, that's it\x01",
            "My uncle comes out to Toko.\x02\x03",
            "#00300FI will be back tonight.\x01",
            "Do not worry so much.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_419E():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_419E)

    ChrTalk(
        0x102,
        "#6P#00108FBut, it is …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10101FIndeed it's dangerous …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006F── Hey, Randy.\x02\x03",
            "#00000FWell, me too\x01",
            "May I ask you a greeting?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(800)

    def lambda_42C8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_42C8)
    Sleep(50)

    def lambda_42D8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_42D8)
    Sleep(50)

    def lambda_42E8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_42E8)
    Sleep(50)

    def lambda_42F8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_42F8)
    Sleep(50)

    def lambda_4308():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4308)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x104,
        "#5P#00305FIt is! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00107FWhat! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#11P#10111FRo, Mr. Lloyd … …! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00004FOnce, as a leader of the support department\x01",
            "Greeting to a colleague's family\x01",
            "It will be courtesy.\x02\x03",
            "#00000FAnd a high class club\x01",
            "It is going to be a good social study.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#04611F#11PWow … interesting, older brother.\x02\x03",
            "#04609FIt's a nice little girl,\x01",
            "Come along as I'm worried ♪\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0xB, 500)
    Sleep(150)

    ChrTalk(
        0x105,
        (
            "#6P#10304FHuh, if I were you\x01",
            "I wonder if you can join us.\x02\x03",
            "#10302FExclusive club \"Neue-Bran\" … ….\x01",
            "I wanted to play once.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x105, 500)

    ChrTalk(
        0xB,
        (
            "#04612F#11PA beautiful older brother please!\x02\x03",
            "#04605Fthat……\x01",
            "Probably your sister?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10309FHuh, that was my brother.\x01",
            "It seems to be getting on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00306FDa ah!\x01",
            "What are you guys! Is it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0xB, 500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x104,
        (
            "#6P#00307FCharlie、お前も\x01",
            "Do not let the story go on without permission!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x104, 500)
    Sleep(150)

    ChrTalk(
        0xB,
        (
            "#04604F#11PSomewhat,\x01",
            "I'll pick you up from the car.\x02\x03",
            "#04602FYes, are older sisters coming?\x02\x03",
            "#04606FOh, but that girl and wolf\x01",
            "I can not take him as expected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F── Ellie, Noel.\x01",
            "夕食はKeyaと済ませてくれ。\x02\x03",
            "#00008FThen contact the section chief and contact him.\x02\x03",
            "#00013FZeitは課長が戻るまで\x01",
            "I ask for your defense here.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0x9,
        "#01201F#12P#Nwon.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#5P#00101FBut, it is …!\x02\x03",
            "#00106F………I understood.\x01",
            "Leave your absence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#11P#10101F……Please be careful!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#01110FHey Hey, Lloyd.\x01",
            "Are you going out somewhere?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 500)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#12P#00004FOh, with Randy\x01",
            "I will come out for a moment.\x02\x03",
            "#00000FBecause it may be late\x01",
            "Do not stay up late and go to bed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#01109FWow!\x01",
            "Take care!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        "#5P#00306FFucking, why is this … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10302FWell, do not you just have to hang on your belly?\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(24500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x12E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 1)
    NewScene("c010B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_10_2F14 end

    def Function_11_4986(): pass

    label("Function_11_4986")

    BeginChrThread(0x101, 3, 0, 12)
    Sleep(300)
    BeginChrThread(0x102, 3, 0, 12)
    Sleep(300)
    BeginChrThread(0x109, 3, 0, 13)
    Sleep(300)
    BeginChrThread(0x105, 3, 0, 13)
    BeginChrThread(0xA, 3, 0, 14)
    BeginChrThread(0x9, 3, 0, 15)
    Return()

    # Function_11_4986 end

    def Function_12_49B4(): pass

    label("Function_12_49B4")


    def lambda_49B9():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_49B9)
    Sleep(300)

    def lambda_49D6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_49D6)
    WaitChrThread(0xFE, 1)

    def lambda_49EB():
        OP_97(0xFE, 0x5DC, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_49EB)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_12_49B4 end

    def Function_13_4A05(): pass

    label("Function_13_4A05")


    def lambda_4A0A():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4A0A)
    Sleep(300)

    def lambda_4A27():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4A27)
    WaitChrThread(0xFE, 1)

    def lambda_4A3C():
        OP_97(0xFE, 0x3E8, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4A3C)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_13_4A05 end

    def Function_14_4A56(): pass

    label("Function_14_4A56")

    Sleep(500)

    def lambda_4A5E():
        OP_96(0xFE, 0x2BC, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4A5E)

    def lambda_4A78():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4A78)
    WaitChrThread(0xFE, 1)

    def lambda_4A8D():
        OP_96(0xFE, 0x190, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4A8D)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_14_4A56 end

    def Function_15_4AAE(): pass

    label("Function_15_4AAE")

    Sleep(1500)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x0)

    def lambda_4ABE():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4ABE)

    def lambda_4AD8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4AD8)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x9, 0x6)
    SetChrSubChip(0x9, 0x0)
    OP_93(0x9, 0x2D, 0x1F4)
    Return()

    # Function_15_4AAE end

    def Function_16_4AF8(): pass

    label("Function_16_4AF8")


    def lambda_4AFD():
        OP_95(0xFE, 1900, 0, 5200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4AFD)
    WaitChrThread(0xA, 1)
    TurnDirection(0xA, 0xB, 500)
    Return()

    # Function_16_4AF8 end

    def Function_17_4B1E(): pass

    label("Function_17_4B1E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis120.itp")
    CreatePortrait(1, 176, 36, 304, 164, 0, 0, 512, 256, 0, 128, 128, 256, 0xFFFFFF, 0x0, "c_vis239.itp")
    OP_68(15900, 1750, 9800, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, 4000, 850, 15000, 0)
    SetChrPos(0x104, 4000, 850, 15000, 0)
    SetChrPos(0x105, 4000, 850, 15000, 0)
    SetChrPos(0x102, 16300, 850, 10200, 45)
    SetChrPos(0x109, 14500, 850, 9100, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x9, 0x5)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, 2500, 0, 5000, 225)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x9, 3, 0, 1)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, 14900, 850, 8100, 45)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetCameraDistance(22500, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(500)
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("Tio")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Is that so … … to that?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x102,
        (
            "#00106FYeah … I'm sorry.\x02\x03",
            "#00108FせっかくTioちゃんが\x01",
            "They even contacted us again.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x1, 0x8, 0x100, 0x80, 0x180, 0x100)
    OP_0D()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("Tio")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……House.\x01",
            "It was nice to hear the story.\x02\x03",
            "Anyway, today with this.\x01",
            "I will contact you again.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x102,
        "#00100FYes, I understand.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0xA,
        "#01102FTio、またねー！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x109,
        (
            "#10100FThat……\x01",
            "Do not worry too much, do you?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x1, 0x8, 0x100, 0x0, 0x180, 0x80)
    OP_0D()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("Tio")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Yes, I will excuse you.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(1021, 0, 50, 0)
    Sound(939, 0, 50, 0)
    OP_CB(0x1, 0x0, 0x0, 0x17700, 0xFA, 0x0)
    OP_CB(0x1, 0x1, 0x3E8, 0x0, 0xFA, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0xFA, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(500)
    OP_24(0x3AB)
    Sound(73, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    SetCameraDistance(23000, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_93(0x102, 0xE1, 0x1F4)

    ChrTalk(
        0x102,
        (
            "#00106FFuu …\x02\x03",
            "#00108FLloyd's … …\x01",
            "I wonder if it is okay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FOnly for the other party\x01",
            "You are worried as expected …\x02",
        )
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    Sleep(300)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 1000, 0, -1500, 0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    NpcTalk(
        0x8,
        "Sergei's voice",
        "Oh, I came back.\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_5077():

        label("loc_5077")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5077")

    QueueWorkItem2(0xA, 2, lambda_5077)
    Sleep(50)

    def lambda_508C():

        label("loc_508C")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_508C")

    QueueWorkItem2(0x109, 2, lambda_508C)
    Sleep(50)

    def lambda_50A1():

        label("loc_50A1")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_50A1")

    QueueWorkItem2(0x102, 2, lambda_50A1)

    ChrTalk(
        0xA,
        "#01110F#11POh, hey!\x02",
    )

    CloseMessageWindow()
    OP_68(1960, 1750, 2650, 2500)
    MoveCamera(40, 17, 0, 2500)
    OP_6E(380, 2500)
    SetCameraDistance(24000, 2500)
    Sleep(2000)

    def lambda_5105():
        OP_95(0xFE, 1000, 0, 1500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5105)

    def lambda_511F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_511F)
    WaitChrThread(0x8, 1)
    TurnDirection(0x8, 0x102, 500)
    OP_6F(0x79)
    Sound(104, 0, 100, 0)

    ChrTalk(
        0x102,
        "#00102FManager……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10102F#6PThank you for your time.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 18)
    Sleep(1000)
    Fade(1000)
    OP_68(14300, 1850, 9700, 0)
    MoveCamera(40, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    EndChrThread(0x8, 0xFF)
    SetChrPos(0x8, 6300, 850, 9700, 90)

    def lambda_51CF():
        OP_95(0xFE, 12300, 850, 9700, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_51CF)
    SetCameraDistance(22500, 2500)
    OP_0D()
    WaitChrThread(0x8, 1)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0xA, 0x2)
    OP_6F(0x79)

    ChrTalk(
        0x8,
        (
            "#6P#01000FIt became late.\x01",
            "Is the situation unchanged?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00106FYes, well.\x01",
            "As it was at the time of contact ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10101F…… We also near the shop\x01",
            "Should I wait?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P#01004FWell, I worry too much.\x02\x03",
            "#01002FIn the vicinity \"Neue-Blanc\"\x01",
            "I also have monitoring of department 1.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10105FAh……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00102FWell, was that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P#01006FHowever, if people like that\x01",
            "Eyes of surveillance may be destroyed.\x02\x03",
            "#01000F…… Anyway tonight\x01",
            "The people#4RThey are#You have to wait for the return of.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(14300, 2350, 9700, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("c0490", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_4B1E end

    def Function_18_5426(): pass

    label("Function_18_5426")


    def lambda_542B():
        OP_95(0xFE, 1000, 850, 10000, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_542B)
    WaitChrThread(0x8, 1)

    def lambda_5449():
        OP_95(0xFE, 10000, 850, 10000, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5449)
    WaitChrThread(0x8, 1)
    Return()

    # Function_18_5426 end

    def Function_19_5463(): pass

    label("Function_19_5463")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(64000, 1100, 8600, 0)
    MoveCamera(50, 15, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x101, 63100, 0, 6900, 0)
    SetChrPos(0x102, 64000, 0, 5500, 0)
    SetChrPos(0x109, 65099, 0, 5100, 0)
    SetChrPos(0x104, 64400, 0, 6900, 0)
    SetChrPos(0x105, 62700, 0, 5500, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 64000, 150, 11400, 180)
    SetCameraDistance(23000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x102,
        "#12P#00108F…… Such a thing ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106Ftruly……\x01",
            "It sounds like ridiculous guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01003FWell, you mean \"fighting spirit\"\x01",
            "I can not talk about succeeding ……\x02\x03",
            "#01000FYou seem to have had various harvests?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FAh……\x02\x03",
            "#00308FThose guys are receiving it now\x01",
            "A contract equivalent to 100 million mirrors …\x02\x03",
            "#00301FContract partner, from the flow\x01",
            "It is no mistake that it is an empire government.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FAlso, I am busy from tomorrow\x01",
            "Because I was saying that … ….\x02\x03",
            "#10300FAfter all during the trade meeting\x01",
            "You seem to intend to do something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01003FHum, then\x01",
            "It's the content of that 100 million contract … …\x02\x03",
            "#01001F── Lloyd, what do you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005F……Oh, yes.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhat is the content of the contract of 100 million mirrors?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Assassination of the president of the Republic\x01",      # 0
            "Securing the safety of the Iraqi Prime Minister\x01",      # 1
            "Clear the black moon\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_583B"),
        (1, "loc_5A66"),
        (2, "loc_5C46"),
        (SWITCH_DEFAULT, "loc_5E42"),
    )


    label("loc_583B")


    ChrTalk(
        0x101,
        (
            "#12P#00008FRepublic of Calvert,\x01",
            "Assassination of President Rock Smith … …\x02\x03",
            "#00006F… Well, no.\x02\x03",
            "If so,\x01",
            "There are too few 100 million mirrors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01004FKuku, that's right.\x02\x03",
            "#01002FIf it can be considered at this point\x01",
            "It seems that it is about securing the safety of the Iraqi prime minister.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00011FAh……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00101FI see.\x02\x03",
            "Osborne's Prime Minister is in the Empire\x01",
            "Having a considerable hostile force\x01",
            "It is said that … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F… … That guy looks alike.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5E42")

    label("loc_5A66")

    OP_2C(0xA3, 0x1)

    ChrTalk(
        0x101,
        (
            "#12P#00003F…… This is kan … ….\x02\x03",
            "#00001FThe Chancellor of Iron and Ireland is quite within the Empire\x01",
            "It is said to have an enemy force.\x02\x03",
            "With this crossbell, from such a force\x01",
            "Would it be possible to protect the Prime Minister?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_5B8F():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5B8F)
    Sleep(50)

    def lambda_5B9F():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5B9F)
    Sleep(50)

    def lambda_5BAF():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5BAF)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x102,
        "#12P#00105FAh……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F……I see……\x01",
            "That seems to be an ant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01004FPowered by Translate\x01",
            "It is a nice place for good eyes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E42")

    label("loc_5C46")


    ChrTalk(
        0x101,
        (
            "#12P#00008FCleaning up \"Black moon\" ……\x02\x03",
            "#00006FNo, during the trade meeting\x01",
            "As expected the timing is bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01004FKuku, that's right.\x02\x03",
            "#01002FIf it can be considered at this point\x01",
            "It seems that it is about securing the safety of the Iraqi prime minister.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00011FAh……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00101FI see.\x02\x03",
            "Osborne's Prime Minister is in the Empire\x01",
            "Having a considerable hostile force\x01",
            "It is said that … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F… … That guy looks alike.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5E42")

    label("loc_5E42")


    ChrTalk(
        0x105,
        (
            "#12P#10303FOh, but that's it\x01",
            "Is there 100 million mirrors a bit too much?\x02\x03",
            "#10301FEven the prime minister is his escort\x01",
            "I guess they will be accompanied.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106Fsurely……\x02\x03",
            "#10101FWhether you are an empire or a republic\x01",
            "A considerable escort officer\x01",
            "It is said that they will accompany them.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_613D")
    OP_2C(0xA3, 0x2)

    ChrTalk(
        0x101,
        (
            "#5P#00003F… … Of course\x01",
            "It is different from a face-up escort.\x02\x03",
            "#00008FHowever, as far as their trends are concerned\x01",
            "Various forms of land called crossbell\x01",
            "It is certain that he is trying to grasp it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FAlmorika village, Mainz,\x01",
            "And sighting information at the Belgard gate\x01",
            "You may be telling it.\x02\x03",
            "#10304FCost of food procurement and buying and selling seven oysters\x01",
            "It seems there was a plausible reason … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00003FOh, I was visiting various places\x01",
            "I think that the real purpose was different.\x02\x03",
            "#00001FThat is exactly like us and the hypocrite,\x01",
            "To be able to respond instantly even if something happens.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_624C")

    label("loc_613D")


    ChrTalk(
        0x101,
        (
            "#5P#00003F… … Of course\x01",
            "It is different from a face-up escort.\x02\x03",
            "#00008FHowever, as far as their trends are concerned\x01",
            "Various forms of land called crossbell\x01",
            "It is certain that he is trying to grasp it.\x02\x03",
            "#00001FThat is exactly like us and the hypocrite,\x01",
            "To be able to respond instantly even if something happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10300FHM……\x02",
    )

    CloseMessageWindow()

    label("loc_624C")


    ChrTalk(
        0x102,
        (
            "#12P#00106Fsurely……\x01",
            "I felt like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00308F……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01000F── Well, at the present moment\x01",
            "It can be estimated that far.\x02\x03",
            "#01003FThe leaders of the countries visited tomorrow,\x01",
            "There is an unveiling ceremony for the Orkis Tower.\x02\x03",
            "#01002FOh, by the way\x01",
            "You guys will have them go to the scene as well?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_63E5():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_63E5)
    Sleep(50)

    def lambda_63F5():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_63F5)
    Sleep(50)

    def lambda_6405():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6405)
    Sleep(50)

    def lambda_6415():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6415)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)

    ChrTalk(
        0x101,
        "#12P#00005Feh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00105FWhat is on site … to the unveiling ceremony?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01004FApparently to the \"red constellation\"\x01",
            "It seems they are being stolen.\x02\x03",
            "#01000F─ - Counterbreak#4RFather#And countermeasures against terrorism\x01",
            "Originally it is not your job.\x02\x03",
            "Switch your mood here\x01",
            "A brief overview of the situation#4RFissured#Do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000F……I see……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FHa ha …\x01",
            "I have a pain in my ears.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FWell, the unveiling ceremony is\x01",
            "Do you mean to participate in security?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01003FWell, as it is nominally,\x01",
            "The unveiling ceremony is more than that\x01",
            "Please concentrate on observing.\x02\x03",
            "#01002FAir at the beginning of the trade meeting … …\x01",
            "Do you have the aura of the leaders?\x02\x03",
            "You should also have a different perspective.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000F……OK.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHuh, then then from the special seat\x01",
            "I'd like you to appreciate it.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(64000, 1600, 8600, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_6F(0x79)
    SetScenarioFlags(0x22, 0)
    NewScene("e4010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_19_5463 end

    def Function_20_673B(): pass

    label("Function_20_673B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    AddParty(0x9, 0xFF, 0xFF)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis120.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00600.itp")
    CreatePortrait(2, 176, 36, 304, 164, 0, 0, 512, 256, 128, 0, 256, 128, 0xFFFFFF, 0x0, "c_vis240.itp")
    SoundLoad(3452)
    SoundLoad(4106)
    SoundLoad(3609)
    SoundLoad(3610)
    OP_68(64000, 1100, 8600, 0)
    MoveCamera(50, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x101, 63100, 0, 6700, 0)
    SetChrPos(0x102, 64400, 0, 6700, 0)
    SetChrPos(0x109, 62700, 0, 5300, 0)
    SetChrPos(0x104, 64000, 0, 5300, 0)
    SetChrPos(0x105, 65099, 0, 4900, 0)
    SetChrPos(0x10A, 65099, 0, 8600, 225)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 64000, 150, 11400, 180)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x8,
        (
            "#01001F─ ─ I see.\x01",
            "Is it a terrorist aiming at the two leaders?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetCameraDistance(23000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x10A,
        (
            "#00606F#5PWell, there was a possibility\x01",
            "What is it so specific?\x02\x03",
            "#00610FWhether you are an empire or a republic\x01",
            "What on earth are you thinking …! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1P#01003FWell, obviously something's aim\x01",
            "You may wish to see it there.\x02\x03",
            "#01000FAlso for the mayor and the guard\x01",
            "You seemed better to tell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00603F#5PYes, I will leave it there.\x02\x03",
            "#00601F── Even so.\x01",
            "You are in that \"Arseille\"\x01",
            "I heard doubting my ears when I heard that he got on.\x02\x03",
            "Moreover, from two people in the national guest class\x01",
            "Heard that you will hear the story so far …\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6AC6():
        TurnDirection(0x101, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6AC6)
    Sleep(100)

    def lambda_6AD6():
        TurnDirection(0x109, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6AD6)
    Sleep(100)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x101,
        (
            "#6P#00012FWell, even one person\x01",
            "Of course you checked it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00302FWell, it was suddenly here\x01",
            "I do not want you to make it awful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00607F#5PWell, suddenly,\x01",
            "At that time consult on above\x01",
            "Whether to accept an invitation …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1P#01004FPowered by Translate\x01",
            "What do you do with the guys doing?\x02\x03",
            "#01002FThe partner who you called also seems to be out of the standard,\x01",
            "It's just good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#00606F#5PDamn\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00309FWell, but it certainly has changed\x01",
            "It was a princess and a prince.\x02\x03",
            "#00300FEspecially when Prince Oliver is\x01",
            "I did not think it was such a weirdo.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6D12():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6D12)
    Sleep(100)

    def lambda_6D22():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6D22)
    Sleep(100)

    def lambda_6D32():
        TurnDirection(0x105, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6D32)
    Sleep(100)

    def lambda_6D42():
        TurnDirection(0x109, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6D42)
    Sleep(100)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x102,
        (
            "#5P#00106FExcuse me, Randy.\x02\x03",
            "#00100FSurely it's funny … …\x01",
            "It was a very light person though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00004FBut, various things\x01",
            "I think that it is a person who thinks carefully.\x02\x03",
            "#00000FMajor who had that escort\x01",
            "It seems that it was quite a skill.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10102FBesides, with Princess Claudia\x01",
            "Assistant Yulia was a wonderful guy …!\x02\x03",
            "#10112FHis highness is frank but there is elegance\x01",
            "Assistant Yulia is already dignified …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#11PHuhu, even for my sister's properly\x01",
            "You seem to have got a sign?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10111FWhy, why not ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00606F#5P…… Completely.\x02\x03",
            "#00600FWell oh - the presence of terrorists\x01",
            "Even knowing it is a harvest.\x02\x03",
            "A bit, tomorrow's security shift\x01",
            "You might as well adjust it … …\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6FE3():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6FE3)
    Sleep(100)

    def lambda_6FF3():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6FF3)
    Sleep(100)

    def lambda_7003():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7003)
    Sleep(100)

    def lambda_7013():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7013)
    Sleep(100)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x101,
        (
            "#6P#00001FAfter all the momentum is tomorrow ……\x01",
            "Is it the actual commerce meeting?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1P#01003FOh, in the afternoon after tomorrow\x01",
            "The heads also return home …\x02\x03",
            "#01001FIf there is something\x01",
            "The chances of tomorrow will be high.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FCertainly …\x01",
            "The meeting was from noon, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00600F#5POh, from 1 pm\x01",
            "Located in Orchise Tower 35F\x01",
            "It is held at \"International Conference Hall\".\x02\x03",
            "Then put a break once\x01",
            "It is going to continue until evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00305FThen, during the meeting,\x01",
            "Should I protect the leaders?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00604F#5PNo, inside the Orchis Tower\x01",
            "A perfect security system is laid.\x02\x03",
            "There is also the security of the building itself,\x01",
            "It would be rather safe during the meeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1P#01003FIn addition to the venue security\x01",
            "Arios will also participate.\x02\x03",
            "#01002FAs a witness to the guild\x01",
            "It seems that it is also in the place of a trade meeting\x01",
            "Speaking of security is safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FReally……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10108FThen, before and after the meeting\x01",
            "It may be the most dangerous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#12PWhen I came out of the tower\x01",
            "Try turning from a distance and a sniper.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FTo be honest, that is the best,\x01",
            "It's a scary pattern …\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(103, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x80000000)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 59000, -3000, 3300, 90)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(3609, 255, 70, 0)

    NpcTalk(
        0xA,
        "Keyaの声",
        "#11P#13AHey Hey, Lloyd.\x02",
    )

    CloseMessageWindow()
    OP_68(64000, 1000, 6300, 2000)
    MoveCamera(62, 15, 0, 2000)
    OP_6E(400, 2000)
    SetCameraDistance(24000, 2000)
    OP_5A()
    SetChrPos(0xA, 61500, 0, 3800, 90)

    def lambda_74A3():
        TurnDirection(0x109, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_74A3)
    Sleep(50)

    def lambda_74B3():
        TurnDirection(0x102, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_74B3)
    Sleep(50)

    def lambda_74C3():
        TurnDirection(0x104, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_74C3)
    Sleep(50)

    def lambda_74D3():
        TurnDirection(0x105, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_74D3)
    Sleep(50)

    def lambda_74E3():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_74E3)
    Sleep(50)

    def lambda_74F3():
        TurnDirection(0x10A, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_74F3)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x10A, 0)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 59000, 0, 3300, 90)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_7546():
        OP_96(0xFE, 0xEE48, 0x0, 0xCE4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_7546)

    def lambda_7560():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_7560)
    WaitChrThread(0xA, 1)

    def lambda_7575():
        OP_95(0xFE, 61500, 0, 3800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_7575)
    WaitChrThread(0xA, 1)
    TurnDirection(0xA, 0x10A, 500)
    OP_6F(0x79)
    OP_63(0xA, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xA,
        "#12P#01105F#3610V#30WOh, it's an obscure ogresan!\x02",
    )

    CloseMessageWindow()
    OP_24(0xE1A)
    OP_C9(0x1, 0x80000000)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x10A, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x10A,
        (
            "#5P#00603F……As usual\x01",
            "You do not seem to be disciplined?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00011FWell, sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00112F#5PKeyaちゃん、この人は\x01",
            "You say Mr. Dudley … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12P#01109FWell, Dudley!\x02\x03",
            "#01110FI have not seen you for a long time.\x01",
            "How are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#5P#00604FHun, an investigator in section 1,\x01",
            "I am always in perfect condition.\x02\x03",
            "#00607F─ ─ not!\x01",
            "Stop turning it off!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12P#01106FWell, why not?\x02\x03",
            "#01111FWell then, Uncle Dudley?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x10A,
        "#5P#00610FWho is the orgy, who the hell!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10112FWell, alright.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00309FHaha, for a child,\x01",
            "It is enough odysan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#11PそれでKeya。\x01",
            "What is it for?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#12P#01106FOh, it was.\x02\x03",
            "#01100FWell, to the Lloyd's\x01",
            "Communication is in there?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#5PCommunication?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F#5POh, the communication bell\x01",
            "It looks like he did not ring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12P#01109FOh, it's not a futu\x01",
            "Kao comes out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#5PThe terminal …\x01",
            "Keya、よく操作が分かったな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F#5Pでも、それならTioすけか？\x01",
            "Even though I contacted you in the evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12P#01104FNo, he is a man of a sovacas.\x02\x03",
            "#01100FSomehow Khao gets red\x01",
            "I'm getting blue.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(63000, 1000, 6300, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    Sleep(1000)
    OP_68(17800, 1750, 10700, 0)
    MoveCamera(13, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 16300, 850, 10200, 45)
    SetChrPos(0x102, 15250, 850, 8300, 45)
    SetChrPos(0x104, 14600, 850, 9400, 45)
    SetChrPos(0x109, 16200, 850, 7400, 0)
    SetChrPos(0x105, 17200, 850, 7800, 0)
    SetChrPos(0x10A, 14100, 850, 11900, 135)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 13000, 850, 10400, 90)
    SetChrPos(0xA, 13300, 850, 9300, 90)
    OP_68(16800, 1750, 10700, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    Sound(72, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(300)
    BeginChrThread(0x101, 3, 0, 21)
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("Voice of Jonah")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4S─ ─ I'm late!\x02\x03",
            "#3SIndeed,\x01",
            "I will keep you waiting!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x101, 3)
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x101,
        (
            "#00012FIt is bad.\x02\x03",
            "#00002FAnyway, it's been a long time.\x01",
            "I am doing fine - ─\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x2, 0x8, 0x180, 0x0, 0x200, 0x80)
    OP_0D()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("Voice of Jonah")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ah, now,\x01",
            "Such a greeting is good!\x02\x03",
            "As soon as possible to you,\x01",
            "There is a need to ask!\x02\x03",
            "From my present base\x01",
            "Do not you see me? Is it?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x101,
        "#00011FHuh……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00105FWhat is the base …?\x01",
            "Have you been sleeping?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x2, 0x8, 0x100, 0x0, 0x180, 0x80)
    OP_0D()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("Voice of Jonah")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Oh, Geo Front B in the partition\x01",
            "The location of the eighth control terminal!\x02\x03",
            "From yesterday to today\x01",
            "I use that terminal arbitrarily\x01",
            "It looks like I have a guy!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x101,
        "#00001FI use it arbitrarily … ….\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x109,
        (
            "#10105FWhy the hell\x01",
            "Did you understand such a thing?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        (
            "#00301FTsu, Jonah public.\x01",
            "What I use arbitrarily\x01",
            "You are not the same.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x2, 0x8, 0x180, 0x0, 0x200, 0x80)
    OP_0D()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("Voice of Jonah")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Well, anyway!\x02\x03",
            "During my absence, at that terminal\x01",
            "I put powerful protection!\x02\x03",
            "So, if it should be broken\x01",
            "At the time of the remote connection experiment of the power net\x01",
            "Try to send an alert ……\x02\x03",
            "That alert was coming today!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x101,
        "#00013Fthat is……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x105,
        (
            "#10303F…… The terminal you protected\x01",
            "There is a person who has hacked.\x02\x03",
            "#10301FThat's it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x2, 0x8, 0x0, 0x80, 0x80, 0x100)
    OP_0D()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("Voice of Jonah")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Oh, that's it!\x01",
            "There is no doubt that it is quite a hacker!\x02\x03",
            "Anyway catch it\x01",
            "I do not want you to touch it again!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x104,
        (
            "#00306FWant to put yourself on the shelf\x01",
            "Do not say something selfish.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00108FBut, it's a pretty hacker ….\x01",
            "I am a little worried.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00003FOh, Len should have already left,\x01",
            "I can not think Roberts as chief.\x02\x03",
            "#00001FBecause I'm going to watch it for the time being\x01",
            "Please contact me later.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x2, 0x8, 0x100, 0x0, 0x180, 0x80)
    OP_0D()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("Voice of Jonah")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Oh, I asked!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(1021, 0, 50, 0)
    Sound(939, 0, 50, 0)
    OP_CB(0x2, 0x0, 0x0, 0x17700, 0xFA, 0x0)
    OP_CB(0x2, 0x1, 0x3E8, 0x0, 0xFA, 0x0)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0xFA, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(500)
    OP_24(0x3AB)
    OP_68(16300, 1750, 10200, 0)
    MoveCamera(13, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    Sound(73, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)

    ChrTalk(
        0x8,
        "#01000F#5PWhy are you going?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#00003FYes, just in case.\x02\x03",
            "#00000FWhat if I could alone alone\x01",
            "You may go and watch it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00301FCome on, do not be unhappy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FI see …\x01",
            "Hackers are the only ones\x01",
            "It will not be limited.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10101FI will be with you!\x02",
    )

    CloseMessageWindow()
    OP_68(15300, 1750, 10700, 2000)
    OP_63(0x10A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x10A)
    OP_6F(0x79)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0x10A,
        (
            "#3452V#30W── Wait.\x02\x03",
            "#4106VI will accompany you as well.\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0x100A)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_865A():
        TurnDirection(0x101, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_865A)
    Sleep(50)

    def lambda_866A():
        TurnDirection(0x104, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_866A)
    Sleep(50)

    def lambda_867A():
        TurnDirection(0x109, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_867A)
    Sleep(50)

    def lambda_868A():
        TurnDirection(0x105, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_868A)
    Sleep(50)

    def lambda_869A():
        TurnDirection(0x102, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_869A)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)

    ChrTalk(
        0x101,
        "#11P#00005FHuh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10302FOh, what kind of wind blowing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00603F#5PHun, before the trade meeting\x01",
            "Even a little irregular element\x01",
            "I just want to grasp it.\x02\x03",
            "#00601FTime is regret, I will finally go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00011FI understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FHuh, then lightly,\x01",
            "Are you going with the exercise after eating?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x10E, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x102,
        (
            "#12P#00100F課長、Keyaちゃん、\x01",
            "Well, let's go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#01002F#5POh, at best, be careful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#6P#01109FTake care.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(24000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Dudley investigatorがパーティに加入しました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "キャンプメニューの[TACTICS]で\x01",
            "You can add it to an attack member.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_32(0x9, 0x0, 0x42)
    OP_32(0x9, 0x5, 0xC8)
    OP_42(0x9, 0x466, 0xFF)
    OP_42(0x9, 0x5E1, 0xFF)
    OP_42(0x9, 0x645, 0xFF)
    OP_42(0x9, 0x4E, 0x3)
    OP_42(0x9, 0x49, 0x4)
    OP_38(0x9, 0x80, 0x2)
    OP_38(0x9, 0x81, 0x1)
    OP_38(0x9, 0x82, 0x2)
    OP_38(0x9, 0x83, 0x2)
    OP_38(0x9, 0x84, 0x1)
    OP_38(0x9, 0x85, 0x1)
    OP_38(0x9, 0x86, 0x1)
    OP_42(0x9, 0x6D, 0x1)
    OP_42(0x9, 0xAE, 0x2)
    OP_42(0x9, 0xB8, 0x3)
    OP_42(0x9, 0x8D, 0x4)
    OP_42(0x9, 0x84, 0x5)
    OP_42(0x9, 0x7D, 0x6)
    AddCraft(0x9, 0x179)
    OP_CC(0x1, 0xFF, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 14400, 850, 12500, 0)
    BeginChrThread(0x8, 0, 0, 0)
    ClearChrFlags(0x8, 0x40)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrPos(0xA, 5570, 150, 6230, 180)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x5)
    SetChrPos(0x9, 2880, 0, 1750, 225)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0x9, 0x40)
    SetChrPos(0x0, 8790, 850, 10000, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x141, 0)
    OP_29(0xA3, 0x1, 0x12)
    OP_29(0xA3, 0x1, 0x13)
    ReplaceBGM("ed7150", "ed7513")
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_20_673B end

    def Function_21_8A44(): pass

    label("Function_21_8A44")

    OP_CB(0x2, 0x0, 0x4B0, 0xFFFFFBB4, 0x1, 0x0)
    Sleep(1)
    OP_CB(0x2, 0x0, 0xFFFFFAEC, 0x4B0, 0x1, 0x0)
    Sleep(1)
    OP_CB(0x2, 0x0, 0xFFFFFC18, 0xFFFFFA24, 0x1, 0x0)
    Sleep(1)
    OP_CB(0x2, 0x0, 0x640, 0xFFFFFB50, 0x1, 0x0)
    Sleep(1)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1, 0x0)
    OP_CC(0x0, 0xFF, 0x0)
    Return()

    # Function_21_8A44 end

    def Function_22_8AB4(): pass

    label("Function_22_8AB4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00900.itc", 0x1E)
    LoadChrToIndex("apl/ch50380.itc", 0x1F)
    LoadChrToIndex("apl/ch51225.itc", 0x20)
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    OP_68(700, 1100, 4100, 0)
    MoveCamera(53, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, 500, 0, 2100, 0)
    SetChrPos(0x102, -1500, 0, 1400, 45)
    SetChrPos(0x109, -2200, 0, 2200, 45)
    SetChrPos(0x105, -1900, 0, 3400, 90)
    SetChrPos(0x104, 900, 0, 900, 0)
    SetChrPos(0x103, 700, 0, 3600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 2700, 0, 5200, 225)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, 700, 0, 4100, 180)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0x9, 0x6)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, -900, 0, 5300, 135)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xC, 2200, 0, 2400, 315)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetCameraDistance(24000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0xA,
        (
            "#01109Fえへへ、Tioだー！\x02\x03",
            "#01110Fねえねえ、Zeit！\x01",
            "Tioが戻ってきたよー！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01200F#5Pwon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00202FI'm home.\x01",
            "Keya、Zeit。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)

    def lambda_8CF9():
        OP_96(0xFE, 0x2BC, 0x0, 0x1194, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_8CF9)
    WaitChrThread(0xA, 1)
    TurnDirection(0x103, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#6P#00204FSergey Manager。\x01",
            "I'm back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01004FOh, I returned well.\x02\x03",
            "#01002FHu, suddenly a friend\x01",
            "You seem to have saved a pinch?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00004FYes, it was really helpful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00106FあそこでTioちゃんが\x01",
            "If you do not come\x01",
            "What was going on ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10112FYeah yeah, I feel snook.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00604F…… Thank you for this time\x01",
            "You seem to have to say.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        "#5P#00205FThat, another great thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00309FHaha, let me be shy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FWell, in fact, at a good timing\x01",
            "I think I came back.\x02\x03",
            "#10300FIf such hackers get involved\x01",
            "We are all over with us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00006FThat's right.\x02",
    )

    CloseMessageWindow()
    OP_68(1300, 1100, 2800, 2000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_93(0x101, 0x2D, 0x1F4)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#6P#00003F── Manager, Mr. Dudley.\x02\x03",
            "#00001FIt is tomorrow's trade meeting … …\x01",
            "We also guard against the Orkis Tower\x01",
            "Could you join us?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_90DE():
        TurnDirection(0xC, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_90DE)
    Sleep(50)

    def lambda_90EE():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_90EE)
    Sleep(50)

    def lambda_90FE():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_90FE)
    Sleep(50)

    def lambda_910E():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_910E)
    Sleep(50)

    def lambda_911E():
        TurnDirection(0x8, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_911E)
    Sleep(50)
    WaitChrThread(0xC, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x8, 0)

    ChrTalk(
        0x102,
        "#6P#00105FLloyd, that is ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00305FCome on.\x01",
            "What happened to you suddenly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P#01000FHM……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00600F#11P…… The security system at the venue\x01",
            "Should I have said that everything is perfect?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FBut today's hacker is\x01",
            "Things like tower drawings\x01",
            "I got it from somewhere.\x02\x03",
            "#00008FIt is not a word of \"silver\"\x01",
            "There is a possibility that something will be set up ─\x02\x03",
            "#00001FNo, rather that information \"somebody\"\x01",
            "I think that there is a high possibility of handed over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10101Fwho……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10301FHmm, who is it?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 3)

    label("loc_9323")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_946D")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhere did the mysterious hacker give the information?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "\"Black moon\"\x01",            # 0
            "\"Red constellation\"\x01",        # 1
            "Other forces\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_93CF"),
        (1, "loc_93CF"),
        (2, "loc_944C"),
        (SWITCH_DEFAULT, "loc_9468"),
    )


    label("loc_93CF")


    ChrTalk(
        0x101,
        (
            "#11P#00006F(No … but more than that.\x01",
            "There must be people who want them. )\x02\x03",
            "#00001F(that is……)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9447")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9447")

    Jump("loc_9468")

    label("loc_944C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9460")
    OP_2C(0xA3, 0x1)

    label("loc_9460")

    SetScenarioFlags(0x0, 3)
    Jump("loc_9468")

    label("loc_9468")

    Jump("loc_9323")

    label("loc_946D")


    ChrTalk(
        0x101,
        (
            "#11P#00003F\"Red constellation\" or \"black moon\",\x01",
            "Or the Imperial Government or Republic Government … …\x02\x03",
            "Even though there seems to be any\x01",
            "There are people who are likely to be more realistic.\x02\x03",
            "#00013FTerrorists of the Empire and the Republic.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#6P#00101FWith His Highness Claudia\x01",
            "I heard from Prince Oliverto …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00301FAim at the top of each country\x01",
            "Are they two terrorists?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10108FIf there is a building diagram of a building indeed\x01",
            "You may be able to aim for a blind spot …\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#6P#00006FOf course, forgery information\x01",
            "There is also a possibility … ….\x02\x03",
            "#00001FAgain tomorrow, at the Orkis Tower\x01",
            "The possibility of something happening\x01",
            "I think that it can be said that it got higher.\x02\x03",
            "You can do security around the tower\x01",
            "Will not you join us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01004FWell, I see.\x02\x03",
            "#01002FDudley, how are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00606F#11PFuu …\x01",
            "Well, that would be nice.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    SetChrFlags(0xC, 0x20)
    SetChrFlags(0xC, 0x2)
    SetChrChipByIndex(0xC, 0x20)
    SetChrSubChip(0xC, 0x0)
    Sleep(100)
    SetChrSubChip(0xC, 0x1)
    Sleep(100)
    SetChrSubChip(0xC, 0x2)
    Sleep(100)
    SetChrSubChip(0xC, 0x3)
    Sleep(100)
    SetChrSubChip(0xC, 0x4)
    Sleep(100)
    SetChrSubChip(0xC, 0x3)
    Sound(318, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0xC,
        (
            "#00611F#11P── At noon of tomorrow,\x01",
            "Come to Orkistower 1F.\x02\x03",
            "As a spare guard\x01",
            "I will put it in the scene of the trade meeting.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_991A():
        TurnDirection(0x101, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_991A)
    Sleep(50)

    def lambda_992A():
        TurnDirection(0x104, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_992A)
    Sleep(50)

    def lambda_993A():
        TurnDirection(0x103, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_993A)
    Sleep(50)

    def lambda_994A():
        TurnDirection(0x102, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_994A)
    Sleep(50)

    def lambda_995A():
        TurnDirection(0x109, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_995A)
    Sleep(50)

    def lambda_996A():
        TurnDirection(0x105, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_996A)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        "#6P#00005FHuh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00305FOops, is it the venue?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FOh\x01",
            "Is not it generous?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xC, 0x1)
    Sleep(80)
    SetChrSubChip(0xC, 0x0)
    Sleep(80)
    ClearChrFlags(0xC, 0x20)
    ClearChrFlags(0xC, 0x2)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "#00603F#11PDo not make a difference.\x01",
            "It is a spare staff to the last.\x02\x03",
            "Even in the attempted assassination of the mayor\x01",
            "Although it was a coincidence, he was useful,\x01",
            "Some people are familiar with the power net.\x02\x03",
            "#00601FBecause it is degree of insurance by any chance\x01",
            "At most valves#2RAside#Try it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FRyo, All right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10102FRespectfully!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00204FHowever, as I thought\x01",
            "I am kind of … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00309FHaha, when will you come\x01",
            "I wonder if they will be deleted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#01111F#5PDere\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x102, 500)
    Sleep(150)

    ChrTalk(
        0xA,
        (
            "#01110F#5PHey Hey Erie.\x01",
            "What is Dere -?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00109FWell, yes.\x01",
            "Keyaちゃんと話している時の\x01",
            "I guess everyone's attitude ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10309FHuh, this is not it\x01",
            "It may be soon.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xC,
        "#00610F#11PKimi, you …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01004FClose, apparently tomorrow\x01",
            "I'm getting busy so dead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01203Fwon.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(24500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(1000)
    Sound(13, 0, 100, 0)
    Sleep(4000)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(2000)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    OP_32(0xFF, 0xFE, 0x0)
    ReplaceBGM(-1, -1)
    ReplaceBGM("ed7150", "ed7125")
    ReplaceBGM("ed7101", "ed7125")
    SetScenarioFlags(0x22, 7)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_22_8AB4 end

    def Function_23_9DA3(): pass

    label("Function_23_9DA3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00302.itc", 0x20)
    LoadChrToIndex("chr/ch02902.itc", 0x21)
    LoadChrToIndex("chr/ch03002.itc", 0x22)
    LoadChrToIndex("chr/ch00202.itc", 0x23)
    LoadChrToIndex("apl/ch50090.itc", 0x24)
    LoadChrToIndex("apl/ch50092.itc", 0x25)
    LoadChrToIndex("apl/ch51090.itc", 0x26)
    LoadEffect(0x0, "event/ev12002.eff")
    OP_68(12600, 2550, 4300, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0x20)
    SetChrSubChip(0x104, 0x2)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x1)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x2)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x101, 13900, 900, 5400, 270)
    SetChrPos(0x102, 11300, 900, 7000, 90)
    SetChrPos(0x103, 11300, 900, 3800, 90)
    SetChrPos(0x104, 13900, 900, 3800, 270)
    SetChrPos(0x109, 11300, 900, 2200, 90)
    SetChrPos(0x105, 13900, 900, 2200, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 11300, 900, 5400, 90)
    SetChrChipByIndex(0x9, 0x6)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 16300, 850, 6400, 270)
    SetMapObjFrame(0xFF, "isu00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "isu00_sd", 0x0, 0x1)
    ClearChrFlags(0x26, 0x80)
    OP_78(0xA, 0x26)
    ClearChrFlags(0x27, 0x80)
    OP_78(0xB, 0x27)
    ClearChrFlags(0x28, 0x80)
    OP_78(0xC, 0x28)
    ClearChrFlags(0x29, 0x80)
    OP_78(0xD, 0x29)
    ClearChrFlags(0x2A, 0x80)
    OP_78(0xE, 0x2A)
    ClearChrFlags(0x2B, 0x80)
    OP_78(0xF, 0x2B)
    ClearChrFlags(0x2C, 0x80)
    OP_78(0x1A, 0x2C)
    ClearChrFlags(0x2D, 0x80)
    OP_78(0x1B, 0x2D)
    OP_49()
    SetChrPos(0x26, 14000, 0, 7000, 0)
    OP_D5(0x26, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x27, 14000, 0, 5400, 0)
    OP_D5(0x27, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x28, 14000, 0, 3800, 0)
    OP_D5(0x28, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x29, 14000, 0, 2200, 0)
    OP_D5(0x29, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x2A, 11200, 0, 7000, 0)
    OP_D5(0x2A, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x2B, 11200, 0, 5400, 0)
    OP_D5(0x2B, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x2C, 11200, 0, 3800, 0)
    OP_D5(0x2C, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x2D, 11200, 0, 2200, 0)
    OP_D5(0x2D, 0x0, 0x15F90, 0x0, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x13, 0x26)
    SetChrSubChip(0x13, 0x5)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 13000, 1350, 7100, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x24)
    SetChrSubChip(0x14, 0x14)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 13100, 1350, 6800, 0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x26)
    SetChrSubChip(0x15, 0x5)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 12200, 1350, 7100, 0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x24)
    SetChrSubChip(0x16, 0x11)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 12300, 1300, 6800, 0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x26)
    SetChrSubChip(0x17, 0x5)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 13000, 1350, 5200, 0)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x24)
    SetChrSubChip(0x18, 0x14)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 13100, 1350, 4900, 0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    SetChrChipByIndex(0x19, 0x26)
    SetChrSubChip(0x19, 0x5)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 12200, 1350, 5200, 0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x24)
    SetChrSubChip(0x1A, 0x11)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 12300, 1300, 4900, 0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x26)
    SetChrSubChip(0x1B, 0x5)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, 13000, 1350, 3800, 0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1C, 0x24)
    SetChrSubChip(0x1C, 0x14)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, 13100, 1350, 3500, 0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1D, 0x26)
    SetChrSubChip(0x1D, 0x5)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, 13000, 1350, 2000, 0)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1E, 0x24)
    SetChrSubChip(0x1E, 0x14)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, 13100, 1350, 1700, 0)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x26)
    SetChrSubChip(0x1F, 0x5)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, 12200, 1350, 2000, 0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x24)
    SetChrSubChip(0x20, 0x11)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, 12300, 1300, 1700, 0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0x26)
    SetChrSubChip(0x21, 0x5)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, 12200, 1350, 3800, 0)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x24)
    SetChrSubChip(0x22, 0x11)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, 12300, 1300, 3500, 0)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    SetChrChipByIndex(0x23, 0x25)
    SetChrSubChip(0x23, 0x0)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, 16300, 750, 5500, 0)
    SetChrChipByIndex(0x24, 0x26)
    SetChrSubChip(0x24, 0x6)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x24, 12650, 1450, 5900, 0)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    SetChrChipByIndex(0x25, 0x26)
    SetChrSubChip(0x25, 0x6)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, 12650, 1450, 2750, 0)
    ClearChrFlags(0x25, 0x80)
    ClearChrBattleFlags(0x25, 0x8000)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 12650, 1550, 5900, 0, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 12650, 1550, 2750, 0, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    OP_68(12600, 2050, 4300, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#00008F#11P…… Slow, the section chief.\x02\x03",
            "#00006FBecause there was such a thing\x01",
            "I think it is unreasonable ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10108FYes……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#5P#00106F…… Now at the Orkis Tower\x01",
            "About future measures\x01",
            "I guess they are talking.\x02\x03",
            "#00108FIt's a politically difficult problem … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#11PIt's also Waldo … …\x02\x03",
            "#10301FDo something terrible at difficult times\x01",
            "You guys did it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6P#01106F…… Hey Hey, everyone.\x02\x03",
            "#01112FIf the doctor is not coming back\x01",
            "As a matter of course, the pot seems to stop.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x0)
    Sleep(100)
    SetChrSubChip(0x101, 0x0)
    Sleep(200)

    ChrTalk(
        0x104,
        (
            "#00304F#11P…… No, when it gets late\x01",
            "I was saying I was beginning to get started earlier.\x02\x03",
            "#00300FKeiko prepared for it,\x01",
            "Even us alone can get it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#6P#01108FBut,\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x0)
    Sleep(100)
    SetChrSubChip(0x101, 0x1)
    Sleep(200)

    ChrTalk(
        0x103,
        "#6P#00208FRandy san ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PAnyway about the pot ……\x01",
            "Randy, is not it impossible?\x02\x03",
            "#00008FBecause it is such a time\x01",
            "If you would rely on us ──\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x2)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00302F#11PHaha, of course I depend on you.\x02\x03",
            "#00303FI told you before … …\x01",
            "My uncle has a relationship with you.\x02\x03",
            "Where the old nest did so now\x01",
            "I do not have to bear that much.\x02\x03",
            "#00304FEating better than that now\x01",
            "Rest while resting … ….\x02\x03",
            "#00300F── Is it your first vote to prepare for tomorrow?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#5Pthat is……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10112FWell, that's true …!\x02\x03",
            "#10100FAre you hungry?\x01",
            "I will say that we can not fight!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00109FHuhu, you#4RRandy#To such toughness of\x01",
            "I always have been helped …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00202F……is not it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#11PWell, even today in the lake\x01",
            "I came across with the ridiculous guys.\x02\x03",
            "#10302FThe one who stopped eating early and was absent\x01",
            "It may be good for tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004F#5PThat's right.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00002F#11P── Okay.\x01",
            "Let's start a pot.\x02\x03",
            "#00004FKeyaが準備してくれたから\x01",
            "Meat, fish, vegetables ─ ─ Tuppery.\x02\x03",
            "#00000FEat lots, rest early … …\x01",
            "Let's prepare for tomorrow!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309F#11POh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10109FLet us eat\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00102FKeyaちゃん、後は私たちに任せて\x01",
            "Eat a lot of your stomach, do not you think?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x1)
    Sleep(100)

    ChrTalk(
        0xA,
        "#6P#01109F…… Well!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00202FZeitはお肉とお魚を\x01",
            "I will cool down later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01200F#11PGurururu …… won.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(23000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x80)
    SetChrBattleFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x80)
    SetChrBattleFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x80)
    SetChrBattleFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x80)
    SetChrBattleFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x80)
    SetChrBattleFlags(0x22, 0x8000)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    SetChrFlags(0x24, 0x80)
    SetChrBattleFlags(0x24, 0x8000)
    SetChrFlags(0x25, 0x80)
    SetChrBattleFlags(0x25, 0x8000)
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
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x103, 0x4)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x2C, 0x80)
    SetChrFlags(0x2D, 0x80)
    SetChrPos(0x26, 22900, 0, 12700, 0)
    SetChrPos(0x27, 22900, 0, 12700, 0)
    SetChrPos(0x28, 22900, 0, 12700, 0)
    SetChrPos(0x29, 22900, 0, 12700, 0)
    SetChrPos(0x2A, 22900, 0, 12700, 0)
    SetChrPos(0x2B, 22900, 0, 12700, 0)
    SetChrPos(0x2C, 22900, 0, 12700, 0)
    SetChrPos(0x2D, 22900, 0, 12700, 0)
    SetMapObjFrame(0xFF, "isu00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "isu00_sd", 0x1, 0x1)
    VolumeBGM(0x3C, 0x7D0)
    Sleep(2000)
    SetScenarioFlags(0x22, 4)
    NewScene("c010B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_23_9DA3 end

    def Function_24_ADCA(): pass

    label("Function_24_ADCA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50539.itc", 0x1E)
    LoadChrToIndex("apl/ch50006.itc", 0x1F)
    LoadChrToIndex("apl/ch51517.itc", 0x20)
    LoadChrToIndex("chr/ch30000.itc", 0x21)
    LoadChrToIndex("chr/ch20400.itc", 0x22)
    LoadChrToIndex("chr/ch21100.itc", 0x23)
    LoadChrToIndex("chr/ch20100.itc", 0x24)
    LoadChrToIndex("chr/ch21000.itc", 0x25)
    LoadChrToIndex("chr/ch21400.itc", 0x26)
    LoadChrToIndex("chr/ch08201.itc", 0x27)
    LoadEffect(0x0, "event\\ev500_00.eff")
    SoundLoad(803)
    SoundLoad(852)
    SoundLoad(3621)
    SoundLoad(3622)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    SetChrPos(0x0, 4000, 850, 15000, 0)
    SetChrPos(0x1, 4000, 850, 15000, 0)
    SetChrPos(0x2, 4000, 850, 15000, 0)
    SetChrPos(0x3, 4000, 850, 15000, 0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 200, 0, 1600, 180)
    SetChrChipByIndex(0x12, 0x21)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 2200, 0, 2300, 225)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -1300, 0, 4400, 180)
    SetChrChipByIndex(0xD, 0x22)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 400, 0, 4000, 180)
    SetChrChipByIndex(0xE, 0x23)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 1700, 0, 4400, 180)
    SetChrChipByIndex(0xF, 0x24)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 900, 0, 5600, 180)
    SetChrChipByIndex(0x10, 0x25)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 3700, 0, 5400, 180)
    SetChrChipByIndex(0x11, 0x26)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 4700, 0, 5400, 180)
    OP_7D(0xFF, 0xE6, 0xDC, 0x0, 0x0)
    OP_68(1000, 1000, 0, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20400, 0)
    OP_68(1020, 1000, 3180, 4000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0xD,
        (
            "#5PYes, the outside world\x01",
            "What's going on ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5P…… My husband ……\x01",
            "I wonder if he is safe ……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x0, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "#12P#01003FOh, everyone calm down.\x02\x03",
            "#01002FAccording to the contact I entered now\x01",
            "Mysterious armed group\x01",
            "It is said that we started withdrawing.\x02\x03",
            "As soon as safety is confirmed,\x01",
            "You can return to the house properly.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B11E():
        TurnDirection(0xE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_B11E)
    Sleep(30)

    def lambda_B12E():
        TurnDirection(0x10, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_B12E)
    Sleep(30)

    def lambda_B13E():
        TurnDirection(0x11, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_B13E)
    Sleep(30)
    WaitChrThread(0xE, 0)
    WaitChrThread(0x10, 0)
    WaitChrThread(0x11, 0)

    ChrTalk(
        0xE,
        "#5PThat's right! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5POh, the goddess#4REidos#Yo\x01",
            "I appreciate your protection …!\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(20000, 1000)

    def lambda_B1BA():
        OP_9A(0xFE, 0x8, 0x4B0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B1BA)
    WaitChrThread(0xA, 1)

    ChrTalk(
        0xA,
        (
            "#5P#01112F#30W___ ___ 0\x01",
            "Are you alright, are you all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#01006FOh, for now.\x02\x03",
            "#01001FThe guy of Lloyd's … …\x01",
            "I hope it is safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#01104F#30W─ ─ Yes, it's okay.\x02\x03",
            "#01121FIf Lloyd's of us, then it's fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#01005FOh, oh … That's right.\x02\x03",
            "#01002FWhatever you say\x01",
            "They are also growing up.\x02\x03",
            "#01004FPossibly\x01",
            "From the Sergey group in the past ──\x02",
        )
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(250)
    Sound(531, 0, 50, 0)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    Sleep(300)
    OP_93(0x8, 0x10E, 0x1F4)
    Sleep(150)
    Fade(250)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x2)
    Sound(802, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x8, 0x3)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#11P#01003FYes, here Support Section -\x02\x03",
            "#01005F… …. Oh, Dudley?\x01",
            "How is your appearance?\x02\x03",
            "#01001F…………what?\x01",
            "It is a flying boat of a hunter … …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xA)
    Sleep(500)

    def lambda_B46B():
        OP_96(0xFE, 0xFFFFFCE0, 0x0, 0xCE4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B46B)
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0x0, 0x1F4)
    SetChrChipByIndex(0xA, 0x27)
    SetChrSubChip(0xA, 0x0)

    def lambda_B498():
        OP_96(0xFE, 0x190, 0x0, 0x1A90, 0xDAC, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B498)
    WaitChrThread(0xA, 1)
    OP_68(1000, 2000, 3000, 3000)

    def lambda_B4C7():
        OP_96(0xFE, 0x514, 0x352, 0x2BC0, 0xDAC, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B4C7)
    WaitChrThread(0xA, 1)

    def lambda_B4E5():
        OP_96(0xFE, 0x514, 0xFA0, 0x3B60, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B4E5)
    FadeToDark(2000, 0, -1)
    OP_0D()
    WaitChrThread(0xA, 1)
    OP_6F(0x79)
    Sleep(1000)
    OP_68(-300, 800, 72310, 0)
    MoveCamera(35, 19, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0xA, 1400, 0, 70000, 0)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    OP_68(-260, 1300, 72270, 2500)

    def lambda_B574():
        OP_96(0xFE, 0xFFFFFED4, 0x0, 0x11A6C, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B574)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0x0, 0x1F4)
    OP_6F(0x79)
    Sleep(300)
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xA)
    Sleep(500)
    Fade(500)
    SetCameraDistance(19500, 800)
    Sound(928, 0, 60, 0)
    Sound(852, 2, 100, 0)
    PlayEffect(0x0, 0x0, 0xA, 0x0, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x79)
    SetCameraDistance(18500, 30000)
    Sleep(500)

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#01119F#40W#11P………………………………\x02\x03",
            "#01118F#40WAfter all …………\x02\x03",
            "#01120F#40WAfter all it does not matter how\x01",
            "…… This seems to be the best … …\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopEffect(0x0, 0x2)
    StopSound(852, 1000, 100)
    Sleep(1300)

    ChrTalk(
        0xA,
        "#01123F#40W#11P……………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0xA, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Sound(802, 0, 100, 0)
    Fade(250)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0xA, 0x20)
    Sleep(500)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)
    SetChrSubChip(0xA, 0x1)
    Sleep(500)
    SetCameraDistance(18000, 20000)

    ChrTalk(
        0xA,
        (
            "#01112F#30W#11P#15A………Hello………?\x02\x03",
            "#01108F#40W#25A………………Yup………\x01",
            "…………Yup…………………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xA)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xA,
        "#01121F#3621V#40W#11P#20A── All right.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(18000, 3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xA,
        (
            "#3622V#30W#40AAlready……\x01",
            "Because I was able to make a proper decision.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    StopBGM(0x1770)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(2000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    OP_32(0xFF, 0xFE, 0x0)
    OP_24(0x323)
    OP_24(0x354)
    Sleep(500)
    SetScenarioFlags(0x22, 0)
    NewScene("c110D", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_24_ADCA end

    def Function_25_B8DB(): pass

    label("Function_25_B8DB")

    TalkBegin(0xFF)
    OP_E5(0xA)
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_E5(0x5)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B8F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BFA6")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "OP_E5(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_B930"),
        (1, "loc_BAE2"),
        (2, "loc_BF8A"),
        (3, "loc_BF92"),
        (SWITCH_DEFAULT, "loc_BFA1"),
    )


    label("loc_B930")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_B943")
    OP_2B(0x94, 0xFFFF)
    Jump("loc_BADD")

    label("loc_B943")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B95E")
    OP_2B(0x8E, 0x8F, 0x90, 0x91, 0x92, 0xFFFF)
    Jump("loc_BADD")

    label("loc_B95E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_B9B7")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Automatic announcement")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Currently, there is no support request.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_BADD")

    label("loc_B9B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_B9D2")
    OP_2B(0x8B, 0x8C, 0x88, 0x80, 0x83, 0xFFFF)
    Jump("loc_BADD")

    label("loc_B9D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_BA0D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_B9FB")
    OP_2B(0x85, 0x86, 0x87, 0x88, 0x80, 0x83, 0xFFFF)
    Jump("loc_BA08")

    label("loc_B9FB")

    OP_2B(0x85, 0x86, 0x88, 0x80, 0x83, 0xFFFF)

    label("loc_BA08")

    Jump("loc_BADD")

    label("loc_BA0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_BA26")
    OP_2B(0x80, 0x81, 0x82, 0x83, 0xFFFF)
    Jump("loc_BADD")

    label("loc_BA26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_BA34")
    Jump("loc_BADD")

    label("loc_BA34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_BA51")
    OP_2B(0x79, 0x7A, 0x7B, 0x77, 0x71, 0x72, 0xFFFF)
    Jump("loc_BADD")

    label("loc_BA51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_END)), "loc_BA6E")
    OP_2B(0x74, 0x75, 0x76, 0x77, 0x71, 0x72, 0xFFFF)
    Jump("loc_BADD")

    label("loc_BA6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_BA87")
    OP_2B(0x6F, 0x70, 0x71, 0x72, 0xFFFF)
    Jump("loc_BADD")

    label("loc_BA87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_BABB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_END)), "loc_BAAB")
    OP_2B(0x6A, 0x6B, 0x6C, 0x6D, 0x67, 0xFFFF)
    Jump("loc_BAB6")

    label("loc_BAAB")

    OP_2B(0x6A, 0x6B, 0x6C, 0x67, 0xFFFF)

    label("loc_BAB6")

    Jump("loc_BADD")

    label("loc_BABB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 7)), scpexpr(EXPR_END)), "loc_BAD2")
    OP_2B(0x65, 0x66, 0x67, 0xFFFF)
    Jump("loc_BADD")

    label("loc_BAD2")

    OP_2B(0x65, 0x66, 0x67, 0x68, 0xFFFF)

    label("loc_BADD")

    Jump("loc_BFA1")

    label("loc_BAE2")

    SetMapFlags(0x40000000)
    OP_E5(0x7)
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BBBF")
    SetChrName("Automatic announcement")

    AnonymousTalk(
        0xFF,
        "This is Crosbell Police.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E5(0x4)"), scpexpr(EXPR_END)), "loc_BB98")

    AnonymousTalk(
        0xFF,
        "We will receive reports.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E5(0xC)
    SetChrName("Automatic announcement")

    AnonymousTalk(
        0xFF,
        (
            "Finish report processing.\x01",
            "Thank you for your hard work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BBBA")

    label("loc_BB98")


    AnonymousTalk(
        0xFF,
        "There are no reportable requests.\x02",
    )

    CloseMessageWindow()

    label("loc_BBBA")

    Jump("loc_BF7C")

    label("loc_BBBF")

    SetChrName("Receptionist franc")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BC13")
    Sound(3062, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        "Yes, here is the crossbell police ~!\x02",
    )

    CloseMessageWindow()
    Jump("loc_BC3F")

    label("loc_BC13")

    Sound(3061, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        "Everyone, thank you very much.\x02",
    )

    CloseMessageWindow()

    label("loc_BC3F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E5(0x4)"), scpexpr(EXPR_END)), "loc_BE88")
    Sound(3067, 255, 100, 0)
    SetChrName("Receptionist franc")

    AnonymousTalk(
        0xFF,
        "Well then we will receive a report ~.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E5(0xC)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BE13")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_END)),
        (14, "loc_BCB0"),
        (13, "loc_BCFA"),
        (12, "loc_BD42"),
        (SWITCH_DEFAULT, "loc_BD8C"),
    )


    label("loc_BCB0")

    Sound(3075, 255, 100, 0)
    SetChrName("Receptionist franc")

    AnonymousTalk(
        0xFF,
        (
            "Class 1st--\x01",
            "Mr. Lloyd is too amazing!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BD8C")

    label("loc_BCFA")

    Sound(3074, 255, 100, 0)
    SetChrName("Receptionist franc")

    AnonymousTalk(
        0xFF,
        (
            "Class 2nd -\x01",
            "Mr. Lloyd is amazing!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BD8C")

    label("loc_BD42")

    Sound(3073, 255, 100, 0)
    SetChrName("Receptionist franc")

    AnonymousTalk(
        0xFF,
        (
            "Class 3rd\x01",
            "Mr. Lloyd, you did it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BD8C")

    label("loc_BD8C")

    Sound(3076, 255, 100, 0)
    SetChrName("Receptionist franc")

    AnonymousTalk(
        0xFF,
        (
            "Items of award also soon\x01",
            "I will deliver to you ~!\x02",
        )
    )

    CloseMessageWindow()
    Sound(3077, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            "Congratulations ~!\x01",
            "Thank you again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BE80")

    label("loc_BE13")

    Sound(3078, 255, 100, 0)
    SetChrName("Receptionist franc")

    AnonymousTalk(
        0xFF,
        "The report is over.\x02",
    )

    CloseMessageWindow()
    Sound(3079, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            "Then, once you have reached the request\x01",
            "nice to meet you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BE80")

    SetScenarioFlags(0x0, 6)
    Jump("loc_BF7C")

    label("loc_BE88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_BF0D")
    Sound(3063, 255, 100, 0)
    SetChrName("Receptionist franc")

    AnonymousTalk(
        0xFF,
        (
            "There …\x01",
            "It was just reported earlier?\x02",
        )
    )

    CloseMessageWindow()
    Sound(3064, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        "Also, I hope you will be able to fulfill your request.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BF7C")

    label("loc_BF0D")

    Sound(3065, 255, 100, 0)
    SetChrName("Receptionist franc")

    AnonymousTalk(
        0xFF,
        (
            "There, reportable\x01",
            "It seems there is no request for it ~.\x02",
        )
    )

    CloseMessageWindow()
    Sound(3066, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        "Thank you again.\x02",
    )

    CloseMessageWindow()

    label("loc_BF7C")

    OP_57(0x0)
    OP_E5(0x8)
    ClearMapFlags(0x40000000)
    Jump("loc_BFA1")

    label("loc_BF8A")

    Call(0, 26)
    Jump("loc_BFA1")

    label("loc_BF92")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BFA1")

    label("loc_BFA1")

    Jump("loc_B8F7")

    label("loc_BFA6")

    OP_E5(0x6)
    OP_C9(0x1, 0x4)
    OP_C9(0x1, 0x100)
    FadeToBright(300, 0)
    OP_0D()
    OP_E5(0xB)
    TalkEnd(0xFF)
    Return()

    # Function_25_B8DB end

    def Function_26_BFC4(): pass

    label("Function_26_BFC4")

    OP_E5(0x6)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 3)), scpexpr(EXPR_END)), "loc_BFE6")
    SetScenarioFlags(0x2A, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BFE6")
    ClearScenarioFlags(0x2A, 0)

    label("loc_BFE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 4)), scpexpr(EXPR_END)), "loc_C003")
    SetScenarioFlags(0x2A, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C003")
    ClearScenarioFlags(0x2A, 1)

    label("loc_C003")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 5)), scpexpr(EXPR_END)), "loc_C020")
    SetScenarioFlags(0x2A, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C020")
    ClearScenarioFlags(0x2A, 2)

    label("loc_C020")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 6)), scpexpr(EXPR_END)), "loc_C03D")
    SetScenarioFlags(0x2A, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C03D")
    ClearScenarioFlags(0x2A, 3)

    label("loc_C03D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 7)), scpexpr(EXPR_END)), "loc_C05A")
    SetScenarioFlags(0x2A, 4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C05A")
    ClearScenarioFlags(0x2A, 4)

    label("loc_C05A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 0)), scpexpr(EXPR_END)), "loc_C077")
    SetScenarioFlags(0x2A, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C077")
    ClearScenarioFlags(0x2A, 5)

    label("loc_C077")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 1)), scpexpr(EXPR_END)), "loc_C083")
    SetScenarioFlags(0x2A, 6)

    label("loc_C083")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C0D5")
    RunExpression(0x7, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x10, 0x3, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    StopBGM(0x0)
    Jump("loc_C150")

    label("loc_C0D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C127")
    OP_24(0x80)
    RunExpression(0x7, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x10, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1F()
    Sound(128, 1, 50, 0)
    Jump("loc_C150")

    label("loc_C127")

    RunExpression(0x7, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x10, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1F()

    label("loc_C150")

    Return()

    # Function_26_BFC4 end

    SaveToFile()

Try(main)
