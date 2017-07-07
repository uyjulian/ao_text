from ScenarioHelper import *

def main():
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
        "Mayor of Dieter",         # 1
        "Arios",               # 2
        "Dudley investigator",         # 3
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
        "Function_3_1292",         # 03, 3
        "Function_4_1792",         # 04, 4
        "Function_5_2439",         # 05, 5
        "Function_6_2B4F",         # 06, 6
        "Function_7_2D0B",         # 07, 7
        "Function_8_3250",         # 08, 8
        "Function_9_395B",         # 09, 9
        "Function_10_3E1F",        # 0A, 10
        "Function_11_466F",        # 0B, 11
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7B0")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_695")
    MenuCmd(1, 0, "★ 【40F】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6A5")

    label("loc_695")

    MenuCmd(1, 0, "【40 F】")

    label("loc_6A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D3")
    MenuCmd(1, 0, "★ 【36F】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6E3")

    label("loc_6D3")

    MenuCmd(1, 0, "【36 F】")

    label("loc_6E3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_710")
    MenuCmd(1, 0, "★ 【21F】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_720")

    label("loc_710")

    MenuCmd(1, 0, "【21F】")

    label("loc_720")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74E")
    MenuCmd(1, 0, "★ 【1F】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_75E")

    label("loc_74E")

    MenuCmd(1, 0, "【1F】")

    label("loc_75E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x77), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_78B")
    MenuCmd(1, 0, "★ 【B8F】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_79B")

    label("loc_78B")

    MenuCmd(1, 0, "【B8F】")

    label("loc_79B")

    MenuCmd(1, 0, " 【get off】")
    Jump("loc_AC2")

    label("loc_7B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 7)), scpexpr(EXPR_END)), "loc_8C5")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E7")
    MenuCmd(1, 0, "★ 【40F】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7F7")

    label("loc_7E7")

    MenuCmd(1, 0, "【40 F】")

    label("loc_7F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_825")
    MenuCmd(1, 0, "★ 【36F】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_835")

    label("loc_825")

    MenuCmd(1, 0, "【36 F】")

    label("loc_835")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_862")
    MenuCmd(1, 0, "★ 【21F】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_872")

    label("loc_862")

    MenuCmd(1, 0, "【21F】")

    label("loc_872")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A0")
    MenuCmd(1, 0, "★ 【1F】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8B0")

    label("loc_8A0")

    MenuCmd(1, 0, "【1F】")

    label("loc_8B0")

    MenuCmd(1, 0, " 【get off】")
    Jump("loc_AC2")

    label("loc_8C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_END)), "loc_95E")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FB")
    MenuCmd(1, 0, "★ 【21F】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_90B")

    label("loc_8FB")

    MenuCmd(1, 0, "【21F】")

    label("loc_90B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_939")
    MenuCmd(1, 0, "★ 【1F】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_949")

    label("loc_939")

    MenuCmd(1, 0, "【1F】")

    label("loc_949")

    MenuCmd(1, 0, " 【get off】")
    Jump("loc_AC2")

    label("loc_95E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 5)), scpexpr(EXPR_END)), "loc_9F8")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_995")
    MenuCmd(1, 0, "★ 【40F】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9A5")

    label("loc_995")

    MenuCmd(1, 0, "【40 F】")

    label("loc_9A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D3")
    MenuCmd(1, 0, "★ 【1F】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9E3")

    label("loc_9D3")

    MenuCmd(1, 0, "【1F】")

    label("loc_9E3")

    MenuCmd(1, 0, " 【get off】")
    Jump("loc_AC2")

    label("loc_9F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A26")
    MenuCmd(1, 0, "★ 【36F】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A36")

    label("loc_A26")

    MenuCmd(1, 0, "【36 F】")

    label("loc_A36")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A64")
    MenuCmd(1, 0, "★ 【35F】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A74")

    label("loc_A64")

    MenuCmd(1, 0, "【35 F】")

    label("loc_A74")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA2")
    MenuCmd(1, 0, "★ 【34F】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AB2")

    label("loc_AA2")

    MenuCmd(1, 0, "【34F】")

    label("loc_AB2")

    MenuCmd(1, 0, " 【get off】")

    label("loc_AC2")

    MenuCmd(2, 0, 10, 10, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B8F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF9")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B8A")

    label("loc_AF9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B17")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B8A")

    label("loc_B17")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B35")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B8A")

    label("loc_B35")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B53")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B8A")

    label("loc_B53")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B71")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B8A")

    label("loc_B71")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B8A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B8A")

    Jump("loc_D67")

    label("loc_B8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 7)), scpexpr(EXPR_END)), "loc_C2E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB6")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C29")

    label("loc_BB6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BD4")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C29")

    label("loc_BD4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C29")

    label("loc_BF2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C10")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C29")

    label("loc_C10")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C29")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C29")

    Jump("loc_D67")

    label("loc_C2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_END)), "loc_C91")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C55")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C8C")

    label("loc_C55")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C73")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C8C")

    label("loc_C73")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C8C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C8C")

    Jump("loc_D67")

    label("loc_C91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 5)), scpexpr(EXPR_END)), "loc_CF4")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB8")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CEF")

    label("loc_CB8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD6")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CEF")

    label("loc_CD6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CEF")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CEF")

    Jump("loc_D67")

    label("loc_CF4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D12")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D67")

    label("loc_D12")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D30")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D67")

    label("loc_D30")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D4E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D67")

    label("loc_D4E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D67")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D67")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D86")
    FadeToDark(500, 0, -1)
    OP_0D()
    Jump("loc_EC7")

    label("loc_D86")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E21")
    Sound(159, 0, 100, 0)
    OP_71(0x0, 0x64, 0x87, 0x0, 0x0)
    OP_79(0x0)
    OP_71(0x0, 0x87, 0x9A, 0x0, 0x20)
    FadeToDark(2000, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_DDD")
    OP_68(0, 4000, 1000, 2000)
    Jump("loc_E16")

    label("loc_DDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_DFC")
    OP_68(70000, 4000, 1000, 2000)
    Jump("loc_E16")

    label("loc_DFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_E16")
    OP_68(140000, 4000, 1000, 2000)

    label("loc_E16")

    OP_0D()
    OP_6F(0x1)
    Sleep(300)
    Jump("loc_EC7")

    label("loc_E21")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EBC")
    Sound(159, 0, 100, 0)
    OP_71(0x0, 0x0, 0x23, 0x0, 0x0)
    OP_79(0x0)
    OP_71(0x0, 0x23, 0x36, 0x0, 0x20)
    FadeToDark(2000, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E78")
    OP_68(0, -3500, 1000, 2000)
    Jump("loc_EB1")

    label("loc_E78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_E97")
    OP_68(70000, -3500, 1000, 2000)
    Jump("loc_EB1")

    label("loc_E97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_EB1")
    OP_68(140000, -3500, 1000, 2000)

    label("loc_EB1")

    OP_0D()
    OP_6F(0x1)
    Sleep(300)
    Jump("loc_EC7")

    label("loc_EBC")

    FadeToDark(500, 0, -1)
    OP_0D()

    label("loc_EC7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1092")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_F0A"),
        (1, "loc_F51"),
        (2, "loc_F98"),
        (3, "loc_FDF"),
        (4, "loc_1026"),
        (5, "loc_1036"),
        (6, "loc_107D"),
        (SWITCH_DEFAULT, "loc_108D"),
    )


    label("loc_F0A")

    EventEnd(0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F23")
    NewScene("c1583", 109, 0, 0)
    IdleLoop()
    Jump("loc_F4C")

    label("loc_F23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_F3A")
    NewScene("c1583", 110, 0, 0)
    IdleLoop()
    Jump("loc_F4C")

    label("loc_F3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_F4C")
    NewScene("c1583", 111, 0, 0)
    IdleLoop()

    label("loc_F4C")

    Jump("loc_108D")

    label("loc_F51")

    EventEnd(0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F6A")
    NewScene("c1550", 100, 0, 0)
    IdleLoop()
    Jump("loc_F93")

    label("loc_F6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_F81")
    NewScene("c1550", 101, 0, 0)
    IdleLoop()
    Jump("loc_F93")

    label("loc_F81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_F93")
    NewScene("c1550", 102, 0, 0)
    IdleLoop()

    label("loc_F93")

    Jump("loc_108D")

    label("loc_F98")

    EventEnd(0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_FB1")
    NewScene("c1540", 100, 0, 0)
    IdleLoop()
    Jump("loc_FDA")

    label("loc_FB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_FC8")
    NewScene("c1540", 101, 0, 0)
    IdleLoop()
    Jump("loc_FDA")

    label("loc_FC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_FDA")
    NewScene("c1540", 102, 0, 0)
    IdleLoop()

    label("loc_FDA")

    Jump("loc_108D")

    label("loc_FDF")

    EventEnd(0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_FF8")
    NewScene("c1530", 100, 0, 0)
    IdleLoop()
    Jump("loc_1021")

    label("loc_FF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_100F")
    NewScene("c1530", 101, 0, 0)
    IdleLoop()
    Jump("loc_1021")

    label("loc_100F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1021")
    NewScene("c1530", 102, 0, 0)
    IdleLoop()

    label("loc_1021")

    Jump("loc_108D")

    label("loc_1026")

    EventEnd(0x5)
    NewScene("c1580", 100, 0, 0)
    IdleLoop()
    Jump("loc_108D")

    label("loc_1036")

    EventEnd(0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_104F")
    NewScene("c1510", 103, 0, 0)
    IdleLoop()
    Jump("loc_1078")

    label("loc_104F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1066")
    NewScene("c1510", 104, 0, 0)
    IdleLoop()
    Jump("loc_1078")

    label("loc_1066")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1078")
    NewScene("c1510", 105, 0, 0)
    IdleLoop()

    label("loc_1078")

    Jump("loc_108D")

    label("loc_107D")

    EventEnd(0x5)
    NewScene("m0400", 100, 0, 0)
    IdleLoop()
    Jump("loc_108D")

    label("loc_108D")

    Jump("loc_1291")

    label("loc_1092")

    SetScenarioFlags(0x25, 1)
    Sleep(500)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_10CC"),
        (1, "loc_113F"),
        (2, "loc_1186"),
        (3, "loc_11CD"),
        (4, "loc_1214"),
        (5, "loc_123A"),
        (6, "loc_1281"),
        (SWITCH_DEFAULT, "loc_1291"),
    )


    label("loc_10CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10E2")
    Call(0, 7)
    Jump("loc_113A")

    label("loc_10E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10F8")
    Call(0, 10)
    Jump("loc_113A")

    label("loc_10F8")

    EventEnd(0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1111")
    NewScene("c1583", 109, 0, 0)
    IdleLoop()
    Jump("loc_113A")

    label("loc_1111")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1128")
    NewScene("c1583", 110, 0, 0)
    IdleLoop()
    Jump("loc_113A")

    label("loc_1128")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_113A")
    NewScene("c1583", 111, 0, 0)
    IdleLoop()

    label("loc_113A")

    Jump("loc_1291")

    label("loc_113F")

    EventEnd(0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1158")
    NewScene("c1550", 100, 0, 0)
    IdleLoop()
    Jump("loc_1181")

    label("loc_1158")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_116F")
    NewScene("c1550", 101, 0, 0)
    IdleLoop()
    Jump("loc_1181")

    label("loc_116F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1181")
    NewScene("c1550", 102, 0, 0)
    IdleLoop()

    label("loc_1181")

    Jump("loc_1291")

    label("loc_1186")

    EventEnd(0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_119F")
    NewScene("c1540", 100, 0, 0)
    IdleLoop()
    Jump("loc_11C8")

    label("loc_119F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_11B6")
    NewScene("c1540", 101, 0, 0)
    IdleLoop()
    Jump("loc_11C8")

    label("loc_11B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_11C8")
    NewScene("c1540", 102, 0, 0)
    IdleLoop()

    label("loc_11C8")

    Jump("loc_1291")

    label("loc_11CD")

    EventEnd(0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_11E6")
    NewScene("c1530", 100, 0, 0)
    IdleLoop()
    Jump("loc_120F")

    label("loc_11E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_11FD")
    NewScene("c1530", 101, 0, 0)
    IdleLoop()
    Jump("loc_120F")

    label("loc_11FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_120F")
    NewScene("c1530", 102, 0, 0)
    IdleLoop()

    label("loc_120F")

    Jump("loc_1291")

    label("loc_1214")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_122A")
    Call(0, 8)
    Jump("loc_1235")

    label("loc_122A")

    EventEnd(0x5)
    NewScene("c1580", 100, 0, 0)
    IdleLoop()

    label("loc_1235")

    Jump("loc_1291")

    label("loc_123A")

    EventEnd(0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1253")
    NewScene("c1510", 103, 0, 0)
    IdleLoop()
    Jump("loc_127C")

    label("loc_1253")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_126A")
    NewScene("c1510", 104, 0, 0)
    IdleLoop()
    Jump("loc_127C")

    label("loc_126A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_127C")
    NewScene("c1510", 105, 0, 0)
    IdleLoop()

    label("loc_127C")

    Jump("loc_1291")

    label("loc_1281")

    EventEnd(0x5)
    NewScene("m0400", 100, 0, 0)
    IdleLoop()
    Jump("loc_1291")

    label("loc_1291")

    Return()

    # Function_2_2AF end

    def Function_3_1292(): pass

    label("Function_3_1292")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    SoundLoad(832)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is an elevator control panel.\x01",
            "Do you want to operate it?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_178A")
    Fade(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1410")
    SetChrPos(0x0, 1800, 0, 100000, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_134D")
    SetChrPos(0x1, 600, 0, 100800, 90)

    label("loc_134D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_136C")
    SetChrPos(0x2, 600, 0, 99200, 90)

    label("loc_136C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_138B")
    SetChrPos(0x3, -500, 0, 100000, 90)

    label("loc_138B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13B4")
    SetChrPos(0x4, -1600, 0, 100800, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_13B4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13DD")
    SetChrPos(0x5, -1600, 0, 99200, 90)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_13DD")

    OP_68(1000, 1000, 100000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19500, 0)
    Jump("loc_1515")

    label("loc_1410")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1515")
    SetChrPos(0x0, 70000, 0, 101800, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1457")
    SetChrPos(0x1, 70800, 0, 100600, 0)

    label("loc_1457")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1476")
    SetChrPos(0x2, 69200, 0, 100600, 0)

    label("loc_1476")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1495")
    SetChrPos(0x3, 70000, 0, 99500, 0)

    label("loc_1495")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14BE")
    SetChrPos(0x4, 70800, 0, 98400, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_14BE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14E7")
    SetChrPos(0x5, 69200, 0, 98400, 0)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_14E7")

    OP_68(70000, 1000, 101000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19500, 0)

    label("loc_1515")

    OP_0D()
    Sleep(500)
    Sound(159, 0, 100, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1543")
    OP_68(1000, -9000, 100000, 3000)
    Jump("loc_15AA")

    label("loc_1543")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1567")
    OP_68(1000, 9000, 100000, 3000)
    Jump("loc_15AA")

    label("loc_1567")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_158B")
    OP_68(70000, -9000, 101000, 3000)
    Jump("loc_15AA")

    label("loc_158B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15AA")
    OP_68(70000, 9000, 101000, 3000)

    label("loc_15AA")

    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15D5")
    Call(0, 9)
    Return()

    label("loc_15D5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1610")
    Sound(832, 2, 100, 0)
    OP_68(1000, 9000, 100000, 0)
    OP_68(1000, 1000, 100000, 3000)
    Jump("loc_16BC")

    label("loc_1610")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_164B")
    Sound(832, 2, 100, 0)
    OP_68(1000, -9000, 100000, 0)
    OP_68(1000, 1000, 100000, 3000)
    Jump("loc_16BC")

    label("loc_164B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1686")
    Sound(832, 2, 100, 0)
    OP_68(70000, 9000, 101000, 0)
    OP_68(70000, 1000, 101000, 3000)
    Jump("loc_16BC")

    label("loc_1686")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16BC")
    Sound(832, 2, 100, 0)
    OP_68(70000, -9000, 101000, 0)
    OP_68(70000, 1000, 101000, 3000)

    label("loc_16BC")

    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    StopSound(832, 1000, 100)
    Sound(160, 0, 100, 0)
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16F9")
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_10(0xF, 0x0)
    OP_10(0x10, 0x1)
    Jump("loc_175A")

    label("loc_16F9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_171B")
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_10(0xF, 0x1)
    OP_10(0x10, 0x0)
    Jump("loc_175A")

    label("loc_171B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_173D")
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_10(0x11, 0x0)
    OP_10(0x12, 0x1)
    Jump("loc_175A")

    label("loc_173D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_175A")
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_10(0x11, 0x1)
    OP_10(0x12, 0x0)

    label("loc_175A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1772")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_1772")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_178A")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_178A")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_3_1292 end

    def Function_4_1792(): pass

    label("Function_4_1792")

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
    SetChrName("Voice of Dieter")

    AnonymousTalk(
        0xFF,
        "─ ─ I see.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "I also heard from Dudley\x01",
            "It is indeed a dangerous situation.\x02",
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
            "#12P#00006FYes……\x02\x03",
            "#00001FTrends in hunting corps and criminal organizations\x01",
            "Imperial government and the republican government's speculation … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00108F… … And we aim for the leaders of both countries\x01",
            "There is also the threat of terrorists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FAnd that is a mysterious hacker.\x02\x03",
            "#00200FThe drawing of the robbed tower\x01",
            "Is it still from this terminal?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02806F#5POh, apparently\x01",
            "Subterminal of Orkis Tower\x01",
            "He seems to have hacked.\x02\x03",
            "#02801FSince there was one case of IBC,\x01",
            "Also in the system division hacking measures\x01",
            "I intended to have strengthened … …\x02\x03",
            "It looks like it was not enough yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FHmm, like hackers\x01",
            "Although the number seems to be still small.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FAfter all, the Epstein Foundation's\x01",
            "Is there a high possibility of stakeholders?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FCurrently, Roberts'\x01",
            "We are exploring that possibility.\x02\x03",
            "#00208FHowever, this time the officials of the foundation\x01",
            "It feels like nothing ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02804F#5PWell, that investigation\x01",
            "I have no choice but to categorize.\x02\x03",
            "#02801FHunting corps and criminal organizations,\x01",
            "Terrorists are worried, but …\x02\x03",
            "More worrisome than that\x01",
            "It is aim and speculation of the leaders.\x02",
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
        "#12P#00001FThe aims and speculation of the leaders … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301FIn other words,\x01",
            "Is it a participant?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02803F#5PWith Princess Claudia you guys met\x01",
            "About Oliver's Prince\x01",
            "I am not too worried.\x02\x03",
            "Daemon Excellency of Remiferia also\x01",
            "It would be a trustworthy person.\x02\x03",
            "#02801F… … The problem is with Prime Minister Osborne\x01",
            "Two people, Rock Smith.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10108FAre you the leaders of two major powers …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305FCertainly the fate of crossbell\x01",
            "I think that it is the two who are holding.\x02\x03",
            "#10301FSpecifically, is there any movement?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02806F#5PNo, it is the reverse.\x02\x03",
            "#02801F── In holding the meeting\x01",
            "Some arrangements and international agreements etc\x01",
            "I sent a proposal in advance … …\x02\x03",
            "The reply returned is\x01",
            "Both countries were too favorable.\x02\x03",
            "As if it was serious, Peace of Western Zemria\x01",
            "As if wishing for development.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00011FWell, that is ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106F…… It is unnatural indeed.\x02\x03",
            "#00101FEvery time there is always a thing\x01",
            "Even though they are two countries repelling each other … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02803F#5POh, the honest meeting itself\x01",
            "I can not predict how it will flow.\x02\x03",
            "#02801FIt can also be a tough development\x01",
            "It seems necessary to prepare.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00208FI see……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FAnd, after all politically\x01",
            "It is a difficult situation …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02804F#5PWell, McDowell chairman too\x01",
            "It will become a power.\x02\x03",
            "#02800FSuccessfully Ribeel and\x01",
            "Letter to Remiperia and others\x01",
            "I might be able to negotiate.\x02\x03",
            "#02809FAnyway getting hungry\x01",
            "goddess#4REidos#There is no choice but to pray.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00108Funcle……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FExcuse me……\x01",
            "In such a difficult time\x01",
            "Let me guide you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02804F#5PHaha, nothing.\x02\x03",
            "#02800FBecause it is such a situation\x01",
            "I wanted to change my mood.\x02\x03",
            "All the way to express your guidance\x01",
            "I bought it and it came out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00002FOh really……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10101FIt is an honor, your honorable Mayor!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FThen, please pleased.\x01",
            "I will show you around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#02809F#5POh, leave it to me.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x8, 0x0, 0x1F4)

    ChrTalk(
        0x8,
        "#11P#02800FOops, it is arrival.\x02",
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

    # Function_4_1792 end

    def Function_5_2439(): pass

    label("Function_5_2439")

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
            "#11P#00203Fyeah yeah.\x02\x03",
            "#00202F……I understand.\x01",
            "It is enough to know so far.\x02\x03",
            "#00204FIt was hard work, Jonah.\x01",
            "See you later.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x0)
    Sleep(300)
    Sound(804, 0, 100, 0)
    Sleep(400)

    ChrTalk(
        0x101,
        "#5P#00001FWhat is Jonah …?\x02",
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
            "#6P#00203FTerrorists' escape route\x01",
            "I heard he was able to figure out.\x02\x03",
            "#00201FOrkis Tower base -\x01",
            "From there follow the Geo Front\x01",
            "You seem to have escaped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#5PWhat is the base?\x01",
            "It will be the underground part of the tower.\x02\x03",
            "#00101FCertainly, each section of Geo Front\x01",
            "It should be connected ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00603F#5PAlright, you will surely catch it.\x02\x03",
            "#00610FIf you do not do it like that\x01",
            "Cross Bell Police is a fame!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01403F#5P── That is also the same here.\x02\x03",
            "#01401FThe guild officially witnessed\x01",
            "That violent act at the international conference … …\x02\x03",
            "If you missed it\x01",
            "I have not made a bad precedent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10107F#11PLet's catch it absolutely!\x02\x03",
            "#10106FRooftop power bomb also\x01",
            "I am a bit worried … ….\x02",
        )
    )

    CloseMessageWindow()

    def lambda_294E():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_294E)
    Sleep(50)

    def lambda_295E():
        TurnDirection(0x102, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_295E)
    Sleep(50)

    def lambda_296E():
        TurnDirection(0x105, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_296E)
    Sleep(50)

    def lambda_297E():
        TurnDirection(0x103, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_297E)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x103, 0)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00003F#5PMr. Kirika and Rector\x01",
            "Probably it will be okay.\x02\x03",
            "#00002FColonel Yulia and Major Muller also\x01",
            "I am following you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F#11PHaha, indeed if that Menzu\x01",
            "There seems to be no mistake.\x02\x03",
            "#00305F… but …\x01",
            "Do not you keep going down for a long time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00204FWell, from the ground 35F\x01",
            "I will get down to basement 8F.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#11PIn the deepest portion of the crossbell\x01",
            "I guess it's guidance.\x02",
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

    # Function_5_2439 end

    def Function_6_2B4F(): pass

    label("Function_6_2B4F")

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
            "#11P#00011FEr …\x01",
            "Is it good here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00202FYes, the previous authentication card\x01",
            "Please hold it over there.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(0, 1000, 1000, 800)

    def lambda_2CA3():
        OP_96(0xFE, 0x0, 0x0, 0x960, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2CA3)
    WaitChrThread(0x101, 1)
    Sleep(300)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I held the temporary authentication card over the panel.\x07\x00\x02",
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

    # Function_6_2B4F end

    def Function_7_2D0B(): pass

    label("Function_7_2D0B")

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
            "#6P#10305FBy the way, that panel …\x02\x03",
            "From 21F to 30F\x01",
            "It seems there is no button?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00102FOh, everything around that\x01",
            "It looks like a maintenance floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#5PMaintenance floor?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#11PAnything, a huge structure\x01",
            "In order to balance weight\x01",
            "It is almost hollow.\x02\x03",
            "#00200FBesides that, when the earthquake occurred\x01",
            "There seems to be a shock absorber.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#5PThat's terrible …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10102FAgain the latest construction technology\x01",
            "It seems to be included.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00306FHold on to it.\x01",
            "Is it necessary to build a huge building?\x02\x03",
            "#00301FIf it is the same floor number, about 30 F in building\x01",
            "Well then it is delicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00106FWell, from the original plan\x01",
            "It seems there was a lot of waste … …\x02\x03",
            "#00100FThe uncle who took over the plan also\x01",
            "It is a person who loves flashy things.\x02\x03",
            "#00104FAfter all, the missing construction cost was\x01",
            "I heard that it was compensated by the assets of the Clois family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10302FWell, that is also a lot of fun.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#5PWell, thanks to Crossbell City\x01",
            "As a new landmark\x01",
            "I think there is a reasonable impact ….\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00002F#5POops, it is about to arrive.\x02",
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

    # Function_7_2D0B end

    def Function_8_3250(): pass

    label("Function_8_3250")

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
            "#00008F#5PAfter all, security\x01",
            "Is it possible to cancel until 21F …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206FYes, the boss says,\x01",
            "Make physical shutdown to 30F\x01",
            "There seems to be a control terminal.\x02\x03",
            "#00201FUnless you release it,\x01",
            "Control from the power net\x01",
            "He said that it was impossible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303FIt means that from 21F to 30F\x01",
            "Is it necessary to go up by themselves?\x02\x03",
            "#00301FBut surely that place\x01",
            "Mostly on the maintenance floor\x01",
            "Did not you say empty?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00106F…… to the official announcement\x01",
            "It seems there was a lie.\x02\x03",
            "#00108FApparently the one\x01",
            "Deep in the Clois family … …\x02\x03",
            "#00101FEven in Kaea's ceremony\x01",
            "It seems to be an area that played an important role.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00307FIs that right?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3648")

    ChrTalk(
        0x10A,
        (
            "#6P#00606F…… even during the security of the trade council\x01",
            "I thought it was strangely unnatural … …\x02\x03",
            "#00610FNo way to place such a place in a public facility\x01",
            "I guess it was built without permission.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3648")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_36D3")

    ChrTalk(
        0x105,
        (
            "#6P#10403FPerhaps Mika of Magic Science\x01",
            "It might be packed block.\x02\x03",
            "#10408FIf possible, before this\x01",
            "I wanted to preview him … ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36D3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_371F")

    ChrTalk(
        0x109,
        (
            "#6P#10103FAnyway …\x01",
            "You seem to be prepared for it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3753")

    label("loc_371F")


    ChrTalk(
        0x103,
        (
            "#00203F… Anyway\x01",
            "You seem to be prepared for it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3753")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_37B2")

    ChrTalk(
        0x106,
        (
            "#6P#10701F……Yes.\x01",
            "\"Red constellation\" people and others\x01",
            "You may be there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37FF")

    label("loc_37B2")


    ChrTalk(
        0x102,
        (
            "#11P#00106FI see …\x01",
            "Ariosさんや《赤い星座》も\x01",
            "There may be.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37FF")


    ChrTalk(
        0x101,
        (
            "#00008F#5POh … and Ka'aa.\x02\x03",
            "#00003F…… Whatever is awaiting\x01",
            "I will definitely break through.\x02\x03",
            "#00000FThey sent us out here\x01",
            "To respond to the section chiefs as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F……Yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00102FHuh … …. Responsible serious.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00304FScreaming ……\x01",
            "You do not have to put it in.\x02",
        )
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

    # Function_8_3250 end

    def Function_9_395B(): pass

    label("Function_9_395B")

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
            "#00003F#11Pby the way……\x02\x03",
            "#00001FWe are blocking the power net\x01",
            "Control terminal\x01",
            "You said it was there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#5PYes, because of its location\x01",
            "Hacking to the top of the tower\x01",
            "It is impossible.\x02\x03",
            "#00201FAs long as it is released\x01",
            "The boss will give detailed information on the tower upper layer\x01",
            "I think you will grab it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00108FFloor where Ka'aa is in\x01",
            "It seems that we also know the trends of the bells ……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3BEA")

    ChrTalk(
        0x10A,
        (
            "#12P#00603FIt is necessary to hold down somehow.\x01",
            "Seems like it …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C7B")

    label("loc_3BEA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C33")

    ChrTalk(
        0x109,
        (
            "#12P#10103FIt is necessary to hold down somehow.\x01",
            "There is …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C7B")

    label("loc_3C33")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C7B")

    ChrTalk(
        0x106,
        (
            "#12P#10703FIt is necessary to hold down somehow.\x01",
            "It looks like it is …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C7B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3CB9")

    ChrTalk(
        0x105,
        "#12P#10401FCertainly was it 30F?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D2E")

    label("loc_3CB9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3CF5")

    ChrTalk(
        0x106,
        "#12P#10701FCertainly it was 30F, was not it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D2E")

    label("loc_3CF5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D2E")

    ChrTalk(
        0x109,
        "#12P#10101FCertainly it was 30F, was not it?\x02",
    )

    CloseMessageWindow()

    label("loc_3D2E")


    ChrTalk(
        0x103,
        (
            "#00203F#5PYes, that is,\x01",
            "He may be in the top layer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00300FIf so then this way\x01",
            "It is a translation if only I can aim for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#11POh … let's put in a spirit!\x02",
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

    # Function_9_395B end

    def Function_10_3E1F(): pass

    label("Function_10_3E1F")

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

    def lambda_3F63():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3F63)
    Sleep(50)

    def lambda_3F73():
        TurnDirection(0xF4, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_3F73)
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
    SetChrName("Voice of Franc")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Oh, good\x01",
            "It was safe!\x02\x03",
            "Here \"Mercapa k#2RMale#It is \"No.\"!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_40AE")
    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x109,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#10102FFran … …!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_40D9")

    label("loc_40AE")

    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x102,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00102FFran-san …!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_40D9")

    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("Abbas' voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It seems the rushed into the tower\x01",
            "What is the situation?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_419B")
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00003FOh, it's too late.\x02",
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
            "#10400FI will lightly explain the situation.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_41DD")

    label("loc_419B")

    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00001FOh, it's too late.\x01",
            "I will explain the situation.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_41DD")

    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "To the bridge of Mercapa\x01",
            "I told the current situation.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("Abbas' voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I see……\x01",
            "It certainly seems to be a stuff.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of Jonah")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Although it is a white doll on the rooftop\x01",
            "Apparently to the surrounding 100 age\x01",
            "It seems that \"barrier\" is developing.\x02\x03",
            "I will not bring it from here.\x01",
            "Do not expect support or something?\x02",
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
            "#00013FI see … OK.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4390")
    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x105,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#10406FWell, somehow here\x01",
            "There seems to be no choice but to do.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_43CE")

    label("loc_4390")

    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x104,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00306FWell, here.\x01",
            "I have no choice but to do something.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_43CE")

    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of Franc")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "By the way it is two other machines … …\x01",
            "Apparently I seemed to be silent.\x02\x03",
            "Kevin Father and Esther\x01",
            "He might have worked hard.\x02",
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
            "#00005FIs it so……\x02",
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
            "#00204F…… Good news.\x02",
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
            "#00300FAh……\x01",
            "I can win well.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of Grace")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "── Anyway!\x01",
            "Do not be unreasonable!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("Voice of McDowell")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "goddess#4REidos#Protection of … …\x01",
            "Be wary of it.\x02",
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
            "#00100FYes……!\x02",
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
            "#00000FOK……!\x02",
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

    # Function_10_3E1F end

    def Function_11_466F(): pass

    label("Function_11_466F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_46A7")
    OP_82(0x0, 0x5, 0xBB8, 0x1F4)
    Sleep(2000)
    OP_82(0x0, 0xA, 0x3E8, 0x1F4)
    Sleep(1000)
    Jump("Function_11_466F")

    label("loc_46A7")

    Return()

    # Function_11_466F end

    SaveToFile()

Try(main)
