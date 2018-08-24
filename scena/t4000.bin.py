from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t4000.bin",                # FileName
        "t4000",                    # MapName
        "t4000",                    # Location
        0x005D,                     # MapIndex
        "ed7124",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x01,                       # PlaceNameNumber
        0x1F,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 93, 0, 4, 0, 5],
    )

    BuildStringList((
        "t4000",                  # 0
        "Sister Ries",            # 1
        "Priest Roland",          # 2
        "Sister Juju",            # 3
        "Tamil",                  # 4
        "Hamil",                  # 5
        "Pluna",                  # 6
        "Lenalee",                # 7
        "Burick",                 # 8
        "Lawyer Ian",             # 9
        "Mainz Mountain Road",    # 10
    ))

    AddCharChip((
        "chr/ch14000.itc",                   # 00
        "chr/ch25400.itc",                   # 01
        "chr/ch25500.itc",                   # 02
        "chr/ch23800.itc",                   # 03
        "chr/ch20500.itc",                   # 04
        "chr/ch22100.itc",                   # 05
        "chr/ch20400.itc",                   # 06
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

    DeclNpc(4294957897, 500,     14000,   90,   389,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(4294964666, 0,       9369,    180,  257,  0x0, 0,   1,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(2299,    0,       14270,   180,  257,  0x0, 0,   2,   0,   0,   1,   0,   8,   255,  0)
    DeclNpc(4294961516, 0,       14529,   180,  385,  0x0, 0,   3,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(4294961516, 0,       13680,   0,    385,  0x0, 0,   3,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(5809,    0,       19469,   90,   385,  0x0, 0,   4,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(7619,    0,       19180,   270,  385,  0x0, 0,   5,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(4294963656, 2000,    31379,   135,  385,  0x0, 0,   6,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(4294956906, 500,     13820,   1200,    4294956906, 2000,    13820,   0x007C, 0,  24, 0x0000)

    PlaceName(5.0, -0.0, -35.0, 0x0000, 0x0000, "Mainz Mountain Road")

    ChipFrameInfo(680, 0)                                        # 0

    ScpFunction((
        "Function_0_2A8",          # 00, 0
        "Function_1_358",          # 01, 1
        "Function_2_4A9",          # 02, 2
        "Function_3_50A",          # 03, 3
        "Function_4_56B",          # 04, 4
        "Function_5_88F",          # 05, 5
        "Function_6_997",          # 06, 6
        "Function_7_9D8",          # 07, 7
        "Function_8_1ECB",         # 08, 8
        "Function_9_2CDA",         # 09, 9
        "Function_10_2DD9",        # 0A, 10
        "Function_11_30B8",        # 0B, 11
        "Function_12_323A",        # 0C, 12
        "Function_13_3818",        # 0D, 13
        "Function_14_38F2",        # 0E, 14
        "Function_15_39D2",        # 0F, 15
        "Function_16_3B4C",        # 10, 16
        "Function_17_4381",        # 11, 17
        "Function_18_4401",        # 12, 18
        "Function_19_4576",        # 13, 19
        "Function_20_45B9",        # 14, 20
        "Function_21_4783",        # 15, 21
        "Function_22_5C40",        # 16, 22
        "Function_23_5F53",        # 17, 23
        "Function_24_61AE",        # 18, 24
        "Function_25_6243",        # 19, 25
    ))


    def Function_0_2A8(): pass

    label("Function_0_2A8")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_2E0"),
        (1, "loc_2EC"),
        (2, "loc_2F8"),
        (3, "loc_304"),
        (4, "loc_310"),
        (5, "loc_31C"),
        (6, "loc_328"),
        (SWITCH_DEFAULT, "loc_334"),
    )


    label("loc_2E0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_340")

    label("loc_2EC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_340")

    label("loc_2F8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_340")

    label("loc_304")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_340")

    label("loc_310")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_340")

    label("loc_31C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_340")

    label("loc_328")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_340")

    label("loc_334")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_340")

    label("loc_340")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_357")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_340")

    label("loc_357")

    Return()

    # Function_0_2A8 end

    def Function_1_358(): pass

    label("Function_1_358")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A8")
    OP_95(0xFE, -2510, 0, 14270, 2000, 0x0)
    OP_95(0xFE, -2510, 0, 12920, 2000, 0x0)
    OP_95(0xFE, 11020, 0, 12920, 2000, 0x0)
    OP_95(0xFE, 18830, 0, 20000, 2000, 0x0)
    OP_95(0xFE, 18830, 0, 24520, 2000, 0x0)
    OP_95(0xFE, 26350, 0, 31740, 2000, 0x0)
    OP_95(0xFE, 26350, 0, 46780, 2000, 0x0)
    OP_95(0xFE, 23030, 0, 51110, 2000, 0x0)
    OP_95(0xFE, 23030, 0, 54060, 2000, 0x0)
    OP_95(0xFE, 21080, 0, 54060, 2000, 0x0)
    OP_95(0xFE, 21080, 0, 48950, 2000, 0x0)
    OP_95(0xFE, 25050, 0, 44720, 2000, 0x0)
    OP_95(0xFE, 25050, 0, 34580, 2000, 0x0)
    OP_95(0xFE, 17430, 0, 27090, 2000, 0x0)
    OP_95(0xFE, 17430, 0, 21180, 2000, 0x0)
    OP_95(0xFE, 9240, 0, 14270, 2000, 0x0)
    Jump("Function_1_358")

    label("loc_4A8")

    Return()

    # Function_1_358 end

    def Function_2_4A9(): pass

    label("Function_2_4A9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_509")
    OP_95(0xFE, 23000, 0, 42000, 6000, 0x0)
    OP_95(0xFE, 19000, 0, 42000, 6000, 0x0)
    OP_95(0xFE, 19000, 0, 39000, 6000, 0x0)
    OP_95(0xFE, 23000, 0, 39000, 6000, 0x0)
    Jump("Function_2_4A9")

    label("loc_509")

    Return()

    # Function_2_4A9 end

    def Function_3_50A(): pass

    label("Function_3_50A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_56A")
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(100)
    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(100)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(100)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(100)
    Jump("Function_3_50A")

    label("loc_56A")

    Return()

    # Function_3_50A end

    def Function_4_56B(): pass

    label("Function_4_56B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5C1")
    SetChrPos(0xA, -6830, 0, 14190, 90)
    BeginChrThread(0xA, 0, 0, 0)
    OP_93(0xB, 0x10E, 0x0)
    OP_93(0xC, 0x10E, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B2")
    SetChrFlags(0xB, 0x10)

    label("loc_5B2")

    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xA, 0x10)
    Jump("loc_861")

    label("loc_5C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5CF")
    Jump("loc_861")

    label("loc_5CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5FB")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F6")
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)

    label("loc_5F6")

    Jump("loc_861")

    label("loc_5FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_620")
    SetChrPos(0xA, -1840, 2000, 32590, 180)
    BeginChrThread(0xA, 0, 0, 0)
    Jump("loc_861")

    label("loc_620")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_62E")
    Jump("loc_861")

    label("loc_62E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_641")
    SetChrFlags(0xA, 0x80)
    Jump("loc_861")

    label("loc_641")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_69E")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xA, 21060, 0, 40570, 90)
    BeginChrThread(0xA, 0, 0, 3)
    SetChrPos(0xB, 23000, 0, 41500, 0)
    SetChrPos(0xC, 23000, 0, 39000, 0)
    BeginChrThread(0xC, 0, 0, 2)
    BeginChrThread(0xB, 0, 0, 2)
    Jump("loc_861")

    label("loc_69E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6C0")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)
    Jump("loc_861")

    label("loc_6C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_6D3")
    SetChrFlags(0xA, 0x80)
    Jump("loc_861")

    label("loc_6D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_6FA")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)
    Jump("loc_861")

    label("loc_6FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_721")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)
    Jump("loc_861")

    label("loc_721")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_739")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_861")

    label("loc_739")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_788")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 23000, 0, 41500, 180)
    SetChrPos(0xA, 23000, 0, 39000, 0)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_861")

    label("loc_788")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7E3")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xB, 11860, 0, 22480, 270)
    SetChrPos(0xA, 10060, 0, 21470, 90)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrPos(0xC, 13660, 0, 23480, 135)
    Jump("loc_861")

    label("loc_7E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_7F6")
    SetChrFlags(0xA, 0x80)
    Jump("loc_861")

    label("loc_7F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_83B")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_81D")
    SetChrFlags(0xD, 0x10)

    label("loc_81D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82C")
    SetChrFlags(0xE, 0x10)

    label("loc_82C")

    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_861")

    label("loc_83B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_858")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)
    Jump("loc_861")

    label("loc_858")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_861")

    label("loc_861")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_874")
    ClearChrFlags(0x8, 0x80)

    label("loc_874")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_88E")
    SetMapFlags(0x10000000)
    Event(0, 21)

    label("loc_88E")

    Return()

    # Function_4_56B end

    def Function_5_88F(): pass

    label("Function_5_88F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_913")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x5A, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_913")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_92A")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    Jump("loc_92A")

    label("loc_92A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_956")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xDC, 0xB4, 0xA0, 0x1E, 0x64, 0x0)
    Jump("loc_97D")

    label("loc_956")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_97D")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xDC, 0xB4, 0xA0, 0x1E, 0x64, 0x0)

    label("loc_97D")

    ClearMapObjFlags(0x1, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_996")
    OP_1B(0x0, 0x0, 0x19)

    label("loc_996")

    Return()

    # Function_5_88F end

    def Function_6_997(): pass

    label("Function_6_997")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9A9")
    Call(0, 22)
    Return()

    label("loc_9A9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_9BA")
    Jump("loc_9D4")

    label("loc_9BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_9C8")
    Jump("loc_9D4")

    label("loc_9C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_9D4")
    Call(0, 10)

    label("loc_9D4")

    TalkEnd(0xFE)
    Return()

    # Function_6_997 end

    def Function_7_9D8(): pass

    label("Function_7_9D8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B21")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB2")

    ChrTalk(
        0xFE,
        (
            "That faintly shining tree... I\x01",
            "wonder what could have caused\x01",
            "it to appear in Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Will it bring light to this land\x01",
            "or will it bring disaster...? We\x01",
            "clergymen cannot say.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B1C")

    label("loc_AB2")


    ChrTalk(
        0xFE,
        (
            "That faintly shining\x01",
            "tree, what could it\x01",
            "be...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if this too is\x01",
            "the will of the Goddess?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B1C")

    Jump("loc_1EC7")

    label("loc_B21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_C44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BFD")

    ChrTalk(
        0xFE,
        (
            "When that barrier vanished all of a\x01",
            "sudden, it seems that armored monsters\x01",
            "began to wander throughout the city...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If this was President\x01",
            "Dieter's idea as well,\x01",
            "I'll never forgive him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C3F")

    label("loc_BFD")


    ChrTalk(
        0xFE,
        (
            "Making monsters wander\x01",
            "the city... It's an\x01",
            "unforgivable act.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C3F")

    Jump("loc_1EC7")

    label("loc_C44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_DA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D24")

    ChrTalk(
        0xFE,
        (
            "It appears Mr. Crois\x01",
            "made a speech in the\x01",
            "city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if confusion throughout the\x01",
            "continent due to Crossbell's\x01",
            "independence can be avoided somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "O Goddess, guide the\x01",
            "people...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D9F")

    label("loc_D24")


    ChrTalk(
        0xFE,
        (
            "Dear me, I wonder if a\x01",
            "conflict between the Empire\x01",
            "and Republic can be avoided...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "O Goddess, guide the\x01",
            "people...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D9F")

    Jump("loc_1EC7")

    label("loc_DA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_F06")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E8A")

    ChrTalk(
        0xFE,
        (
            "Today, we're holding\x01",
            "mass in the cathedral\x01",
            "chapel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is where we pray for the\x01",
            "Goddess to give her guidance to\x01",
            "those who died in the attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you have time, please\x01",
            "attend too, everyone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F01")

    label("loc_E8A")


    ChrTalk(
        0xFE,
        (
            "Many visitors came to\x01",
            "mass today to mourn over\x01",
            "the attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you have time, please\x01",
            "attend too, everyone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_F01")

    Jump("loc_1EC7")

    label("loc_F06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_104E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FB6")

    ChrTalk(
        0xFE,
        (
            "Gunshots and explosions\x01",
            "sounds have been frequently\x01",
            "heard since last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It appears that the\x01",
            "fight in Mainz has\x01",
            "become quite intense...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1049")

    label("loc_FB6")


    ChrTalk(
        0xFE,
        (
            "In any case... It can't be\x01",
            "said that the armed group\x01",
            "won't come here as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We must urgently\x01",
            "consider this to protect\x01",
            "the cathedral...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1049")

    Jump("loc_1EC7")

    label("loc_104E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_10E9")

    ChrTalk(
        0xFE,
        (
            "It seems to be raining\x01",
            "across the entire state\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As expected, it seems there\x01",
            "are few who stroll the\x01",
            "highways in this weather.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EC7")

    label("loc_10E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1156")

    ChrTalk(
        0xFE,
        (
            "Haha... The children\x01",
            "really love Sister Juju.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's one kind of\x01",
            "talent. I envy her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EC7")

    label("loc_1156")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_12AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1237")

    ChrTalk(
        0xFE,
        (
            "Rosenberg Studio... It's\x01",
            "a name I hear every now\x01",
            "and then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a very old studio, but\x01",
            "don't think its owner has\x01",
            "ever visited the cathedral.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder what kind of\x01",
            "person he could be?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12A9")

    label("loc_1237")


    ChrTalk(
        0xFE,
        (
            "The Rosenberg Studio's\x01",
            "owner has never visited\x01",
            "the cathedral.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder what kind of\x01",
            "person he could be?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12A9")

    Jump("loc_1EC7")

    label("loc_12AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_1326")

    ChrTalk(
        0xFE,
        (
            "It seems Tamil and Hamil\x01",
            "went back home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well then, it's time I\x01",
            "started the evening\x01",
            "cleaning...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EC7")

    label("loc_1326")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_14D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_142D")

    ChrTalk(
        0xFE,
        (
            "Occasionally, Sir Ian\x01",
            "pops up in at the\x01",
            "cathedral just like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems he comes often when\x01",
            "dealing with especially\x01",
            "difficult matters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't know what kind of\x01",
            "worries he's having now, but...\x01",
            "I hope he does his best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14CC")

    label("loc_142D")


    ChrTalk(
        0xFE,
        (
            "Occasionally, Sir Ian\x01",
            "pops up in at the\x01",
            "cathedral just like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't know what kind of\x01",
            "worries he's having now, but...\x01",
            "I hope he does his best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14CC")

    Jump("loc_1EC7")

    label("loc_14D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_165D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15BE")

    ChrTalk(
        0xFE,
        (
            "They say mysterious\x01",
            "monsters have been spotted\x01",
            "everywhere lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It appears the CGF are asking\x01",
            "everyone not to enter places\x01",
            "far from human settlements.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone, please be very\x01",
            "careful as well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1658")

    label("loc_15BE")


    ChrTalk(
        0xFE,
        (
            "They say mysterious\x01",
            "monsters have been spotted\x01",
            "everywhere lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone, please very\x01",
            "careful not to enter places\x01",
            "far from human settlements.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1658")

    Jump("loc_1EC7")

    label("loc_165D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_17CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_170E")

    ChrTalk(
        0xFE,
        (
            "Earlier, Her Highness\x01",
            "Princess Klaudia of Liberl\x01",
            "was at the cathedral.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After greeting Archbishop\x01",
            "Eralda, it seems she\x01",
            "headed to the graveyard.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17C6")

    label("loc_170E")


    ChrTalk(
        0xFE,
        (
            "Her Highness princess Klaudia\x01",
            "seems to have headed for\x01",
            "Orchis Tower some time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's the location of today's\x01",
            "conference... Her Highness's\x01",
            "attitude is a matter of concern.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17C6")

    Jump("loc_1EC7")

    label("loc_17CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_195E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18D7")

    ChrTalk(
        0xFE,
        (
            "I saw the unveiling\x01",
            "ceremony even from here,\x01",
            "an elevated place, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When the Orchis Tower\x01",
            "veil was lifted, it was\x01",
            "truly overwhelming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To think that such a building\x01",
            "was made human hands... Dear\x01",
            "me, I can't hide my surprise.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1959")

    label("loc_18D7")


    ChrTalk(
        0xFE,
        (
            "Orchis Tower's shape was\x01",
            "truly overwhelming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To think it was built by\x01",
            "human hands... Dear me, I\x01",
            "can't hide my surprise.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1959")

    Jump("loc_1EC7")

    label("loc_195E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1A01")

    ChrTalk(
        0xFE,
        (
            "Because of the trade\x01",
            "conference, security in the\x01",
            "city has been tightened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I will pay attention\x01",
            "during my patrols of the\x01",
            "cathedral as well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EC7")

    label("loc_1A01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1BC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B05")

    ChrTalk(
        0xFE,
        (
            "The weather today is\x01",
            "unfortunate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, it seems the rain is limited to the\x01",
            "city. It appears that, if you go to Mainz\x01",
            "Mountain Path, the sky is refreshingly clear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Perhaps the weather is a\x01",
            "mere whim of the\x01",
            "Goddess.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BBE")

    label("loc_1B05")


    ChrTalk(
        0xFE,
        (
            "It seems the rain is limited to the city. It\x01",
            "appears that, if you go to Mainz Mountain\x01",
            "Path, the sky is refreshingly clear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Perhaps the weather is a\x01",
            "mere whim of the\x01",
            "Goddess.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BBE")

    Jump("loc_1EC7")

    label("loc_1BC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_1CE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C88")

    ChrTalk(
        0xFE,
        (
            "Oh... I suppose you all\x01",
            "are going home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please come visit anytime. May\x01",
            "the blessing of the Goddess be\x01",
            "with you all tomorrow as well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01109FYeah, later!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1CDF")

    label("loc_1C88")


    ChrTalk(
        0xFE,
        "It is dark after sunset.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please watch your steps\x01",
            "when descending the\x01",
            "stairs.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CDF")

    Jump("loc_1EC7")

    label("loc_1CE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_1D7E")

    ChrTalk(
        0xFE,
        (
            "The sister scheduled to be\x01",
            "appointed today seems to\x01",
            "have arrived moments ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think she's currently\x01",
            "greeting Archbishop\x01",
            "Eralda.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EC7")

    label("loc_1D7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1EC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E49")

    ChrTalk(
        0xFE,
        (
            "Welcome to Crossbell\x01",
            "Cathedral.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In this place, Archbishop Eralda,\x01",
            "head of Crossbell parish,\x01",
            "preaches the Septian teachings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please be quiet inside\x01",
            "the premises.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1EC7")

    label("loc_1E49")


    ChrTalk(
        0xFE,
        (
            "At this Crossbell Cathedral,\x01",
            "Archbishop Eralda preaches\x01",
            "the Septian teachings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please be quiet inside\x01",
            "the premises.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EC7")

    TalkEnd(0xFE)
    Return()

    # Function_7_9D8 end

    def Function_8_1ECB(): pass

    label("Function_8_1ECB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1F3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EE9")
    Call(0, 9)
    Jump("loc_1F3A")

    label("loc_1EE9")


    ChrTalk(
        0xFE,
        (
            "Then, Coutaz and Hugott\x01",
            "are safe too, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, thank\x01",
            "goodness...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F3A")

    Jump("loc_2CD6")

    label("loc_1F3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1F9B")

    ChrTalk(
        0xFE,
        (
            "I wonder if the city\x01",
            "children are safe...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tamil, Hamil,\x01",
            "everyone...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CD6")

    label("loc_1F9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_20D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2064")

    ChrTalk(
        0xFE,
        (
            "I think the most\x01",
            "important thing is the\x01",
            "children's future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if independence\x01",
            "will protect them...? Or\x01",
            "if it will threaten them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I don't know anymore...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_20D2")

    label("loc_2064")


    ChrTalk(
        0xFE,
        (
            "By being independent, I\x01",
            "wonder what will happen to\x01",
            "the children's future...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I don't know anymore...\x02",
    )

    CloseMessageWindow()

    label("loc_20D2")

    Jump("loc_2CD6")

    label("loc_20D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2222")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2109")
    Call(0, 23)
    Return()

    label("loc_2109")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2176")

    ChrTalk(
        0xFE,
        (
            "I give cookies to the\x01",
            "children who come to\x01",
            "mass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please attend too, if\x01",
            "you like.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_221D")

    label("loc_2176")


    ChrTalk(
        0xFE,
        (
            "As I thought, because of that\x01",
            "attack, it seems there are many who\x01",
            "are worried about the present peace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope that such a thing\x01",
            "doesn't ever happen\x01",
            "again...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_221D")

    Jump("loc_2CD6")

    label("loc_2222")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_22F3")

    ChrTalk(
        0xFE,
        (
            "Today, Tamil and Hamil came\x01",
            "to visit, but they went\x01",
            "back home immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're in the middle of an incident like\x01",
            "this, so their parents can be more at\x01",
            "ease if the children stay home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CD6")

    label("loc_22F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2301")
    Jump("loc_2CD6")

    label("loc_2301")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_23F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23A0")

    ChrTalk(
        0xFE,
        "S-Stop you two!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Which one of you is the\x01",
            "bad Tamil who flipped up\x01",
            "my skirt!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Hehe, I wonder who☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "*pant pant*...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_23EE")

    label("loc_23A0")


    ChrTalk(
        0xFE,
        (
            "U-Umm, aah... I-Is this\x01",
            "one Tamil?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, but, maybe... Are\x01",
            "you Hamil?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23EE")

    Jump("loc_2CD6")

    label("loc_23F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2636")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2595")

    ChrTalk(
        0xFE,
        (
            "Yesterday, when I was being\x01",
            "taught how to do a lesson by\x01",
            "Sister Marble, I noticed that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Children have a completely different\x01",
            "motivation for doing things depending on\x01",
            "whether or not they're interested in them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In order to teach something,\x01",
            "the most important thing is\x01",
            "getting them interested in it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Well, that it's the\x01",
            "most difficult thing in\x01",
            "the first place, though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2631")

    label("loc_2595")


    ChrTalk(
        0xFE,
        (
            "Being taught how to do a Sunday\x01",
            "School lesson, I thought I grew\x01",
            "a little, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To become a full fledged\x01",
            "sister, I still need a\x01",
            "lot of training.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2631")

    Jump("loc_2CD6")

    label("loc_2636")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_2644")
    Jump("loc_2CD6")

    label("loc_2644")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_2652")
    Jump("loc_2CD6")

    label("loc_2652")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2660")
    Jump("loc_2CD6")

    label("loc_2660")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_27EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2755")

    ChrTalk(
        0xFE,
        (
            "The person who was\x01",
            "escorting Princess\x01",
            "Klaudia... Captain Julia...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Seeing her from up close,\x01",
            "she was a sharp person\x01",
            "like the rumors say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. I feel like I\x01",
            "understand why the women\x01",
            "make a fuss over her.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_27E6")

    label("loc_2755")


    ChrTalk(
        0xFE,
        (
            "Captain Julia is a pious\x01",
            "person. Even if she's busy,\x01",
            "she regularly comes to church.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. Unexpectedly, our\x01",
            "habit could suit her\x01",
            "well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27E6")

    Jump("loc_2CD6")

    label("loc_27EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_27FC")
    Call(0, 10)
    Jump("loc_2CD6")

    label("loc_27FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_280D")
    Call(0, 11)
    Jump("loc_2CD6")

    label("loc_280D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_281B")
    Jump("loc_2CD6")

    label("loc_281B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_29C3")
    TurnDirection(0xFE, 0x153, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2920")

    ChrTalk(
        0xFE,
        (
            "Ah, KeA, are you going\x01",
            "home already today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01100FYes! Lloyd and the\x01",
            "others came to pick me\x01",
            "up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Haha, well good then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In that case, I'll see\x01",
            "you on the day of your\x01",
            "next class.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01109FYeah. Bye, Sister!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_29BE")

    label("loc_2920")


    ChrTalk(
        0xFE,
        (
            "KeA, I'll see you on the\x01",
            "day of your next class.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll bake cookies for\x01",
            "everyone next time as\x01",
            "well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01109FYeah, I'll be looking\x01",
            "forward to it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29BE")

    Jump("loc_2CD6")

    label("loc_29C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_2B38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AC8")

    ChrTalk(
        0xFE,
        (
            "I wonder if the one who\x01",
            "entered the chapel just now\x01",
            "was a newly appointed sister?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am a novice who has been in\x01",
            "service here for not even one year,\x01",
            "but finally, I have a junior...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "S-Somehow my heart has\x01",
            "started racing!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B33")

    label("loc_2AC8")


    ChrTalk(
        0xFE,
        (
            "Finally, I too have a\x01",
            "junior... How exciting!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I must teach her many\x01",
            "things in a senior-like\x01",
            "way.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B33")

    Jump("loc_2CD6")

    label("loc_2B38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2CD6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C2B")

    ChrTalk(
        0xFE,
        (
            "Oh, good morning. Today\x01",
            "we're holding Sunday\x01",
            "School classes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Could you the\x01",
            "guardians of one of the\x01",
            "children?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The auditorium where we hold\x01",
            "classes is the room to the right\x01",
            "after entering the chapel.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2CD6")

    label("loc_2C2B")


    ChrTalk(
        0xFE,
        (
            "The auditorium where we hold Sunday\x01",
            "School classes is the room to the\x01",
            "right after entering the chapel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. If you like, why\x01",
            "not go have a look at\x01",
            "the lessons?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CD6")

    TalkEnd(0xFE)
    Return()

    # Function_8_1ECB end

    def Function_9_2CDA(): pass

    label("Function_9_2CDA")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xA,
        (
            "Tamil, Hamil, I'm really\x01",
            "glad you're safe!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "*sob*... Ah, my Goddess.\x01",
            "Thank you for your\x01",
            "mercy!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xB)

    ChrTalk(
        0xB,
        (
            "H-Hey Sister, you don't\x01",
            "have to cry like that,\x01",
            "you know...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Hehe. Thank you, Sister.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    ClearChrFlags(0xB, 0x10)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_9_2CDA end

    def Function_10_2DD9(): pass

    label("Function_10_2DD9")

    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FD7")

    ChrTalk(
        0x8,
        (
            "#04400FSister Juju. I heard something\x01",
            "worrisome about the Mainz area where\x01",
            "you're going for lessons tomorrow...\x02\x03",
            "#04403FSome time ago, there was a bizarre\x01",
            "incident around there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yes, now that you\x01",
            "mention it, there was\x01",
            "something like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I think it was something about\x01",
            "spirit-like beings being sighted in\x01",
            "the old ruins of the Mainz region.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04401F...Could you tell me\x01",
            "about that in a little\x01",
            "more detail?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yes, all right. Although\x01",
            "I don't know many\x01",
            "details.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_30AF")

    label("loc_2FD7")


    ChrTalk(
        0xA,
        (
            "...Right, it was tough\x01",
            "when I went to Mainz\x01",
            "before with Sister Hatina.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The father of a little girl\x01",
            "called Kimmy, worried about the\x01",
            "class, came marching in and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04403F(You're digressing a\x01",
            "little...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30AF")

    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_10_2DD9 end

    def Function_11_30B8(): pass

    label("Function_11_30B8")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_318C")

    ChrTalk(
        0xA,
        "Enough, Tamil!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hiding under the skirt\x01",
            "of a girl is extremely\x01",
            "naughty, you know!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Tehehe, sorryyy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'll try not to do it\x01",
            "anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "You won't just try, you\x01",
            "won't!!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3231")

    label("loc_318C")


    ChrTalk(
        0xB,
        (
            "But you know, Sister...\x01",
            "There's just one thing I\x01",
            "want to tell you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Shouldn't you wear a\x01",
            "pair that's a little\x01",
            "sexier?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "T-That's none of your\x01",
            "business!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3231")

    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_11_30B8 end

    def Function_12_323A(): pass

    label("Function_12_323A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_331A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3258")
    Call(0, 9)
    Jump("loc_3315")

    label("loc_3258")


    ChrTalk(
        0xFE,
        (
            "Tch, she got carried away. Although\x01",
            "we were the ones who were worried,\x01",
            "she suddenly started to cry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, oh well. When she cools\x01",
            "off, I'll use this story to\x01",
            "tease her next time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3315")

    Jump("loc_3814")

    label("loc_331A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3328")
    Jump("loc_3814")

    label("loc_3328")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3385")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3343")
    Call(0, 13)
    Jump("loc_3380")

    label("loc_3343")


    ChrTalk(
        0xFE,
        (
            "If Hamil doesn't get it,\x01",
            "there's no way I ever\x01",
            "could...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3380")

    Jump("loc_3814")

    label("loc_3385")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3393")
    Jump("loc_3814")

    label("loc_3393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_33A1")
    Jump("loc_3814")

    label("loc_33A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_33AF")
    Jump("loc_3814")

    label("loc_33AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_33D4")

    ChrTalk(
        0xFE,
        "Hehe, who is who?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3814")

    label("loc_33D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3417")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33EF")
    Call(0, 14)
    Jump("loc_3412")

    label("loc_33EF")


    ChrTalk(
        0xFE,
        (
            "Alright, let's do it at\x01",
            "once!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3412")

    Jump("loc_3814")

    label("loc_3417")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_3425")
    Jump("loc_3814")

    label("loc_3425")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_3436")
    Call(0, 15)
    Jump("loc_3814")

    label("loc_3436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_34B9")

    ChrTalk(
        0xFE,
        (
            "It seems the kids from\x01",
            "East Street are having\x01",
            "class today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, I guess I'll peep\x01",
            "from that window there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3814")

    label("loc_34B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3613")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_358E")

    ChrTalk(
        0xFE,
        (
            "There's just about no\x01",
            "one who can distinguish\x01",
            "between Hamil and I.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's why I\x01",
            "occasionally pose as\x01",
            "Hamil and do pranks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But if it's my mom, I\x01",
            "get found out\x01",
            "immediately.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_360E")

    label("loc_358E")


    ChrTalk(
        0xFE,
        (
            "If it's my mom, even if I\x01",
            "impersonate Hamil, I get\x01",
            "found out immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ummm, does she have a\x01",
            "way to tell us apart?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_360E")

    Jump("loc_3814")

    label("loc_3613")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3663")

    ChrTalk(
        0xFE,
        (
            "Orchis Tower was really\x01",
            "huuuge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Honestly, I felt small.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3814")

    label("loc_3663")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3674")
    Call(0, 11)
    Jump("loc_3814")

    label("loc_3674")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3682")
    Jump("loc_3814")

    label("loc_3682")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_37A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_373E")

    ChrTalk(
        0xFE,
        (
            "I thought I'd try flipping\x01",
            "up the new sister's skirt\x01",
            "just now, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She skillfully dodged me\x01",
            "somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mrr... It seems she's no\x01",
            "ordinary person.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_37A0")

    label("loc_373E")


    ChrTalk(
        0xFE,
        (
            "To dodge my skirt-\x01",
            "flip...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That new sister... She\x01",
            "doesn't seem like an\x01",
            "ordinary person.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37A0")

    Jump("loc_3814")

    label("loc_37A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_380B")

    ChrTalk(
        0xFE,
        (
            "It seems a new sister\x01",
            "has just arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, I'll tease her a\x01",
            "little, later.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3814")

    label("loc_380B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3814")

    label("loc_3814")

    TalkEnd(0xFE)
    Return()

    # Function_12_323A end

    def Function_13_3818(): pass

    label("Function_13_3818")

    OP_4B(0xC, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xB,
        (
            "The adults are in a\x01",
            "tizzy for some reason...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            ""Independence"...? What\x01",
            "could that be?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hamil, studying is your\x01",
            "forte. You tell me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I-It's no use. I don't\x01",
            "get it either...\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xB, 0xFF)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_13_3818 end

    def Function_14_38F2(): pass

    label("Function_14_38F2")

    OP_4B(0xC, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xB,
        (
            "...And so, if the sister\x01",
            "gets mad, we'll do this...\x01",
            "*mutter mutter*...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Eeeh, why do I have to\x01",
            "do that too...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Why not? I won't tell\x01",
            "KeA you wet the bed\x01",
            "lately!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Ugh, if you say that...\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_14_38F2 end

    def Function_15_39D2(): pass

    label("Function_15_39D2")

    OP_4B(0xC, 0xFF)
    OP_4B(0xB, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3ABA")

    ChrTalk(
        0xB,
        (
            "We were forced to take\x01",
            "part in Sunday School\x01",
            "class too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "*sigh*, why'd you peep\x01",
            "in on the lesson,\x01",
            "Hamil...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "N-No, no. You were the\x01",
            "one who said that,\x01",
            "Tamil.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Don't casually blame me,\x01",
            "geez.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3B43")

    label("loc_3ABA")


    ChrTalk(
        0xC,
        (
            "But aren't you glad? You\x01",
            "got to study a lot and\x01",
            "it was worth it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Unlike you, I hate\x01",
            "studying! Tch, that's\x01",
            "why bookworms are...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B43")

    OP_4C(0xC, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_15_39D2 end

    def Function_16_3B4C(): pass

    label("Function_16_3B4C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3BD4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B6A")
    Call(0, 9)
    Jump("loc_3BCF")

    label("loc_3B6A")


    ChrTalk(
        0xFE,
        (
            "Yes, the city children\x01",
            "seem to all be fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, thank you for\x01",
            "worrying about us,\x01",
            "sister.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BCF")

    Jump("loc_437D")

    label("loc_3BD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3BE2")
    Jump("loc_437D")

    label("loc_3BE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3C8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BFD")
    Call(0, 13)
    Jump("loc_3C8A")

    label("loc_3BFD")


    ChrTalk(
        0xFE,
        (
            "I don't really get what\x01",
            "independence is, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "According to what the city\x01",
            "adults were saying, it seems\x01",
            "serious for some reason...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C8A")

    Jump("loc_437D")

    label("loc_3C8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3C9D")
    Jump("loc_437D")

    label("loc_3C9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3CAB")
    Jump("loc_437D")

    label("loc_3CAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3CB9")
    Jump("loc_437D")

    label("loc_3CB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3D1F")

    ChrTalk(
        0xFE,
        (
            "*pant, pant*... W-Why do\x01",
            "even I have to...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We'll be scolded later\x01",
            "for sure...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_437D")

    label("loc_3D1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3D73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D3A")
    Call(0, 14)
    Jump("loc_3D6E")

    label("loc_3D3A")


    ChrTalk(
        0xFE,
        (
            "Ooh, I've got no\x01",
            "choice... Just this\x01",
            "once, ok?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D6E")

    Jump("loc_437D")

    label("loc_3D73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_3D81")
    Jump("loc_437D")

    label("loc_3D81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_3D92")
    Call(0, 15)
    Jump("loc_437D")

    label("loc_3D92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3DE5")

    ChrTalk(
        0xFE,
        (
            "Stop it I say... I won't\x01",
            "care if you get scolded\x01",
            "by the sister.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_437D")

    label("loc_3DE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3F25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EB0")

    ChrTalk(
        0xFE,
        (
            "It seems like mom and\x01",
            "dad can tell us twins\x01",
            "apart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They say they know just by\x01",
            "looking at us, even though we\x01",
            "have almost the same face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Parents can be\x01",
            "amazing...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3F20")

    label("loc_3EB0")


    ChrTalk(
        0xFE,
        (
            "Mom and dad say that they\x01",
            "can tell Tamil and I apart\x01",
            "just by looking at us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Parents can be\x01",
            "amazing...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F20")

    Jump("loc_437D")

    label("loc_3F25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3FB0")

    ChrTalk(
        0xFE,
        (
            "*sigh*, it was a rare chance,\x01",
            "so I would've liked to see the\x01",
            "unveiling ceremony with KeA...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...Ah, i-it's nothing.\x02",
    )

    CloseMessageWindow()
    Jump("loc_437D")

    label("loc_3FB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_40E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4059")

    ChrTalk(
        0xFE,
        (
            "While playing hide and\x01",
            "seek, Tamil hid under\x01",
            "the sister's skirt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, it was obvious\x01",
            "she was going to be\x01",
            "angry, so why did he...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_40DE")

    label("loc_4059")


    ChrTalk(
        0xFE,
        (
            "Even so... When they get angry\x01",
            "at Tamil, I feel they're\x01",
            "getting angry at me too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Being twins is a\x01",
            "disadvantage, somehow...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40DE")

    Jump("loc_437D")

    label("loc_40E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_40F1")
    Jump("loc_437D")

    label("loc_40F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_4303")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42A9")
    TurnDirection(0xFE, 0x153, 0)

    ChrTalk(
        0xFE,
        (
            "Ah, KeA! Is senior class\x01",
            "over?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01109FYes, it ended just now.\x02\x03",
            "#01100FHamil, were you playing\x01",
            "until now after classes\x01",
            "were over?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Y-Yes. With Tamil.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way, you already\x01",
            "perfectly understand that\x01",
            "I'm Hamil, huh, KeA?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01105FHuuuh, why?\x02\x03",
            "#01109FYou have the same face\x01",
            "as Tamil, but Hamil is\x01",
            "Hamil, I know that.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "(Man, this makes me\x01",
            "super happy...!)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_42FE")

    label("loc_42A9")

    TurnDirection(0xFE, 0x153, 0)

    ChrTalk(
        0xFE,
        (
            "Umm, please be careful,\x01",
            "KeA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01109FYes. Let's play together\x01",
            "again!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42FE")

    Jump("loc_437D")

    label("loc_4303")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_4374")

    ChrTalk(
        0xFE,
        (
            "Don't, Tamil... What if\x01",
            "she's a scary person?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I won't care if she gets\x01",
            "angry at you, ok?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_437D")

    label("loc_4374")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_437D")

    label("loc_437D")

    TalkEnd(0xFE)
    Return()

    # Function_16_3B4C end

    def Function_17_4381(): pass

    label("Function_17_4381")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4396")
    Call(0, 18)
    Jump("loc_43FD")

    label("loc_4396")


    ChrTalk(
        0xFE,
        (
            "*sigh*... I guess if KeA\x01",
            "said it, I guess I've\x01",
            "gotta do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll do my homework from\x01",
            "now on.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43FD")

    TalkEnd(0xFE)
    Return()

    # Function_17_4381 end

    def Function_18_4401(): pass

    label("Function_18_4401")

    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0xD,
        (
            "Sister was mad at me,\x01",
            "you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "You didn't do your\x01",
            "homework. You got what\x01",
            "you deserved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "*sigh*, she was quite lenient\x01",
            "before, but became strict after\x01",
            "we started senior class, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01105FYou have to do your\x01",
            "homework next time, ok?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    TurnDirection(0xD, 0x153, 500)
    Sleep(500)

    ChrTalk(
        0xD,
        "Okaaay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F(That's KeA for you...)\x02",
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    TurnDirection(0xD, 0xE, 0)
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x0, 5)
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_18_4401 end

    def Function_19_4576(): pass

    label("Function_19_4576")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_458B")
    Call(0, 18)
    Jump("loc_45B5")

    label("loc_458B")


    ChrTalk(
        0xFE,
        (
            "Pfft. You were even\x01",
            "lectured by KeA.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45B5")

    TalkEnd(0xFE)
    Return()

    # Function_19_4576 end

    def Function_20_45B9(): pass

    label("Function_20_45B9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46F9")
    TurnDirection(0xFE, 0x153, 0)

    ChrTalk(
        0xFE,
        "Oh, KeA! Going home?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01110FYeah! You too, Burick?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yeah. I was thinking of\x01",
            "buying Crossbell Times on\x01",
            "West Street on my way back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "KeA... I won't lose in\x01",
            "the next class!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01111FOh...? Was it a\x01",
            "competition...?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "N-No, nevermind. Forget\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_477F")

    label("loc_46F9")


    ChrTalk(
        0xFE,
        (
            "When KeA started\x01",
            "attending senior class,\x01",
            "I was shocked, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I thought I'd take this\x01",
            "chance to study properly\x01",
            "once again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_477F")

    TalkEnd(0xFE)
    Return()

    # Function_20_45B9 end

    def Function_21_4783(): pass

    label("Function_21_4783")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05900.itc", 0x1E)
    LoadChrToIndex("apl/ch51020.itc", 0x1F)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02200.itp")
    OP_11(0xA0, 0xDC, 0xDC, 0x3C, 0x64, 0x0)
    OP_68(13460, 3600, 9960, 0)
    MoveCamera(310, 9, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(31000, 0)
    OP_68(13460, 10600, 9960, 7500)
    SetChrPos(0x101, 0, 0, 2450, 0)
    SetChrPos(0x102, 1000, 0, 2100, 0)
    SetChrPos(0x103, -750, 0, 1900, 0)
    SetChrPos(0x104, 0, 0, 350, 0)
    SetChrPos(0x109, 1000, 0, 850, 0)
    SetChrPos(0x105, -1000, 0, 150, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0xC, 0x8)
    SetChrChipByIndex(0x10, 0x1E)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    ClearChrFlags(0x10, 0x4)
    SetChrPos(0x10, 70, 2000, 28890, 180)
    FadeToBright(1000, 0)

    def lambda_48CA():
        OP_9B(0x0, 0x101, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_48CA)
    Sleep(100)

    def lambda_48E2():
        OP_9B(0x0, 0x102, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_48E2)
    Sleep(100)

    def lambda_48FA():
        OP_9B(0x0, 0x103, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_48FA)
    Sleep(100)

    def lambda_4912():
        OP_9B(0x0, 0x104, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4912)
    Sleep(100)

    def lambda_492A():
        OP_9B(0x0, 0x109, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_492A)
    Sleep(100)

    def lambda_4942():
        OP_9B(0x0, 0x105, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4942)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(1000)
    OP_11(0xA0, 0xDC, 0xDC, 0x3C, 0x64, 0x0)
    OP_68(0, 900, 16750, 0)
    MoveCamera(315, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18880, 0)
    SetCameraDistance(18380, 1500)
    OP_0D()
    OP_6F(0x79)

    def lambda_49C1():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_49C1)
    Sleep(50)

    def lambda_49D1():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_49D1)
    Sleep(50)

    def lambda_49E1():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_49E1)
    Sleep(50)

    def lambda_49F1():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_49F1)
    Sleep(50)

    def lambda_4A01():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4A01)
    Sleep(50)

    def lambda_4A11():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4A11)
    Sleep(50)

    def lambda_4A21():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4A21)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x101, 2)

    ChrTalk(
        0x101,
        (
            "#00003F#11P...Already evening, huh?\x02\x03",
            "#00001FI'd like to hand in our\x01",
            "report today, so we've\x01",
            "got to gather info.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PYes... I hope there are\x01",
            "some clues.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4B8C")

    ChrTalk(
        0x103,
        (
            "#00200FFor now, we're paying a\x01",
            "visit to Ries or Miss\x01",
            "Marble, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#11PYeah, let's try the\x01",
            "Sunday School classroom\x01",
            "first.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C1E")

    label("loc_4B8C")


    ChrTalk(
        0x103,
        (
            "#00200FFor now, we're paying a\x01",
            "visit to Miss Marble,\x01",
            "correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#11PYeah, I hope she doesn't\x01",
            "have Sunday School\x01",
            "lessons, though...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C1E")

    ClearChrFlags(0x10, 0x80)

    NpcTalk(
        0x10,
        "Man's Voice",
        "Oh, you all are...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_4CC1():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4CC1)
    Sleep(0)

    def lambda_4CD1():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4CD1)
    Sleep(0)

    def lambda_4CE1():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4CE1)
    Sleep(0)

    def lambda_4CF1():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4CF1)
    Sleep(0)

    def lambda_4D01():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4D01)
    Sleep(0)

    def lambda_4D11():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4D11)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_68(-30, 1100, 18180, 3000)
    MoveCamera(318, 18, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(18330, 3000)
    OP_9B(0x0, 0x10, 0x0, 0x1F40, 0x7D0, 0x0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00005F#6PLawyer Ian...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16C, 1)), scpexpr(EXPR_END)), "loc_5037")

    ChrTalk(
        0x102,
        "#00104F#6PLong time no see.\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    AnonymousTalk(
        0x10,
        (
            "Yes, since the trade conference,\x01",
            "right?\x02\x03",
            "Oh, by the way, I was told you\x01",
            "stopped by my office at noon?\x02\x03",
            "I'm sorry. You came on purpose, and\x01",
            "yet...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    ChrTalk(
        0x101,
        (
            "#00012F#6PNo... But, you seem\x01",
            "busy, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F#6PI'm told you're helping\x01",
            "write our draft\x01",
            "constitution?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#02210F#11PWell, haha...\x02\x03",
            "Because the mayor asked me\x01",
            "so earnestly, I couldn't\x01",
            "really turn him down.\x02\x03",
            "#02200FWell, I agree with his ideas\x01",
            "even on a personal level.\x02\x03",
            "Maybe they'll be difficult\x01",
            "to realize, but... I want to\x01",
            "at least give him a hand.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5558")

    label("loc_5037")


    ChrTalk(
        0x102,
        (
            "#00104F#6PLong time no see.\x02\x03",
            "#00108FIt seems you've been\x01",
            "quite busy lately?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#00005F#5PIs that so?\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    AnonymousTalk(
        0x10,
        (
            "Well, haha...\x02\x03",
            "Actually, the mayor asked me to\x01",
            "draft the constitution for state\x01",
            "independence.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
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
    OP_93(0x101, 0x0, 0x1F4)

    ChrTalk(
        0x101,
        "#00007F#6PHuh!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F#6PA Constitution... That's\x01",
            "different from a state\x01",
            "law, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x109, 500)

    ChrTalk(
        0x102,
        (
            "#00104F#11PA Constitution is the fundamental law\x01",
            "that establishes the basic conditions\x01",
            "of a state's existence.\x02\x03",
            "#00100FAs the supreme law that establishes a\x01",
            "nation's soverignty, government and\x01",
            "fundamental principles, interference\x01",
            "from other nations is not permitted.\x02\x03",
            "It's something that's absolutely\x01",
            "indispensable for having the\x01",
            "appearance of a nation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F#6P...Right... Another\x01",
            "complicated thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#6PHowever, I think that\x01",
            "someone like Lawyer Ian\x01",
            "is truly suited for it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#02210F#11PHaha... Because the mayor\x01",
            "asked me so earnestly, I\x01",
            "couldn't really turn him down.\x02\x03",
            "#02200FWell, I agree with his ideas\x01",
            "even on a personal level.\x02\x03",
            "Maybe they'll be difficult to\x01",
            "realize, but... I want to at\x01",
            "least give him a hand.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5558")


    def lambda_555D():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_555D)

    ChrTalk(
        0x101,
        "#00002F#6PIs that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#6PCould it be that you\x01",
            "came to pray during one\x01",
            "of your breaks?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#02210F#11PYes. I had reached a bit of an\x01",
            "impasse but it seems this has\x01",
            "been a nice change of pace.\x02\x03",
            "#02202FReally, it's not bad for a man\x01",
            "to pray to the Goddess in\x01",
            "times of trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309F#6PHaha... You said it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#6PThank you so much for\x01",
            "all your hard work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#02210F#11PHaha, I should say the\x01",
            "same to all of you.\x02\x03",
            "#02200FIt's already evening,\x01",
            "but... Could you have\x01",
            "come due to a job?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PYes, there's something\x01",
            "we'd like to consult with\x01",
            "a Church official about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#02203F#11PHm, it seems you have your own\x01",
            "circumstances.\x02\x03",
            "#02200FI'm busy as well. However, if there's\x01",
            "something I can help you with, don't\x01",
            "hesitate to pay my office a visit.\x02\x03",
            "You all are welcome there any time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004F#6PThank you very much.\x02",
    )

    CloseMessageWindow()
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x109, 0x1F)
    SetChrSubChip(0x109, 0x0)
    OP_0D()

    ChrTalk(
        0x109,
        (
            "#10100F#6PPlease be careful on\x01",
            "your way back!\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    OP_0D()

    def lambda_5917():

        label("loc_5917")

        TurnDirection(0x101, 0x10, 500)
        Yield()
        Jump("loc_5917")

    QueueWorkItem2(0x101, 2, lambda_5917)

    def lambda_5929():

        label("loc_5929")

        TurnDirection(0x102, 0x10, 500)
        Yield()
        Jump("loc_5929")

    QueueWorkItem2(0x102, 2, lambda_5929)

    def lambda_593B():

        label("loc_593B")

        TurnDirection(0x103, 0x10, 500)
        Yield()
        Jump("loc_593B")

    QueueWorkItem2(0x103, 2, lambda_593B)

    def lambda_594D():

        label("loc_594D")

        TurnDirection(0x104, 0x10, 500)
        Yield()
        Jump("loc_594D")

    QueueWorkItem2(0x104, 2, lambda_594D)

    def lambda_595F():

        label("loc_595F")

        TurnDirection(0x109, 0x10, 500)
        Yield()
        Jump("loc_595F")

    QueueWorkItem2(0x109, 2, lambda_595F)

    def lambda_5971():

        label("loc_5971")

        TurnDirection(0x105, 0x10, 500)
        Yield()
        Jump("loc_5971")

    QueueWorkItem2(0x105, 2, lambda_5971)
    OP_9B(0x0, 0x10, 0x13B, 0xBB8, 0x8FC, 0x1)
    OP_68(-670, 900, 16640, 3000)
    MoveCamera(315, 23, 0, 3000)
    OP_9B(0x0, 0x10, 0x32, 0x2710, 0x9C4, 0x0)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    SetChrFlags(0x10, 0x80)
    OP_6F(0x79)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00001F#11P...He seems busy.\x02",
    )

    CloseMessageWindow()

    def lambda_5A01():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5A01)
    Sleep(0)

    def lambda_5A11():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5A11)
    Sleep(0)

    def lambda_5A21():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5A21)
    Sleep(0)

    def lambda_5A31():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5A31)
    Sleep(0)

    def lambda_5A41():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5A41)
    Sleep(0)

    def lambda_5A51():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5A51)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x102,
        (
            "#00103F#12PYes, writing a constitution\x01",
            "draft can be very demanding...\x02\x03",
            "#00101FIf something poor is published,\x01",
            "the Empire and Republic will say\x01",
            "it lacks persuasive power...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#6PWhoa...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#6PHehe. That's a different\x01",
            "kind of worry than how\x01",
            "busy we are, huh.\x02\x03",
            "#10300FBy the way... Are we\x01",
            "visiting the Sunday\x01",
            "School classroom?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#11PYeah, let's go.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    SetChrPos(0x0, 0, 0, 17450, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0xB, 0x8)
    ClearChrFlags(0xC, 0x8)
    OP_CC(0x1, 0xFF, 0x0)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0x161, 5)
    OP_29(0xA6, 0x1, 0x6)
    EventEnd(0x5)
    Return()

    # Function_21_4783 end

    def Function_22_5C40(): pass

    label("Function_22_5C40")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_68(-8010, 1550, 13580, 0)
    MoveCamera(315, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17850, 0)
    SetChrPos(0x101, -7750, 250, 14000, 270)
    SetChrPos(0x102, -8000, 250, 15050, 225)
    SetChrPos(0x103, -7900, 250, 12900, 315)
    SetChrPos(0x104, -6850, 0, 14900, 225)
    SetChrPos(0x109, -6750, 0, 12450, 315)
    SetChrPos(0x105, -6250, 0, 13500, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#04403F#5P...Come now, this way.\x02\x03",
            "#04400FI don't want other\x01",
            "people to see us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#12PR-Right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103F#12P...Excuse us.\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x1F4)
    Sound(121, 0, 100, 0)
    OP_71(0x1, 0x0, 0x14, 0x0, 0x0)
    OP_79(0x1)

    def lambda_5DC3():
        OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_5DC3)
    OP_9B(0x0, 0x8, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0x8, 3)

    def lambda_5DE7():
        OP_95(0x102, -11400, 500, 14750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5DE7)
    Sleep(200)

    def lambda_5E04():
        OP_95(0x103, -11400, 500, 13250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5E04)
    Sleep(100)

    def lambda_5E21():
        OP_95(0x101, -11400, 500, 14000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5E21)
    Sleep(100)

    def lambda_5E3E():
        OP_95(0x104, -11400, 500, 14750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5E3E)
    Sleep(100)

    def lambda_5E5B():
        OP_95(0x109, -11400, 500, 13250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5E5B)
    Sleep(200)

    def lambda_5E78():
        OP_95(0x105, -11400, 500, 14000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5E78)
    Sleep(500)
    FadeToDark(1000, 0, -1)

    def lambda_5E9F():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_5E9F)
    Sleep(50)

    def lambda_5EB3():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_5EB3)
    Sleep(50)

    def lambda_5EC7():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5EC7)
    Sleep(150)

    def lambda_5EDB():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 3, lambda_5EDB)
    Sleep(50)

    def lambda_5EEF():
        OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_5EEF)
    Sleep(50)

    def lambda_5F03():
        OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 3, lambda_5F03)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x105, 3)
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 0)
    NewScene("t4030", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_22_5C40 end

    def Function_23_5F53(): pass

    label("Function_23_5F53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_612C")

    ChrTalk(
        0xA,
        (
            "We're holding mass\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Why don't you take part,\x01",
            "everyone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(I wonder if she'd be\x01",
            "our sister for the\x01",
            "pageant...?)\x02\x03",
            "#00000FUmm, excuse me. I'd like\x01",
            "to ask you something...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Asked Sister Juju to\x01",
            "participate in the\x01",
            "charity event pageant.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            "H-Huuuh? I, in a beauty\x01",
            "contest...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I-It's impossible.\x01",
            "Someone like me has no\x01",
            "appeal at all, you see...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm sorry, please try\x01",
            "inviting someone else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FI-I see...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x199, 1)
    Jump("loc_61AA")

    label("loc_612C")


    ChrTalk(
        0xA,
        (
            "I-It's impossible for\x01",
            "someone like me to appear\x01",
            "in a beauty contest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I think there's other\x01",
            "more appropriate people.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61AA")

    TalkEnd(0xA)
    Return()

    # Function_23_5F53 end

    def Function_24_61AE(): pass

    label("Function_24_61AE")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "～Crossbell Cathedral Dormitory～\x01",
            "　　Worship-visitors, please\x01",
            "      visit to the chapel.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_24_61AE end

    def Function_25_6243(): pass

    label("Function_25_6243")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001F...Anyway, let's go to\x01",
            "Ries' place. We may\x01",
            "learn something.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 370, 0, -7350, 0)
    EventEnd(0x4)
    Return()

    # Function_25_6243 end

    SaveToFile()

Try(main)
