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

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A4D")
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
        (1, "loc_A6B"),
        (2, "loc_E7A"),
        (3, "loc_1234"),
        (4, "loc_159B"),
        (SWITCH_DEFAULT, "loc_1A2F"),
    )


    label("loc_53F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A63")

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
            "Cancel\x01",                     # 12
        )
    )

    Call(0, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_66D")
    Call(0, 2)
    SetScenarioFlags(0x0, 0)

    label("loc_66D")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_6BF"),
        (1, "loc_70B"),
        (2, "loc_757"),
        (3, "loc_7A3"),
        (4, "loc_7EF"),
        (5, "loc_83B"),
        (6, "loc_887"),
        (7, "loc_8D3"),
        (8, "loc_91F"),
        (9, "loc_96B"),
        (10, "loc_9B7"),
        (11, "loc_A03"),
        (SWITCH_DEFAULT, "loc_A4F"),
    )


    label("loc_6BF")

    SetScenarioFlags(0x5C, 0)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000000, 0x0, 0x0, 0x0, 0x30087200, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 0)
    Call(0, 3)
    Jump("loc_A5E")

    label("loc_70B")

    SetScenarioFlags(0x5C, 1)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000000, 0x0, 0x0, 0x0, 0x30087200, 0x30087200, 0x30087200, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 1)
    Call(0, 3)
    Jump("loc_A5E")

    label("loc_757")

    SetScenarioFlags(0x5C, 2)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000000, 0x0, 0x0, 0x0, 0x30087200, 0x30087200, 0x30087200, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 2)
    Call(0, 3)
    Jump("loc_A5E")

    label("loc_7A3")

    SetScenarioFlags(0x5C, 3)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000100, 0x30000000, 0x30000200, 0x30000300, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 3)
    Call(0, 3)
    Jump("loc_A5E")

    label("loc_7EF")

    SetScenarioFlags(0x5C, 4)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000100, 0x0, 0x0, 0x0, 0x30087500, 0x30087500, 0x30087500, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 4)
    Call(0, 3)
    Jump("loc_A5E")

    label("loc_83B")

    SetScenarioFlags(0x5C, 5)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000100, 0x0, 0x0, 0x0, 0x30087500, 0x30087500, 0x30087500, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 5)
    Call(0, 3)
    Jump("loc_A5E")

    label("loc_887")

    SetScenarioFlags(0x5C, 6)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000200, 0x0, 0x0, 0x0, 0x30087100, 0x30087100, 0x30087100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 6)
    Call(0, 3)
    Jump("loc_A5E")

    label("loc_8D3")

    SetScenarioFlags(0x5C, 7)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000200, 0x30000000, 0x30000100, 0x30000300, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 7)
    Call(0, 3)
    Jump("loc_A5E")

    label("loc_91F")

    SetScenarioFlags(0x5D, 0)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000200, 0x0, 0x0, 0x0, 0x30087100, 0x30087100, 0x30087100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 0)
    Call(0, 3)
    Jump("loc_A5E")

    label("loc_96B")

    SetScenarioFlags(0x5D, 1)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000300, 0x0, 0x0, 0x0, 0x30087000, 0x30087000, 0x30087000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 1)
    Call(0, 3)
    Jump("loc_A5E")

    label("loc_9B7")

    SetScenarioFlags(0x5D, 2)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000300, 0x0, 0x0, 0x0, 0x30087000, 0x30087000, 0x30087000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 2)
    Call(0, 3)
    Jump("loc_A5E")

    label("loc_A03")

    SetScenarioFlags(0x5D, 3)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000300, 0x0, 0x0, 0x0, 0x30087000, 0x30087000, 0x30087000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 3)
    Call(0, 3)
    Jump("loc_A5E")

    label("loc_A4F")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A5E")

    label("loc_A5E")

    Jump("loc_53F")

    label("loc_A63")

    ClearScenarioFlags(0x0, 0)
    Jump("loc_1A48")

    label("loc_A6B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E72")

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
            "Cancel\x01",                            # 9
        )
    )

    Call(0, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B72")
    Call(0, 2)
    SetScenarioFlags(0x0, 0)

    label("loc_B72")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_BB2"),
        (1, "loc_BFE"),
        (2, "loc_C4A"),
        (3, "loc_C96"),
        (4, "loc_CE2"),
        (5, "loc_D2E"),
        (6, "loc_D7A"),
        (7, "loc_DC6"),
        (8, "loc_E12"),
        (SWITCH_DEFAULT, "loc_E5E"),
    )


    label("loc_BB2")

    SetScenarioFlags(0x5D, 4)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000400, 0x0, 0x0, 0x0, 0x30087400, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 4)
    Call(0, 3)
    Jump("loc_E6D")

    label("loc_BFE")

    SetScenarioFlags(0x5D, 5)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30003100, 0x0, 0x0, 0x0, 0x30087400, 0x30087400, 0x30087400, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 5)
    Call(0, 3)
    Jump("loc_E6D")

    label("loc_C4A")

    SetScenarioFlags(0x5D, 6)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000800, 0x0, 0x0, 0x0, 0x30087300, 0x30087300, 0x30087300, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 6)
    Call(0, 3)
    Jump("loc_E6D")

    label("loc_C96")

    SetScenarioFlags(0x5D, 7)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000800, 0x0, 0x0, 0x0, 0x30087300, 0x30087300, 0x30087300, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 7)
    Call(0, 3)
    Jump("loc_E6D")

    label("loc_CE2")

    SetScenarioFlags(0x5E, 0)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000500, 0x0, 0x0, 0x0, 0x30087500, 0x30087500, 0x30087500, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5E, 0)
    Call(0, 3)
    Jump("loc_E6D")

    label("loc_D2E")

    SetScenarioFlags(0x5E, 1)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30003200, 0x0, 0x0, 0x0, 0x30087500, 0x30087500, 0x30087500, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5E, 1)
    Call(0, 3)
    Jump("loc_E6D")

    label("loc_D7A")

    SetScenarioFlags(0x5E, 2)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000900, 0x0, 0x0, 0x0, 0x30087000, 0x30087000, 0x30087000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5E, 2)
    Call(0, 3)
    Jump("loc_E6D")

    label("loc_DC6")

    SetScenarioFlags(0x5E, 3)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000900, 0x0, 0x0, 0x0, 0x30087000, 0x30087000, 0x30087000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5E, 3)
    Call(0, 3)
    Jump("loc_E6D")

    label("loc_E12")

    SetScenarioFlags(0x5E, 4)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30004100, 0x0, 0x0, 0x0, 0x30087400, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5E, 4)
    Call(0, 3)
    Jump("loc_E6D")

    label("loc_E5E")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E6D")

    label("loc_E6D")

    Jump("loc_A6B")

    label("loc_E72")

    ClearScenarioFlags(0x0, 0)
    Jump("loc_1A48")

    label("loc_E7A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_122C")

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
            "Cancel\x01",                                  # 8
        )
    )

    Call(0, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F84")
    Call(0, 2)
    SetScenarioFlags(0x0, 0)

    label("loc_F84")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_FBE"),
        (1, "loc_100A"),
        (2, "loc_1056"),
        (3, "loc_10A2"),
        (4, "loc_10EE"),
        (5, "loc_113A"),
        (6, "loc_1186"),
        (7, "loc_11D2"),
        (SWITCH_DEFAULT, "loc_1218"),
    )


    label("loc_FBE")

    SetScenarioFlags(0x5C, 0)
    Battle(0xFFFFFFFF, 0x30200101, "", 0x30002400, 0x0, 0x0, 0x0, 0x30087400, 0x30087400, 0x30087400, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 0)
    Call(0, 3)
    Jump("loc_1227")

    label("loc_100A")

    SetScenarioFlags(0x5C, 1)
    Battle(0xFFFFFFFF, 0x30200101, "", 0x30002400, 0x0, 0x0, 0x0, 0x30087400, 0x30087400, 0x30087400, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 1)
    Call(0, 3)
    Jump("loc_1227")

    label("loc_1056")

    SetScenarioFlags(0x5C, 2)
    Battle(0xFFFFFFFF, 0x30200101, "", 0x30003400, 0x0, 0x0, 0x0, 0x30087100, 0x30087100, 0x30087100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 2)
    Call(0, 3)
    Jump("loc_1227")

    label("loc_10A2")

    SetScenarioFlags(0x5C, 3)
    Battle(0xFFFFFFFF, 0x30200101, "", 0x30003300, 0x0, 0x0, 0x0, 0x30087000, 0x30087000, 0x30087000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 3)
    Call(0, 3)
    Jump("loc_1227")

    label("loc_10EE")

    SetScenarioFlags(0x5C, 4)
    Battle(0xFFFFFFFF, 0x30200101, "", 0x30003600, 0x0, 0x0, 0x0, 0x30087100, 0x30087100, 0x30087100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 4)
    Call(0, 3)
    Jump("loc_1227")

    label("loc_113A")

    SetScenarioFlags(0x5C, 5)
    Battle(0xFFFFFFFF, 0x30200101, "", 0x30004200, 0x0, 0x0, 0x0, 0x30087200, 0x30087200, 0x30087200, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 5)
    Call(0, 3)
    Jump("loc_1227")

    label("loc_1186")

    SetScenarioFlags(0x5C, 6)
    Battle(0xFFFFFFFF, 0x30200101, "", 0x30003700, 0x0, 0x0, 0x0, 0x30087300, 0x30087300, 0x30087300, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 6)
    Call(0, 3)
    Jump("loc_1227")

    label("loc_11D2")

    Battle(0xFFFFFFFF, 0x30200101, "", 0x30003700, 0x0, 0x0, 0x0, 0x30087300, 0x30087300, 0x30087300, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    Call(0, 3)
    Jump("loc_1227")

    label("loc_1218")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1227")

    label("loc_1227")

    Jump("loc_E7A")

    label("loc_122C")

    ClearScenarioFlags(0x0, 0)
    Jump("loc_1A48")

    label("loc_1234")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1593")

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
            "Cancel\x01",                                # 7
        )
    )

    Call(0, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_132E")
    Call(0, 2)
    SetScenarioFlags(0x0, 0)

    label("loc_132E")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1362"),
        (1, "loc_13AE"),
        (2, "loc_13FA"),
        (3, "loc_1446"),
        (4, "loc_1492"),
        (5, "loc_14DE"),
        (6, "loc_1538"),
        (SWITCH_DEFAULT, "loc_1584"),
    )


    label("loc_1362")

    SetScenarioFlags(0x5C, 0)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000000, 0x30000100, 0x0, 0x0, 0x30087500, 0x30087500, 0x30087500, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 0)
    Call(0, 3)
    Jump("loc_158E")

    label("loc_13AE")

    SetScenarioFlags(0x5C, 1)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000000, 0x30000200, 0x0, 0x0, 0x30087100, 0x30087100, 0x30087100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 1)
    Call(0, 3)
    Jump("loc_158E")

    label("loc_13FA")

    SetScenarioFlags(0x5C, 2)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000000, 0x30000300, 0x0, 0x0, 0x30087000, 0x30087000, 0x30087000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 2)
    Call(0, 3)
    Jump("loc_158E")

    label("loc_1446")

    SetScenarioFlags(0x5C, 3)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000000, 0x30000800, 0x0, 0x0, 0x30087300, 0x30087300, 0x30087300, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 3)
    Call(0, 3)
    Jump("loc_158E")

    label("loc_1492")

    SetScenarioFlags(0x5C, 4)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000000, 0x30000400, 0x0, 0x0, 0x30087400, 0x30087400, 0x30087400, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 4)
    Call(0, 3)
    Jump("loc_158E")

    label("loc_14DE")

    SetScenarioFlags(0x5C, 5)
    SetChrChipPat(0x5, 0x1, 0x20)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000000, 0x30003200, 0x0, 0x0, 0x30087200, 0x30087200, 0x30087200, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    SetChrChipPat(0x5, 0x1, 0x5)
    ClearScenarioFlags(0x5C, 5)
    Call(0, 3)
    Jump("loc_158E")

    label("loc_1538")

    SetScenarioFlags(0x5C, 6)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000000, 0x30000900, 0x0, 0x0, 0x30087000, 0x30087000, 0x30087000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 6)
    Call(0, 3)
    Jump("loc_158E")

    label("loc_1584")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_158E")

    Jump("loc_1234")

    label("loc_1593")

    ClearScenarioFlags(0x0, 0)
    Jump("loc_1A48")

    label("loc_159B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A27")

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
            "Cancel\x01",                           # 10
        )
    )

    Call(0, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16DA")
    Call(0, 2)
    SetScenarioFlags(0x0, 0)

    label("loc_16DA")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1720"),
        (1, "loc_176C"),
        (2, "loc_17B8"),
        (3, "loc_1804"),
        (4, "loc_1850"),
        (5, "loc_189C"),
        (6, "loc_18E8"),
        (7, "loc_1934"),
        (8, "loc_1980"),
        (9, "loc_19CC"),
        (SWITCH_DEFAULT, "loc_1A18"),
    )


    label("loc_1720")

    SetScenarioFlags(0x5C, 7)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000100, 0x30000200, 0x0, 0x0, 0x30087100, 0x30087100, 0x30087100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 7)
    Call(0, 3)
    Jump("loc_1A22")

    label("loc_176C")

    SetScenarioFlags(0x5D, 0)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000100, 0x30000300, 0x0, 0x0, 0x30087500, 0x30087500, 0x30087500, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 0)
    Call(0, 3)
    Jump("loc_1A22")

    label("loc_17B8")

    SetScenarioFlags(0x5D, 1)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000100, 0x30000800, 0x0, 0x0, 0x30087300, 0x30087300, 0x30087300, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 1)
    Call(0, 3)
    Jump("loc_1A22")

    label("loc_1804")

    SetScenarioFlags(0x5D, 2)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000100, 0x30000400, 0x0, 0x0, 0x30087400, 0x30087400, 0x30087400, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 2)
    Call(0, 3)
    Jump("loc_1A22")

    label("loc_1850")

    SetScenarioFlags(0x5D, 3)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000200, 0x30000300, 0x0, 0x0, 0x30087000, 0x30087000, 0x30087000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 3)
    Call(0, 3)
    Jump("loc_1A22")

    label("loc_189C")

    SetScenarioFlags(0x5D, 4)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000200, 0x30000800, 0x0, 0x0, 0x30087100, 0x30087100, 0x30087100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 4)
    Call(0, 3)
    Jump("loc_1A22")

    label("loc_18E8")

    SetScenarioFlags(0x5D, 5)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000200, 0x30000400, 0x0, 0x0, 0x30087200, 0x30087200, 0x30087200, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 5)
    Call(0, 3)
    Jump("loc_1A22")

    label("loc_1934")

    SetScenarioFlags(0x5D, 6)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000300, 0x30000800, 0x0, 0x0, 0x30087300, 0x30087300, 0x30087300, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 6)
    Call(0, 3)
    Jump("loc_1A22")

    label("loc_1980")

    SetScenarioFlags(0x5D, 7)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000300, 0x30000400, 0x0, 0x0, 0x30087400, 0x30087400, 0x30087400, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 7)
    Call(0, 3)
    Jump("loc_1A22")

    label("loc_19CC")

    SetScenarioFlags(0x5E, 0)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000400, 0x30000800, 0x0, 0x0, 0x30087000, 0x30087000, 0x30087000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5E, 0)
    Call(0, 3)
    Jump("loc_1A22")

    label("loc_1A18")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1A22")

    Jump("loc_159B")

    label("loc_1A27")

    ClearScenarioFlags(0x0, 0)
    Jump("loc_1A48")

    label("loc_1A2F")

    FadeToBright(300, 0)
    OP_0D()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A48")

    label("loc_1A48")

    Jump("loc_4A1")

    label("loc_1A4D")

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
