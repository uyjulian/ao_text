from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1520.bin",                # FileName
        "c1520",                    # MapName
        "c1520",                    # Location
        0x00AA,                     # MapIndex
        "ed7550",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 170, 0, 0, 0, 1],
    )

    BuildStringList((
        "c1520",                  # 0
        "Mayor Dieter",           # 1
        "Arios",                  # 2
        "Detective Dudley",       # 3
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(3200,    0,       100000,  2000,    3300,    900,     100000,  0x007C, 0,  3,  0x0000)
    DeclActor(70000,   0,       103200,  2000,    70000,   900,     103300,  0x007C, 0,  3,  0x0000)

    ChipFrameInfo(352, 0)                                        # 0

    ScpFunction((
        "Function_0_160",          # 00, 0
        "Function_1_1BA",          # 01, 1
        "Function_2_2AF",          # 02, 2
        "Function_3_11ED",         # 03, 3
        "Function_4_16DF",         # 04, 4
        "Function_5_2561",         # 05, 5
        "Function_6_2CC0",         # 06, 6
        "Function_7_2E8D",         # 07, 7
        "Function_8_3469",         # 08, 8
        "Function_9_3BE1",         # 09, 9
        "Function_10_40B1",        # 0A, 10
        "Function_11_49E3",        # 0B, 11
    ))


    def Function_0_160(): pass

    label("Function_0_160")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_174")
    ClearScenarioFlags(0x22, 0)
    Event(0, 4)
    Jump("loc_1B9")

    label("loc_174")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_188")
    ClearScenarioFlags(0x22, 1)
    Event(0, 5)
    Jump("loc_1B9")

    label("loc_188")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19E")
    Event(0, 6)
    Jump("loc_1B9")

    label("loc_19E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_GE), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B9")
    Event(0, 2)

    label("loc_1B9")

    Return()

    # Function_0_160 end

    def Function_1_1BA(): pass

    label("Function_1_1BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D3")
    VolumeBGM(0x46, 0xC8)
    Jump("loc_21C")

    label("loc_1D3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_20A")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x160), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_21C")

    label("loc_20A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_21C")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_21C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_235")
    OP_10(0xF, 0x1)
    OP_10(0x10, 0x0)
    Jump("loc_27B")

    label("loc_235")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24E")
    OP_10(0xF, 0x0)
    OP_10(0x10, 0x1)
    Jump("loc_27B")

    label("loc_24E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_267")
    OP_10(0x11, 0x1)
    OP_10(0x12, 0x0)
    Jump("loc_27B")

    label("loc_267")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27B")
    OP_10(0x11, 0x0)
    OP_10(0x12, 0x1)

    label("loc_27B")

    OP_70(0x0, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2AE")
    Sound(927, 1, 100, 0)

    label("loc_2AE")

    Return()

    # Function_1_1BA end

    def Function_2_2AF(): pass

    label("Function_2_2AF")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    ClearScenarioFlags(0x0, 0)
    ClearScenarioFlags(0x0, 1)
    ClearScenarioFlags(0x0, 2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_GE), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x77), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3E3")
    SetScenarioFlags(0x0, 0)
    OP_68(0, 1000, 1000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x0, 0, 0, 1800, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34E")
    SetChrPos(0x1, 800, 0, 600, 0)

    label("loc_34E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36D")
    SetChrPos(0x2, -800, 0, 600, 0)

    label("loc_36D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38C")
    SetChrPos(0x3, 0, 0, -500, 0)

    label("loc_38C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B5")
    SetChrPos(0x4, 800, 0, -1600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_3B5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3DE")
    SetChrPos(0x5, -800, 0, -1600, 0)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_3DE")

    Jump("loc_5F8")

    label("loc_3E3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_GE), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F0")
    SetScenarioFlags(0x0, 1)
    OP_68(70000, 1000, 1000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x0, 70000, 0, 1800, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_45B")
    SetChrPos(0x1, 70800, 0, 600, 0)

    label("loc_45B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47A")
    SetChrPos(0x2, 69200, 0, 600, 0)

    label("loc_47A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_499")
    SetChrPos(0x3, 70000, 0, -500, 0)

    label("loc_499")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C2")
    SetChrPos(0x4, 70800, 0, -1600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_4C2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4EB")
    SetChrPos(0x5, 69200, 0, -1600, 0)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_4EB")

    Jump("loc_5F8")

    label("loc_4F0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_GE), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F8")
    SetScenarioFlags(0x0, 2)
    OP_68(140000, 1000, 1000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x0, 140000, 0, 1800, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_568")
    SetChrPos(0x1, 140800, 0, 600, 0)

    label("loc_568")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_587")
    SetChrPos(0x2, 139200, 0, 600, 0)

    label("loc_587")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5A6")
    SetChrPos(0x3, 140000, 0, -500, 0)

    label("loc_5A6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5CF")
    SetChrPos(0x4, 140800, 0, -1600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_5CF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F8")
    SetChrPos(0x5, 139200, 0, -1600, 0)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_5F8")

    FadeToBright(500, 0)
    OP_0D()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_63E")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_63E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_65B")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_65B")

    MenuCmd(0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_77D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_690")
    MenuCmd(1, 0, "★[40F]")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_69B")

    label("loc_690")

    MenuCmd(1, 0, "  [40F]")

    label("loc_69B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C4")
    MenuCmd(1, 0, "★[36F]")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6CF")

    label("loc_6C4")

    MenuCmd(1, 0, "  [36F]")

    label("loc_6CF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F7")
    MenuCmd(1, 0, "★[21F]")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_702")

    label("loc_6F7")

    MenuCmd(1, 0, "  [21F]")

    label("loc_702")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72B")
    MenuCmd(1, 0, "★[ 1F]")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_736")

    label("loc_72B")

    MenuCmd(1, 0, "  [ 1F]")

    label("loc_736")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x77), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75E")
    MenuCmd(1, 0, "★[B8F]")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_769")

    label("loc_75E")

    MenuCmd(1, 0, "  [B8F]")

    label("loc_769")

    MenuCmd(1, 0, "  [Get Off]")
    Jump("loc_A1D")

    label("loc_77D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 7)), scpexpr(EXPR_END)), "loc_869")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AF")
    MenuCmd(1, 0, "★[40F]")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7BA")

    label("loc_7AF")

    MenuCmd(1, 0, "  [40F]")

    label("loc_7BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E3")
    MenuCmd(1, 0, "★[36F]")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7EE")

    label("loc_7E3")

    MenuCmd(1, 0, "  [36F]")

    label("loc_7EE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_816")
    MenuCmd(1, 0, "★[21F]")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_821")

    label("loc_816")

    MenuCmd(1, 0, "  [21F]")

    label("loc_821")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_84A")
    MenuCmd(1, 0, "★[ 1F]")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_855")

    label("loc_84A")

    MenuCmd(1, 0, "  [ 1F]")

    label("loc_855")

    MenuCmd(1, 0, "  [Get Off]")
    Jump("loc_A1D")

    label("loc_869")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_END)), "loc_8ED")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_89A")
    MenuCmd(1, 0, "★[21F]")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8A5")

    label("loc_89A")

    MenuCmd(1, 0, "  [21F]")

    label("loc_8A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CE")
    MenuCmd(1, 0, "★[ 1F]")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8D9")

    label("loc_8CE")

    MenuCmd(1, 0, "  [ 1F]")

    label("loc_8D9")

    MenuCmd(1, 0, "  [Get Off]")
    Jump("loc_A1D")

    label("loc_8ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 5)), scpexpr(EXPR_END)), "loc_972")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_91F")
    MenuCmd(1, 0, "★[40F]")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_92A")

    label("loc_91F")

    MenuCmd(1, 0, "  [40F]")

    label("loc_92A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_953")
    MenuCmd(1, 0, "★[ 1F]")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_95E")

    label("loc_953")

    MenuCmd(1, 0, "  [ 1F]")

    label("loc_95E")

    MenuCmd(1, 0, "  [Get Off]")
    Jump("loc_A1D")

    label("loc_972")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_99B")
    MenuCmd(1, 0, "★[36F]")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9A6")

    label("loc_99B")

    MenuCmd(1, 0, "  [36F]")

    label("loc_9A6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9CF")
    MenuCmd(1, 0, "★[35F]")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9DA")

    label("loc_9CF")

    MenuCmd(1, 0, "  [35F]")

    label("loc_9DA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A03")
    MenuCmd(1, 0, "★[34F]")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A0E")

    label("loc_A03")

    MenuCmd(1, 0, "  [34F]")

    label("loc_A0E")

    MenuCmd(1, 0, "  [Get Off]")

    label("loc_A1D")

    MenuCmd(2, 0, 10, 10, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_AEA")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A54")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AE5")

    label("loc_A54")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A72")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AE5")

    label("loc_A72")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A90")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AE5")

    label("loc_A90")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AAE")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AE5")

    label("loc_AAE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ACC")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AE5")

    label("loc_ACC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE5")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AE5")

    Jump("loc_CC2")

    label("loc_AEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 7)), scpexpr(EXPR_END)), "loc_B89")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B11")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B84")

    label("loc_B11")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B2F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B84")

    label("loc_B2F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B4D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B84")

    label("loc_B4D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B6B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B84")

    label("loc_B6B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B84")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B84")

    Jump("loc_CC2")

    label("loc_B89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_END)), "loc_BEC")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB0")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BE7")

    label("loc_BB0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BCE")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BE7")

    label("loc_BCE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE7")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BE7")

    Jump("loc_CC2")

    label("loc_BEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 5)), scpexpr(EXPR_END)), "loc_C4F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C13")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C4A")

    label("loc_C13")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C31")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C4A")

    label("loc_C31")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C4A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C4A")

    Jump("loc_CC2")

    label("loc_C4F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C6D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CC2")

    label("loc_C6D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C8B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CC2")

    label("loc_C8B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA9")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CC2")

    label("loc_CA9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CC2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CE1")
    FadeToDark(500, 0, -1)
    OP_0D()
    Jump("loc_E22")

    label("loc_CE1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D7C")
    Sound(159, 0, 100, 0)
    OP_71(0x0, 0x64, 0x87, 0x0, 0x0)
    OP_79(0x0)
    OP_71(0x0, 0x87, 0x9A, 0x0, 0x20)
    FadeToDark(2000, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_D38")
    OP_68(0, 4000, 1000, 2000)
    Jump("loc_D71")

    label("loc_D38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_D57")
    OP_68(70000, 4000, 1000, 2000)
    Jump("loc_D71")

    label("loc_D57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_D71")
    OP_68(140000, 4000, 1000, 2000)

    label("loc_D71")

    OP_0D()
    OP_6F(0x1)
    Sleep(300)
    Jump("loc_E22")

    label("loc_D7C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E17")
    Sound(159, 0, 100, 0)
    OP_71(0x0, 0x0, 0x23, 0x0, 0x0)
    OP_79(0x0)
    OP_71(0x0, 0x23, 0x36, 0x0, 0x20)
    FadeToDark(2000, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_DD3")
    OP_68(0, -3500, 1000, 2000)
    Jump("loc_E0C")

    label("loc_DD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_DF2")
    OP_68(70000, -3500, 1000, 2000)
    Jump("loc_E0C")

    label("loc_DF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_E0C")
    OP_68(140000, -3500, 1000, 2000)

    label("loc_E0C")

    OP_0D()
    OP_6F(0x1)
    Sleep(300)
    Jump("loc_E22")

    label("loc_E17")

    FadeToDark(500, 0, -1)
    OP_0D()

    label("loc_E22")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FED")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_E65"),
        (1, "loc_EAC"),
        (2, "loc_EF3"),
        (3, "loc_F3A"),
        (4, "loc_F81"),
        (5, "loc_F91"),
        (6, "loc_FD8"),
        (SWITCH_DEFAULT, "loc_FE8"),
    )


    label("loc_E65")

    EventEnd(0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E7E")
    NewScene("c1583", 109, 0, 0)
    IdleLoop()
    Jump("loc_EA7")

    label("loc_E7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_E95")
    NewScene("c1583", 110, 0, 0)
    IdleLoop()
    Jump("loc_EA7")

    label("loc_E95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_EA7")
    NewScene("c1583", 111, 0, 0)
    IdleLoop()

    label("loc_EA7")

    Jump("loc_FE8")

    label("loc_EAC")

    EventEnd(0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_EC5")
    NewScene("c1550", 100, 0, 0)
    IdleLoop()
    Jump("loc_EEE")

    label("loc_EC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_EDC")
    NewScene("c1550", 101, 0, 0)
    IdleLoop()
    Jump("loc_EEE")

    label("loc_EDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_EEE")
    NewScene("c1550", 102, 0, 0)
    IdleLoop()

    label("loc_EEE")

    Jump("loc_FE8")

    label("loc_EF3")

    EventEnd(0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F0C")
    NewScene("c1540", 100, 0, 0)
    IdleLoop()
    Jump("loc_F35")

    label("loc_F0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_F23")
    NewScene("c1540", 101, 0, 0)
    IdleLoop()
    Jump("loc_F35")

    label("loc_F23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_F35")
    NewScene("c1540", 102, 0, 0)
    IdleLoop()

    label("loc_F35")

    Jump("loc_FE8")

    label("loc_F3A")

    EventEnd(0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F53")
    NewScene("c1530", 100, 0, 0)
    IdleLoop()
    Jump("loc_F7C")

    label("loc_F53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_F6A")
    NewScene("c1530", 101, 0, 0)
    IdleLoop()
    Jump("loc_F7C")

    label("loc_F6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_F7C")
    NewScene("c1530", 102, 0, 0)
    IdleLoop()

    label("loc_F7C")

    Jump("loc_FE8")

    label("loc_F81")

    EventEnd(0x5)
    NewScene("c1580", 100, 0, 0)
    IdleLoop()
    Jump("loc_FE8")

    label("loc_F91")

    EventEnd(0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_FAA")
    NewScene("c1510", 103, 0, 0)
    IdleLoop()
    Jump("loc_FD3")

    label("loc_FAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_FC1")
    NewScene("c1510", 104, 0, 0)
    IdleLoop()
    Jump("loc_FD3")

    label("loc_FC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_FD3")
    NewScene("c1510", 105, 0, 0)
    IdleLoop()

    label("loc_FD3")

    Jump("loc_FE8")

    label("loc_FD8")

    EventEnd(0x5)
    NewScene("m0400", 100, 0, 0)
    IdleLoop()
    Jump("loc_FE8")

    label("loc_FE8")

    Jump("loc_11EC")

    label("loc_FED")

    SetScenarioFlags(0x25, 1)
    Sleep(500)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1027"),
        (1, "loc_109A"),
        (2, "loc_10E1"),
        (3, "loc_1128"),
        (4, "loc_116F"),
        (5, "loc_1195"),
        (6, "loc_11DC"),
        (SWITCH_DEFAULT, "loc_11EC"),
    )


    label("loc_1027")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_103D")
    Call(0, 7)
    Jump("loc_1095")

    label("loc_103D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1053")
    Call(0, 10)
    Jump("loc_1095")

    label("loc_1053")

    EventEnd(0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_106C")
    NewScene("c1583", 109, 0, 0)
    IdleLoop()
    Jump("loc_1095")

    label("loc_106C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1083")
    NewScene("c1583", 110, 0, 0)
    IdleLoop()
    Jump("loc_1095")

    label("loc_1083")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1095")
    NewScene("c1583", 111, 0, 0)
    IdleLoop()

    label("loc_1095")

    Jump("loc_11EC")

    label("loc_109A")

    EventEnd(0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_10B3")
    NewScene("c1550", 100, 0, 0)
    IdleLoop()
    Jump("loc_10DC")

    label("loc_10B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_10CA")
    NewScene("c1550", 101, 0, 0)
    IdleLoop()
    Jump("loc_10DC")

    label("loc_10CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_10DC")
    NewScene("c1550", 102, 0, 0)
    IdleLoop()

    label("loc_10DC")

    Jump("loc_11EC")

    label("loc_10E1")

    EventEnd(0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_10FA")
    NewScene("c1540", 100, 0, 0)
    IdleLoop()
    Jump("loc_1123")

    label("loc_10FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1111")
    NewScene("c1540", 101, 0, 0)
    IdleLoop()
    Jump("loc_1123")

    label("loc_1111")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1123")
    NewScene("c1540", 102, 0, 0)
    IdleLoop()

    label("loc_1123")

    Jump("loc_11EC")

    label("loc_1128")

    EventEnd(0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1141")
    NewScene("c1530", 100, 0, 0)
    IdleLoop()
    Jump("loc_116A")

    label("loc_1141")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1158")
    NewScene("c1530", 101, 0, 0)
    IdleLoop()
    Jump("loc_116A")

    label("loc_1158")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_116A")
    NewScene("c1530", 102, 0, 0)
    IdleLoop()

    label("loc_116A")

    Jump("loc_11EC")

    label("loc_116F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1185")
    Call(0, 8)
    Jump("loc_1190")

    label("loc_1185")

    EventEnd(0x5)
    NewScene("c1580", 100, 0, 0)
    IdleLoop()

    label("loc_1190")

    Jump("loc_11EC")

    label("loc_1195")

    EventEnd(0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_11AE")
    NewScene("c1510", 103, 0, 0)
    IdleLoop()
    Jump("loc_11D7")

    label("loc_11AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_11C5")
    NewScene("c1510", 104, 0, 0)
    IdleLoop()
    Jump("loc_11D7")

    label("loc_11C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_11D7")
    NewScene("c1510", 105, 0, 0)
    IdleLoop()

    label("loc_11D7")

    Jump("loc_11EC")

    label("loc_11DC")

    EventEnd(0x5)
    NewScene("m0400", 100, 0, 0)
    IdleLoop()
    Jump("loc_11EC")

    label("loc_11EC")

    Return()

    # Function_2_2AF end

    def Function_3_11ED(): pass

    label("Function_3_11ED")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    SoundLoad(832)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's an elevator control\x01",
            "panel. Operate?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16D7")
    Fade(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_135D")
    SetChrPos(0x0, 1800, 0, 100000, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_129A")
    SetChrPos(0x1, 600, 0, 100800, 90)

    label("loc_129A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12B9")
    SetChrPos(0x2, 600, 0, 99200, 90)

    label("loc_12B9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12D8")
    SetChrPos(0x3, -500, 0, 100000, 90)

    label("loc_12D8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1301")
    SetChrPos(0x4, -1600, 0, 100800, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_1301")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_132A")
    SetChrPos(0x5, -1600, 0, 99200, 90)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_132A")

    OP_68(1000, 1000, 100000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19500, 0)
    Jump("loc_1462")

    label("loc_135D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1462")
    SetChrPos(0x0, 70000, 0, 101800, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13A4")
    SetChrPos(0x1, 70800, 0, 100600, 0)

    label("loc_13A4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13C3")
    SetChrPos(0x2, 69200, 0, 100600, 0)

    label("loc_13C3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13E2")
    SetChrPos(0x3, 70000, 0, 99500, 0)

    label("loc_13E2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_140B")
    SetChrPos(0x4, 70800, 0, 98400, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_140B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1434")
    SetChrPos(0x5, 69200, 0, 98400, 0)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_1434")

    OP_68(70000, 1000, 101000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19500, 0)

    label("loc_1462")

    OP_0D()
    Sleep(500)
    Sound(159, 0, 100, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1490")
    OP_68(1000, -9000, 100000, 3000)
    Jump("loc_14F7")

    label("loc_1490")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14B4")
    OP_68(1000, 9000, 100000, 3000)
    Jump("loc_14F7")

    label("loc_14B4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14D8")
    OP_68(70000, -9000, 101000, 3000)
    Jump("loc_14F7")

    label("loc_14D8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14F7")
    OP_68(70000, 9000, 101000, 3000)

    label("loc_14F7")

    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1522")
    Call(0, 9)
    Return()

    label("loc_1522")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_155D")
    Sound(832, 2, 100, 0)
    OP_68(1000, 9000, 100000, 0)
    OP_68(1000, 1000, 100000, 3000)
    Jump("loc_1609")

    label("loc_155D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1598")
    Sound(832, 2, 100, 0)
    OP_68(1000, -9000, 100000, 0)
    OP_68(1000, 1000, 100000, 3000)
    Jump("loc_1609")

    label("loc_1598")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15D3")
    Sound(832, 2, 100, 0)
    OP_68(70000, 9000, 101000, 0)
    OP_68(70000, 1000, 101000, 3000)
    Jump("loc_1609")

    label("loc_15D3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1609")
    Sound(832, 2, 100, 0)
    OP_68(70000, -9000, 101000, 0)
    OP_68(70000, 1000, 101000, 3000)

    label("loc_1609")

    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    StopSound(832, 1000, 100)
    Sound(160, 0, 100, 0)
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1646")
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_10(0xF, 0x0)
    OP_10(0x10, 0x1)
    Jump("loc_16A7")

    label("loc_1646")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1668")
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_10(0xF, 0x1)
    OP_10(0x10, 0x0)
    Jump("loc_16A7")

    label("loc_1668")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_168A")
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_10(0x11, 0x0)
    OP_10(0x12, 0x1)
    Jump("loc_16A7")

    label("loc_168A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16A7")
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_10(0x11, 0x1)
    OP_10(0x12, 0x0)

    label("loc_16A7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16BF")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_16BF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16D7")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_16D7")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_3_11ED end

    def Function_4_16DF(): pass

    label("Function_4_16DF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05600.itc", 0x1E)
    SoundLoad(832)
    OP_68(70000, 2100, 1000, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 70000, 0, 0, 0)
    SetChrPos(0x102, 68700, 0, -600, 0)
    SetChrPos(0x103, 69300, 0, -1600, 0)
    SetChrPos(0x104, 70600, 0, -1000, 315)
    SetChrPos(0x109, 67400, 0, -600, 45)
    SetChrPos(0x105, 71600, 0, -1600, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 70000, 0, 1800, 180)
    OP_71(0x0, 0x23, 0x36, 0x0, 0x20)
    VolumeBGM(0x50, 0x3E8)
    Sound(832, 2, 100, 0)
    Sleep(1000)
    Sleep(300)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Dieter's Voice")

    AnonymousTalk(
        0xFF,
        "─I see.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "I heard that from Mr.\x01",
            "Dudley too. The situation\x01",
            "is indeed quite dangerous.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(70000, 1100, 1000, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#12P#00006FRight...\x02\x03",
            "#00001FThere's the actions of the jaeger corps and the\x01",
            "crime syndicate, and on top of that, the motives\x01",
            "of the Imperial and Republican governments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00108F...There's the threat of\x01",
            "terrorists aiming for\x01",
            "their heads of state, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FThere's also that\x01",
            "mysterious hacker,\x01",
            "right?\x02\x03",
            "#00200FHe was able to steal the\x01",
            "tower blueprints using\x01",
            "one of your terminals?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02806F#5PYeah. It seems the Orchis Tower sub-\x01",
            "terminal was hacked into.\x02\x03",
            "#02801FAfter the incident at IBC, I had our\x01",
            "Systems Division strengthen anti-\x01",
            "hacking countermeasures, but...\x02\x03",
            "It seems it wasn't enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FHmm. There's still very\x01",
            "few hackers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FIt's likely to be\x01",
            "someone connected to the\x01",
            "Epstein Foundation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FChief Roberts is looking\x01",
            "into that possibility as we\x01",
            "speak.\x02\x03",
            "#00208FI feel like the hacking this\x01",
            "time isn't someone connected\x01",
            "to the foundation, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02804F#5PWell, we'll just have to wait\x01",
            "for the results of that\x01",
            "investigation.\x02\x03",
            "#02801FBut jaeger corps, crime\x01",
            "syndicates and terrorists...\x01",
            "All of them worry me...\x02\x03",
            "But what worries me even more\x01",
            "is their motive for targeting\x01",
            "the heads of state.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00001FTheir motive for\x01",
            "targeting the heads of\x01",
            "state...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301FYou think it's someone\x01",
            "connected to the\x01",
            "conference?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02803F#5PI'm not suspecting Princess\x01",
            "Klaudia and Prince Olivert,\x01",
            "whom you all met.\x02\x03",
            "And I trust the Archduke of\x01",
            "Remiferia as well.\x02\x03",
            "#02801F...The problem is\x01",
            "Chancellor Osborne and\x01",
            "President Rocksmith.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10108FThe leaders of the two\x01",
            "major powers, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305FThose two certainly have the\x01",
            "most to gain from getting their\x01",
            "hands on Crossbell's fate.\x02\x03",
            "#10301FAre there any specific actions\x01",
            "they've taken in that regard?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02806F#5PNo, the opposite.\x02\x03",
            "#02801F─We sent several proposals\x01",
            "for treaties and accords\x01",
            "for the conference, but...\x02\x03",
            "The replies from both\x01",
            "sides have been nothing\x01",
            "but favorable.\x02\x03",
            "As if they're really\x01",
            "hoping for peace and\x01",
            "growth in West Zemuria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00011FT-That's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106FThat's definitely\x01",
            "strange.\x02\x03",
            "#00101FNormally, those\x01",
            "countries clash over the\x01",
            "smallest things...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02803F#5PYeah. I have no idea how\x01",
            "this conference is going\x01",
            "to go.\x02\x03",
            "#02801FIt seems I'll need to be\x01",
            "prepared in case things\x01",
            "go south.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00208FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FSo it's a difficult\x01",
            "situation politically,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02804F#5PHaha, well I think I'll ask\x01",
            "Chairman MacDowell for his\x01",
            "help as well.\x02\x03",
            "#02800FIf it goes well, Liberl and\x01",
            "Remiferia might join me as\x01",
            "allies in this negotiation.\x02\x03",
            "#02809FAnyway, aside from preparing\x01",
            "for the worst, all I can do\x01",
            "is pray to the Goddess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00108F"Uncle"...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FSorry... For making you\x01",
            "give this tour during\x01",
            "such a difficult time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02804F#5PHaha, perish the thought.\x02\x03",
            "#02800FOn the contrary, it's precisely\x01",
            "because of the situation that I\x01",
            "wanted a change of pace.\x02\x03",
            "I volunteered specifically to\x01",
            "escort you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00002FIs that right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10101FWe're honored, Mr.\x01",
            "Mayor!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309FThen, we gladly accept.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02809F#5PYes, please leave it to\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x8, 0x0, 0x1F4)

    ChrTalk(
        0x8,
        "#11P#02800FOh, we're here.\x02",
    )

    CloseMessageWindow()
    StopSound(832, 1000, 100)
    ClearMapObjFlags(0x0, 0x20)
    OP_71(0x0, 0x37, 0x5A, 0x0, 0x0)
    OP_79(0x0)
    Sound(160, 0, 100, 0)
    VolumeBGM(0x64, 0x3E8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(107, 0, 100, 0)
    Sleep(500)
    OP_24(0x340)
    SetScenarioFlags(0x22, 0)
    NewScene("c1530", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_4_16DF end

    def Function_5_2561(): pass

    label("Function_5_2561")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02400.itc", 0x1E)
    LoadChrToIndex("chr/ch00900.itc", 0x1F)
    LoadChrToIndex("apl/ch51255.itc", 0x20)
    SoundLoad(832)
    OP_68(0, -10000, 0, 0)
    MoveCamera(45, 11, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x101, -600, 0, 0, 225)
    SetChrPos(0x102, 500, 0, 0, 225)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x1)
    SetChrFlags(0x103, 0x20)
    SetChrFlags(0x103, 0x10)
    SetChrFlags(0x103, 0x2)
    SetChrPos(0x103, -1500, 0, -1500, 270)
    SetChrPos(0x104, 1600, 0, -1000, 270)
    SetChrPos(0x109, 400, 0, -1300, 270)
    SetChrPos(0x105, 900, 0, -2200, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -700, 0, 1500, 180)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -1900, 0, 1300, 180)
    OP_71(0x0, 0x87, 0x9A, 0x0, 0x20)
    Sound(832, 2, 100, 0)
    BlurSwitch(0x1B58, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(0, 20000, 0, 7000)
    MoveCamera(45, 33, 0, 7000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(0, -900, 0, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    CancelBlur(0)
    OP_68(0, 1100, 0, 3000)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#11P#00203FYes... Yes.\x02\x03",
            "#00202FUnderstood. At least we\x01",
            "know that much.\x02\x03",
            "#00204FNice work Jona. See you\x01",
            "later.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x0)
    Sleep(300)
    Sound(804, 0, 100, 0)
    Sleep(400)

    ChrTalk(
        0x101,
        "#5P#00001FWhat did Jona say?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(802, 0, 100, 0)
    Fade(250)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x103, 0x20)
    ClearChrFlags(0x103, 0x10)
    ClearChrFlags(0x103, 0x2)
    OP_0D()
    OP_93(0x103, 0x2D, 0x1F4)

    ChrTalk(
        0x103,
        (
            "#6P#00203FHe computed the\x01",
            "terrorists' escape route.\x02\x03",
            "#00201FIt seems they'll escape to\x01",
            "the Geofront from Orchis\x01",
            "Tower's foundation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#5PThe foundation... That's\x01",
            "part of the tower's\x01",
            "basement.\x02\x03",
            "#00101FIndeed, it's connected\x01",
            "to several Geofront\x01",
            "sections.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00603F#5PAlright, we'll certainly capture\x01",
            "them.\x02\x03",
            "#00610FIf they get away after such\x01",
            "conduct, it'll be a stain on the\x01",
            "name of the Crossbell Police!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01403F#5P─I feel the same.\x02\x03",
            "#01401FThe guild has officially\x01",
            "witnessed their reckless actions\x01",
            "at this international conference.\x02\x03",
            "It would set a bad precedent if\x01",
            "we were to ignore it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10107F#11PYes, we'll get them for\x01",
            "sure!\x02\x03",
            "#10106FI'm a bit worried about\x01",
            "the orbal bombs on the\x01",
            "roof, though.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2AC8():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2AC8)
    Sleep(50)

    def lambda_2AD8():
        TurnDirection(0x102, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2AD8)
    Sleep(50)

    def lambda_2AE8():
        TurnDirection(0x105, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2AE8)
    Sleep(50)

    def lambda_2AF8():
        TurnDirection(0x103, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2AF8)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x103, 0)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00003F#5PIf Kilika and Lechter\x01",
            "are handling it, it'll\x01",
            "probably be all right.\x02\x03",
            "#00002FCaptain Julia and Major\x01",
            "Mueller are with them,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F#11PHaha, with that\x01",
            "combination there can't\x01",
            "be any doubt.\x02\x03",
            "#00305F...But it sure is a long\x01",
            "way down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00204FWe're going from 35F to\x01",
            "B8F.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#11PIt's taking us to the\x01",
            "depths of Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(0, 3100, 0, 2000)
    FadeToDark(2000, 0, -1)
    StopSound(832, 2000, 100)
    OP_0D()
    OP_6F(0x1)
    StopBGM(0x1388)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x340)
    SetScenarioFlags(0x22, 0)
    NewScene("m0400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_2561 end

    def Function_6_2CC0(): pass

    label("Function_6_2CC0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(0, 1000, 700, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(22250, 0)
    SetChrPos(0x101, 0, 0, 1300, 0)
    SetChrPos(0x102, 800, 0, 0, 0)
    SetChrPos(0x103, -800, 0, 0, 0)
    SetChrPos(0x104, 0, 0, -1600, 0)
    SetChrPos(0x109, 1200, 0, -1000, 0)
    SetChrPos(0x105, -1200, 0, -1000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetCameraDistance(21500, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#11P#00011FUmm... Is this where it\x01",
            "goes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00202FYes. Insert the\x01",
            "authentication card we\x01",
            "just got there.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(0, 1000, 1000, 800)

    def lambda_2E17():
        OP_96(0xFE, 0x0, 0x0, 0x960, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2E17)
    WaitChrThread(0x101, 1)
    Sleep(300)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Inserted the\x01",
            "authentication card into\x01",
            "the panel.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(72, 0, 100, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(500)
    SetScenarioFlags(0x164, 5)
    Call(0, 2)
    Return()

    # Function_6_2CC0 end

    def Function_7_2E8D(): pass

    label("Function_7_2E8D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(832)
    OP_68(0, 2300, 0, 0)
    MoveCamera(35, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x101, 0, 0, 1500, 180)
    SetChrPos(0x102, 1100, 0, 600, 225)
    SetChrPos(0x103, 1100, 0, -1000, 315)
    SetChrPos(0x104, 0, 0, -1500, 0)
    SetChrPos(0x109, -1100, 0, 600, 135)
    SetChrPos(0x105, -1100, 0, -1000, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_71(0x0, 0x23, 0x36, 0x0, 0x20)
    Sound(832, 2, 100, 0)
    Sleep(500)
    OP_68(0, 1300, 0, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x105,
        (
            "#6P#10305FCome to think of it,\x01",
            "there's something about\x01",
            "this panel...\x02\x03",
            "It doesn't look like\x01",
            "there are buttons for\x01",
            "21F through 30F.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00102FOh, they must all be\x01",
            "maintenance floors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#5PMaintenance floors?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#11PI'm told those floors are mostly\x01",
            "empty. It's necessary to maintain\x01",
            "this huge tower's weight balance.\x02\x03",
            "#00200FApart from that, it seems there\x01",
            "is equipment there to absorb the\x01",
            "shock of potential earthquakes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#5PThat's pretty amazing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10102FIt seems like the latest\x01",
            "building technologies\x01",
            "are all here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00306FSeriously though. Was it\x01",
            "really necessary to make\x01",
            "it this big?\x02\x03",
            "#00301FYou could make it 30\x01",
            "stories and still have the\x01",
            "same number of floors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00106FWell, I'm sure many changes\x01",
            "were made from the initial\x01",
            "design.\x02\x03",
            "#00100F"Uncle", who took over the\x01",
            "design, also likes flashy\x01",
            "things.\x02\x03",
            "#00104FIn the end, the Crois family\x01",
            "made up for the construction\x01",
            "budget shortfall personally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FWow, how magnanimous of\x01",
            "him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#5PWell, thanks to him, the tower's\x01",
            "had a huge impact as Crossbell\x01",
            "City's newest landmark, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00002F#5POh, looks like we're\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()
    MoveCamera(35, 30, 0, 4000)
    SetCameraDistance(19000, 4000)
    Sleep(3000)
    StopSound(832, 2000, 100)
    ClearMapObjFlags(0x0, 0x20)
    OP_71(0x0, 0x37, 0x5A, 0x0, 0x0)
    OP_79(0x0)
    OP_6F(0x79)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x164, 6)
    OP_24(0x340)
    EventEnd(0x5)
    NewScene("c1583", 109, 0, 0)
    IdleLoop()
    Return()

    # Function_7_2E8D end

    def Function_8_3469(): pass

    label("Function_8_3469")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(832)
    OP_68(0, 2300, 0, 0)
    MoveCamera(35, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 0, 0, 1500, 180)
    SetChrPos(0x102, 1100, 0, 600, 225)
    SetChrPos(0x103, 1100, 0, -1000, 315)
    SetChrPos(0x104, 0, 0, -1500, 0)
    SetChrPos(0xF4, -1100, 0, 600, 135)
    SetChrPos(0xF5, -1100, 0, -1000, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_71(0x0, 0x23, 0x36, 0x0, 0x20)
    Sound(832, 2, 100, 0)
    OP_68(0, 1300, 0, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00008F#5P─In the end, we could\x01",
            "only disable security up\x01",
            "to 21F.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206FAccording to chief, there's\x01",
            "a physically isolated\x01",
            "terminal on 30F.\x02\x03",
            "#00201FHe says control of the\x01",
            "orbal network is impossible\x01",
            "until it's breached.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303FThen that means we need to\x01",
            "go from 21F to 30F\x01",
            "ourselves.\x02\x03",
            "#00301FBut, I think I remember\x01",
            "something about them being\x01",
            "empty maintenance floors?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00106FIt seems that was a lie.\x02\x03",
            "#00108FIt seems that section\x01",
            "contains the mysteries of\x01",
            "the Crois clan...\x02\x03",
            "#00101FIt seems it had an\x01",
            "important role to play in\x01",
            "KeA's ceremony as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00307FS-Seriously?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3871")

    ChrTalk(
        0x10A,
        (
            "#6P#00606F...I thought it was strange\x01",
            "during the trade conference\x01",
            "security detail, but...\x02\x03",
            "#00610FIt can't believe they\x01",
            "created a place like this\x01",
            "inside a public building.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3871")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3930")

    ChrTalk(
        0x105,
        (
            "#6P#10403FThis area is probably full of\x01",
            "the fruits of magical science.\x02\x03",
            "#10408FIf possible, I would've liked\x01",
            "to have a look at before things\x01",
            "turned out like this, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3930")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3983")

    ChrTalk(
        0x109,
        (
            "#6P#10103FAt any rate... It seems\x01",
            "we'll need to prepare.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39BD")

    label("loc_3983")


    ChrTalk(
        0x103,
        (
            "#00203F...In any case, we need\x01",
            "to resolve ourselves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39BD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3A1E")

    ChrTalk(
        0x106,
        (
            "#6P#10701F...Right. Red\x01",
            "Constellation personnel\x01",
            "may be waiting for us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A77")

    label("loc_3A1E")


    ChrTalk(
        0x102,
        (
            "#11P#00106FYou're right... It's\x01",
            "possible Arios and Red\x01",
            "Constellation are there too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A77")


    ChrTalk(
        0x101,
        (
            "#00008F#5PYeah... And KeA.\x02\x03",
            "#00003F...No matter what's waiting\x01",
            "for us, we have to break\x01",
            "through it.\x02\x03",
            "#00000FWe have to answer the\x01",
            "expectations of chief and the\x01",
            "others who got us this far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F...Right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00102FHaha... No pressure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00304FLet's get fired up!\x02",
    )

    CloseMessageWindow()
    OP_68(0, -1700, 0, 3000)
    StopSound(832, 2000, 100)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0x1770)
    OP_6F(0x79)
    WaitBGM()
    ReplaceBGM("ed7352", "ed7000")
    SetScenarioFlags(0x1A6, 1)
    OP_29(0xB1, 0x1, 0xA)
    OP_24(0x340)
    SetScenarioFlags(0x25, 1)
    EventEnd(0x5)
    NewScene("c1580", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_3469 end

    def Function_9_3BE1(): pass

    label("Function_9_3BE1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(832)
    OP_68(0, 2300, 100000, 0)
    MoveCamera(55, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 1500, 0, 100000, 270)
    SetChrPos(0x102, 600, 0, 101100, 225)
    SetChrPos(0x103, -1000, 0, 101100, 135)
    SetChrPos(0x104, -1500, 0, 100000, 90)
    SetChrPos(0xF4, 600, 0, 98900, 315)
    SetChrPos(0xF5, -1000, 0, 98900, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    BeginChrThread(0x101, 3, 0, 11)
    Sound(832, 2, 100, 0)
    OP_68(0, 1300, 100000, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00003F#11PBy the way...\x02\x03",
            "#00001FHe said there was a control\x01",
            "terminal isolated from the\x01",
            "orbal network, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#5PYes. Because of it, hacking the\x01",
            "tower's upper floors is\x01",
            "impossible.\x02\x03",
            "#00201FIf we unlock it, I think chief\x01",
            "will be able to grab detailed info\x01",
            "regarding the upper floors...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00108FSuch as the location of\x01",
            "KeA and what Bell and\x01",
            "the others are planning.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3E93")

    ChrTalk(
        0x10A,
        (
            "#12P#00603FWe've got to gain\x01",
            "control of it somehow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F2A")

    label("loc_3E93")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3EE1")

    ChrTalk(
        0x109,
        (
            "#12P#10103FWe need to gain control\x01",
            "of it somehow...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F2A")

    label("loc_3EE1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F2A")

    ChrTalk(
        0x106,
        (
            "#12P#10703FWe need to gain control\x01",
            "of it somehow...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F2A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F5C")

    ChrTalk(
        0x105,
        "#12P#10401F30F, was it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FC1")

    label("loc_3F5C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F95")

    ChrTalk(
        0x106,
        "#12P#10701FIt's on 30F, right?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FC1")

    label("loc_3F95")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3FC1")

    ChrTalk(
        0x109,
        "#12P#10101F30F, right?\x02",
    )

    CloseMessageWindow()

    label("loc_3FC1")


    ChrTalk(
        0x103,
        (
            "#00203F#5PYes. The top floor of\x01",
            "this central section, I\x01",
            "believe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00300FIn that case, let's set\x01",
            "our sights for the top.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#11PYeah... Let's do this!\x02",
    )

    CloseMessageWindow()
    OP_68(0, -8700, 100000, 2000)
    StopSound(832, 2000, 100)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetScenarioFlags(0x1A6, 3)
    Sound(160, 0, 100, 0)
    Sleep(500)
    OP_24(0x340)
    EventEnd(0x5)
    ClearMapFlags(0x8000000)
    NewScene("c1582", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_9_3BE1 end

    def Function_10_40B1(): pass

    label("Function_10_40B1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(832)
    SoundLoad(803)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    OP_68(0, 2300, 0, 0)
    MoveCamera(35, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 0, 0, 1500, 180)
    SetChrPos(0x102, 1100, 0, 600, 225)
    SetChrPos(0x103, 1100, 0, -1000, 315)
    SetChrPos(0x104, 0, 0, -1500, 0)
    SetChrPos(0xF4, -1100, 0, 600, 135)
    SetChrPos(0xF5, -1100, 0, -1000, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_71(0x0, 0x23, 0x36, 0x0, 0x20)
    Sound(832, 2, 100, 0)
    OP_68(0, 1300, 0, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_41F5():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_41F5)
    Sleep(50)

    def lambda_4205():
        TurnDirection(0xF4, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_4205)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0xF4, 0)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x6)
    Sound(802, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x7)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    Sound(2085, 255, 100, 0)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00013FHello?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Fran's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "T-Thank goodness...\x01",
            "You're all ok!\x02\x03",
            "This is Merkabah No. 9\x01",
            "speaking!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_432C")
    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x109,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#10102FFran!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_434C")

    label("loc_432C")

    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x102,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00102FFran!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_434C")

    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("Abbas' Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It seems you've\x01",
            "infiltrated the tower.\x01",
            "How is it going?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_443D")
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00003FWe're actually just\x01",
            "about finished already.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x105,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#10400FI'll give you a brief\x01",
            "explanation.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_449B")

    label("loc_443D")

    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00001FWell, we're just about\x01",
            "finished. I'll give you\x01",
            "a brief explanation.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_449B")

    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd informed the\x01",
            "Merkabah bridge crew of\x01",
            "the current situation.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("Abbas' Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I see... It really does\x01",
            "seem like you're almost\x01",
            "done.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Jona's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It looks like that white doll\x01",
            "on the roof has deployed a\x01",
            "100-arge radius Barrier.\x02\x03",
            "We can't get any closer so\x01",
            "don't expect cover fire or\x01",
            "anything, ok?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00013FAlright... I understand.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_46A9")
    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x105,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#10406FWell, I guess we're going\x01",
            "to have to do something\x01",
            "about it ourselves.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_470B")

    label("loc_46A9")

    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x104,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00306FWell, I guess we'll just\x01",
            "have to do something\x01",
            "about it ourselves, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_470B")

    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Fran's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "By the way, the other two\x01",
            "Aions... It seems they've been\x01",
            "silenced.\x02\x03",
            "It seems Father Kevin, Estelle\x01",
            "& friends and the others have\x01",
            "been doing a great job for us.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005FSo that's how it is.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00204F...That's good news.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x104,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00300FYeah... Those were some\x01",
            "nice wins.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Grace's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "─Anyway! Don't do\x01",
            "anything reckless!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("Chairman MacDowell's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "May Aidios protect\x01",
            "you... And please, be\x01",
            "careful out there.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x102,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00100FRight!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00000FRoger!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x6)
    Sound(804, 0, 100, 0)
    OP_68(0, -1700, 0, 3000)
    StopSound(832, 2000, 100)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    OP_24(0x323)
    OP_24(0x340)
    SetScenarioFlags(0x22, 0)
    NewScene("e4201", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_10_40B1 end

    def Function_11_49E3(): pass

    label("Function_11_49E3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A1B")
    OP_82(0x0, 0x5, 0xBB8, 0x1F4)
    Sleep(2000)
    OP_82(0x0, 0xA, 0x3E8, 0x1F4)
    Sleep(1000)
    Jump("Function_11_49E3")

    label("loc_4A1B")

    Return()

    # Function_11_49E3 end

    SaveToFile()

Try(main)
