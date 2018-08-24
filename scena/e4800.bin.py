from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e4800.bin",                # FileName
        "e4800",                    # MapName
        "e4800",                    # Location
        0x00A0,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0xFF,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 160, 0, 0, 0, 1],
    )

    BuildStringList((
        "e4800",                  # 0
        "Detective Raymond",      # 1
        "Fake Brand Trader",      # 2
        "Republican Terrorist",   # 3
        "Republican Terrorist",   # 4
        "Republican Terrorist",   # 5
        "SE制御",                 # 6
        "be4800",                 # 7
        "be4800",                 # 8
    ))

    ATBonus("ATBonus_1CC", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_28C", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_290", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_294", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_298", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_29C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_1EC", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_1F0", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_1F4", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_1F8", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_1FC", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_200", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_204", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_208", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_2AC", 8, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B0", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B4", 5, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B8", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2BC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C8", 0, 0, 180)

    # monster count: 0

    # event battle count: 2

    BattleInfo(
        "BattleInfo_2CC", 0x00CA, 255, 6, 45, 3, 3, 30, 0, "be4800", 0x00000000, 100, 0, 0, 0,
        (
            ("ms42500.dat", "ms42500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_28C", "MonsterBattlePostion_1EC", "ed7507", "ed7453", "ATBonus_1CC"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_310", 0x00CA, 255, 6, 45, 3, 3, 30, 0, "be4800", 0x00000000, 100, 0, 0, 0,
        (
            ("ms24100.dat", "ms42500.dat", "ms42500.dat", "ms42500.dat", 0, 0, 0, 0, "MonsterBattlePostion_2AC", "MonsterBattlePostion_1EC", "ed7507", "ed7453", "ATBonus_1CC"),
            (),
            (),
            (),
        )
    )

    DeclNpc(0,       0,       0,       0,    449,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 14,  -26.5,                 0.15000000596046448,   -2.0,                  1406.25,               [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.06666667014360428,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.06666667014360428,   0.0,                   5.300000190734863,     -0.010000000707805157, 0.13333334028720856,   1.0])

    ChipFrameInfo(924, 0)                                        # 0

    ScpFunction((
        "Function_0_39C",          # 00, 0
        "Function_1_3D7",          # 01, 1
        "Function_2_447",          # 02, 2
        "Function_3_640",          # 03, 3
        "Function_4_695",          # 04, 4
        "Function_5_CA3",          # 05, 5
        "Function_6_CE7",          # 06, 6
        "Function_7_1C11",         # 07, 7
        "Function_8_1C48",         # 08, 8
        "Function_9_1C7F",         # 09, 9
        "Function_10_1CB6",        # 0A, 10
        "Function_11_1CEE",        # 0B, 11
        "Function_12_1D26",        # 0C, 12
        "Function_13_1D5E",        # 0D, 13
        "Function_14_1D96",        # 0E, 14
        "Function_15_35F5",        # 0F, 15
        "Function_16_3625",        # 10, 16
        "Function_17_3655",        # 11, 17
    ))


    def Function_0_39C(): pass

    label("Function_0_39C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_3B0")
    ClearScenarioFlags(0x22, 0)
    Event(0, 4)
    Jump("loc_3D6")

    label("loc_3B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_3C4")
    ClearScenarioFlags(0x22, 1)
    Event(0, 6)
    Jump("loc_3D6")

    label("loc_3C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_3D6")
    ClearScenarioFlags(0x22, 2)
    SetScenarioFlags(0x0, 0)
    Event(0, 2)

    label("loc_3D6")

    Return()

    # Function_0_39C end

    def Function_1_3D7(): pass

    label("Function_1_3D7")

    OP_F0(0x1, 0x7D0)
    SetMapObjFrame(0xFF, "huta01b", 0x0, 0x1)
    SetMapObjFrame(0xFF, "huta02a", 0x0, 0x1)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_423")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_423")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_43A")
    OP_24(0x339)
    OP_24(0x1C3)
    ClearScenarioFlags(0x0, 0)
    Jump("loc_446")

    label("loc_43A")

    Sound(825, 1, 60, 0)
    Sound(451, 1, 80, 0)

    label("loc_446")

    Return()

    # Function_1_3D7 end

    def Function_2_447(): pass

    label("Function_2_447")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(451)
    SoundLoad(825)
    CreatePortrait(0, 128, 4, 640, 68, 0, 20, 512, 64, 0, 0, 512, 64, 0xFFFFFF, 0x0, "c_vis501.itp")
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    ClearMapObjFlags(0x0, 0x4)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_7D(0xFF, 0xDC, 0xDC, 0x0, 0x0)
    OP_11(0xFF, 0xBD, 0xAC, 0x3C, 0x320, 0x0)
    OP_68(-14000, 0, 0, 0)
    MoveCamera(100, 42, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(140000, 0)
    BeginChrThread(0xD, 1, 0, 3)
    MoveCamera(107, 42, 0, 7000)
    SetCameraDistance(90000, 7000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_25(0x339, 0x3C)
    Fade(1000)
    OP_68(-18000, 1000, 0, 0)
    MoveCamera(132, 13, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(76000, 0)
    OP_68(-18000, -1000, 0, 7600)
    SetCameraDistance(46000, 7600)
    OP_0D()
    Sleep(1000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(3500)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(1000)
    Fade(500)
    OP_68(75000, -4500, 0, 0)
    MoveCamera(270, 0, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(55000, 0)
    OP_25(0x339, 0x64)
    Sound(455, 0, 100, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x1F40)
    OP_68(-75000, -4500, 0, 8000)
    MoveCamera(270, 25, 0, 8000)
    SetCameraDistance(55000, 8000)
    Sleep(6000)
    StopSound(451, 2000, 70)
    StopSound(825, 2000, 90)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 0)
    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_447 end

    def Function_3_640(): pass

    label("Function_3_640")

    Sound(825, 2, 0, 0)
    Sound(451, 2, 0, 0)
    Sleep(200)
    OP_25(0x339, 0xA)
    OP_25(0x1C3, 0xA)
    Sleep(200)
    OP_25(0x339, 0x14)
    OP_25(0x1C3, 0x14)
    Sleep(200)
    OP_25(0x339, 0x1E)
    OP_25(0x1C3, 0x1E)
    Sleep(200)
    OP_25(0x339, 0x28)
    OP_25(0x1C3, 0x28)
    Sleep(200)
    OP_25(0x1C3, 0x32)
    Sleep(200)
    OP_25(0x1C3, 0x3C)
    Sleep(200)
    OP_25(0x1C3, 0x46)
    Sleep(200)
    OP_25(0x1C3, 0x50)
    Return()

    # Function_3_640 end

    def Function_4_695(): pass

    label("Function_4_695")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch30200.itc", 0x1E)
    OP_68(-38500, 800, 570, 0)
    MoveCamera(42, 27, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13160, 0)
    SetChrChipByIndex(0x8, 0x1E)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x101, -39650, 0, 30, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_71A")
    SetChrPos(0x102, -38330, 0, 1030, 225)
    Jump("loc_7AD")

    label("loc_71A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_740")
    SetChrPos(0x103, -38330, 0, 1030, 225)
    Jump("loc_7AD")

    label("loc_740")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_766")
    SetChrPos(0x104, -38330, 0, 1030, 225)
    Jump("loc_7AD")

    label("loc_766")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_78C")
    SetChrPos(0x109, -38330, 0, 1030, 225)
    Jump("loc_7AD")

    label("loc_78C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7AD")
    SetChrPos(0x105, -38330, 0, 1030, 225)

    label("loc_7AD")

    SetChrPos(0x8, -37780, 0, -710, 315)
    PlayBGM("ed7561", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x231), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FDetective Raymond! Are\x01",
            "you ok!?\x02\x03",
            "It would've been alright\x01",
            "if you left everything\x01",
            "to us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "N-No... Basically, this\x01",
            "a case given to an\x01",
            "inspector to handle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I can't let you guys\x01",
            "have all the fun.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_91F")

    ChrTalk(
        0x102,
        (
            "#00100F*giggle*... Thank you\x01",
            "very much.\x02\x03",
            "By the way, where did\x01",
            "the fake brand trader\x01",
            "go?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD2")

    label("loc_91F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_98A")

    ChrTalk(
        0x103,
        (
            "#00200FHaha... I've changed my\x01",
            "opinion of you.\x02\x03",
            "So, the fake brand\x01",
            "trader is...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD2")

    label("loc_98A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9F7")

    ChrTalk(
        0x104,
        (
            "#00300FHaha... She's got guts,\x01",
            "I'll give her that.\x02\x03",
            "So, where did that\x01",
            "grandma go?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD2")

    label("loc_9F7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A67")

    ChrTalk(
        0x109,
        (
            "#10100FAhaha... Thank you very\x01",
            "much.\x02\x03",
            "By the way, where did\x01",
            "the fake brand trader\x01",
            "go?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD2")

    label("loc_A67")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AD2")

    ChrTalk(
        0x105,
        (
            "#10300FHehe... That one's got\x01",
            "spirit, she does.\x02\x03",
            "Well then, where did\x01",
            "that madame go?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AD2")

    OP_93(0x101, 0x0, 0x1F4)
    Sleep(500)
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(700)
    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_93(0x101, 0xE1, 0x1F4)
    OP_68(-42630, 800, -350, 3000)
    MoveCamera(42, 27, 0, 3000)
    OP_6E(700, 3000)
    SetCameraDistance(14660, 3000)
    BeginChrThread(0x101, 1, 0, 5)
    Sleep(1500)
    OP_93(0x1, 0x10E, 0x1F4)
    OP_93(0x8, 0x10E, 0x1F4)
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    Sleep(500)
    Fade(500)
    Sound(105, 0, 100, 0)
    SetMapObjFrame(0xFF, "huta01a", 0x0, 0x1)
    SetMapObjFrame(0xFF, "huta01b", 0x1, 0x1)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00003FThey probably used this from the\x01",
            "roof of some car and went\x01",
            "inside.\x02\x03",
            "#00000FWe should be able to corner them\x01",
            "if we clear the cars one-by-one\x01",
            "starting with the caboose.\x02\x03",
            "Let's go, Mr. Raymond!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Y-Yeah! We'll catch her\x01",
            "for sure!\x02",
        )
    )

    CloseMessageWindow()
    StopSound(825, 1000, 60)
    StopSound(451, 1000, 80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    AddParty(0xA0, 0xFF, 0xFF)
    SetScenarioFlags(0x22, 5)
    NewScene("e0410", 0, 0, 0)
    IdleLoop()
    EventEnd(0x5)
    Return()

    # Function_4_695 end

    def Function_5_CA3(): pass

    label("Function_5_CA3")

    OP_95(0xFE, -42770, -480, -2630, 2000, 0x0)
    OP_95(0xFE, -45480, -410, -2520, 2000, 0x0)
    OP_95(0xFE, -45940, -150, -1320, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_5_CA3 end

    def Function_6_CE7(): pass

    label("Function_6_CE7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch42550.itc", 0x1E)
    LoadChrToIndex("chr/ch42551.itc", 0x1F)
    LoadEffect(0x0, "battle/cr425100.eff")
    SoundLoad(860)
    SoundLoad(861)
    OP_68(26540, 660, -1340, 0)
    MoveCamera(36, 30, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13440, 0)
    SetChrPos(0x101, 25610, -210, -1990, 45)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D80")
    SetChrPos(0x102, 26910, -800, -3100, 0)
    Jump("loc_E13")

    label("loc_D80")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DA6")
    SetChrPos(0x103, 26910, -800, -3100, 0)
    Jump("loc_E13")

    label("loc_DA6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DCC")
    SetChrPos(0x104, 26910, -800, -3100, 0)
    Jump("loc_E13")

    label("loc_DCC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DF2")
    SetChrPos(0x109, 26910, -800, -3100, 0)
    Jump("loc_E13")

    label("loc_DF2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E13")
    SetChrPos(0x105, 26910, -800, -3100, 0)

    label("loc_E13")

    SetChrPos(0x1A1, 26970, -140, -1380, 180)
    SetChrChipByIndex(0xA, 0x1F)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 7250, -230, 2260, 90)
    SetChrChipByIndex(0xB, 0x1F)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 7300, -210, -2020, 90)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(21380, 780, -150, 3000)
    MoveCamera(36, 30, 0, 3000)
    OP_6E(700, 3000)
    SetCameraDistance(13440, 3000)
    BeginChrThread(0x101, 1, 0, 7)
    Sleep(200)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EBE")
    BeginChrThread(0x102, 1, 0, 8)
    Jump("loc_F25")

    label("loc_EBE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ED9")
    BeginChrThread(0x103, 1, 0, 8)
    Jump("loc_F25")

    label("loc_ED9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EF4")
    BeginChrThread(0x104, 1, 0, 8)
    Jump("loc_F25")

    label("loc_EF4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F0F")
    BeginChrThread(0x109, 1, 0, 8)
    Jump("loc_F25")

    label("loc_F0F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F25")
    BeginChrThread(0x105, 1, 0, 8)

    label("loc_F25")

    Sleep(500)
    BeginChrThread(0x1A1, 1, 0, 9)
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x1A1, 1)
    StopBGM(0x7D0)
    Sound(860, 2, 80, 0)
    Sound(861, 2, 80, 0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 17890, 0, 1310, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x0, 0x1, 0xFF, 0x0, 18360, 0, -950, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1A1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrFlags(0x0, 0x10)
    SetChrFlags(0x1, 0x10)
    SetChrFlags(0x1A1, 0x10)
    Sound(809, 0, 100, 0)

    def lambda_101F():
        OP_9D(0xFE, 0x4FBA, 0x0, 0x32, 0x12C, 0xDAC)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_101F)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_106C")

    def lambda_104F():
        OP_9D(0xFE, 0x5492, 0x0, 0x3B6, 0x12C, 0xDAC)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_104F)
    Jump("loc_112F")

    label("loc_106C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_109E")

    def lambda_1081():
        OP_9D(0xFE, 0x5492, 0x0, 0x3B6, 0x12C, 0xDAC)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1081)
    Jump("loc_112F")

    label("loc_109E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10D0")

    def lambda_10B3():
        OP_9D(0xFE, 0x5492, 0x0, 0x3B6, 0x12C, 0xDAC)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_10B3)
    Jump("loc_112F")

    label("loc_10D0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1102")

    def lambda_10E5():
        OP_9D(0xFE, 0x5492, 0x0, 0x3B6, 0x12C, 0xDAC)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_10E5)
    Jump("loc_112F")

    label("loc_1102")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_112F")

    def lambda_1117():
        OP_9D(0xFE, 0x5492, 0x0, 0x3B6, 0x12C, 0xDAC)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1117)

    label("loc_112F")

    Sleep(50)

    def lambda_1137():
        OP_9D(0xFE, 0x5348, 0xFFFFFFBA, 0xFFFFFD12, 0x12C, 0xDAC)
        ExitThread()

    QueueWorkItem(0x1A1, 1, lambda_1137)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x1A1, 1)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    StopSound(860, 500, 70)
    StopSound(861, 500, 70)

    ChrTalk(
        0x1A1,
        "Uwaaaah!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FW-What!?\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7507", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x1FB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(19560, 800, 0, 3000)
    MoveCamera(36, 30, 0, 3000)
    OP_6E(700, 3000)
    SetCameraDistance(13440, 3000)
    BeginChrThread(0xA, 1, 0, 10)
    BeginChrThread(0xB, 1, 0, 11)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xB, 1)

    ChrTalk(
        0x101,
        (
            "#00001FThe Republican\x01",
            "terrorists that targeted\x01",
            "the trade conference?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "You guys look like\x01",
            "Crossbell Police.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I don't know what's\x01",
            "going on, but you're not\x01",
            "gonna arrest us!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You're dead meat if you\x01",
            "chase us any further!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1363")

    ChrTalk(
        0x102,
        (
            "#00105F...T-They seem to be\x01",
            "serious.\x02\x03",
            "#00106FAlthough I don't really know\x01",
            "why they're teaming up with\x01",
            "the fake brand trader...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1587")

    label("loc_1363")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13F6")

    ChrTalk(
        0x103,
        (
            "#00201F...It seems they're not\x01",
            "kidding.\x02\x03",
            "#00206FThough I don't understand\x01",
            "why they teamed up with\x01",
            "the fake brand trader.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1587")

    label("loc_13F6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1495")

    ChrTalk(
        0x104,
        (
            "#00301FTch... that equipment...\x01",
            "It's really them.\x02\x03",
            "#00306FI've no clue why they're\x01",
            "doing the fake brand\x01",
            "trader's dirty work, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1587")

    label("loc_1495")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_151E")

    ChrTalk(
        0x109,
        (
            "#10101FThat equipment... It's\x01",
            "really them!\x02\x03",
            "#10106FBut, why are they\x01",
            "teaming up with the fake\x01",
            "brand trader...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1587")

    label("loc_151E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1587")

    ChrTalk(
        0x105,
        (
            "#10305FHmm... There's no\x01",
            "mistake.\x02\x03",
            "#10309FI guess they're that\x01",
            "madame's trump card?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1587")


    ChrTalk(
        0x101,
        (
            "#00003FAnyway... We can't give\x01",
            "in to this level of\x01",
            "threat.\x02\x03",
            "#00007FWe're taking you down!\x01",
            "All of you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A1,
        "E-Eek... W-Wait...!\x02",
    )

    CloseMessageWindow()

    def lambda_1610():
        OP_95(0xFE, 17910, 0, 70, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1610)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1654")

    def lambda_163A():
        OP_95(0xFE, 19150, 0, 990, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_163A)
    Jump("loc_170B")

    label("loc_1654")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1683")

    def lambda_1669():
        OP_95(0xFE, 19150, 0, 990, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1669)
    Jump("loc_170B")

    label("loc_1683")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16B2")

    def lambda_1698():
        OP_95(0xFE, 19150, 0, 990, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1698)
    Jump("loc_170B")

    label("loc_16B2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16E1")

    def lambda_16C7():
        OP_95(0xFE, 19150, 0, 990, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_16C7)
    Jump("loc_170B")

    label("loc_16E1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_170B")

    def lambda_16F6():
        OP_95(0xFE, 19150, 0, 990, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_16F6)

    label("loc_170B")


    def lambda_1710():
        OP_95(0xFE, 19750, 0, -620, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A1, 1, lambda_1710)
    Sleep(200)
    Battle("BattleInfo_2CC", 0x30200011, 0x0, 0x0, 0x25, 0xFF)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x1A1, 0x1)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    LoadChrToIndex("chr/ch42553.itc", 0x1E)
    LoadChrToIndex("chr/ch42500.itc", 0x1F)
    LoadChrToIndex("chr/ch42551.itc", 0x20)
    OP_68(19560, 800, 0, 0)
    MoveCamera(36, 30, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13440, 0)
    SetChrPos(0x101, 19410, 0, 70, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17DB")
    SetChrPos(0x102, 20650, 0, 990, 270)
    Jump("loc_186E")

    label("loc_17DB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1801")
    SetChrPos(0x103, 20650, 0, 990, 270)
    Jump("loc_186E")

    label("loc_1801")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1827")
    SetChrPos(0x104, 20650, 0, 990, 270)
    Jump("loc_186E")

    label("loc_1827")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_184D")
    SetChrPos(0x109, 20650, 0, 990, 270)
    Jump("loc_186E")

    label("loc_184D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_186E")
    SetChrPos(0x105, 20650, 0, 990, 270)

    label("loc_186E")

    SetChrPos(0x1A1, 21250, 0, -620, 270)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x2)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 17110, -100, 980, 90)
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x2)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 17280, 0, -680, 90)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xA,
        (
            "W-What's with these\x01",
            "guys...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Tch... Blondie here\x01",
            "aside, those other two\x01",
            "are bad news.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We've bought some time.\x01",
            "Pull back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Right!\x02",
    )

    CloseMessageWindow()
    Fade(500)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x1F)
    SetChrSubChip(0xB, 0x0)
    OP_0D()
    BeginChrThread(0xA, 1, 0, 12)
    BeginChrThread(0xB, 1, 0, 13)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xB, 1)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)

    ChrTalk(
        0x1A1,
        "T-That was scary...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00010FUgh... They ran away\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A3E")

    ChrTalk(
        0x102,
        (
            "#00103FBut there's nowhere left\x01",
            "to run.\x02\x03",
            "#00100FLet's brace ourselves.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BD7")

    label("loc_1A3E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1AA4")

    ChrTalk(
        0x103,
        (
            "#00203FBut now, there's nowhere\x01",
            "left to run.\x02\x03",
            "#00200FLet's brace ourselves.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BD7")

    label("loc_1AA4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1B09")

    ChrTalk(
        0x104,
        (
            "#00303FThere's really no place\x01",
            "left to run.\x02\x03",
            "#00301FLet's brace ourselves.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BD7")

    label("loc_1B09")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1B6F")

    ChrTalk(
        0x109,
        (
            "#10103FBut now, there's nowhere\x01",
            "left to run.\x02\x03",
            "#10101FLet's brace ourselves!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BD7")

    label("loc_1B6F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1BD7")

    ChrTalk(
        0x105,
        (
            "#10304FWell, they should have\x01",
            "no place left to run.\x02\x03",
            "#10300FLet's brace ourselves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BD7")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    SetChrPos(0x0, 15470, -90, -890, 270)
    OP_37()
    OP_29(0x81, 0x1, 0x6)
    OP_29(0x81, 0x1, 0x7)
    SetScenarioFlags(0x173, 6)
    ModifyEventFlags(1, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_6_CE7 end

    def Function_7_1C11(): pass

    label("Function_7_1C11")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_95(0xFE, 22420, -220, -2090, 4000, 0x0)
    OP_95(0xFE, 17910, 0, 70, 4000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_7_1C11 end

    def Function_8_1C48(): pass

    label("Function_8_1C48")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_95(0xFE, 22670, -440, -2580, 4000, 0x0)
    OP_95(0xFE, 19750, 0, 990, 4000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_8_1C48 end

    def Function_9_1C7F(): pass

    label("Function_9_1C7F")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_95(0xFE, 22380, -230, -2140, 4000, 0x0)
    OP_95(0xFE, 19350, 0, -750, 4000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_9_1C7F end

    def Function_10_1CB6(): pass

    label("Function_10_1CB6")

    OP_95(0xFE, 15020, -220, 2070, 4000, 0x0)
    OP_95(0xFE, 17110, -100, 980, 4000, 0x0)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_10_1CB6 end

    def Function_11_1CEE(): pass

    label("Function_11_1CEE")

    OP_95(0xFE, 15260, -240, -2280, 4000, 0x0)
    OP_95(0xFE, 17280, 0, -680, 4000, 0x0)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_11_1CEE end

    def Function_12_1D26(): pass

    label("Function_12_1D26")

    OP_93(0xFE, 0x13B, 0x1F4)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    OP_95(0xFE, 15020, -220, 2070, 5000, 0x0)
    OP_95(0xFE, 7250, -230, 2260, 5000, 0x0)
    Return()

    # Function_12_1D26 end

    def Function_13_1D5E(): pass

    label("Function_13_1D5E")

    OP_93(0xFE, 0xE1, 0x1F4)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    OP_95(0xFE, 15260, -240, -2280, 5000, 0x0)
    OP_95(0xFE, 7300, -210, -2020, 5000, 0x0)
    Return()

    # Function_13_1D5E end

    def Function_14_1D96(): pass

    label("Function_14_1D96")

    EventBegin(0x0)
    Fade(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch42500.itc", 0x1E)
    LoadChrToIndex("chr/ch42552.itc", 0x1F)
    LoadChrToIndex("chr/ch24100.itc", 0x20)
    LoadChrToIndex("chr/ch00050.itc", 0x21)
    LoadChrToIndex("chr/ch00150.itc", 0x22)
    LoadChrToIndex("chr/ch00250.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch02950.itc", 0x25)
    LoadChrToIndex("chr/ch03050.itc", 0x26)
    LoadChrToIndex("apl/ch51720.itc", 0x27)
    OP_68(-38140, 1300, -300, 0)
    MoveCamera(332, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18670, 0)
    SetChrPos(0x101, -23650, -380, -2500, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E49")
    SetChrPos(0x102, -22520, -370, -2480, 270)
    Jump("loc_1EDC")

    label("loc_1E49")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E6F")
    SetChrPos(0x103, -22520, -370, -2480, 270)
    Jump("loc_1EDC")

    label("loc_1E6F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E95")
    SetChrPos(0x104, -22520, -370, -2480, 270)
    Jump("loc_1EDC")

    label("loc_1E95")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1EBB")
    SetChrPos(0x109, -22520, -370, -2480, 270)
    Jump("loc_1EDC")

    label("loc_1EBB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1EDC")
    SetChrPos(0x105, -22520, -370, -2480, 270)

    label("loc_1EDC")

    SetChrPos(0x1A1, -21360, -370, -2470, 270)
    SetChrChipByIndex(0xA, 0x1E)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -39510, -10, -30, 270)
    SetChrChipByIndex(0xB, 0x1E)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, -40270, -10, -1410, 315)
    SetChrChipByIndex(0xC, 0x1E)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -40300, -10, 1210, 225)
    SetChrChipByIndex(0x9, 0x20)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -41450, -10, -50, 90)
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0x101, 1, 0, 15)
    Sleep(200)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F97")
    BeginChrThread(0x102, 1, 0, 16)
    Jump("loc_1FFE")

    label("loc_1F97")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1FB2")
    BeginChrThread(0x103, 1, 0, 16)
    Jump("loc_1FFE")

    label("loc_1FB2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1FCD")
    BeginChrThread(0x104, 1, 0, 16)
    Jump("loc_1FFE")

    label("loc_1FCD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1FE8")
    BeginChrThread(0x109, 1, 0, 16)
    Jump("loc_1FFE")

    label("loc_1FE8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1FFE")
    BeginChrThread(0x105, 1, 0, 16)

    label("loc_1FFE")

    Sleep(200)
    BeginChrThread(0x1A1, 1, 0, 17)
    WaitChrThread(0x1A1, 1)

    ChrTalk(
        0x101,
        "#00007FWait!!\x02",
    )

    CloseMessageWindow()

    def lambda_2023():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2023)
    Sleep(100)

    def lambda_2033():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2033)
    Sleep(100)

    def lambda_2043():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2043)
    WaitChrThread(0xC, 1)
    Fade(500)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x1F)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "#5PHmph... Persistent to\x01",
            "the bitter end. I'll\x01",
            "give you that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PWell these kids were an\x01",
            "unforeseen windfall,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FThere's no place to run this\x01",
            "time.\x02\x03",
            "#00001FIt's impossible to run any\x01",
            "further than you already\x01",
            "have. Surrender and give up.\x02\x03",
            "The terrorists with you too,\x01",
            "of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A1,
        (
            "T-That's right!\x01",
            "Surrender!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Ugh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Indeed...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "So this is our limit,\x01",
            "huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PMy, my... There's\x01",
            "something lacking in\x01",
            "youths lately.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1A1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0xA, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0xB, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0xC, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_234F")

    ChrTalk(
        0x102,
        (
            "#00105FWhat do you mean?\x02\x03",
            "#00106FYou're not planning to\x01",
            "escape again, are you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24DB")

    label("loc_234F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_23B8")

    ChrTalk(
        0x103,
        (
            "#00205FWhat do you mean?\x02\x03",
            "#00203FYou're not planning to\x01",
            "escape again, are you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24DB")

    label("loc_23B8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2417")

    ChrTalk(
        0x104,
        (
            "#00305FWhaddya mean by that?\x02\x03",
            "#00306FYou plannin' to run away\x01",
            "again?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24DB")

    label("loc_2417")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2482")

    ChrTalk(
        0x109,
        (
            "#10105FW-What do you mean?\x02\x03",
            "#10101FYou're not planning to\x01",
            "escape again, are you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24DB")

    label("loc_2482")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_24DB")

    ChrTalk(
        0x105,
        (
            "#10305FHmm?\x02\x03",
            "#10302FLooks like you're\x01",
            "planning to escape\x01",
            "again, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24DB")


    ChrTalk(
        0x9,
        "#5PPlan? Hah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PYou're still saying that\x01",
            "optimistic bullshit, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P...Once this train gets\x01",
            "to Altair City, you're\x01",
            "mine!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PThe Republic's my home\x01",
            "turf, see?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5POnce the train stops,\x01",
            "I'm outta here!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1A1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006FE-Escape...\x02\x03",
            "#00011FYou're still planning on\x01",
            "running this late in the\x01",
            "game!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hah! Fine then, listen\x01",
            "up!\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x9,
        (
            "#5P#5SAs long as this continent\x01",
            "exists... anything can be\x01",
            "my escape route!!#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x9,
        (
            "#5P#5SAs long as you guys are on\x01",
            "my heels... you have no\x01",
            "hope of catching me!#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x9,
        (
            "#5P#5SDo you understand now,\x01",
            "fools!?#3S\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Yeah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Come at us!\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1A1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006FH-Hmm... They must be crazy.\x01",
            "They're really planning on\x01",
            "running 'til the bitter end.\x02\x03",
            "I'm scared this old lady\x01",
            "will really go through with\x01",
            "it, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A1,
        (
            "U-Us too... We can't let\x01",
            "them get away!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A1,
        (
            "This is an important\x01",
            "duty entrusted to the\x01",
            "police.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2917")

    ChrTalk(
        0x102,
        "#00105FMr. Raymond...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A07")

    label("loc_2917")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2955")

    ChrTalk(
        0x103,
        (
            "#00205FMr. Raymond... You're\x01",
            "right.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A07")

    label("loc_2955")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2993")

    ChrTalk(
        0x104,
        (
            "#00302FHehe. You've got spirit,\x01",
            "eh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A07")

    label("loc_2993")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_29D1")

    ChrTalk(
        0x109,
        (
            "#10102FMr. Raymond... That's\x01",
            "right!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A07")

    label("loc_29D1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A07")

    ChrTalk(
        0x105,
        (
            "#10302FHmm... Hehe, that's\x01",
            "nice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A07")


    ChrTalk(
        0x101,
        (
            "#00001FIf that's the case... We\x01",
            "have no choice but to\x01",
            "capture her here.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A84")
    SetChrChipByIndex(0x102, 0x22)
    SetChrSubChip(0x102, 0x0)
    Jump("loc_2AF3")

    label("loc_2A84")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2AA1")
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x0)
    Jump("loc_2AF3")

    label("loc_2AA1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2ABE")
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    Jump("loc_2AF3")

    label("loc_2ABE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2ADB")
    SetChrChipByIndex(0x109, 0x25)
    SetChrSubChip(0x109, 0x0)
    Jump("loc_2AF3")

    label("loc_2ADB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2AF3")
    SetChrChipByIndex(0x105, 0x26)
    SetChrSubChip(0x105, 0x0)

    label("loc_2AF3")

    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x1A1, 0x27)
    SetChrSubChip(0x1A1, 0x0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00007FLet's go everyone! We'll\x01",
            "disable them!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PHow many times do I have\x01",
            "to tell you?\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x9,
        (
            "#5P#5SIf you guys can really\x01",
            "catch me, JUST GO AHEAD\x01",
            "AND TRY!!#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x9,
        (
            "#5P#5S─C'mon you guys, get\x01",
            "'em!!#3S\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle("BattleInfo_310", 0x30200011, 0x0, 0x0, 0x21, 0xFF)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C39")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C43")

    label("loc_2C39")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C43")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-38140, 1300, -300, 0)
    MoveCamera(332, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18670, 0)
    LoadChrToIndex("chr/ch42553.itc", 0x1E)
    LoadChrToIndex("chr/ch24153.itc", 0x1F)
    LoadChrToIndex("chr/ch24100.itc", 0x20)
    LoadChrToIndex("chr/ch00050.itc", 0x21)
    LoadChrToIndex("chr/ch00150.itc", 0x22)
    LoadChrToIndex("chr/ch00250.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch02950.itc", 0x25)
    LoadChrToIndex("chr/ch03050.itc", 0x26)
    LoadChrToIndex("apl/ch51720.itc", 0x27)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x2)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -39510, -10, -30, 90)
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x2)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, -40270, -10, -1410, 90)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x2)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -40300, -10, 1210, 90)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D3E")
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    Jump("loc_2D58")

    label("loc_2D3E")

    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    label("loc_2D58")

    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -41450, -10, -50, 90)
    SetChrPos(0x101, -36930, 0, -130, 270)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2DBA")
    SetChrPos(0x102, -35010, -90, 810, 270)
    SetChrChipByIndex(0x102, 0x22)
    SetChrSubChip(0x102, 0x0)
    Jump("loc_2E6D")

    label("loc_2DBA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2DE8")
    SetChrPos(0x103, -35010, -90, 810, 270)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x0)
    Jump("loc_2E6D")

    label("loc_2DE8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2E16")
    SetChrPos(0x104, -35010, -90, 810, 270)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    Jump("loc_2E6D")

    label("loc_2E16")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2E44")
    SetChrPos(0x109, -35010, -90, 810, 270)
    SetChrChipByIndex(0x109, 0x25)
    SetChrSubChip(0x109, 0x0)
    Jump("loc_2E6D")

    label("loc_2E44")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2E6D")
    SetChrPos(0x105, -35010, -90, 810, 270)
    SetChrChipByIndex(0x105, 0x26)
    SetChrSubChip(0x105, 0x0)

    label("loc_2E6D")

    SetChrPos(0x1A1, -35640, -130, -1310, 270)
    SetChrChipByIndex(0x1A1, 0x27)
    SetChrSubChip(0x1A1, 0x0)
    PlayBGM("ed7111", 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#00006FPhew...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A1,
        "W-We did it...\x02",
    )

    CloseMessageWindow()
    Fade(500)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2EEC")
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    Jump("loc_2F5B")

    label("loc_2EEC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F09")
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    Jump("loc_2F5B")

    label("loc_2F09")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F26")
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Jump("loc_2F5B")

    label("loc_2F26")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F43")
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    Jump("loc_2F5B")

    label("loc_2F43")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F5B")
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)

    label("loc_2F5B")

    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x1A1, 0xFF)
    SetChrSubChip(0x1A1, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3076")

    ChrTalk(
        0xA,
        "U-Ugggh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Owowow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PD-Damn it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Hmm. I feel a little\x01",
            "bad for attacking an old\x01",
            "lady)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PY-You guys... You won't\x01",
            "get away with thiiis...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1A1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_3230")

    label("loc_3076")

    OP_2C(0x81, 0x1)

    ChrTalk(
        0x9,
        (
            "#5PN-No... This cannot\x01",
            "beee!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PG-Guys, pull yourselves\x01",
            "together! Show 'em\x01",
            "you've got guts!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "U-Ugggh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Owowow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PC-Crap!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PYou... How dare you!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PIf it's like this, then\x01",
            "my getaway by jumping\x01",
            "off the train is...!!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1A1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006FI-I really don't think you'll\x01",
            "get through that in one piece\x01",
            "so please just stop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PUgh!!\x02",
    )

    CloseMessageWindow()

    label("loc_3230")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_32AB")

    ChrTalk(
        0x102,
        (
            "#00106FW-What an insane\x01",
            "tenacity she has...\x02\x03",
            "#00101FAlthough the terrorists\x01",
            "are all exhausted...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3473")

    label("loc_32AB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3323")

    ChrTalk(
        0x103,
        (
            "#00206F...She's insanely tough.\x02\x03",
            "#00200FMaybe even more than all\x01",
            "those terrorists\x01",
            "combined...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3473")

    label("loc_3323")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_339F")

    ChrTalk(
        0x104,
        (
            "#00306FJeez, a tenacious\x01",
            "grandma as always.\x02\x03",
            "#00301FEven though the\x01",
            "terrorists are all\x01",
            "exhausted.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3473")

    label("loc_339F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3405")

    ChrTalk(
        0x109,
        (
            "#10106FUgh... How tenacious.\x02\x03",
            "#10101FIsn't she tougher than\x01",
            "the terrorists?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3473")

    label("loc_3405")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3473")

    ChrTalk(
        0x105,
        (
            "#10302FHaha... What a strong\x01",
            "madame.\x02\x03",
            "#10300FIsn't she way stronger\x01",
            "than the terrorists?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3473")


    ChrTalk(
        0x101,
        (
            "#00006FYeah, seriously.\x02\x03",
            "#00000FAlright then, Mr.\x01",
            "Raymond. What should we\x01",
            "do with them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A1,
        "Hmm, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A1,
        (
            "We'll arrive in Altair City soon.\x01",
            "I'll contact the Republican Army\x01",
            "and hand them over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FWell... They all look\x01",
            "Republican, so I think\x01",
            "that's best.\x02\x03",
            "#00000FAlright. Let's ask the\x01",
            "conductor to contact\x01",
            "them for us.\x02",
        )
    )

    CloseMessageWindow()
    StopSound(451, 1000, 80)
    StopSound(825, 1000, 60)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 1)
    NewScene("t5000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_14_1D96 end

    def Function_15_35F5(): pass

    label("Function_15_35F5")

    OP_95(0xFE, -35330, -200, -1940, 4000, 0x0)
    OP_95(0xFE, -36930, 0, -130, 4000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_15_35F5 end

    def Function_16_3625(): pass

    label("Function_16_3625")

    OP_95(0xFE, -34700, -190, -1850, 4000, 0x0)
    OP_95(0xFE, -35010, -90, 810, 4000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_16_3625 end

    def Function_17_3655(): pass

    label("Function_17_3655")

    OP_95(0xFE, -34350, -530, -2710, 4000, 0x0)
    OP_95(0xFE, -35640, -130, -1310, 4000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_17_3655 end

    SaveToFile()

Try(main)
