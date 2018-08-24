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
        "Function_5_9AF",          # 05, 5
        "Function_6_B78",          # 06, 6
        "Function_7_E32",          # 07, 7
        "Function_8_E6A",          # 08, 8
        "Function_9_2F00",         # 09, 9
        "Function_10_2F8F",        # 0A, 10
        "Function_11_4AC3",        # 0B, 11
        "Function_12_4AF1",        # 0C, 12
        "Function_13_4B42",        # 0D, 13
        "Function_14_4B93",        # 0E, 14
        "Function_15_4BEB",        # 0F, 15
        "Function_16_4C35",        # 10, 16
        "Function_17_4C5B",        # 11, 17
        "Function_18_5587",        # 12, 18
        "Function_19_55C4",        # 13, 19
        "Function_20_6B94",        # 14, 20
        "Function_21_9137",        # 15, 21
        "Function_22_91A7",        # 16, 22
        "Function_23_A5DB",        # 17, 23
        "Function_24_B661",        # 18, 24
        "Function_25_C190",        # 19, 25
        "Function_26_C915",        # 1A, 26
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_921")

    ChrTalk(
        0x8,
        (
            "#01000FI'll inform the mayor\x01",
            "and CGF about the\x01",
            "terrorists.\x02\x03",
            "Dudley, I'm counting on\x01",
            "you to keep my guys\x01",
            "safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00603FYes, please leave it to\x01",
            "me.\x02\x03",
            "#00601F...C'mon, we're going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FRight!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_9AB")

    label("loc_921")


    ChrTalk(
        0x8,
        (
            "#01000FI don't know if something's\x01",
            "happened in the Geofront,\x01",
            "but be very careful.\x02\x03",
            "Dudley, I'm counting on you\x01",
            "to keep my guys safe.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9AB")

    TalkEnd(0xFE)
    Return()

    # Function_4_83F end

    def Function_5_9AF(): pass

    label("Function_5_9AF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B0B")

    ChrTalk(
        0xA,
        (
            "#01100FEveryone, have a safe\x01",
            "trip!\x02\x03",
            "#01109FEhehe, you be careful\x01",
            "too, ok Dudley?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00603FDidn't I tell you not to\x01",
            "address me so casually!?\x02",
        )
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
            "#00606F...Damn, whatever! Guys,\x01",
            "we're leaving, on the\x01",
            "double!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F(Hmm. As expected, not\x01",
            "even Dudley is a match\x01",
            "for KeA.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_B74")

    label("loc_B0B")


    ChrTalk(
        0xA,
        (
            "#01109FEveryone, have a safe\x01",
            "trip!\x02\x03",
            "Ehehe, you be careful\x01",
            "too, ok Dudley?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#00603F(Honestly...)\x02",
    )

    CloseMessageWindow()

    label("loc_B74")

    TalkEnd(0xFE)
    Return()

    # Function_5_9AF end

    def Function_6_B78(): pass

    label("Function_6_B78")

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
            "#00603FHmph. A self-important wolf as always.\x02\x03",
            "#00600FStill, since you're treated like a police\x01",
            "dog, there will be times when we'll need your\x01",
            "help. Be prepared to sortie at any time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01200F...Woof.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CA2")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_CA2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CD6")
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_CD6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D0A")
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_D0A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D3E")
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_D3E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D72")
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_D72")

    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#00306F(How can he call others\x01",
            "self-important,\x01",
            "right...?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(Haha, It's Dudley's way of\x01",
            "encouraging him. There's\x01",
            "nothing we can do.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_E2E")

    label("loc_E11")


    ChrTalk(
        0x9,
        "#01200FGrrrowl... Woof.\x02",
    )

    CloseMessageWindow()

    label("loc_E2E")

    TalkEnd(0xFE)
    Return()

    # Function_6_B78 end

    def Function_7_E32(): pass

    label("Function_7_E32")

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

    # Function_7_E32 end

    def Function_8_E6A(): pass

    label("Function_8_E6A")

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
            "#01003F#11PYes, yes...\x02\x03",
            "#01000FRight. They should be\x01",
            "back soon─\x02",
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
            "#01005F#11P...Oh, they just got\x01",
            "back.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x101,
        "Lloyd's Voice",
        "We're home.\x02",
    )

    CloseMessageWindow()
    OP_68(4100, 1750, 10400, 2500)
    SetCameraDistance(25000, 2500)
    Sleep(1000)
    OP_90(0x101, 1700, 4850, 14100, 180)
    BeginChrThread(0x101, 3, 0, 9)

    def lambda_1180():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1180)
    Sleep(400)

    def lambda_1194():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1194)
    Sleep(600)

    def lambda_11A8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x153, 2, lambda_11A8)
    Sleep(400)

    def lambda_11BC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_11BC)
    Sleep(600)

    def lambda_11D0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_11D0)
    WaitChrThread(0x101, 0)

    def lambda_11E5():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_11E5)
    WaitChrThread(0x102, 0)

    def lambda_11F6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_11F6)
    WaitChrThread(0x153, 0)

    def lambda_1207():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x153, 2, lambda_1207)
    WaitChrThread(0x109, 0)

    def lambda_1218():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1218)
    WaitChrThread(0x105, 0)

    def lambda_1229():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_1229)

    ChrTalk(
        0x153,
        "#5P#01110FChiieef! I'm baaack!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105FOh, are you on the\x01",
            "phone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#01004F#12PNo, it's not a problem.\x02",
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
            "#01002F#6PHey, go boot up that\x01",
            "terminal at once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FUh, excuse me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100FIs it a message from HQ?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01003F#6PYou'll understand once\x01",
            "you boot it up.\x02\x03",
            "#01001FKeA and you new guys,\x01",
            "too. Get over here.\x02",
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
        "#6P#10105FY-Yes, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FIt looks like something\x01",
            "happened.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_140F():
        OP_97(0x101, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_140F)
    Sleep(250)

    def lambda_142C():
        OP_97(0x153, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 0, lambda_142C)
    Sleep(250)

    def lambda_1449():
        OP_97(0x102, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1449)
    Sleep(250)

    def lambda_1466():
        OP_97(0x109, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1466)
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
        "#5P#00001FUmm...\x02",
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
        "#01109FAh, it's Tio!\x02",
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
            "#2668V#40W...Good evening. Long\x01",
            "time no see.\x07\x00\x02",
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
            "#00002FTio! Why are you...?\x02\x03",
            "Are you back in\x01",
            "Crossbell?\x02",
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
            "#30W...I'm still at the Epstein\x01",
            "Foundation research lab in\x01",
            "Lｳman State.\x02\x03",
            "Because it looks like my\x01",
            "return will be a little\x01",
            "later than anticipated...\x02\x03",
            "I selfishly asked them to\x01",
            "let me use this line.\x07\x00\x02",
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
            "#00109FTio... I'm so happy to see\x01",
            "you.\x02\x03",
            "#00105FHuh? I didn't think the\x01",
            "orbal net could connect to\x01",
            "networks outside the state.\x02",
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
            "Yes. Without a wire connection,\x01",
            "it's normally impossible to process\x01",
            "large volumes of information.\x02\x03",
            "However, at present, remote\x01",
            "connection tests between the\x01",
            "foundation and IBC are progressing.\x02\x03",
            "Well, about 10 powerful wireless\x01",
            "signal boosters have been installed\x01",
            "between Lｳman and Crossbell...\x02\x03",
            "That's why you're able to see and\x01",
            "hear me now.\x07\x00\x02",
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
        (
            "#00004FTechnological progress\x01",
            "is an amazing thing.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x153,
        (
            "#01110FHey, hey, Tio!\x02\x03",
            "You said "later than\x01",
            "anticipated", but when\x01",
            "are you coming back?\x02",
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
            "The end of this month,\x01",
            "or the beginning of\x01",
            "next, I think.\x02\x03",
            "Until then, I'll make do\x01",
            "with my doses of KeA via\x01",
            "this comm link.\x02\x03",
            "So, KeA, please smile\x01",
            "more.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x153,
        (
            "#01109FEhehe... Alright!\x02\x03",
            "#01110FC'mon Zeit. Come say hi\x01",
            "to Tio!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x9,
        "#01200FGrrrr, woof!\x02",
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
            "Yes, I'm fine. I'm doing\x01",
            "well.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x101,
        "#00002FHaha...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00104FHaha... So the orbal net\x01",
            "has even this kind of\x01",
            "feature.\x02",
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
            "By the way, it looks\x01",
            "like Randy isn't back\x01",
            "yet, either...\x02\x03",
            "And Noｱl and Wazy have\x01",
            "already joined?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x101,
        (
            "#00000FYeah. They just started\x01",
            "work today.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x109,
        (
            "#10102FHaha. Tio, long time no\x01",
            "see!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x105,
        (
            "#10302FYo. I'm here as well\x01",
            "now.\x02",
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
            "Haha... It's been a\x01",
            "while for me as well.\x02\x03",
            "Anyway, I can understand\x01",
            "Noｱl's transfer, but...\x02\x03",
            "It's a bit strange\x01",
            "seeing Wazy there.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x105,
        "#10309FAhaha. I think so too.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x109,
        (
            "#10106FGeez... It's no laughing\x01",
            "matter.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00004FHaha. Well for now,\x01",
            "these members will have\x01",
            "to do.\x02\x03",
            "#00002FBut Tio... Please come\x01",
            "back soon!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00102FYes. You see, without\x01",
            "you here, it's not the\x01",
            "real Support Section.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x153,
        "#01109FYeah, yeah!\x02",
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
            "*chuckle*... Then, I'll do\x01",
            "my best to return to you\x01",
            "soon.\x02\x03",
            "I was thinking of calling\x01",
            "Jona too, but...\x02\x03",
            "It looks like he's pulling\x01",
            "all-nighters, so he wouldn't\x01",
            "answer even if I called.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x101,
        (
            "#00000FI see. He's also doing his\x01",
            "best, huh.\x02\x03",
            "#00006FWell, it seems he's doing it\x01",
            "to make up for the damage he\x01",
            "caused to the foundation.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00104FI hope he doesn't overdo\x01",
            "it.\x02\x03",
            "#00100FAnd that goes for you\x01",
            "too, Tio, ok?\x02",
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
            "...I'm sorry, it seems\x01",
            "my time is up.\x02\x03",
            "They did a big favor,\x01",
            "letting me use this\x01",
            "experimental line...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x101,
        "#00001FOh...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00106FToo bad, I wanted to\x01",
            "talk more...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x8,
        (
            "#01004FWell, there will be\x01",
            "other chances.\x02\x03",
            "#01002FTio, contact us again\x01",
            "when your schedule\x01",
            "permits.\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 4)), scpexpr(EXPR_END)), "loc_2598")

    AnonymousTalk(
        0x101,
        (
            "#00004F...See you, Tio.\x02\x03",
            "#00002FWhen you get back, I'll\x01",
            "keep the promise I made\x01",
            "you back then.\x02",
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
            "Roger... I'll be looking\x01",
            "forward to it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x153,
        "#01111FA promise...?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00104FI'm a little worried\x01",
            "about that, but... I'm\x01",
            "sure it's fine.\x02\x03",
            "#00102FTio, please contact us\x01",
            "again.\x02",
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
            "#10109FBe well! Take care of\x01",
            "yourself!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_260B")

    label("loc_2598")


    AnonymousTalk(
        0x101,
        (
            "#00002FLater, Tio. Take care of\x01",
            "yourself.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        "#00102FPlease call anytime.\x02",
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

    label("loc_260B")


    AnonymousTalk(
        0x105,
        (
            "#10302FAdios, and have a\x01",
            "pleasant night.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x9,
        "#01200FGrrr... Woof.\x02",
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
            "Yes, see you again. Good\x01",
            "night.\x07\x00\x02",
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
        "#6P#01106FShe's gone...\x02",
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
            "#6P#00104FSomehow after seeing her\x01",
            "face, I want to see her\x01",
            "even more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10302FHaha. Youth.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10109FHaha. The Support\x01",
            "Section members sure are\x01",
            "close with each other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FHaha. In the beginning,\x01",
            "we were complete\x01",
            "strangers, though.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#00000FOh, Chief. Sorry for\x01",
            "getting back so late.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_28D9():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_28D9)
    Sleep(50)

    def lambda_28E9():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_28E9)
    Sleep(50)

    def lambda_28F9():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_28F9)
    Sleep(50)

    def lambda_2909():
        TurnDirection(0x153, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x153, 0, lambda_2909)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x153, 0)

    ChrTalk(
        0x8,
        (
            "#01004FI don't mind.\x02\x03",
            "#01000FI'll hear today's report\x01",
            "later.\x02\x03",
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
        (
            "#11P#00011FT-That's right, I\x01",
            "completely forgot!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#6P#00108FCome to think of it, we\x01",
            "haven't assigned duties\x01",
            "to these members...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2A44():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2A44)
    Sleep(100)

    def lambda_2A54():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x153, 2, lambda_2A54)
    WaitChrThread(0x109, 2)

    ChrTalk(
        0x109,
        (
            "#6P#10105FI see, in the Special\x01",
            "Support Section, we take\x01",
            "turns cooking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10305FOh, is that right?\x02\x03",
            "#10306FHmm. That's kind of a\x01",
            "pain.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12B, 3)), scpexpr(EXPR_END)), "loc_2C1C")

    ChrTalk(
        0x101,
        (
            "#00003FSince you've joined the Support\x01",
            "Section, Wazy, you'll do your\x01",
            "share of the work, too.\x02\x03",
            "#00000FUnexpectedly, it looks like you\x01",
            "know how to cook, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FWell, I must admit I'm\x01",
            "not too bad.\x02\x03",
            "#10300FBut since it's a pain, I\x01",
            "usually have Abbas do\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D52")

    label("loc_2C1C")


    ChrTalk(
        0x101,
        (
            "#00003FSince you've joined the Support\x01",
            "Section, Wazy, you'll do your\x01",
            "share of the work, too.\x02\x03",
            "#00000FWe got a new recipe notebook,\x01",
            "so I can teach you if you need\x01",
            "help, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FI'm happy to hear that,\x01",
            "but I'm not bad at\x01",
            "cooking.\x02\x03",
            "#10309FBut since it's a pain, I\x01",
            "usually have Abbas do\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D52")


    ChrTalk(
        0x101,
        (
            "#00013FHuh? Then don't\x01",
            "complain!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00109FHaha. Well for today,\x01",
            "shall we divide the work\x01",
            "between us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10102FIn that case, I think we\x01",
            "should pick something\x01",
            "quick and easy.\x02",
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
            "#01006F...Good grief. Guess\x01",
            "I'll go have a smoke,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#6P#01203FGrrowl... Woof.\x02",
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

    # Function_8_E6A end

    def Function_9_2F00(): pass

    label("Function_9_2F00")


    def lambda_2F05():
        OP_97(0x101, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2F05)
    Sleep(200)

    def lambda_2F22():
        OP_97(0x102, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2F22)
    Sleep(200)

    def lambda_2F3F():
        OP_97(0x153, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 0, lambda_2F3F)
    Sleep(200)

    def lambda_2F5C():
        OP_97(0x109, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2F5C)
    Sleep(200)

    def lambda_2F79():
        OP_97(0x105, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2F79)
    Return()

    # Function_9_2F00 end

    def Function_10_2F8F(): pass

    label("Function_10_2F8F")

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
        "#6P#00105FRandy's cousin?\x02",
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
            "#11P#04609F#3942V#30WEhehe, hiya. I'm Shirley\x01",
            "Orlando.\x02\x03",
            "#04602F#3943VYou're late. I was\x01",
            "getting tired of\x01",
            "waiting.\x02",
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
            "What the hell'd you come\x01",
            "here for?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11P#04605FAww, Randy. That's cold!\x02\x03",
            "#04606FAren't you being a little too\x01",
            "cold to your cute cousin you\x01",
            "haven't seen for two years?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303F#30WCut the crap and\x01",
            "answer... Why have you\x01",
            "come?\x02\x03",
            "#00311FWait, no─ What are you\x01",
            "doing here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#11P#04604FHaha...\x02",
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
            "#3944V#40WYou're slow, Randy.\x02\x03",
            "#3945V#30WIf I had set and antipersonnel\x01",
            "trap, you'd all be mincemeat\x01",
            "the moment you entered.\x02\x03",
            "#3946VWhen did you become such a\x01",
            "fool?\x02",
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
        "#12P#N#10107FWhat are you saying!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0xB,
        (
            "#11P#04612FHaha, no need to worry.\x01",
            "I didn't set any traps.\x02\x03",
            "#04602FThough it might've been\x01",
            "fun if Randy was alone.\x02\x03",
            "#04604FOutside of wartime, I\x01",
            "don't want to involve\x01",
            "civilians, you see.\x02",
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
        "#01105F#6P#NHuuuh?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#6P#N#10306F*sigh*... We have\x01",
            "another radical kid\x01",
            "here.\x02",
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
            "#12P#00003F─You. You're Shirley, right?\x02\x03",
            "#00001FAllow me to introduce\x01",
            "myself... I'm Lloyd Bannings\x01",
            "of the Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11P#04602FOh, hiya.\x02\x03",
            "#04609FSorry for the other day,\x01",
            "'k? I bit her earlobe\x01",
            "unconsciously...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006F...That aside.\x02\x03",
            "#00013FThis is a Crossbell police annex, and even\x01",
            "the sofa you're sitting on was provided\x01",
            "with public funds.\x02\x03",
            "And about traps, involving people and\x01",
            "such... Could you refrain from making such\x01",
            "careless statements in front of a child?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11P#04612FAhaha, sorry, sorry.\x02\x03",
            "#04611FI guess I wanted to play\x01",
            "with him since I missed\x01",
            "him so much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306F...Hmph. So I'm your\x01",
            "favorite ball, huh.\x02\x03",
            "#00301FYou're probably here to\x01",
            "invite me to come talk to\x01",
            "uncle. I'm right, aren't I?\x02",
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

    def lambda_3A87():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3A87)
    Sleep(50)

    def lambda_3A97():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3A97)
    Sleep(50)

    def lambda_3AA7():
        TurnDirection(0x109, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3AA7)
    Sleep(50)

    def lambda_3AB7():
        TurnDirection(0x105, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3AB7)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        "#12P#00005FHuh!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00101FThen...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#11P#04604FHaha, right answer.\x02",
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
            "#04602F#11PPapa said it before, right?\x01",
            "That he'd need to talk to\x01",
            "you sooner or later.\x02\x03",
            "We'll be busy tomorrow, so\x01",
            "how about tonight?\x02\x03",
            "#04605FAh, but you can refuse too,\x01",
            "you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FHah! If I refused, he'd\x01",
            "stop at nothing to make\x01",
            "it happen.\x02\x03",
            "#00311FI know how you guys\x01",
            "work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#04609F#11PHaha. You've gotten back\x01",
            "into your stride.\x02\x03",
            "#04602FPapa said he'd head to\x01",
            "Neue-Blanc ahead of you\x01",
            "guys. Whaddya say?\x02",
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
            "#5P#00300FSorry everyone, but I\x01",
            "won't be joining you for\x01",
            "dinn...\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x79)
    WaitChrThread(0xA, 3)

    ChrTalk(
        0xA,
        (
            "#6P#01101FHey Randy.\x02\x03",
            "This lady... Could she\x01",
            "be a bad person?\x02",
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

    def lambda_3E5A():
        TurnDirection(0x104, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3E5A)
    Sleep(50)

    def lambda_3E6A():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3E6A)
    Sleep(50)

    def lambda_3E7A():
        TurnDirection(0x102, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3E7A)
    Sleep(50)

    def lambda_3E8A():
        TurnDirection(0x109, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3E8A)
    Sleep(50)

    def lambda_3E9A():
        TurnDirection(0x105, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3E9A)
    Sleep(50)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        "#11P#00011FKeA!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00107FKeA, get back!\x02",
    )

    CloseMessageWindow()
    OP_68(3920, 800, 5320, 1000)
    MoveCamera(42, 20, 0, 1000)
    OP_6E(400, 1000)
    SetCameraDistance(24000, 1000)

    def lambda_3F1F():
        OP_95(0xFE, 1400, 0, 5500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3F1F)
    Sleep(300)

    def lambda_3F3C():
        OP_95(0xFE, 1800, 0, 4300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3F3C)
    WaitChrThread(0x102, 1)

    def lambda_3F5A():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3F5A)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0xA, 500)

    def lambda_3F72():
        OP_96(0xFE, 0x1F4, 0x0, 0x13EC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3F72)

    def lambda_3F8C():
        OP_96(0xFE, 0x384, 0x0, 0xF3C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3F8C)

    def lambda_3FA6():
        OP_96(0xFE, 0x3E8, 0x0, 0x12C0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3FA6)
    Sleep(300)

    def lambda_3FC3():
        OP_95(0xFE, 1300, 0, 2700, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3FC3)
    Sleep(300)

    def lambda_3FE0():
        OP_95(0xFE, 2200, 0, 2500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3FE0)
    WaitChrThread(0x101, 1)

    def lambda_3FFE():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3FFE)

    ChrTalk(
        0xB,
        (
            "#04606F#11PThat's pretty mean.\x02\x03",
            "#04605FBut what's with that\x01",
            "girl!? She's\x01",
            "ridiculously cute!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#6P#01105FHmm?\x02",
    )

    CloseMessageWindow()

    def lambda_4081():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4081)
    Sleep(100)

    def lambda_4091():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4091)

    def lambda_409E():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_409E)
    WaitChrThread(0x104, 2)
    Sleep(150)

    ChrTalk(
        0x104,
        (
            "#6P#00303FWe're taking care of\x01",
            "her.\x02\x03",
            "#00312F#30W...Lay a hand on her and\x01",
            "I'll kill you.\x02",
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
            "#04602FAt least I'll refrain\x01",
            "from blowing up this\x01",
            "building.\x02\x03",
            "#04609FAh, that's a joke, of\x01",
            "course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106F(W-What the heck is this\x01",
            "conversation...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10308F(This is bad for your\x01",
            "heart.)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#5P#00304FWell that's how it is,\x01",
            "so I'll go see uncle.\x02\x03",
            "#00300FI'll be back tonight, so\x01",
            "don't worry too much.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_42B3():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_42B3)

    ChrTalk(
        0x102,
        "#6P#00108FB-But...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10101FIt's too dangerous!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006F─Hey, Randy.\x02\x03",
            "#00000FWhat if we ask to meet\x01",
            "him, too?\x02",
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

    def lambda_43C7():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_43C7)
    Sleep(50)

    def lambda_43D7():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_43D7)
    Sleep(50)

    def lambda_43E7():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_43E7)
    Sleep(50)

    def lambda_43F7():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_43F7)
    Sleep(50)

    def lambda_4407():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4407)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x104,
        "#5P#00305F!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00107FWhat!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#11P#10111FL-Lloyd!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00004FAs Support Section leader,\x01",
            "greeting a co-worker's relative\x01",
            "is just good manners, right?\x02\x03",
            "#00000FAnd also, he's in a high class\x01",
            "club. It could be nice as a\x01",
            "social study.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#04611F#11PWow... You're funny,\x01",
            "mister.\x02\x03",
            "#04609FSure, sure! I'm here for\x01",
            "Randy anyway. Come\x01",
            "along!♪\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0xB, 500)
    Sleep(150)

    ChrTalk(
        0x105,
        (
            "#6P#10304FHaha, if that's the\x01",
            "case, then allow me to\x01",
            "come too.\x02\x03",
            "#10302FThe high class club\x01",
            "Neue-Blanc... I always\x01",
            "wanted to pay a visit.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x105, 500)

    ChrTalk(
        0xB,
        (
            "#04612F#11PWelcome then, Mr.\x01",
            "Handsome!\x02\x03",
            "#04605FHuh... Could you be a\x01",
            "girl?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10309FHehe. Let's go with boy,\x01",
            "for now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00306FAaaagh!! The heck are\x01",
            "you guys thinking!?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0xB, 500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x104,
        (
            "#6P#00307FYou too, Shirley. Would\x01",
            "you just shut up\x01",
            "already?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x104, 500)
    Sleep(150)

    ChrTalk(
        0xB,
        (
            "#04604F#11PFine, fine. The car's\x01",
            "ready for all of you.\x02\x03",
            "#04602FOh yeah, are you ladies\x01",
            "coming too?\x02\x03",
            "#04606FAh, but that kid and the\x01",
            "wolf can't come, as you\x01",
            "might imagine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F...Elie, Noｱl. Please\x01",
            "dine with KeA.\x02\x03",
            "#00008FAnd contact the chief,\x01",
            "just in case.\x02\x03",
            "#00013FZeit, I need you to\x01",
            "guard this place until\x01",
            "chief gets back.\x02",
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
            "#00106F...I understand. Leave\x01",
            "watching the place to\x01",
            "us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#11P#10101FPlease, be careful!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#01110FHey Lloyd, you going\x01",
            "somewhere?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 500)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#12P#00004FYeah, I'm going out with\x01",
            "Randy and Wazy for a\x01",
            "bit.\x02\x03",
            "#00000FWe could be out late, so\x01",
            "don't stay up late and\x01",
            "get to sleep, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5P#01109FOkay! See you later!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        (
            "#5P#00306FDamn. Why is this\x01",
            "happening to me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FWell, we'd best prepare\x01",
            "for the worst, eh?\x02",
        )
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

    # Function_10_2F8F end

    def Function_11_4AC3(): pass

    label("Function_11_4AC3")

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

    # Function_11_4AC3 end

    def Function_12_4AF1(): pass

    label("Function_12_4AF1")


    def lambda_4AF6():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4AF6)
    Sleep(300)

    def lambda_4B13():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4B13)
    WaitChrThread(0xFE, 1)

    def lambda_4B28():
        OP_97(0xFE, 0x5DC, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4B28)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_12_4AF1 end

    def Function_13_4B42(): pass

    label("Function_13_4B42")


    def lambda_4B47():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4B47)
    Sleep(300)

    def lambda_4B64():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4B64)
    WaitChrThread(0xFE, 1)

    def lambda_4B79():
        OP_97(0xFE, 0x3E8, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4B79)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_13_4B42 end

    def Function_14_4B93(): pass

    label("Function_14_4B93")

    Sleep(500)

    def lambda_4B9B():
        OP_96(0xFE, 0x2BC, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4B9B)

    def lambda_4BB5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4BB5)
    WaitChrThread(0xFE, 1)

    def lambda_4BCA():
        OP_96(0xFE, 0x190, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4BCA)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_14_4B93 end

    def Function_15_4BEB(): pass

    label("Function_15_4BEB")

    Sleep(1500)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x0)

    def lambda_4BFB():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4BFB)

    def lambda_4C15():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4C15)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x9, 0x6)
    SetChrSubChip(0x9, 0x0)
    OP_93(0x9, 0x2D, 0x1F4)
    Return()

    # Function_15_4BEB end

    def Function_16_4C35(): pass

    label("Function_16_4C35")


    def lambda_4C3A():
        OP_95(0xFE, 1900, 0, 5200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4C3A)
    WaitChrThread(0xA, 1)
    TurnDirection(0xA, 0xB, 500)
    Return()

    # Function_16_4C35 end

    def Function_17_4C5B(): pass

    label("Function_17_4C5B")

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
            "I see. So that's what\x01",
            "happened.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x102,
        (
            "#00106FYes... I'm sorry.\x02\x03",
            "#00108FI know you don't call\x01",
            "that often.\x02",
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
            "Don't worry about it.\x01",
            "I'm fine just hearing\x01",
            "your voice.\x02\x03",
            "That's all for today.\x01",
            "I'll call again.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x102,
        "#00100FOkay, understood.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0xA,
        "#01102FBye, Tio!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x109,
        (
            "#10100FUmm... Don't worry about\x01",
            "us too much, ok?\x02",
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
            "Alright. Goodbye.\x07\x00\x02",
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
            "#00108FLloyd and the others...\x01",
            "I really wonder if\x01",
            "they'll be all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FWhen those are the kind of\x01",
            "people they're talking to,\x01",
            "you're right to be worried.\x02",
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

    def lambda_51E1():

        label("loc_51E1")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_51E1")

    QueueWorkItem2(0xA, 2, lambda_51E1)
    Sleep(50)

    def lambda_51F6():

        label("loc_51F6")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_51F6")

    QueueWorkItem2(0x109, 2, lambda_51F6)
    Sleep(50)

    def lambda_520B():

        label("loc_520B")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_520B")

    QueueWorkItem2(0x102, 2, lambda_520B)

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

    def lambda_526E():
        OP_95(0xFE, 1000, 0, 1500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_526E)

    def lambda_5288():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_5288)
    WaitChrThread(0x8, 1)
    TurnDirection(0x8, 0x102, 500)
    OP_6F(0x79)
    Sound(104, 0, 100, 0)

    ChrTalk(
        0x102,
        "#00102FChief!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10102F#6PG-Good work.\x02",
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

    def lambda_532C():
        OP_95(0xFE, 12300, 850, 9700, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_532C)
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
            "#6P#01000FSorry I'm late. What's\x01",
            "the situation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00106FThe same as when I\x01",
            "contacted you earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10101F...Would it be better if\x01",
            "we were on standby in\x01",
            "the shop nearby?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P#01004FAh, don't be so worried.\x02\x03",
            "#01002FSection One is\x01",
            "surveilling the area\x01",
            "around Neue-Blanc.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10105FAh!\x02",
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
            "#6P#01006FStill, if they were worried\x01",
            "about it, they could avoid\x01",
            "being surveilled, I guess.\x02\x03",
            "#01000F...Anyhow, we can only wait\x01",
            "for them to return.\x02",
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

    # Function_17_4C5B end

    def Function_18_5587(): pass

    label("Function_18_5587")


    def lambda_558C():
        OP_95(0xFE, 1000, 850, 10000, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_558C)
    WaitChrThread(0x8, 1)

    def lambda_55AA():
        OP_95(0xFE, 10000, 850, 10000, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_55AA)
    WaitChrThread(0x8, 1)
    Return()

    # Function_18_5587 end

    def Function_19_55C4(): pass

    label("Function_19_55C4")

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
        "#12P#00108FNo way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FReally... What an\x01",
            "unbelievable group.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01003FWell, the part about you\x01",
            "becoming the next War\x01",
            "God aside...\x02\x03",
            "#01000FIt was a pretty good\x01",
            "haul, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FYeah...\x02\x03",
            "#00308FThey've accepted a hundred million\x01",
            "mira contract...\x02\x03",
            "#00301FAnd based on how things are going,\x01",
            "I'm certain they're working for\x01",
            "the Imperial government.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FAnd they said they'd be\x01",
            "busy starting\x01",
            "tomorrow...\x02\x03",
            "#10300FThey must be planning to\x01",
            "do something during the\x01",
            "trade conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01003FHmm, but what could that\x01",
            "hundred million mira contract\x01",
            "be for, specifically?\x02\x03",
            "#01001F─Lloyd, what do you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005F...Ah, right.\x02",
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
            "#1KWhat is the hundred million mira contract for?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Assassination of the Republican President\x01",      # 0
            "Protecting the Blood and Iron Chancellor\x01",       # 1
            "Taking care of Heiyue\x01",                          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5A34"),
        (1, "loc_5CAC"),
        (2, "loc_5EB4"),
        (SWITCH_DEFAULT, "loc_60F1"),
    )


    label("loc_5A34")


    ChrTalk(
        0x101,
        (
            "#12P#00008FThe assassination of Republican\x01",
            "President Rocksmith...\x02\x03",
            "#00006F...No, that's not it.\x02\x03",
            "For the sake of argument, if\x01",
            "that were the case, 100 million\x01",
            "mira would be too little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01004FHehe. Exactly.\x02\x03",
            "#01002FBased on what we know at this point,\x01",
            "protecting the Blood and Iron\x01",
            "Chancellor is the most likely option.\x02",
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
        "#12P#00011FAh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00101FI-I see.\x02\x03",
            "They say Chancellor Osborne\x01",
            "has a considerable number of\x01",
            "enemies within the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F...That's likely, then.\x02",
    )

    CloseMessageWindow()
    Jump("loc_60F1")

    label("loc_5CAC")

    OP_2C(0xA3, 0x1)

    ChrTalk(
        0x101,
        (
            "#12P#00003FThis is just my intuition but...\x02\x03",
            "#00001FThey say the Blood and Iron\x01",
            "Chancellor has a considerable number\x01",
            "of enemies within the Empire.\x02\x03",
            "It's possible they've been hired to\x01",
            "protect the chancellor from them\x01",
            "while he's in Crossbell.\x02",
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

    def lambda_5E16():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5E16)
    Sleep(50)

    def lambda_5E26():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5E26)
    Sleep(50)

    def lambda_5E36():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5E36)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x102,
        "#12P#00105FAh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301FI see... That seems\x01",
            "likely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01004FHehe... Good\x01",
            "observation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60F1")

    label("loc_5EB4")


    ChrTalk(
        0x101,
        (
            "#12P#00008FTaking care of Heiyue...\x02\x03",
            "#00006FOh, but during a trade\x01",
            "conference is the wrong timing\x01",
            "for that type of contract.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01004FHehe. Exactly.\x02\x03",
            "#01002FBased on what we know at this point,\x01",
            "protecting the Blood and Iron\x01",
            "Chancellor is the most likely option.\x02",
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
        "#12P#00011FAh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00101FI-I see.\x02\x03",
            "They say Chancellor Osborne\x01",
            "has a considerable number of\x01",
            "enemies within the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F...That's likely, then.\x02",
    )

    CloseMessageWindow()
    Jump("loc_60F1")

    label("loc_60F1")


    ChrTalk(
        0x105,
        (
            "#12P#10303FHmm, but isn't a hundred\x01",
            "million mira a little\x01",
            "too much for that?\x02\x03",
            "#10301FThe chancellor will be\x01",
            "bringing his own\x01",
            "escorts, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FThat's true...\x02\x03",
            "#10101FIt seems both Imperial and Republican\x01",
            "officials will be traveling with a\x01",
            "considerable number of escort officers.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_64A9")
    OP_2C(0xA3, 0x2)

    ChrTalk(
        0x101,
        (
            "#5P#00003FWe can assume the protection offered\x01",
            "by the contract is different than\x01",
            "that of the chancellor's escorts.\x02\x03",
            "#00008FStill, based on their actions, it's\x01",
            "certain that they're trying to gain\x01",
            "an understanding of Crossbell's land.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FSightings of them at Armorica\x01",
            "Village, Mainz and Bellguard Gate\x01",
            "would seem to indicate that.\x02\x03",
            "#10304FSecuring food supplies and conducting\x01",
            "septium trade are plausible reasons\x01",
            "to visit those places, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00003FYeah. I think their real reasons\x01",
            "for visiting was something else.\x02\x03",
            "#00001FThat's why we, like the bracers,\x01",
            "need to be able to respond, no\x01",
            "matter what happens.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_660B")

    label("loc_64A9")


    ChrTalk(
        0x101,
        (
            "#5P#00003FWe can assume the protection offered\x01",
            "by the contract is different than\x01",
            "that of the chancellor's escorts.\x02\x03",
            "#00008FStill, based on their actions, it's\x01",
            "certain that they're trying to gain\x01",
            "an understanding of Crossbell's land.\x02\x03",
            "#00001FThat's why we, like the bracers, need\x01",
            "to be able to respond, no matter what\x01",
            "happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10300FHmm...\x02",
    )

    CloseMessageWindow()

    label("loc_660B")


    ChrTalk(
        0x102,
        (
            "#12P#00106FIndeed... I feel the\x01",
            "same.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00308F...............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01000F─Well, that's as much as we\x01",
            "can deduce at present.\x02\x03",
            "#01003FTomorrow, each nation's head\x01",
            "of state will arrive and\x01",
            "Orchis Tower will be unveiled.\x02\x03",
            "#01002FOh, and by the way, you guys\x01",
            "are going to be there, you\x01",
            "know?\x02",
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

    def lambda_67BB():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_67BB)
    Sleep(50)

    def lambda_67CB():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_67CB)
    Sleep(50)

    def lambda_67DB():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_67DB)
    Sleep(50)

    def lambda_67EB():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_67EB)
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
        (
            "#12P#00105FBy "there" do you\x01",
            "mean... The unveiling\x01",
            "ceremony?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01004FIt appears you've caught\x01",
            "the attention of Red\x01",
            "Constellation.\x02\x03",
            "#01000F─Counterintelligence and\x01",
            "antiterrorism isn't\x01",
            "normally your job.\x02\x03",
            "Take this as an opportunity\x01",
            "get a little higher level\x01",
            "view of the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FHaha... Didn't want to\x01",
            "hear that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FUmm, we're participating\x01",
            "in the unveiling ceremony\x01",
            "security detail?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01003FWell, that's how it'll be on paper, but more\x01",
            "importantly, I want you to devote yourselves\x01",
            "to observing the situation at that ceremony.\x02\x03",
            "#01002FThe atmosphere at the start of the trade\x01",
            "conference... And the aura given off by the\x01",
            "heads of state.\x02\x03",
            "That should give you a different view of\x01",
            "things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHehe, then we'll observe\x01",
            "from front row seats.\x02",
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

    # Function_19_55C4 end

    def Function_20_6B94(): pass

    label("Function_20_6B94")

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
            "#01001F─I see. Terrorists\x01",
            "targeting each leader,\x01",
            "huh.\x02",
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
            "#00606F#5PDamn. The possibility was\x01",
            "there, but to think the\x01",
            "threat is that concrete...\x02\x03",
            "#00610FThe Empire and Republic...\x01",
            "What the hell are they\x01",
            "thinking!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1P#01003FThey must have some\x01",
            "objective behind their\x01",
            "actions.\x02\x03",
            "#01000FWe should inform the\x01",
            "mayor's office and CGF,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00603F#5PYes, leave that to me.\x02\x03",
            "#00601F...Anyway, when I heard\x01",
            "you boarded the Arseille,\x01",
            "I could hardly believe it.\x02\x03",
            "On top of that, you heard\x01",
            "that much from those state\x01",
            "guest class VIPs...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6F4C():
        TurnDirection(0x101, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6F4C)
    Sleep(100)

    def lambda_6F5C():
        TurnDirection(0x109, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6F5C)
    Sleep(100)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x101,
        (
            "#6P#00012FHaha, so even Section\x01",
            "One checked up on them,\x01",
            "huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00302FWell it was sudden for us,\x01",
            "too. Could you not give us\x01",
            "such a hard time over it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00607F#5PHmph. It may have been sudden, but\x01",
            "how about accepting AFTER consulting\x01",
            "with your superiors next time!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1P#01004FHehe, what are you doing making\x01",
            "these guys follow standard\x01",
            "procedure?\x02\x03",
            "#01002FBesides, their hosts were\x01",
            "anything but the usual suspects.\x01",
            "I think it was just fine.\x02",
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
            "#12P#00309FAh, but both the princess\x01",
            "and the prince were very\x01",
            "strange.\x02\x03",
            "#00300FEspecially Prince Olivert.\x01",
            "I wouldn't have thought he\x01",
            "was such an oddball.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_71F3():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_71F3)
    Sleep(100)

    def lambda_7203():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7203)
    Sleep(100)

    def lambda_7213():
        TurnDirection(0x105, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7213)
    Sleep(100)

    def lambda_7223():
        TurnDirection(0x109, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7223)
    Sleep(100)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x102,
        (
            "#5P#00106FThat's rude, Randy.\x02\x03",
            "#00100FAlso, I don't know if you'd\x01",
            "call it happy, but... He's\x01",
            "a very carefree person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00004FBut, I think he has\x01",
            "carefully considered the\x01",
            "situation.\x02\x03",
            "#00000FThat major that guarding\x01",
            "him seemed incredibly\x01",
            "skilled, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10102FAlso, Princess Klaudia\x01",
            "and Captain Julia were\x01",
            "so lovely!\x02\x03",
            "#10112FThe princess was so kind\x01",
            "yet elegant, and Captain\x01",
            "Julia was just so cool!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#11PHaha. Looks like you\x01",
            "managed to get an autograph\x01",
            "for your sister too, right?\x02",
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
            "#00600FWell whatever─ Even just knowing\x01",
            "of the existence of terrorists\x01",
            "can be considered a good result.\x02\x03",
            "I had better make adjustments to\x01",
            "tomorrow's security detail...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7526():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7526)
    Sleep(100)

    def lambda_7536():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7536)
    Sleep(100)

    def lambda_7546():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7546)
    Sleep(100)

    def lambda_7556():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7556)
    Sleep(100)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x101,
        (
            "#6P#00001FTomorrow is critical...\x01",
            "It's the trade\x01",
            "conference's main session.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1P#01003FYeah. The heads of state are returning\x01",
            "to their respective countries at noon\x01",
            "the day after tomorrow.\x02\x03",
            "#01001FIf something's going to happen, it'll\x01",
            "likely be tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FThe conference starts at\x01",
            "noon, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00600F#5PYeah. The trade conference\x01",
            "will begin at 1PM tomorrow\x01",
            "on Orchis Tower 35F.\x02\x03",
            "It's scheduled to continue\x01",
            "until evening with a\x01",
            "single break in between.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00305FThen, if we just protect the heads\x01",
            "of state during the conference, we\x01",
            "should be fine, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00604F#5PWell, a full security detail will\x01",
            "be set up inside Orchis Tower.\x02\x03",
            "The building itself has its own\x01",
            "security system, so the conference\x01",
            "should be rather secure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1P#01003FIn addition, Arios is scheduled\x01",
            "to participate in the venue\x01",
            "security detail as well.\x02\x03",
            "#01002FHe'll serve as a guild observer\x01",
            "too. It really can't get any\x01",
            "safer.\x02",
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
            "#12P#10108FIn that case, the most dangerous\x01",
            "moments might be before and\x01",
            "after the conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#12PSuch as VIPs getting sniped\x01",
            "from a distance just as\x01",
            "they exit the tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FHonestly, that's what\x01",
            "I'm most afraid of.\x02",
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
        "#11P#13AHey, Lloyd.\x02",
    )

    CloseMessageWindow()
    OP_68(64000, 1000, 6300, 2000)
    MoveCamera(62, 15, 0, 2000)
    OP_6E(400, 2000)
    SetCameraDistance(24000, 2000)
    OP_5A()
    SetChrPos(0xA, 61500, 0, 3800, 90)

    def lambda_7AD2():
        TurnDirection(0x109, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7AD2)
    Sleep(50)

    def lambda_7AE2():
        TurnDirection(0x102, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7AE2)
    Sleep(50)

    def lambda_7AF2():
        TurnDirection(0x104, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7AF2)
    Sleep(50)

    def lambda_7B02():
        TurnDirection(0x105, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7B02)
    Sleep(50)

    def lambda_7B12():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7B12)
    Sleep(50)

    def lambda_7B22():
        TurnDirection(0x10A, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_7B22)
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

    def lambda_7B75():
        OP_96(0xFE, 0xEE48, 0x0, 0xCE4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_7B75)

    def lambda_7B8F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_7B8F)
    WaitChrThread(0xA, 1)

    def lambda_7BA4():
        OP_95(0xFE, 61500, 0, 3800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_7BA4)
    WaitChrThread(0xA, 1)
    TurnDirection(0xA, 0x10A, 500)
    OP_6F(0x79)
    OP_63(0xA, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xA,
        (
            "#12P#01105F#3610V#30WAh, it's that sullen\x01",
            "guy!\x02",
        )
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
            "#5P#00603F...You haven't been\x01",
            "disciplining her, have\x01",
            "you.\x02",
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
            "#00112F#5PKeA, this is Detective\x01",
            "Dudley.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12P#01109FYeah, Dudley!\x02\x03",
            "#01110FLong time no see. How\x01",
            "have you been?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#5P#00604FHmph, as a Section One\x01",
            "detective, I am always\x01",
            "in top form.\x02\x03",
            "#00607F...That's not it! Stop\x01",
            "addressing me so\x01",
            "casually!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12P#01106FAww, can't I?\x02\x03",
            "#01111FThen, Old Man Dudley?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x10A,
        "#5P#00610FWho's an old man now!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10112FN-Now now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00309FHaha. From the viewpoint\x01",
            "of a child, you're\x01",
            "plenty old.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#11PSo, KeA? What do you\x01",
            "need?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#12P#01106FOh, that's right.\x02\x03",
            "#01100FUmm, there was a call\x01",
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
            "#00105F#5PMy, it appears that it\x01",
            "didn't ring...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12P#01109FAh, not the normal one,\x01",
            "the one with a face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#5PThe terminal? You're\x01",
            "getting pretty good at\x01",
            "that, KeA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F#5PWas it PeTiote? I guess\x01",
            "she called this evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12P#01104FUh-uh, it was someone\x01",
            "with freckles.\x02\x03",
            "#01100FHis face turned red and\x01",
            "then pale somehow...\x02",
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
            "#4SYou're late!\x02\x03",
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
            "#00012FHaha, sorry.\x02\x03",
            "#00002FIt's been a while\x01",
            "though, Jona. How have\x01",
            "you been?\x02",
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
            "Spare the greetings, for\x01",
            "crying out loud!\x02\x03",
            "I want to ask for a\x01",
            "favor. It's urgent!\x02\x03",
            "Can you go check out my\x01",
            "base!?\x07\x00\x02",
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
            "#00105FBase... The place you\x01",
            "were staying?\x02",
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
            "Yeah, the place with the No.8\x01",
            "control terminal in Geofront\x01",
            "B-Division!\x02\x03",
            "It seems someone's been using\x01",
            "that terminal ever since\x01",
            "yesterday without permission.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x101,
        (
            "#00001FWithout permission, he\x01",
            "says...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x109,
        "#10105FHow do you know that?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        (
            "#00301FJona, buddy. Maybe you should say\x01",
            "they're using it without\x01",
            "permission, the same as yourself.\x02",
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
            "A-Anyway!\x02\x03",
            "Because I was going to be away, I\x01",
            "set up strong protection on that\x01",
            "terminal!\x02\x03",
            "And, in the event it was breached, I\x01",
            "had it send an alert when I'm doing\x01",
            "orbal net remote connection tests...\x02\x03",
            "And today, I got that alert!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x101,
        "#00013FThen that means...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x105,
        (
            "#10303F...Someone hacked the\x01",
            "terminal you protected.\x02\x03",
            "#10301FIs that it?\x02",
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
            "Yeah, exactly! They're a\x01",
            "skilled hacker, no doubt\x01",
            "about it!\x02\x03",
            "Anyway, I want you to catch\x01",
            "them so they don't touch my\x01",
            "terminal ever again!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x104,
        (
            "#00306FMan. Asking us to turn a blind eye\x01",
            "AND asking us to do this thing for\x01",
            "him? How impertinent can you get?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00108FBut, he said it was a\x01",
            "skilled hacker... I'm a\x01",
            "little worried about that.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00003FYeah. Renne went home, and I\x01",
            "don't think Chief Roberts\x01",
            "would do anything like that.\x02\x03",
            "#00001FFor now, we'll take a look\x01",
            "around the area. We'll\x01",
            "contact you later.\x02",
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
            "Yeah, I'm counting on\x01",
            "you!\x07\x00\x02",
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
        "#01000F#5PWhat, you're going?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#00003FYes, just to be sure.\x02\x03",
            "#00000FI could go alone, if you\x01",
            "guys want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00301FWhoa there. Don't be so\x01",
            "reckless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FThat's right... It's not\x01",
            "necessarily a hacker\x01",
            "that's there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10101FLet's go together!\x02",
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
            "#3452V#30W─Wait.\x02\x03",
            "#4106VI will accompany you.\x02",
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

    def lambda_8D4D():
        TurnDirection(0x101, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8D4D)
    Sleep(50)

    def lambda_8D5D():
        TurnDirection(0x104, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_8D5D)
    Sleep(50)

    def lambda_8D6D():
        TurnDirection(0x109, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8D6D)
    Sleep(50)

    def lambda_8D7D():
        TurnDirection(0x105, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8D7D)
    Sleep(50)

    def lambda_8D8D():
        TurnDirection(0x102, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8D8D)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)

    ChrTalk(
        0x101,
        "#11P#00005FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FWow. To what do we owe\x01",
            "this honor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00603F#5PHmph, I just want to understand an\x01",
            "irregular element before the trade\x01",
            "conference, even if just a little.\x02\x03",
            "#00601FTime is precious. Let's go at\x01",
            "once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00011FR-Roger that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FHaha, then let's go for\x01",
            "some light after-meal\x01",
            "exercise.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x10E, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x102,
        (
            "#12P#00100FChief, KeA, see you\x01",
            "later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01002F#5PSure! Be careful out\x01",
            "there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#6P#01109FBye-bye!\x02",
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
            "Detective Dudley has\x01",
            "joined the party.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You can change attack\x01",
            "members from [TACTICS]\x01",
            "under the camp menu.\x07\x00\x02",
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

    # Function_20_6B94 end

    def Function_21_9137(): pass

    label("Function_21_9137")

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

    # Function_21_9137 end

    def Function_22_91A7(): pass

    label("Function_22_91A7")

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
            "#01110FHey Zeit! Tio's back!\x02",
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
        "#12P#00202FI'm home, KeA, Zeit.\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)

    def lambda_93C0():
        OP_96(0xFE, 0x2BC, 0x0, 0x1194, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_93C0)
    WaitChrThread(0xA, 1)
    TurnDirection(0x103, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#6P#00204FChief Sergei, I just got\x01",
            "back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01004FYeah, welcome home.\x02\x03",
            "#01002FHmph, looks like you\x01",
            "saved your friends from\x01",
            "that predicament.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00004FYeah. She really saved\x01",
            "us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00106FIf Tio hadn't come for\x01",
            "us, I don't know what\x01",
            "would've happened...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10112FYeah, that's a scary\x01",
            "thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00604F...I'm obliged to thank\x01",
            "you for your help this\x01",
            "time only.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        (
            "#5P#00205FWell, that was no big\x01",
            "deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00309FHaha, don't get all\x01",
            "embarrassed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FWell that really was\x01",
            "impeccable timing.\x02\x03",
            "#10300FAgainst a hacker like\x01",
            "that, with just us it'd\x01",
            "be game over.\x02",
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
            "#6P#00003F─Chief, Mr. Dudley.\x02\x03",
            "#00001FAbout tomorrow's trade\x01",
            "conference... May we participate\x01",
            "in Orchis Tower security, too?\x02",
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

    def lambda_97BB():
        TurnDirection(0xC, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_97BB)
    Sleep(50)

    def lambda_97CB():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_97CB)
    Sleep(50)

    def lambda_97DB():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_97DB)
    Sleep(50)

    def lambda_97EB():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_97EB)
    Sleep(50)

    def lambda_97FB():
        TurnDirection(0x8, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_97FB)
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
            "#12P#00305FHey now. What's this all\x01",
            "of sudden?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P#01000FHmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00600F#11P...Didn't I tell you the\x01",
            "venue security\x01",
            "organization is perfect?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FHowever, today's hacker\x01",
            "obtained the tower\x01",
            "blueprints from somewhere.\x02\x03",
            "#00008FThese are not Yin's words,\x01",
            "but there's a possibility\x01",
            "that something's going on...\x02\x03",
            "#00001FErr, it's more likely he\x01",
            "gave that information to\x01",
            ""someone".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10101FSomeone...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10301FHmm, who would that be?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 3)

    label("loc_9A1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B85")
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
            "Heiyue\x01",                 # 0
            "Red Constellation\x01",      # 1
            "A different party\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9AE5"),
        (1, "loc_9AE5"),
        (2, "loc_9B64"),
        (SWITCH_DEFAULT, "loc_9B80"),
    )


    label("loc_9AE5")


    ChrTalk(
        0x101,
        (
            "#11P#00006F(No... there should be\x01",
            "someone else who wants\x01",
            "it more.)\x02\x03",
            "#00001F(That is...)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B5F")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9B5F")

    Jump("loc_9B80")

    label("loc_9B64")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B78")
    OP_2C(0xA3, 0x1)

    label("loc_9B78")

    SetScenarioFlags(0x0, 3)
    Jump("loc_9B80")

    label("loc_9B80")

    Jump("loc_9A1E")

    label("loc_9B85")


    ChrTalk(
        0x101,
        (
            "#11P#00003FRed Constellation, Heiyue, the\x01",
            "Imperial government or even\x01",
            "the Republican government...\x02\x03",
            "All of them seem plausible,\x01",
            "but I can think of an even\x01",
            "more likely group.\x02\x03",
            "#00013FImperial and Republican\x01",
            "terrorists.\x02",
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
            "#6P#00101FWe heard about them from\x01",
            "Princess Klaudia and\x01",
            "Prince Olivert...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00301FTwo terrorist groups aiming\x01",
            "for their respective\x01",
            "countries' heads of state, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10108FIndeed, if they had a map of the\x01",
            "building, they might be able to\x01",
            "aim for its weak points...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#6P#00006FOf course, there's also the\x01",
            "possibility that it's false\x01",
            "information...\x02\x03",
            "#00001FAs I thought. I think we can\x01",
            "say it's likely something will\x01",
            "occur at Orchis Tower tomorrow.\x02\x03",
            "Even securing the tower's\x01",
            "outskirts would be fine. Will\x01",
            "you let us participate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01004FHaha, I see now.\x02\x03",
            "#01002FHow 'bout it, Dudley?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00606F#11P*sigh*... Well, all\x01",
            "right.\x02",
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
            "#00611F#11P...Come to Orchis Tower 1F\x01",
            "tomorrow at exactly noon.\x02\x03",
            "You'll enter the trade\x01",
            "conference venue as reserve\x01",
            "security personnel.\x02",
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

    def lambda_A0E9():
        TurnDirection(0x101, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A0E9)
    Sleep(50)

    def lambda_A0F9():
        TurnDirection(0x104, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_A0F9)
    Sleep(50)

    def lambda_A109():
        TurnDirection(0x103, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_A109)
    Sleep(50)

    def lambda_A119():
        TurnDirection(0x102, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_A119)
    Sleep(50)

    def lambda_A129():
        TurnDirection(0x109, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A129)
    Sleep(50)

    def lambda_A139():
        TurnDirection(0x105, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_A139)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        "#6P#00005FHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00305FWow, the venue itself?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FWow. That's quite\x01",
            "generous.\x02",
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
            "#00603F#11PDon't misunderstand. In the end,\x01",
            "you're just reserve personnel.\x02\x03",
            "Though it was a coincidence, you were\x01",
            "useful in the mayoral assassination\x01",
            "attempt incident. And you have someone\x01",
            "knowledgeable in orbal networks.\x02\x03",
            "#00601FYou're just insurance in case\x01",
            "something goes wrong. Know your place.\x02",
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
        "#6P#10102FWe humbly accept!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00204FAs I thought, this is a\x01",
            "way of hiding one's\x01",
            "embarrassment...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00309FHaha, I wonder when\x01",
            "he'll start fawning over\x01",
            "us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#01111F#5PFawning...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x102, 500)
    Sleep(150)

    ChrTalk(
        0xA,
        (
            "#01110F#5PHey Elie, what does\x01",
            ""fawn" mean?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00109FH-Hmm. It's how everyone\x01",
            "acts when talking with\x01",
            "you, KeA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10309FHehe, at this rate it\x01",
            "might not be too long.\x02",
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
            "#5P#01004FHaha. Looks like you guys\x01",
            "are going to be so busy\x01",
            "tomorrow you'll die.\x02",
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

    # Function_22_91A7 end

    def Function_23_A5DB(): pass

    label("Function_23_A5DB")

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
            "#00008F#11P...Chief sure is late.\x02\x03",
            "#00006FIt's understandable\x01",
            "after what happened,\x01",
            "but...\x02",
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
            "#5P#00106FHe's probably discussing\x01",
            "countermeasures at\x01",
            "Orchis Tower around now.\x02\x03",
            "#00108FIt's also a complex\x01",
            "problem on a political\x01",
            "level...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#11PWald too...\x02\x03",
            "#10301FHe did such a crazy\x01",
            "thing at this difficult\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6P#01106F...Hey everyone.\x02\x03",
            "#01112FSince Chief isn't coming\x01",
            "back, should we call off\x01",
            "the hot pot?\x02",
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
            "#00304F#11P...No, he said to go ahead and\x01",
            "begin if he was late.\x02\x03",
            "#00300FKeddo, you did all that work to\x01",
            "prepare it for us, so we'll go on\x01",
            "eatin' it even if it's just us.\x02",
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
        "#6P#00208FRandy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PSetting aside the hot\x01",
            "pot... Randy, aren't you\x01",
            "pushing yourself?\x02\x03",
            "#00008FIt's especially in times\x01",
            "like these that you've\x01",
            "got to rely on─\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x2)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00302F#11PHaha, of course I'm\x01",
            "countin' on you.\x02\x03",
            "#00303FI said it before too,\x01",
            "but... I severed my ties\x01",
            "with uncle and the others.\x02\x03",
            "I just can't stand what\x01",
            "they've been doing these\x01",
            "days.\x02\x03",
            "#00304FMore importantly, let's\x01",
            "eat our meal and rest\x01",
            "while we can...\x02\x03",
            "#00300F─Preparin' for tomorrow\x01",
            "comes first, right?\x02",
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
            "#6P#10112FT-That's right!\x02\x03",
            "#10100FYou can't fight on an\x01",
            "empty stomach, they say!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00109F*giggle*, your toughness\x01",
            "always helps us out,\x01",
            "Randy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00202F...Indeed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#11PWell, we came across one\x01",
            "hell of a bunch at the\x01",
            "lake today too.\x02\x03",
            "#10302FFinishing our meal and\x01",
            "turning in early might\x01",
            "help us out tomorrow.\x02",
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
            "#00002F#11P─Alright, then. Let's\x01",
            "start on the hot pot.\x02\x03",
            "#00004FKeA prepared it after all,\x01",
            "so there's plenty of meat,\x01",
            "fish and vegetables.\x02\x03",
            "#00000FLet's eat a lot, go to bed\x01",
            "early and... get ready for\x01",
            "tomorrow!\x02",
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
            "#5P#00102FKeA, leave the rest to\x01",
            "us and eat up, ok?\x02",
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
            "#6P#00202FZeit, I'll cook some\x01",
            "meat and fish for you\x01",
            "later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01200F#11PGrrrowl... Woof.\x02",
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

    # Function_23_A5DB end

    def Function_24_B661(): pass

    label("Function_24_B661")

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
            "#5PW-What the heck is\x01",
            "happening outside...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5P...My husband... I\x01",
            "wonder if he's\x01",
            "alright...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x0, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "#12P#01003FAah, everyone, please calm down.\x02\x03",
            "#01002FAccording to a communication I just\x01",
            "received, it appears that the mysterious\x01",
            "armed group has started to withdraw.\x02\x03",
            "Please return to your homes until safety\x01",
            "is confirmed.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BA02():
        TurnDirection(0xE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_BA02)
    Sleep(30)

    def lambda_BA12():
        TurnDirection(0x10, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_BA12)
    Sleep(30)

    def lambda_BA22():
        TurnDirection(0x11, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_BA22)
    Sleep(30)
    WaitChrThread(0xE, 0)
    WaitChrThread(0x10, 0)
    WaitChrThread(0x11, 0)

    ChrTalk(
        0xE,
        "#5PR-Really!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5POh, Aidios! Thank you\x01",
            "for your protection!\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(20000, 1000)

    def lambda_BA8D():
        OP_9A(0xFE, 0x8, 0x4B0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_BA8D)
    WaitChrThread(0xA, 1)

    ChrTalk(
        0xA,
        (
            "#5P#01112F#30WChief... Is it alright\x01",
            "now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#01006FYeah, for now.\x02\x03",
            "#01001FLloyd and the others...\x01",
            "I hope they're safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#01104F#30W─Yeah, they are.\x02\x03",
            "#01121FIf it's Lloyd and the\x01",
            "others, they'll be all\x01",
            "right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#01005FHmm, yeah... You're\x01",
            "right.\x02\x03",
            "#01002FThey've grown up, no\x01",
            "matter what you say.\x02\x03",
            "#01004FMaybe more than that old\x01",
            "Sergei team─\x02",
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
            "#11P#01003FYes, this is the Support\x01",
            "Section─\x02\x03",
            "#01005F...Oh, Dudley, huh. How\x01",
            "is it going over there?\x02\x03",
            "#01001F...What? A jaeger\x01",
            "airship you say...?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xA)
    Sleep(500)

    def lambda_BD52():
        OP_96(0xFE, 0xFFFFFCE0, 0x0, 0xCE4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_BD52)
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0x0, 0x1F4)
    SetChrChipByIndex(0xA, 0x27)
    SetChrSubChip(0xA, 0x0)

    def lambda_BD7F():
        OP_96(0xFE, 0x190, 0x0, 0x1A90, 0xDAC, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_BD7F)
    WaitChrThread(0xA, 1)
    OP_68(1000, 2000, 3000, 3000)

    def lambda_BDAE():
        OP_96(0xFE, 0x514, 0x352, 0x2BC0, 0xDAC, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_BDAE)
    WaitChrThread(0xA, 1)

    def lambda_BDCC():
        OP_96(0xFE, 0x514, 0xFA0, 0x3B60, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_BDCC)
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

    def lambda_BE5B():
        OP_96(0xFE, 0xFFFFFED4, 0x0, 0x11A6C, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_BE5B)
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
            "#01120F#40WAs I thought, no matter what\x01",
            "I do... ...It seems that\x01",
            "this is for the best...\x02",
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
        "#01123F#40W#11P...............\x02",
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
        "#01121F#3621V#40W#11P#20A─It's ok.\x02",
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
            "#3622V#30W#40AI have... made up my\x01",
            "mind.\x02",
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

    # Function_24_B661 end

    def Function_25_C190(): pass

    label("Function_25_C190")

    TalkBegin(0xFF)
    OP_E5(0xA)
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_E5(0x5)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C1AC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C8F7")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "OP_E5(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_C1E5"),
        (1, "loc_C3A1"),
        (2, "loc_C8DB"),
        (3, "loc_C8E3"),
        (SWITCH_DEFAULT, "loc_C8F2"),
    )


    label("loc_C1E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_C1F8")
    OP_2B(0x94, 0xFFFF)
    Jump("loc_C39C")

    label("loc_C1F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_C213")
    OP_2B(0x8E, 0x8F, 0x90, 0x91, 0x92, 0xFFFF)
    Jump("loc_C39C")

    label("loc_C213")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_C276")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Announcement")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Currently there are no\x01",
            "support requests.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_C39C")

    label("loc_C276")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_C291")
    OP_2B(0x8B, 0x8C, 0x88, 0x80, 0x83, 0xFFFF)
    Jump("loc_C39C")

    label("loc_C291")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C2CC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_C2BA")
    OP_2B(0x85, 0x86, 0x87, 0x88, 0x80, 0x83, 0xFFFF)
    Jump("loc_C2C7")

    label("loc_C2BA")

    OP_2B(0x85, 0x86, 0x88, 0x80, 0x83, 0xFFFF)

    label("loc_C2C7")

    Jump("loc_C39C")

    label("loc_C2CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_C2E5")
    OP_2B(0x80, 0x81, 0x82, 0x83, 0xFFFF)
    Jump("loc_C39C")

    label("loc_C2E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_C2F3")
    Jump("loc_C39C")

    label("loc_C2F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_C310")
    OP_2B(0x79, 0x7A, 0x7B, 0x77, 0x71, 0x72, 0xFFFF)
    Jump("loc_C39C")

    label("loc_C310")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_END)), "loc_C32D")
    OP_2B(0x74, 0x75, 0x76, 0x77, 0x71, 0x72, 0xFFFF)
    Jump("loc_C39C")

    label("loc_C32D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C346")
    OP_2B(0x6F, 0x70, 0x71, 0x72, 0xFFFF)
    Jump("loc_C39C")

    label("loc_C346")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_C37A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_END)), "loc_C36A")
    OP_2B(0x6A, 0x6B, 0x6C, 0x6D, 0x67, 0xFFFF)
    Jump("loc_C375")

    label("loc_C36A")

    OP_2B(0x6A, 0x6B, 0x6C, 0x67, 0xFFFF)

    label("loc_C375")

    Jump("loc_C39C")

    label("loc_C37A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 7)), scpexpr(EXPR_END)), "loc_C391")
    OP_2B(0x65, 0x66, 0x67, 0xFFFF)
    Jump("loc_C39C")

    label("loc_C391")

    OP_2B(0x65, 0x66, 0x67, 0x68, 0xFFFF)

    label("loc_C39C")

    Jump("loc_C8F2")

    label("loc_C3A1")

    SetMapFlags(0x40000000)
    OP_E5(0x7)
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C496")
    SetChrName("Announcement")

    AnonymousTalk(
        0xFF,
        (
            "This is Crossbell\x01",
            "Police.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E5(0x4)"), scpexpr(EXPR_END)), "loc_C46E")

    AnonymousTalk(
        0xFF,
        (
            "I will receive your\x01",
            "report.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E5(0xC)
    SetChrName("Announcement")

    AnonymousTalk(
        0xFF,
        (
            "Report processing,\x01",
            "complete. Thank you for\x01",
            "your hard work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C491")

    label("loc_C46E")


    AnonymousTalk(
        0xFF,
        (
            "There no reportable\x01",
            "requests.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C491")

    Jump("loc_C8CD")

    label("loc_C496")

    SetChrName("Receptionist Fran")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C4ED")
    Sound(3062, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            "Yes, this is Crossbell\x01",
            "Poliiice!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C522")

    label("loc_C4ED")

    Sound(3061, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            "Everyone, thank you for\x01",
            "your hard wooork.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C522")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E5(0x4)"), scpexpr(EXPR_END)), "loc_C7BD")
    Sound(3067, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        (
            "Then, I'll receive your\x01",
            "report, okaaay?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E5(0xC)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C723")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_END)),
        (14, "loc_C5A3"),
        (13, "loc_C5F0"),
        (12, "loc_C639"),
        (SWITCH_DEFAULT, "loc_C67E"),
    )


    label("loc_C5A3")

    Sound(3075, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        (
            "1st Class!── Lloyd,\x01",
            "you're too amazing!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C67E")

    label("loc_C5F0")

    Sound(3074, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        (
            "2nd Class!── Lloyd,\x01",
            "you're amazing!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C67E")

    label("loc_C639")

    Sound(3073, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        (
            "3rd Class!── Lloyd, you\x01",
            "did it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C67E")

    label("loc_C67E")

    Sound(3076, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        (
            "I will immediately send\x01",
            "over your special item!\x02",
        )
    )

    CloseMessageWindow()
    Sound(3077, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            "Thank you for your hard\x01",
            "wooork! I hope to be\x01",
            "working with you agaaain.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C7B5")

    label("loc_C723")

    Sound(3078, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        (
            "That's all for your\x01",
            "report, right?\x02",
        )
    )

    CloseMessageWindow()
    Sound(3079, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            "Then, please contact me\x01",
            "again the next time you\x01",
            "complete a requeeest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C7B5")

    SetScenarioFlags(0x0, 6)
    Jump("loc_C8CD")

    label("loc_C7BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_C842")
    Sound(3063, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        (
            "Oh... Didn't you just\x01",
            "report?\x02",
        )
    )

    CloseMessageWindow()
    Sound(3064, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            "Please do it again when\x01",
            "you complete a request.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C8CD")

    label("loc_C842")

    Sound(3065, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        (
            "Oh... It seems you don't\x01",
            "have any requests you\x01",
            "can repooort.\x02",
        )
    )

    CloseMessageWindow()
    Sound(3066, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            "Please, let's work\x01",
            "together agaaain.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C8CD")

    OP_57(0x0)
    OP_E5(0x8)
    ClearMapFlags(0x40000000)
    Jump("loc_C8F2")

    label("loc_C8DB")

    Call(0, 26)
    Jump("loc_C8F2")

    label("loc_C8E3")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C8F2")

    label("loc_C8F2")

    Jump("loc_C1AC")

    label("loc_C8F7")

    OP_E5(0x6)
    OP_C9(0x1, 0x4)
    OP_C9(0x1, 0x100)
    FadeToBright(300, 0)
    OP_0D()
    OP_E5(0xB)
    TalkEnd(0xFF)
    Return()

    # Function_25_C190 end

    def Function_26_C915(): pass

    label("Function_26_C915")

    OP_E5(0x6)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 3)), scpexpr(EXPR_END)), "loc_C937")
    SetScenarioFlags(0x2A, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C937")
    ClearScenarioFlags(0x2A, 0)

    label("loc_C937")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 4)), scpexpr(EXPR_END)), "loc_C954")
    SetScenarioFlags(0x2A, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C954")
    ClearScenarioFlags(0x2A, 1)

    label("loc_C954")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 5)), scpexpr(EXPR_END)), "loc_C971")
    SetScenarioFlags(0x2A, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C971")
    ClearScenarioFlags(0x2A, 2)

    label("loc_C971")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 6)), scpexpr(EXPR_END)), "loc_C98E")
    SetScenarioFlags(0x2A, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C98E")
    ClearScenarioFlags(0x2A, 3)

    label("loc_C98E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 7)), scpexpr(EXPR_END)), "loc_C9AB")
    SetScenarioFlags(0x2A, 4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C9AB")
    ClearScenarioFlags(0x2A, 4)

    label("loc_C9AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 0)), scpexpr(EXPR_END)), "loc_C9C8")
    SetScenarioFlags(0x2A, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C9C8")
    ClearScenarioFlags(0x2A, 5)

    label("loc_C9C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 1)), scpexpr(EXPR_END)), "loc_C9D4")
    SetScenarioFlags(0x2A, 6)

    label("loc_C9D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CA26")
    RunExpression(0x7, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x10, 0x3, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    StopBGM(0x0)
    Jump("loc_CAA1")

    label("loc_CA26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CA78")
    OP_24(0x80)
    RunExpression(0x7, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x10, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1F()
    Sound(128, 1, 50, 0)
    Jump("loc_CAA1")

    label("loc_CA78")

    RunExpression(0x7, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x10, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1F()

    label("loc_CAA1")

    Return()

    # Function_26_C915 end

    SaveToFile()

Try(main)
