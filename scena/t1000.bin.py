﻿from ScenarioHelper import *

def main():
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
        "tourist",                 # 1
        "tourist",                 # 2
        "tourist",                 # 3
        "tourist",                 # 4
        "tourist",                 # 5
        "tourist",                 # 6
        "Crew salsa",           # 7
        "Lisha",               # 8
        "Keya",                 # 9
        "Franc",                 # 10
        "Cecil",                 # 11
        "Ilia",                 # 12
        "Shuri",                 # 13
        "Marybele",             # 14
        "Zeit",               # 15
        "Water-bus",               # 16
        "passenger",                   # 17
        "passenger",                   # 18
        "passenger",                   # 19
        "passenger",                   # 20
        "passenger",                   # 21
        "passenger",                   # 22
        "passenger",                   # 23
        "passenger",                   # 24
        "SE control",                 # 25
        "boat",                 # 26
        "boat",                 # 27
        "Direction to the theme park",       # 28
        "Destination towards a mansion",               # 29
        "To the lake bath area",           # 30
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

    PlaceName(-5.0, 0.0, 95.0, 0x0000, 0x0000, "Direction to the theme park")
    PlaceName(-95.0, 0.0, 20.0, 0x0000, 0x0000, "Destination towards a mansion")
    PlaceName(75.0, 0.0, 15.0, 0x0000, 0x0000, "To the lake bath area")
    PlaceName(1.0, 0.0, 17.5, 0x0000, 0x0052, "")

    ChipFrameInfo(1296, 0)                                       # 0

    ScpFunction((
        "Function_0_510",          # 00, 0
        "Function_1_5C0",          # 01, 1
        "Function_2_5EB",          # 02, 2
        "Function_3_721",          # 03, 3
        "Function_4_8DF",          # 04, 4
        "Function_5_964",          # 05, 5
        "Function_6_A02",          # 06, 6
        "Function_7_A86",          # 07, 7
        "Function_8_B16",          # 08, 8
        "Function_9_BFB",          # 09, 9
        "Function_10_C83",         # 0A, 10
        "Function_11_D2B",         # 0B, 11
        "Function_12_DDE",         # 0C, 12
        "Function_13_1253",        # 0D, 13
        "Function_14_129E",        # 0E, 14
        "Function_15_1372",        # 0F, 15
        "Function_16_2D35",        # 10, 16
        "Function_17_2D9D",        # 11, 17
        "Function_18_2DD1",        # 12, 18
        "Function_19_2E11",        # 13, 19
        "Function_20_2E51",        # 14, 20
        "Function_21_2E91",        # 15, 21
        "Function_22_2ED1",        # 16, 22
        "Function_23_2F11",        # 17, 23
        "Function_24_2F51",        # 18, 24
        "Function_25_2F91",        # 19, 25
        "Function_26_2FA7",        # 1A, 26
        "Function_27_35B6",        # 1B, 27
        "Function_28_36B4",        # 1C, 28
        "Function_29_376C",        # 1D, 29
        "Function_30_3781",        # 1E, 30
        "Function_31_37E1",        # 1F, 31
        "Function_32_382F",        # 20, 32
        "Function_33_387D",        # 21, 33
        "Function_34_38CB",        # 22, 34
        "Function_35_3919",        # 23, 35
        "Function_36_396D",        # 24, 36
        "Function_37_3D00",        # 25, 37
        "Function_38_3D55",        # 26, 38
        "Function_39_3D7A",        # 27, 39
        "Function_40_3E82",        # 28, 40
        "Function_41_3EA8",        # 29, 41
        "Function_42_3F3B",        # 2A, 42
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
    Jump("loc_9FE")

    label("loc_975")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_9F5")

    ChrTalk(
        0x8,
        (
            "Somewhat, while looking at the lake\x01",
            "Waiting is also a fun day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I was a bit tired of walking around,\x01",
            "Let's wait here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9FE")

    label("loc_9F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_9FE")

    label("loc_9FE")

    TalkEnd(0xFE)
    Return()

    # Function_5_964 end

    def Function_6_A02(): pass

    label("Function_6_A02")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_A13")
    Jump("loc_A82")

    label("loc_A13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_A79")

    ChrTalk(
        0x9,
        (
            "The water bus is still\x01",
            "It seems they have not come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "After all it is a bit more\x01",
            "Let's play around.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A82")

    label("loc_A79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_A82")

    label("loc_A82")

    TalkEnd(0xFE)
    Return()

    # Function_6_A02 end

    def Function_7_A86(): pass

    label("Function_7_A86")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_A97")
    Jump("loc_B12")

    label("loc_A97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_AA5")
    Jump("loc_B12")

    label("loc_AA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_B12")

    ChrTalk(
        0xA,
        "Hey, if you are … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "When I got on board\x01",
            "To become anxious\x01",
            "Do not tell me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B12")

    TalkEnd(0xFE)
    Return()

    # Function_7_A86 end

    def Function_8_B16(): pass

    label("Function_8_B16")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_B27")
    Jump("loc_BF7")

    label("loc_B27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_B96")

    ChrTalk(
        0xB,
        (
            "From the bustle of Michelin\x01",
            "I want to be separated for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "This place is a nice place, do not heal …\x02",
    )

    CloseMessageWindow()
    Jump("loc_BF7")

    label("loc_B96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_BF7")

    ChrTalk(
        0xB,
        (
            "Well, to the hotel\x01",
            "Do you have anything left behind?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "…… Not, it's a hassle.\x01",
            "………………maybe.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BF7")

    TalkEnd(0xFE)
    Return()

    # Function_8_B16 end

    def Function_9_BFB(): pass

    label("Function_9_BFB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_C0C")
    Jump("loc_C7F")

    label("loc_C0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_C1A")
    Jump("loc_C7F")

    label("loc_C1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_C7F")

    ChrTalk(
        0xC,
        (
            "With a boyfriend\x01",
            "It was straying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well ~, come quickly\x01",
            "Because I'm going home earlier.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C7F")

    TalkEnd(0xFE)
    Return()

    # Function_9_BFB end

    def Function_10_C83(): pass

    label("Function_10_C83")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_C94")
    Jump("loc_D27")

    label("loc_C94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_CA2")
    Jump("loc_D27")

    label("loc_CA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_D27")

    ChrTalk(
        0xD,
        (
            "Girlfriend first\x01",
            "It seems I went.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Oh ~, I wonder where they went.\x01",
            "I have to find it before the water bus leaves ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D27")

    TalkEnd(0xFE)
    Return()

    # Function_10_C83 end

    def Function_11_D2B(): pass

    label("Function_11_D2B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_D3C")
    Jump("loc_DDA")

    label("loc_D3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_D4A")
    Jump("loc_DDA")

    label("loc_D4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_DD1")

    ChrTalk(
        0xE,
        (
            "The water bus will soon\x01",
            "Towards the crossbar departure\x01",
            "I will leave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "When you ride,\x01",
            "Please boarding as soon as possible.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DDA")

    label("loc_DD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_DDA")

    label("loc_DDA")

    TalkEnd(0xFE)
    Return()

    # Function_11_D2B end

    def Function_12_DDE(): pass

    label("Function_12_DDE")

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
        "#01803F………… …………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005F… …. Lisha?\x01",
            "Have you been in such a place?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xF, 0x5A, 0x1F4)

    ChrTalk(
        0xF,
        "#01805FMr. Lloyd, Kia-chan ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01105FHey Lisha,\x01",
            "How are you doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FIs it also a matter of trouble?\x01",
            "If I am OK … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01809FOh yeah, that's a big deal ….\x02\x03",
            "#01804FEven outside the entertainment district\x01",
            "There are lively places,\x01",
            "I am a bit tired.\x02\x03",
            "#01802FBut, if I hit the wind here\x01",
            "I was relieved a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00003FWell … I wish I could.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01108FLisha, you really okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01809FYeah, it's already fine.\x02\x03",
            "#01803FWell then, Mr. Lloyd.\x01",
            "I am with the Iria's place\x01",
            "I am going.\x02\x03",
            "#01802FTo meet you with you guys\x01",
            "I will go with you.\x01",
            "please do not worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FOh, ah ……\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xF, 0x40)
    OP_68(-7800, -800, -26950, 4000)
    BeginChrThread(0xF, 3, 0, 13)
    Sleep(300)

    def lambda_1158():

        label("loc_1158")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_1158")

    QueueWorkItem2(0x101, 2, lambda_1158)

    def lambda_116A():

        label("loc_116A")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_116A")

    QueueWorkItem2(0x153, 2, lambda_116A)
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
        "#01105FWhat is wrong, Lloyd?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x153, 500)

    ChrTalk(
        0x101,
        (
            "#6P#00003F… Well, nothing.\x02\x03",
            "#00000FShall we go soon?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x15A, 5)
    SetChrPos(0x0, -8850, -2000, -26600, 270)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_12_DDE end

    def Function_13_1253(): pass

    label("Function_13_1253")

    OP_93(0xFE, 0x2D, 0x1F4)

    def lambda_125F():
        OP_95(0xFE, -8610, -2000, -24800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_125F)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x0)

    def lambda_1284():
        OP_95(0xFE, -610, -2000, -24800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1284)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_13_1253 end

    def Function_14_129E(): pass

    label("Function_14_129E")

    EventBegin(0x1)
    Sound(2094, 255, 100, 0)

    ChrTalk(
        0x101,
        "#0000FI'm going to catch you here.\x02",
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
            "Do you fish?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "To fish\x01",      # 0
            "quit\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_136D")
    OP_E2(0x2)
    MiniGame(0x6, 0x5, 0x5B9A, 0xFFFFEC78, 0xFFFF296E, 0x5A, 0x72C4, 0xFFFFE890, 0xFFFF277A)

    label("loc_136D")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_14_129E end

    def Function_15_1372(): pass

    label("Function_15_1372")

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
            "#00002F#6PWell ……\x01",
            "Surely Mr. Marybele\x01",
            "Are you waiting for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#11PYeah, I will meet you at 9:30.\x01",
            "It should be just time ….\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearChrFlags(0x11, 0x8)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x11,
        "Daughter's voice",
        "#2713V#1P#30WOh, came and came ~!\x02",
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
        "#00005F#6PThis voice ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10111F#11PWell, no way …! Is it?\x02",
    )

    CloseMessageWindow()

    def lambda_1C73():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1C73)
    Sleep(50)

    def lambda_1C83():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1C83)
    Sleep(50)

    def lambda_1C93():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1C93)
    Sleep(50)

    def lambda_1CA3():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1CA3)
    Sleep(50)

    def lambda_1CB3():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1CB3)
    Sleep(50)

    def lambda_1CC3():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_1CC3)
    Sleep(50)

    def lambda_1CD3():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_1CD3)
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

    def lambda_1D43():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1D43)
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
            "#2714V#30WOnee, everyone,\x01",
            "Good morning!\x02\x03",
            "#2715V#30WKa'a-chan, good morning ~!\x02",
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
        "#01109F#6Pgood morning!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305F#6POh, Fran?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#5PHow, why are you here …?\x02\x03",
            "#10101FWhen I saw you yesterday,\x01",
            "You did not say that! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#06409F#11PWell, my older sisters\x01",
            "Make it surprised ~.\x02\x03",
            "#06402FAnd special guests\x01",
            "I'm not alone.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x13, 0x8)
    ClearChrFlags(0x12, 0x8)
    ClearChrFlags(0xF, 0x8)
    ClearChrFlags(0x14, 0x8)

    NpcTalk(
        0x12,
        "Female voice",
        "#1PHe seems to have come.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x13,
        "Female voice",
        (
            "#1PAlright, we also got all the items\x01",
            "I think I can enjoy it today ~!\x02",
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
        "#00005F#6PWhat! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#6PHere, this voice ……\x02",
    )

    CloseMessageWindow()
    OP_68(-5400, -3000, -50350, 3000)

    def lambda_218F():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_218F)
    Sleep(100)

    def lambda_21A7():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_21A7)
    Sleep(100)

    def lambda_21BF():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_21BF)
    Sleep(100)

    def lambda_21D7():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_21D7)
    WaitChrThread(0x13, 1)

    ChrTalk(
        0x101,
        "#00011F#6PIt is! Is it?\x02",
    )

    WaitChrThread(0x12, 1)
    WaitChrThread(0xF, 1)
    WaitChrThread(0x14, 1)
    OP_6F(0x79)
    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00307F#6POhhhhhhhhhhh! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#01110F#6POh, Cecil!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#6PAnd to Iria's … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#6PWell, beautiful place\x01",
            "You are gathering.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#6PHere, what is likely to do this …\x02\x03",
            "#00101F─ ─ Bell, you do! Is it?\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x15, 0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_END)), "loc_2357")
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x15,
        "Female voice",
        "#3774V#1P#30WUhufu - That's correct.\x02",
    )

    CloseMessageWindow()
    OP_24(0xEBE)
    OP_C9(0x1, 0x80000000)
    Jump("loc_237F")

    label("loc_2357")


    NpcTalk(
        0x15,
        "Female voice",
        "#1PUhufu - That's correct.\x02",
    )

    CloseMessageWindow()

    label("loc_237F")

    OP_68(-4680, -3000, -50240, 2500)

    def lambda_2395():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2395)
    WaitChrThread(0x15, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00012F#6PMr. Maria Bell ……\x01",
            "What on earth is this?\x02",
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
            "Huff, as I invited you all\x01",
            "People who hear that they are on good terms with each other\x01",
            "I called you.\x02\x03",
            "Alkan Shell's people\x01",
            "Renewal performance beginning next month\x01",
            "I also serve as encouragement, though.\x02",
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
        "My brother, you guys.\x02",
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
            "Heh.\x01",
            "It has been a long time since I was away.\x02",
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
        "Why, why … me.\x02",
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
            "#00012F#6Pmy mother……\x01",
            "What should I say?\x02\x03",
            "#00002FCecil elder sister, was he able to take a vacation?\x02",
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
            "Yeah, where I accidentally took it\x01",
            "Ilia contacts me ……\x02\x03",
            "Because the lloyds will come\x01",
            "I got used to speechless words.\x02\x03",
            "I wonder if it was annoying?\x02",
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
        "#00009F#6PNo … I am very happy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00307F#6POooooooooooo!\x01",
            "I am watching a dream, too! Is it?\x02\x03",
            "#00306FTo Ms. Iria for Cecil\x01",
            "There are so many beautiful places ……\x02\x03",
            "#00309FHappy New Year!\x01",
            "Tension MAX!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00211F#5PRandy and Uzzai.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10304F#6PWell, I know the feeling.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10112F#6PBut, I was a little surprised … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#6PThere is also a place to stay\x01",
            "Did you prepare it for the same hotel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#02904F#11PYeah, your room is\x01",
            "On the VIP floor of Hotel 3F\x01",
            "I am preparing.\x02\x03",
            "First we will show you around the room\x01",
            "You'd better leave your luggage.\x02\x03",
            "#02902FAfter that, at the Michelin Resort\x01",
            "I hope you go to a new eyeball.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#6PNew eyeball … …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#6PIs not it a theme park?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#06409F#11PEven, I heard it\x01",
            "I was surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01802F#11PActually, that new facility\x01",
            "He seems to have opened … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01709F#11PIt is reserved to noon until noon\x01",
            "It seems to be doing it ~!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#02904F#11PYeah, by all means by all means\x01",
            "I want to have fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#01105F#6PFlute ~ …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#6PUm?\x01",
            "That facility is one ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#02912F#11PUfufu …\x01",
            "For inland crossbells\x01",
            "Paradise that I brought up#4RParadise#… ….\x02\x03",
            "#02909FFacing the beautiful Elm lake\x01",
            "Pure white \"Lake bathing area#8RLake beach#That's it.\x02",
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

    # Function_15_1372 end

    def Function_16_2D35(): pass

    label("Function_16_2D35")

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

    # Function_16_2D35 end

    def Function_17_2D9D(): pass

    label("Function_17_2D9D")


    def lambda_2DA2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2DA2)
    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x9C4, 0x1)
    OP_9B(0x0, 0xFE, 0xFFA6, 0x3A98, 0x9C4, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_17_2D9D end

    def Function_18_2DD1(): pass

    label("Function_18_2DD1")


    def lambda_2DD6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2DD6)
    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x9C4, 0x1)
    OP_95(0xFE, -7250, -4000, -52000, 2500, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_18_2DD1 end

    def Function_19_2E11(): pass

    label("Function_19_2E11")


    def lambda_2E16():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2E16)
    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x9C4, 0x1)
    OP_95(0xFE, -6250, -4000, -49500, 2500, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_19_2E11 end

    def Function_20_2E51(): pass

    label("Function_20_2E51")


    def lambda_2E56():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2E56)
    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x9C4, 0x1)
    OP_95(0xFE, -7250, -4000, -50000, 2500, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_20_2E51 end

    def Function_21_2E91(): pass

    label("Function_21_2E91")


    def lambda_2E96():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2E96)
    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x9C4, 0x1)
    OP_95(0xFE, -8750, -4000, -51000, 2500, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_21_2E91 end

    def Function_22_2ED1(): pass

    label("Function_22_2ED1")


    def lambda_2ED6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2ED6)
    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x9C4, 0x1)
    OP_95(0xFE, -7750, -4000, -48500, 2500, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_22_2ED1 end

    def Function_23_2F11(): pass

    label("Function_23_2F11")


    def lambda_2F16():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2F16)
    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x9C4, 0x1)
    OP_95(0xFE, -8750, -4000, -49000, 2500, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_23_2F11 end

    def Function_24_2F51(): pass

    label("Function_24_2F51")


    def lambda_2F56():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2F56)
    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x9C4, 0x1)
    OP_95(0xFE, -6250, -4000, -51500, 2500, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_24_2F51 end

    def Function_25_2F91(): pass

    label("Function_25_2F91")

    Sound(475, 0, 100, 0)
    Sleep(1000)
    Sound(477, 0, 100, 0)
    Sound(476, 0, 100, 0)
    Return()

    # Function_25_2F91 end

    def Function_26_2FA7(): pass

    label("Function_26_2FA7")

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
        "#00201F#11P#NThe sound of a bell…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3345")

    ChrTalk(
        0x101,
        (
            "#00011F#5P#Nthis is……\x01",
            "Have you been on the top floor of \"Mirror Castle\"?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#00101F#5P#NYes, seems like it\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_33AA")

    label("loc_3345")


    ChrTalk(
        0x102,
        (
            "#00101F#5P#Nthis is……\x01",
            "The bell on the \"mirror of castle\"?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00001F#5P#NIs there such a thing ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_33AA")


    ChrTalk(
        0x104,
        (
            "#00306F#5P#NThere is something in the water\x01",
            "Bonjari shimmer … …\x02\x03",
            "#00301FTiossuke, you have any idea?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00203F#11P#NApparently something like \"spirit pressure\"\x01",
            "It seems to be increasing …\x02\x03",
            "#00201FIt is also in the back\x01",
            "From the theme park direction.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00003F#5P#NIs that right\x02\x03",
            "#00013FArios on them\x01",
            "It seems likely that you headed for it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#00107F#5P#NYes, let's check it out!\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x94, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3577")
    Jump("loc_357C")

    label("loc_3577")

    OP_29(0x94, 0x4, 0x40)

    label("loc_357C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x95, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_358D")
    Jump("loc_3592")

    label("loc_358D")

    OP_29(0x95, 0x4, 0x40)

    label("loc_3592")

    OP_C9(0x1, 0x10000)
    OP_50(0x52, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x21, 5)
    OP_32(0xFF, 0xFF, 0x0)
    OP_66(0x2, 0x1)
    OP_24(0x1E3)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_26_2FA7 end

    def Function_27_35B6(): pass

    label("Function_27_35B6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_36B3")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_360F")
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 0, -5500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(333)
    Jump("loc_36AE")

    label("loc_360F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_365D")
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 0, -5500, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(233)
    Jump("loc_36AE")

    label("loc_365D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36AB")
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 0, -5500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(233)
    Jump("loc_36AE")

    label("loc_36AB")

    Sleep(233)

    label("loc_36AE")

    Jump("Function_27_35B6")

    label("loc_36B3")

    Return()

    # Function_27_35B6 end

    def Function_28_36B4(): pass

    label("Function_28_36B4")

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

    # Function_28_36B4 end

    def Function_29_376C(): pass

    label("Function_29_376C")

    OP_96(0xFE, 0x445C, 0xFFFFEE08, 0xFFFF1C76, 0x7D0, 0x0)
    Return()

    # Function_29_376C end

    def Function_30_3781(): pass

    label("Function_30_3781")

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

    # Function_30_3781 end

    def Function_31_37E1(): pass

    label("Function_31_37E1")

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

    # Function_31_37E1 end

    def Function_32_382F(): pass

    label("Function_32_382F")

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

    # Function_32_382F end

    def Function_33_387D(): pass

    label("Function_33_387D")

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

    # Function_33_387D end

    def Function_34_38CB(): pass

    label("Function_34_38CB")

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

    # Function_34_38CB end

    def Function_35_3919(): pass

    label("Function_35_3919")

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

    # Function_35_3919 end

    def Function_36_396D(): pass

    label("Function_36_396D")

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

    def lambda_3C0E():
        OP_98(0xFE, 0x9C40, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3C0E)
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

    # Function_36_396D end

    def Function_37_3D00(): pass

    label("Function_37_3D00")


    def lambda_3D05():
        OP_95(0xFE, -7250, -4000, -50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D05)
    Sleep(500)

    def lambda_3D22():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3D22)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_3D3B():
        OP_95(0xFE, 7250, -4000, -50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D3B)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_37_3D00 end

    def Function_38_3D55(): pass

    label("Function_38_3D55")

    Sleep(1000)
    Sound(475, 0, 100, 0)
    Sleep(1500)
    Sound(477, 0, 100, 0)
    Sleep(4000)
    Sound(476, 0, 100, 0)
    Sleep(1000)
    Sound(477, 0, 100, 0)
    Return()

    # Function_38_3D55 end

    def Function_39_3D7A(): pass

    label("Function_39_3D7A")

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

    def lambda_3E36():
        OP_98(0xFE, 0xFFFFD120, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3E36)
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

    # Function_39_3D7A end

    def Function_40_3E82(): pass

    label("Function_40_3E82")

    Sleep(1000)

    label("loc_3E85")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3EA7")
    Sound(918, 0, 30, 0)
    Sleep(2200)
    Sound(918, 0, 20, 0)
    Sleep(5000)
    Jump("loc_3E85")

    label("loc_3EA7")

    Return()

    # Function_40_3E82 end

    def Function_41_3EA8(): pass

    label("Function_41_3EA8")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Water crossing bus · timetable to \"Crossbell City\"\x01\x01",
            "※ For further visit\x01",
            "We are waiting for you!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_41_3EA8 end

    def Function_42_3F3B(): pass

    label("Function_42_3F3B")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4002")

    ChrTalk(
        0x101,
        "#00005FThis red guiding boat ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FYeah, Mr. Arios\x01",
            "Probably due to what I got on board\x01",
            "There is no doubt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F……Anyways,\x01",
            "I should hurry and chase after.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4038")

    label("loc_4002")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Red guiding boat is moored.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_4038")

    EventEnd(0x3)
    Return()

    # Function_42_3F3B end

    SaveToFile()

Try(main)
