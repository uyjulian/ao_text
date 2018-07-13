from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "b0101.bin",                # FileName
        "b0101",                    # MapName
        "b0101",                    # Location
        0x0000,                     # MapIndex
        "ed7450",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0xFF,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "b0101",                  # 0
    ))

    ChipFrameInfo(420, 0)                                        # 0

    ScpFunction((
        "Function_0_1A4",          # 00, 0
        "Function_1_1A8",          # 01, 1
        "Function_2_20E",          # 02, 2
        "Function_3_237",          # 03, 3
        "Function_4_264",          # 04, 4
        "Function_5_2DB",          # 05, 5
        "Function_6_340",          # 06, 6
        "Function_7_445",          # 07, 7
    ))


    def Function_0_1A4(): pass

    label("Function_0_1A4")

    Event(0, 7)
    Return()

    # Function_0_1A4 end

    def Function_1_1A8(): pass

    label("Function_1_1A8")

    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis120.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFF000000, 0x1, "c_vis120.itp")
    OP_C9(0x0, 0x10)
    SetMapFlags(0x80)
    OP_16(0x0)
    Return()

    # Function_1_1A8 end

    def Function_2_20E(): pass

    label("Function_2_20E")

    OP_60(0x2)
    OP_60(0x1)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    Sleep(500)
    OP_0D()
    Return()

    # Function_2_20E end

    def Function_3_237(): pass

    label("Function_3_237")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0xC8, 0x0, 0x0)
    Call(0, 4)
    Call(0, 5)
    OP_CB(0x1, 0x3, 0x0, 0x1F4, 0x0, 0x0)
    Return()

    # Function_3_237 end

    def Function_4_264(): pass

    label("Function_4_264")

    SetChrName("")
    SetMessageWindowPos(120, 0, 28, 1)

    AnonymousTalk(
        0xFF,
        (
            "　　　Craft Viewer",
            scpstr(0x18),
            scpstr(0x6),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        1,
        32,
        96,
        1,
        (
            "S Craft①\x01",          # 0
            "S Craft②\x01",          # 1
            "S Craft③\x01",          # 2
            "Combi Craft①\x01",      # 3
            "Combi Craft②\x01",      # 4
            "Back\x01",               # 5
        )
    )

    MenuCmd(4, 1, 0x3)
    Sleep(200)
    MenuCmd(6, 1)
    Return()

    # Function_4_264 end

    def Function_5_2DB(): pass

    label("Function_5_2DB")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_309"),
        (1, "loc_312"),
        (2, "loc_31B"),
        (3, "loc_324"),
        (4, "loc_32D"),
        (5, "loc_336"),
        (SWITCH_DEFAULT, "loc_33F"),
    )


    label("loc_309")

    MenuCmd(5, 1, 0x0)
    Jump("loc_33F")

    label("loc_312")

    MenuCmd(5, 1, 0x1)
    Jump("loc_33F")

    label("loc_31B")

    MenuCmd(5, 1, 0x2)
    Jump("loc_33F")

    label("loc_324")

    MenuCmd(5, 1, 0x3)
    Jump("loc_33F")

    label("loc_32D")

    MenuCmd(5, 1, 0x4)
    Jump("loc_33F")

    label("loc_336")

    MenuCmd(5, 1, 0x5)
    Jump("loc_33F")

    label("loc_33F")

    Return()

    # Function_5_2DB end

    def Function_6_340(): pass

    label("Function_6_340")

    MenuCmd(4, 2, 0x3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_3AE"),
        (1, "loc_3B7"),
        (2, "loc_3C0"),
        (3, "loc_3C9"),
        (4, "loc_3D2"),
        (5, "loc_3DB"),
        (6, "loc_3E4"),
        (7, "loc_3ED"),
        (8, "loc_3F6"),
        (9, "loc_3FF"),
        (10, "loc_408"),
        (11, "loc_411"),
        (12, "loc_41A"),
        (13, "loc_423"),
        (14, "loc_42C"),
        (15, "loc_435"),
        (SWITCH_DEFAULT, "loc_43E"),
    )


    label("loc_3AE")

    MenuCmd(5, 2, 0x0)
    Jump("loc_43E")

    label("loc_3B7")

    MenuCmd(5, 2, 0x1)
    Jump("loc_43E")

    label("loc_3C0")

    MenuCmd(5, 2, 0x2)
    Jump("loc_43E")

    label("loc_3C9")

    MenuCmd(5, 2, 0x3)
    Jump("loc_43E")

    label("loc_3D2")

    MenuCmd(5, 2, 0x4)
    Jump("loc_43E")

    label("loc_3DB")

    MenuCmd(5, 2, 0x5)
    Jump("loc_43E")

    label("loc_3E4")

    MenuCmd(5, 2, 0x6)
    Jump("loc_43E")

    label("loc_3ED")

    MenuCmd(5, 2, 0x7)
    Jump("loc_43E")

    label("loc_3F6")

    MenuCmd(5, 2, 0x8)
    Jump("loc_43E")

    label("loc_3FF")

    MenuCmd(5, 2, 0x9)
    Jump("loc_43E")

    label("loc_408")

    MenuCmd(5, 2, 0xA)
    Jump("loc_43E")

    label("loc_411")

    MenuCmd(5, 2, 0xB)
    Jump("loc_43E")

    label("loc_41A")

    MenuCmd(5, 2, 0xC)
    Jump("loc_43E")

    label("loc_423")

    MenuCmd(5, 2, 0xD)
    Jump("loc_43E")

    label("loc_42C")

    MenuCmd(5, 2, 0xE)
    Jump("loc_43E")

    label("loc_435")

    MenuCmd(5, 2, 0xF)
    Jump("loc_43E")

    label("loc_43E")

    MenuEnd(0x3)
    OP_60(0x2)
    Return()

    # Function_6_340 end

    def Function_7_445(): pass

    label("Function_7_445")

    OP_CB(0x1, 0x3, 0x0, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    Sleep(500)
    PlayBGM("ed7450", 0)
    OP_C9(0x0, 0x8)
    SetMapFlags(0x2000000)
    SetChrName("")
    SetMessageWindowPos(120, 0, 28, 1)

    AnonymousTalk(
        0xFF,
        (
            "　　　Craft Viewer",
            scpstr(0x18),
            scpstr(0x6),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    label("loc_4A1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A43")
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        1,
        32,
        96,
        1,
        (
            "S Craft①\x01",          # 0
            "S Craft②\x01",          # 1
            "S Craft③\x01",          # 2
            "Combi Craft①\x01",      # 3
            "Combi Craft②\x01",      # 4
            "Back\x01",               # 5
        )
    )

    MenuCmd(4, 1, 0x3)
    Call(0, 5)
    MenuEnd(0x0)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_53F"),
        (1, "loc_A69"),
        (2, "loc_E76"),
        (3, "loc_122E"),
        (4, "loc_1593"),
        (SWITCH_DEFAULT, "loc_1A25"),
    )


    label("loc_53F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A61")

    Menu(
        2,
        -1,
        108,
        1,
        (
            "#176I: Tiger Charge\x01",        # 0
            "#176I: Rising Sun\x01",          # 1
            "#176I: Meteo Breaker\x01",       # 2
            "#177I: Aura Rain\x01",           # 3
            "#177I: Aerial Cannon\x01",       # 4
            "#177I: Divine Crusade\x01",      # 5
            "#178I: Ether Buster\x01",        # 6
            "#178I: Zero Field\x01",          # 7
            "#178I: Eidolon Gear\x01",        # 8
            "#179I: Crimson Gale\x01",        # 9
            "#179I: Death Scorpion\x01",      # 10
            "#179I: Berserker\x01",           # 11
            "Quit\x01",                       # 12
        )
    )

    Call(0, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_66B")
    Call(0, 2)
    SetScenarioFlags(0x0, 0)

    label("loc_66B")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_6BD"),
        (1, "loc_709"),
        (2, "loc_755"),
        (3, "loc_7A1"),
        (4, "loc_7ED"),
        (5, "loc_839"),
        (6, "loc_885"),
        (7, "loc_8D1"),
        (8, "loc_91D"),
        (9, "loc_969"),
        (10, "loc_9B5"),
        (11, "loc_A01"),
        (SWITCH_DEFAULT, "loc_A4D"),
    )


    label("loc_6BD")

    SetScenarioFlags(0x5C, 0)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000000, 0x0, 0x0, 0x0, 0x30087200, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 0)
    Call(0, 3)
    Jump("loc_A5C")

    label("loc_709")

    SetScenarioFlags(0x5C, 1)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000000, 0x0, 0x0, 0x0, 0x30087200, 0x30087200, 0x30087200, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 1)
    Call(0, 3)
    Jump("loc_A5C")

    label("loc_755")

    SetScenarioFlags(0x5C, 2)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000000, 0x0, 0x0, 0x0, 0x30087200, 0x30087200, 0x30087200, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 2)
    Call(0, 3)
    Jump("loc_A5C")

    label("loc_7A1")

    SetScenarioFlags(0x5C, 3)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000100, 0x30000000, 0x30000200, 0x30000300, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 3)
    Call(0, 3)
    Jump("loc_A5C")

    label("loc_7ED")

    SetScenarioFlags(0x5C, 4)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000100, 0x0, 0x0, 0x0, 0x30087500, 0x30087500, 0x30087500, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 4)
    Call(0, 3)
    Jump("loc_A5C")

    label("loc_839")

    SetScenarioFlags(0x5C, 5)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000100, 0x0, 0x0, 0x0, 0x30087500, 0x30087500, 0x30087500, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 5)
    Call(0, 3)
    Jump("loc_A5C")

    label("loc_885")

    SetScenarioFlags(0x5C, 6)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000200, 0x0, 0x0, 0x0, 0x30087100, 0x30087100, 0x30087100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 6)
    Call(0, 3)
    Jump("loc_A5C")

    label("loc_8D1")

    SetScenarioFlags(0x5C, 7)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000200, 0x30000000, 0x30000100, 0x30000300, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 7)
    Call(0, 3)
    Jump("loc_A5C")

    label("loc_91D")

    SetScenarioFlags(0x5D, 0)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000200, 0x0, 0x0, 0x0, 0x30087100, 0x30087100, 0x30087100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 0)
    Call(0, 3)
    Jump("loc_A5C")

    label("loc_969")

    SetScenarioFlags(0x5D, 1)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000300, 0x0, 0x0, 0x0, 0x30087000, 0x30087000, 0x30087000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 1)
    Call(0, 3)
    Jump("loc_A5C")

    label("loc_9B5")

    SetScenarioFlags(0x5D, 2)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000300, 0x0, 0x0, 0x0, 0x30087000, 0x30087000, 0x30087000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 2)
    Call(0, 3)
    Jump("loc_A5C")

    label("loc_A01")

    SetScenarioFlags(0x5D, 3)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000300, 0x0, 0x0, 0x0, 0x30087000, 0x30087000, 0x30087000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 3)
    Call(0, 3)
    Jump("loc_A5C")

    label("loc_A4D")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A5C")

    label("loc_A5C")

    Jump("loc_53F")

    label("loc_A61")

    ClearScenarioFlags(0x0, 0)
    Jump("loc_1A3E")

    label("loc_A69")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E6E")

    Menu(
        2,
        -1,
        108,
        1,
        (
            "#180I: Deadly Heaven\x01",              # 0
            "#180I: Akashic Arm\x01",                # 1
            "#184I: Blast Storm\x01",                # 2
            "#184I: Armed Force\x01",                # 3
            "#181I: Paraselene Dance\x01",           # 4
            "#187I: True Paraselene Dance\x01",      # 5
            "#185I: Justice Hammer\x01",             # 6
            "#185I: Justice Magnum\x01",             # 7
            "#186I: Killing Driver\x01",             # 8
            "Quit\x01",                              # 9
        )
    )

    Call(0, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B6E")
    Call(0, 2)
    SetScenarioFlags(0x0, 0)

    label("loc_B6E")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_BAE"),
        (1, "loc_BFA"),
        (2, "loc_C46"),
        (3, "loc_C92"),
        (4, "loc_CDE"),
        (5, "loc_D2A"),
        (6, "loc_D76"),
        (7, "loc_DC2"),
        (8, "loc_E0E"),
        (SWITCH_DEFAULT, "loc_E5A"),
    )


    label("loc_BAE")

    SetScenarioFlags(0x5D, 4)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000400, 0x0, 0x0, 0x0, 0x30087400, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 4)
    Call(0, 3)
    Jump("loc_E69")

    label("loc_BFA")

    SetScenarioFlags(0x5D, 5)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30003100, 0x0, 0x0, 0x0, 0x30087400, 0x30087400, 0x30087400, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 5)
    Call(0, 3)
    Jump("loc_E69")

    label("loc_C46")

    SetScenarioFlags(0x5D, 6)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000800, 0x0, 0x0, 0x0, 0x30087300, 0x30087300, 0x30087300, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 6)
    Call(0, 3)
    Jump("loc_E69")

    label("loc_C92")

    SetScenarioFlags(0x5D, 7)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000800, 0x0, 0x0, 0x0, 0x30087300, 0x30087300, 0x30087300, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 7)
    Call(0, 3)
    Jump("loc_E69")

    label("loc_CDE")

    SetScenarioFlags(0x5E, 0)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000500, 0x0, 0x0, 0x0, 0x30087500, 0x30087500, 0x30087500, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5E, 0)
    Call(0, 3)
    Jump("loc_E69")

    label("loc_D2A")

    SetScenarioFlags(0x5E, 1)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30003200, 0x0, 0x0, 0x0, 0x30087500, 0x30087500, 0x30087500, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5E, 1)
    Call(0, 3)
    Jump("loc_E69")

    label("loc_D76")

    SetScenarioFlags(0x5E, 2)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000900, 0x0, 0x0, 0x0, 0x30087000, 0x30087000, 0x30087000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5E, 2)
    Call(0, 3)
    Jump("loc_E69")

    label("loc_DC2")

    SetScenarioFlags(0x5E, 3)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000900, 0x0, 0x0, 0x0, 0x30087000, 0x30087000, 0x30087000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5E, 3)
    Call(0, 3)
    Jump("loc_E69")

    label("loc_E0E")

    SetScenarioFlags(0x5E, 4)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30004100, 0x0, 0x0, 0x0, 0x30087400, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5E, 4)
    Call(0, 3)
    Jump("loc_E69")

    label("loc_E5A")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E69")

    label("loc_E69")

    Jump("loc_A69")

    label("loc_E6E")

    ClearScenarioFlags(0x0, 0)
    Jump("loc_1A3E")

    label("loc_E76")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1226")

    Menu(
        2,
        -1,
        108,
        1,
        (
            "#183I: Wind God's Wave\x01",                  # 0
            "#183I: Final Tachi -Black Emperor-\x01",      # 1
            "#190I: Death Parade\x01",                     # 2
            "#207I: Crimson Fall\x01",                     # 3
            "#189I: Fake Salt Pale\x01",                   # 4
            "#188I: Holy Craft - Grand Cross\x01",         # 5
            "#191I: Crimson Zanber\x01",                   # 6
            "#191I: Merry Merry Castle\x01",               # 7
            "Quit\x01",                                    # 8
        )
    )

    Call(0, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F7E")
    Call(0, 2)
    SetScenarioFlags(0x0, 0)

    label("loc_F7E")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_FB8"),
        (1, "loc_1004"),
        (2, "loc_1050"),
        (3, "loc_109C"),
        (4, "loc_10E8"),
        (5, "loc_1134"),
        (6, "loc_1180"),
        (7, "loc_11CC"),
        (SWITCH_DEFAULT, "loc_1212"),
    )


    label("loc_FB8")

    SetScenarioFlags(0x5C, 0)
    Battle(0xFFFFFFFF, 0x30200101, "", 0x30002400, 0x0, 0x0, 0x0, 0x30087400, 0x30087400, 0x30087400, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 0)
    Call(0, 3)
    Jump("loc_1221")

    label("loc_1004")

    SetScenarioFlags(0x5C, 1)
    Battle(0xFFFFFFFF, 0x30200101, "", 0x30002400, 0x0, 0x0, 0x0, 0x30087400, 0x30087400, 0x30087400, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 1)
    Call(0, 3)
    Jump("loc_1221")

    label("loc_1050")

    SetScenarioFlags(0x5C, 2)
    Battle(0xFFFFFFFF, 0x30200101, "", 0x30003400, 0x0, 0x0, 0x0, 0x30087100, 0x30087100, 0x30087100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 2)
    Call(0, 3)
    Jump("loc_1221")

    label("loc_109C")

    SetScenarioFlags(0x5C, 3)
    Battle(0xFFFFFFFF, 0x30200101, "", 0x30003300, 0x0, 0x0, 0x0, 0x30087000, 0x30087000, 0x30087000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 3)
    Call(0, 3)
    Jump("loc_1221")

    label("loc_10E8")

    SetScenarioFlags(0x5C, 4)
    Battle(0xFFFFFFFF, 0x30200101, "", 0x30003600, 0x0, 0x0, 0x0, 0x30087100, 0x30087100, 0x30087100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 4)
    Call(0, 3)
    Jump("loc_1221")

    label("loc_1134")

    SetScenarioFlags(0x5C, 5)
    Battle(0xFFFFFFFF, 0x30200101, "", 0x30004200, 0x0, 0x0, 0x0, 0x30087200, 0x30087200, 0x30087200, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 5)
    Call(0, 3)
    Jump("loc_1221")

    label("loc_1180")

    SetScenarioFlags(0x5C, 6)
    Battle(0xFFFFFFFF, 0x30200101, "", 0x30003700, 0x0, 0x0, 0x0, 0x30087300, 0x30087300, 0x30087300, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 6)
    Call(0, 3)
    Jump("loc_1221")

    label("loc_11CC")

    Battle(0xFFFFFFFF, 0x30200101, "", 0x30003700, 0x0, 0x0, 0x0, 0x30087300, 0x30087300, 0x30087300, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    Call(0, 3)
    Jump("loc_1221")

    label("loc_1212")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1221")

    label("loc_1221")

    Jump("loc_E76")

    label("loc_1226")

    ClearScenarioFlags(0x0, 0)
    Jump("loc_1A3E")

    label("loc_122E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_158B")

    Menu(
        2,
        -1,
        108,
        1,
        (
            "#176I#177I: Star Blast\x01",                # 0
            "#176I#178I: Omega Strike\x01",              # 1
            "#176I#179I: Burning Rage\x01",              # 2
            "#176I#184I: Brave Hearts\x01",              # 3
            "#176I#180I: Strike Heaven\x01",             # 4
            "#176I#187I: Double Dragon Strike\x01",      # 5
            "#176I#185I: Hearts of Iron\x01",            # 6
            "Quit\x01",                                  # 7
        )
    )

    Call(0, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1326")
    Call(0, 2)
    SetScenarioFlags(0x0, 0)

    label("loc_1326")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_135A"),
        (1, "loc_13A6"),
        (2, "loc_13F2"),
        (3, "loc_143E"),
        (4, "loc_148A"),
        (5, "loc_14D6"),
        (6, "loc_1530"),
        (SWITCH_DEFAULT, "loc_157C"),
    )


    label("loc_135A")

    SetScenarioFlags(0x5C, 0)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000000, 0x30000100, 0x0, 0x0, 0x30087500, 0x30087500, 0x30087500, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 0)
    Call(0, 3)
    Jump("loc_1586")

    label("loc_13A6")

    SetScenarioFlags(0x5C, 1)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000000, 0x30000200, 0x0, 0x0, 0x30087100, 0x30087100, 0x30087100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 1)
    Call(0, 3)
    Jump("loc_1586")

    label("loc_13F2")

    SetScenarioFlags(0x5C, 2)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000000, 0x30000300, 0x0, 0x0, 0x30087000, 0x30087000, 0x30087000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 2)
    Call(0, 3)
    Jump("loc_1586")

    label("loc_143E")

    SetScenarioFlags(0x5C, 3)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000000, 0x30000800, 0x0, 0x0, 0x30087300, 0x30087300, 0x30087300, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 3)
    Call(0, 3)
    Jump("loc_1586")

    label("loc_148A")

    SetScenarioFlags(0x5C, 4)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000000, 0x30000400, 0x0, 0x0, 0x30087400, 0x30087400, 0x30087400, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 4)
    Call(0, 3)
    Jump("loc_1586")

    label("loc_14D6")

    SetScenarioFlags(0x5C, 5)
    SetChrChipPat(0x5, 0x1, 0x20)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000000, 0x30003200, 0x0, 0x0, 0x30087200, 0x30087200, 0x30087200, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    SetChrChipPat(0x5, 0x1, 0x5)
    ClearScenarioFlags(0x5C, 5)
    Call(0, 3)
    Jump("loc_1586")

    label("loc_1530")

    SetScenarioFlags(0x5C, 6)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000000, 0x30000900, 0x0, 0x0, 0x30087000, 0x30087000, 0x30087000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 6)
    Call(0, 3)
    Jump("loc_1586")

    label("loc_157C")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1586")

    Jump("loc_122E")

    label("loc_158B")

    ClearScenarioFlags(0x0, 0)
    Jump("loc_1A3E")

    label("loc_1593")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A1D")

    Menu(
        2,
        -1,
        108,
        1,
        (
            "#177I#178I: Cold Gehenna\x01",         # 0
            "#177I#179I: Riot Star\x01",            # 1
            "#177I#184I: Southern Cross\x01",       # 2
            "#177I#180I: Akashic Star\x01",         # 3
            "#178I#179I: Haken Storm\x01",          # 4
            "#178I#184I: Blast Hammer\x01",         # 5
            "#178I#180I: Sigma Ascension\x01",      # 6
            "#179I#184I: Howling Raid\x01",         # 7
            "#179I#180I: Last Rebellion\x01",       # 8
            "#180I#184I: Blue Breaker\x01",         # 9
            "Quit\x01",                             # 10
        )
    )

    Call(0, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16D0")
    Call(0, 2)
    SetScenarioFlags(0x0, 0)

    label("loc_16D0")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1716"),
        (1, "loc_1762"),
        (2, "loc_17AE"),
        (3, "loc_17FA"),
        (4, "loc_1846"),
        (5, "loc_1892"),
        (6, "loc_18DE"),
        (7, "loc_192A"),
        (8, "loc_1976"),
        (9, "loc_19C2"),
        (SWITCH_DEFAULT, "loc_1A0E"),
    )


    label("loc_1716")

    SetScenarioFlags(0x5C, 7)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000100, 0x30000200, 0x0, 0x0, 0x30087100, 0x30087100, 0x30087100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 7)
    Call(0, 3)
    Jump("loc_1A18")

    label("loc_1762")

    SetScenarioFlags(0x5D, 0)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000100, 0x30000300, 0x0, 0x0, 0x30087500, 0x30087500, 0x30087500, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 0)
    Call(0, 3)
    Jump("loc_1A18")

    label("loc_17AE")

    SetScenarioFlags(0x5D, 1)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000100, 0x30000800, 0x0, 0x0, 0x30087300, 0x30087300, 0x30087300, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 1)
    Call(0, 3)
    Jump("loc_1A18")

    label("loc_17FA")

    SetScenarioFlags(0x5D, 2)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000100, 0x30000400, 0x0, 0x0, 0x30087400, 0x30087400, 0x30087400, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 2)
    Call(0, 3)
    Jump("loc_1A18")

    label("loc_1846")

    SetScenarioFlags(0x5D, 3)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000200, 0x30000300, 0x0, 0x0, 0x30087000, 0x30087000, 0x30087000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 3)
    Call(0, 3)
    Jump("loc_1A18")

    label("loc_1892")

    SetScenarioFlags(0x5D, 4)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000200, 0x30000800, 0x0, 0x0, 0x30087100, 0x30087100, 0x30087100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 4)
    Call(0, 3)
    Jump("loc_1A18")

    label("loc_18DE")

    SetScenarioFlags(0x5D, 5)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000200, 0x30000400, 0x0, 0x0, 0x30087200, 0x30087200, 0x30087200, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 5)
    Call(0, 3)
    Jump("loc_1A18")

    label("loc_192A")

    SetScenarioFlags(0x5D, 6)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000300, 0x30000800, 0x0, 0x0, 0x30087300, 0x30087300, 0x30087300, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 6)
    Call(0, 3)
    Jump("loc_1A18")

    label("loc_1976")

    SetScenarioFlags(0x5D, 7)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000300, 0x30000400, 0x0, 0x0, 0x30087400, 0x30087400, 0x30087400, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 7)
    Call(0, 3)
    Jump("loc_1A18")

    label("loc_19C2")

    SetScenarioFlags(0x5E, 0)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000400, 0x30000800, 0x0, 0x0, 0x30087000, 0x30087000, 0x30087000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5E, 0)
    Call(0, 3)
    Jump("loc_1A18")

    label("loc_1A0E")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1A18")

    Jump("loc_1593")

    label("loc_1A1D")

    ClearScenarioFlags(0x0, 0)
    Jump("loc_1A3E")

    label("loc_1A25")

    FadeToBright(300, 0)
    OP_0D()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A3E")

    label("loc_1A3E")

    Jump("loc_4A1")

    label("loc_1A43")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    OP_57(0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    StopBGM(0x3E8)
    Sleep(500)
    OP_C9(0x1, 0x8)
    ClearMapFlags(0x2000000)
    OP_B9(0x2)
    Return()

    # Function_7_445 end

    SaveToFile()

Try(main)
