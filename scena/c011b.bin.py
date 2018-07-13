from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Chief Sergei",           # 1
        "Zeit",                   # 2
        "KeA",                    # 3
        "Shirley",                # 4
        "Detective Dudley",       # 5
        "Citizen",                # 6
        "Citizen",                # 7
        "Citizen",                # 8
        "Citizen",                # 9
        "Citizen",                # 10
        "Policeman",              # 11
        "食器",                   # 12
        "食器",                   # 13
        "食器",                   # 14
        "食器",                   # 15
        "食器",                   # 16
        "食器",                   # 17
        "食器",                   # 18
        "食器",                   # 19
        "食器",                   # 20
        "食器",                   # 21
        "食器",                   # 22
        "食器",                   # 23
        "食器",                   # 24
        "食器",                   # 25
        "食器",                   # 26
        "食器",                   # 27
        "食器",                   # 28
        "食器",                   # 29
        "食器",                   # 30
        "椅子",                   # 31
        "椅子",                   # 32
        "椅子",                   # 33
        "椅子",                   # 34
        "椅子",                   # 35
        "椅子",                   # 36
        "椅子",                   # 37
        "椅子",                   # 38
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
        "Function_5_9B3",          # 05, 5
        "Function_6_B75",          # 06, 6
        "Function_7_E31",          # 07, 7
        "Function_8_E69",          # 08, 8
        "Function_9_306B",         # 09, 9
        "Function_10_30FA",        # 0A, 10
        "Function_11_4D44",        # 0B, 11
        "Function_12_4D72",        # 0C, 12
        "Function_13_4DC3",        # 0D, 13
        "Function_14_4E14",        # 0E, 14
        "Function_15_4E6C",        # 0F, 15
        "Function_16_4EB6",        # 10, 16
        "Function_17_4EDC",        # 11, 17
        "Function_18_5802",        # 12, 18
        "Function_19_583F",        # 13, 19
        "Function_20_6E66",        # 14, 20
        "Function_21_94BF",        # 15, 21
        "Function_22_952F",        # 16, 22
        "Function_23_AA15",        # 17, 23
        "Function_24_BB31",        # 18, 24
        "Function_25_C686",        # 19, 25
        "Function_26_CE14",        # 1A, 26
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_92A")

    ChrTalk(
        0x8,
        (
            "#01000FI'll contact the mayor and che CGFs\x01",
            "about terrorists information.\x02\x03",
            "Dudley, I leave to you to\x01",
            "keep my guys safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00603FYes, please leave them to me.\x02\x03",
            "#00601F...Come now, let's go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FSir!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_9AF")

    label("loc_92A")


    ChrTalk(
        0x8,
        (
            "#01000FI don't know if something's\x01",
            "happened in the Geofront,\x01",
            "but be very careful.\x02\x03",
            "Dudley, I leave to you to\x01",
            "keep my guys safe.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9AF")

    TalkEnd(0xFE)
    Return()

    # Function_4_83F end

    def Function_5_9B3(): pass

    label("Function_5_9B3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B07")

    ChrTalk(
        0xA,
        (
            "#01100FEveryone, have a safe trip!\x02\x03",
            "#01109FEhehe, you be careful too, Dudley, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#00603FI told you to not address me so casually...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#01105FUhm?\x02",
    )

    CloseMessageWindow()
    OP_63(0x10A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x10A,
        (
            "#00606F...Damn, whatever!\x01",
            "You guys, let's go at once!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F(Hmm, as expected, not even\x01",
            "Mr. Dudley is a match for KeA.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_B71")

    label("loc_B07")


    ChrTalk(
        0xA,
        (
            "#01109FEveryone, have a safe trip!\x02\x03",
            "Ehehe, you be careful too, Dudley, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#00603F(Honestly...)\x02",
    )

    CloseMessageWindow()

    label("loc_B71")

    TalkEnd(0xFE)
    Return()

    # Function_5_9B3 end

    def Function_6_B75(): pass

    label("Function_6_B75")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E11")

    ChrTalk(
        0x9,
        "#01200FGrrrrowl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00603FHmph, a self-important wolf as always.\x02\x03",
            "#00600FStill, since you're treated like a police dog,\x01",
            "there're times when we need your help.\x01",
            "Be prepared to sortie at any time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01200F...Woof.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C97")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_C97")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CCB")
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_CCB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CFF")
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_CFF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D33")
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_D33")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D67")
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_D67")

    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#00306F(How can he call self-\x01",
            "important others, right...?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(*giggle*, we can't do anything about it,\x01",
            "since it's Mr. Dudley way to encourage.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_E2D")

    label("loc_E11")


    ChrTalk(
        0x9,
        "#01200FGrrrowl...woof.\x02",
    )

    CloseMessageWindow()

    label("loc_E2D")

    TalkEnd(0xFE)
    Return()

    # Function_6_B75 end

    def Function_7_E31(): pass

    label("Function_7_E31")

    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00000FThis is Tio's room.\x01",
            "Let's not enter.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_7_E31 end

    def Function_8_E69(): pass

    label("Function_8_E69")

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
            "#01003F#11PHm, hm...\x02\x03",
            "#01000FRight.\x01",
            "They should be coming\x01",
            "back by now──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(3054, 255, 80, 0)

    ChrTalk(
        0x9,
        "#01200F#12PWoof.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x8, 0x10E, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#01005F#11P...Oh. \x01",
            "They just came back.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x101,
        "Lloyd's Voice",
        "We're back.\x02",
    )

    CloseMessageWindow()
    OP_68(4100, 1750, 10400, 2500)
    SetCameraDistance(25000, 2500)
    Sleep(1000)
    OP_90(0x101, 1700, 4850, 14100, 180)
    BeginChrThread(0x101, 3, 0, 9)

    def lambda_118A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_118A)
    Sleep(400)

    def lambda_119E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_119E)
    Sleep(600)

    def lambda_11B2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x153, 2, lambda_11B2)
    Sleep(400)

    def lambda_11C6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_11C6)
    Sleep(600)

    def lambda_11DA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_11DA)
    WaitChrThread(0x101, 0)

    def lambda_11EF():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_11EF)
    WaitChrThread(0x102, 0)

    def lambda_1200():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1200)
    WaitChrThread(0x153, 0)

    def lambda_1211():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x153, 2, lambda_1211)
    WaitChrThread(0x109, 0)

    def lambda_1222():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1222)
    WaitChrThread(0x105, 0)

    def lambda_1233():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_1233)

    ChrTalk(
        0x153,
        "#5P#01110FChief, we're home!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105FOh, are you at the phone?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#01004F#12PWell, it doesn't matter.\x02",
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
            "#01002F#6PHey, boot up that\x01",
            "terminal at once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FHuh, yes...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FDid a message come from\x01",
            "police headquarters?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01003F#6PYou'll see when you boot it up.\x02\x03",
            "#01001FHey, new guys and\x01",
            "KeA too, come here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#5P#01100FHm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10105FY-Yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FThere seems to be something.\x02",
    )

    CloseMessageWindow()

    def lambda_1411():
        OP_97(0x101, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1411)
    Sleep(250)

    def lambda_142E():
        OP_97(0x153, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 0, lambda_142E)
    Sleep(250)

    def lambda_144B():
        OP_97(0x102, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_144B)
    Sleep(250)

    def lambda_1468():
        OP_97(0x109, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1468)
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
        "#5P#00001FUhhm...\x02",
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
        "#00005F!!\x02",
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
        "#01109FAah, it's Tio!\x02",
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
            "#2668V#40W...Good evening.\x01",
            "It has been a long time.\x07\x00\x02",
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
            "#00002FTio...!\x01",
            "Why did you...\x02\x03",
            "Are you perhaps coming\x01",
            "back to Crossbell!?\x02",
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
            "#30W...I will be still staying at the Epstein\x01",
            "Foundation research lab in Leman.\x02\x03",
            "Since my scheduled return is\x01",
            "going to be delayed a little bit...\x02\x03",
            "I selfishly asked to\x01",
            "let me use the line.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x101,
        "#00000FI see...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00109FTio... \x01",
            "I'm happy to see your face.\x02\x03",
            "#00105FOh, but the orbal net...\x01",
            "Wasn't it impossible to connect at\x01",
            "the network outside Crossbell...?\x02",
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
            "Yes, properly speaking, if you don't \x01",
            "connect by wire it is not possible to \x01",
            "process a huge volume of information.\x02\x03",
            "However, at present, remote connection\x01",
            "tests between the Foundation and IBC \x01",
            "are progressing.\x02\x03",
            "Well, about 10 powerful wireless\x01",
            "boosters have been placed between\x01",
            "Leman and Crossbell...\x02\x03",
            "And that is why video and\x01",
            "voice can be sent like this.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x102,
        "#00102FI see...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        "#00004FTechnical progresses are amazing...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x153,
        (
            "#01110FHey, hey Tio!\x02\x03",
            "You said you're going to come\x01",
            "back later, but when is it?\x02",
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
            "I think I will be able to come back\x01",
            "there at the end of the month, or \x01",
            "the beginning of the next one.\x02\x03",
            "Until then, I think I will\x01",
            "endure with some doses of\x01",
            "KeA in this way.\x02\x03",
            "So, KeA, please\x01",
            "show yourself more. \x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x153,
        (
            "#01109FEhehe...yes!\x02\x03",
            "#01110FHey now, you too Zeit.\x01",
            "Show your face to Tio.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x9,
        "#01200FUrrrol...woof.\x02",
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
            "Yes, I'm fine.\x01",
            "I'm doing well.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x101,
        "#00002FHa ha...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00104F*giggle*... The orbal net\x01",
            "has also this kind of benefit.\x02",
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
            "By the way, it appears that even\x01",
            "Mr. Randy is not back yet...\x02\x03",
            "And it looks like Miss Noｱl and\x01",
            "Mr. Wazy have joined already?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x101,
        (
            "#00000FYeah, they started working\x01",
            "for us just today.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x109,
        (
            "#10102FEh eh...\x01",
            "Tio, long time no see!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x105,
        (
            "#10302FHey.\x01",
            "I'll be intruding for a while.\x02",
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
            "Uh uh...\x01",
            "Long time no see too.\x02\x03",
            "At any rate, I can understand\x01",
            "Miss Noｱl's transferring in, but...\x02\x03",
            "Having Mr. Wazy over there\x01",
            "makes the scene a little strange.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x105,
        "#10309FAhaha, I agree too.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x109,
        (
            "#10106FGeez...\x01",
            "It's no laughing matter.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00004FHa ha, well, for the time being this\x01",
            "lineup will have to do somehow.\x02\x03",
            "#00002FStill, Tio...\x01",
            "Come back quickly!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00102FYes, without you here, Tio, this\x01",
            "is not the real Support Section\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x153,
        "#01109FYes, yes!\x02",
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
            "*chuckle*... Then, I'll do my best\x01",
            "to be able to come back quicker.\x02\x03",
            "Actually, I was also thinking to call \x01",
            "Jona to join this conversation, but...\x02\x03",
            "It appears he kept doing all nighters and\x01",
            "although I called him, he didn't wake up.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x101,
        (
            "#00000FIs that so...?\x01",
            "He seems to be doing his best too.\x02\x03",
            "#00006FWell, although it appears he's doing\x01",
            "it to make up for the damage he \x01",
            "caused to the Foundation.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00104FPay attention that he doesn't\x01",
            "exaggerate in doing things.\x02\x03",
            "#00100FAnd naturally, you\x01",
            "too Tio, alright?\x02",
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
            "Yes, understood.\x07\x00\x02",
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
            "...Sorry, it seems\x01",
            "it is time to go.\x02\x03",
            "I asked for a big favor to let me use\x01",
            "the line for live tests, after all...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x101,
        "#00001FI see...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00106FI wanted to talk to you\x01",
            "more, what a pity...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x8,
        (
            "#01004FWell, you'll have other chances, I think.\x02\x03",
            "#01002FTio, contact us again\x01",
            "when it's possible.\x02",
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
            "Roger.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 4)), scpexpr(EXPR_END)), "loc_26CB")

    AnonymousTalk(
        0x101,
        (
            "#00004F...See you, Tio.\x02\x03",
            "#00002FWhen you come back, I'll keep\x01",
            "the promise I made you back then,\x02",
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
            "Yes...\x01",
            "I am looking forward to it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x153,
        "#01111FPromise?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00104FSomehow I'm a little worried about that...\x01",
            "Oh, well.\x02\x03",
            "#00102FTio, please contact us again.\x01\x02",
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
            "#10109FBe well!\x01",
            "Watch your health!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_274F")

    label("loc_26CB")


    AnonymousTalk(
        0x101,
        (
            "#00002FBye, Tio.\x01",
            "Please watch your health.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00102FPlease contact us\x01",
            "again if you want.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x109,
        "#10109FTio, be well!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_274F")


    AnonymousTalk(
        0x105,
        "#10302FAdiｾs, have a pleasant night.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x9,
        "#01200FGrrowl...woof.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x153,
        "#01110FSee you, Tio!\x02",
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
            "Yes, see you again.\x01",
            "Good night.\x07\x00\x02",
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
        "#6P#01106FShe's vanished...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008FYeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00104F...For some reason, seeing her face made\x01",
            "me want to meet her all the more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10302FUh uh, youth.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10109FEh eh, in the Support Section\x01",
            "you're all good friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FHa ha, although in the beginning\x01",
            "we were complete strangers.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#00000FOh, right, Chief.\x01",
            "Sorry for being back late.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2A26():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2A26)
    Sleep(50)

    def lambda_2A36():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2A36)
    Sleep(50)

    def lambda_2A46():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2A46)
    Sleep(50)

    def lambda_2A56():
        TurnDirection(0x153, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x153, 0, lambda_2A56)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x153, 0)

    ChrTalk(
        0x8,
        (
            "#01004FWell, don't mind it.\x02\x03",
            "#01000FI'll hear your\x01",
            "report later...\x02\x03",
            "What about dinner?\x02",
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
        "#11P#00011FR-Right, I forgot!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#6P#00108FNow that you mention it, we haven't\x01",
            "decided cooking turns among us yet...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2B8B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2B8B)
    Sleep(100)

    def lambda_2B9B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x153, 2, lambda_2B9B)
    WaitChrThread(0x109, 2)

    ChrTalk(
        0x109,
        (
            "#6P#10105FI see, in the Special Support\x01",
            "Section you take turns to cook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10305FOh, is that so?\x02\x03",
            "#10306F...Hm.\x01",
            "It's a bit of a pain.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12B, 3)), scpexpr(EXPR_END)), "loc_2D58")

    ChrTalk(
        0x101,
        (
            "#00003FBecause you've joined the SSS, you'll\x01",
            "have to properly do your share too.\x02\x03",
            "#00000FYou unexpectedly look like\x01",
            "to know how to cook...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FWell, I must admit I'm not bad.\x02\x03",
            "#10300FAlthough since it's a bother, I had\x01",
            "Abbas do it most of the time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EA7")

    label("loc_2D58")


    ChrTalk(
        0x101,
        (
            "#00003FBecause you've joined the SSS, you'll\x01",
            "have to properly do your share too.\x02\x03",
            "#00000FWe have just gotten a new recipe\x01",
            "notebook, so I can teach you if \x01",
            "you're not good at it, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FI'm happy to hear that, but\x01",
            "I'm not bad at cooking.\x02\x03",
            "#10309FAlthough since it's a bother, I had\x01",
            "Abbas do it most of the time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EA7")


    ChrTalk(
        0x101,
        (
            "#00013FHey, in that case\x01",
            "don't complain!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00109F*giggle*, well, should we divide\x01",
            "work among us just for today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10102FThen, something that can be made\x01",
            "quick and easy seems it would be nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#6P#01109FKeA will help too!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01006F...Oh boy. I guess I'll wait\x01",
            "while taking a smoke.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#6P#01203FGrrowl...woof.\x02",
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

    # Function_8_E69 end

    def Function_9_306B(): pass

    label("Function_9_306B")


    def lambda_3070():
        OP_97(0x101, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3070)
    Sleep(200)

    def lambda_308D():
        OP_97(0x102, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_308D)
    Sleep(200)

    def lambda_30AA():
        OP_97(0x153, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 0, lambda_30AA)
    Sleep(200)

    def lambda_30C7():
        OP_97(0x109, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_30C7)
    Sleep(200)

    def lambda_30E4():
        OP_97(0x105, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_30E4)
    Return()

    # Function_9_306B end

    def Function_10_30FA(): pass

    label("Function_10_30FA")

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
        "#12P#00011FWha...!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 3)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x105, 3)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        "#6P#00105FRandy's cousin...?\x02",
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
            "#11P#04609F#3942V#30WEhehe, hello, nice to meet you.\x01",
            "I'm Shirley Orlandooo.\x02\x03",
            "#04602F#3943VYou're laaate.\x01",
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
            "#6P#00301F#30W...You...\x02\x03",
            "What the heck did you come for...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11P#04605FOh, you're so cooold, Randy bro.\x02\x03",
            "#04606FAren't you being too cold towards your\x01",
            "cute cousin you haven't seen in 2 years?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303F#30WCut it out and answer me...\x01",
            "What did you come here to do?\x02\x03",
            "#00311FNo── what were you doing here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#11P#04604FHu hu...\x02",
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
            "#3944V#40W──You've become weak, Randy bro.\x02\x03",
            "#3945V#30WIf I had set antipersonnel traps\x01",
            "you'd have been turned into minced \x01",
            "meat the moment you'd entered.\x02\x03",
            "#3946VWhen did you become\x01",
            "such a half-wit?\x02",
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
        "#6P#00311F#30W............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00101FY-You...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#N#10107FWhat're you suddenly...!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0xB,
        (
            "#11P#04612FHu hu, no need to worry,\x01",
            "I didn't set any traps.\x02\x03",
            "#04602FAlthough if Randy bro had been alone,\x01",
            "we'd have had that kind of fun too.\x02\x03",
            "#04604FAs long as we aren't "at war",\x01",
            "I don't want to involve civilians.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00110F......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#01105F#6P#NEeeh...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#6P#N#10306F*sigh*...\x01",
            "We have another rampant kid here.\x02",
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
            "#12P#00003F──You.\x01",
            "Shirley, right?\x02\x03",
            "#00001FAllow me to introduce myself...\x01",
            "I'm Lloyd Bannings from the Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11P#04602FOh, hello, nice to meet you.\x02\x03",
            "#04609FSorry for the other day, 'k?\x01",
            "I bit your earlobe unintentionally...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006F...That aside.\x02\x03",
            "#00013FThis is a detached Crossbell police office,\x01",
            "and even the sofa you're sitting on\x01",
            "was provided with public funds.\x02\x03",
            "And about traps, involving and what not...\x01",
            "Could you hold back from careless\x01",
            "speech in front of the child?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11P#04612FAhaha, sorry, sorry.\x02\x03",
            "#04611FBecause I missed him, I unintentionally\x01",
            "want to be playful with bro, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306F...Hmph.\x01",
            "As if you'd be missing me.\x02\x03",
            "#00301FThe main point is that you came to call\x01",
            "for me as uncle's messenger, right?\x02",
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

    def lambda_3C6B():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3C6B)
    Sleep(50)

    def lambda_3C7B():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3C7B)
    Sleep(50)

    def lambda_3C8B():
        TurnDirection(0x109, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3C8B)
    Sleep(50)

    def lambda_3C9B():
        TurnDirection(0x105, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3C9B)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        "#12P#00005FWhat...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00101FThen...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#11P#04604FHu hu, correct.\x02",
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
            "#04602F#11PDidn't papa tell you that\x01",
            "you'd have talked one day?\x02\x03",
            "He said that tomorrow we're going\x01",
            "to be busy so what about tonight?\x02\x03",
            "#04605FAh, you can even refuse, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FHah! In case I refused he\x01",
            "wouldn't stop at anything, right?\x02\x03",
            "#00311FI can see right through\x01",
            "how you guys do things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#04609F#11PHu hu. It seems you've\x01",
            "gotten back into your stride.\x02\x03",
            "#04602FPapa said he'll go on ahead at\x01",
            ""Neue-Blanc", what will you do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00304FHmph, fine.\x02",
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
            "#5P#00300FEveryone, sorry but I won't\x01",
            "join you for dinn──\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x79)
    WaitChrThread(0xA, 3)

    ChrTalk(
        0xA,
        (
            "#6P#01101FHey, hey Randy.\x02\x03",
            "Could this miss be\x01",
            "a bad person?\x02",
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

    def lambda_404B():
        TurnDirection(0x104, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_404B)
    Sleep(50)

    def lambda_405B():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_405B)
    Sleep(50)

    def lambda_406B():
        TurnDirection(0x102, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_406B)
    Sleep(50)

    def lambda_407B():
        TurnDirection(0x109, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_407B)
    Sleep(50)

    def lambda_408B():
        TurnDirection(0x105, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_408B)
    Sleep(50)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        "#11P#00011FHey, KeA...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00107FKeA, stand back...!\x02",
    )

    CloseMessageWindow()
    OP_68(3920, 800, 5320, 1000)
    MoveCamera(42, 20, 0, 1000)
    OP_6E(400, 1000)
    SetCameraDistance(24000, 1000)

    def lambda_411D():
        OP_95(0xFE, 1400, 0, 5500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_411D)
    Sleep(300)

    def lambda_413A():
        OP_95(0xFE, 1800, 0, 4300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_413A)
    WaitChrThread(0x102, 1)

    def lambda_4158():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4158)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0xA, 500)

    def lambda_4170():
        OP_96(0xFE, 0x1F4, 0x0, 0x13EC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4170)

    def lambda_418A():
        OP_96(0xFE, 0x384, 0x0, 0xF3C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_418A)

    def lambda_41A4():
        OP_96(0xFE, 0x3E8, 0x0, 0x12C0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_41A4)
    Sleep(300)

    def lambda_41C1():
        OP_95(0xFE, 1300, 0, 2700, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_41C1)
    Sleep(300)

    def lambda_41DE():
        OP_95(0xFE, 2200, 0, 2500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_41DE)
    WaitChrThread(0x101, 1)

    def lambda_41FC():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_41FC)

    ChrTalk(
        0xB,
        (
            "#04606F#11PCalling me a bad person is cruel.\x02\x03",
            "#04605FBy the way, who's that kid!?\x01",
            "She's totally cute!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#6P#01105FHm?\x02",
    )

    CloseMessageWindow()

    def lambda_4288():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4288)
    Sleep(100)

    def lambda_4298():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4298)

    def lambda_42A5():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_42A5)
    WaitChrThread(0x104, 2)
    Sleep(150)

    ChrTalk(
        0x104,
        (
            "#6P#00303FA kid we're looking after here.\x02\x03",
            "#00312F#30W──Lay a hand on her and I'll kill you.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x32, 0x0, 0xBB8, 0x96)

    ChrTalk(
        0x101,
        "#6P#00013F...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00108F......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#04612F#11PAhaha, got it.\x02\x03",
            "#04602FAt least I'll refrain from\x01",
            "blowing up this building.\x02\x03",
            "#04609FAh, that's a joke, of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10106F(W-What a conversation...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10308F(This is bad for the heart.)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#5P#00304F──Well, bein' this the situation\x01",
            "I'll go to show my face to uncle.\x02\x03",
            "#00300FI'll be back durin' the night,\x01",
            "so don't be worried.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_44CE():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_44CE)

    ChrTalk(
        0x102,
        "#6P#00108FB-But...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10101FIsn't it dangerous...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006F──Hey, Randy.\x02\x03",
            "#00000FIn this case, could I\x01",
            "come to say hi too?\x02",
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

    def lambda_45F0():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_45F0)
    Sleep(50)

    def lambda_4600():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4600)
    Sleep(50)

    def lambda_4610():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4610)
    Sleep(50)

    def lambda_4620():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4620)
    Sleep(50)

    def lambda_4630():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4630)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x104,
        "#5P#00305F!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00107FEeeh!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#11P#10111FM-Mr. Lloyd...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00004FWell, after all, greeting as the\x01",
            "Support Section leader a coworker's\x01",
            "relative is good manners, right?\x02\x03",
            "#00000FAnd also, he's in a high class club.\x01",
            "It could be nice as a social study.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#04611F#11PEeh... You're funny, mister.\x02\x03",
            "#04609FWhy not, why not? Since you're\x01",
            "going out of your way, come along!♪\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0xB, 500)
    Sleep(150)

    ChrTalk(
        0x105,
        (
            "#6P#10304FUh uh, then allow\x01",
            "me to come too.\x02\x03",
            "#10302FThe high class club "Neue-Blanc"...\x01",
            "I always wanted to go have fun there.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x105, 500)

    ChrTalk(
        0xB,
        (
            "#04612F#11PThe handsome mister is welcome too!\x02\x03",
            "#04605FOh...\x01",
            "Or could you be, perhaps, a miss?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10309FHu hu, let's go with\x01",
            "mister, for now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00306FAaaargh!!\x01",
            "The heck are you thinkin'!?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0xB, 500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x104,
        (
            "#6P#00307FShirley, you too, don't\x01",
            "continue with the talkings!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x104, 500)
    Sleep(150)

    ChrTalk(
        0xB,
        (
            "#04604F#11PNow, now, I came to pick\x01",
            "you up with the car, you see.\x02\x03",
            "#04602FOh, right, are you coming too, ladies?\x02\x03",
            "#04606FAh, however, that kid and the wolf\x01",
            "can't come, like you can imagine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F──Elie, Noｱl.\x01",
            "Please dine with KeA.\x02\x03",
            "#00008FAnd also, contact the Chief.\x02\x03",
            "#00013FZeit, until the Chief comes back I'm\x01",
            "counting on you to protect the place.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0x9,
        "#01201F#12P#NWoof.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#5P#00101FB-But...!\x02\x03",
            "#00106F......I understand.\x01",
            "Leave watching over the house to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#11P#10101F...Please, be careful!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#01110FHey, hey Lloyd.\x01",
            "Are you going somewhere?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 500)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#12P#00004FYeah, I'm going out for a\x01",
            "bit with Randy and Wazy.\x02\x03",
            "#00000FWe could come back late, don't\x01",
            "nightwalk and go to sleep, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#01109FYes!\x01",
            "Have a safe trip!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        "#5P#00306FShit, why did such a thing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10302FWell, better prepare ourselves for the worst.\x02",
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

    # Function_10_30FA end

    def Function_11_4D44(): pass

    label("Function_11_4D44")

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

    # Function_11_4D44 end

    def Function_12_4D72(): pass

    label("Function_12_4D72")


    def lambda_4D77():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4D77)
    Sleep(300)

    def lambda_4D94():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4D94)
    WaitChrThread(0xFE, 1)

    def lambda_4DA9():
        OP_97(0xFE, 0x5DC, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4DA9)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_12_4D72 end

    def Function_13_4DC3(): pass

    label("Function_13_4DC3")


    def lambda_4DC8():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4DC8)
    Sleep(300)

    def lambda_4DE5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4DE5)
    WaitChrThread(0xFE, 1)

    def lambda_4DFA():
        OP_97(0xFE, 0x3E8, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4DFA)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_13_4DC3 end

    def Function_14_4E14(): pass

    label("Function_14_4E14")

    Sleep(500)

    def lambda_4E1C():
        OP_96(0xFE, 0x2BC, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4E1C)

    def lambda_4E36():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4E36)
    WaitChrThread(0xFE, 1)

    def lambda_4E4B():
        OP_96(0xFE, 0x190, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4E4B)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_14_4E14 end

    def Function_15_4E6C(): pass

    label("Function_15_4E6C")

    Sleep(1500)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x0)

    def lambda_4E7C():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4E7C)

    def lambda_4E96():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4E96)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x9, 0x6)
    SetChrSubChip(0x9, 0x0)
    OP_93(0x9, 0x2D, 0x1F4)
    Return()

    # Function_15_4E6C end

    def Function_16_4EB6(): pass

    label("Function_16_4EB6")


    def lambda_4EBB():
        OP_95(0xFE, 1900, 0, 5200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4EBB)
    WaitChrThread(0xA, 1)
    TurnDirection(0xA, 0xB, 500)
    Return()

    # Function_16_4EB6 end

    def Function_17_4EDC(): pass

    label("Function_17_4EDC")

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
            "Is that so...? Such a thing has...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x102,
        (
            "#00106FYes...I'm sorry.\x02\x03",
            "#00108FYou contacted us again\x01",
            "on purpose, and yet...\x02",
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
            "...No.\x01",
            "I am glad I heard the story.\x02\x03",
            "I will excuse myself now.\x01",
            "I will contact you again. \x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x102,
        "#00100FYes, understood.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0xA,
        "#01102FTio, bye!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x109,
        (
            "#10100FUhmm...\x01",
            "Don't be worried too much, ok?\x02",
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
            "Yes, excuse me.\x07\x00\x02",
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
            "#00106F*sigh*...\x02\x03",
            "#00108FI wonder if Lloyd and the\x01",
            "others will really be fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FConsidering their opponents,\x01",
            "it really worries you...\x02",
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
        "Sergei's Voice",
        "Hey, I'm back.\x02",
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

    def lambda_543F():

        label("loc_543F")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_543F")

    QueueWorkItem2(0xA, 2, lambda_543F)
    Sleep(50)

    def lambda_5454():

        label("loc_5454")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5454")

    QueueWorkItem2(0x109, 2, lambda_5454)
    Sleep(50)

    def lambda_5469():

        label("loc_5469")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5469")

    QueueWorkItem2(0x102, 2, lambda_5469)

    ChrTalk(
        0xA,
        "#01110F#11PAh, it's Chief!\x02",
    )

    CloseMessageWindow()
    OP_68(1960, 1750, 2650, 2500)
    MoveCamera(40, 17, 0, 2500)
    OP_6E(380, 2500)
    SetCameraDistance(24000, 2500)
    Sleep(2000)

    def lambda_54CC():
        OP_95(0xFE, 1000, 0, 1500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_54CC)

    def lambda_54E6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_54E6)
    WaitChrThread(0x8, 1)
    TurnDirection(0x8, 0x102, 500)
    OP_6F(0x79)
    Sound(104, 0, 100, 0)

    ChrTalk(
        0x102,
        "#00102FChief...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10102F#6PG-Good evening.\x02",
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

    def lambda_5590():
        OP_95(0xFE, 12300, 850, 9700, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5590)
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
            "#6P#01000FSorry I'm late.\x01",
            "Has the situation changed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00106FNo, it is as I told you\x01",
            "when I contacted you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10101F...Shouldn't we be on standby\x01",
            "near that establishment?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P#01004FWell, don't be so worried.\x02\x03",
            "#01002FThe "Neue-Blanc" environs are also\x01",
            "surveilled by Section One.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10105FAh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00102FI-I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P#01006FStill, if they just wanted it those guys\x01",
            "could avoid being surveilled, I guess.\x02\x03",
            "#01000F...At any rate, tonight we can\x01",
            "only wait for them to return.\x02",
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

    # Function_17_4EDC end

    def Function_18_5802(): pass

    label("Function_18_5802")


    def lambda_5807():
        OP_95(0xFE, 1000, 850, 10000, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5807)
    WaitChrThread(0x8, 1)

    def lambda_5825():
        OP_95(0xFE, 10000, 850, 10000, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5825)
    WaitChrThread(0x8, 1)
    Return()

    # Function_18_5802 end

    def Function_19_583F(): pass

    label("Function_19_583F")

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
        "#12P#00108F...No way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FReally...\x01",
            "They seem to be a terrifying group.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01003FWell, setting aside the story of\x01",
            "you succeeding the "War God"...\x02\x03",
            "#01000FSeems it was a fruitful meeting, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FYeah...\x02\x03",
            "#00308FWhat those guys have accepted at present\x01",
            "is a 100 million mira contract...\x02\x03",
            "#00301FJudging by the course of events, I'm sure \x01",
            "their contractor is the Imperial government.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FAlso, because they said that they're \x01",
            "going to be busy starting tomorrow...\x02\x03",
            "#10300FThey really seem to be planning to do\x01",
            "something during the Trade Conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01003FHm, in that case the content of that\x01",
            "100 million mira contract could be...\x02\x03",
            "#01001F──Lloyd, what do you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005F...Ah, yes.\x02",
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
            "#1KThe 100 million mira contract content is?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Republican President Assassination\x01",            # 0
            "Blood and Iron Chancellor Ensured Safety\x01",      # 1
            "Cleaning Up the Heiyue\x01",                        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5CF1"),
        (1, "loc_5F64"),
        (2, "loc_6181"),
        (SWITCH_DEFAULT, "loc_63A7"),
    )


    label("loc_5CF1")


    ChrTalk(
        0x101,
        (
            "#12P#00008FThe assassination of President Rocksmith\x01",
            "of the Calvard Republic...\x02\x03",
            "#00006F...No, that's not it.\x02\x03",
            "For argument's sake, if that was the case,\x01",
            "100 million mira would be too little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01004FEheh, exactly.\x02\x03",
            "#01002FIf we think considering this point, it should be\x01",
            "the Blood and Iron Chancellor ensured safety.\x02",
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
        "#12P#00011FAh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00101FI-Indeed.\x02\x03",
            "It is said that Chancellor \x01",
            "Osborne has got many \x01",
            "oppositors in the Empire...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F...That's likely, then.\x02",
    )

    CloseMessageWindow()
    Jump("loc_63A7")

    label("loc_5F64")

    OP_2C(0xA3, 0x1)

    ChrTalk(
        0x101,
        (
            "#12P#00003F...This is just my intuition, but...\x02\x03",
            "#00001FIt is said that the Blood and Iron Chancellor\x01",
            "has got many oppositors in the Empire.\x02\x03",
            "I think it's possible that they're\x01",
            "going to protect the Chancellor from\x01",
            "such people while in Crossbell.\x02",
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

    def lambda_60D2():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_60D2)
    Sleep(50)

    def lambda_60E2():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_60E2)
    Sleep(50)

    def lambda_60F2():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_60F2)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x102,
        "#12P#00105FAh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F...I see...\x01",
            "That's likely, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01004FEheh...\x01",
            "That's a good observation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63A7")

    label("loc_6181")


    ChrTalk(
        0x101,
        (
            "#12P#00008FCleaning up the "Heiyue"...\x02\x03",
            "#00006FNo, it could really be bad timing\x01",
            "during the Trade Conference, hm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01004FEheh, exactly.\x02\x03",
            "#01002FIf we think considering this point, it should be\x01",
            "the Blood and Iron Chancellor ensured safety.\x02",
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
        "#12P#00011FAh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00101FI-Indeed.\x02\x03",
            "It is said that Chancellor \x01",
            "Osborne has got many \x01",
            "oppositors in the Empire...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F...That's likely, then.\x02",
    )

    CloseMessageWindow()
    Jump("loc_63A7")

    label("loc_63A7")


    ChrTalk(
        0x105,
        (
            "#12P#10303FHm, but conversely, isn't 100 million\x01",
            "mira a little too much for that?\x02\x03",
            "#10301FAnd also, the Chancellor is probably\x01",
            "going to take along his own guards.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FRight...\x02\x03",
            "#10101FBoth the Empire and Republic\x01",
            "seem they're going to send\x01",
            "many guards as escorts.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6736")
    OP_2C(0xA3, 0x2)

    ChrTalk(
        0x101,
        (
            "#5P#00003F...Naturally they're going to be different\x01",
            "from those official guards.\x02\x03",
            "#00008FStill, as far as their actions go, it is a fact\x01",
            "that they're trying, in many aspects, to grasp\x01",
            "Crossbell's topography.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FEyewitness reports at Armorica\x01",
            "Village, Mainz and Bellguard\x01",
            "Gate could indicate that.\x02\x03",
            "#10304FAlthough it seems the most plausible reasons\x01",
            "are buying food supplies and Septium...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00003FYeah, I think that their real purpose for\x01",
            "visiting different regions was something else.\x02\x03",
            "#00001FThat was to see if we and the Bracers too\x01",
            "could deal right away if something happened.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6877")

    label("loc_6736")


    ChrTalk(
        0x101,
        (
            "#5P#00003F...Naturally they'll be different\x01",
            "from those official guards.\x02\x03",
            "#00008FStill, as far as their actions go, it is a fact\x01",
            "that they're trying, in many aspects, to\x01",
            "grasp Crossbell's topography.\x02\x03",
            "#00001FThat was to see if we and the Bracers too\x01",
            "could deal right away if something happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10300FHm...\x02",
    )

    CloseMessageWindow()

    label("loc_6877")


    ChrTalk(
        0x102,
        (
            "#12P#00106FTrue...\x01",
            "I had that impression.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00308F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01000F──Well, at present we can\x01",
            "only guess this much.\x02\x03",
            "#01003FTomorrow, VIPs from every country are going to\x01",
            "arrive and there's the Orchis Tower inauguration.\x02\x03",
            "#01002FOh, by the way, I'll have you go\x01",
            "there at the site too, you know?\x02",
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

    def lambda_6A36():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6A36)
    Sleep(50)

    def lambda_6A46():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6A46)
    Sleep(50)

    def lambda_6A56():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6A56)
    Sleep(50)

    def lambda_6A66():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6A66)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)

    ChrTalk(
        0x101,
        "#12P#00005FHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00105FWith "the site" do you mean...the inauguration?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01004FIt appear that your attention has been\x01",
            "captivated by the "Red Constellation".\x02\x03",
            "#01000F──Counterespionage and anti-terrorism\x01",
            "is not your job by nature.\x02\x03",
            "It's time you get a change of mood and try\x01",
            "to look down on the situation a little more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000F...Indeed...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FHa ha...\x01",
            "That remark tingles in my ear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FUhmm, does it mean that we're going\x01",
            "to join security at the inauguration?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01003FWell, nominally it's going to be like that, but more\x01",
            "importantly, you're going to devote yourselves to\x01",
            "survey the situation at the inauguration ceremony.\x02\x03",
            "#01002FThe atmosphere at the Trade Conference beginning...\x01",
            "The VIPs aura and stuff like that.\x02\x03",
            "You should be able to have a \x01",
            "different look on things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000F...Understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHu hu, then I guess we're going to see\x01",
            "everything from some special seats.\x02",
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

    # Function_19_583F end

    def Function_20_6E66(): pass

    label("Function_20_6E66")

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
            "#01001F──I see. Terrorists aiming\x01",
            "at both the VIPs.\x02",
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
            "#00606F#5PDamn, the possibility was there,\x01",
            "but to think it was really concrete...\x02\x03",
            "#00610FWhat the heck are the Empire\x01",
            "and the Republic thinking...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1P#01003FWell, of course if they've got some targets,\x01",
            "might as well know what they're.\x02\x03",
            "#01000FWe'd better to inform the\x01",
            "mayor and the CGF too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00603F#5PYes, leave that to me.\x02\x03",
            "#00601F...At any rate.\x01",
            "When I heard you boarded that \x01",
            ""Arseille", I couldn't believe it.\x02\x03",
            "Furthermore, to think you could hear such\x01",
            "things from two state guest class persons...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7243():
        TurnDirection(0x101, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7243)
    Sleep(100)

    def lambda_7253():
        TurnDirection(0x109, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7253)
    Sleep(100)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x101,
        (
            "#6P#00012FHa ha, Section One was\x01",
            "checking on them too, I bet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00302FWell, since it was something sudden for us,\x01",
            "I'd wish you didn't scold us over it too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00607F#5PHmph, it may have been sudden, but in such\x01",
            "a situation you should've accepted the invite\x01",
            "or not after advising with your superiors...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1P#01004FEh eh, why don't you\x01",
            "let them deal with it?\x02\x03",
            "#01002FWho summoned them seemed quite\x01",
            "unusual too, so they were right for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#00606F#5PGh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00309FMan, still the princess and prince\x01",
            "were both truly an odd bunch.\x02\x03",
            "#00300FEspecially Prince Olivert, I'd never\x01",
            "thought he had such a lover.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_74E9():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_74E9)
    Sleep(100)

    def lambda_74F9():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_74F9)
    Sleep(100)

    def lambda_7509():
        TurnDirection(0x105, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7509)
    Sleep(100)

    def lambda_7519():
        TurnDirection(0x109, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7519)
    Sleep(100)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x102,
        (
            "#5P#00106FRandy, that's rude.\x02\x03",
            "#00100FHe was...cheerful?\x01",
            "And a very witty person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00004FHowever, I think he's a man who\x01",
            "thinks through many things well.\x02\x03",
            "#00000FEven the Major escorting\x01",
            "him looked quite capable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10102FAlso, Princess Klaudia and\x01",
            "Captain Julia were amazing...!\x02\x03",
            "#10112FThe princess was sociable but also had grace\x01",
            "and Captain Julia had commanding eyes and...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#11PHu hu, it seems you even managed\x01",
            "to get a sign for your sister too, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10111FH-How do you...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00606F#5P...Honestly.\x02\x03",
            "#00600FWhatever── Even just knowing the existence\x01",
            "of terrorists can be considered a good result.\x02\x03",
            "It could be better to adjust \x01",
            "tomorrow's guard shift a little...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7804():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7804)
    Sleep(100)

    def lambda_7814():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7814)
    Sleep(100)

    def lambda_7824():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7824)
    Sleep(100)

    def lambda_7834():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7834)
    Sleep(100)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x101,
        (
            "#6P#00001FSo the critical moment is really going to\x01",
            "be tomorrow...at the "Trade Conference"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1P#01003FYeah. The VIPs are scheduled to return\x01",
            "home the day after tomorrow's afternoon...\x02\x03",
            "#01001FIf something has to happen,\x01",
            "it's very likely to be tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FThe conference is going to\x01",
            "start at noon, am I right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00600F#5PYeah, from 13:00. The "Trade\x01",
            "Conference" is going to open\x01",
            "at Orchis Tower 35F.\x02\x03",
            "There's going to be one break after\x01",
            "that and then it's scheduled to \x01",
            "continue at least until evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00305FSo it means that things will be\x01",
            "alright if we protect that bunch\x01",
            "of VIPs through the conference?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00604F#5PWell, inside Orchis Tower there's going to be\x01",
            "a complete security system deployed.\x02\x03",
            "There's also the building security personnel, so\x01",
            "during the conference it should be rather secure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1P#01003FArios is also scheduled to participate\x01",
            "as an addition to the venue guards.\x02\x03",
            "#01002FSince at the Trade Conference location\x01",
            "there're going to be observers from the\x01",
            "Guild too, it's going to be really safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10108FIn that case, the most dangerous moments\x01",
            "could be before and after the conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#12PJust when coming out from the tower a\x01",
            "sniper could make its move from afar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FFrankly, that's the most\x01",
            "scary pattern there is...\x02",
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
        "KeA's Voice",
        "#11P#13AHey, hey Lloyd.\x02",
    )

    CloseMessageWindow()
    OP_68(64000, 1000, 6300, 2000)
    MoveCamera(62, 15, 0, 2000)
    OP_6E(400, 2000)
    SetCameraDistance(24000, 2000)
    OP_5A()
    SetChrPos(0xA, 61500, 0, 3800, 90)

    def lambda_7E39():
        TurnDirection(0x109, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7E39)
    Sleep(50)

    def lambda_7E49():
        TurnDirection(0x102, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7E49)
    Sleep(50)

    def lambda_7E59():
        TurnDirection(0x104, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7E59)
    Sleep(50)

    def lambda_7E69():
        TurnDirection(0x105, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7E69)
    Sleep(50)

    def lambda_7E79():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7E79)
    Sleep(50)

    def lambda_7E89():
        TurnDirection(0x10A, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_7E89)
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

    def lambda_7EDC():
        OP_96(0xFE, 0xEE48, 0x0, 0xCE4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_7EDC)

    def lambda_7EF6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_7EF6)
    WaitChrThread(0xA, 1)

    def lambda_7F0B():
        OP_95(0xFE, 61500, 0, 3800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_7F0B)
    WaitChrThread(0xA, 1)
    TurnDirection(0xA, 0x10A, 500)
    OP_6F(0x79)
    OP_63(0xA, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xA,
        "#12P#01105F#3610V#30WAh, it's the sullen old man!\x02",
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
            "#5P#00603F...Looks like she has no home\x01",
            "discipline as always, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00011FS-Sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00112F#5PKeA, this man is\x01",
            "Mr. Dudley...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12P#01109FYep, Dudley!\x02\x03",
            "#01110FLong time no see.\x01",
            "Have you been well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#5P#00604FHmph, as a Section One detective,\x01",
            "my condition is always in top form.\x02\x03",
            "#00607F──That's not it! Stop addressing\x01",
            "me so casually!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12P#01106FEeh, I can't?\x02\x03",
            "#01111FThen, "uncle" Dudley?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x10A,
        "#5P#00610FWho's an "uncle", who!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10112FN-Now, now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00309FHa ha, from the point of view of a child, you're\x01",
            "plenty of an "uncle", or a middle age man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#11PSo, KeA?\x01",
            "What do you need?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#12P#01106FOh, right.\x02\x03",
            "#01100FEhm, there's a call\x01",
            "for you guys.\x02",
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
        "#00005F#5PA call?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F#5PMy, it appears that the\x01",
            "receiver bell didn't ring...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12P#01109FAh, it's not the normal one, but\x01",
            "the one with a face appearing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#5PThe terminal then...?\x01",
            "KeA, you learned well how to use it, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F#5PBut, is it peTiote then?\x01",
            "It seems she called in the evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12P#01104FNope, it's a person with freckles.\x02\x03",
            "#01100FAlthough somehow his\x01",
            "face is red and pale...\x02",
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
    SetChrName("Jona's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4S──You're late!\x02\x03",
            "#3SJeez, how long are you\x01",
            "gonna make me wait!!\x07\x00\x02",
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
            "#00012FHa ha, sorry.\x02\x03",
            "#00002FAt any rate, it's been a long\x01",
            "time, are you doing fi──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x2, 0x8, 0x180, 0x0, 0x200, 0x80)
    OP_0D()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("Jona's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Oh, jeez, spare\x01",
            "the greetings!\x02\x03",
            "I've got an urgent favor\x01",
            "I want you to do to me!\x02\x03",
            "Can't you go to have a\x01",
            "look in my base now!?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x101,
        "#00011FWhat...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00105F"Base"...\x01",
            "The place you were staying at?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x2, 0x8, 0x100, 0x0, 0x180, 0x80)
    OP_0D()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("Jona's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Yeah, the place that has the 8th control\x01",
            "terminal in Geofront B-Division, you know!\x02\x03",
            "It seems there's someone who used\x01",
            "that terminal as he pleased from\x01",
            "yesterday, today too!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x101,
        "#00001FUsed as he pleased...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x109,
        (
            "#10105FHow on earth did\x01",
            "you figure it out?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        (
            "#00301FBy the way, oh great Jona.\x01",
            "Isn't he doin' exactly\x01",
            "what you're doin'?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x2, 0x8, 0x180, 0x0, 0x200, 0x80)
    OP_0D()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("Jona's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "T-That aside!\x02\x03",
            "I applied a strong protection on\x01",
            "that terminal since I'm away!\x02\x03",
            "So, in case that gets breached,\x01",
            "it sends an alert when I'm doing live\x01",
            "remote connection orbal net tests...\x02\x03",
            "And today that alert came in!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x101,
        "#00013FWell...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x105,
        (
            "#10303F...There's someone who hacked the\x01",
            "terminal you put the protection on.\x02\x03",
            "#10301FIs that the case?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x2, 0x8, 0x0, 0x80, 0x80, 0x100)
    OP_0D()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("Jona's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Yeah, that's it!\x01",
            "It's quite a skilled hacker!\x02\x03",
            "Anyway, I want you to catch him\x01",
            "so he doesn't touch it anymore!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x104,
        (
            "#00306FMan, he plays the innocent\x01",
            "part and says what he wants.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00108FHowever, a "skilled hacker"...\x01",
            "It worries me a little.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00003FYeah. Renne should've gone back by now\x01",
            "and I can't think it's Chief Roberts.\x02\x03",
            "#00001FFor starters, we'll go to take a look,\x01",
            "so contact us later.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x2, 0x8, 0x100, 0x0, 0x180, 0x80)
    OP_0D()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("Jona's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Yeah, I'm counting on you!\x07\x00\x02",
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
        "#01000F#5POh, are you going?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#00003FYes, just in case.\x02\x03",
            "#00000FIf you want, I could even\x01",
            "go alone to have a look.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00301FHey now, don't be crazy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FRight...\x01",
            "It's not said that there's\x01",
            "only a hacker there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10101FI'll accompany you!\x02",
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
            "#3452V#30W──Wait.\x02\x03",
            "#4106VI'll come with you too.\x02",
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

    def lambda_90D4():
        TurnDirection(0x101, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_90D4)
    Sleep(50)

    def lambda_90E4():
        TurnDirection(0x104, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_90E4)
    Sleep(50)

    def lambda_90F4():
        TurnDirection(0x109, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_90F4)
    Sleep(50)

    def lambda_9104():
        TurnDirection(0x105, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_9104)
    Sleep(50)

    def lambda_9114():
        TurnDirection(0x102, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_9114)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)

    ChrTalk(
        0x101,
        "#11P#00005FHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10302FEeh, to what do we owe this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00603F#5PHmph, I just want to understand an\x01",
            "irregular element before the Trade\x01",
            "Conference, even if  just a little.\x02\x03",
            "#00601FTime is precious, let's go at once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00011FU-Understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FHu hu, then let's go for a\x01",
            "light after meal exercise.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x10E, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x102,
        (
            "#12P#00100FChief, KeA, we're\x01",
            "going now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#01002F#5PYeah, be careful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#6P#01109FHave a safe trip!\x02",
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
            "Detective Dudley has joined the party.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You can add him to the attack members\x01",
            "from [TACTICS] under the camp menu.\x07\x00\x02",
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

    # Function_20_6E66 end

    def Function_21_94BF(): pass

    label("Function_21_94BF")

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

    # Function_21_94BF end

    def Function_22_952F(): pass

    label("Function_22_952F")

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
            "#01109FEhehe, it's Tio!\x02\x03",
            "#01110FHey, hey Zeit!\x01",
            "Tio's back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01200F#5PWoof.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00202FI'm home,\x01",
            "KeA, Zeit.\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)

    def lambda_974D():
        OP_96(0xFE, 0x2BC, 0x0, 0x1194, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_974D)
    WaitChrThread(0xA, 1)
    TurnDirection(0x103, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#6P#00204FChief Sergei, I\x01",
            "just came back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01004FYeah, it's nice having you back.\x02\x03",
            "#01002FEh, it seems you saved your colleagues \x01",
            "who suddenly were in a pinch, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00004FYes, she really helped us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00106FIf Tio hadn't arrived\x01",
            "there, I don't know\x01",
            "what would've happened...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10112FYes, yes, it gives me the shivers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00604F...I will thank you\x01",
            "for this time only.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        "#5P#00205FWell, I didn't do anything major.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00309FHa ha, don't get shy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FWell, I think you came back\x01",
            "just at the right time.\x02\x03",
            "#10300FAfter we got involved with such a\x01",
            "hacker we didn't know what to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00006FRight...\x02",
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
            "#6P#00003F──Chief, Mr. Dudley.\x02\x03",
            "#00001FAbout tomorrow's Trade Conference...\x01",
            "Could you please have us take part\x01",
            "in the Orchis Tower security too?\x02",
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

    def lambda_9B7B():
        TurnDirection(0xC, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_9B7B)
    Sleep(50)

    def lambda_9B8B():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_9B8B)
    Sleep(50)

    def lambda_9B9B():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_9B9B)
    Sleep(50)

    def lambda_9BAB():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_9BAB)
    Sleep(50)

    def lambda_9BBB():
        TurnDirection(0x8, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_9BBB)
    Sleep(50)
    WaitChrThread(0xC, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x8, 0)

    ChrTalk(
        0x102,
        "#6P#00105FLloyd, that's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00305FHey now.\x01",
            "What suddenly got into you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P#01000FHm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00600F#11P...Didn't I tell you that the venue\x01",
            "security system is perfect?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FStill, today's hacker managed\x01",
            "to get what seemed to be the\x01",
            "tower blueprints in some way.\x02\x03",
            "#00008FThese are not "Yin"'s words, but there's\x01",
            "the possibility that something's going on──\x02\x03",
            "#00001FNo, rather I think it's very likely he\x01",
            "gave those information to "someone".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10101FTo someone...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10301FHm, to whom I wonder?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 3)

    label("loc_9E05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F72")
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
            "#1KTo whom did the mysterious\x01",
            "hacker give the information?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            ""Heiyue"\x01",                 # 0
            ""Red Constellation"\x01",      # 1
            "A Different Party\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9ED0"),
        (1, "loc_9ED0"),
        (2, "loc_9F51"),
        (SWITCH_DEFAULT, "loc_9F6D"),
    )


    label("loc_9ED0")


    ChrTalk(
        0x101,
        (
            "#11P#00006F(No... there should be a party\x01",
            "who wants those more.)\x02\x03",
            "#00001F(And that is...)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9F4C")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9F4C")

    Jump("loc_9F6D")

    label("loc_9F51")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9F65")
    OP_2C(0xA3, 0x1)

    label("loc_9F65")

    SetScenarioFlags(0x0, 3)
    Jump("loc_9F6D")

    label("loc_9F6D")

    Jump("loc_9E05")

    label("loc_9F72")


    ChrTalk(
        0x101,
        (
            "#11P#00003FThe "Red Constellation", or the "Heiyue", or even\x01",
            "the Imperial government or the Republican one...\x02\x03",
            "They all seem plausible choices, but\x01",
            "there should be a way more likely group.\x02\x03",
            "#00013FThe Imperial and Republican terrorists.\x02",
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
            "#6P#00101FWe heard about them from Princess\x01",
            "Klaudia and Prince Olivert...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00301FTwo groups of terrorists aiming\x01",
            "at each other's top figures?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10108FIt's true that if they have the building\x01",
            "structure map they can aim from blind spots...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#6P#00006FOf course there's also the possibility\x01",
            "of camouflaged information...\x02\x03",
            "#00001FI think we can say that the possibility\x01",
            "that tomorrow something is going to\x01",
            "happen at Orchis Tower has increased.\x02\x03",
            "It would be fine even with guarding the tower\x01",
            "environs...could you make us participate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01004FEh eh, I see.\x02\x03",
            "#01002FWhat about it, Dudley?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00606F#11P*sigh*...\x01",
            "Well, alright.\x02",
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
            "#00611F#11P──Come exactly tomorrow at\x01",
            "noon at Orchis Tower 1F.\x02\x03",
            "I'm going to make you enter the Trade Conference\x01",
            "venue as reserve guards personnel.\x02",
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

    def lambda_A4F8():
        TurnDirection(0x101, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A4F8)
    Sleep(50)

    def lambda_A508():
        TurnDirection(0x104, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_A508)
    Sleep(50)

    def lambda_A518():
        TurnDirection(0x103, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_A518)
    Sleep(50)

    def lambda_A528():
        TurnDirection(0x102, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_A528)
    Sleep(50)

    def lambda_A538():
        TurnDirection(0x109, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A538)
    Sleep(50)

    def lambda_A548():
        TurnDirection(0x105, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_A548)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        "#6P#00005FWhat...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00305FWhoa, the venue?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FEeh...\x01",
            "Aren't you very generous?\x02",
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
            "#00603F#11PDon't misunderstand.\x01",
            "You're just reserve personnel.\x02\x03",
            "You were useful in the mayor attempted\x01",
            "assassination, although by coincidence,\x01",
            "and you also have someone knowledgeable\x01",
            "about the orbal net.\x02\x03",
            "#00601FBear it well in mind that you're only insurance\x01",
            "in the remote possibility that something happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FU-Understood!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10102FI humbly accept!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00204FAnyway, I think this is a way\x01",
            "to hide his embarrassment...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00309FHa ha, I wonder when he'll\x01",
            "start to fawn upon us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#01111F#5PTo fawn...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x102, 500)
    Sleep(150)

    ChrTalk(
        0xA,
        (
            "#01110F#5PHey, hey Elie.\x01",
            "What does "to fawn" mean?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00109FW-Well.\x01",
            "It's like the attitude everyone has\x01",
            "when talking with you, KeA...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10309FHu hu, at this rate it could\x01",
            "be not so far in the future.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xC,
        "#00610F#11PB-Bastards...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01004FEh eh, it appears that tomorrow \x01",
            "we're going to be busy like crazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01203FWoof.\x02",
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

    # Function_22_952F end

    def Function_23_AA15(): pass

    label("Function_23_AA15")

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
            "#00008F#11P...The Chief sure is late.\x02\x03",
            "#00006FIt's no wonder since such a\x01",
            "thing happened, but still...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10108FYes...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#5P#00106F...At this hour he's probably\x01",
            "discussing hereafter counter-\x01",
            "measures at Orchis Tower.\x02\x03",
            "#00108FIt's also a complex problem at a political level...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#11PWald too...\x02\x03",
            "#10301FHe did such a crazy thing\x01",
            "at a difficult time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6P#01106F...Hey, hey everyone.\x02\x03",
            "#01112FSince Chief is not coming back,\x01",
            "should we cancel the hot pot?\x02",
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
            "#00304F#11P...No, he said to go ahead\x01",
            "and begin if he was late.\x02\x03",
            "#00300FKeddo, you went out of your way to prepare it,\x01",
            "so we'll go on eatin' it even if it's just us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#6P#01108FB-But...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x0)
    Sleep(100)
    SetChrSubChip(0x101, 0x1)
    Sleep(200)

    ChrTalk(
        0x103,
        "#6P#00208FMr. Randy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PSetting aside the hot pot...\x01",
            "Randy, aren't you pushing yourself?\x02\x03",
            "#00008FYou should count on us\x01",
            "right on times like this──\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x2)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00302F#11PHa ha, of course I'm countin' on you.\x02\x03",
            "#00303FI said it before too...\x01",
            "I severed my ties with uncle and the others.\x02\x03",
            "Now of all times there's no need to broad over\x01",
            "that much on what my old haunt has just done.\x02\x03",
            "#00304FMore importantly, eatin' our meals\x01",
            "and restin' while we can rest...\x02\x03",
            "#00300F──Preparin' for tomorrow comes first, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#5PWell...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10112FY-You're right!\x02\x03",
            "#10100FAfter all, they say that you can't\x01",
            "fight on an empty stomach!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00109F*giggle*, Randy's toughness\x01",
            "always helps us out...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00202F...Right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#11PWell, today we came across one hell\x01",
            "of a bunch of people at the lake too.\x02\x03",
            "#10302FFinishing to eat ahead of time and resting maybe\x01",
            "is the best course of action in lieu of tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004F#5PRight...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00002F#11P──Alright.\x01",
            "Then, let's start with the hot pot.\x02\x03",
            "#00004FSince KeA made the preparations for us,\x01",
            "there's plenty of meat, fish and vegetables.\x02\x03",
            "#00000FLet's eat a lot, rest before than\x01",
            "usual and get ready for tomorrow!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309F#11PYeah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10109FBon appetit!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00102FKeA, leave the rest to us\x01",
            "and fill your belly a lot, ok?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x1)
    Sleep(100)

    ChrTalk(
        0xA,
        "#6P#01109F...Yep!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00202FZeit, I will cool down some\x01",
            "meat and fish for you later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01200F#11PGrrrowl...woof.\x02",
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

    # Function_23_AA15 end

    def Function_24_BB31(): pass

    label("Function_24_BB31")

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
            "#5PW-What in the world is\x01",
            "happening outside....?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5P...My husband...\x01",
            "I wonder if he's alright...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x0, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "#12P#01003FAah, everyone, please calm down.\x02\x03",
            "#01002FAccording to a communication I have just\x01",
            "received, it appears that the mysterious\x01",
            "armed group has started to withdraw.\x02\x03",
            "Until safety is confirmed, please\x01",
            "return back to your houses.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BEE4():
        TurnDirection(0xE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_BEE4)
    Sleep(30)

    def lambda_BEF4():
        TurnDirection(0x10, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_BEF4)
    Sleep(30)

    def lambda_BF04():
        TurnDirection(0x11, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_BF04)
    Sleep(30)
    WaitChrThread(0xE, 0)
    WaitChrThread(0x10, 0)
    WaitChrThread(0x11, 0)

    ChrTalk(
        0xE,
        "#5PI-Is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5POoh, o Aidios...!\x01",
            "Thank you for your protection...!\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(20000, 1000)

    def lambda_BF7B():
        OP_9A(0xFE, 0x8, 0x4B0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_BF7B)
    WaitChrThread(0xA, 1)

    ChrTalk(
        0xA,
        (
            "#5P#01112F#30WChief...\x01",
            "Is it alright now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#01006FYeah, for the time being.\x02\x03",
            "#01001FLloyd and the others...\x01",
            "I hope they're safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#01104F#30W──Yes, they're.\x02\x03",
            "#01121FIf it's them, they'll be fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#01005FHm, yeah...you're right.\x02\x03",
            "#01002FNo matter what one could say,\x01",
            "they've grown up too.\x02\x03",
            "#01004FMaybe more than the\x01",
            "former Sergei Unit──\x02",
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
            "#11P#01003FYes, this is the Support Section──\x02\x03",
            "#01005F...Ooh, Dudley, eh?\x01",
            "How is it going over there?\x02\x03",
            "#01001F...What?\x01",
            "A jaegers' airship you say...?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xA)
    Sleep(500)

    def lambda_C246():
        OP_96(0xFE, 0xFFFFFCE0, 0x0, 0xCE4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_C246)
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0x0, 0x1F4)
    SetChrChipByIndex(0xA, 0x27)
    SetChrSubChip(0xA, 0x0)

    def lambda_C273():
        OP_96(0xFE, 0x190, 0x0, 0x1A90, 0xDAC, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_C273)
    WaitChrThread(0xA, 1)
    OP_68(1000, 2000, 3000, 3000)

    def lambda_C2A2():
        OP_96(0xFE, 0x514, 0x352, 0x2BC0, 0xDAC, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_C2A2)
    WaitChrThread(0xA, 1)

    def lambda_C2C0():
        OP_96(0xFE, 0x514, 0xFA0, 0x3B60, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_C2C0)
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

    def lambda_C34F():
        OP_96(0xFE, 0xFFFFFED4, 0x0, 0x11A6C, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_C34F)
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
            "#01119F#40W#11P............\x02\x03",
            "#01118F#40W...As I thought...\x02\x03",
            "#01120F#40WAs I thought, no matter how...\x01",
            "...It seems that this is for the best...\x02",
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
        "#01123F#40W#11P............\x02",
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
            "#01112F#30W#11P#15A...Hello...?\x02\x03",
            "#01108F#40W#25A...Yes...\x01",
            "......Yes......\x02",
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
        "#01121F#3621V#40W#11P#20A──It's ok.\x02",
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
            "#3622V#30W#40AI have...\x01",
            "Made up my mind properly.\x02",
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

    # Function_24_BB31 end

    def Function_25_C686(): pass

    label("Function_25_C686")

    TalkBegin(0xFF)
    OP_E5(0xA)
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_E5(0x5)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C6A2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CDF6")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "OP_E5(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_C6DB"),
        (1, "loc_C897"),
        (2, "loc_CDDA"),
        (3, "loc_CDE2"),
        (SWITCH_DEFAULT, "loc_CDF1"),
    )


    label("loc_C6DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_C6EE")
    OP_2B(0x94, 0xFFFF)
    Jump("loc_C892")

    label("loc_C6EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_C709")
    OP_2B(0x8E, 0x8F, 0x90, 0x91, 0x92, 0xFFFF)
    Jump("loc_C892")

    label("loc_C709")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_C76C")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Announcement")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Currently there are no support requests.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_C892")

    label("loc_C76C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_C787")
    OP_2B(0x8B, 0x8C, 0x88, 0x80, 0x83, 0xFFFF)
    Jump("loc_C892")

    label("loc_C787")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C7C2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_C7B0")
    OP_2B(0x85, 0x86, 0x87, 0x88, 0x80, 0x83, 0xFFFF)
    Jump("loc_C7BD")

    label("loc_C7B0")

    OP_2B(0x85, 0x86, 0x88, 0x80, 0x83, 0xFFFF)

    label("loc_C7BD")

    Jump("loc_C892")

    label("loc_C7C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_C7DB")
    OP_2B(0x80, 0x81, 0x82, 0x83, 0xFFFF)
    Jump("loc_C892")

    label("loc_C7DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_C7E9")
    Jump("loc_C892")

    label("loc_C7E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_C806")
    OP_2B(0x79, 0x7A, 0x7B, 0x77, 0x71, 0x72, 0xFFFF)
    Jump("loc_C892")

    label("loc_C806")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_END)), "loc_C823")
    OP_2B(0x74, 0x75, 0x76, 0x77, 0x71, 0x72, 0xFFFF)
    Jump("loc_C892")

    label("loc_C823")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C83C")
    OP_2B(0x6F, 0x70, 0x71, 0x72, 0xFFFF)
    Jump("loc_C892")

    label("loc_C83C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_C870")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_END)), "loc_C860")
    OP_2B(0x6A, 0x6B, 0x6C, 0x6D, 0x67, 0xFFFF)
    Jump("loc_C86B")

    label("loc_C860")

    OP_2B(0x6A, 0x6B, 0x6C, 0x67, 0xFFFF)

    label("loc_C86B")

    Jump("loc_C892")

    label("loc_C870")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 7)), scpexpr(EXPR_END)), "loc_C887")
    OP_2B(0x65, 0x66, 0x67, 0xFFFF)
    Jump("loc_C892")

    label("loc_C887")

    OP_2B(0x65, 0x66, 0x67, 0x68, 0xFFFF)

    label("loc_C892")

    Jump("loc_CDF1")

    label("loc_C897")

    SetMapFlags(0x40000000)
    OP_E5(0x7)
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C98C")
    SetChrName("Announcement")

    AnonymousTalk(
        0xFF,
        "This is Crossbell Police.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E5(0x4)"), scpexpr(EXPR_END)), "loc_C964")

    AnonymousTalk(
        0xFF,
        "I will receive your report.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E5(0xC)
    SetChrName("Announcement")

    AnonymousTalk(
        0xFF,
        (
            "Report processing, complete.\x01",
            "Thank you for your hard work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C987")

    label("loc_C964")


    AnonymousTalk(
        0xFF,
        "There no reportable requests.\x02",
    )

    CloseMessageWindow()

    label("loc_C987")

    Jump("loc_CDCC")

    label("loc_C98C")

    SetChrName("Receptionist Fran")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C9E3")
    Sound(3062, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        "Yes, this is Crossbell Poliiice!\x02",
    )

    CloseMessageWindow()
    Jump("loc_CA18")

    label("loc_C9E3")

    Sound(3061, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        "Everyone, thank you for your hard wooork.\x02",
    )

    CloseMessageWindow()

    label("loc_CA18")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E5(0x4)"), scpexpr(EXPR_END)), "loc_CCB6")
    Sound(3067, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        "Then, I'll receive your report, okaaay?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E5(0xC)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CC29")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_END)),
        (14, "loc_CA99"),
        (13, "loc_CAE7"),
        (12, "loc_CB32"),
        (SWITCH_DEFAULT, "loc_CB76"),
    )


    label("loc_CA99")

    Sound(3075, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        (
            "Rank 1st...\x01",
            "That's too amazing, Mr. Lloyd!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CB76")

    label("loc_CAE7")

    Sound(3074, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        (
            "Rank 2nd──\x01",
            "That's amazing, Mr. Lloyd!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CB76")

    label("loc_CB32")

    Sound(3073, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        (
            "Rank 3rd──\x01",
            "You did, Mr. Lloyd!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CB76")

    label("loc_CB76")

    Sound(3076, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        (
            "I will immediately send you\x01",
            "the special article you gaaained!\x02",
        )
    )

    CloseMessageWindow()
    Sound(3077, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            "Thank you for your hard wooork!\x01",
            "I hope to be working with you agaaain.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CCAE")

    label("loc_CC29")

    Sound(3078, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        "The report is oveeer.\x02",
    )

    CloseMessageWindow()
    Sound(3079, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            "Then, please contact me again the\x01",
            "next time you complete a requeeest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CCAE")

    SetScenarioFlags(0x0, 6)
    Jump("loc_CDCC")

    label("loc_CCB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_CD43")
    Sound(3063, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        (
            "Oh...\x01",
            "Haven't you just made a report?\x02",
        )
    )

    CloseMessageWindow()
    Sound(3064, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        "Please do it again when you complete a request.\x02",
    )

    CloseMessageWindow()
    Jump("loc_CDCC")

    label("loc_CD43")

    Sound(3065, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        (
            "Oh...it seems you don't have\x01",
            "any request you can repooort.\x02",
        )
    )

    CloseMessageWindow()
    Sound(3066, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        "Please, let's work together agaaain.\x02",
    )

    CloseMessageWindow()

    label("loc_CDCC")

    OP_57(0x0)
    OP_E5(0x8)
    ClearMapFlags(0x40000000)
    Jump("loc_CDF1")

    label("loc_CDDA")

    Call(0, 26)
    Jump("loc_CDF1")

    label("loc_CDE2")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CDF1")

    label("loc_CDF1")

    Jump("loc_C6A2")

    label("loc_CDF6")

    OP_E5(0x6)
    OP_C9(0x1, 0x4)
    OP_C9(0x1, 0x100)
    FadeToBright(300, 0)
    OP_0D()
    OP_E5(0xB)
    TalkEnd(0xFF)
    Return()

    # Function_25_C686 end

    def Function_26_CE14(): pass

    label("Function_26_CE14")

    OP_E5(0x6)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 3)), scpexpr(EXPR_END)), "loc_CE36")
    SetScenarioFlags(0x2A, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CE36")
    ClearScenarioFlags(0x2A, 0)

    label("loc_CE36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 4)), scpexpr(EXPR_END)), "loc_CE53")
    SetScenarioFlags(0x2A, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CE53")
    ClearScenarioFlags(0x2A, 1)

    label("loc_CE53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 5)), scpexpr(EXPR_END)), "loc_CE70")
    SetScenarioFlags(0x2A, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CE70")
    ClearScenarioFlags(0x2A, 2)

    label("loc_CE70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 6)), scpexpr(EXPR_END)), "loc_CE8D")
    SetScenarioFlags(0x2A, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CE8D")
    ClearScenarioFlags(0x2A, 3)

    label("loc_CE8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 7)), scpexpr(EXPR_END)), "loc_CEAA")
    SetScenarioFlags(0x2A, 4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CEAA")
    ClearScenarioFlags(0x2A, 4)

    label("loc_CEAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 0)), scpexpr(EXPR_END)), "loc_CEC7")
    SetScenarioFlags(0x2A, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CEC7")
    ClearScenarioFlags(0x2A, 5)

    label("loc_CEC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 1)), scpexpr(EXPR_END)), "loc_CED3")
    SetScenarioFlags(0x2A, 6)

    label("loc_CED3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CF25")
    RunExpression(0x7, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x10, 0x3, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    StopBGM(0x0)
    Jump("loc_CFA0")

    label("loc_CF25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CF77")
    OP_24(0x80)
    RunExpression(0x7, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x10, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1F()
    Sound(128, 1, 50, 0)
    Jump("loc_CFA0")

    label("loc_CF77")

    RunExpression(0x7, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x10, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1F()

    label("loc_CFA0")

    Return()

    # Function_26_CE14 end

    SaveToFile()

Try(main)
