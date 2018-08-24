from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "昇降機",                 # 1
        "SE制御",                 # 2
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
        "#00105F#6P#40WW-What's this...?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_306")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2C3")
    OP_FC(0xC)
    Jump("loc_2C6")

    label("loc_2C3")

    OP_FC(0x6)

    label("loc_2C6")


    ChrTalk(
        0x109,
        (
            "#10105F#13P#40WThe situation throughout\x01",
            "Crossbell...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E0")

    label("loc_306")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_373")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_330")
    OP_FC(0xC)
    Jump("loc_333")

    label("loc_330")

    OP_FC(0x6)

    label("loc_333")


    ChrTalk(
        0x106,
        (
            "#10712F#13P#40WThe situation throughout\x01",
            "Crossbell...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E0")

    label("loc_373")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3E0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_39D")
    OP_FC(0xC)
    Jump("loc_3A0")

    label("loc_39D")

    OP_FC(0x6)

    label("loc_3A0")


    ChrTalk(
        0x10A,
        (
            "#00605F#13P#40WThe situation throughout\x01",
            "Crossbell, huh...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E0")

    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00306F#6P#40WNo... It's not just\x01",
            "that.\x02\x03",
            "#00301FPast events seem to be\x01",
            "mixed in with them...?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00208F#12P#40WFragments of the real\x01",
            "world...\x02\x03",
            "#00201FA linked fate surpassing\x01",
            "space and time...?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_524")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4DD")
    OP_FC(0xC)
    Jump("loc_4E0")

    label("loc_4DD")

    OP_FC(0x6)

    label("loc_4E0")


    ChrTalk(
        0x105,
        (
            "#10406F#13P#40WWe can't even say it's\x01",
            "impossible anymore.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_601")

    label("loc_524")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_596")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_54E")
    OP_FC(0xC)
    Jump("loc_551")

    label("loc_54E")

    OP_FC(0x6)

    label("loc_551")


    ChrTalk(
        0x10A,
        (
            "#00606F#13P#40WIt can't be... But I'm\x01",
            "not so sure anymore.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_601")

    label("loc_596")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_601")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5C0")
    OP_FC(0xC)
    Jump("loc_5C3")

    label("loc_5C0")

    OP_FC(0x6)

    label("loc_5C3")


    ChrTalk(
        0x106,
        (
            "#10706F#13P#40W...It appears that it's\x01",
            "not impossible...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_601")

    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00003F#6P#40W...The Sept-Terrion of\x01",
            "Zero...\x02\x03",
            "#00001FThe Azure Tree is its\x01",
            "perfect form...\x02",
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

    def lambda_757():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_757)
    Sleep(50)

    def lambda_767():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_767)
    Sleep(50)

    def lambda_777():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_777)
    Sleep(50)

    def lambda_787():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_787)
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
        "#00007F#6P#4S...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00310F#12PW-What the!?\x02",
    )

    CloseMessageWindow()

    def lambda_B7C():
        OP_93(0xF4, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_B7C)
    Sleep(50)

    def lambda_B8C():
        OP_93(0xF5, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_B8C)
    Sleep(50)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)

    ChrTalk(
        0x102,
        (
            "#00108F#12PThat just now was from\x01",
            "when we entered the Fort\x01",
            "of Sun's basement...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#6PNo, Estelle and Joshua\x01",
            "weren't there...\x02\x03",
            "#00208F...Also...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#6P............\x02",
    )

    CloseMessageWindow()
    OP_63(0xF4, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CE7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CB9")
    OP_FC(0xFFFA)
    Jump("loc_CBC")

    label("loc_CB9")

    OP_FC(0xFFF4)

    label("loc_CBC")


    ChrTalk(
        0x10A,
        "#00601F#13PWhat... What's wrong?\x02",
    )

    CloseMessageWindow()
    Jump("loc_D92")

    label("loc_CE7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D39")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D11")
    OP_FC(0xFFFA)
    Jump("loc_D14")

    label("loc_D11")

    OP_FC(0xFFF4)

    label("loc_D14")


    ChrTalk(
        0x109,
        "#10101F#13PW-What's wrong?\x02",
    )

    CloseMessageWindow()
    Jump("loc_D92")

    label("loc_D39")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D92")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D63")
    OP_FC(0xFFFA)
    Jump("loc_D66")

    label("loc_D63")

    OP_FC(0xFFF4)

    label("loc_D66")


    ChrTalk(
        0x106,
        (
            "#10701F#13PIs something the\x01",
            "matter...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D92")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E07")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DBC")
    OP_FC(0xFFFA)
    Jump("loc_DBF")

    label("loc_DBC")

    OP_FC(0xFFF4)

    label("loc_DBF")


    ChrTalk(
        0x105,
        (
            "#10401F#13P...It looks like you saw\x01",
            "something we\x01",
            "couldn't...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ED7")

    label("loc_E07")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E6F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E31")
    OP_FC(0xFFFA)
    Jump("loc_E34")

    label("loc_E31")

    OP_FC(0xFFF4)

    label("loc_E34")


    ChrTalk(
        0x106,
        (
            "#10701F#13PDid you see something we\x01",
            "couldn't...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ED7")

    label("loc_E6F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ED7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E99")
    OP_FC(0xFFFA)
    Jump("loc_E9C")

    label("loc_E99")

    OP_FC(0xFFF4)

    label("loc_E9C")


    ChrTalk(
        0x109,
        (
            "#10101F#13PDid you see something\x01",
            "that we couldn't...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ED7")

    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00006F#5P...Yeah, just for a\x01",
            "moment.\x02\x03",
            "#00008FThough it's faint... I\x01",
            "feel I understand what\x01",
            "KeA's true power is.\x02",
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
