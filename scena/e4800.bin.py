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
        "Function_5_CBB",          # 05, 5
        "Function_6_CFF",          # 06, 6
        "Function_7_1C90",         # 07, 7
        "Function_8_1CC7",         # 08, 8
        "Function_9_1CFE",         # 09, 9
        "Function_10_1D35",        # 0A, 10
        "Function_11_1D6D",        # 0B, 11
        "Function_12_1DA5",        # 0C, 12
        "Function_13_1DDD",        # 0D, 13
        "Function_14_1E15",        # 0E, 14
        "Function_15_3710",        # 0F, 15
        "Function_16_3740",        # 10, 16
        "Function_17_3770",        # 11, 17
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
            "#00000FMr. Raymond...\x01",
            "Are you ok!?\x02\x03",
            "It would've been alright if\x01",
            "you left everything to us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "N-No... Basically, this is\x01",
            "a case I was given by the\x01",
            "Inspector, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I couldn't let you\x01",
            "guys have all the fun.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_92A")

    ChrTalk(
        0x102,
        (
            "#00100F*giggle*...\x01",
            "Thank you very much.\x02\x03",
            "By the way, where did\x01",
            "the fake brand trader go...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE0")

    label("loc_92A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9A0")

    ChrTalk(
        0x103,
        (
            "#00200FUh uh...\x01",
            "I have a better opinion of you.\x02\x03",
            "So, where did the\x01",
            "fake brand trader go...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE0")

    label("loc_9A0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A04")

    ChrTalk(
        0x104,
        (
            "#00300FHa ha...\x01",
            "What admirable guts.\x02\x03",
            "So, where did  \x01",
            "that grandma go...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE0")

    label("loc_A04")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A77")

    ChrTalk(
        0x109,
        (
            "#10100FAhaha...\x01",
            "Thank you very much.\x02\x03",
            "By the way, where did\x01",
            "the fake brand trader go...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE0")

    label("loc_A77")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AE0")

    ChrTalk(
        0x105,
        (
            "#10300FHu hu...\x01",
            "That's a nice disposition.\x02\x03",
            "Well then, where did that madame go...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE0")

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
            "#00003FShe probably used this from the\x01",
            "roof of some car and escaped inside.\x02\x03",
            "#00000FWe should be able to corner her if we clear\x01",
            "the cars one-by-one starting from the rear.\x02\x03",
            "Let's go, Mr. Raymond!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Y-Yeah, of course! \x01",
            "We'll catch her for sure!\x02",
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

    def Function_5_CBB(): pass

    label("Function_5_CBB")

    OP_95(0xFE, -42770, -480, -2630, 2000, 0x0)
    OP_95(0xFE, -45480, -410, -2520, 2000, 0x0)
    OP_95(0xFE, -45940, -150, -1320, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_5_CBB end

    def Function_6_CFF(): pass

    label("Function_6_CFF")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D98")
    SetChrPos(0x102, 26910, -800, -3100, 0)
    Jump("loc_E2B")

    label("loc_D98")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DBE")
    SetChrPos(0x103, 26910, -800, -3100, 0)
    Jump("loc_E2B")

    label("loc_DBE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DE4")
    SetChrPos(0x104, 26910, -800, -3100, 0)
    Jump("loc_E2B")

    label("loc_DE4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E0A")
    SetChrPos(0x109, 26910, -800, -3100, 0)
    Jump("loc_E2B")

    label("loc_E0A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E2B")
    SetChrPos(0x105, 26910, -800, -3100, 0)

    label("loc_E2B")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ED6")
    BeginChrThread(0x102, 1, 0, 8)
    Jump("loc_F3D")

    label("loc_ED6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EF1")
    BeginChrThread(0x103, 1, 0, 8)
    Jump("loc_F3D")

    label("loc_EF1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F0C")
    BeginChrThread(0x104, 1, 0, 8)
    Jump("loc_F3D")

    label("loc_F0C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F27")
    BeginChrThread(0x109, 1, 0, 8)
    Jump("loc_F3D")

    label("loc_F27")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F3D")
    BeginChrThread(0x105, 1, 0, 8)

    label("loc_F3D")

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

    def lambda_1037():
        OP_9D(0xFE, 0x4FBA, 0x0, 0x32, 0x12C, 0xDAC)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1037)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1084")

    def lambda_1067():
        OP_9D(0xFE, 0x5492, 0x0, 0x3B6, 0x12C, 0xDAC)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1067)
    Jump("loc_1147")

    label("loc_1084")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10B6")

    def lambda_1099():
        OP_9D(0xFE, 0x5492, 0x0, 0x3B6, 0x12C, 0xDAC)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1099)
    Jump("loc_1147")

    label("loc_10B6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10E8")

    def lambda_10CB():
        OP_9D(0xFE, 0x5492, 0x0, 0x3B6, 0x12C, 0xDAC)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_10CB)
    Jump("loc_1147")

    label("loc_10E8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_111A")

    def lambda_10FD():
        OP_9D(0xFE, 0x5492, 0x0, 0x3B6, 0x12C, 0xDAC)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_10FD)
    Jump("loc_1147")

    label("loc_111A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1147")

    def lambda_112F():
        OP_9D(0xFE, 0x5492, 0x0, 0x3B6, 0x12C, 0xDAC)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_112F)

    label("loc_1147")

    Sleep(50)

    def lambda_114F():
        OP_9D(0xFE, 0x5348, 0xFFFFFFBA, 0xFFFFFD12, 0x12C, 0xDAC)
        ExitThread()

    QueueWorkItem(0x1A1, 1, lambda_114F)
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
        "#00005FW-What the...!?\x02",
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
            "#00001FThe Republican terrorists that\x01",
            "targeted the Trade Conference...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "You guys look like Crossbell Police.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I don't know what's going on,\x01",
            "but you're not gonna arrest us!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "You're dead meat if you chase us any further!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1385")

    ChrTalk(
        0x102,
        (
            "#00105F...T-They seem to be serious.\x02\x03",
            "#00106FAlthough I don't really\x01",
            "know why they're teaming up\x01",
            "with the fake brand trader...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15CB")

    label("loc_1385")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_141D")

    ChrTalk(
        0x103,
        (
            "#00201F...That seems no empty threat.\x02\x03",
            "#00206FThough I have no idea why\x01",
            "terrorists are teaming up\x01",
            "with a fake brand trader...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15CB")

    label("loc_141D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14CD")

    ChrTalk(
        0x104,
        (
            "#00301FTch...that equipment...\x01",
            "It seems they really are 'em.\x02\x03",
            "#00306FThough I have no idea why\x01",
            "they have become the fake\x01",
            "brand trader's underlings...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15CB")

    label("loc_14CD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1569")

    ChrTalk(
        0x109,
        (
            "#10101FThat equipment...\x01",
            "It seems they really are them!\x02\x03",
            "#10106FB-But why would they be teaming\x01",
            "up with the fake brand trader...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15CB")

    label("loc_1569")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15CB")

    ChrTalk(
        0x105,
        (
            "#10305FEeh...\x01",
            "It seems they're them.\x02\x03",
            "#10309FThat madame's hidden-ball play?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15CB")


    ChrTalk(
        0x101,
        (
            "#00003FAnyway... \x01",
            "We can't give in to\x01",
            "these kind of threats.\x02\x03",
            "#00007FWe're taking you down! All of you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A1,
        (
            "E-Eek...\x01",
            "W-Wait...!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1656():
        OP_95(0xFE, 17910, 0, 70, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1656)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_169A")

    def lambda_1680():
        OP_95(0xFE, 19150, 0, 990, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1680)
    Jump("loc_1751")

    label("loc_169A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16C9")

    def lambda_16AF():
        OP_95(0xFE, 19150, 0, 990, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_16AF)
    Jump("loc_1751")

    label("loc_16C9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16F8")

    def lambda_16DE():
        OP_95(0xFE, 19150, 0, 990, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_16DE)
    Jump("loc_1751")

    label("loc_16F8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1727")

    def lambda_170D():
        OP_95(0xFE, 19150, 0, 990, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_170D)
    Jump("loc_1751")

    label("loc_1727")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1751")

    def lambda_173C():
        OP_95(0xFE, 19150, 0, 990, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_173C)

    label("loc_1751")


    def lambda_1756():
        OP_95(0xFE, 19750, 0, -620, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A1, 1, lambda_1756)
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1821")
    SetChrPos(0x102, 20650, 0, 990, 270)
    Jump("loc_18B4")

    label("loc_1821")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1847")
    SetChrPos(0x103, 20650, 0, 990, 270)
    Jump("loc_18B4")

    label("loc_1847")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_186D")
    SetChrPos(0x104, 20650, 0, 990, 270)
    Jump("loc_18B4")

    label("loc_186D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1893")
    SetChrPos(0x109, 20650, 0, 990, 270)
    Jump("loc_18B4")

    label("loc_1893")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_18B4")
    SetChrPos(0x105, 20650, 0, 990, 270)

    label("loc_18B4")

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
        "W-What's with these guys...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Tch... Looks like aside from blondie there,\x01",
            "we can't make light of the other two.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We bought some time.\x01",
            "Pull back for now!\x02",
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
            "#00010FUgh.. \x01",
            "They ran away again.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1AAD")

    ChrTalk(
        0x102,
        (
            "#00103FHowever, they have no\x01",
            "more place to run to.\x02\x03",
            "#00100FLet's brace ourselves.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C56")

    label("loc_1AAD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1B11")

    ChrTalk(
        0x103,
        (
            "#00203FBut now, they have\x01",
            "no place to run.\x02\x03",
            "#00200FLet's brace ourselves.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C56")

    label("loc_1B11")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1B7F")

    ChrTalk(
        0x104,
        (
            "#00303FBut they really have no\x01",
            "more place to run to.\x02\x03",
            "#00301FLet's brace ourselves!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C56")

    label("loc_1B7F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1BEB")

    ChrTalk(
        0x109,
        (
            "#10103FHowever, they have no\x01",
            "more place to run to.\x02\x03",
            "#10101FLet's brace ourselves!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C56")

    label("loc_1BEB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C56")

    ChrTalk(
        0x105,
        (
            "#10304FWell, they really have no\x01",
            "more place to run to.\x02\x03",
            "#10300FLet's brace ourselves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C56")

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

    # Function_6_CFF end

    def Function_7_1C90(): pass

    label("Function_7_1C90")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_95(0xFE, 22420, -220, -2090, 4000, 0x0)
    OP_95(0xFE, 17910, 0, 70, 4000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_7_1C90 end

    def Function_8_1CC7(): pass

    label("Function_8_1CC7")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_95(0xFE, 22670, -440, -2580, 4000, 0x0)
    OP_95(0xFE, 19750, 0, 990, 4000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_8_1CC7 end

    def Function_9_1CFE(): pass

    label("Function_9_1CFE")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_95(0xFE, 22380, -230, -2140, 4000, 0x0)
    OP_95(0xFE, 19350, 0, -750, 4000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_9_1CFE end

    def Function_10_1D35(): pass

    label("Function_10_1D35")

    OP_95(0xFE, 15020, -220, 2070, 4000, 0x0)
    OP_95(0xFE, 17110, -100, 980, 4000, 0x0)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_10_1D35 end

    def Function_11_1D6D(): pass

    label("Function_11_1D6D")

    OP_95(0xFE, 15260, -240, -2280, 4000, 0x0)
    OP_95(0xFE, 17280, 0, -680, 4000, 0x0)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_11_1D6D end

    def Function_12_1DA5(): pass

    label("Function_12_1DA5")

    OP_93(0xFE, 0x13B, 0x1F4)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    OP_95(0xFE, 15020, -220, 2070, 5000, 0x0)
    OP_95(0xFE, 7250, -230, 2260, 5000, 0x0)
    Return()

    # Function_12_1DA5 end

    def Function_13_1DDD(): pass

    label("Function_13_1DDD")

    OP_93(0xFE, 0xE1, 0x1F4)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    OP_95(0xFE, 15260, -240, -2280, 5000, 0x0)
    OP_95(0xFE, 7300, -210, -2020, 5000, 0x0)
    Return()

    # Function_13_1DDD end

    def Function_14_1E15(): pass

    label("Function_14_1E15")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1EC8")
    SetChrPos(0x102, -22520, -370, -2480, 270)
    Jump("loc_1F5B")

    label("loc_1EC8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1EEE")
    SetChrPos(0x103, -22520, -370, -2480, 270)
    Jump("loc_1F5B")

    label("loc_1EEE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F14")
    SetChrPos(0x104, -22520, -370, -2480, 270)
    Jump("loc_1F5B")

    label("loc_1F14")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F3A")
    SetChrPos(0x109, -22520, -370, -2480, 270)
    Jump("loc_1F5B")

    label("loc_1F3A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F5B")
    SetChrPos(0x105, -22520, -370, -2480, 270)

    label("loc_1F5B")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2016")
    BeginChrThread(0x102, 1, 0, 16)
    Jump("loc_207D")

    label("loc_2016")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2031")
    BeginChrThread(0x103, 1, 0, 16)
    Jump("loc_207D")

    label("loc_2031")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_204C")
    BeginChrThread(0x104, 1, 0, 16)
    Jump("loc_207D")

    label("loc_204C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2067")
    BeginChrThread(0x109, 1, 0, 16)
    Jump("loc_207D")

    label("loc_2067")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_207D")
    BeginChrThread(0x105, 1, 0, 16)

    label("loc_207D")

    Sleep(200)
    BeginChrThread(0x1A1, 1, 0, 17)
    WaitChrThread(0x1A1, 1)

    ChrTalk(
        0x101,
        "#00007FWait!!\x02",
    )

    CloseMessageWindow()

    def lambda_20A2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_20A2)
    Sleep(100)

    def lambda_20B2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_20B2)
    Sleep(100)

    def lambda_20C2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_20C2)
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
            "#5PHmph... Persistent to the\x01",
            "bitter end. I'll give you that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PWell these kids are an\x01",
            "unforeseen windfall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...There's no place\x01",
            "to run this time.\x02\x03",
            "#00001FIt's impossible to run any\x01",
            "further than you already have\x01",
            "Please give up and surrender.\x02\x03",
            "The terrorists with\x01",
            "you too, of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A1,
        "T-That's right! Surrender!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Ugh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "So this is all we can do, huh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5P...........\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PMy, my... \x01",
            "Youngsters nowadays\x01",
            "lack in guts, eh?\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_23D2")

    ChrTalk(
        0x102,
        (
            "#00105FWhat do you mean...?\x02\x03",
            "#00106FYou're not planning to\x01",
            "escape again, are you...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2583")

    label("loc_23D2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2442")

    ChrTalk(
        0x103,
        (
            "#00205FWhat do you mean...?\x02\x03",
            "#00203FYou are not planning to\x01",
            "escape again, are you...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2583")

    label("loc_2442")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_24BB")

    ChrTalk(
        0x104,
        (
            "#00305FWhat's the meanin' of that...?\x02\x03",
            "#00306FDon't tell me you're\x01",
            "plannin' to run away again?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2583")

    label("loc_24BB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2529")

    ChrTalk(
        0x109,
        (
            "#10105FW-What do you mean?\x02\x03",
            "#10101FYou're not planning to\x01",
            "escape again, are you...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2583")

    label("loc_2529")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2583")

    ChrTalk(
        0x105,
        (
            "#10305FEeeh...?\x02\x03",
            "#10302FYou seem to be planning\x01",
            "to escape again, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2583")


    ChrTalk(
        0x9,
        "#5PPlan...? Hah!!\x02",
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
            "#5P...Once this train gets to\x01",
            "Altair City, you're mine!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PThe Republic's my\x01",
            "home turf, see?\x02",
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
            "#00006FO-Outta here...\x02\x03",
            "#00011FYou're still planning\x01",
            "on running this late\x01",
            "in the game!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hah...! \x01",
            "Fine then, listen up!\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x9,
        (
            "#5P#5SAs long as this continent exists...\x01",
            "Everything can be my escape route!#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x9,
        (
            "#5P#5SAs long as you guys are on\x01",
            "my heels... You have no\x01",
            "hope of catching me!#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x9,
        (
            "#5P#5SYou understand\x01",
            "now, fools!?#3S\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Oooh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "We'll follow you!!\x02",
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
            "running until the bitter end.\x02\x03",
            "I'm afraid this old lady will\x01",
            "really go through with it, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A1,
        (
            "U-Us too... We can't\x01",
            "let them run away!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A1,
        (
            "This is an important duty\x01",
            "entrusted to me by the Inspector!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_29DD")

    ChrTalk(
        0x102,
        "#00105FMr. Raymond...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2AD2")

    label("loc_29DD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A1F")

    ChrTalk(
        0x103,
        (
            "#00205FMr. Raymond...\x01",
            "...You are right.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AD2")

    label("loc_2A1F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A5D")

    ChrTalk(
        0x104,
        "#00302FEh eh, you show some spirit.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2AD2")

    label("loc_2A5D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A9B")

    ChrTalk(
        0x109,
        (
            "#10102FMr. Raymond...\x01",
            "That's right!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AD2")

    label("loc_2A9B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2AD2")

    ChrTalk(
        0x105,
        (
            "#10302FEeh...\x01",
            "Hu hu, that's nice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AD2")


    ChrTalk(
        0x101,
        (
            "#00001FIf that's the case...\x01",
            "We have no choice but\x01",
            "to capture them here.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B50")
    SetChrChipByIndex(0x102, 0x22)
    SetChrSubChip(0x102, 0x0)
    Jump("loc_2BBF")

    label("loc_2B50")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B6D")
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x0)
    Jump("loc_2BBF")

    label("loc_2B6D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B8A")
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    Jump("loc_2BBF")

    label("loc_2B8A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2BA7")
    SetChrChipByIndex(0x109, 0x25)
    SetChrSubChip(0x109, 0x0)
    Jump("loc_2BBF")

    label("loc_2BA7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2BBF")
    SetChrChipByIndex(0x105, 0x26)
    SetChrSubChip(0x105, 0x0)

    label("loc_2BBF")

    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x1A1, 0x27)
    SetChrSubChip(0x1A1, 0x0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00007FLet's go everyone!\x01",
            "We'll disable them!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P...How many times are you\x01",
            "gonna make me say it?\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x9,
        (
            "#5P#5SIf you guys can really catch me, \x01",
            "JUST GO AHEAD AND TRY!!#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x9,
        "#5P#5S──C'mon you guys, get 'em!!#3S\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle("BattleInfo_310", 0x30200011, 0x0, 0x0, 0x21, 0xFF)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D12")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D1C")

    label("loc_2D12")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D1C")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E17")
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    Jump("loc_2E31")

    label("loc_2E17")

    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    label("loc_2E31")

    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -41450, -10, -50, 90)
    SetChrPos(0x101, -36930, 0, -130, 270)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2E93")
    SetChrPos(0x102, -35010, -90, 810, 270)
    SetChrChipByIndex(0x102, 0x22)
    SetChrSubChip(0x102, 0x0)
    Jump("loc_2F46")

    label("loc_2E93")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2EC1")
    SetChrPos(0x103, -35010, -90, 810, 270)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x0)
    Jump("loc_2F46")

    label("loc_2EC1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2EEF")
    SetChrPos(0x104, -35010, -90, 810, 270)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    Jump("loc_2F46")

    label("loc_2EEF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F1D")
    SetChrPos(0x109, -35010, -90, 810, 270)
    SetChrChipByIndex(0x109, 0x25)
    SetChrSubChip(0x109, 0x0)
    Jump("loc_2F46")

    label("loc_2F1D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F46")
    SetChrPos(0x105, -35010, -90, 810, 270)
    SetChrChipByIndex(0x105, 0x26)
    SetChrSubChip(0x105, 0x0)

    label("loc_2F46")

    SetChrPos(0x1A1, -35640, -130, -1310, 270)
    SetChrChipByIndex(0x1A1, 0x27)
    SetChrSubChip(0x1A1, 0x0)
    PlayBGM("ed7111", 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#00006F*phew*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A1,
        "Somehow w-we did it...\x02",
    )

    CloseMessageWindow()
    Fade(500)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2FCF")
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    Jump("loc_303E")

    label("loc_2FCF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2FEC")
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    Jump("loc_303E")

    label("loc_2FEC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3009")
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Jump("loc_303E")

    label("loc_3009")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3026")
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    Jump("loc_303E")

    label("loc_3026")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_303E")
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)

    label("loc_303E")

    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x1A1, 0xFF)
    SetChrSubChip(0x1A1, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3168")

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
            "#00003F(Uhhm, maybe attacking the old \x01",
            "lady too was a little too much...?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PY-You guys...\x01",
            "You won't get away with thiiis...\x02",
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
    Jump("loc_3329")

    label("loc_3168")

    OP_2C(0x81, 0x1)

    ChrTalk(
        0x9,
        (
            "#5PN-No way...\x01",
            "This cannot beee...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PG-Guys, pull yourselves together!\x01",
            "Show 'em you've got guts!\x02",
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
        (
            "#5PYou...\x01",
            "How dare you!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PIf it's like this, then\x01",
            "I'll run away by jumping\x01",
            "off the train...!!\x02",
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
            "get out of that unscathed,\x01",
            "so please just stop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PUgh...!!\x02",
    )

    CloseMessageWindow()

    label("loc_3329")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_33A4")

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
    Jump("loc_356E")

    label("loc_33A4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3414")

    ChrTalk(
        0x103,
        (
            "#00206F...She is\x01",
            "insanely tough.\x02\x03",
            "#00200FThe terrorists are all\x01",
            "exhausted, and yet...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_356E")

    label("loc_3414")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_348D")

    ChrTalk(
        0x104,
        (
            "#00306FJeez, a very tenacious\x01",
            "grandma as always.\x02\x03",
            "#00301FAnd the terrorists\x01",
            "are all exhausted.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_356E")

    label("loc_348D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_34F5")

    ChrTalk(
        0x109,
        (
            "#10106FUgh...how tenacious.\x02\x03",
            "#10101FIsn't she tougher\x01",
            "than the terrorists...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_356E")

    label("loc_34F5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_356E")

    ChrTalk(
        0x105,
        (
            "#10302FHa ha...\x01",
            "What a hearty madame.\x02\x03",
            "#10300FIsn't she definitely stronger\x01",
            "than the terrorists...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_356E")


    ChrTalk(
        0x101,
        (
            "#00006FYeah...seriously.\x02\x03",
            "#00000FAlright then, Mr. Raymond.\x01",
            "What should we do with them?\x01\x02",
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
            "I guess contacting the Republican Army\x01",
            "and handing them over would be good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FWell... They all look\x01",
            "to be Republicans,\x01",
            "so I think that's best.\x02\x03",
            "#00000FAlright. Let's ask the conductor\x01",
            "to contact them for us.\x02",
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

    # Function_14_1E15 end

    def Function_15_3710(): pass

    label("Function_15_3710")

    OP_95(0xFE, -35330, -200, -1940, 4000, 0x0)
    OP_95(0xFE, -36930, 0, -130, 4000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_15_3710 end

    def Function_16_3740(): pass

    label("Function_16_3740")

    OP_95(0xFE, -34700, -190, -1850, 4000, 0x0)
    OP_95(0xFE, -35010, -90, 810, 4000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_16_3740 end

    def Function_17_3770(): pass

    label("Function_17_3770")

    OP_95(0xFE, -34350, -530, -2710, 4000, 0x0)
    OP_95(0xFE, -35640, -130, -1310, 4000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_17_3770 end

    SaveToFile()

Try(main)
