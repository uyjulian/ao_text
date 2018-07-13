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
        "Function_8_1F5B",         # 08, 8
        "Function_9_2D46",         # 09, 9
        "Function_10_2E4B",        # 0A, 10
        "Function_11_3154",        # 0B, 11
        "Function_12_32FF",        # 0C, 12
        "Function_13_390D",        # 0D, 13
        "Function_14_39E4",        # 0E, 14
        "Function_15_3AD4",        # 0F, 15
        "Function_16_3C5B",        # 10, 16
        "Function_17_44CA",        # 11, 17
        "Function_18_454C",        # 12, 18
        "Function_19_46DF",        # 13, 19
        "Function_20_4735",        # 14, 20
        "Function_21_4932",        # 15, 21
        "Function_22_5E64",        # 16, 22
        "Function_23_6183",        # 17, 23
        "Function_24_63F4",        # 18, 24
        "Function_25_648C",        # 19, 25
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB4")

    ChrTalk(
        0xFE,
        (
            "That palely shining tree...\x01",
            "I wonder what could have\x01",
            "caused it to appear in Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Will it bring light to this land\x01",
            "or will it bring disaster...?\x01",
            "We clergyman cannot fathom.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B1D")

    label("loc_AB4")


    ChrTalk(
        0xFE,
        "That palely shining tree, what could it be...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder if this too is the will of the Goddess?\x02",
    )

    CloseMessageWindow()

    label("loc_B1D")

    Jump("loc_1F57")

    label("loc_B22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_C48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF9")

    ChrTalk(
        0xFE,
        (
            "Just when the barrier vanished all of a sudden,\x01",
            "it seems that armored monsters began to\x01",
            "loiter around the city...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If this too is President\x01",
            "Dieter's idea, I'll never\x01",
            "forgive him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C43")

    label("loc_BF9")


    ChrTalk(
        0xFE,
        (
            "Making monsters loitering in the city...\x01",
            "That's an unforgivable act.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C43")

    Jump("loc_1F57")

    label("loc_C48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_DC9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D37")

    ChrTalk(
        0xFE,
        (
            "It appears that there was a speech\x01",
            "by Mr. Crois in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if disorders due to\x01",
            "Crossbell independence can't\x01",
            "be avoided to reach Zemuria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "O Goddess, please give guidance to the people...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DC4")

    label("loc_D37")


    ChrTalk(
        0xFE,
        (
            "Dear me, I wonder if a conflict between\x01",
            "the Empire and Republic can be avoided...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "O Goddess, please give guidance to the people...\x02",
    )

    CloseMessageWindow()

    label("loc_DC4")

    Jump("loc_1F57")

    label("loc_DC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_F4B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EB1")

    ChrTalk(
        0xFE,
        (
            "Today, we're holding mass\x01",
            "in the Cathedral chapel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a function to pray the Goddess to give\x01",
            "her guidance to those who died in the raid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you have the time, please\x01",
            "attend too, everyone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F46")

    label("loc_EB1")


    ChrTalk(
        0xFE,
        (
            "Many worship visitors came\x01",
            "to today mass to mourn for\x01",
            "the raid that happened before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you have the time, please\x01",
            "attend too, everyone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_F46")

    Jump("loc_1F57")

    label("loc_F4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_108F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FF8")

    ChrTalk(
        0xFE,
        (
            "Since last night, gunshots and explosions\x01",
            "sounds can be frequently heard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It appears that the\x01",
            "fight in Mainz has\x01",
            "become quite severe...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_108A")

    label("loc_FF8")


    ChrTalk(
        0xFE,
        (
            "In any case...\x01",
            "It is not said that the armed\x01",
            "group won't come here too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We must urgently consider this\x01",
            "even to protect the Cathedral...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_108A")

    Jump("loc_1F57")

    label("loc_108F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_113F")

    ChrTalk(
        0xFE,
        (
            "Today, it appears that it's raining on the\x01",
            "entire autonomous state of Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As expected, it seems there're few\x01",
            "persons who stroll to the highways.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F57")

    label("loc_113F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_11B0")

    ChrTalk(
        0xFE,
        (
            "Ha ha...\x01",
            "Sister Juju is really\x01",
            "loved by children.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's one type of talent.\x01",
            "I envy her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F57")

    label("loc_11B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_12F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1288")

    ChrTalk(
        0xFE,
        (
            "The Rosenberg Studio...\x01",
            "It's a name I hear now and then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a very old studio, but\x01",
            "I think its owner never\x01",
            "visited the Cathedral.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder what kind of\x01",
            "person could he be?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12F4")

    label("loc_1288")


    ChrTalk(
        0xFE,
        (
            "The Rosenberg Studio owner\x01",
            "never visited the Cathedral.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder what kind of\x01",
            "person could he be?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12F4")

    Jump("loc_1F57")

    label("loc_12F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_137B")

    ChrTalk(
        0xFE,
        (
            "It appears that Tamil and\x01",
            "Hamil went back home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well then, it's time I must\x01",
            "start the evening cleaning...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F57")

    label("loc_137B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_1525")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1484")

    ChrTalk(
        0xFE,
        (
            "Occasionally, Mr. Ian pops up\x01",
            "in the Cathedral just like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems he comes often\x01",
            "when he's dealing with\x01",
            "especially difficult matters.\x02",
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
    Jump("loc_1520")

    label("loc_1484")


    ChrTalk(
        0xFE,
        (
            "Occasionally, Mr. Ian pops up\x01",
            "in the Cathedral just like that.\x02",
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

    label("loc_1520")

    Jump("loc_1F57")

    label("loc_1525")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_16DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1623")

    ChrTalk(
        0xFE,
        (
            "They say that lately mysterious monsters\x01",
            "have been spotted in every place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It appears that the CGF too are\x01",
            "appealing to not enter alone in\x01",
            "places far from human settlements.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Everyone, please be very careful too.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16D6")

    label("loc_1623")


    ChrTalk(
        0xFE,
        (
            "They say that lately mysterious \x01",
            "monsters have been spotted\x01",
            "in every place and so on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone, please very careful too to not \x01",
            "enter places far from human settlements.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16D6")

    Jump("loc_1F57")

    label("loc_16DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1853")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17A2")

    ChrTalk(
        0xFE,
        (
            "Just some time ago, Her Highness\x01",
            "Princess Klaudia of Liberl was at\x01",
            "the Cathedral.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After having greeted Archbishop Eralda,\x01",
            "it seems she headed over to the graveyard.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_184E")

    label("loc_17A2")


    ChrTalk(
        0xFE,
        (
            "Her Highness princess Klaudia\x01",
            "seems to have headed towards\x01",
            "Orchis Tower some time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Today conference location...\x01",
            "Her Highness's moves are a matter of concern.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_184E")

    Jump("loc_1F57")

    label("loc_1853")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_19EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1970")

    ChrTalk(
        0xFE,
        (
            "I could see the state of the\x01",
            "unveiling ceremony even from\x01",
            "here, an elevated place, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When the Orchis Tower veil was taken off,\x01",
            "if was truly overwhelming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To think that such a building\x01",
            "was made by man...\x01",
            "Dear me, I can't hide my surprise.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19EA")

    label("loc_1970")


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
            "To think it was built by man...\x01",
            "Dear me, I can't hide my surprise.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19EA")

    Jump("loc_1F57")

    label("loc_19EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1A87")

    ChrTalk(
        0xFE,
        (
            "Because of the Trade Conference, \x01",
            "security in the city has been strengthened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I too will pay attention\x01",
            "to patrol the Cathedral.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F57")

    label("loc_1A87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1C49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B8B")

    ChrTalk(
        0xFE,
        "Today the weather became not good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, it seems rain is limited to the \x01",
            "city area. It appears that if you go to Mainz\x01",
            "Mountain Path, the sky is refreshingly clear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe the weather\x01",
            "is a mere whim of\x01",
            "the Goddess.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C44")

    label("loc_1B8B")


    ChrTalk(
        0xFE,
        (
            "It seems rain is limited to the city area. \x01",
            "It appears that if you go to Mainz Mountain \x01",
            "Path, the sky is refreshingly clear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe the weather\x01",
            "is a mere whim of\x01",
            "the Goddess.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C44")

    Jump("loc_1F57")

    label("loc_1C49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_1D65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D05")

    ChrTalk(
        0xFE,
        (
            "Oh...\x01",
            "Is it time you go home?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please come visit anytime.\x01",
            "May the blessing of the Goddess\x01",
            "be on you all tomorrow too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01109FYes, see you again!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D60")

    label("loc_1D05")


    ChrTalk(
        0xFE,
        "It becomes dim after sunset.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please watch your steps\x01",
            "when descending the stairs.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D60")

    Jump("loc_1F57")

    label("loc_1D65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_1E06")

    ChrTalk(
        0xFE,
        (
            "The Sister who is scheduled to be appointed\x01",
            "today seems to have arrived moments ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think she's currently greeting\x01",
            "Archbishop Eralda.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F57")

    label("loc_1E06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1F57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ED9")

    ChrTalk(
        0xFE,
        "Welcome to Crossbell Cathedral.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In this place, Archbishop Eralda,\x01",
            "chief of the parish of Crossbell,\x01",
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
    Jump("loc_1F57")

    label("loc_1ED9")


    ChrTalk(
        0xFE,
        (
            "In this Crossbell Cathedral,\x01",
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

    label("loc_1F57")

    TalkEnd(0xFE)
    Return()

    # Function_7_9D8 end

    def Function_8_1F5B(): pass

    label("Function_8_1F5B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1FCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F79")
    Call(0, 9)
    Jump("loc_1FCA")

    label("loc_1F79")


    ChrTalk(
        0xFE,
        (
            "Then, Coutaz\x01",
            "and Hugott too\x01",
            "are safe, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh*, thank goodness...\x02",
    )

    CloseMessageWindow()

    label("loc_1FCA")

    Jump("loc_2D42")

    label("loc_1FCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_202B")

    ChrTalk(
        0xFE,
        "I wonder if the city children are safe...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Tamil, Hamil, everyone...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D42")

    label("loc_202B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_216E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20FA")

    ChrTalk(
        0xFE,
        (
            "I think that the most important\x01",
            "thing is the children's future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if independence will protect those...?\x01",
            "Or if it will threaten them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't know\x01",
            "anymore...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2169")

    label("loc_20FA")


    ChrTalk(
        0xFE,
        (
            "By being independent,\x01",
            "I wonder what will happen\x01",
            "to the children's futures...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't know\x01",
            "anymore...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2169")

    Jump("loc_2D42")

    label("loc_216E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_22CA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21A0")
    Call(0, 23)
    Return()

    label("loc_21A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_220D")

    ChrTalk(
        0xFE,
        (
            "I give cookies to the children\x01",
            "who come to mass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please attend too, if you like.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_22C5")

    label("loc_220D")


    ChrTalk(
        0xFE,
        (
            "As I thought, because of that raid incident, \x01",
            "it seems there're many persons who felt \x01",
            "worried about the present peace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope that such a thing\x01",
            "doesn't happen ever again...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22C5")

    Jump("loc_2D42")

    label("loc_22CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_239C")

    ChrTalk(
        0xFE,
        (
            "Today, Tamil and Hamil\x01",
            "had come to play, but they\x01",
            "went back home immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're in the middle of such an incident,\x01",
            "so their parents can be more at ease\x01",
            "if the children stay at home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D42")

    label("loc_239C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_23AA")
    Jump("loc_2D42")

    label("loc_23AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2499")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2443")

    ChrTalk(
        0xFE,
        "S-Stop you two!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Which one is the bad Tamil\x01",
            "who flipped up my skirt!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "He he, I wonder who☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "*pant pant*...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2494")

    label("loc_2443")


    ChrTalk(
        0xFE,
        (
            "E-Eehmm, eehm...\x01",
            "I-Is this one Tamil?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, but, maybe...\x01",
            "Are you Hamil?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2494")

    Jump("loc_2D42")

    label("loc_2499")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_26C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2620")

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
            "Children have a complete different motivation\x01",
            "to do things if they have interest for them or not.\x02",
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
            "...Well, to begin with, that it's\x01",
            "the most difficult thing, though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_26BB")

    label("loc_2620")


    ChrTalk(
        0xFE,
        (
            "Being taught how to do a\x01",
            "Sunday School lesson I\x01",
            "thought I grew a little, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To become a full fledged Sister,\x01",
            "I still need a lot of training.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26BB")

    Jump("loc_2D42")

    label("loc_26C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_26CE")
    Jump("loc_2D42")

    label("loc_26CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_26DC")
    Jump("loc_2D42")

    label("loc_26DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_26EA")
    Jump("loc_2D42")

    label("loc_26EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2877")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27E0")

    ChrTalk(
        0xFE,
        (
            "The person who was escorting Princess\x01",
            "Klaudia...Captain Julia...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Seeing her from up close, she\x01",
            "was a firm person like rumors go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, I somehow feel like I understand\x01",
            "why the women make a fuss for her.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2872")

    label("loc_27E0")


    ChrTalk(
        0xFE,
        (
            "Captain Julia is a pious person.\x01",
            "Even if she's busy, she comes\x01",
            "regularly to church.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, unexpectedly,\x01",
            "our habit could suit\x01",
            "her well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2872")

    Jump("loc_2D42")

    label("loc_2877")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2888")
    Call(0, 10)
    Jump("loc_2D42")

    label("loc_2888")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2899")
    Call(0, 11)
    Jump("loc_2D42")

    label("loc_2899")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_28A7")
    Jump("loc_2D42")

    label("loc_28A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_2A32")
    TurnDirection(0xFE, 0x153, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29A3")

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
            "#01100FYes! Lloyd and the others\x01",
            "have come to pick me up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uh uh, I'm glad for you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then, see you on the\x01",
            "next day of class.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01109FYes, byebye Sister!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A2D")

    label("loc_29A3")


    ChrTalk(
        0xFE,
        (
            "KeA, see you on the\x01",
            "next day of class.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Next time too, I'll bake\x01",
            "cookies for everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01109FYes, I'll look forward to it!\x02",
    )

    CloseMessageWindow()

    label("loc_2A2D")

    Jump("loc_2D42")

    label("loc_2A32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_2BA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B2E")

    ChrTalk(
        0xFE,
        (
            "I wonder if who entered the chapel\x01",
            "now is a new appointed Sister?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am a novice who has been \x01",
            "in service here for not even one\x01",
            "year, but finally, I have a junior too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "S-Somehow my heart\x01",
            "has stated racing...!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B9C")

    label("loc_2B2E")


    ChrTalk(
        0xFE,
        (
            "Finally, I too have a junior...\x01",
            "How exciting...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I must teach her many things\x01",
            "in a senior-like way.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B9C")

    Jump("loc_2D42")

    label("loc_2BA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2D42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C91")

    ChrTalk(
        0xFE,
        (
            "Oh, good morning.\x01",
            "Today we're holding\x01",
            "Sunday School classes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Could you be some of\x01",
            "the children's guardians?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The auditorium where we do classes is the\x01",
            "room to the right after entering the chapel.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2D42")

    label("loc_2C91")


    ChrTalk(
        0xFE,
        (
            "The auditorium where we do Sunday School classes \x01",
            "is the room to the right after entering the chapel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, if you like, why don't you\x01",
            "go have a look at the lessons?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D42")

    TalkEnd(0xFE)
    Return()

    # Function_8_1F5B end

    def Function_9_2D46(): pass

    label("Function_9_2D46")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xA,
        (
            "Tamil, Hamil, I'm really\x01",
            "glad you're safe...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "*sob*...ah, my Goddess.\x01",
            "Thank you for your mercy...!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xB)

    ChrTalk(
        0xB,
        (
            "H-Hey Sister, you don't have\x01",
            "to cry like that, you know...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Uh uh, thank you, Sister.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    ClearChrFlags(0xB, 0x10)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_9_2D46 end

    def Function_10_2E4B(): pass

    label("Function_10_2E4B")

    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3063")

    ChrTalk(
        0x8,
        (
            "#04400FSister Juju.\x01",
            "I heard something worrisome about the Mainz area\x01",
            "where tomorrow you're going on a business trip...\x02\x03",
            "#04403FLike that some time ago around those\x01",
            "parts there was a bizarre incident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yes, now that you mention it,\x01",
            "there was something like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I think it was a story about eye\x01",
            "witnesses of spirit-like things in \x01",
            "the old ruins of Mainz region.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04401F...Could you tell me a little more\x01",
            "in detail about that story?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yes, all right.\x01",
            "Although I don't know many details.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_314B")

    label("loc_3063")


    ChrTalk(
        0xA,
        (
            "...Right, then when I went to \x01",
            "Mainz together with Sister \x01",
            "Hatina before it was tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The father of a little girl called\x01",
            "Kimmy, worried about the class,\x01",
            "came marching in and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#04403F(You're digressing a little...)\x02",
    )

    CloseMessageWindow()

    label("loc_314B")

    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_10_2E4B end

    def Function_11_3154(): pass

    label("Function_11_3154")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_324F")

    ChrTalk(
        0xA,
        "Enough, Tamil...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hiding under the skirt of a girl is\x01",
            "something extremely naughty, you know!?\x02",
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
        "I'll try as much as possible to not do it anymore.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "N-Not as much as you can, you won't!!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_32F6")

    label("loc_324F")


    ChrTalk(
        0xB,
        (
            "But you know, Sister...\x01",
            "There's just one thing I want to tell you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Shouldn't you wear a pair\x01",
            "that are a little sexier?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "T-That's none of your business!!\x02",
    )

    CloseMessageWindow()

    label("loc_32F6")

    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_11_3154 end

    def Function_12_32FF(): pass

    label("Function_12_32FF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_33D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_331D")
    Call(0, 9)
    Jump("loc_33D1")

    label("loc_331D")


    ChrTalk(
        0xFE,
        (
            "Tch, she got out of tune.\x01",
            "Although we were the ones worried,\x01",
            "she suddenly started to cry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, oh well.\x01",
            "When she cools down, I'll use this\x01",
            "story to tease her next time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33D1")

    Jump("loc_3909")

    label("loc_33D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_33E4")
    Jump("loc_3909")

    label("loc_33E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3439")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33FF")
    Call(0, 13)
    Jump("loc_3434")

    label("loc_33FF")


    ChrTalk(
        0xFE,
        (
            "Hamil doesn't get it,\x01",
            "and I don't get it too...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3434")

    Jump("loc_3909")

    label("loc_3439")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3447")
    Jump("loc_3909")

    label("loc_3447")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3455")
    Jump("loc_3909")

    label("loc_3455")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3463")
    Jump("loc_3909")

    label("loc_3463")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_348B")

    ChrTalk(
        0xFE,
        "He he, which is who?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3909")

    label("loc_348B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_34CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34A6")
    Call(0, 14)
    Jump("loc_34C9")

    label("loc_34A6")


    ChrTalk(
        0xFE,
        "Alright, let's do it at once!\x02",
    )

    CloseMessageWindow()

    label("loc_34C9")

    Jump("loc_3909")

    label("loc_34CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_34DC")
    Jump("loc_3909")

    label("loc_34DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_34ED")
    Call(0, 15)
    Jump("loc_3909")

    label("loc_34ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3573")

    ChrTalk(
        0xFE,
        (
            "It seems that today those from\x01",
            "East Street are having class.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He he, I guess I'll peep\x01",
            "from that window there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3909")

    label("loc_3573")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_36E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3654")

    ChrTalk(
        0xFE,
        (
            "There isn't about anyone who can\x01",
            "distinguish between me and Hamil.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's why I occasionally pose\x01",
            "as Hamil and make pranks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But if it comes down to mom,\x01",
            "I get discovered immediately.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_36E3")

    label("loc_3654")


    ChrTalk(
        0xFE,
        (
            "When it comes down to mom,\x01",
            "even if I impersonate Hamil,\x01",
            "I get discovered immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ummm, does she have a method to tell us apart?\x02",
    )

    CloseMessageWindow()

    label("loc_36E3")

    Jump("loc_3909")

    label("loc_36E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3738")

    ChrTalk(
        0xFE,
        (
            "Orchis Tower was\x01",
            "really huuuge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Honestly, I felt small.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3909")

    label("loc_3738")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3749")
    Call(0, 11)
    Jump("loc_3909")

    label("loc_3749")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3757")
    Jump("loc_3909")

    label("loc_3757")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_3891")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_382D")

    ChrTalk(
        0xFE,
        (
            "Some time ago I thought\x01",
            "to try to flip up the rookie\x01",
            "Sister's skirt, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Somehow she dodged me\x01",
            "in a great skillful way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mrmrmr... It seems she's\x01",
            "not your common person.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_388C")

    label("loc_382D")


    ChrTalk(
        0xFE,
        (
            "To dodge my\x01",
            "skirt-flip...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That rookie Sister...\x01",
            "She doesn't seem an ordinary person.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_388C")

    Jump("loc_3909")

    label("loc_3891")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_3900")

    ChrTalk(
        0xFE,
        (
            "It seems that a rookie\x01",
            "Sister has just arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He he, I'll tease\x01",
            "her a little, later.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3909")

    label("loc_3900")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3909")

    label("loc_3909")

    TalkEnd(0xFE)
    Return()

    # Function_12_32FF end

    def Function_13_390D(): pass

    label("Function_13_390D")

    OP_4B(0xC, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xB,
        (
            "Somehow it seems the\x01",
            "adults are making a noise...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            ""Independence"...\x01",
            "What could that be?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hamil, studying is your forte.\x01",
            "Tell me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I-It's no use.\x01",
            "I don't get it too...\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xB, 0xFF)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_13_390D end

    def Function_14_39E4(): pass

    label("Function_14_39E4")

    OP_4B(0xC, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xB,
        (
            "...And so, if the Sister gets mad,\x01",
            "we'll do it like this...*mutter mutter*...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Eeeh, why do I have\x01",
            "to do that too...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Why not, I won't tell KeA that \x01",
            "you wetted the bed lately!\x02",
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

    # Function_14_39E4 end

    def Function_15_3AD4(): pass

    label("Function_15_3AD4")

    OP_4B(0xC, 0xFF)
    OP_4B(0xB, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BCA")

    ChrTalk(
        0xB,
        (
            "We were forced to take part in\x01",
            "Sunday School class too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "*sigh*, why did you have to say\x01",
            "to peep at the lesson, Hamil...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "N-No, no.\x01",
            "You were the one who said that, Tamil.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Don't casually\x01",
            "blame me, geez.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3C52")

    label("loc_3BCA")


    ChrTalk(
        0xC,
        (
            "But aren't you glad?\x01",
            "You could study a lot\x01",
            "and it was worth it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Unlike you, I hate studying!\x01",
            "Tch, that's why bookworms are...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C52")

    OP_4C(0xC, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_15_3AD4 end

    def Function_16_3C5B(): pass

    label("Function_16_3C5B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3CE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C79")
    Call(0, 9)
    Jump("loc_3CDF")

    label("loc_3C79")


    ChrTalk(
        0xFE,
        (
            "Yes, the city children\x01",
            "seem to be all fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, thank you for worrying\x01",
            "about us, Sister.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CDF")

    Jump("loc_44C6")

    label("loc_3CE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3CF2")
    Jump("loc_44C6")

    label("loc_3CF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3DAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D0D")
    Call(0, 13)
    Jump("loc_3DA6")

    label("loc_3D0D")


    ChrTalk(
        0xFE,
        (
            "I don't really get it what\x01",
            "independence is, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "According to what the city\x01",
            "adults where saying, it seems\x01",
            "to somehow be something serious...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DA6")

    Jump("loc_44C6")

    label("loc_3DAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3DB9")
    Jump("loc_44C6")

    label("loc_3DB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3DC7")
    Jump("loc_44C6")

    label("loc_3DC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3DD5")
    Jump("loc_44C6")

    label("loc_3DD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3E38")

    ChrTalk(
        0xFE,
        (
            "*pant, pant*...\x01",
            "W-Why even I have to...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "We'll be scolded for sure later...\x02",
    )

    CloseMessageWindow()
    Jump("loc_44C6")

    label("loc_3E38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3E8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E53")
    Call(0, 14)
    Jump("loc_3E87")

    label("loc_3E53")


    ChrTalk(
        0xFE,
        (
            "Uuh, I've got no choice...\x01",
            "Just this once, ok?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E87")

    Jump("loc_44C6")

    label("loc_3E8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_3E9A")
    Jump("loc_44C6")

    label("loc_3E9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_3EAB")
    Call(0, 15)
    Jump("loc_44C6")

    label("loc_3EAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3F01")

    ChrTalk(
        0xFE,
        (
            "Stop it I say...\x01",
            "I won't care if you'll get scodled by the Sister.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44C6")

    label("loc_3F01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4064")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FE0")

    ChrTalk(
        0xFE,
        (
            "It appears that mother and\x01",
            "father can properly tell us\x01",
            "twins apart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They say that they know just by looking at us, \x01",
            "although we have almost the same face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Parents can be amazing...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_405F")

    label("loc_3FE0")


    ChrTalk(
        0xFE,
        (
            "Mother and father say that they\x01",
            "can tell who is me and who is\x01",
            "Tamil just by looking at us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Parents can be amazing...\x02",
    )

    CloseMessageWindow()

    label("loc_405F")

    Jump("loc_44C6")

    label("loc_4064")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_40EE")

    ChrTalk(
        0xFE,
        (
            "*sigh*, it was a rare chance\x01",
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
    Jump("loc_44C6")

    label("loc_40EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4220")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4197")

    ChrTalk(
        0xFE,
        (
            "Tamil, while playing\x01",
            "hide and see, hid\x01",
            "under the Sister's skirt.\x02",
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
    Jump("loc_421B")

    label("loc_4197")


    ChrTalk(
        0xFE,
        (
            "Even so...\x01",
            "When they get angry at Tamil,\x01",
            "I feel they're getting angry at me too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Being twins is somehow\x01",
            "a disadvantage...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_421B")

    Jump("loc_44C6")

    label("loc_4220")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_422E")
    Jump("loc_44C6")

    label("loc_422E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_444A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43EB")
    TurnDirection(0xFE, 0x153, 0)

    ChrTalk(
        0xFE,
        (
            "Ah, KeA!\x01",
            "Is senior class over?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01109FYes, it just ended now.\x02\x03",
            "#01100FHamil, were you playing until\x01",
            "now after classes were over?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Y-Yes.\x01",
            "With Tamil.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way, even you can\x01",
            "already perfectly understand\x01",
            "that I am Hamil, eh, KeA?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01105FEeh, why?\x02\x03",
            "#01109FYou have the same face of Tamil,\x01",
            "but Hamil is Hamil, I know that.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "(Man, it makes me super happy...!)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4445")

    label("loc_43EB")

    TurnDirection(0xFE, 0x153, 0)

    ChrTalk(
        0xFE,
        "Ehhm, please be careful, KeA.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01109FYes. Let's play all together again!\x02",
    )

    CloseMessageWindow()

    label("loc_4445")

    Jump("loc_44C6")

    label("loc_444A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_44BD")

    ChrTalk(
        0xFE,
        (
            "Don't, Tamil...\x01",
            "What if she's a scary person?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I won't care if she'll\x01",
            "get angry at you, ok?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44C6")

    label("loc_44BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_44C6")

    label("loc_44C6")

    TalkEnd(0xFE)
    Return()

    # Function_16_3C5B end

    def Function_17_44CA(): pass

    label("Function_17_44CA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44DF")
    Call(0, 18)
    Jump("loc_4548")

    label("loc_44DF")


    ChrTalk(
        0xFE,
        (
            "*sigh*...\x01",
            "I guess if KeA says it,\x01",
            "it can't be helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From now on, I'll try\x01",
            "to do my homework.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4548")

    TalkEnd(0xFE)
    Return()

    # Function_17_44CA end

    def Function_18_454C(): pass

    label("Function_18_454C")

    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0xD,
        (
            "The Sister got slightly\x01",
            "mad at me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "You didn't do your homework,\x01",
            "so you got what you deserved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "*sigh*, in the past she was quite lenient,\x01",
            "but after we started senior class, she\x01",
            "became strict, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01105FNext time you have to properly\x01",
            "do your homework, ok?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    TurnDirection(0xD, 0x153, 500)
    Sleep(500)

    ChrTalk(
        0xD,
        "Yeees...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F(A-As expected from KeA...)\x02",
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    TurnDirection(0xD, 0xE, 0)
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x0, 5)
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_18_454C end

    def Function_19_46DF(): pass

    label("Function_19_46DF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46F4")
    Call(0, 18)
    Jump("loc_4731")

    label("loc_46F4")


    ChrTalk(
        0xFE,
        (
            "Pfft, you too lost face getting\x01",
            "told by this child, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4731")

    TalkEnd(0xFE)
    Return()

    # Function_19_46DF end

    def Function_20_4735(): pass

    label("Function_20_4735")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48A6")
    TurnDirection(0xFE, 0x153, 0)

    ChrTalk(
        0xFE,
        (
            "Oh, Kea, are going\x01",
            "back home now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01110FYes! Are you going home to, Burik?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yeah, and since I'm here,\x01",
            "I thought to buy Crossbell Times\x01",
            "on West Street and go back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "KeA...\x01",
            "I won't lose in the next class!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01111FHoee, was it a matter of victory or defeat?\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "N-No, it's nothing.\x01",
            "Forget it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_492E")

    label("loc_48A6")


    ChrTalk(
        0xFE,
        (
            "When KeA attended\x01",
            "senior class, I was\x01",
            "really shocked, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Taking this as a chance, I thought\x01",
            "to study properly once again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_492E")

    TalkEnd(0xFE)
    Return()

    # Function_20_4735 end

    def Function_21_4932(): pass

    label("Function_21_4932")

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

    def lambda_4A79():
        OP_9B(0x0, 0x101, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4A79)
    Sleep(100)

    def lambda_4A91():
        OP_9B(0x0, 0x102, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4A91)
    Sleep(100)

    def lambda_4AA9():
        OP_9B(0x0, 0x103, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4AA9)
    Sleep(100)

    def lambda_4AC1():
        OP_9B(0x0, 0x104, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4AC1)
    Sleep(100)

    def lambda_4AD9():
        OP_9B(0x0, 0x109, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4AD9)
    Sleep(100)

    def lambda_4AF1():
        OP_9B(0x0, 0x105, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4AF1)
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

    def lambda_4B70():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4B70)
    Sleep(50)

    def lambda_4B80():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4B80)
    Sleep(50)

    def lambda_4B90():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4B90)
    Sleep(50)

    def lambda_4BA0():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4BA0)
    Sleep(50)

    def lambda_4BB0():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4BB0)
    Sleep(50)

    def lambda_4BC0():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4BC0)
    Sleep(50)

    def lambda_4BD0():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4BD0)
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
            "#00003F#11P...Already evening, eh?\x02\x03",
            "#00001FI'd like to submit the written report by the end of\x01",
            "today and we must somehow collect information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PYes...\x01",
            "I hope there're some leads.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4D61")

    ChrTalk(
        0x103,
        (
            "#00200FIn any case, why don't we\x01",
            "try to visit Miss Ries or\x01",
            "teacher Marble?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#11PYeah, first, let's visit the\x01",
            "Sunday School classroom.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DE9")

    label("loc_4D61")


    ChrTalk(
        0x103,
        (
            "#00200FIn any case, why don't we\x01",
            "try to visit teacher Marble?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#11PYeah, I hope she hasn't\x01",
            "got Sunday School lessons...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DE9")

    ClearChrFlags(0x10, 0x80)

    NpcTalk(
        0x10,
        "Man's Voice",
        "Oh, everyone...\x02",
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

    def lambda_4E89():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4E89)
    Sleep(0)

    def lambda_4E99():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4E99)
    Sleep(0)

    def lambda_4EA9():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4EA9)
    Sleep(0)

    def lambda_4EB9():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4EB9)
    Sleep(0)

    def lambda_4EC9():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4EC9)
    Sleep(0)

    def lambda_4ED9():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4ED9)
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16C, 1)), scpexpr(EXPR_END)), "loc_5213")

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
            "Yes, since the Trade Conference,\x01",
            "right?\x02\x03",
            "Oh, by the way, you had come to\x01",
            "the office at noon, I was told?\x02\x03",
            "I'm sorry. You came\x01",
            "on purpose, and yet...\x02",
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
            "#00012F#6PNo...\x01",
            "However, you seem busy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F#6PIt seems you're collaborating in\x01",
            "writing the constitution draft?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#02210F#11PWell, ha ha...\x02\x03",
            "Because the mayor asked me enthusiastically,\x01",
            "I wasn't really able to turn him down.\x02\x03",
            "#02200FWell, even at a personal level,\x01",
            "I agree with his ideas.\x02\x03",
            "Maybe they're difficult to realize, but...\x01",
            "At least I want to give him a hand.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_575C")

    label("loc_5213")


    ChrTalk(
        0x102,
        (
            "#00104F#6PLong time no see.\x02\x03",
            "#00108FIt seems that recently you\x01",
            "have been quite busy...?\x02",
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
            "Well, ha ha...\x02\x03",
            "...Actually, I've been asked \x01",
            "by the mayor to...\x02\x03",
            "Write the constitution draft for\x01",
            "the national independence.\x02",
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
        "#00007F#6PEEH!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F#6PA "constitution"...\x01",
            "It's not an autonomous state law, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x109, 500)

    ChrTalk(
        0x102,
        (
            "#00104F#11PA "constitution" is the fundamental\x01",
            "law that establishes the basic\x01",
            "conditions of a state's existence.\x02\x03",
            "#00100FIt doesn't allow other states interference in\x01",
            "the supreme laws that establish a nation's\x01",
            "sovereignty, structure and fundamental principles.\x02\x03",
            "It's something absolutely indispensable\x01",
            "for having the appearance of a state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F#6P...Right...\x01",
            "Another complicated thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#6PHowever, I think that someone like\x01",
            "Lawyer Ian is truly suited for it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#02210F#11PHa ha...\x01",
            "Because the mayor asked me enthusiastically,\x01",
            "I wasn't really able to turn him down.\x02\x03",
            "#02200FWell, even at a personal level,\x01",
            "I agree with his ideas.\x02\x03",
            "Maybe they're difficult to realize, but...\x01",
            "At least I want to give him a hand.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_575C")


    def lambda_5761():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5761)

    ChrTalk(
        0x101,
        "#00002F#6PIs that so...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#6PCould it be that with taking a breather you\x01",
            "also took the chance to come to pray?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#02210F#11PYes, I had reached an impasse but it\x01",
            "seems this has been a nice change of mood.\x02\x03",
            "#02202FReally, it's not bad for man to pray to\x01",
            "the Goddess in times of trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#6PHa ha...\x01",
            "Indeed, you can say that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00104F#6PThank you so much for all your work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#02210F#11PHa ha, likewise.\x02\x03",
            "#02200FIt's already evening, but...\x01",
            "Could you have come due to a job?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PYes, there's something we'd like to\x01",
            "consult with some people of the Church.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#02203F#11PHm, it seems you have your own circumstances.\x02\x03",
            "#02200FI'm busy too, however...\x01",
            "If there's something I could help you with,\x01",
            "do not hesitate to pay a visit to my office.\x02\x03",
            "You're all very welcome.\x02",
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
        "#10100F#6PPlease be careful on your way back!\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    OP_0D()

    def lambda_5B12():

        label("loc_5B12")

        TurnDirection(0x101, 0x10, 500)
        Yield()
        Jump("loc_5B12")

    QueueWorkItem2(0x101, 2, lambda_5B12)

    def lambda_5B24():

        label("loc_5B24")

        TurnDirection(0x102, 0x10, 500)
        Yield()
        Jump("loc_5B24")

    QueueWorkItem2(0x102, 2, lambda_5B24)

    def lambda_5B36():

        label("loc_5B36")

        TurnDirection(0x103, 0x10, 500)
        Yield()
        Jump("loc_5B36")

    QueueWorkItem2(0x103, 2, lambda_5B36)

    def lambda_5B48():

        label("loc_5B48")

        TurnDirection(0x104, 0x10, 500)
        Yield()
        Jump("loc_5B48")

    QueueWorkItem2(0x104, 2, lambda_5B48)

    def lambda_5B5A():

        label("loc_5B5A")

        TurnDirection(0x109, 0x10, 500)
        Yield()
        Jump("loc_5B5A")

    QueueWorkItem2(0x109, 2, lambda_5B5A)

    def lambda_5B6C():

        label("loc_5B6C")

        TurnDirection(0x105, 0x10, 500)
        Yield()
        Jump("loc_5B6C")

    QueueWorkItem2(0x105, 2, lambda_5B6C)
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
        "#00001F#11P...He seems to be busy.\x02",
    )

    CloseMessageWindow()

    def lambda_5C02():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5C02)
    Sleep(0)

    def lambda_5C12():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5C12)
    Sleep(0)

    def lambda_5C22():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5C22)
    Sleep(0)

    def lambda_5C32():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5C32)
    Sleep(0)

    def lambda_5C42():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5C42)
    Sleep(0)

    def lambda_5C52():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5C52)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x102,
        (
            "#00103F#12PYes, writing a constitution draft\x01",
            "can be really proving...\x02\x03",
            "#00101FIf you publish something poor, the Empire\x01",
            "and Republic could say that it doesn't\x01",
            "have that much of a persuasive power...\x02",
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
            "#10304F#6PHu hu, a different kind of worries\x01",
            "compared to our busyness, right?\x02\x03",
            "#10300FBy the way...\x01",
            "Are we going to visit the Sunday School classroom?\x02",
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

    # Function_21_4932 end

    def Function_22_5E64(): pass

    label("Function_22_5E64")

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
            "#04400FI don't want other \x01",
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
        "#00103F#12P...Pardon our intrusion.\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x1F4)
    Sound(121, 0, 100, 0)
    OP_71(0x1, 0x0, 0x14, 0x0, 0x0)
    OP_79(0x1)

    def lambda_5FF3():
        OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_5FF3)
    OP_9B(0x0, 0x8, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0x8, 3)

    def lambda_6017():
        OP_95(0x102, -11400, 500, 14750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6017)
    Sleep(200)

    def lambda_6034():
        OP_95(0x103, -11400, 500, 13250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6034)
    Sleep(100)

    def lambda_6051():
        OP_95(0x101, -11400, 500, 14000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6051)
    Sleep(100)

    def lambda_606E():
        OP_95(0x104, -11400, 500, 14750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_606E)
    Sleep(100)

    def lambda_608B():
        OP_95(0x109, -11400, 500, 13250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_608B)
    Sleep(200)

    def lambda_60A8():
        OP_95(0x105, -11400, 500, 14000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_60A8)
    Sleep(500)
    FadeToDark(1000, 0, -1)

    def lambda_60CF():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_60CF)
    Sleep(50)

    def lambda_60E3():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_60E3)
    Sleep(50)

    def lambda_60F7():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_60F7)
    Sleep(150)

    def lambda_610B():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 3, lambda_610B)
    Sleep(50)

    def lambda_611F():
        OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_611F)
    Sleep(50)

    def lambda_6133():
        OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 3, lambda_6133)
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

    # Function_22_5E64 end

    def Function_23_6183(): pass

    label("Function_23_6183")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_636F")

    ChrTalk(
        0xA,
        "Today is mass day.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Why don't you take part\x01",
            "in it too, everyone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(I wonder if she would appear as \x01",
            "the "Sister" entry in the pageant...?)\x02\x03",
            "#00000FExcuse us.\x01",
            "There's something I want to ask you...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You asked her to participate \x01",
            "in the charity event pageant.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            "E-Eeh...?\x01",
            "I, in a beauty contest...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I-It's impossible.\x01",
            "Someone like me has\x01",
            "nothing like charm...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm sorry, please try to\x01",
            "invite another person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FI-I see...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x199, 1)
    Jump("loc_63F0")

    label("loc_636F")


    ChrTalk(
        0xA,
        (
            "I-It's impossible for someone like\x01",
            "me to show up in a beauty contest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I think there're other more\x01",
            "appropriate persons.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63F0")

    TalkEnd(0xA)
    Return()

    # Function_23_6183 end

    def Function_24_63F4(): pass

    label("Function_24_63F4")

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
            "　  go around for the chapel.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_24_63F4 end

    def Function_25_648C(): pass

    label("Function_25_648C")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001F...At any rate, let's try going\x01",
            "to Miss Ries's place. Maybe\x01",
            "we can get some information.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 370, 0, -7350, 0)
    EventEnd(0x4)
    Return()

    # Function_25_648C end

    SaveToFile()

Try(main)
