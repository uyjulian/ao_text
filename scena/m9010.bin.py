﻿from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m9010.bin",                # FileName
        "m9010",                    # MapName
        "m9010",                    # Location
        0x0000,                     # MapIndex
        "ed7353",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x2A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "m9010",                  # 0
        "Elevator",                 # 1
        "SE control",                 # 2
    ))

    DeclNpc(0,       0,       0,       0,    508,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(216, 0)                                        # 0

    ScpFunction((
        "Function_0_D8",           # 00, 0
        "Function_1_E8",           # 01, 1
        "Function_2_ED",           # 02, 2
    ))


    def Function_0_D8(): pass

    label("Function_0_D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_E7")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_E7")

    Return()

    # Function_0_D8 end

    def Function_1_E8(): pass

    label("Function_1_E8")

    OP_F0(0x1, 0x320)
    Return()

    # Function_1_E8 end

    def Function_2_ED(): pass

    label("Function_2_ED")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(1032)
    LoadEffect(0x0, "event/ev17066.eff")
    LoadEffect(0x1, "event/ev17065.eff")
    SetChrPos(0x101, -900, 0, 1500, 315)
    SetChrPos(0x102, 900, 0, 1500, 45)
    SetChrPos(0x103, -1600, 0, 0, 270)
    SetChrPos(0x104, 1600, 0, 0, 90)
    SetChrPos(0xF4, -900, 0, -1500, 225)
    SetChrPos(0xF5, 900, 0, -1500, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(0, 1550, 0, 0)
    MoveCamera(245, 51, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(34950, 0)
    OP_68(0, 1550, 0, 8000)
    MoveCamera(325, 21, 0, 8000)
    OP_6E(1000, 8000)
    SetCameraDistance(9870, 8000)
    OP_78(0x0, 0x8)
    SetChrPos(0x8, 0, 0, 0, 0)
    SetChrFlags(0x8, 0x4)
    Sound(1032, 2, 100, 0)
    Sound(112, 2, 30, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    MoveCamera(350, 21, 0, 30000)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#00105F#6P#40WTh-This is……?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2C2")
    OP_FC(0xC)
    Jump("loc_2C5")

    label("loc_2C2")

    OP_FC(0x6)

    label("loc_2C5")


    ChrTalk(
        0x109,
        "#10105F#13P#40WCrossbell situation around the country … …?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B8")

    label("loc_2F9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_35A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_323")
    OP_FC(0xC)
    Jump("loc_326")

    label("loc_323")

    OP_FC(0x6)

    label("loc_326")


    ChrTalk(
        0x106,
        "#10712F#13P#40WCrossbell situation around the country … …?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B8")

    label("loc_35A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_384")
    OP_FC(0xC)
    Jump("loc_387")

    label("loc_384")

    OP_FC(0x6)

    label("loc_387")


    ChrTalk(
        0x10A,
        "#00605F#13P#40WCrossbell situation in various parts …?\x02",
    )

    CloseMessageWindow()

    label("loc_3B8")

    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00306F#6P#40WNo … not only that.\x02\x03",
            "#00301FEven things like past events\x01",
            "You seem to be misunderstood … ….?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00208F#12P#40WReal world fragment ……\x02\x03",
            "#00201FBeyond the spacetime\x01",
            "Causal linkage … ….?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4F2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4AA")
    OP_FC(0xC)
    Jump("loc_4AD")

    label("loc_4AA")

    OP_FC(0x6)

    label("loc_4AD")


    ChrTalk(
        0x105,
        (
            "#10406F#13P#40W…… What is not possible\x01",
            "It sounds like it can not be said.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CD")

    label("loc_4F2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_55E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_51C")
    OP_FC(0xC)
    Jump("loc_51F")

    label("loc_51C")

    OP_FC(0x6)

    label("loc_51F")


    ChrTalk(
        0x10A,
        (
            "#00606F#13P#40WFoolishly well\x01",
            "It seems impossible to say.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CD")

    label("loc_55E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5CD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_588")
    OP_FC(0xC)
    Jump("loc_58B")

    label("loc_588")

    OP_FC(0x6)

    label("loc_58B")


    ChrTalk(
        0x106,
        (
            "#10706F#13P#40W…… What is not possible\x01",
            "It seems unlikely to be … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CD")

    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00003F#6P#40W…… \"Treasure of Zero\" ……\x02\x03",
            "#00001FAs its finished form\x01",
            "\"A big blue tree\" ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(10, 1650, 1300, 3000)
    MoveCamera(357, 13, 0, 3000)
    OP_6E(1000, 3000)
    SetCameraDistance(9000, 3000)
    Sleep(1500)
    PlayEffect(0x0, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    Sound(921, 0, 100, 0)
    OP_6F(0x79)
    Sound(934, 0, 100, 0)
    Sound(928, 0, 50, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_717():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_717)
    Sleep(50)

    def lambda_727():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_727)
    Sleep(50)

    def lambda_737():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_737)
    Sleep(50)

    def lambda_747():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_747)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    Sound(829, 0, 100, 0)
    SetCameraDistance(8000, 2000)
    StopSound(1032, 2000, 90)
    StopSound(112, 2000, 20)
    VolumeBGM(0x46, 0x3E8)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    Sleep(300)
    Sound(824, 0, 50, 0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis293.itp")
    OP_CB(0x0, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(800)
    Sound(824, 0, 50, 0)
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis294.itp")
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x1, 0x0, 0x0)
    Sleep(800)
    Sound(824, 0, 50, 0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis295.itp")
    OP_CB(0x0, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x1, 0x1, 0x0)
    Sleep(800)
    Sound(824, 0, 50, 0)
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis333.itp")
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x1, 0x0, 0x0)
    Sleep(800)
    Sound(824, 0, 50, 0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis334.itp")
    OP_CB(0x0, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x1, 0x1, 0x0)
    Sleep(800)
    Sound(824, 0, 100, 0)
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis346.itp")
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x1, 0x0, 0x0)
    Sleep(800)
    Sound(829, 0, 100, 0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    Sound(1032, 2, 100, 0)
    Sound(112, 2, 30, 0)
    SetCameraDistance(9000, 2000)
    FadeToBright(2000, 16777215)
    VolumeBGM(0x64, 0x3E8)
    Sleep(1500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#00007F#6P#4S……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00310F#12PWhat is it! Is it?\x02",
    )

    CloseMessageWindow()

    def lambda_B42():
        OP_93(0xF4, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_B42)
    Sleep(50)

    def lambda_B52():
        OP_93(0xF5, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_B52)
    Sleep(50)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)

    ChrTalk(
        0x102,
        (
            "#00108F#12PNow is the \"Fort of the Sun\"\x01",
            "When I entered the basement …! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#6PNo, the esters\x01",
            "I was not with him ……\x02\x03",
            "#00208F……in addition………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#6P………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0xF4, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CAF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C82")
    OP_FC(0xFFFA)
    Jump("loc_C85")

    label("loc_C82")

    OP_FC(0xFFF4)

    label("loc_C85")


    ChrTalk(
        0x10A,
        "#00601F#13PWhat was … what?\x02",
    )

    CloseMessageWindow()
    Jump("loc_D5C")

    label("loc_CAF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D08")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CD9")
    OP_FC(0xFFFA)
    Jump("loc_CDC")

    label("loc_CD9")

    OP_FC(0xFFF4)

    label("loc_CDC")


    ChrTalk(
        0x109,
        "#10101F#13PWell, what happened?\x02",
    )

    CloseMessageWindow()
    Jump("loc_D5C")

    label("loc_D08")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D5C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D32")
    OP_FC(0xFFFA)
    Jump("loc_D35")

    label("loc_D32")

    OP_FC(0xFFF4)

    label("loc_D35")


    ChrTalk(
        0x106,
        "#10701F#13PWhat happened……?\x02",
    )

    CloseMessageWindow()

    label("loc_D5C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DD4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D86")
    OP_FC(0xFFFA)
    Jump("loc_D89")

    label("loc_D86")

    OP_FC(0xFFF4)

    label("loc_D89")


    ChrTalk(
        0x105,
        (
            "#10401F#13P…… Apparently to us\x01",
            "You seem to have seen something you can not see?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EAF")

    label("loc_DD4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E40")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DFE")
    OP_FC(0xFFFA)
    Jump("loc_E01")

    label("loc_DFE")

    OP_FC(0xFFF4)

    label("loc_E01")


    ChrTalk(
        0x106,
        (
            "#10701F#13PWhat we can not see\x01",
            "You saw it … …?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EAF")

    label("loc_E40")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EAF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E6A")
    OP_FC(0xFFFA)
    Jump("loc_E6D")

    label("loc_E6A")

    OP_FC(0xFFF4)

    label("loc_E6D")


    ChrTalk(
        0x109,
        (
            "#10101F#13PWhat we can not see\x01",
            "Did you see it …?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EAF")

    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00006F#5P…… Oh, for a moment.\x02\x03",
            "#00008FDazzling#2RA rag#While\x01",
            "Ka'ah's true power is what\x01",
            "I feel I understood.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 1550, 0, 0)
    MoveCamera(0, 25, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(13000, 0)
    OP_0D()
    OP_68(0, -8750, 0, 3000)
    Sleep(1000)
    StopSound(1032, 2000, 90)
    StopSound(112, 2000, 20)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(0, -8750, 0, 0)
    Sleep(1000)
    SetScenarioFlags(0x22, 0)
    NewScene("m9011", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_ED end

    SaveToFile()

Try(main)
