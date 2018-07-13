from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c010b.bin",                # FileName
        "c010b",                    # MapName
        "c010b",                    # Location
        0x0004,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\x03',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 4, 0, 4, 0, 5],
    )

    BuildStringList((
        "c010b",                  # 0
        "Gina",                   # 1
        "Old Man Conte",          # 2
        "Abel",                   # 3
        "Mimi",                   # 4
        "Pluna",                  # 5
        "Lenalee",                # 6
        "Haas",                   # 7
        "Sally",                  # 8
        "Policeman",              # 9
        "Policeman",              # 10
        "Koppe",                  # 11
        "KeA",                    # 12
        "Zeit",                   # 13
        "Shirley",                # 14
        "Jaeger Gareth",          # 15
        "車",                     # 16
        "Dummy",                  # 17
        "Policeman",              # 18
        "Patrol Officer Kate",    # 19
        "市民１",                 # 20
        "SE制御",                 # 21
        "Central Square",         # 22
        "West Street",            # 23
        "Governmental District",  # 24
        "Residential Street",     # 25
        "Entertainment District", # 26
        "East Street",            # 27
        "Downtown",               # 28
        "Waterfront Area",        # 29
        "IBC",                    # 30
        "Station Street",         # 31
        "Back Street",            # 32
        "St. Ursula Byroad",      # 33
        "East Crossbell Highway", # 34
        "West Crossbell HIghway", # 35
        "Mainz Mountain Road",    # 36
        "Orchis Tower",           # 37
    ))

    AddCharChip((
        "chr/ch21300.itc",                   # 00
        "chr/ch20002.itc",                   # 01
        "chr/ch20200.itc",                   # 02
        "chr/ch20700.itc",                   # 03
        "chr/ch34600.itc",                   # 04
        "chr/ch22100.itc",                   # 05
        "chr/ch20500.itc",                   # 06
        "chr/ch26000.itc",                   # 07
        "chr/ch30000.itc",                   # 08
        "chr/ch39200.itc",                   # 09
    ))

    DeclNpc(12619,   0,       2160,    90,   261,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(4294961206, 150,     4449,    270,  325,  0x0, 0,   1,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(4294961197, 0,       4294957887, 90,   389,  0x0, 0,   2,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(4294967007, 0,       4294956977, 225,  261,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(850,     0,       17969,   90,   277,  0x0, 0,   6,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(2539,    0,       17870,   270,  277,  0x0, 0,   5,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(14130,   0,       340,     270,  261,  0x0, 0,   7,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(4294961197, 0,       4294957887, 90,   389,  0x0, 0,   4,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(13850,   0,       24000,   180,  385,  0x0, 0,   8,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(10050,   0,       24000,   180,  385,  0x0, 0,   8,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(4294944487, 1299,    4294948467, 180,  389,  0x0, 0,   9,   0,   0,   2,   0,   18,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    236,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 45,  12.449999809265137,    27.34000015258789,     -1.0,                  625.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -1.2450000047683716,   -5.4679999351501465,   0.20000000298023224,   1.0])

    DeclActor(0,       0,       4294965696, 1000,    0,       2500,    0,       0x007C, 0,  46, 0x0000)

    PlaceName(-5.449999809265137, 0.0, -2.7200000286102295, 0x0000, 0x0000, "Central Square")
    PlaceName(-70.54000091552734, 0.0, 1.7300000190734863, 0x0000, 0x0000, "West Street")
    PlaceName(21.290000915527344, 0.0, 85.38999938964844, 0x0000, 0x0000, "Governmental District")
    PlaceName(-130.92999267578125, 0.0, 75.48999786376953, 0x0000, 0x0000, "Residential Street")
    PlaceName(-58.65999984741211, 0.0, 67.56999969482422, 0x0000, 0x0000, "Entertainment District")
    PlaceName(74.98999786376953, 0.0, -25.489999771118164, 0x0000, 0x0000, "East Street")
    PlaceName(110.13999938964844, 0.0, -79.94000244140625, 0x0000, 0x0000, "Downtown")
    PlaceName(102.70999908447266, 0.0, 39.849998474121094, 0x0000, 0x0000, "Waterfront Area")
    PlaceName(76.97000122070312, 0.0, 132.91000366210938, 0x0000, 0x0000, "IBC")
    PlaceName(5.690000057220459, 0.0, -71.02999877929688, 0x0000, 0x0000, "Station Street")
    PlaceName(-40.84000015258789, 0.0, 31.93000030517578, 0x0000, 0x0000, "Back Street")
    PlaceName(2.7200000286102295, 0.0, -101.72000122070312, 0x0000, 0x0000, "St. Ursula Byroad")
    PlaceName(128.4499969482422, 0.0, -11.630000114440918, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-121.02999877929688, 0.0, 0.25, 0x0000, 0x0000, "West Crossbell HIghway")
    PlaceName(-115.08999633789062, 0.0, 99.25, 0x0000, 0x0000, "Mainz Mountain Road")
    PlaceName(15.0, 0.0, 216.75, 0x0000, 0x0000, "Orchis Tower")
    PlaceName(-27.229999542236328, 0.0, -16.579999923706055, 0x0000, 0x0051, "")
    PlaceName(25.989999771118164, 0.0, 9.15999984741211, 0x0000, 0x0054, "")
    PlaceName(-2.9700000286102295, 0.0, -24.5, 0x0000, 0x0057, "")
    PlaceName(-27.969999313354492, 0.0, 12.130000114440918, 0x0000, 0x0053, "")
    PlaceName(-7.670000076293945, 0.0, 35.88999938964844, 0x0000, 0x0053, "")
    PlaceName(-57.91999816894531, 0.0, 7.179999828338623, 0x0000, 0x0053, "")
    PlaceName(-67.56999969482422, 0.0, 27.969999313354492, 0x0000, 0x0053, "")
    PlaceName(-43.810001373291016, 0.0, 59.650001525878906, 0x0000, 0x0052, "")
    PlaceName(-39.11000061035156, 0.0, 46.779998779296875, 0x0000, 0x0053, "")
    PlaceName(-30.440000534057617, 0.0, 38.36000061035156, 0x0000, 0x0053, "")
    PlaceName(-2.2300000190734863, 0.0, 108.6500015258789, 0x0000, 0x0051, "")
    PlaceName(108.6500015258789, 0.0, -25.489999771118164, 0x0000, 0x0052, "")
    PlaceName(91.81999969482422, 0.0, -115.08999633789062, 0x0000, 0x0053, "")
    PlaceName(78.94999694824219, 0.0, -96.7699966430664, 0x0000, 0x0053, "")

    ChipFrameInfo(1712, 0)                                       # 0

    ScpFunction((
        "Function_0_6B0",          # 00, 0
        "Function_1_760",          # 01, 1
        "Function_2_7AD",          # 02, 2
        "Function_3_7D8",          # 03, 3
        "Function_4_802",          # 04, 4
        "Function_5_8E5",          # 05, 5
        "Function_6_96D",          # 06, 6
        "Function_7_9C3",          # 07, 7
        "Function_8_B2F",          # 08, 8
        "Function_9_B81",          # 09, 9
        "Function_10_BC2",         # 0A, 10
        "Function_11_C44",         # 0B, 11
        "Function_12_CAC",         # 0C, 12
        "Function_13_DE1",         # 0D, 13
        "Function_14_E85",         # 0E, 14
        "Function_15_F27",         # 0F, 15
        "Function_16_FD1",         # 10, 16
        "Function_17_10E4",        # 11, 17
        "Function_18_11B0",        # 12, 18
        "Function_19_12F8",        # 13, 19
        "Function_20_2830",        # 14, 20
        "Function_21_2866",        # 15, 21
        "Function_22_28AA",        # 16, 22
        "Function_23_28EE",        # 17, 23
        "Function_24_2932",        # 18, 24
        "Function_25_296F",        # 19, 25
        "Function_26_29B3",        # 1A, 26
        "Function_27_29F7",        # 1B, 27
        "Function_28_2A3B",        # 1C, 28
        "Function_29_2A7F",        # 1D, 29
        "Function_30_2AD0",        # 1E, 30
        "Function_31_2B32",        # 1F, 31
        "Function_32_2BAB",        # 20, 32
        "Function_33_2C2E",        # 21, 33
        "Function_34_2CB1",        # 22, 34
        "Function_35_32CA",        # 23, 35
        "Function_36_34DB",        # 24, 36
        "Function_37_35B4",        # 25, 37
        "Function_38_3608",        # 26, 38
        "Function_39_37F0",        # 27, 39
        "Function_40_39B6",        # 28, 40
        "Function_41_3A4D",        # 29, 41
        "Function_42_3A57",        # 2A, 42
        "Function_43_457B",        # 2B, 43
        "Function_44_474B",        # 2C, 44
        "Function_45_4770",        # 2D, 45
        "Function_46_4858",        # 2E, 46
        "Function_47_4A10",        # 2F, 47
        "Function_48_4A3A",        # 30, 48
        "Function_49_4A64",        # 31, 49
        "Function_50_4A8E",        # 32, 50
    ))


    def Function_0_6B0(): pass

    label("Function_0_6B0")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_6E8"),
        (1, "loc_6F4"),
        (2, "loc_700"),
        (3, "loc_70C"),
        (4, "loc_718"),
        (5, "loc_724"),
        (6, "loc_730"),
        (SWITCH_DEFAULT, "loc_73C"),
    )


    label("loc_6E8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_748")

    label("loc_6F4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_748")

    label("loc_700")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_748")

    label("loc_70C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_748")

    label("loc_718")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_748")

    label("loc_724")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_748")

    label("loc_730")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_748")

    label("loc_73C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_748")

    label("loc_748")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_75F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_748")

    label("loc_75F")

    Return()

    # Function_0_6B0 end

    def Function_1_760(): pass

    label("Function_1_760")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7AC")
    OP_95(0xFE, 11850, 0, -1800, 2000, 0x0)
    OP_95(0xFE, 11850, 0, 39440, 2000, 0x0)
    Sleep(2000)
    SetChrPos(0xFE, 30000, 0, -3010, 270)
    Jump("Function_1_760")

    label("loc_7AC")

    Return()

    # Function_1_760 end

    def Function_2_7AD(): pass

    label("Function_2_7AD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7D7")
    OP_94(0xFE, 0xFFFFA484, 0xFFFFB348, 0xFFFFA722, 0xFFFFB9BA, 0x3E8)
    Sleep(300)
    Jump("Function_2_7AD")

    label("loc_7D7")

    Return()

    # Function_2_7AD end

    def Function_3_7D8(): pass

    label("Function_3_7D8")

    SetMapObjFlags(0x17, 0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_7F2")
    ClearMapObjFlags(0x17, 0x2000000)
    Jump("loc_801")

    label("loc_7F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_801")
    ClearMapObjFlags(0x17, 0x2000000)

    label("loc_801")

    Return()

    # Function_3_7D8 end

    def Function_4_802(): pass

    label("Function_4_802")

    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xF, -4240, 0, -7750, 225)
    SetChrPos(0xB, -4450, 0, -9880, 315)
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_871")
    ClearScenarioFlags(0x22, 0)
    Event(0, 19)
    Jump("loc_8E4")

    label("loc_871")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_885")
    ClearScenarioFlags(0x22, 1)
    Event(0, 34)
    Jump("loc_8E4")

    label("loc_885")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_899")
    ClearScenarioFlags(0x22, 2)
    Event(0, 35)
    Jump("loc_8E4")

    label("loc_899")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_8AD")
    ClearScenarioFlags(0x22, 3)
    Event(0, 38)
    Jump("loc_8E4")

    label("loc_8AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_8C1")
    ClearScenarioFlags(0x22, 4)
    Event(0, 39)
    Jump("loc_8E4")

    label("loc_8C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_8D5")
    ClearScenarioFlags(0x22, 5)
    Event(0, 42)
    Jump("loc_8E4")

    label("loc_8D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_8E4")
    ClearScenarioFlags(0x22, 6)
    Event(0, 43)

    label("loc_8E4")

    Return()

    # Function_4_802 end

    def Function_5_8E5(): pass

    label("Function_5_8E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_8FA")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 4)

    label("loc_8FA")

    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x14, 0x4)
    SetMapObjFlags(0x15, 0x4)
    SetMapObjFrame(0xFF, "black", 0x0, 0x1)
    SetMapObjFrame(0xFF, "nwindow", 0x0, 0x1)
    OP_1B(0x0, 0xFF, 0xFFFF)
    OP_1B(0x1, 0xFF, 0xFFFF)
    OP_1B(0x3, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_96C")
    OP_1B(0x0, 0x0, 0x2F)
    OP_1B(0x1, 0x0, 0x30)
    OP_1B(0x3, 0x0, 0x31)

    label("loc_96C")

    Return()

    # Function_5_8E5 end

    def Function_6_96D(): pass

    label("Function_6_96D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "My, it's already this late.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have to go home quickly\x01",
            "and help mama.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_96D end

    def Function_7_9C3(): pass

    label("Function_7_9C3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA8")

    ChrTalk(
        0xFE,
        (
            "Oh, now that I notice it, hasn't\x01",
            "it grown completely dark?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ho ho, could I've been too absorbed\x01",
            "by the Trade Conference atmosphere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have to go home quickly so to \x01",
            "not make my old woman worry.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B2B")

    label("loc_AA8")


    ChrTalk(
        0xFE,
        (
            "Oh, now that I notice it, hasn't\x01",
            "it grown completely dark?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have to go home quickly so to \x01",
            "not make my old woman worry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B2B")

    TalkEnd(0xFE)
    Return()

    # Function_7_9C3 end

    def Function_8_B2F(): pass

    label("Function_8_B2F")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Well then, sorry to have\x01",
            "made you waiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "So, let's go at once.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_B2F end

    def Function_9_B81(): pass

    label("Function_9_B81")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Yes, let's go quickly. Both\x01",
            "Mimi and I are starving.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_B81 end

    def Function_10_BC2(): pass

    label("Function_10_BC2")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Eating out, eating out, today I'm eating out♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mimi you know, wants to eat the\x01",
            ""eastern cuisine" of East Street.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_BC2 end

    def Function_11_C44(): pass

    label("Function_11_C44")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C59")
    Call(0, 12)
    Jump("loc_CA8")

    label("loc_C59")


    ChrTalk(
        0xFE,
        "Hmm, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(...Judging by her reaction,\x01",
            "she isn't doing it at all.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CA8")

    TalkEnd(0xFE)
    Return()

    # Function_11_C44 end

    def Function_12_CAC(): pass

    label("Function_12_CAC")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xC,
        (
            "By the way, Lenalee, are you\x01",
            "keeping up with your jogging?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Eh, oh, yes...\x01",
            "Well, more or less.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "After thinking that dieting\x01",
            "forcibly is not good, I lately\x01",
            "do it when I feel inclined to...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Eeeh, is that so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "(...Judging by her reaction,\x01",
            "she isn't doing it at all.)\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_12_CAC end

    def Function_13_DE1(): pass

    label("Function_13_DE1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DF6")
    Call(0, 12)
    Jump("loc_E81")

    label("loc_DF6")


    ChrTalk(
        0xFE,
        (
            "E-Even if you say "feel inclined",\x01",
            "you have to properly keep at it, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let's see, then, today I'll\x01",
            "run and then I'll go home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E81")

    TalkEnd(0xFE)
    Return()

    # Function_13_DE1 end

    def Function_14_E85(): pass

    label("Function_14_E85")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Well then, I guess I'll slowly go back home for today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thank goodness today many people passed by\x01",
            "and I was able to hand over a lot of balloons.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_E85 end

    def Function_15_F27(): pass

    label("Function_15_F27")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F3C")
    Call(0, 16)
    Jump("loc_FCD")

    label("loc_F3C")


    ChrTalk(
        0xFE,
        (
            "Until the VIPs are\x01",
            "escorted to Michelam,\x01",
            "this road is blocked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone from the Support Section,\x01",
            "please understand and cooperate too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FCD")

    TalkEnd(0xFE)
    Return()

    # Function_15_F27 end

    def Function_16_FD1(): pass

    label("Function_16_FD1")

    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)
    TurnDirection(0x10, 0x0, 0)

    ChrTalk(
        0x10,
        (
            "The Support Section members\x01",
            "and Detective Dudley...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x0, 500)

    ChrTalk(
        0x11,
        (
            "Until the VIPs finish going to the\x01",
            "theater, the area ahead is sealed.\x01",
            "Do you need to go inside?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00600FNo, we don't.\x01",
            "Continue to guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Roger!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Roger!\x02",
    )

    CloseMessageWindow()
    OP_93(0x10, 0xB4, 0x0)
    OP_93(0x11, 0xB4, 0x0)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    SetScenarioFlags(0x149, 1)
    Return()

    # Function_16_FD1 end

    def Function_17_10E4(): pass

    label("Function_17_10E4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10F9")
    Call(0, 16)
    Jump("loc_11AC")

    label("loc_10F9")


    ChrTalk(
        0xFE,
        (
            "The whole zone from the Entertainment\x01",
            "District to the Waterfront Area is sealed until\x01",
            "the VIPs are finished with the theater.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I won't let pass even an ant through here!\x02",
    )

    CloseMessageWindow()

    label("loc_11AC")

    TalkEnd(0xFE)
    Return()

    # Function_17_10E4 end

    def Function_18_11B0(): pass

    label("Function_18_11B0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12DB")

    ChrTalk(
        0x12,
        "Nyaago.[It's been a while. How have you been?]\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00600FThe Support Section pet cat?\x02\x03",
            "#00603F(*pet, pet*...)\x01",
            "...You have settled in a\x01",
            "toilsome place too, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "Nyaa～～o......㈱[That's right]\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F(Mr. Dudley... He's unexpectedly\x01",
            "good in dealing with cats...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_12F4")

    label("loc_12DB")


    ChrTalk(
        0x12,
        "Nyaon...[I'm tired]\x02",
    )

    CloseMessageWindow()

    label("loc_12F4")

    TalkEnd(0xFE)
    Return()

    # Function_18_11B0 end

    def Function_19_12F8(): pass

    label("Function_19_12F8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02710.itc", 0x1E)
    LoadChrToIndex("chr/ch08200.itc", 0x1F)
    LoadChrToIndex("chr/ch02750.itc", 0x20)
    LoadChrToIndex("apl/ch51200.itc", 0x21)
    OP_68(9400, 1400, -5200, 0)
    MoveCamera(55, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, 15800, 0, -4900, 270)
    SetChrPos(0x102, 16000, 0, -6500, 270)
    SetChrPos(0x104, 16700, 0, -3400, 270)
    SetChrPos(0x109, 18000, 0, -3800, 270)
    SetChrPos(0x105, 18800, 0, -4400, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x14, 0x1E)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    ClearChrFlags(0x14, 0x4)
    SetChrPos(0x14, 17500, 0, -7000, 270)
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x13, 0x1F)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    ClearChrFlags(0x13, 0x4)
    SetChrPos(0x13, 17000, 0, -5200, 270)
    ClearChrFlags(0x18, 0x4)
    ClearChrFlags(0x18, 0x80)
    OP_90(0x18, -12500, -4200, -16400, 225)
    SetChrFlags(0x8, 0x80)

    def lambda_1434():
        OP_97(0x101, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1434)
    Sleep(50)

    def lambda_1451():
        OP_97(0x102, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1451)
    Sleep(50)

    def lambda_146E():
        OP_97(0x104, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_146E)
    Sleep(50)

    def lambda_148B():
        OP_97(0x14, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_148B)
    Sleep(50)

    def lambda_14A8():
        OP_97(0x13, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_14A8)
    Sleep(50)

    def lambda_14C5():
        OP_97(0x109, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_14C5)
    Sleep(50)

    def lambda_14E2():
        OP_97(0x105, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_14E2)
    SetCameraDistance(14700, 3500)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0)
    OP_6F(0x79)
    TurnDirection(0x101, 0x13, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 2)), scpexpr(EXPR_END)), "loc_159D")

    ChrTalk(
        0x101,
        (
            "#6P#00000FNow that I think about it, it's tomorrow\x01",
            "that you're going with Shizuku on the\x01",
            "department store rooftop?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15FF")

    label("loc_159D")


    ChrTalk(
        0x101,
        (
            "#6P#00000FOh, right, it's tomorrow that you're going\x01",
            "with Shizuku on the department rooftop.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15FF")


    def lambda_1604():
        TurnDirection(0x102, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1604)
    Sleep(50)

    def lambda_1614():
        TurnDirection(0x104, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1614)
    Sleep(50)

    def lambda_1624():
        TurnDirection(0x109, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1624)
    Sleep(50)

    def lambda_1634():
        TurnDirection(0x105, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1634)
    Sleep(50)

    def lambda_1644():
        TurnDirection(0x14, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_1644)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x14, 0)
    WaitChrThread(0x14, 0)
    SetChrSubChip(0x14, 0x5)

    ChrTalk(
        0x13,
        (
            "#11P#01109FYes!\x01",
            "Ina-ugura-tion ceremony, was it?\x02\x03",
            "#01110FWe promised to go\x01",
            "see it together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00109F*giggle*, I see.\x02\x03",
            "#00105FOh, but considering her condition, for\x01",
            "Shizuku to "see" the inauguration is...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x102, 500)

    ChrTalk(
        0x13,
        (
            "#5P#01100FYou see, she said that she was fine\x01",
            "even just with feeling the atmosphere.\x02\x03",
            "KeA will describe to her\x01",
            "what atmosphere it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00002FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#00300F#30W...That child is praiseworthy too.\x02",
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x13, 0x104, 500)

    ChrTalk(
        0x13,
        (
            "#12P#01105FHey, hey Randy. \x02\x03",
            "#01112FYou haven't been feeling\x01",
            "well since a bit, eh?\x02",
        )
    )

    CloseMessageWindow()
    OP_68(9400, 1400, -4700, 1000)
    Sleep(300)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(700)

    def lambda_18C6():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_18C6)
    Sleep(50)

    def lambda_18D6():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_18D6)
    Sleep(50)

    def lambda_18E6():
        TurnDirection(0x104, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_18E6)
    Sleep(50)

    def lambda_18F6():
        TurnDirection(0x109, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_18F6)
    Sleep(50)

    def lambda_1906():
        TurnDirection(0x105, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1906)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    Sleep(100)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x1)
    SetChrFlags(0x104, 0x10)
    SetChrFlags(0x104, 0x2)
    SetChrFlags(0x104, 0x20)
    BeginChrThread(0x104, 3, 0, 20)
    Sleep(300)

    ChrTalk(
        0x104,
        "#5P#00309FHa ha, that's not true.\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 3)
    SetChrSubChip(0x104, 0x5)
    Sleep(110)
    SetChrSubChip(0x104, 0x6)
    Sleep(110)
    SetChrSubChip(0x104, 0x7)
    Sound(822, 0, 100, 0)
    OP_63(0x104, 0x12C, 1300, 0x36, 0x39, 0xFA, 0x0)
    Sleep(1300)
    SetChrSubChip(0x104, 0x8)
    Sleep(110)
    SetChrSubChip(0x104, 0x9)
    Sleep(110)
    SetChrSubChip(0x104, 0xA)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x104,
        (
            "#5P#00303F*griiiin*, here, look!\x02\x03",
            "#00302FI'm the same as always cool\x01",
            "and handsome nice guy, no?\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x104)

    ChrTalk(
        0x13,
        "#12P#01111FNais gai?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#11P#10112FSenior, "nice guy" is really\x01",
            "a dead expression...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#11PHu hu, could mere bravado\x01",
            "mean he's feeling well inside?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0xB)
    Sleep(90)
    ClearChrFlags(0x104, 0x10)
    ClearChrFlags(0x104, 0x2)
    ClearChrFlags(0x104, 0x20)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sleep(150)
    TurnDirection(0x104, 0x109, 500)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x104,
        (
            "#5P#00301FDamn!\x01",
            "Don't cut in, juniors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FHa ha...\x02\x03",
            "#00000FStill, Randy, please don't torment\x01",
            "yourself too much over it, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00106FRight, we're here with you\x01",
            "for moments like this...\x02\x03",
            "#00101FDon't think you're going to\x01",
            "settle everything alone, hm?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x13, 500)

    ChrTalk(
        0x104,
        (
            "#5P#00304FHa ha, I know.\x02\x03",
            "#00308F──But still, those guys\x01",
            "are even my relatives.\x02\x03",
            "#00300FI think I'll try to speak\x01",
            "frankly to them, once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00105FIsn't that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00001F...Kind of dangerous?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 3)), scpexpr(EXPR_END)), "loc_1E11")

    ChrTalk(
        0x104,
        (
            "#5P#00304FWell, I'm well familiar with the guy.\x02\x03",
            "#00301FAt any rate, that uncle of mine...\x01",
            "He said he had something to talk 'bout,\x01",
            "but that was the last I've heard of 'im.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FYeah, even when we tried visiting at\x01",
            "noon he seemed to pretend to be out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F2F")

    label("loc_1E11")


    ChrTalk(
        0x104,
        (
            "#5P#00304FWell, I'm well familiar with the guy.\x02\x03",
            "#00301FAt any rate, that uncle of mine...\x01",
            "He said he had something to talk 'bout,\x01",
            "but that was the last I've heard of 'im.\x02\x03",
            "Even if we visited what remains of Revache,\x01",
            "it seems he'd pretend to be out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00001FIs that so...?\x02",
    )

    CloseMessageWindow()

    label("loc_1F2F")


    def lambda_1F34():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1F34)

    def lambda_1F41():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1F41)
    Sleep(50)

    def lambda_1F51():
        OP_93(0x102, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1F51)
    Sleep(50)

    def lambda_1F61():
        OP_93(0x14, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_1F61)
    Sleep(50)

    def lambda_1F71():
        OP_93(0x13, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_1F71)
    Sleep(50)

    def lambda_1F81():
        OP_93(0x109, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1F81)
    Sleep(50)

    def lambda_1F91():
        OP_93(0x105, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1F91)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x14, 0)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    SetCameraDistance(17500, 3000)

    def lambda_1FBF():
        OP_97(0x101, 0xFFFFD508, 0x0, 0xFFFFEC78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1FBF)
    Sleep(50)

    def lambda_1FDC():
        OP_97(0x102, 0xFFFFD508, 0x0, 0xFFFFEC78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1FDC)
    Sleep(50)

    def lambda_1FF9():
        OP_97(0x104, 0xFFFFD508, 0x0, 0xFFFFEC78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1FF9)
    Sleep(50)

    def lambda_2016():
        OP_97(0x14, 0xFFFFD508, 0x0, 0xFFFFEC78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_2016)
    Sleep(50)

    def lambda_2033():
        OP_97(0x13, 0xFFFFD508, 0x0, 0xFFFFEC78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_2033)
    Sleep(50)

    def lambda_2050():
        OP_97(0x109, 0xFFFFD508, 0x0, 0xFFFFEC78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2050)
    Sleep(50)

    def lambda_206D():
        OP_97(0x105, 0xFFFFD508, 0x0, 0xFFFFEC78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_206D)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_69(0x2, 0x0)
    OP_6B(0x18)
    OP_68(-12500, -3000, -16400, 0)
    MoveCamera(33, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(20000, 0)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x13, 0xFF)
    EndChrThread(0x14, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    SetChrPos(0x101, -13100, -4200, -17800, 225)
    SetChrPos(0x104, -13900, -4200, -17000, 225)
    SetChrPos(0x13, -12100, -4200, -16800, 225)
    SetChrPos(0x109, -12900, -4200, -16000, 225)
    SetChrPos(0x102, -11100, -4200, -15800, 225)
    SetChrPos(0x105, -11900, -4200, -15000, 225)
    SetChrPos(0x14, -13900, -4200, -18700, 225)
    BeginChrThread(0x14, 3, 0, 28)
    BeginChrThread(0x18, 3, 0, 24)
    Sleep(50)
    BeginChrThread(0x101, 3, 0, 21)
    Sleep(50)
    BeginChrThread(0x104, 3, 0, 22)
    Sleep(50)
    BeginChrThread(0x13, 3, 0, 23)
    Sleep(50)
    BeginChrThread(0x109, 3, 0, 25)
    Sleep(50)
    BeginChrThread(0x102, 3, 0, 26)
    Sleep(50)
    BeginChrThread(0x105, 3, 0, 27)
    MoveCamera(40, 23, 0, 10000)
    SetCameraDistance(16000, 10000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x104,
        (
            "#00306F#5P*sigh*, he really makes me mad.\x02\x03",
            "#00305FOh, right, the Chief will be\x01",
            "comin' home late tonight, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#11PYeah, it seems that the arrangements for\x01",
            "tomorrow's inauguration are dragging on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#11P*giggle*, then, it could\x01",
            "be nice to end the day\x01",
            "eating out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109F#5PAh, it would be, every now and then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#11PSo, will that restaurant over there do\x01",
            "or should we go to The Old Dragon?\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x101,
        (
            "#6P#00002FYeah, let's put down the baggages\x01",
            "and then let's go with everyo──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x105, 3)
    OP_6B(0xFF)
    OP_6F(0x79)
    SetChrChipByIndex(0x14, 0x20)
    SetChrSubChip(0x14, 0x0)
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(2937, 255, 100, 0)

    ChrTalk(
        0x14,
        "#01201F#40W#11PGrrrrrowl...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x13, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-26700, -7000, -24400, 2000)
    SetCameraDistance(17000, 2000)

    def lambda_24A2():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_24A2)
    Sleep(50)

    def lambda_24B2():
        OP_93(0x104, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_24B2)
    Sleep(50)

    def lambda_24C2():
        OP_93(0x13, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_24C2)
    Sleep(50)

    def lambda_24D2():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_24D2)
    Sleep(50)

    def lambda_24E2():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_24E2)
    Sleep(50)

    def lambda_24F2():
        OP_93(0x105, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_24F2)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)

    def lambda_2517():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_2517)
    OP_6F(0x79)

    def lambda_2532():
        OP_97(0x101, 0xFFFFF63C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2532)
    Sleep(100)

    def lambda_254F():
        OP_97(0x104, 0xFFFFF63C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_254F)
    Sleep(100)

    def lambda_256C():
        OP_97(0x13, 0xFFFFF63C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_256C)
    Sleep(100)

    def lambda_2589():
        OP_97(0x109, 0xFFFFF63C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2589)
    Sleep(100)

    def lambda_25A6():
        OP_97(0x102, 0xFFFFF63C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_25A6)
    Sleep(100)

    def lambda_25C3():
        OP_97(0x105, 0xFFFFF63C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_25C3)
    WaitChrThread(0x104, 0)

    def lambda_25E1():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_25E1)
    WaitChrThread(0x109, 0)

    def lambda_25F2():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_25F2)

    ChrTalk(
        0x101,
        "#11P#00001FZeit?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#11PIs something wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#12P#01105FUhmm, we have\x01",
            "a visitor, he says.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00005FA visitor?\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_93(0x104, 0x13B, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x104,
        "#11P#00311F#40W............\x02",
    )

    CloseMessageWindow()
    Sleep(150)

    def lambda_26B7():
        OP_95(0xFE, -28500, -8200, -22800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_26B7)
    Sleep(500)

    def lambda_26D4():

        label("loc_26D4")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_26D4")

    QueueWorkItem2(0x101, 2, lambda_26D4)
    Sleep(100)

    def lambda_26E9():

        label("loc_26E9")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_26E9")

    QueueWorkItem2(0x109, 2, lambda_26E9)

    def lambda_26FB():

        label("loc_26FB")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_26FB")

    QueueWorkItem2(0x13, 2, lambda_26FB)
    Sleep(50)

    def lambda_2710():

        label("loc_2710")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_2710")

    QueueWorkItem2(0x102, 2, lambda_2710)

    def lambda_2722():

        label("loc_2722")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_2722")

    QueueWorkItem2(0x105, 2, lambda_2722)
    WaitChrThread(0x104, 1)

    def lambda_2738():
        OP_95(0xFE, -28500, -8200, -19800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2738)
    Sleep(100)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    Sleep(400)

    ChrTalk(
        0x101,
        "#11P#00011FRandy?\x02",
    )


    def lambda_2789():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2789)
    WaitChrThread(0x104, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x13, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10301F#11P...Anyway, let's enter.\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    BeginChrThread(0x101, 3, 0, 29)
    Sleep(400)
    BeginChrThread(0x109, 3, 0, 29)
    Sleep(400)
    BeginChrThread(0x13, 3, 0, 29)
    Sleep(400)
    BeginChrThread(0x105, 3, 0, 29)
    Sleep(400)
    BeginChrThread(0x102, 3, 0, 29)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x13, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    SetScenarioFlags(0x22, 1)
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_19_12F8 end

    def Function_20_2830(): pass

    label("Function_20_2830")

    SetChrSubChip(0x104, 0x2)
    Sleep(100)
    SetChrSubChip(0x104, 0x3)
    Sleep(100)
    SetChrSubChip(0x104, 0x4)
    Sleep(100)
    SetChrSubChip(0x104, 0x5)
    Sleep(100)
    SetChrSubChip(0x104, 0x4)
    Sleep(100)
    SetChrSubChip(0x104, 0x3)
    Sleep(100)
    SetChrSubChip(0x104, 0x4)
    Sleep(100)
    SetChrSubChip(0x104, 0x5)
    Return()

    # Function_20_2830 end

    def Function_21_2866(): pass

    label("Function_21_2866")


    def lambda_286B():
        OP_95(0xFE, -20000, -8200, -25100, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_286B)
    WaitChrThread(0xFE, 1)

    def lambda_2889():
        OP_95(0xFE, -23800, -8200, -25100, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2889)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x18, 500)
    Return()

    # Function_21_2866 end

    def Function_22_28AA(): pass

    label("Function_22_28AA")


    def lambda_28AF():
        OP_95(0xFE, -20000, -8200, -23100, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_28AF)
    WaitChrThread(0xFE, 1)

    def lambda_28CD():
        OP_95(0xFE, -23800, -8200, -23700, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_28CD)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x18, 500)
    Return()

    # Function_22_28AA end

    def Function_23_28EE(): pass

    label("Function_23_28EE")


    def lambda_28F3():
        OP_95(0xFE, -20000, -8200, -25100, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_28F3)
    WaitChrThread(0xFE, 1)

    def lambda_2911():
        OP_95(0xFE, -23000, -8200, -25700, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2911)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x18, 500)
    Return()

    # Function_23_28EE end

    def Function_24_2932(): pass

    label("Function_24_2932")


    def lambda_2937():
        OP_95(0xFE, -20000, -8200, -24400, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2937)
    WaitChrThread(0xFE, 1)

    def lambda_2955():
        OP_95(0xFE, -22700, -8200, -24400, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2955)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_24_2932 end

    def Function_25_296F(): pass

    label("Function_25_296F")


    def lambda_2974():
        OP_95(0xFE, -20000, -8200, -23100, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2974)
    WaitChrThread(0xFE, 1)

    def lambda_2992():
        OP_95(0xFE, -22400, -8200, -23100, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2992)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x18, 500)
    Return()

    # Function_25_296F end

    def Function_26_29B3(): pass

    label("Function_26_29B3")


    def lambda_29B8():
        OP_95(0xFE, -20000, -8200, -25100, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_29B8)
    WaitChrThread(0xFE, 1)

    def lambda_29D6():
        OP_95(0xFE, -21600, -8200, -25100, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_29D6)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x18, 500)
    Return()

    # Function_26_29B3 end

    def Function_27_29F7(): pass

    label("Function_27_29F7")


    def lambda_29FC():
        OP_95(0xFE, -20000, -8200, -23100, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_29FC)
    WaitChrThread(0xFE, 1)

    def lambda_2A1A():
        OP_95(0xFE, -21600, -8200, -23700, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2A1A)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x18, 500)
    Return()

    # Function_27_29F7 end

    def Function_28_2A3B(): pass

    label("Function_28_2A3B")


    def lambda_2A40():
        OP_95(0xFE, -20000, -8200, -25100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2A40)
    WaitChrThread(0xFE, 1)

    def lambda_2A5E():
        OP_95(0xFE, -28500, -8200, -26000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2A5E)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_28_2A3B end

    def Function_29_2A7F(): pass

    label("Function_29_2A7F")


    def lambda_2A84():
        OP_95(0xFE, -28500, -8200, -22800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2A84)
    WaitChrThread(0xFE, 1)

    def lambda_2AA2():
        OP_95(0xFE, -28500, -8200, -19800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2AA2)
    Sleep(500)

    def lambda_2ABF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2ABF)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_29_2A7F end

    def Function_30_2AD0(): pass

    label("Function_30_2AD0")


    def lambda_2AD5():
        OP_95(0xFE, -12800, -4200, -16800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2AD5)
    WaitChrThread(0xFE, 1)

    def lambda_2AF3():
        OP_95(0xFE, -1000, 0, -16800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2AF3)
    WaitChrThread(0xFE, 1)

    def lambda_2B11():
        OP_95(0xFE, 2500, 0, -14700, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2B11)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_30_2AD0 end

    def Function_31_2B32(): pass

    label("Function_31_2B32")


    def lambda_2B37():
        OP_95(0xFE, -19800, -4200, -23800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2B37)
    WaitChrThread(0xFE, 1)

    def lambda_2B55():
        OP_95(0xFE, -12800, -4200, -16800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2B55)
    WaitChrThread(0xFE, 1)

    def lambda_2B73():
        OP_95(0xFE, -1000, 0, -16800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2B73)
    WaitChrThread(0xFE, 1)

    def lambda_2B91():
        OP_95(0xFE, 1700, 0, -16800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2B91)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_31_2B32 end

    def Function_32_2BAB(): pass

    label("Function_32_2BAB")

    Sleep(500)

    def lambda_2BB3():
        OP_95(0xFE, -19800, -4200, -23800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2BB3)
    WaitChrThread(0xFE, 1)

    def lambda_2BD1():
        OP_95(0xFE, -12800, -4200, -16800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2BD1)
    WaitChrThread(0xFE, 1)

    def lambda_2BEF():
        OP_95(0xFE, -1000, 0, -16800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2BEF)
    WaitChrThread(0xFE, 1)

    def lambda_2C0D():
        OP_95(0xFE, 900, 0, -16000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2C0D)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_32_2BAB end

    def Function_33_2C2E(): pass

    label("Function_33_2C2E")

    Sleep(800)

    def lambda_2C36():
        OP_95(0xFE, -19800, -4200, -23800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2C36)
    WaitChrThread(0xFE, 1)

    def lambda_2C54():
        OP_95(0xFE, -12800, -4200, -16800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2C54)
    WaitChrThread(0xFE, 1)

    def lambda_2C72():
        OP_95(0xFE, -1000, 0, -16800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2C72)
    WaitChrThread(0xFE, 1)

    def lambda_2C90():
        OP_95(0xFE, 600, 0, -17200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2C90)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_33_2C2E end

    def Function_34_2CB1(): pass

    label("Function_34_2CB1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch03400.itc", 0x1E)
    LoadChrToIndex("chr/ch42900.itc", 0x1F)
    SetChrPos(0x101, -22100, -8200, -23800, 90)
    SetChrPos(0x104, -20600, -8200, -23800, 90)
    SetChrPos(0x105, -23600, -8200, -23800, 90)
    SetChrPos(0x102, -22000, -8200, -20000, 0)
    SetChrPos(0x109, -22000, -8200, -20000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x15, 0x1E)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    ClearChrFlags(0x15, 0x4)
    SetChrPos(0x15, -19800, -4200, -23800, 0)
    SetChrChipByIndex(0x16, 0x1F)
    SetChrSubChip(0x16, 0x0)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 4700, 500, -16800, 270)
    OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0x16, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x17, 0x80)
    OP_78(0x16, 0x17)
    OP_49()
    SetChrPos(0x17, 5800, 0, -16500, 0)
    OP_D5(0x17, 0x0, 0x0, 0x0, 0x0)
    ClearMapObjFlags(0x16, 0x4)
    SetMapObjFlags(0x16, 0x1000)
    OP_74(0x16, 0x1E)
    OP_70(0x16, 0x1)
    OP_68(-16500, -3900, -20500, 0)
    MoveCamera(5, 27, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18000, 0)
    BeginChrThread(0x15, 3, 0, 30)
    BeginChrThread(0x104, 3, 0, 31)
    BeginChrThread(0x101, 3, 0, 32)
    BeginChrThread(0x105, 3, 0, 33)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(3700, 1300, -16800, 12500)
    MoveCamera(35, 27, 0, 12500)
    SetCameraDistance(15000, 12500)
    WaitChrThread(0x105, 3)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00011FThis is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10305FIf I remember correctly, a\x01",
            "bullet proof limousine, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303FHeh, you bought this\x01",
            "stuff immediately, hm?\x02\x03",
            "#00302FBusiness is thrivin', huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#5P#04609FAhaha, thank goodness yes,\x01",
            "we're rolling in mira.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(462, 0, 100, 0)
    OP_71(0x16, 0xF1, 0x10E, 0x0, 0x0)
    OP_79(0x16)
    OP_68(3200, 1200, -16800, 1000)
    ClearChrFlags(0x16, 0x80)

    def lambda_2F89():
        OP_96(0xFE, 0xE74, 0x0, 0xFFFFBE60, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2F89)

    def lambda_2FA3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_2FA3)
    WaitChrThread(0x16, 1)
    TurnDirection(0x16, 0x15, 500)

    ChrTalk(
        0x16,
        "#11PYoung miss, thank you for your hard work.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x16,
        (
            "#11PAnd young master──\x01",
            "It has been a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00300FGareth...long time no see.\x02\x03",
            "#00306FThat aside, really, drop it\x01",
            "with the "young master".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#11P...I think you have heard\x01",
            "about Master Balder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#11PIt is really regrettable...\x01",
            "I am very sorry for your loss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00308F...Yeah.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#5P#04604FNo gloomy stories!\x01",
            "Tonight we go party big time!\x02\x03",
            "#04602FCome on, come on, jump in!\x01",
            "You too guys, quick, quick!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_31AD():
        OP_95(0xFE, 3200, 0, -18400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_31AD)
    WaitChrThread(0x16, 1)
    TurnDirection(0x16, 0x104, 500)

    ChrTalk(
        0x101,
        (
            "#00001FWell...\x01",
            "Then, don't mind if I do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10304FHu hu, sorry to intrude.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(14500, 2000)
    FadeToDark(2000, 0, -1)

    def lambda_323B():
        OP_95(0xFE, 3700, 0, -16800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_323B)
    Sleep(500)

    def lambda_3258():
        OP_95(0xFE, 3700, 0, -16800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3258)
    WaitChrThread(0x104, 1)

    def lambda_3276():
        OP_95(0xFE, 4700, 500, -16800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3276)

    def lambda_3290():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3290)

    def lambda_32A1():
        OP_95(0xFE, 3700, 0, -16800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_32A1)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0x104, 0xFF)
    SetScenarioFlags(0x22, 0)
    NewScene("e0111", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_34_2CB1 end

    def Function_35_32CA(): pass

    label("Function_35_32CA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch30600.itc", 0x1E)
    SoundLoad(835)
    SetChrChipByIndex(0x1A, 0x1E)
    SetChrChipByIndex(0x19, 0x8)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x1A, 0x8000)
    SetChrFlags(0x19, 0x8000)
    ClearChrFlags(0x17, 0x80)
    OP_78(0x17, 0x17)
    OP_49()
    ClearMapObjFlags(0x17, 0x4)
    SetMapObjFlags(0x17, 0x1000)
    SetMapObjFrame(0x17, "chukin", 0x0, 0x1)
    OP_71(0x17, 0x79, 0xB4, 0x0, 0x20)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0xF, -6100, 0, -9410, 0)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrPos(0xB, -5000, 0, -9410, 0)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0x1A, -1200, 0, -2400, 180)
    BeginChrThread(0x1A, 0, 0, 0)
    SetChrPos(0x19, -18700, 0, 3950, 180)
    BeginChrThread(0x19, 0, 0, 36)
    SetChrPos(0x17, 4700, 0, -30500, 90)
    OP_D5(0x17, 0x0, 0x15F90, 0x0, 0x0)
    BeginChrThread(0x17, 0, 0, 37)
    OP_68(-1000, 3500, 11000, 0)
    MoveCamera(40, 6, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(30000, 0)
    OP_68(-1000, 1500, 11000, 10000)
    MoveCamera(23, 6, 0, 10000)
    SetCameraDistance(34500, 10000)
    Sound(835, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2500)
    Sound(457, 0, 70, 0)
    OP_6F(0x79)
    Fade(500)
    OP_68(-25800, -7600, -16800, 0)
    MoveCamera(35, 12, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(23500, 0)
    SetCameraDistance(20500, 4000)
    Sleep(3000)
    StopSound(835, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 4)
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_35_32CA end

    def Function_36_34DB(): pass

    label("Function_36_34DB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_35B3")
    OP_95(0xFE, -15910, 0, 1150, 1000, 0x0)
    OP_95(0xFE, -290, 0, 16770, 1000, 0x0)
    OP_95(0xFE, -300, 800, 24250, 1000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0xD7, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(1000)
    OP_95(0xFE, -290, 0, 16770, 1000, 0x0)
    OP_95(0xFE, -15910, 0, 1150, 1000, 0x0)
    OP_95(0xFE, -18720, 0, 3960, 1000, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1000)
    Jump("Function_36_34DB")

    label("loc_35B3")

    Return()

    # Function_36_34DB end

    def Function_37_35B4(): pass

    label("Function_37_35B4")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 4700, 0, -30500)
    OP_9F(0x1, 4700, 0, -12500)
    OP_9F(0x1, 8580, 0, 4180)
    OP_9F(0x1, 11000, 0, 30000)
    OP_9F(0x1, 11000, 0, 60000)
    OP_9F(0x2, 0xFE, 6000, 0x6)
    Return()

    # Function_37_35B4 end

    def Function_38_3608(): pass

    label("Function_38_3608")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch30600.itc", 0x1E)
    SoundLoad(835)
    SetChrChipByIndex(0x1A, 0x1E)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0x1A, 0x8000)
    SetChrFlags(0x19, 0x8000)
    ClearChrFlags(0x17, 0x80)
    OP_78(0x17, 0x17)
    OP_49()
    ClearMapObjFlags(0x17, 0x4)
    SetMapObjFlags(0x17, 0x1000)
    SetMapObjFrame(0x17, "chukin", 0x0, 0x1)
    OP_71(0x17, 0x79, 0xB4, 0x0, 0x20)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0x1A, -1200, 0, -2400, 180)
    BeginChrThread(0x1A, 0, 0, 0)
    SetChrPos(0xA, -6100, 0, -9400, 90)
    SetChrPos(0xB, -5000, 0, -9400, 270)
    SetChrPos(0x17, 15000, 0, -5000, 270)
    OP_D5(0x17, 0x0, 0x41EB0, 0x0, 0x0)
    OP_68(-1000, 2500, 11000, 0)
    MoveCamera(25, 6, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(34500, 0)
    OP_68(-1000, 1500, 11000, 7000)
    MoveCamera(23, 5, 0, 7000)
    Sound(458, 0, 80, 0)

    def lambda_3771():
        OP_9B(0x1, 0xFE, 0x0, 0x9C40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3771)
    StopSound(835, 1000, 100)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-25800, -7600, -16800, 0)
    MoveCamera(35, 12, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(23500, 0)
    SetCameraDistance(20500, 4000)
    Sleep(3000)
    StopSound(835, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 6)
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_38_3608 end

    def Function_39_37F0(): pass

    label("Function_39_37F0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch23400.itc", 0x1E)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x1B, 0x1E)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x12, 0x4)
    ClearMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x14, 0x4)
    ClearMapObjFlags(0x15, 0x4)
    SetMapObjFrame(0xFF, "white", 0x0, 0x1)
    SetMapObjFrame(0xFF, "lwindow", 0x0, 0x1)
    SetMapObjFrame(0xFF, "black", 0x1, 0x1)
    SetMapObjFrame(0xFF, "nwindow", 0x1, 0x1)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0x1B, 1500, 0, -4700, 270)
    BeginChrThread(0x1B, 1, 0, 40)
    OP_68(-15350, 1800, 5500, 0)
    MoveCamera(10, 5, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(20000, 0)
    OP_68(3000, 1800, -6000, 12000)
    MoveCamera(45, 5, 0, 12000)
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0x1C, 1, 0, 41)
    Sleep(10000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 7)
    NewScene("c012B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_39_37F0 end

    def Function_40_39B6(): pass

    label("Function_40_39B6")

    OP_63(0xFE, 0x0, 1850, 0x26, 0x27, 0xFA, 0x0)

    label("loc_39C8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A4C")
    OP_9B(0x1, 0xFE, 0x28, 0x3E8, 0x7D0, 0x0)

    def lambda_39E7():
        OP_A6(0xFE, 0x1E, 0x1E, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_39E7)
    OP_9B(0x1, 0xFE, 0x37, 0x1F4, 0x3E8, 0x0)
    Sleep(1500)
    OP_9B(0x1, 0xFE, 0xFFD3, 0x5DC, 0x7D0, 0x0)

    def lambda_3A21():
        OP_A6(0xFE, 0x1E, 0x1E, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3A21)
    OP_9B(0x1, 0xFE, 0xFFD3, 0x1F4, 0x3E8, 0x0)
    Sleep(2000)
    Jump("loc_39C8")

    label("loc_3A4C")

    Return()

    # Function_40_39B6 end

    def Function_41_3A4D(): pass

    label("Function_41_3A4D")

    Sleep(3000)
    Sound(1012, 0, 80, 0)
    Return()

    # Function_41_3A4D end

    def Function_42_3A57(): pass

    label("Function_42_3A57")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51425.itc", 0x1E)
    LoadChrToIndex("apl/ch51443.itc", 0x1F)
    LoadChrToIndex("apl/ch51426.itc", 0x20)
    SoundLoad(2916)
    SoundLoad(2760)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    OP_68(-28700, -7200, -22000, 0)
    MoveCamera(0, 13, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(13500, 0)
    SetChrPos(0x101, -22000, -8200, -20000, 0)
    SetChrPos(0x102, -22000, -8200, -20000, 0)
    SetChrPos(0x103, -22000, -8200, -20000, 0)
    SetChrPos(0x109, -22000, -8200, -20000, 0)
    SetChrChipByIndex(0x104, 0x1E)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x104, -28700, -8200, -20000, 180)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x105, 0x20)
    SetChrSubChip(0x105, 0x0)
    SetChrFlags(0x105, 0x10)
    SetChrFlags(0x105, 0x2)
    SetChrFlags(0x105, 0x20)
    SetChrFlags(0x105, 0x40)
    SetChrPos(0x105, -21000, -8200, -22800, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x12, 0x4)
    ClearMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x14, 0x4)
    ClearMapObjFlags(0x15, 0x4)
    SetMapObjFrame(0xFF, "white", 0x0, 0x1)
    SetMapObjFrame(0xFF, "lwindow", 0x0, 0x1)
    SetMapObjFrame(0xFF, "black", 0x1, 0x1)
    SetMapObjFrame(0xFF, "nwindow", 0x1, 0x1)
    SetCameraDistance(15000, 3000)
    FadeToBright(2000, 0)
    Sleep(1000)
    Sound(103, 0, 70, 0)
    ClearMapObjFlags(0xF, 0x10)
    OP_71(0xF, 0x0, 0xA, 0x0, 0x0)
    OP_79(0xF)

    def lambda_3C6F():
        OP_96(0xFE, 0xFFFF8FE4, 0xFFFFDFF8, 0xFFFFA2A4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3C6F)

    def lambda_3C89():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3C89)
    WaitChrThread(0x104, 1)
    Sound(104, 0, 70, 0)
    OP_71(0xF, 0xA, 0x0, 0x0, 0x0)
    OP_79(0xF)
    SetMapObjFlags(0xF, 0x10)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x105,
        "Young Man's Voice",
        "#2916V#30W──Are you going?\x02",
    )

    CloseMessageWindow()
    OP_24(0xB64)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#5P#00308F#2760V#30WYou...?\x02",
    )

    CloseMessageWindow()
    OP_24(0xAC8)
    OP_C9(0x1, 0x80000000)
    VolumeBGM(0x64, 0x64)
    PlayBGM("ed7568", 0)
    OP_68(-22350, -7200, -23350, 2000)
    MoveCamera(31, 13, 0, 2000)
    SetCameraDistance(13000, 2000)
    TurnDirection(0x104, 0x105, 350)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00301F#5P#NMan, why the heck are\x01",
            "you up this late at night?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_3DB5():
        OP_96(0xFE, 0xFFFFA36C, 0xFFFFDFF8, 0xFFFFA2A4, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3DB5)
    Sleep(1000)
    OP_68(-21400, -7200, -22930, 2500)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)
    SetCameraDistance(12000, 40000)

    ChrTalk(
        0x105,
        (
            "#10302F#5PHu hu, I went to hang out\x01",
            "for a bit at my favorite bar.\x02\x03",
            "#10306FWell, my personality is what it is and\x01",
            "I won't be really bothered by this, but...\x02\x03",
            "#10301FDon't you think the others will get angry?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306F...Probably.\x02\x03",
            "#00301FHowever──this is my problem.\x02\x03",
            "Nothing to do with uncle and Shirley.\x02\x03",
            "To say nothing of bein' alright\x01",
            "to involve Lloyd and the others.\x02\x03",
            "#00303FI'm goin' out to... To conclude\x01",
            "things properly myself.\x02\x03",
            "#00300FIt's just like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10308F#5PHmm, well, whatever.\x02\x03",
            "#10306FBoth you and Wald...\x01",
            "Men are just idiots.\x02\x03",
            "#10302FWhy can you only live\x01",
            "being awkward like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FLeave me alone, will you?\x02\x03",
            "#00305F...Anyway, you... I thought\x01",
            "of askin' you since a while.\x02\x03",
            "#00302FSeriously, whose side are you on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#5PHu hu, what're you saying,\x01",
            "I don't understand at all.\x02\x03",
            "#10300FAlthough, I think your \x01",
            "other conjecture is right.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#6P#00303F...I see. I thought I sensed similar vibes...\x02\x03",
            "#00311FTo those of some guys I had to\x01",
            "do with many times in the past...\x02\x03",
            "So it means you pretended to have met\x01",
            "that girl for the first time too, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#5PHu hu, I wonder?\x02\x03",
            "#10302F──As thanks for having kept your silence,\x01",
            "tomorrow's morning I'll pretend to know nothing.\x02\x03",
            "You can go wild to your heart's content.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00304FYeah... I owe you one.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x104, 0x1F)
    SetChrSubChip(0x104, 0x7)
    SetChrFlags(0x104, 0x10)
    SetChrFlags(0x104, 0x2)
    SetChrFlags(0x104, 0x20)
    Sleep(80)
    SetChrSubChip(0x104, 0x0)
    Sleep(500)
    SetCameraDistance(12000, 2000)
    OP_68(-20360, -7200, -22560, 2500)

    def lambda_437B():

        label("loc_437B")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_437B")

    QueueWorkItem2(0x104, 3, lambda_437B)

    def lambda_438D():
        OP_95(0xFE, -20000, -8200, -23900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_438D)
    Sleep(800)
    SetChrSubChip(0x105, 0x1)
    WaitChrThread(0x104, 1)
    EndChrThread(0x104, 0x3)
    SetChrChipByIndex(0x104, 0x1E)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x104, 0x10)
    ClearChrFlags(0x104, 0x2)
    ClearChrFlags(0x104, 0x20)

    def lambda_43CD():
        OP_95(0xFE, -13000, -4200, -17000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_43CD)
    Sleep(500)
    SetChrSubChip(0x105, 0x2)
    Sleep(500)
    OP_6F(0x79)
    OP_68(-20360, -6600, -23560, 2000)
    WaitChrThread(0x104, 1)

    def lambda_4408():
        OP_95(0xFE, 0, 0, -17000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4408)
    Sleep(1000)
    OP_6F(0x79)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x105)
    Sleep(500)

    ChrTalk(
        0x105,
        (
            "#5P#10306F...Well, I guess our battle potential worries\x01",
            "me a little, in case he would fall.\x02\x03",
            "#10308FConsidering the situation...\x01",
            "Should l have Abbas follow him...?\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(12500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    EndChrThread(0x104, 0x1)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x105, 0x10)
    ClearChrFlags(0x105, 0x2)
    ClearChrFlags(0x105, 0x20)
    ClearChrFlags(0x105, 0x40)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(2000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    OP_32(0xFF, 0xFE, 0x0)
    RemoveParty(0x3, 0xFF)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x23, 2)
    NewScene("c0120", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_42_3A57 end

    def Function_43_457B(): pass

    label("Function_43_457B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02750.itc", 0x1E)
    SoundLoad(868)
    SetChrChipByIndex(0x14, 0x1E)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    SetMapObjFrame(0xFF, "bell", 0x0, 0x1)
    ClearMapObjFlags(0x18, 0x4)
    ClearMapObjFlags(0x19, 0x4)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0x14, -28800, -8200, -23050, 180)
    BeginChrThread(0x14, 0, 0, 44)
    OP_68(7000, 7500, 11000, 0)
    MoveCamera(35, -5, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(34500, 0)
    OP_68(5000, 2500, 11000, 7000)
    MoveCamera(30, 5, 0, 7000)
    Sound(868, 2, 20, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-28700, -6900, -21200, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(18000, 0)
    MoveCamera(40, 20, 0, 4000)
    SetCameraDistance(15000, 4000)
    StopSound(868, 1000, 20)
    StopBGM(0x1388)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7560", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x230), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetCameraDistance(14000, 3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x23, 0)
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_43_457B end

    def Function_44_474B(): pass

    label("Function_44_474B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_476F")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    OP_A1(0xFE, 0x5DC, 0x3, 0x3, 0x2, 0x1)
    Jump("Function_44_474B")

    label("loc_476F")

    Return()

    # Function_44_474B end

    def Function_45_4770(): pass

    label("Function_45_4770")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4784")
    Call(0, 16)
    Jump("loc_4841")

    label("loc_4784")

    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)
    TurnDirection(0x10, 0x0, 0)
    TurnDirection(0x11, 0x0, 0)

    ChrTalk(
        0x10,
        (
            "Until the VIPs are\x01",
            "escorted to Michelam,\x01",
            "this road is blocked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Everyone from the Support Section,\x01",
            "please understand and cooperate too.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10, 0xB4, 0x0)
    OP_93(0x11, 0xB4, 0x0)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)

    label("loc_4841")

    Sleep(50)
    SetChrPos(0x0, 11850, 0, 22430, 180)
    EventEnd(0x4)
    Return()

    # Function_45_4770 end

    def Function_46_4858(): pass

    label("Function_46_4858")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "         The "Crossbell's Bell"\x01",
            "A giant bell excavated in the\x01",
            "autonomous state Crossbell in S1185.\x01",
            "From the condition of the unearthed\x01",
            "remains, it is thought to be from the \x01",
            "Middle Ages period.\x01",
            "Made by multiple metals, when\x01",
            "hit it rings of a pleasant low tone.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It is surmised it was built by an \x01",
            "influential person of those times, but\x01",
            "it is still debated for what it was used.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_46_4858 end

    def Function_47_4A10(): pass

    label("Function_47_4A10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A39")
    EventBegin(0x1)
    Call(0, 50)
    Sleep(50)
    SetChrPos(0x0, 4240, 0, -20650, 0)
    EventEnd(0x4)

    label("loc_4A39")

    Return()

    # Function_47_4A10 end

    def Function_48_4A3A(): pass

    label("Function_48_4A3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A63")
    EventBegin(0x1)
    Call(0, 50)
    Sleep(50)
    SetChrPos(0x0, 16840, 0, -3910, 270)
    EventEnd(0x4)

    label("loc_4A63")

    Return()

    # Function_48_4A3A end

    def Function_49_4A64(): pass

    label("Function_49_4A64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A8D")
    EventBegin(0x1)
    Call(0, 50)
    Sleep(50)
    SetChrPos(0x0, -13380, 0, 14530, 135)
    EventEnd(0x4)

    label("loc_4A8D")

    Return()

    # Function_49_4A64 end

    def Function_50_4A8E(): pass

    label("Function_50_4A8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B2E")

    ChrTalk(
        0x10A,
        (
            "#00603FThe Geofront B-Division entrance\x01",
            "is in Residential Street.\x02\x03",
            "#00600FLet's go there directly on the double.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, roger.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4BA4")

    label("loc_4B2E")


    ChrTalk(
        0x10A,
        (
            "#00603FThe Geofront B-Division entrance\x01",
            "is in Residential Street.\x02\x03",
            "#00600FLet's go there directly on the double.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BA4")

    Return()

    # Function_50_4A8E end

    SaveToFile()

Try(main)
