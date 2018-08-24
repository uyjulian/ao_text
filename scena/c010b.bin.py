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
        "Function_7_9C0",          # 07, 7
        "Function_8_B2F",          # 08, 8
        "Function_9_B83",          # 09, 9
        "Function_10_BBA",         # 0A, 10
        "Function_11_C3D",         # 0B, 11
        "Function_12_CA5",         # 0C, 12
        "Function_13_DCC",         # 0D, 13
        "Function_14_E61",         # 0E, 14
        "Function_15_F07",         # 0F, 15
        "Function_16_FA3",         # 10, 16
        "Function_17_10BE",        # 11, 17
        "Function_18_118E",        # 12, 18
        "Function_19_12DE",        # 13, 19
        "Function_20_2712",        # 14, 20
        "Function_21_2748",        # 15, 21
        "Function_22_278C",        # 16, 22
        "Function_23_27D0",        # 17, 23
        "Function_24_2814",        # 18, 24
        "Function_25_2851",        # 19, 25
        "Function_26_2895",        # 1A, 26
        "Function_27_28D9",        # 1B, 27
        "Function_28_291D",        # 1C, 28
        "Function_29_2961",        # 1D, 29
        "Function_30_29B2",        # 1E, 30
        "Function_31_2A14",        # 1F, 31
        "Function_32_2A8D",        # 20, 32
        "Function_33_2B10",        # 21, 33
        "Function_34_2B93",        # 22, 34
        "Function_35_3184",        # 23, 35
        "Function_36_3395",        # 24, 36
        "Function_37_346E",        # 25, 37
        "Function_38_34C2",        # 26, 38
        "Function_39_36AA",        # 27, 39
        "Function_40_3870",        # 28, 40
        "Function_41_3907",        # 29, 41
        "Function_42_3911",        # 2A, 42
        "Function_43_440B",        # 2B, 43
        "Function_44_45DB",        # 2C, 44
        "Function_45_4600",        # 2D, 45
        "Function_46_46DA",        # 2E, 46
        "Function_47_486F",        # 2F, 47
        "Function_48_4899",        # 30, 48
        "Function_49_48C3",        # 31, 49
        "Function_50_48ED",        # 32, 50
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
        (
            "My, it's already this\x01",
            "late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have to hurry home and\x01",
            "help my mom.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_96D end

    def Function_7_9C0(): pass

    label("Function_7_9C0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA8")

    ChrTalk(
        0xFE,
        (
            "Oh, wouldn't you know it.\x01",
            "It's grown completely\x01",
            "dark, hasn't it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hoho. Could I have been\x01",
            "too absorbed by the trade\x01",
            "conference's atmosphere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I must hurry home so as\x01",
            "not to make my old woman\x01",
            "worry.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B2B")

    label("loc_AA8")


    ChrTalk(
        0xFE,
        (
            "Oh, wouldn't you know it.\x01",
            "It's grown completely\x01",
            "dark, hasn't it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I must hurry home so as\x01",
            "not to make my old woman\x01",
            "worry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B2B")

    TalkEnd(0xFE)
    Return()

    # Function_7_9C0 end

    def Function_8_B2F(): pass

    label("Function_8_B2F")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Well then, sorry to have\x01",
            "kept you waiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Then, let's go at once.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_B2F end

    def Function_9_B83(): pass

    label("Function_9_B83")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Yes, let's hurry. Mimi\x01",
            "and I are starving.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_B83 end

    def Function_10_BBA(): pass

    label("Function_10_BBA")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Eating out, eating out,\x01",
            "today I'm eating out♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mimi, you know, wants to\x01",
            "eat the "eastern\x01",
            "cuisine" of East Street.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_BBA end

    def Function_11_C3D(): pass

    label("Function_11_C3D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C52")
    Call(0, 12)
    Jump("loc_CA1")

    label("loc_C52")


    ChrTalk(
        0xFE,
        "Hmm, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(...Judging by her\x01",
            "reaction, she isn't\x01",
            "doing it at all.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CA1")

    TalkEnd(0xFE)
    Return()

    # Function_11_C3D end

    def Function_12_CA5(): pass

    label("Function_12_CA5")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xC,
        (
            "By the way, Lenalee, are\x01",
            "you keeping up with your\x01",
            "jogging?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Eh, oh, yes... Well,\x01",
            "more or less.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I think forced dieting\x01",
            "isn't good, so lately I do\x01",
            "it when I feel like it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Hmm. Is that right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "(...Judging by her\x01",
            "reaction, she isn't\x01",
            "doing it at all.)\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_12_CA5 end

    def Function_13_DCC(): pass

    label("Function_13_DCC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DE1")
    Call(0, 12)
    Jump("loc_E5D")

    label("loc_DE1")


    ChrTalk(
        0xFE,
        (
            "E-Even if you say "feel\x01",
            "inclined", you have to\x01",
            "keep at it, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let's see, then today\x01",
            "I'll run and then go\x01",
            "home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E5D")

    TalkEnd(0xFE)
    Return()

    # Function_13_DCC end

    def Function_14_E61(): pass

    label("Function_14_E61")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Well then, I guess I'll\x01",
            "make my way back home\x01",
            "for the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thank goodness. Many people\x01",
            "passed by today and I was able\x01",
            "to hand out a lot of balloons.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_E61 end

    def Function_15_F07(): pass

    label("Function_15_F07")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F1C")
    Call(0, 16)
    Jump("loc_F9F")

    label("loc_F1C")


    ChrTalk(
        0xFE,
        (
            "This road is closed until\x01",
            "the heads of state are\x01",
            "escorted to Michelam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Support Section, please\x01",
            "understand and\x01",
            "cooperate.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F9F")

    TalkEnd(0xFE)
    Return()

    # Function_15_F07 end

    def Function_16_FA3(): pass

    label("Function_16_FA3")

    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)
    TurnDirection(0x10, 0x0, 0)

    ChrTalk(
        0x10,
        (
            "The Support Section and\x01",
            "Detective Dudley...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x0, 500)

    ChrTalk(
        0x11,
        (
            "This area is sealed off until the\x01",
            "heads of state are finished at\x01",
            "the theater. Do you want to pass?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00600FNo, we're all right.\x01",
            "Continue to be vigilant.\x02",
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

    # Function_16_FA3 end

    def Function_17_10BE(): pass

    label("Function_17_10BE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10D3")
    Call(0, 16)
    Jump("loc_118A")

    label("loc_10D3")


    ChrTalk(
        0xFE,
        (
            "The whole zone from Entertainment District\x01",
            "to Waterfront Area is sealed off until the\x01",
            "heads of state are finished at the theater.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I won't let even an ant\x01",
            "pass through here!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_118A")

    TalkEnd(0xFE)
    Return()

    # Function_17_10BE end

    def Function_18_118E(): pass

    label("Function_18_118E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12C0")

    ChrTalk(
        0x12,
        (
            "Nyaago. [It's been a\x01",
            "while. How have you\x01",
            "been?]\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00600FThe Support Section pet\x01",
            "cat, huh.\x02\x03",
            "#00603F(*pet, pet*...) ...You've\x01",
            "picked a tough place to\x01",
            "be too, haven't you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Nyaa~~o......㈱ [That's\x01",
            "right]\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F(Dudley... He's\x01",
            "unexpectedly good at\x01",
            "dealing with cats...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_12DA")

    label("loc_12C0")


    ChrTalk(
        0x12,
        "Nyaon... [I'm tired]\x02",
    )

    CloseMessageWindow()

    label("loc_12DA")

    TalkEnd(0xFE)
    Return()

    # Function_18_118E end

    def Function_19_12DE(): pass

    label("Function_19_12DE")

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

    def lambda_141A():
        OP_97(0x101, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_141A)
    Sleep(50)

    def lambda_1437():
        OP_97(0x102, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1437)
    Sleep(50)

    def lambda_1454():
        OP_97(0x104, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1454)
    Sleep(50)

    def lambda_1471():
        OP_97(0x14, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_1471)
    Sleep(50)

    def lambda_148E():
        OP_97(0x13, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_148E)
    Sleep(50)

    def lambda_14AB():
        OP_97(0x109, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_14AB)
    Sleep(50)

    def lambda_14C8():
        OP_97(0x105, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_14C8)
    SetCameraDistance(14700, 3500)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0)
    OP_6F(0x79)
    TurnDirection(0x101, 0x13, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 2)), scpexpr(EXPR_END)), "loc_156E")

    ChrTalk(
        0x101,
        (
            "#6P#00000FOh yeah, you're going to the\x01",
            "department store rooftop with\x01",
            "Shizuku tomorrow, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C6")

    label("loc_156E")


    ChrTalk(
        0x101,
        (
            "#6P#00000FOh, right, you're going with\x01",
            "Shizuku to the department\x01",
            "rooftop tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15C6")


    def lambda_15CB():
        TurnDirection(0x102, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_15CB)
    Sleep(50)

    def lambda_15DB():
        TurnDirection(0x104, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_15DB)
    Sleep(50)

    def lambda_15EB():
        TurnDirection(0x109, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_15EB)
    Sleep(50)

    def lambda_15FB():
        TurnDirection(0x105, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_15FB)
    Sleep(50)

    def lambda_160B():
        TurnDirection(0x14, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_160B)
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
            "#11P#01109FYes! un-veil-ing\x01",
            "ceremony, was it?\x02\x03",
            "#01110FWe promised to see it\x01",
            "together!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00109FHaha, is that right.\x02\x03",
            "#00105FBut for Shizuku,\x01",
            ""seeing" the unveiling\x01",
            "ceremony is a little...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x102, 500)

    ChrTalk(
        0x13,
        (
            "#5P#01100FUmm, she said she was\x01",
            "fine with just feeling\x01",
            "the atmosphere, y'know?\x02\x03",
            "KeA will explain to her\x01",
            "what it's like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00002FOh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#00300F#30WThat girl's brave, too.\x02",
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x13, 0x104, 500)

    ChrTalk(
        0x13,
        (
            "#12P#01105FHey Randy.\x02\x03",
            "#01112FYou're looking down.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(9400, 1400, -4700, 1000)
    Sleep(300)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(700)

    def lambda_1840():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1840)
    Sleep(50)

    def lambda_1850():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1850)
    Sleep(50)

    def lambda_1860():
        TurnDirection(0x104, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1860)
    Sleep(50)

    def lambda_1870():
        TurnDirection(0x109, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1870)
    Sleep(50)

    def lambda_1880():
        TurnDirection(0x105, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1880)
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
        "#5P#00309FHaha, that's not true.\x02",
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
            "#5P#00303FPresto! Here look!\x02\x03",
            "#00302FI'm the same cool,\x01",
            "handsome, nice guy as\x01",
            "usual, right?\x02",
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
            "#11P#10112FRandy, nobody says "nice\x01",
            "guy" anymore...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#11PHaha. Does pretending\x01",
            "that you're fine mean\x01",
            "you actually are?\x02",
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
            "#5P#00301FHey! Don't butt in,\x01",
            "guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FHaha...\x02\x03",
            "#00000FBut Randy, don't think\x01",
            "too hard about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00106FThat's right. We're here\x01",
            "for you in times like\x01",
            "these.\x02\x03",
            "#00101FYou're not thinking of\x01",
            "doing anything by\x01",
            "yourself, are you?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x13, 500)

    ChrTalk(
        0x104,
        (
            "#5P#00304FHaha, I know.\x02\x03",
            "#00308F─It's just, those guys\x01",
            "are my family, more or\x01",
            "less.\x02\x03",
            "#00300FI'm thinking of giving\x01",
            "it to them straight.\x02",
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
        "#12P#00001F...kind of dangerous?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 3)), scpexpr(EXPR_END)), "loc_1D4C")

    ChrTalk(
        0x104,
        (
            "#5P#00304FI'm well aware of that.\x02\x03",
            "#00301FThat uncle of mine though. He said\x01",
            "he had somethin' to say to me, but\x01",
            "I haven't heard from him since.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FEven if I visited the old\x01",
            "Revache building, he'd\x01",
            "pretend he's not there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E51")

    label("loc_1D4C")


    ChrTalk(
        0x104,
        (
            "#5P#00304FI'm well aware of that.\x02\x03",
            "#00301FThat uncle of mine though. He said\x01",
            "he had somethin' to say to me, but\x01",
            "I haven't heard from him since.\x02\x03",
            "Even if I visited the old Revache\x01",
            "building, he'd pretend he wasn't\x01",
            "there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00001FSo that's how it is.\x02",
    )

    CloseMessageWindow()

    label("loc_1E51")


    def lambda_1E56():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1E56)

    def lambda_1E63():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1E63)
    Sleep(50)

    def lambda_1E73():
        OP_93(0x102, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1E73)
    Sleep(50)

    def lambda_1E83():
        OP_93(0x14, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_1E83)
    Sleep(50)

    def lambda_1E93():
        OP_93(0x13, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_1E93)
    Sleep(50)

    def lambda_1EA3():
        OP_93(0x109, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1EA3)
    Sleep(50)

    def lambda_1EB3():
        OP_93(0x105, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1EB3)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x14, 0)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    SetCameraDistance(17500, 3000)

    def lambda_1EE1():
        OP_97(0x101, 0xFFFFD508, 0x0, 0xFFFFEC78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1EE1)
    Sleep(50)

    def lambda_1EFE():
        OP_97(0x102, 0xFFFFD508, 0x0, 0xFFFFEC78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1EFE)
    Sleep(50)

    def lambda_1F1B():
        OP_97(0x104, 0xFFFFD508, 0x0, 0xFFFFEC78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1F1B)
    Sleep(50)

    def lambda_1F38():
        OP_97(0x14, 0xFFFFD508, 0x0, 0xFFFFEC78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_1F38)
    Sleep(50)

    def lambda_1F55():
        OP_97(0x13, 0xFFFFD508, 0x0, 0xFFFFEC78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_1F55)
    Sleep(50)

    def lambda_1F72():
        OP_97(0x109, 0xFFFFD508, 0x0, 0xFFFFEC78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1F72)
    Sleep(50)

    def lambda_1F8F():
        OP_97(0x105, 0xFFFFD508, 0x0, 0xFFFFEC78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1F8F)
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
            "#00306F#5P*sigh*, man, I'm hungry.\x02\x03",
            "#00305FOh yeah, chief 'll be\x01",
            "late tonight, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#11PYeah. Looks like security\x01",
            "planning for tomorrow's unveiling\x01",
            "ceremony has gone over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#11PHaha, then maybe we\x01",
            "should end the day by\x01",
            "eating out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F#5POh, that's nice every\x01",
            "now and then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#11PSo, are we going to the\x01",
            "restaurant over there,\x01",
            "or to The Old Dragon?\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x101,
        (
            "#6P#00002FYeah, let's drop off our\x01",
            "stuff and head to─\x02",
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
        "#01201F#40W#11PGrrrrr...\x02",
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

    def lambda_2389():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2389)
    Sleep(50)

    def lambda_2399():
        OP_93(0x104, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2399)
    Sleep(50)

    def lambda_23A9():
        OP_93(0x13, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_23A9)
    Sleep(50)

    def lambda_23B9():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_23B9)
    Sleep(50)

    def lambda_23C9():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_23C9)
    Sleep(50)

    def lambda_23D9():
        OP_93(0x105, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_23D9)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)

    def lambda_23FE():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_23FE)
    OP_6F(0x79)

    def lambda_2419():
        OP_97(0x101, 0xFFFFF63C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2419)
    Sleep(100)

    def lambda_2436():
        OP_97(0x104, 0xFFFFF63C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2436)
    Sleep(100)

    def lambda_2453():
        OP_97(0x13, 0xFFFFF63C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_2453)
    Sleep(100)

    def lambda_2470():
        OP_97(0x109, 0xFFFFF63C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2470)
    Sleep(100)

    def lambda_248D():
        OP_97(0x102, 0xFFFFF63C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_248D)
    Sleep(100)

    def lambda_24AA():
        OP_97(0x105, 0xFFFFF63C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_24AA)
    WaitChrThread(0x104, 0)

    def lambda_24C8():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_24C8)
    WaitChrThread(0x109, 0)

    def lambda_24D9():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_24D9)

    ChrTalk(
        0x101,
        "#11P#00001FZeit?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#11PSomething wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#12P#01105FHmm? He says we have a\x01",
            "visitor.\x02",
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

    def lambda_2599():
        OP_95(0xFE, -28500, -8200, -22800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2599)
    Sleep(500)

    def lambda_25B6():

        label("loc_25B6")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_25B6")

    QueueWorkItem2(0x101, 2, lambda_25B6)
    Sleep(100)

    def lambda_25CB():

        label("loc_25CB")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_25CB")

    QueueWorkItem2(0x109, 2, lambda_25CB)

    def lambda_25DD():

        label("loc_25DD")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_25DD")

    QueueWorkItem2(0x13, 2, lambda_25DD)
    Sleep(50)

    def lambda_25F2():

        label("loc_25F2")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_25F2")

    QueueWorkItem2(0x102, 2, lambda_25F2)

    def lambda_2604():

        label("loc_2604")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_2604")

    QueueWorkItem2(0x105, 2, lambda_2604)
    WaitChrThread(0x104, 1)

    def lambda_261A():
        OP_95(0xFE, -28500, -8200, -19800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_261A)
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


    def lambda_266B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_266B)
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

    # Function_19_12DE end

    def Function_20_2712(): pass

    label("Function_20_2712")

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

    # Function_20_2712 end

    def Function_21_2748(): pass

    label("Function_21_2748")


    def lambda_274D():
        OP_95(0xFE, -20000, -8200, -25100, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_274D)
    WaitChrThread(0xFE, 1)

    def lambda_276B():
        OP_95(0xFE, -23800, -8200, -25100, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_276B)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x18, 500)
    Return()

    # Function_21_2748 end

    def Function_22_278C(): pass

    label("Function_22_278C")


    def lambda_2791():
        OP_95(0xFE, -20000, -8200, -23100, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2791)
    WaitChrThread(0xFE, 1)

    def lambda_27AF():
        OP_95(0xFE, -23800, -8200, -23700, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_27AF)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x18, 500)
    Return()

    # Function_22_278C end

    def Function_23_27D0(): pass

    label("Function_23_27D0")


    def lambda_27D5():
        OP_95(0xFE, -20000, -8200, -25100, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_27D5)
    WaitChrThread(0xFE, 1)

    def lambda_27F3():
        OP_95(0xFE, -23000, -8200, -25700, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_27F3)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x18, 500)
    Return()

    # Function_23_27D0 end

    def Function_24_2814(): pass

    label("Function_24_2814")


    def lambda_2819():
        OP_95(0xFE, -20000, -8200, -24400, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2819)
    WaitChrThread(0xFE, 1)

    def lambda_2837():
        OP_95(0xFE, -22700, -8200, -24400, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2837)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_24_2814 end

    def Function_25_2851(): pass

    label("Function_25_2851")


    def lambda_2856():
        OP_95(0xFE, -20000, -8200, -23100, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2856)
    WaitChrThread(0xFE, 1)

    def lambda_2874():
        OP_95(0xFE, -22400, -8200, -23100, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2874)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x18, 500)
    Return()

    # Function_25_2851 end

    def Function_26_2895(): pass

    label("Function_26_2895")


    def lambda_289A():
        OP_95(0xFE, -20000, -8200, -25100, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_289A)
    WaitChrThread(0xFE, 1)

    def lambda_28B8():
        OP_95(0xFE, -21600, -8200, -25100, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_28B8)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x18, 500)
    Return()

    # Function_26_2895 end

    def Function_27_28D9(): pass

    label("Function_27_28D9")


    def lambda_28DE():
        OP_95(0xFE, -20000, -8200, -23100, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_28DE)
    WaitChrThread(0xFE, 1)

    def lambda_28FC():
        OP_95(0xFE, -21600, -8200, -23700, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_28FC)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x18, 500)
    Return()

    # Function_27_28D9 end

    def Function_28_291D(): pass

    label("Function_28_291D")


    def lambda_2922():
        OP_95(0xFE, -20000, -8200, -25100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2922)
    WaitChrThread(0xFE, 1)

    def lambda_2940():
        OP_95(0xFE, -28500, -8200, -26000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2940)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_28_291D end

    def Function_29_2961(): pass

    label("Function_29_2961")


    def lambda_2966():
        OP_95(0xFE, -28500, -8200, -22800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2966)
    WaitChrThread(0xFE, 1)

    def lambda_2984():
        OP_95(0xFE, -28500, -8200, -19800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2984)
    Sleep(500)

    def lambda_29A1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_29A1)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_29_2961 end

    def Function_30_29B2(): pass

    label("Function_30_29B2")


    def lambda_29B7():
        OP_95(0xFE, -12800, -4200, -16800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_29B7)
    WaitChrThread(0xFE, 1)

    def lambda_29D5():
        OP_95(0xFE, -1000, 0, -16800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_29D5)
    WaitChrThread(0xFE, 1)

    def lambda_29F3():
        OP_95(0xFE, 2500, 0, -14700, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_29F3)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_30_29B2 end

    def Function_31_2A14(): pass

    label("Function_31_2A14")


    def lambda_2A19():
        OP_95(0xFE, -19800, -4200, -23800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2A19)
    WaitChrThread(0xFE, 1)

    def lambda_2A37():
        OP_95(0xFE, -12800, -4200, -16800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2A37)
    WaitChrThread(0xFE, 1)

    def lambda_2A55():
        OP_95(0xFE, -1000, 0, -16800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2A55)
    WaitChrThread(0xFE, 1)

    def lambda_2A73():
        OP_95(0xFE, 1700, 0, -16800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2A73)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_31_2A14 end

    def Function_32_2A8D(): pass

    label("Function_32_2A8D")

    Sleep(500)

    def lambda_2A95():
        OP_95(0xFE, -19800, -4200, -23800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2A95)
    WaitChrThread(0xFE, 1)

    def lambda_2AB3():
        OP_95(0xFE, -12800, -4200, -16800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2AB3)
    WaitChrThread(0xFE, 1)

    def lambda_2AD1():
        OP_95(0xFE, -1000, 0, -16800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2AD1)
    WaitChrThread(0xFE, 1)

    def lambda_2AEF():
        OP_95(0xFE, 900, 0, -16000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2AEF)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_32_2A8D end

    def Function_33_2B10(): pass

    label("Function_33_2B10")

    Sleep(800)

    def lambda_2B18():
        OP_95(0xFE, -19800, -4200, -23800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2B18)
    WaitChrThread(0xFE, 1)

    def lambda_2B36():
        OP_95(0xFE, -12800, -4200, -16800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2B36)
    WaitChrThread(0xFE, 1)

    def lambda_2B54():
        OP_95(0xFE, -1000, 0, -16800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2B54)
    WaitChrThread(0xFE, 1)

    def lambda_2B72():
        OP_95(0xFE, 600, 0, -17200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2B72)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_33_2B10 end

    def Function_34_2B93(): pass

    label("Function_34_2B93")

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
            "#6P#10305FA Reinford bulletproof\x01",
            "limousine?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303FHmph, bought this\x01",
            "without a second\x01",
            "thought, eh?\x02\x03",
            "#00302FBusiness must be good,\x01",
            "eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#5P#04609FAhaha. Fortunately,\x01",
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

    def lambda_2E50():
        OP_96(0xFE, 0xE74, 0x0, 0xFFFFBE60, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2E50)

    def lambda_2E6A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_2E6A)
    WaitChrThread(0x16, 1)
    TurnDirection(0x16, 0x15, 500)

    ChrTalk(
        0x16,
        "#11PLady Shirley, good work.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x16,
        (
            "#11PAnd young master... It\x01",
            "has been a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00300FGareth... Long time no\x01",
            "see.\x02\x03",
            "#00306FThat aside, you should\x01",
            "really drop the "young\x01",
            "master" bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#11P...I think you've heard\x01",
            "about the incident with\x01",
            "Master Baldur.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#11PHe was truly a good\x01",
            "person. I offer my\x01",
            "heartfelt condolences.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00308FYeah.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#5P#04604FCut the doom and gloom!\x01",
            "We're gonna have a blast\x01",
            "tonight!\x02\x03",
            "#04602FC'mon, get in! You guys\x01",
            "too! Hurry!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_306F():
        OP_95(0xFE, 3200, 0, -18400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_306F)
    WaitChrThread(0x16, 1)
    TurnDirection(0x16, 0x104, 500)

    ChrTalk(
        0x101,
        (
            "#00001FSure... Then, don't mind\x01",
            "if I do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10304FHaha, excuse me.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(14500, 2000)
    FadeToDark(2000, 0, -1)

    def lambda_30F5():
        OP_95(0xFE, 3700, 0, -16800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_30F5)
    Sleep(500)

    def lambda_3112():
        OP_95(0xFE, 3700, 0, -16800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3112)
    WaitChrThread(0x104, 1)

    def lambda_3130():
        OP_95(0xFE, 4700, 500, -16800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3130)

    def lambda_314A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_314A)

    def lambda_315B():
        OP_95(0xFE, 3700, 0, -16800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_315B)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0x104, 0xFF)
    SetScenarioFlags(0x22, 0)
    NewScene("e0111", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_34_2B93 end

    def Function_35_3184(): pass

    label("Function_35_3184")

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

    # Function_35_3184 end

    def Function_36_3395(): pass

    label("Function_36_3395")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_346D")
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
    Jump("Function_36_3395")

    label("loc_346D")

    Return()

    # Function_36_3395 end

    def Function_37_346E(): pass

    label("Function_37_346E")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 4700, 0, -30500)
    OP_9F(0x1, 4700, 0, -12500)
    OP_9F(0x1, 8580, 0, 4180)
    OP_9F(0x1, 11000, 0, 30000)
    OP_9F(0x1, 11000, 0, 60000)
    OP_9F(0x2, 0xFE, 6000, 0x6)
    Return()

    # Function_37_346E end

    def Function_38_34C2(): pass

    label("Function_38_34C2")

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

    def lambda_362B():
        OP_9B(0x1, 0xFE, 0x0, 0x9C40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_362B)
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

    # Function_38_34C2 end

    def Function_39_36AA(): pass

    label("Function_39_36AA")

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

    # Function_39_36AA end

    def Function_40_3870(): pass

    label("Function_40_3870")

    OP_63(0xFE, 0x0, 1850, 0x26, 0x27, 0xFA, 0x0)

    label("loc_3882")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3906")
    OP_9B(0x1, 0xFE, 0x28, 0x3E8, 0x7D0, 0x0)

    def lambda_38A1():
        OP_A6(0xFE, 0x1E, 0x1E, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_38A1)
    OP_9B(0x1, 0xFE, 0x37, 0x1F4, 0x3E8, 0x0)
    Sleep(1500)
    OP_9B(0x1, 0xFE, 0xFFD3, 0x5DC, 0x7D0, 0x0)

    def lambda_38DB():
        OP_A6(0xFE, 0x1E, 0x1E, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_38DB)
    OP_9B(0x1, 0xFE, 0xFFD3, 0x1F4, 0x3E8, 0x0)
    Sleep(2000)
    Jump("loc_3882")

    label("loc_3906")

    Return()

    # Function_40_3870 end

    def Function_41_3907(): pass

    label("Function_41_3907")

    Sleep(3000)
    Sound(1012, 0, 80, 0)
    Return()

    # Function_41_3907 end

    def Function_42_3911(): pass

    label("Function_42_3911")

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

    def lambda_3B29():
        OP_96(0xFE, 0xFFFF8FE4, 0xFFFFDFF8, 0xFFFFA2A4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3B29)

    def lambda_3B43():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3B43)
    WaitChrThread(0x104, 1)
    Sound(104, 0, 70, 0)
    OP_71(0xF, 0xA, 0x0, 0x0, 0x0)
    OP_79(0xF)
    SetMapObjFlags(0xF, 0x10)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x105,
        "Young Man's Voice",
        "#2916V#30W─You're going?\x02",
    )

    CloseMessageWindow()
    OP_24(0xB64)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#5P#00308F#2760V#30WYou, huh...\x02",
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
            "you up this late at\x01",
            "night?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_3C70():
        OP_96(0xFE, 0xFFFFA36C, 0xFFFFDFF8, 0xFFFFA2A4, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3C70)
    Sleep(1000)
    OP_68(-21400, -7200, -22930, 2500)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)
    SetCameraDistance(12000, 40000)

    ChrTalk(
        0x105,
        (
            "#10302F#5PHehe, I went to hang out\x01",
            "for a bit at my favorite\x01",
            "bar.\x02\x03",
            "#10306FWell, my personality being\x01",
            "what it is, I'm not really\x01",
            "bothered by it, but...\x02\x03",
            "#10301FDon't you think the others\x01",
            "will get angry?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306F...Probably.\x02\x03",
            "#00301FHowever─ This is my\x01",
            "problem.\x02\x03",
            "It's got nothin' to do\x01",
            "with uncle and Shirley.\x02\x03",
            "To say nothin' of it\x01",
            "bein' alright to involve\x01",
            "Lloyd and the others.\x02\x03",
            "#00303FI'm goin' out to... To\x01",
            "conclude things\x01",
            "properly, myself.\x02\x03",
            "#00300FThat's just how it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10308F#5PHmm, well, whatever.\x02\x03",
            "#10306FBoth you and Wald... All\x01",
            "men are idiots, aren't\x01",
            "they.\x02\x03",
            "#10302FWhy do you have to be so\x01",
            "antisocial like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FLeave me alone, will\x01",
            "you?\x02\x03",
            "#00305F...Anyway, you... I've\x01",
            "been wantin' to ask you\x01",
            "for a while.\x02\x03",
            "#00302FSeriously, whose side\x01",
            "are you on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#5PHehe. I have no idea\x01",
            "what you're talking\x01",
            "about.\x02\x03",
            "#10300FAlthough, I think your\x01",
            "other guess was right.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#6P#00303F...I see.\x02\x03",
            "#00311FI thought you seemed like\x01",
            "those guys I fought lots\x01",
            "of times way back when.\x02\x03",
            "You pretended to meet\x01",
            "that girl for the first\x01",
            "time too, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#5PHehe, I wonder?\x02\x03",
            "#10302F─As thanks for keeping your\x01",
            "silence, I'll pretend to know\x01",
            "nothing tomorrow morning.\x02\x03",
            "You can go wild to your\x01",
            "heart's content.\x02",
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

    def lambda_420F():

        label("loc_420F")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_420F")

    QueueWorkItem2(0x104, 3, lambda_420F)

    def lambda_4221():
        OP_95(0xFE, -20000, -8200, -23900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4221)
    Sleep(800)
    SetChrSubChip(0x105, 0x1)
    WaitChrThread(0x104, 1)
    EndChrThread(0x104, 0x3)
    SetChrChipByIndex(0x104, 0x1E)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x104, 0x10)
    ClearChrFlags(0x104, 0x2)
    ClearChrFlags(0x104, 0x20)

    def lambda_4261():
        OP_95(0xFE, -13000, -4200, -17000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4261)
    Sleep(500)
    SetChrSubChip(0x105, 0x2)
    Sleep(500)
    OP_6F(0x79)
    OP_68(-20360, -6600, -23560, 2000)
    WaitChrThread(0x104, 1)

    def lambda_429C():
        OP_95(0xFE, 0, 0, -17000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_429C)
    Sleep(1000)
    OP_6F(0x79)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x105)
    Sleep(500)

    ChrTalk(
        0x105,
        (
            "#5P#10306F...Well, without him, I\x01",
            "guess I'm a little worried\x01",
            "about our combat strength.\x02\x03",
            "#10308FDepending on the\x01",
            "situation, maybe I'll have\x01",
            "Abbas follow him...\x02",
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

    # Function_42_3911 end

    def Function_43_440B(): pass

    label("Function_43_440B")

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

    # Function_43_440B end

    def Function_44_45DB(): pass

    label("Function_44_45DB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_45FF")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    OP_A1(0xFE, 0x5DC, 0x3, 0x3, 0x2, 0x1)
    Jump("Function_44_45DB")

    label("loc_45FF")

    Return()

    # Function_44_45DB end

    def Function_45_4600(): pass

    label("Function_45_4600")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4614")
    Call(0, 16)
    Jump("loc_46C3")

    label("loc_4614")

    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)
    TurnDirection(0x10, 0x0, 0)
    TurnDirection(0x11, 0x0, 0)

    ChrTalk(
        0x10,
        (
            "This road is closed until\x01",
            "the heads of state are\x01",
            "escorted to Michelam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Support Section, please\x01",
            "understand and\x01",
            "cooperate.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10, 0xB4, 0x0)
    OP_93(0x11, 0xB4, 0x0)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)

    label("loc_46C3")

    Sleep(50)
    SetChrPos(0x0, 11850, 0, 22430, 180)
    EventEnd(0x4)
    Return()

    # Function_45_4600 end

    def Function_46_46DA(): pass

    label("Function_46_46DA")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "       The Crossbell Bell\x01",
            "A giant bell excavated in Crossbell State in S1185. From\x01",
            "the condition of the unearthed remains, it is thought to\x01",
            "date back to the middle ages. Made of multiple metals,\x01",
            "when hit, it rings in a pleasant low tone.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Thought to have been built by\x01",
            "influential person of those times, for\x01",
            "what it was used is still debated.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_46_46DA end

    def Function_47_486F(): pass

    label("Function_47_486F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4898")
    EventBegin(0x1)
    Call(0, 50)
    Sleep(50)
    SetChrPos(0x0, 4240, 0, -20650, 0)
    EventEnd(0x4)

    label("loc_4898")

    Return()

    # Function_47_486F end

    def Function_48_4899(): pass

    label("Function_48_4899")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_48C2")
    EventBegin(0x1)
    Call(0, 50)
    Sleep(50)
    SetChrPos(0x0, 16840, 0, -3910, 270)
    EventEnd(0x4)

    label("loc_48C2")

    Return()

    # Function_48_4899 end

    def Function_49_48C3(): pass

    label("Function_49_48C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_48EC")
    EventBegin(0x1)
    Call(0, 50)
    Sleep(50)
    SetChrPos(0x0, -13380, 0, 14530, 135)
    EventEnd(0x4)

    label("loc_48EC")

    Return()

    # Function_49_48C3 end

    def Function_50_48ED(): pass

    label("Function_50_48ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4989")

    ChrTalk(
        0x10A,
        (
            "#00603FThe Geofront B-Division\x01",
            "entrance is on\x01",
            "Residential Street.\x02\x03",
            "#00600FLet's go there on the\x01",
            "double.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, understood.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_49F6")

    label("loc_4989")


    ChrTalk(
        0x10A,
        (
            "#00603FThe Geofront B-Division\x01",
            "entrance is on\x01",
            "Residential Street.\x02\x03",
            "#00600FLet's go there on the\x01",
            "double.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49F6")

    Return()

    # Function_50_48ED end

    SaveToFile()

Try(main)
