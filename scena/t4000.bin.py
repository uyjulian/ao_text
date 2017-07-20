from ScenarioHelper import *

def main():
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
        "Sister · Lease",       # 1
        "Priest Roland",           # 2
        "Sister Juzy",     # 3
        "Tamil",                 # 4
        "Hamill",                 # 5
        "Pruna",               # 6
        "Linally",               # 7
        "Brick",               # 8
        "Ian lawyer",           # 9
        "Mainz Mountain Road",           # 10
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
        "Function_8_1CCC",         # 08, 8
        "Function_9_2999",         # 09, 9
        "Function_10_2A9B",        # 0A, 10
        "Function_11_2D36",        # 0B, 11
        "Function_12_2EC6",        # 0C, 12
        "Function_13_34B3",        # 0D, 13
        "Function_14_3595",        # 0E, 14
        "Function_15_368A",        # 0F, 15
        "Function_16_3814",        # 10, 16
        "Function_17_4017",        # 11, 17
        "Function_18_4093",        # 12, 18
        "Function_19_420D",        # 13, 19
        "Function_20_4257",        # 14, 20
        "Function_21_443C",        # 15, 21
        "Function_22_56F3",        # 16, 22
        "Function_23_5A12",        # 17, 23
        "Function_24_5C54",        # 18, 24
        "Function_25_5CD6",        # 19, 25
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_AEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A9C")

    ChrTalk(
        0xFE,
        (
            "That pale bright tree,\x01",
            "On what reasons crossover\x01",
            "Did it appear?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Will bring light to this land,\x01",
            "Or will it cause disaster …?\x01",
            "We are immune to clerics as well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_AEA")

    label("loc_A9C")


    ChrTalk(
        0xFE,
        "That pale bright tree emerges ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Is this also a goddess's suggestion?\x02",
    )

    CloseMessageWindow()

    label("loc_AEA")

    Jump("loc_1CC8")

    label("loc_AEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_BEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BA6")

    ChrTalk(
        0xFE,
        (
            "Suddenly, if you think the barrier disappeared,\x01",
            "In the town there is a thing of armor figure\x01",
            "It is said that he started to wander around … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is President Dieter's\x01",
            "If it is intention,\x01",
            "It is absolutely unacceptable practice.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_BE5")

    label("loc_BA6")


    ChrTalk(
        0xFE,
        (
            "To make the town wander around the city ……\x01",
            "It is absolutely unacceptable practice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BE5")

    Jump("loc_1CC8")

    label("loc_BEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_D2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC4")

    ChrTalk(
        0xFE,
        (
            "A speech by Mr. Dieter\x01",
            "I heard that it was held in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because the crossbell is independent,\x01",
            "The confusion on the continent is\x01",
            "Is not it inevitable?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Goddess, please lead people … …\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D27")

    label("loc_CC4")


    ChrTalk(
        0xFE,
        (
            "No longer with the Empire and the Republic\x01",
            "Collisions will be inevitable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Goddess, please lead people … …\x02",
    )

    CloseMessageWindow()

    label("loc_D27")

    Jump("loc_1CC8")

    label("loc_D2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_E99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E08")

    ChrTalk(
        0xFE,
        (
            "Today at the chapel inside the cathedral\x01",
            "We are doing masses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To the people who were the victim of the raid incident\x01",
            "It is an event that wishes guidance of the goddess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If your time is okay,\x01",
            "Everyone please participate by all means.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E94")

    label("loc_E08")


    ChrTalk(
        0xFE,
        (
            "Mourning the previous attacks,\x01",
            "For today's mass\x01",
            "Many worshipers are visiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If your time is okay,\x01",
            "Everyone please participate by all means.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_E94")

    Jump("loc_1CC8")

    label("loc_E99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_FB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F37")

    ChrTalk(
        0xFE,
        (
            "From last night, gunshot and explosion sound etc\x01",
            "I hear it frequently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Battle of Mainz direction\x01",
            "To pretty intense things\x01",
            "It seems to be getting …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FB4")

    label("loc_F37")


    ChrTalk(
        0xFE,
        (
            "anyway……\x01",
            "Should the armed group go so far\x01",
            "It does not necessarily have to come down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "About the protection of the cathedral\x01",
            "I have to consider urgently … ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FB4")

    Jump("loc_1CC8")

    label("loc_FB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1035")

    ChrTalk(
        0xFE,
        (
            "Today in the entire cross-autonomous state\x01",
            "It seems that it is raining.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a matter of fact the person who goes to the highway\x01",
            "It seems to be small.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CC8")

    label("loc_1035")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_10BA")

    ChrTalk(
        0xFE,
        (
            "my mother……\x01",
            "Sister Juju\x01",
            "It is really liked by children.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That is a kind of talent.\x01",
            "I am jealous.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CC8")

    label("loc_10BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_120A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1195")

    ChrTalk(
        0xFE,
        (
            "Rosenberg Studio ……\x01",
            "It's a name to hear from time to time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although it is a workshop which has been in long ago,\x01",
            "The fact that that Lord visits the Cathedral\x01",
            "I think that it was not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What kind of person is\x01",
            "I guess you are coming.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1205")

    label("loc_1195")


    ChrTalk(
        0xFE,
        (
            "The Lord of Rosenberg workshop\x01",
            "I have not visited the cathedral.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What kind of person is\x01",
            "I guess you are coming.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1205")

    Jump("loc_1CC8")

    label("loc_120A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_1280")

    ChrTalk(
        0xFE,
        (
            "Tamil and Hamir are\x01",
            "You seem to have returned home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, at least\x01",
            "I have to start cleaning in the evening …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CC8")

    label("loc_1280")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_1404")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1374")

    ChrTalk(
        0xFE,
        (
            "Ian, occasionally Oh\x01",
            "It is on the cathedral.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Especially difficult cases\x01",
            "When handling, etc.,\x01",
            "You seem to be getting along well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What is it now\x01",
            "I do not know whether I have any problems … …\x01",
            "I want you to work hard.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13FF")

    label("loc_1374")


    ChrTalk(
        0xFE,
        (
            "Ian, occasionally Oh\x01",
            "It is on the cathedral.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What is it now\x01",
            "I do not know whether I have any problems … …\x01",
            "I want you to work hard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13FF")

    Jump("loc_1CC8")

    label("loc_1404")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_154E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14CA")

    ChrTalk(
        0xFE,
        (
            "Recently, the incomprehensible material in various places\x01",
            "I was witnessed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The guard is also located in a remote location\x01",
            "Do not enter alone\x01",
            "It seems to be calling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Everyone please be careful enough.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1549")

    label("loc_14CA")


    ChrTalk(
        0xFE,
        (
            "These days, in various places\x01",
            "The incomprehensible monster\x01",
            "I was witnessed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To prevent you from entering a place where it is far away,\x01",
            "Everyone please be careful enough.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1549")

    Jump("loc_1CC8")

    label("loc_154E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_168F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15FF")

    ChrTalk(
        0xFE,
        (
            "As I mentioned earlier,\x01",
            "His Highness, Claudia\x01",
            "I came to the cathedral.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since being greeted by Eldar Archbishop,\x01",
            "You seem to have headed to the cemetery.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_168A")

    label("loc_15FF")


    ChrTalk(
        0xFE,
        (
            "Highness Prince Claudia\x01",
            "To the Orkis Tower earlier\x01",
            "It seems that it was headed for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Where to go today's plenary session ……\x01",
            "Trends in your Highness are also worrisome.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_168A")

    Jump("loc_1CC8")

    label("loc_168F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1802")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1785")

    ChrTalk(
        0xFE,
        (
            "The state of the unveiling ceremony,\x01",
            "Even from here on the hill\x01",
            "I was able to see … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Orkis Tower, which took off the veil,\x01",
            "It was a word of excitement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That kind of building\x01",
            "What is made by human hand … …\x01",
            "No, I can not hide surprises.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17FD")

    label("loc_1785")


    ChrTalk(
        0xFE,
        (
            "The figure of Orkis Tower,\x01",
            "It was a word of excitement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That that was made with human hand … …\x01",
            "No, I can not hide surprises.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17FD")

    Jump("loc_1CC8")

    label("loc_1802")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_187E")

    ChrTalk(
        0xFE,
        (
            "For the trade meeting,\x01",
            "Security is being strengthened in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I also looked around the cathedral\x01",
            "I think I will be careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CC8")

    label("loc_187E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_19F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_195B")

    ChrTalk(
        0xFE,
        "Today it was unfortunate weather.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, it seems only rainy areas are urban areas,\x01",
            "If you go to the Mainz mountain road\x01",
            "It is a refreshing sunny pattern.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The weather is mere,\x01",
            "Maybe it is a capricious goddess\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19F1")

    label("loc_195B")


    ChrTalk(
        0xFE,
        (
            "It seems that only rainy areas are urban areas,\x01",
            "If you go to the Mainz mountain road\x01",
            "It is a refreshing sunny pattern.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The weather is mere,\x01",
            "Maybe it is a capricious goddess\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19F1")

    Jump("loc_1CC8")

    label("loc_19F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_1AFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AA3")

    ChrTalk(
        0xFE,
        (
            "Gee\x01",
            "Is it about time you left?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please come again.\x01",
            "To everyone tomorrow\x01",
            "The goddess's protection …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01109FYes, again!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1AFA")

    label("loc_1AA3")


    ChrTalk(
        0xFE,
        "The day is getting dim.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When going down the stairs,\x01",
            "Please note your feet.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AFA")

    Jump("loc_1CC8")

    label("loc_1AFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_1B93")

    ChrTalk(
        0xFE,
        (
            "Sister who was scheduled to go to work today\x01",
            "It seems that you saw it before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now to Archbishop Ellarda\x01",
            "It will be a place to say hello.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CC8")

    label("loc_1B93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1CC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C4D")

    ChrTalk(
        0xFE,
        "Welcome to Crossbell Cathedral.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Here, the head of the crossbell parish\x01",
            "Archbishop Ellarda\x01",
            "I am preaching the teachings of Shichao.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On the premises,\x01",
            "Please be quiet.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1CC8")

    label("loc_1C4D")


    ChrTalk(
        0xFE,
        (
            "Here at the Crossbell Cathedral,\x01",
            "Archbishop Ellarda\x01",
            "I am preaching the teachings of Shichao.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On the premises,\x01",
            "Please be quiet.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CC8")

    TalkEnd(0xFE)
    Return()

    # Function_7_9D8 end

    def Function_8_1CCC(): pass

    label("Function_8_1CCC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1D53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CEA")
    Call(0, 9)
    Jump("loc_1D4E")

    label("loc_1CEA")


    ChrTalk(
        0xFE,
        (
            "Well then, Kouta and\x01",
            "Yuggots\x01",
            "There is no injury, is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ha, it was really nice …\x02",
    )

    CloseMessageWindow()

    label("loc_1D4E")

    Jump("loc_2995")

    label("loc_1D53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1DAB")

    ChrTalk(
        0xFE,
        "Is the children in the city safe …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Tamil, Hamill, everyone ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2995")

    label("loc_1DAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1EE9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E75")

    ChrTalk(
        0xFE,
        (
            "The most important thing is,\x01",
            "I think that it is the future of children.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Independence is what protects them … …?\x01",
            "Or is it threatening?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do not understand\x01",
            "I got it …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1EE4")

    label("loc_1E75")


    ChrTalk(
        0xFE,
        (
            "By being independent,\x01",
            "The future of children\x01",
            "What will happen …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do not understand\x01",
            "I got it …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EE4")

    Jump("loc_2995")

    label("loc_1EE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_201E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F1B")
    Call(0, 23)
    Return()

    label("loc_1F1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F8C")

    ChrTalk(
        0xFE,
        (
            "For children who came to the mass\x01",
            "I'm giving you a cookie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "If you do not mind, please join us.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2019")

    label("loc_1F8C")


    ChrTalk(
        0xFE,
        (
            "After all, in that raid incident\x01",
            "Those who felt uneasy about the current peace\x01",
            "There seems to be quite a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Never again, such a thing\x01",
            "I do not have to get up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2019")

    Jump("loc_2995")

    label("loc_201E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_20D8")

    ChrTalk(
        0xFE,
        (
            "Tamil and Hamir are here today\x01",
            "I had come to play,\x01",
            "I immediately went home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Such a case is in the middle of happening,\x01",
            "My parents who stayed at home also\x01",
            "You can be relieved.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2995")

    label("loc_20D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_20E6")
    Jump("loc_2995")

    label("loc_20E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_21FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_218E")

    ChrTalk(
        0xFE,
        "And stop, you guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I turned over my skirt,\x01",
            "Which is bad Tamil-kun! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "To, which way ~ ☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Ha Ha……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_21F8")

    label("loc_218E")


    ChrTalk(
        0xFE,
        (
            "Er, um … um …\x01",
            "Is this here Tamil?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There, but after all, …\x01",
            "Is this Hamir-kun?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21F8")

    Jump("loc_2995")

    label("loc_21FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_23CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_232E")

    ChrTalk(
        0xFE,
        (
            "Yesterday, Sister Marble\x01",
            "Have you taught me how to teach classes\x01",
            "I noticed ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Children, whether they are interested or not\x01",
            "Motivation is different at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In order to teach something,\x01",
            "It will be interesting to it\x01",
            "It is the most important thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "… Well, in the first place\x01",
            "That is the most difficult thing, though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_23C5")

    label("loc_232E")


    ChrTalk(
        0xFE,
        (
            "How to teach Sunday school classes\x01",
            "I was taught,\x01",
            "I thought that I could grow a bit … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To become a sister of one serving,\x01",
            "I do not have enough training yet.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23C5")

    Jump("loc_2995")

    label("loc_23CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_23D8")
    Jump("loc_2995")

    label("loc_23D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_23E6")
    Jump("loc_2995")

    label("loc_23E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_23F4")
    Jump("loc_2995")

    label("loc_23F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_254B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24B6")

    ChrTalk(
        0xFE,
        (
            "I had escorted Princess Claudia\x01",
            "A man named Julia Julia … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As rumored to see close,\x01",
            "It was the one who made it kiriri.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, the women are making noise\x01",
            "I feel like understanding.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2546")

    label("loc_24B6")


    ChrTalk(
        0xFE,
        (
            "Assistant Yulia is busy\x01",
            "It is indispensable to attend church\x01",
            "He is a devout person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, unexpected father clothing also\x01",
            "It suits you\x01",
            "You might do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2546")

    Jump("loc_2995")

    label("loc_254B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_255C")
    Call(0, 10)
    Jump("loc_2995")

    label("loc_255C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_256D")
    Call(0, 11)
    Jump("loc_2995")

    label("loc_256D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_257B")
    Jump("loc_2995")

    label("loc_257B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_2700")
    TurnDirection(0xFE, 0x153, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2674")

    ChrTalk(
        0xFE,
        (
            "Oh, Ka'aa-chan.\x01",
            "You are already home today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01100FYup! Lloyd's\x01",
            "He came to pick me up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hehe, that was nice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well then,\x01",
            "Also on the next class day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01109FYeah, yeah yeah Sister!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_26FB")

    label("loc_2674")


    ChrTalk(
        0xFE,
        (
            "Ka'a-chan,\x01",
            "Also on the next class day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Next time, to everyone again\x01",
            "I will bake cookies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01109FYes, I am looking forward to it!\x02",
    )

    CloseMessageWindow()

    label("loc_26FB")

    Jump("loc_2995")

    label("loc_2700")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_284A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27D5")

    ChrTalk(
        0xFE,
        (
            "I went into the chapel right now\x01",
            "Is it a new sister?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I, working here\x01",
            "It is a new rice that has not been less than a year ago,\x01",
            "Finally I have juniors …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Is not it something?\x01",
            "I've been throbbing … ….!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2845")

    label("loc_27D5")


    ChrTalk(
        0xFE,
        (
            "My juniors are finally here ……\x01",
            "I've been throbbing … ….!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He seems to be a seniors, and various things\x01",
            "I will not tell you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2845")

    Jump("loc_2995")

    label("loc_284A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2995")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2913")

    ChrTalk(
        0xFE,
        (
            "Oh, hello there.\x01",
            "Today Sunday school classes\x01",
            "It is done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Did you mean …\x01",
            "Are you parents of children?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The auditorium who is doing classes\x01",
            "I entered the chapel and it is the right room.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2995")

    label("loc_2913")


    ChrTalk(
        0xFE,
        (
            "The auditorium which is doing class on Sunday school\x01",
            "I entered the chapel and it is the right room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, if you do not mind, let me see the situation of the lesson\x01",
            "Why do not you look into it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2995")

    TalkEnd(0xFE)
    Return()

    # Function_8_1CCC end

    def Function_9_2999(): pass

    label("Function_9_2999")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xA,
        (
            "Tamil, Hamir,\x01",
            "It was truly okay and good!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Dusk … … Oh, Goddess.\x01",
            "I appreciate mercy … …!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xB)

    ChrTalk(
        0xB,
        (
            "Wait a minute, Sister,\x01",
            "Even if you do not cry like that … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Hehe, Thank you Sister.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    ClearChrFlags(0xB, 0x10)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_9_2999 end

    def Function_10_2A9B(): pass

    label("Function_10_2A9B")

    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C56")

    ChrTalk(
        0x8,
        (
            "#04400FSister Juju.\x01",
            "About Mainz direction to go on business tomorrow\x01",
            "I heard about the story you are interested in … …\x02\x03",
            "#04403FA while ago, at around that\x01",
            "There were strange incidents … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Oh, that's true\x01",
            "There was such a story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "In the old ruins of Mainz direction,\x01",
            "Something like a ghost was witnessed\x01",
            "It seems like it was a story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04401F…… That story, a bit more\x01",
            "May I ask you a favor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well, that's fine.\x01",
            "I am not familiar with it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2D2D")

    label("loc_2C56")


    ChrTalk(
        0xA,
        (
            "……Yes Yes,\x01",
            "Along with Sister Hatina before\x01",
            "It was serious when I went to Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Kimi-chan's a girl\x01",
            "Was my father interested in the lesson?\x01",
            "I got on board ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#04403F(I am derailing a bit … …)\x02",
    )

    CloseMessageWindow()

    label("loc_2D2D")

    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_10_2A9B end

    def Function_11_2D36(): pass

    label("Function_11_2D36")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E23")

    ChrTalk(
        0xA,
        "Already, Tamil Kimi … ….!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "To get into a woman 's skirt,\x01",
            "Harench It is a very ruthless work! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Hey, sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I will try not to do it anymore.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "It is absolutely not possible!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2EBD")

    label("loc_2E23")


    ChrTalk(
        0xB,
        (
            "But sister …\x01",
            "I just want to say something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I wish I had a bit more Iloche\x01",
            "You should do better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Oh, it's an unnecessary care! It is!\x02",
    )

    CloseMessageWindow()

    label("loc_2EBD")

    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_11_2D36 end

    def Function_12_2EC6(): pass

    label("Function_12_2EC6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2F91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EE4")
    Call(0, 9)
    Jump("loc_2F8C")

    label("loc_2EE4")


    ChrTalk(
        0xFE,
        (
            "Well, I guess it is going crazy.\x01",
            "Although I was worried about this,\x01",
            "I'm crying Ichinari.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, oh well.\x01",
            "By the time this popularity has cooled down\x01",
            "To tease frightening material.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F8C")

    Jump("loc_34AF")

    label("loc_2F91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2F9F")
    Jump("loc_34AF")

    label("loc_2F9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2FF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FBA")
    Call(0, 13)
    Jump("loc_2FF3")

    label("loc_2FBA")


    ChrTalk(
        0xFE,
        (
            "Do not know Hamill,\x01",
            "I do not know for sure …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FF3")

    Jump("loc_34AF")

    label("loc_2FF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3006")
    Jump("loc_34AF")

    label("loc_3006")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3014")
    Jump("loc_34AF")

    label("loc_3014")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3022")
    Jump("loc_34AF")

    label("loc_3022")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3052")

    ChrTalk(
        0xFE,
        "Hello, who is it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_34AF")

    label("loc_3052")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3096")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_306D")
    Call(0, 14)
    Jump("loc_3091")

    label("loc_306D")


    ChrTalk(
        0xFE,
        "Okay, soon I will make a decision!\x02",
    )

    CloseMessageWindow()

    label("loc_3091")

    Jump("loc_34AF")

    label("loc_3096")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_30A4")
    Jump("loc_34AF")

    label("loc_30A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_30B5")
    Call(0, 15)
    Jump("loc_34AF")

    label("loc_30B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3129")

    ChrTalk(
        0xFE,
        (
            "Today the guys in east street\x01",
            "It looks like I'm taking classes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To, from the windows of my direction\x01",
            "I guess I should do it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34AF")

    label("loc_3129")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3276")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31FD")

    ChrTalk(
        0xFE,
        (
            "He who can distinguish Hamill from me\x01",
            "It is not quite right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So, pretend to be Hamill once in a while\x01",
            "Do not misunderstood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, if Mother is an opponent\x01",
            "It is getting out soon.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3271")

    label("loc_31FD")


    ChrTalk(
        0xFE,
        (
            "Mother is your opponent,\x01",
            "Even if you replace with Hamill\x01",
            "It is getting out soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Umamu, how do you distinguish it or not?\x02",
    )

    CloseMessageWindow()

    label("loc_3271")

    Jump("loc_34AF")

    label("loc_3276")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_32E1")

    ChrTalk(
        0xFE,
        (
            "What is Orkistower?\x01",
            "I was really scared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "To be honest, I seemed to be chewy.\x02",
    )

    CloseMessageWindow()
    Jump("loc_34AF")

    label("loc_32E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_32F2")
    Call(0, 11)
    Jump("loc_34AF")

    label("loc_32F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3300")
    Jump("loc_34AF")

    label("loc_3300")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_343A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33D3")

    ChrTalk(
        0xFE,
        (
            "To a new sister a little while ago\x01",
            "Trying to turn the skirt\x01",
            "I thought that … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To some terrible Azayaka\x01",
            "I got pushed away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mumumu … apparently\x01",
            "Well, why do not you tadamono.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3435")

    label("loc_33D3")


    ChrTalk(
        0xFE,
        (
            "My skirt turning\x01",
            "I can not fend off …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That new sister,\x01",
            "Well, why do not you tadamono.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3435")

    Jump("loc_34AF")

    label("loc_343A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_34A6")

    ChrTalk(
        0xFE,
        (
            "A new sister earlier\x01",
            "She seems to have come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hello, a bit later\x01",
            "Keep it alright.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34AF")

    label("loc_34A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_34AF")

    label("loc_34AF")

    TalkEnd(0xFE)
    Return()

    # Function_12_2EC6 end

    def Function_13_34B3(): pass

    label("Function_13_34B3")

    OP_4B(0xC, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xB,
        (
            "Some adults\x01",
            "It looks like he is making a noise ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "What is Dokitsu?\x01",
            "What do you mean?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hamill, you are good at studying.\x01",
            "Please tell me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It is unreasonable.\x01",
            "I also do not know well … …\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xB, 0xFF)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_13_34B3 end

    def Function_14_3595(): pass

    label("Function_14_3595")

    OP_4B(0xC, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xB,
        (
            "…… So, if Sister gets angry\x01",
            "Doing this … … Gonyoogonyo ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well, why am I?\x01",
            "I have to do something like that ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Okay, I got a bed during this time\x01",
            "Because I'm sorry to Kea!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Uh, as I said it … …\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_14_3595 end

    def Function_15_368A(): pass

    label("Function_15_368A")

    OP_4B(0xC, 0xFF)
    OP_4B(0xB, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_377C")

    ChrTalk(
        0xB,
        (
            "To us Sunday School classes\x01",
            "I got involved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Oh, Hamill looks at the lesson\x01",
            "I should say something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "No, no.\x01",
            "It was Tamil that said it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Please do not blame me casually,\x01",
            "Not at all.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_380B")

    label("loc_377C")


    ChrTalk(
        0xC,
        (
            "But it was good.\x01",
            "I have learned a lot\x01",
            "It also became a preparatory lesson.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Unlike you I hate studying!\x01",
            "Because it is this, Garishuguchi … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_380B")

    OP_4C(0xC, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_15_368A end

    def Function_16_3814(): pass

    label("Function_16_3814")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3899")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3832")
    Call(0, 9)
    Jump("loc_3894")

    label("loc_3832")


    ChrTalk(
        0xFE,
        (
            "Yeah, the children of the city\x01",
            "Everyone seems safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, you worried\x01",
            "Thank you, Sister.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3894")

    Jump("loc_4013")

    label("loc_3899")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_38A7")
    Jump("loc_4013")

    label("loc_38A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3948")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38C2")
    Call(0, 13)
    Jump("loc_3943")

    label("loc_38C2")


    ChrTalk(
        0xFE,
        (
            "About Dokitsu\x01",
            "I do not know well … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The city's adults\x01",
            "As long as you listen to talking,\x01",
            "It seems like a difficult thing …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3943")

    Jump("loc_4013")

    label("loc_3948")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3956")
    Jump("loc_4013")

    label("loc_3956")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3964")
    Jump("loc_4013")

    label("loc_3964")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3972")
    Jump("loc_4013")

    label("loc_3972")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_39D3")

    ChrTalk(
        0xFE,
        (
            "Ha Ha……\x01",
            "Why did I do this to me …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I will be scolded later … …\x02",
    )

    CloseMessageWindow()
    Jump("loc_4013")

    label("loc_39D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3A22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39EE")
    Call(0, 14)
    Jump("loc_3A1D")

    label("loc_39EE")


    ChrTalk(
        0xFE,
        (
            "No, I can not help it ……\x01",
            "It's just this time, is not it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A1D")

    Jump("loc_4013")

    label("loc_3A22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_3A30")
    Jump("loc_4013")

    label("loc_3A30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_3A41")
    Call(0, 15)
    Jump("loc_4013")

    label("loc_3A41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3A88")

    ChrTalk(
        0xFE,
        (
            "I do not want to stop … …\x01",
            "I do not know if Sister gets angry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4013")

    label("loc_3A88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3BB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B42")

    ChrTalk(
        0xFE,
        (
            "Mom and dad,\x01",
            "The distinction between us twin\x01",
            "It seems to be properly attached.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although it is almost the same face,\x01",
            "You just understand it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Parents might be amazing ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3BB2")

    label("loc_3B42")


    ChrTalk(
        0xFE,
        (
            "Mom and dad,\x01",
            "Which is me and which is Tamil\x01",
            "You just understand it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Parents might be amazing ……\x02",
    )

    CloseMessageWindow()

    label("loc_3BB2")

    Jump("loc_4013")

    label("loc_3BB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3C35")

    ChrTalk(
        0xFE,
        (
            "Ha, because it's no problem\x01",
            "The unveiling ceremony is with Kea-chan\x01",
            "I wanted to see it together ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… Ah, no, not at all.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4013")

    label("loc_3C35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3D5C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CE0")

    ChrTalk(
        0xFE,
        (
            "Tamil, with hide and seeskill\x01",
            "In the skirt of Sister\x01",
            "I hid it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, being angry\x01",
            "Even though I understand it,\x01",
            "I wonder why such a thing ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3D57")

    label("loc_3CE0")


    ChrTalk(
        0xFE,
        (
            "Even so ……\x01",
            "Tamil is getting angry,\x01",
            "I feel like I am getting angry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The twins are\x01",
            "It is somewhat something ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D57")

    Jump("loc_4013")

    label("loc_3D5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3D6A")
    Jump("loc_4013")

    label("loc_3D6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_3F9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F3F")
    TurnDirection(0xFE, 0x153, 0)

    ChrTalk(
        0xFE,
        (
            "Oh, Ka'a-chan!\x01",
            "Is the older class lesson done?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01109FYeah, Tocco is over now.\x02\x03",
            "#01100FAfter Hamir finishes the lesson\x01",
            "Have you been playing until now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No.\x01",
            "Together with Tamil.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hey, Kaea-chan, too\x01",
            "I already got Hamir properly\x01",
            "You know it is Kampeki.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01105FEr, why?\x02\x03",
            "#01109FTamil and face are soooo surprised\x01",
            "Hamir is Hamill and I can tell.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "(Damn it, I'm soooo happy …!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3F99")

    label("loc_3F3F")

    TurnDirection(0xFE, 0x153, 0)

    ChrTalk(
        0xFE,
        "Well, be careful Kea-chan.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01109FYeah, we all play with you again!\x02",
    )

    CloseMessageWindow()

    label("loc_3F99")

    Jump("loc_4013")

    label("loc_3F9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_400A")

    ChrTalk(
        0xFE,
        (
            "No, Tamil …\x01",
            "What if I was a scary person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if I get angry\x01",
            "You do not know, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4013")

    label("loc_400A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4013")

    label("loc_4013")

    TalkEnd(0xFE)
    Return()

    # Function_16_3814 end

    def Function_17_4017(): pass

    label("Function_17_4017")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_402C")
    Call(0, 18)
    Jump("loc_408F")

    label("loc_402C")


    ChrTalk(
        0xFE,
        (
            "Huh\x01",
            "If Ka'a told me\x01",
            "Is it useless?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From now on\x01",
            "Just like doing your homework.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_408F")

    TalkEnd(0xFE)
    Return()

    # Function_17_4017 end

    def Function_18_4093(): pass

    label("Function_18_4093")

    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0xD,
        (
            "Stick to Sister\x01",
            "I got angry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "You did not do your homework\x01",
            "Is not it Jigo Tseku?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Well, it used to be fairly old in the past\x01",
            "Since becoming a senior class\x01",
            "You have grown milky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01105FHomework, this time properly\x01",
            "Do not do it if you do not do it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    TurnDirection(0xD, 0x153, 500)
    Sleep(500)

    ChrTalk(
        0xD,
        "Aa\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F(Well, as expected it is key … …)\x02",
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    TurnDirection(0xD, 0xE, 0)
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x0, 5)
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_18_4093 end

    def Function_19_420D(): pass

    label("Function_19_420D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4222")
    Call(0, 18)
    Jump("loc_4253")

    label("loc_4222")


    ChrTalk(
        0xFE,
        (
            "Puppy, you too\x01",
            "I do not feel like shaping this child.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4253")

    TalkEnd(0xFE)
    Return()

    # Function_19_420D end

    def Function_20_4257(): pass

    label("Function_20_4257")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43B1")
    TurnDirection(0xFE, 0x153, 0)

    ChrTalk(
        0xFE,
        (
            "Oh, Ka'aa,\x01",
            "Are you going home now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01110FYup! Where is Brick going?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, because it's it\x01",
            "Cross Bell Times at Nishi Dori\x01",
            "I thought that I should buy it and return.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ka'a-chan ……\x01",
            "I will not lose in the next lesson!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01111FBrian, did you win or lose?\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "No, no.\x01",
            "Forget it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4438")

    label("loc_43B1")


    ChrTalk(
        0xFE,
        (
            "Ka'aa becomes an older class\x01",
            "When participating,\x01",
            "I was surprised at running though ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With this, again\x01",
            "I thought about studying.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4438")

    TalkEnd(0xFE)
    Return()

    # Function_20_4257 end

    def Function_21_443C(): pass

    label("Function_21_443C")

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

    def lambda_4583():
        OP_9B(0x0, 0x101, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4583)
    Sleep(100)

    def lambda_459B():
        OP_9B(0x0, 0x102, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_459B)
    Sleep(100)

    def lambda_45B3():
        OP_9B(0x0, 0x103, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_45B3)
    Sleep(100)

    def lambda_45CB():
        OP_9B(0x0, 0x104, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_45CB)
    Sleep(100)

    def lambda_45E3():
        OP_9B(0x0, 0x109, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_45E3)
    Sleep(100)

    def lambda_45FB():
        OP_9B(0x0, 0x105, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_45FB)
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

    def lambda_467A():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_467A)
    Sleep(50)

    def lambda_468A():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_468A)
    Sleep(50)

    def lambda_469A():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_469A)
    Sleep(50)

    def lambda_46AA():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_46AA)
    Sleep(50)

    def lambda_46BA():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_46BA)
    Sleep(50)

    def lambda_46CA():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_46CA)
    Sleep(50)

    def lambda_46DA():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_46DA)
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
            "#00003F#11PAlready almost evening huh\x02\x03",
            "#00001FI'd like to submit a report today,\x01",
            "I have to gather information somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PYeah ….\x01",
            "I hope I have clues.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4835")

    ChrTalk(
        0x103,
        (
            "#00200FTentatively,\x01",
            "Mr. Lease or Marble\x01",
            "Are you going to visit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#11POh, first Sunday school\x01",
            "Let's visit the classroom.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48B5")

    label("loc_4835")


    ChrTalk(
        0x103,
        (
            "#00200FFor the time being, marble sensei\x01",
            "Are you going to visit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#11POh, Sunday school classes\x01",
            "I hope it will not be included ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48B5")

    ClearChrFlags(0x10, 0x80)

    NpcTalk(
        0x10,
        "Male voice",
        "Oh you guys\x02",
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

    def lambda_4955():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4955)
    Sleep(0)

    def lambda_4965():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4965)
    Sleep(0)

    def lambda_4975():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4975)
    Sleep(0)

    def lambda_4985():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4985)
    Sleep(0)

    def lambda_4995():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4995)
    Sleep(0)

    def lambda_49A5():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_49A5)
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
        "#00005F#6PIan-sensei\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16C, 1)), scpexpr(EXPR_END)), "loc_4C7F")

    ChrTalk(
        0x102,
        "#00104F#6PNice to see you!\x02",
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
            "Oh, it's been since the commerce meeting.\x02\x03",
            "Oops, by the way, in the daytime,\x01",
            "You came to the office?\x02\x03",
            "I'm sorry.\x01",
            "You should have come to the trouble to visit us.\x02",
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
            "#00012F#6PHouse……\x01",
            "But, she seems to be busy, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F#6PAnything to draft a constitutional draft\x01",
            "Are you cooperating?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#02210F#11PAhaha\x02\x03",
            "The mayor enthusiastically will ask\x01",
            "You can not refuse it.\x02\x03",
            "#02200FWell, as for me personally\x01",
            "I agree with his idea.\x02\x03",
            "Although realization may be difficult, …\x01",
            "Please think that you can at least force it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50C6")

    label("loc_4C7F")


    ChrTalk(
        0x102,
        (
            "#00104F#6PNice to see you!\x02\x03",
            "#00108FRecently, I'm pretty busy anything\x01",
            "You seem to be being told?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#00005F#5PReally?\x02",
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
            "Ahaha\x02\x03",
            "…… Actually concerning national independence of the example\x01",
            "Ask the mayor to prepare a draft constitution.\x02",
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
            "#10101F#6P\"Constitution\" … ….\x01",
            "Is not autonomous state law, is it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x109, 500)

    ChrTalk(
        0x102,
        (
            "#00104F#11P\"Constitution\" means\x01",
            "Established basic conditions for the existence of the state\x01",
            "It becomes a fundamental law.\x02\x03",
            "#00100FGovernance rights and mechanisms of the country,\x01",
            "With the highest regulations that set out the principle\x01",
            "It will not allow interference from other countries.\x02\x03",
            "In order to have a state as a state\x01",
            "It will be absolutely indispensable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F#6PThe\x01",
            "It is also a difficult shimmer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#6PBut if Professor Ian\x01",
            "I wonder if it is just right for you …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#02210F#11Pmy mother……\x01",
            "The mayor enthusiastically will ask\x01",
            "You can not refuse it.\x02\x03",
            "#02200FWell, as for me personally\x01",
            "I agree with his idea.\x02\x03",
            "Although realization may be difficult, …\x01",
            "Please think that you can at least force it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50C6")


    def lambda_50CB():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_50CB)

    ChrTalk(
        0x101,
        "#00002F#6PIs that right…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#6PI'm going to relax for a moment.\x01",
            "I wonder if it came even to pray?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#02210F#11POh, it was a bit boiled down\x01",
            "It seems that it turned out a good change.\x02\x03",
            "#02202FAfter all, when human beings are in trouble\x01",
            "It is not bad that you ask Goddess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#6PHa ha …\x01",
            "Surely I can say that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00104F#6PThanks for all your hard work\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#02210F#11PHaha, same to you\x02\x03",
            "#02200FIt is evening soon ….\x01",
            "Did you come by work?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PYeah, a bit church official\x01",
            "There was something I wanted to talk to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#02203F#11PHmm. Seems you have something going on\x02\x03",
            "#02200FAlthough I am also busy … …\x01",
            "If there is something that seems to work\x01",
            "Please do not hesitate to visit our office.\x02\x03",
            "I will always welcome you warmly\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004F#6PThank you so much\x02",
    )

    CloseMessageWindow()
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x109, 0x1F)
    SetChrSubChip(0x109, 0x0)
    OP_0D()

    ChrTalk(
        0x109,
        "#10100F#6PPlease take care on your way home!\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    OP_0D()

    def lambda_53DC():

        label("loc_53DC")

        TurnDirection(0x101, 0x10, 500)
        Yield()
        Jump("loc_53DC")

    QueueWorkItem2(0x101, 2, lambda_53DC)

    def lambda_53EE():

        label("loc_53EE")

        TurnDirection(0x102, 0x10, 500)
        Yield()
        Jump("loc_53EE")

    QueueWorkItem2(0x102, 2, lambda_53EE)

    def lambda_5400():

        label("loc_5400")

        TurnDirection(0x103, 0x10, 500)
        Yield()
        Jump("loc_5400")

    QueueWorkItem2(0x103, 2, lambda_5400)

    def lambda_5412():

        label("loc_5412")

        TurnDirection(0x104, 0x10, 500)
        Yield()
        Jump("loc_5412")

    QueueWorkItem2(0x104, 2, lambda_5412)

    def lambda_5424():

        label("loc_5424")

        TurnDirection(0x109, 0x10, 500)
        Yield()
        Jump("loc_5424")

    QueueWorkItem2(0x109, 2, lambda_5424)

    def lambda_5436():

        label("loc_5436")

        TurnDirection(0x105, 0x10, 500)
        Yield()
        Jump("loc_5436")

    QueueWorkItem2(0x105, 2, lambda_5436)
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
        "#00001F#11PHe seems busy\x02",
    )

    CloseMessageWindow()

    def lambda_54C7():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_54C7)
    Sleep(0)

    def lambda_54D7():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_54D7)
    Sleep(0)

    def lambda_54E7():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_54E7)
    Sleep(0)

    def lambda_54F7():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_54F7)
    Sleep(0)

    def lambda_5507():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5507)
    Sleep(0)

    def lambda_5517():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5517)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x102,
        (
            "#00103F#12PWell, as it becomes a draft constitution\x01",
            "Because it requires a considerable thing …\x02\x03",
            "#00101FIf you announce bad things\x01",
            "It's just an empire from around the Republic\x01",
            "It will be said that there is no persuasive power … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#6PRight…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#6PHuh, what is our busyness\x01",
            "I do not think its struggle is different.\x02\x03",
            "#10300FThat's … …\x01",
            "Are you going to visit the classroom on Sunday School?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#11PYeah, let's go\x02",
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

    # Function_21_443C end

    def Function_22_56F3(): pass

    label("Function_22_56F3")

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
            "#04403F#5PWell then come in\x02\x03",
            "#04400FTo other people\x01",
            "I do not want to see it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#12PRight\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103F#12PExcuse us\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x1F4)
    Sound(121, 0, 100, 0)
    OP_71(0x1, 0x0, 0x14, 0x0, 0x0)
    OP_79(0x1)

    def lambda_5882():
        OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_5882)
    OP_9B(0x0, 0x8, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0x8, 3)

    def lambda_58A6():
        OP_95(0x102, -11400, 500, 14750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_58A6)
    Sleep(200)

    def lambda_58C3():
        OP_95(0x103, -11400, 500, 13250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_58C3)
    Sleep(100)

    def lambda_58E0():
        OP_95(0x101, -11400, 500, 14000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_58E0)
    Sleep(100)

    def lambda_58FD():
        OP_95(0x104, -11400, 500, 14750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_58FD)
    Sleep(100)

    def lambda_591A():
        OP_95(0x109, -11400, 500, 13250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_591A)
    Sleep(200)

    def lambda_5937():
        OP_95(0x105, -11400, 500, 14000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5937)
    Sleep(500)
    FadeToDark(1000, 0, -1)

    def lambda_595E():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_595E)
    Sleep(50)

    def lambda_5972():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_5972)
    Sleep(50)

    def lambda_5986():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5986)
    Sleep(150)

    def lambda_599A():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 3, lambda_599A)
    Sleep(50)

    def lambda_59AE():
        OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_59AE)
    Sleep(50)

    def lambda_59C2():
        OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 3, lambda_59C2)
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

    # Function_22_56F3 end

    def Function_23_5A12(): pass

    label("Function_23_5A12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BE8")

    ChrTalk(
        0xA,
        "Today is Mass Day.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Everyone participating\x01",
            "What do you think~?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(In Miscon's \"Sister\" frame\x01",
            "I wonder if it will get out ……? )\x02\x03",
            "#00000FExcuse me.\x01",
            "It is a little consultation … …\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Charity event\x01",
            "I asked for participation in Miscon.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            "Well, yeah … ….?\x01",
            "I mean MissCon ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It is impossible.\x01",
            "I'm really,\x01",
            "There is no sex appeal at all … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm sorry but another person\x01",
            "Please invite me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FIs that so …?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x199, 1)
    Jump("loc_5C50")

    label("loc_5BE8")


    ChrTalk(
        0xA,
        (
            "I, something like me\x01",
            "It is impossible for Miscon to appear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Worthy people\x01",
            "I think there are more.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C50")

    TalkEnd(0xA)
    Return()

    # Function_23_5A12 end

    def Function_24_5C54(): pass

    label("Function_24_5C54")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "~ Cross Bell Cathedral Dormitory ~\x01",
            "For worshipers go to the chapel\x01",
            "Please turn around.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_24_5C54 end

    def Function_25_5CD6(): pass

    label("Function_25_5CD6")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FTentatively,\x01",
            "Let's go to Mr. Leith.\x01",
            "There may be some information available.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 370, 0, -7350, 0)
    EventEnd(0x4)
    Return()

    # Function_25_5CD6 end

    SaveToFile()

Try(main)
