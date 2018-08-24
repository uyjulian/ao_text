from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1000.bin",                # FileName
        "t1000",                    # MapName
        "t1000",                    # Location
        0x0041,                     # MapIndex
        "ed7565",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x04,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 65, 0, 2, 0, 3],
    )

    BuildStringList((
        "t1000",                  # 0
        "Tourist",                # 1
        "Tourist",                # 2
        "Tourist",                # 3
        "Tourist",                # 4
        "Tourist",                # 5
        "Tourist",                # 6
        "Crewman Salsa",          # 7
        "Rixia",                  # 8
        "KeA",                    # 9
        "Fran",                   # 10
        "Cecil",                  # 11
        "Ilya",                   # 12
        "Sully",                  # 13
        "Mariabell",              # 14
        "Zeit",                   # 15
        "水上バス",               # 16
        "Passenger",              # 17
        "Passenger",              # 18
        "Passenger",              # 19
        "Passenger",              # 20
        "Passenger",              # 21
        "Passenger",              # 22
        "Passenger",              # 23
        "Passenger",              # 24
        "SE制御",                 # 25
        "ボート",                 # 26
        "ボート",                 # 27
        "To Theme Park",          # 28
        "To Residential Area",    # 29
        "To Lake Beach",          # 30
    ))

    AddCharChip((
        "chr/ch20000.itc",                   # 00
        "chr/ch20900.itc",                   # 01
        "chr/ch20300.itc",                   # 02
        "chr/ch20200.itc",                   # 03
        "chr/ch21300.itc",                   # 04
        "chr/ch24400.itc",                   # 05
        "chr/ch28400.itc",                   # 06
        "chr/ch05200.itc",                   # 07
    ))

    DeclNpc(7730,    4294965296, 4294942786, 90,   389,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(9050,    4294965296, 4294942786, 270,  389,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(4294959907, 4294963296, 4294919186, 180,  389,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(4294959907, 4294963296, 4294918186, 0,    389,  0x0, 0,   3,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(4294939647, 4294963296, 4294917076, 270,  389,  0x0, 0,   4,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(4294966657, 4294965296, 4294941266, 180,  389,  0x0, 0,   5,   0,   0,   1,   0,   10,  255,  0)
    DeclNpc(4294963556, 4294963296, 4294920116, 180,  389,  0x0, 0,   6,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   7,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(23450,   4294962296, 4294912366, 1200,    29380,   4294961296, 4294911866, 0x007C, 0,  14, 0x0000)
    DeclActor(10350,   4294963306, 4294920886, 1200,    10350,   4294964796, 4294920886, 0x007C, 0,  41, 0x0000)
    DeclActor(3300,    4294962296, 4294909136, 2500,    3300,    4294963796, 4294909136, 0x007C, 0,  42, 0x0000)

    PlaceName(-5.0, 0.0, 95.0, 0x0000, 0x0000, "To Theme Park")
    PlaceName(-95.0, 0.0, 20.0, 0x0000, 0x0000, "To Residential Area")
    PlaceName(75.0, 0.0, 15.0, 0x0000, 0x0000, "To Lake Beach")
    PlaceName(1.0, 0.0, 17.5, 0x0000, 0x0052, "")

    ChipFrameInfo(1296, 0)                                       # 0

    ScpFunction((
        "Function_0_510",          # 00, 0
        "Function_1_5C0",          # 01, 1
        "Function_2_5EB",          # 02, 2
        "Function_3_721",          # 03, 3
        "Function_4_8DF",          # 04, 4
        "Function_5_964",          # 05, 5
        "Function_6_A12",          # 06, 6
        "Function_7_A9B",          # 07, 7
        "Function_8_B31",          # 08, 8
        "Function_9_C29",          # 09, 9
        "Function_10_CBC",         # 0A, 10
        "Function_11_D78",         # 0B, 11
        "Function_12_E24",         # 0C, 12
        "Function_13_12AC",        # 0D, 13
        "Function_14_12F7",        # 0E, 14
        "Function_15_13BE",        # 0F, 15
        "Function_16_2DB1",        # 10, 16
        "Function_17_2E19",        # 11, 17
        "Function_18_2E4D",        # 12, 18
        "Function_19_2E8D",        # 13, 19
        "Function_20_2ECD",        # 14, 20
        "Function_21_2F0D",        # 15, 21
        "Function_22_2F4D",        # 16, 22
        "Function_23_2F8D",        # 17, 23
        "Function_24_2FCD",        # 18, 24
        "Function_25_300D",        # 19, 25
        "Function_26_3023",        # 1A, 26
        "Function_27_365A",        # 1B, 27
        "Function_28_3758",        # 1C, 28
        "Function_29_3810",        # 1D, 29
        "Function_30_3825",        # 1E, 30
        "Function_31_3885",        # 1F, 31
        "Function_32_38D3",        # 20, 32
        "Function_33_3921",        # 21, 33
        "Function_34_396F",        # 22, 34
        "Function_35_39BD",        # 23, 35
        "Function_36_3A11",        # 24, 36
        "Function_37_3DA4",        # 25, 37
        "Function_38_3DF9",        # 26, 38
        "Function_39_3E1E",        # 27, 39
        "Function_40_3F26",        # 28, 40
        "Function_41_3F4C",        # 29, 41
        "Function_42_3FB2",        # 2A, 42
    ))


    def Function_0_510(): pass

    label("Function_0_510")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_548"),
        (1, "loc_554"),
        (2, "loc_560"),
        (3, "loc_56C"),
        (4, "loc_578"),
        (5, "loc_584"),
        (6, "loc_590"),
        (SWITCH_DEFAULT, "loc_59C"),
    )


    label("loc_548")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_5A8")

    label("loc_554")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_5A8")

    label("loc_560")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_5A8")

    label("loc_56C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_5A8")

    label("loc_578")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_5A8")

    label("loc_584")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_5A8")

    label("loc_590")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5A8")

    label("loc_59C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5A8")

    label("loc_5A8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5BF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5A8")

    label("loc_5BF")

    Return()

    # Function_0_510 end

    def Function_1_5C0(): pass

    label("Function_1_5C0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5EA")
    OP_94(0xFE, 0xFFFFE3A4, 0xFFFFA132, 0x1AB8, 0xFFFF90A2, 0x3E8)
    Sleep(500)
    Jump("Function_1_5C0")

    label("loc_5EA")

    Return()

    # Function_1_5C0 end

    def Function_2_5EB(): pass

    label("Function_2_5EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_5F9")
    Jump("loc_6D5")

    label("loc_5F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_663")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_634")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -10480, -2000, -26610, 270)
    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_634")

    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 1130, -4000, -53460, 180)
    Jump("loc_6D5")

    label("loc_663")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_69B")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 1130, -4000, -53460, 180)
    Jump("loc_6D5")

    label("loc_69B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_6CC")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_6D5")

    label("loc_6CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_6D5")

    label("loc_6D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_6E9")
    ClearScenarioFlags(0x22, 0)
    Event(0, 15)
    Jump("loc_720")

    label("loc_6E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_6FD")
    ClearScenarioFlags(0x22, 1)
    Event(0, 26)
    Jump("loc_720")

    label("loc_6FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_711")
    ClearScenarioFlags(0x22, 2)
    Event(0, 36)
    Jump("loc_720")

    label("loc_711")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_720")
    ClearScenarioFlags(0x22, 3)
    Event(0, 39)

    label("loc_720")

    Return()

    # Function_2_5EB end

    def Function_3_721(): pass

    label("Function_3_721")

    SetMapObjFrame(0xFF, "t1000_sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "t1000_sky_y", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_757")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_757")

    Sound(126, 1, 80, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_774")
    SoundLoad(918)
    BeginChrThread(0x20, 3, 0, 40)

    label("loc_774")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_79E")
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    OP_70(0x0, 0x1E)
    Jump("loc_7A4")

    label("loc_79E")

    SetMapObjFlags(0x0, 0x4)

    label("loc_7A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7C9")
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    Jump("loc_7DB")

    label("loc_7C9")

    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)

    label("loc_7DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7EF")
    ClearMapObjFlags(0x1, 0x4)

    label("loc_7EF")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_80B")
    ClearMapObjFlags(0x7, 0x4)
    OP_66(0x2, 0x1)

    label("loc_80B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_829")
    OP_11(0xD1, 0xED, 0xFC, 0x32, 0xC8, 0x0)

    label("loc_829")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_84B")
    SetMapObjFrame(0xFF, "t1000_water", 0x2, "loop_off")

    label("loc_84B")

    LoadEffect(0xF, "eff\\mgm03_02.eff")
    PlayEffect(0xF, 0x8, 0xFF, 0x0, 29380, -6000, -55430, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8BC")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x3C, 0x1F4, 0x0)
    Jump("loc_8DE")

    label("loc_8BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_8DE")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x3C, 0x1F4, 0x0)

    label("loc_8DE")

    Return()

    # Function_3_721 end

    def Function_4_8DF(): pass

    label("Function_4_8DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8F6")
    Call(0, 12)
    Return()

    label("loc_8F6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_907")
    Jump("loc_960")

    label("loc_907")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_915")
    Jump("loc_960")

    label("loc_915")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_923")
    Jump("loc_960")

    label("loc_923")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_93B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_936")

    label("loc_936")

    Jump("loc_960")

    label("loc_93B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_949")
    Jump("loc_960")

    label("loc_949")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_957")
    Jump("loc_960")

    label("loc_957")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_960")

    label("loc_960")

    TalkEnd(0xFE)
    Return()

    # Function_4_8DF end

    def Function_5_964(): pass

    label("Function_5_964")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_975")
    Jump("loc_A0E")

    label("loc_975")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_A05")

    ChrTalk(
        0x8,
        (
            "Well, even staring at\x01",
            "the lake while waiting\x01",
            "is fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm a little tired from\x01",
            "walking around, so I\x01",
            "think I'll wait here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A0E")

    label("loc_A05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_A0E")

    label("loc_A0E")

    TalkEnd(0xFE)
    Return()

    # Function_5_964 end

    def Function_6_A12(): pass

    label("Function_6_A12")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_A23")
    Jump("loc_A97")

    label("loc_A23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_A8E")

    ChrTalk(
        0x9,
        (
            "It seems the water bus\x01",
            "isn't here yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In that case, let's have\x01",
            "a little more fun.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A97")

    label("loc_A8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_A97")

    label("loc_A97")

    TalkEnd(0xFE)
    Return()

    # Function_6_A12 end

    def Function_7_A9B(): pass

    label("Function_7_A9B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_AAC")
    Jump("loc_B2D")

    label("loc_AAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_ABA")
    Jump("loc_B2D")

    label("loc_ABA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_B2D")

    ChrTalk(
        0xA,
        "Wait, dear...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Please don't say something\x01",
            "that will make me worry about\x01",
            "when it's time to board.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B2D")

    TalkEnd(0xFE)
    Return()

    # Function_7_A9B end

    def Function_8_B31(): pass

    label("Function_8_B31")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_B42")
    Jump("loc_C25")

    label("loc_B42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_BBC")

    ChrTalk(
        0xB,
        (
            "I kind of don't want to\x01",
            "leave because of how fun\x01",
            "it is here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "This is a nice place, it\x01",
            "heals me...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C25")

    label("loc_BBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_C25")

    ChrTalk(
        0xB,
        (
            "Uhmm, I haven't left\x01",
            "anything at the hotel,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...I...shouldn't have.\x01",
            "...Perhaps.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C25")

    TalkEnd(0xFE)
    Return()

    # Function_8_B31 end

    def Function_9_C29(): pass

    label("Function_9_C29")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_C3A")
    Jump("loc_CB8")

    label("loc_C3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_C48")
    Jump("loc_CB8")

    label("loc_C48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_CB8")

    ChrTalk(
        0xC,
        (
            "I got separated from my\x01",
            "boyfriend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Geez. If he doesn't come\x01",
            "quick, I'll go home\x01",
            "without him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CB8")

    TalkEnd(0xFE)
    Return()

    # Function_9_C29 end

    def Function_10_CBC(): pass

    label("Function_10_CBC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_CCD")
    Jump("loc_D74")

    label("loc_CCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_CDB")
    Jump("loc_D74")

    label("loc_CDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_D74")

    ChrTalk(
        0xD,
        (
            "My girlfriend seems to\x01",
            "have left ahead of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "*sigh*, I wonder where she's\x01",
            "gone. I've got to find her\x01",
            "before the water bus departs...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D74")

    TalkEnd(0xFE)
    Return()

    # Function_10_CBC end

    def Function_11_D78(): pass

    label("Function_11_D78")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_D89")
    Jump("loc_E20")

    label("loc_D89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_D97")
    Jump("loc_E20")

    label("loc_D97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_E17")

    ChrTalk(
        0xE,
        (
            "The water bus will soon\x01",
            "depart for the Crossbell\x01",
            "City landing field.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "If you are boarding,\x01",
            "please hurry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E20")

    label("loc_E17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_E20")

    label("loc_E20")

    TalkEnd(0xFE)
    Return()

    # Function_11_D78 end

    def Function_12_E24(): pass

    label("Function_12_E24")

    EventBegin(0x0)
    OP_4B(0xF, 0xFF)
    Fade(500)
    OP_68(-9680, -800, -26810, 0)
    MoveCamera(314, 20, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(30350, 0)
    SetChrPos(0x101, -7850, -2000, -27000, 270)
    SetChrPos(0x153, -7850, -2000, -26200, 270)
    OP_0D()
    Sleep(2000)
    OP_64(0xF)

    ChrTalk(
        0xF,
        "#01803F...*sigh*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005F...Rixia? So this is\x01",
            "where you were.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xF, 0x5A, 0x1F4)

    ChrTalk(
        0xF,
        "#01805FLloyd, KeA...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01105FHey Rixia, are you\x01",
            "feeling down for some\x01",
            "reason?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FIs something worrying\x01",
            "you? If you want, I...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01809FAh, no, it's nothing serious...\x02\x03",
            "#01804FUmm, it's just a little mental fatigue.\x01",
            "I was thinking there are busy places\x01",
            "even outside Entertainment District.\x02\x03",
            "#01802FHowever, catching the breeze here gave\x01",
            "me great peace of mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00003F...I see. Good then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01108FRixia, are you really\x01",
            "all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01809FYes, I'm fine now.\x02\x03",
            "#01803FThen, Lloyd. I'll go\x01",
            "find Ilya and the\x01",
            "others.\x02\x03",
            "#01802FI'll attend the theme\x01",
            "park with everyone, so\x01",
            "please don't worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FR-Right...\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xF, 0x40)
    OP_68(-7800, -800, -26950, 4000)
    BeginChrThread(0xF, 3, 0, 13)
    Sleep(300)

    def lambda_11A1():

        label("loc_11A1")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_11A1")

    QueueWorkItem2(0x101, 2, lambda_11A1)

    def lambda_11B3():

        label("loc_11B3")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_11B3")

    QueueWorkItem2(0x153, 2, lambda_11B3)
    WaitChrThread(0xF, 3)
    SetChrFlags(0xF, 0x80)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x153, 0xFF)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    TurnDirection(0x153, 0x101, 500)
    OP_63(0x153, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x153,
        "#01105FWhat's wrong, Lloyd?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x153, 500)

    ChrTalk(
        0x101,
        (
            "#6P#00003F...No, it's nothing.\x02\x03",
            "#00000FI guess it's about time\x01",
            "for us to be going, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x15A, 5)
    SetChrPos(0x0, -8850, -2000, -26600, 270)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_12_E24 end

    def Function_13_12AC(): pass

    label("Function_13_12AC")

    OP_93(0xFE, 0x2D, 0x1F4)

    def lambda_12B8():
        OP_95(0xFE, -8610, -2000, -24800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12B8)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x0)

    def lambda_12DD():
        OP_95(0xFE, -610, -2000, -24800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12DD)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_13_12AC end

    def Function_14_12F7(): pass

    label("Function_14_12F7")

    EventBegin(0x1)
    Sound(2094, 255, 100, 0)

    ChrTalk(
        0x101,
        (
            "#0000FIt seems we can fish\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(27760, -3400, -57630, 1500)
    MoveCamera(315, 28, 0, 1500)
    OP_6E(300, 1500)
    SetCameraDistance(35500, 1500)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Fish?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Fish\x01",        # 0
            "Cancel\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13B9")
    OP_E2(0x2)
    MiniGame(0x6, 0x5, 0x5B9A, 0xFFFFEC78, 0xFFFF296E, 0x5A, 0x72C4, 0xFFFFE890, 0xFFFF277A)

    label("loc_13B9")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_14_12F7 end

    def Function_15_13BE(): pass

    label("Function_15_13BE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch08200.itc", 0x1E)
    LoadChrToIndex("chr/ch08500.itc", 0x1F)
    LoadChrToIndex("chr/ch05200.itc", 0x20)
    LoadChrToIndex("chr/ch05100.itc", 0x21)
    LoadChrToIndex("chr/ch07500.itc", 0x22)
    LoadChrToIndex("chr/ch10100.itc", 0x23)
    LoadChrToIndex("chr/ch05500.itc", 0x24)
    LoadChrToIndex("chr/ch20600.itc", 0x28)
    LoadChrToIndex("chr/ch20200.itc", 0x29)
    LoadChrToIndex("chr/ch20300.itc", 0x2A)
    LoadChrToIndex("chr/ch21600.itc", 0x2B)
    LoadChrToIndex("chr/ch21300.itc", 0x2C)
    LoadChrToIndex("chr/ch21200.itc", 0x2D)
    LoadChrToIndex("chr/ch27700.itc", 0x2E)
    LoadChrToIndex("chr/ch23600.itc", 0x2F)
    SoundLoad(2713)
    SoundLoad(2714)
    SoundLoad(2715)
    SoundLoad(3774)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis406.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01700.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu06400.itp")
    CreatePortrait(3, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu05900.itp")
    CreatePortrait(4, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01800.itp")
    CreatePortrait(5, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu14000.itp")
    CreatePortrait(6, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02900.itp")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -7250, -4000, -41000, 180)
    SetChrPos(0x102, -7250, -4000, -41000, 180)
    SetChrPos(0x103, -7250, -4000, -41000, 180)
    SetChrPos(0x104, -7250, -4000, -41000, 180)
    SetChrPos(0x109, -7250, -4000, -41000, 180)
    SetChrPos(0x105, -7250, -4000, -41000, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x1E)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -7250, -4000, -41000, 180)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0x1F)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 2500, -4000, -50000, 270)
    SetChrFlags(0x11, 0x8)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 0x21)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 4500, -4000, -49500, 270)
    SetChrFlags(0x13, 0x8)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 0x22)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 4350, -4000, -51000, 270)
    SetChrFlags(0x12, 0x8)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 0x20)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 5650, -4000, -51000, 270)
    SetChrFlags(0xF, 0x8)
    OP_4B(0xF, 0xFF)
    ClearChrFlags(0x14, 0x80)
    SetChrChipByIndex(0x14, 0x23)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 6000, -4000, -49350, 270)
    SetChrFlags(0x14, 0x8)
    ClearChrFlags(0x15, 0x80)
    SetChrChipByIndex(0x15, 0x24)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 4650, -4000, -50000, 270)
    SetChrFlags(0x15, 0x8)
    ClearChrFlags(0x17, 0x80)
    OP_78(0x0, 0x17)
    OP_49()
    SetChrPos(0x17, -25070, -5500, -38200, 90)
    OP_D5(0x17, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x79, 0xB4, 0x0, 0x20)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrChipByIndex(0x18, 0x28)
    SetChrChipByIndex(0x19, 0x29)
    SetChrChipByIndex(0x1A, 0x2A)
    SetChrChipByIndex(0x1B, 0x2B)
    SetChrChipByIndex(0x1C, 0x2C)
    SetChrChipByIndex(0x1D, 0x2D)
    SetChrChipByIndex(0x1E, 0x2E)
    SetChrChipByIndex(0x1F, 0x2F)
    SetChrSubChip(0x18, 0x0)
    SetChrSubChip(0x19, 0x0)
    SetChrSubChip(0x1A, 0x0)
    SetChrSubChip(0x1B, 0x0)
    SetChrSubChip(0x1C, 0x0)
    SetChrSubChip(0x1D, 0x0)
    SetChrSubChip(0x1E, 0x0)
    SetChrSubChip(0x1F, 0x0)
    SetChrFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x18, -7250, -4000, -41000, 180)
    SetChrPos(0x19, -7250, -4000, -41000, 180)
    SetChrPos(0x1A, -7250, -4000, -41000, 180)
    SetChrPos(0x1B, -7250, -4000, -41000, 180)
    SetChrPos(0x1C, -7250, -4000, -41000, 180)
    SetChrPos(0x1D, -7250, -4000, -41000, 180)
    SetChrPos(0x1E, -7250, -4000, -41000, 180)
    SetChrPos(0x1F, -7250, -4000, -41000, 180)
    OP_A7(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x19, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-5070, 1300, -18200, 0)
    MoveCamera(330, 9, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(78000, 0)
    PlaceName2(340, 40, "c_plac20", 0x0, 2500)
    OP_68(-5070, -2700, -18200, 10000)
    MoveCamera(330, 9, 0, 10000)
    OP_6E(600, 10000)
    SetCameraDistance(78000, 10000)
    FadeToBright(1000, 0)
    BeginChrThread(0x17, 3, 0, 16)
    BeginChrThread(0x20, 1, 0, 25)
    WaitChrThread(0x17, 3)
    OP_0D()
    Fade(500)
    OP_68(-7250, -3000, -46000, 0)
    MoveCamera(315, 21, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(50000, 0)
    OP_0D()
    OP_74(0x0, 0xA)
    OP_71(0x0, 0x1, 0x1E, 0x0, 0x8)
    Sound(108, 0, 80, 0)
    Sound(107, 0, 100, 0)
    OP_79(0x0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0xF1, 0x12C, 0x0, 0x20)
    BeginChrThread(0x18, 3, 0, 17)
    Sleep(800)
    BeginChrThread(0x19, 3, 0, 17)
    Sleep(800)
    BeginChrThread(0x1A, 3, 0, 17)
    Sleep(800)
    BeginChrThread(0x1B, 3, 0, 17)
    Sleep(800)
    BeginChrThread(0x1C, 3, 0, 17)
    Sleep(800)
    BeginChrThread(0x1D, 3, 0, 17)
    Sleep(800)
    BeginChrThread(0x1E, 3, 0, 17)
    Sleep(800)
    BeginChrThread(0x1F, 3, 0, 17)
    Sleep(800)
    BeginChrThread(0x101, 3, 0, 18)
    Sleep(800)
    BeginChrThread(0x10, 3, 0, 24)
    Sleep(800)
    BeginChrThread(0x104, 3, 0, 21)
    Sleep(800)
    BeginChrThread(0x103, 3, 0, 20)
    Sleep(800)
    BeginChrThread(0x102, 3, 0, 19)
    Sleep(800)
    BeginChrThread(0x105, 3, 0, 23)
    Sleep(800)
    BeginChrThread(0x109, 3, 0, 22)
    Fade(500)
    OP_68(-7460, -3000, -50070, 0)
    MoveCamera(315, 21, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(32000, 0)
    OP_0D()
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x105, 3)
    WaitChrThread(0x10, 3)
    EndChrThread(0x18, 0x3)
    EndChrThread(0x19, 0x3)
    EndChrThread(0x1A, 0x3)
    EndChrThread(0x1B, 0x3)
    EndChrThread(0x1C, 0x3)
    EndChrThread(0x1D, 0x3)
    EndChrThread(0x1E, 0x3)
    EndChrThread(0x1F, 0x3)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)

    ChrTalk(
        0x101,
        (
            "#00002F#6PNow then... I think\x01",
            "Mariabell is waiting for\x01",
            "us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#11PYes, our appointment was\x01",
            "for 9:30 so we should be\x01",
            "right on time...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearChrFlags(0x11, 0x8)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x11,
        "Girl's Voice",
        "#2713V#1P#30WAh, you came, you came!\x02",
    )

    CloseMessageWindow()
    OP_24(0xA99)
    OP_C9(0x1, 0x80000000)
    OP_63(0x10, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#6PThis voice...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10111F#11PN-No way...!?\x02",
    )

    CloseMessageWindow()

    def lambda_1CC3():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1CC3)
    Sleep(50)

    def lambda_1CD3():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1CD3)
    Sleep(50)

    def lambda_1CE3():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1CE3)
    Sleep(50)

    def lambda_1CF3():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1CF3)
    Sleep(50)

    def lambda_1D03():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1D03)
    Sleep(50)

    def lambda_1D13():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_1D13)
    Sleep(50)

    def lambda_1D23():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_1D23)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)
    WaitChrThread(0x10, 2)
    Sleep(300)
    Fade(500)
    OP_68(-3250, -3000, -50350, 0)
    MoveCamera(30, 21, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(32000, 0)
    OP_68(-6250, -3000, -50350, 2500)

    def lambda_1D93():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1D93)
    Sleep(500)
    OP_63(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitChrThread(0x11, 1)
    OP_6F(0x79)
    OP_0D()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0x11,
        (
            "#2714V#30WNoｱl, everyone, good morning!\x02\x03",
            "#2715V#30WGood morning to you too, KeA!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xA9B)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    OP_C9(0x1, 0x80000000)

    ChrTalk(
        0x10,
        "#01109F#6PGood morniiing!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305F#6POh, if it isn't Fran!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#5PW-What are you doing\x01",
            "here...?\x02\x03",
            "#10101FWhen I saw you\x01",
            "yesterday, you didn't\x01",
            "say anything about this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#06409F#11PEhehe. I wanted to\x01",
            "surprise you guys.\x02\x03",
            "#06402FAnd I'm not the only\x01",
            "special guest, you know.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x13, 0x8)
    ClearChrFlags(0x12, 0x8)
    ClearChrFlags(0xF, 0x8)
    ClearChrFlags(0x14, 0x8)

    NpcTalk(
        0x12,
        "Woman's Voice",
        (
            "#1PHaha, looks like you're\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x13,
        "Woman's Voice",
        (
            "#1PAlright, the gang's all\x01",
            "here so I'm going to\x01",
            "have some fun today!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
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
        0x101,
        "#00005F#6PHuuuh!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#6PT-That voice...\x02",
    )

    CloseMessageWindow()
    OP_68(-5400, -3000, -50350, 3000)

    def lambda_21FA():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_21FA)
    Sleep(100)

    def lambda_2212():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2212)
    Sleep(100)

    def lambda_222A():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_222A)
    Sleep(100)

    def lambda_2242():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2242)
    WaitChrThread(0x13, 1)

    ChrTalk(
        0x101,
        "#00011F#6P!?\x02",
    )

    WaitChrThread(0x12, 1)
    WaitChrThread(0xF, 1)
    WaitChrThread(0x14, 1)
    OP_6F(0x79)
    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00307F#6POoooh!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#01110F#6PAh, it's Cecil!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205F#6PIlya, Rixia and Sully as\x01",
            "well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302F#6PWow, more beauties, huh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#6PT-The only one who would\x01",
            "do something like this\x01",
            "is...\x02\x03",
            "#00101F─Bell! It's you, isn't\x01",
            "it!?\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x15, 0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_END)), "loc_23C6")
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x15,
        "Woman's Voice",
        "#3774V#1P#30WUhuhu─ Right answer.\x02",
    )

    CloseMessageWindow()
    OP_24(0xEBE)
    OP_C9(0x1, 0x80000000)
    Jump("loc_23F2")

    label("loc_23C6")


    NpcTalk(
        0x15,
        "Woman's Voice",
        "#1PUhuhu─ Right answer.\x02",
    )

    CloseMessageWindow()

    label("loc_23F2")

    OP_68(-4680, -3000, -50240, 2500)

    def lambda_2408():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2408)
    WaitChrThread(0x15, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00012F#6PMariabell... What is the\x01",
            "meaning of this?\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x6, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x6, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x6, 0x3)
    OP_CC(0x0, 0x6, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x15,
        (
            "Huhu. At the same time I invited\x01",
            "all of you, I also invited some\x01",
            "people I heard you are good friends\x02\x03",
            "with.\x02\x03",
            "Although this is also to show my\x01",
            "support for the Arc-en-Ciel renewal\x01",
            "performance starting next month.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x6, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x6, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x6, 0x3)
    OP_CC(0x0, 0x6, 0x0)
    Sleep(300)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x13,
        "Little bro, guys, yoo-hoo!\x02",
    )

    CloseMessageWindow()
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    Sound(2634, 255, 100, 0)
    OP_CB(0x4, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x4, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    OP_CC(0x0, 0x4, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0xF,
        (
            "Haha. Nice to see you after so\x01",
            "long.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x4, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x4, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    OP_CC(0x0, 0x4, 0x0)
    OP_CB(0x5, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x5, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x5, 0x3)
    OP_CC(0x0, 0x5, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x14,
        "W-Why did I have to come...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x5, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x5, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x5, 0x3)
    OP_CC(0x0, 0x5, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00012F#6PHaha... I don't even\x01",
            "know what to say.\x02\x03",
            "#00002FCecil, did you get a day\x01",
            "off?\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x12,
        (
            "Yes, I had just gotten one when\x01",
            "Ilya contacted me...\x02\x03",
            "She said you all were coming so I\x01",
            "took her up on it.\x02\x03",
            "Am I a bother to you, perhaps?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)

    ChrTalk(
        0x101,
        "#00009F#6PNo... I'm really happy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00307F#6PUwoooooh!! Am I\x01",
            "dreamin'!?\x02\x03",
            "#00306FCecil, Ilya and so many\x01",
            "beautiful women...\x02\x03",
            "#00309FHyahhoo!! I'm super\x01",
            "excited!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00211F#5PRandy, you're annoying.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#6PWell, I understand how\x01",
            "he feels.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112F#6PHowever, I'm a little\x01",
            "surprised...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#6PCould they be staying in\x01",
            "the same hotel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#02904F#11PYes. I've had rooms\x01",
            "prepared for all of you\x01",
            "on the 3F VIP floor.\x02\x03",
            "I'll first show you to\x01",
            "your rooms where you can\x01",
            "leave your luggage.\x02\x03",
            "#02902FAfter that, you can head\x01",
            "to Michelam resort's\x01",
            "newest attraction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#6PNewest attraction...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#6PNot the theme park?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#06409F#11PEhehe. I was surprised\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01802F#11PActually, uhhm, it seems\x01",
            "they've opened a new\x01",
            "facility...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01709F#11PShe said she reserved it\x01",
            "for us until noon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#02904F#11PYes. I do hope you all\x01",
            "enjoy it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#01105F#6PHuuuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#6PUmm... Just what is this\x01",
            "facility...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#02912F#11PUhuhu... It is a paradise I\x01",
            "created specifically for the\x01",
            "landlocked Crossbell...\x02\x03",
            "#02909FIt is a "Lake Beach" of pure\x01",
            "white sand, overlooking\x01",
            "beautiful Elm Lake.\x02",
        )
    )

    CloseMessageWindow()
    StopSound(126, 1000, 80)
    SetCameraDistance(32375, 1500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_E5(0xA)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_E5(0xB)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 0)
    NewScene("t1020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_15_13BE end

    def Function_16_2DB1(): pass

    label("Function_16_2DB1")

    OP_9B(0x1, 0xFE, 0x0, 0x3A98, 0xBB8, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
    Sound(478, 0, 100, 0)
    OP_82(0x32, 0x0, 0xBB8, 0x1F4)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x5B, 0x78, 0x1F4, 0x8)
    OP_79(0x0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x12D, 0x168, 0x0, 0x20)
    Return()

    # Function_16_2DB1 end

    def Function_17_2E19(): pass

    label("Function_17_2E19")


    def lambda_2E1E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2E1E)
    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x9C4, 0x1)
    OP_9B(0x0, 0xFE, 0xFFA6, 0x3A98, 0x9C4, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_17_2E19 end

    def Function_18_2E4D(): pass

    label("Function_18_2E4D")


    def lambda_2E52():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2E52)
    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x9C4, 0x1)
    OP_95(0xFE, -7250, -4000, -52000, 2500, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_18_2E4D end

    def Function_19_2E8D(): pass

    label("Function_19_2E8D")


    def lambda_2E92():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2E92)
    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x9C4, 0x1)
    OP_95(0xFE, -6250, -4000, -49500, 2500, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_19_2E8D end

    def Function_20_2ECD(): pass

    label("Function_20_2ECD")


    def lambda_2ED2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2ED2)
    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x9C4, 0x1)
    OP_95(0xFE, -7250, -4000, -50000, 2500, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_20_2ECD end

    def Function_21_2F0D(): pass

    label("Function_21_2F0D")


    def lambda_2F12():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2F12)
    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x9C4, 0x1)
    OP_95(0xFE, -8750, -4000, -51000, 2500, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_21_2F0D end

    def Function_22_2F4D(): pass

    label("Function_22_2F4D")


    def lambda_2F52():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2F52)
    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x9C4, 0x1)
    OP_95(0xFE, -7750, -4000, -48500, 2500, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_22_2F4D end

    def Function_23_2F8D(): pass

    label("Function_23_2F8D")


    def lambda_2F92():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2F92)
    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x9C4, 0x1)
    OP_95(0xFE, -8750, -4000, -49000, 2500, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_23_2F8D end

    def Function_24_2FCD(): pass

    label("Function_24_2FCD")


    def lambda_2FD2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2FD2)
    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x9C4, 0x1)
    OP_95(0xFE, -6250, -4000, -51500, 2500, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_24_2FCD end

    def Function_25_300D(): pass

    label("Function_25_300D")

    Sound(475, 0, 100, 0)
    Sleep(1000)
    Sound(477, 0, 100, 0)
    Sound(476, 0, 100, 0)
    Return()

    # Function_25_300D end

    def Function_26_3023(): pass

    label("Function_26_3023")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00302.itc", 0x1E)
    LoadChrToIndex("chr/ch00001.itc", 0x1F)
    LoadChrToIndex("chr/ch00101.itc", 0x20)
    LoadChrToIndex("chr/ch00201.itc", 0x21)
    LoadChrToIndex("chr/ch00301.itc", 0x22)
    LoadEffect(0x0, "event\\ev315_00.eff")
    SoundLoad(483)
    SetChrChipByIndex(0x104, 0x1E)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x21, 0x80)
    OP_78(0x1, 0x21)
    OP_49()
    SetChrPos(0x21, -20090, -5500, -68880, 90)
    OP_D5(0x21, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x79, 0xB4, 0x0, 0x20)
    SetMapObjFrame(0x1, "light00", 0x0, 0x1)
    SetMapObjFrame(0x1, "light01", 0x0, 0x1)
    ClearChrFlags(0x22, 0x80)
    OP_78(0x7, 0x22)
    OP_49()
    SetChrPos(0x22, 1700, -5500, -59250, 90)
    OP_D5(0x22, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x7, 0x1000)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0x1, 0x3C, 0x0, 0x20)
    SetChrBattleFlags(0x101, 0x20)
    SetChrBattleFlags(0x102, 0x20)
    SetChrBattleFlags(0x103, 0x20)
    SetChrBattleFlags(0x104, 0x20)
    OP_90(0x101, -20090, 0, -68280, 90)
    OP_90(0x102, -20090, 0, -69480, 90)
    OP_90(0x103, -21090, 0, -68880, 90)
    OP_90(0x104, -18290, 0, -68880, 90)
    OP_11(0xD1, 0xED, 0xFC, 0x32, 0xC8, 0x0)
    SetMapObjFrame(0xFF, "t1000_water", 0x2, "loop")
    OP_68(740, -4500, -59120, 0)
    MoveCamera(325, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(60000, 0)
    FadeToBright(1000, 0)
    OP_68(14740, -4500, -59120, 10000)
    SetCameraDistance(35000, 10000)
    BeginChrThread(0x21, 3, 0, 28)
    BeginChrThread(0x20, 1, 0, 35)
    WaitChrThread(0x21, 3)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_68(3500, -4000, -58250, 0)
    MoveCamera(318, 24, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(23500, 0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_90(0x101, 17500, 0, -58250, 0)
    OP_90(0x102, 16500, 0, -58750, 0)
    OP_90(0x103, 17500, 0, -59750, 0)
    OP_90(0x104, 16500, 0, -60250, 0)
    OP_68(22000, -4000, -54650, 10000)
    MoveCamera(0, 28, 0, 10000)
    SetCameraDistance(18500, 10000)
    Sleep(1500)
    BeginChrThread(0x101, 3, 0, 31)
    Sleep(1000)
    BeginChrThread(0x102, 3, 0, 32)
    Sleep(1000)
    BeginChrThread(0x103, 3, 0, 33)
    Sleep(1000)
    BeginChrThread(0x104, 3, 0, 34)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x79)
    Fade(500)
    OP_68(20020, 4600, -48340, 0)
    MoveCamera(342, 3, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    OP_68(20020, 1000, -48340, 4000)
    OP_6F(0x79)

    ChrTalk(
        0x103,
        "#00201F#11P#NThe sound of a bell...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33D5")

    ChrTalk(
        0x101,
        (
            "#00011F#5P#NThis is... the one on\x01",
            "the Mirror Castle's top\x01",
            "floor?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#00101F#5P#NYes... It seems so.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_344A")

    label("loc_33D5")


    ChrTalk(
        0x102,
        (
            "#00101F#5P#NThis is... The bell atop\x01",
            "Mirror Castle?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00001F#5P#NSomething like that is\x01",
            "there, huh...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_344A")


    ChrTalk(
        0x104,
        (
            "#00306F#5P#NThe water's surface is\x01",
            "glimmering for some\x01",
            "reason...\x02\x03",
            "#00301FPeTiote, do you know\x01",
            "something?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00203F#11P#NIt seems that something\x01",
            "like a "spiritual\x01",
            "pressure" is rising...\x02\x03",
            "#00201FIt's coming from the\x01",
            "theme park further in.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00003F#5P#NI see...\x02\x03",
            "#00013FThen it's likely Arios\x01",
            "and KeA went there.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#00107F#5P#NYes... Let's go!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x0, 22000, -4910, -53650, 0)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x182, 5)
    OP_29(0xAD, 0x1, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x94, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_361B")
    Jump("loc_3620")

    label("loc_361B")

    OP_29(0x94, 0x4, 0x40)

    label("loc_3620")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x95, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3631")
    Jump("loc_3636")

    label("loc_3631")

    OP_29(0x95, 0x4, 0x40)

    label("loc_3636")

    OP_C9(0x1, 0x10000)
    OP_50(0x52, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x21, 5)
    OP_32(0xFF, 0xFF, 0x0)
    OP_66(0x2, 0x1)
    OP_24(0x1E3)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_26_3023 end

    def Function_27_365A(): pass

    label("Function_27_365A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3757")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36B3")
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 0, -5500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(333)
    Jump("loc_3752")

    label("loc_36B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3701")
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 0, -5500, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(233)
    Jump("loc_3752")

    label("loc_3701")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_374F")
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 0, -5500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(233)
    Jump("loc_3752")

    label("loc_374F")

    Sleep(233)

    label("loc_3752")

    Jump("Function_27_365A")

    label("loc_3757")

    Return()

    # Function_27_365A end

    def Function_28_3758(): pass

    label("Function_28_3758")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x21, 0, 0, 27)
    OP_9B(0x1, 0xFE, 0x0, 0x36B0, 0x1D4C, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0x1388, 0x1964, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x1388, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9B(0x1, 0xFE, 0xFFF1, 0x7D0, 0xFA0, 0x0)
    OP_9B(0x1, 0xFE, 0xFFE2, 0x2EE0, 0xBB8, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9B(0x1, 0xFE, 0xFFD3, 0xBB8, 0x5DC, 0x0)
    OP_9B(0x1, 0xFE, 0xFFD3, 0x5DC, 0x3E8, 0x0)
    OP_82(0x1E, 0x0, 0xBB8, 0x1F4)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_71(0x1, 0x1, 0x3C, 0x1F4, 0x20)
    Return()

    # Function_28_3758 end

    def Function_29_3810(): pass

    label("Function_29_3810")

    OP_96(0xFE, 0x445C, 0xFFFFEE08, 0xFFFF1C76, 0x7D0, 0x0)
    Return()

    # Function_29_3810 end

    def Function_30_3825(): pass

    label("Function_30_3825")

    ClearChrBattleFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x1)
    OP_9D(0xFE, 0x445C, 0xFFFFEFCA, 0xFFFF1F00, 0x258, 0x7D0)
    Sound(30, 0, 100, 0)
    SetChrSubChip(0xFE, 0x1)
    OP_9D(0xFE, 0x445C, 0xFFFFEC78, 0xFFFF2478, 0x320, 0x7D0)
    ClearChrFlags(0xFE, 0x4)
    Sound(31, 0, 100, 0)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_30_3825 end

    def Function_31_3885(): pass

    label("Function_31_3885")

    BeginChrThread(0xFE, 2, 0, 29)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x3)
    BeginChrThread(0xFE, 2, 0, 30)
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0x5A, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x1)
    OP_95(0xFE, 22000, -4900, -53650, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_31_3885 end

    def Function_32_38D3(): pass

    label("Function_32_38D3")

    BeginChrThread(0xFE, 2, 0, 29)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x3)
    BeginChrThread(0xFE, 2, 0, 30)
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0x5A, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x1)
    OP_95(0xFE, 21400, -4900, -54650, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_32_38D3 end

    def Function_33_3921(): pass

    label("Function_33_3921")

    BeginChrThread(0xFE, 2, 0, 29)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x3)
    BeginChrThread(0xFE, 2, 0, 30)
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0x5A, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x1)
    OP_95(0xFE, 22600, -4900, -54650, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_33_3921 end

    def Function_34_396F(): pass

    label("Function_34_396F")

    BeginChrThread(0xFE, 2, 0, 29)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x3)
    BeginChrThread(0xFE, 2, 0, 30)
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0x5A, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x1)
    OP_95(0xFE, 22000, -4900, -55650, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_34_396F end

    def Function_35_39BD(): pass

    label("Function_35_39BD")

    Sound(483, 2, 50, 0)
    Sleep(200)
    OP_25(0x1E3, 0x3C)
    Sleep(200)
    OP_25(0x1E3, 0x46)
    Sleep(200)
    OP_25(0x1E3, 0x50)
    Sleep(200)
    OP_25(0x1E3, 0x5A)
    Sleep(200)
    OP_25(0x1E3, 0x64)
    Sleep(2000)
    StopSound(483, 500, 100)
    Sound(481, 0, 100, 0)
    Sleep(2500)
    Sound(484, 0, 70, 0)
    Sleep(500)
    Sound(477, 0, 60, 0)
    Sleep(5000)
    Sound(478, 0, 60, 0)
    Return()

    # Function_35_39BD end

    def Function_36_3A11(): pass

    label("Function_36_3A11")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch20600.itc", 0x1E)
    LoadChrToIndex("chr/ch20200.itc", 0x1F)
    LoadChrToIndex("chr/ch20300.itc", 0x20)
    LoadChrToIndex("chr/ch21600.itc", 0x21)
    LoadChrToIndex("chr/ch21300.itc", 0x22)
    LoadChrToIndex("chr/ch21200.itc", 0x23)
    LoadChrToIndex("chr/ch27700.itc", 0x24)
    LoadChrToIndex("chr/ch23600.itc", 0x25)
    ClearChrFlags(0x17, 0x80)
    OP_78(0x0, 0x17)
    OP_49()
    SetChrPos(0x17, -45000, -5500, -38200, 0)
    OP_D5(0x17, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x79, 0xB4, 0x0, 0x20)
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrChipByIndex(0x1A, 0x20)
    SetChrChipByIndex(0x1B, 0x21)
    SetChrChipByIndex(0x1C, 0x22)
    SetChrChipByIndex(0x1D, 0x23)
    SetChrChipByIndex(0x1E, 0x24)
    SetChrChipByIndex(0x1F, 0x25)
    SetChrSubChip(0x18, 0x0)
    SetChrSubChip(0x19, 0x0)
    SetChrSubChip(0x1A, 0x0)
    SetChrSubChip(0x1B, 0x0)
    SetChrSubChip(0x1C, 0x0)
    SetChrSubChip(0x1D, 0x0)
    SetChrSubChip(0x1E, 0x0)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    OP_A7(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x19, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x18, -7250, -4000, -40000, 180)
    SetChrPos(0x19, -7250, -4000, -40000, 180)
    SetChrPos(0x1A, -7250, -4000, -40000, 180)
    SetChrPos(0x1B, -7250, -4000, -40000, 180)
    SetChrPos(0x1C, -7250, -4000, -40000, 180)
    SetChrPos(0x1D, -7250, -4000, -40000, 180)
    SetChrPos(0x1E, -7250, -4000, -40000, 180)
    SetChrPos(0x1F, -7250, -4000, -40000, 180)
    SetChrFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    PlaceName2(340, 200, "c_plac20", 0x0, 3000)
    FadeToBright(2000, 0)
    OP_68(20240, -2400, -36530, 0)
    MoveCamera(334, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(64730, 0)
    OP_68(-1240, -2400, -36530, 15000)
    BeginChrThread(0x20, 1, 0, 38)

    def lambda_3CB2():
        OP_98(0xFE, 0x9C40, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3CB2)
    WaitChrThread(0x17, 1)
    OP_71(0x0, 0x5B, 0x78, 0x0, 0x0)
    Sound(478, 0, 100, 0)
    OP_79(0x0)
    OP_71(0x0, 0x12D, 0x168, 0x0, 0x20)
    OP_6F(0x1)
    EndChrThread(0x20, 0x1)
    OP_0D()
    Fade(1000)
    OP_68(-5240, -1300, -48610, 0)
    MoveCamera(327, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(31570, 0)
    OP_0D()
    OP_71(0x0, 0x1, 0x1E, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x0)
    OP_71(0x0, 0xF1, 0x12C, 0x0, 0x20)
    BeginChrThread(0x18, 3, 0, 37)
    Sleep(1000)
    BeginChrThread(0x19, 3, 0, 37)
    Sleep(1000)
    BeginChrThread(0x1A, 3, 0, 37)
    Sleep(1000)
    BeginChrThread(0x1B, 3, 0, 37)
    Sleep(1000)
    BeginChrThread(0x1C, 3, 0, 37)
    Sleep(1000)
    BeginChrThread(0x1D, 3, 0, 37)
    Sleep(1000)
    BeginChrThread(0x1E, 3, 0, 37)
    Sleep(1000)
    BeginChrThread(0x1F, 3, 0, 37)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventEnd(0x5)
    NewScene("t1030", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_36_3A11 end

    def Function_37_3DA4(): pass

    label("Function_37_3DA4")


    def lambda_3DA9():
        OP_95(0xFE, -7250, -4000, -50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3DA9)
    Sleep(500)

    def lambda_3DC6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3DC6)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_3DDF():
        OP_95(0xFE, 7250, -4000, -50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3DDF)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_37_3DA4 end

    def Function_38_3DF9(): pass

    label("Function_38_3DF9")

    Sleep(1000)
    Sound(475, 0, 100, 0)
    Sleep(1500)
    Sound(477, 0, 100, 0)
    Sleep(4000)
    Sound(476, 0, 100, 0)
    Sleep(1000)
    Sound(477, 0, 100, 0)
    Return()

    # Function_38_3DF9 end

    def Function_39_3E1E(): pass

    label("Function_39_3E1E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(479)
    ClearChrFlags(0x17, 0x80)
    OP_78(0x0, 0x17)
    OP_49()
    SetChrPos(0x17, -5000, -5500, -38200, 0)
    OP_D5(0x17, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    OP_74(0x0, 0x1E)
    OP_70(0x0, 0x0)
    Sound(475, 0, 100, 0)
    OP_68(1000, -500, -38550, 0)
    MoveCamera(315, 17, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(35000, 0)
    MoveCamera(325, 17, 0, 4500)
    Sound(477, 0, 100, 0)
    Sound(479, 2, 100, 0)
    SetChrPos(0x17, -5000, -5500, -38200, 0)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_3EDA():
        OP_98(0xFE, 0xFFFFD120, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3EDA)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x17, 0x1)
    SetMapObjFlags(0x0, 0x4)
    StopBGM(0xFA0)
    StopSound(479, 3000, 100)
    StopSound(126, 3000, 80)
    WaitBGM()
    SetScenarioFlags(0x22, 1)
    NewScene("c1200", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_39_3E1E end

    def Function_40_3F26(): pass

    label("Function_40_3F26")

    Sleep(1000)

    label("loc_3F29")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3F4B")
    Sound(918, 0, 30, 0)
    Sleep(2200)
    Sound(918, 0, 20, 0)
    Sleep(5000)
    Jump("loc_3F29")

    label("loc_3F4B")

    Return()

    # Function_40_3F26 end

    def Function_41_3F4C(): pass

    label("Function_41_3F4C")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Crossbell City-Bound Water Bus - Schedule\x01\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_41_3F4C end

    def Function_42_3FB2(): pass

    label("Function_42_3FB2")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4063")

    ChrTalk(
        0x101,
        "#00005FThis red orbal boat...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FYes, it's probably the\x01",
            "one Arios came on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...Anyway, we've got to\x01",
            "hurry and chase after\x01",
            "him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_409D")

    label("loc_4063")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A red orbal boat is\x01",
            "anchored here.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_409D")

    EventEnd(0x3)
    Return()

    # Function_42_3FB2 end

    SaveToFile()

Try(main)
