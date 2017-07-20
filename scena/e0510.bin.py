from ScenarioHelper import *

def main():
    CreateScenaFile(
        "e0510.bin",                # FileName
        "e0510",                    # MapName
        "e0510",                    # Location
        0x00A1,                     # MapIndex
        "ed7565",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0xFF,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 161, 0, 1, 0, 2],
    )

    BuildStringList((
        "e0510",                  # 0
        "Erie",                 # 1
        "Noel",                 # 2
        "Randy",               # 3
        "Crew salsa",           # 4
        "Citizen",                   # 5
        "tourist",                 # 6
        "tourist",                 # 7
        "Marsun",               # 8
        "Lima",                   # 9
        "corona",                 # 10
        "Franc",                 # 11
        "Cecil",                 # 12
        "Ilia",                 # 13
        "Lisha",               # 14
        "Shuri",                 # 15
        "Marybele",             # 16
        "Zeit",               # 17
        "SE control",                 # 18
    ))

    AddCharChip((
        "chr/ch00100.itc",                   # 00
        "chr/ch02900.itc",                   # 01
        "chr/ch00302.itc",                   # 02
        "chr/ch28400.itc",                   # 03
        "chr/ch33002.itc",                   # 04
        "chr/ch20402.itc",                   # 05
        "chr/ch22102.itc",                   # 06
        "chr/ch26202.itc",                   # 07
        "chr/ch22702.itc",                   # 08
        "chr/ch20702.itc",                   # 09
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

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    388,  0x0, 1,   2,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(4294967196, 0,       4294951876, 0,    389,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(4294964846, 150,     4294963497, 180,  453,  0x0, 0,   4,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(4294964846, 150,     4294960847, 180,  453,  0x0, 0,   5,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(4294963846, 150,     4294960847, 180,  453,  0x0, 0,   6,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(4294964247, 150,     4294955946, 180,  389,  0x0, 0,   7,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(4294963546, 150,     4294955946, 180,  389,  0x0, 0,   9,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(4294965046, 150,     4294955946, 180,  389,  0x0, 0,   8,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(844, 0)                                        # 0

    ScpFunction((
        "Function_0_34C",          # 00, 0
        "Function_1_3FC",          # 01, 1
        "Function_2_4FF",          # 02, 2
        "Function_3_554",          # 03, 3
        "Function_4_8C2",          # 04, 4
        "Function_5_B46",          # 05, 5
        "Function_6_E70",          # 06, 6
        "Function_7_1005",         # 07, 7
        "Function_8_1100",         # 08, 8
        "Function_9_1188",         # 09, 9
        "Function_10_120E",        # 0A, 10
        "Function_11_13D1",        # 0B, 11
        "Function_12_15AA",        # 0C, 12
        "Function_13_1627",        # 0D, 13
        "Function_14_2967",        # 0E, 14
        "Function_15_38B3",        # 0F, 15
        "Function_16_38DB",        # 10, 16
        "Function_17_3903",        # 11, 17
    ))


    def Function_0_34C(): pass

    label("Function_0_34C")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_384"),
        (1, "loc_390"),
        (2, "loc_39C"),
        (3, "loc_3A8"),
        (4, "loc_3B4"),
        (5, "loc_3C0"),
        (6, "loc_3CC"),
        (SWITCH_DEFAULT, "loc_3D8"),
    )


    label("loc_384")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3E4")

    label("loc_390")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3E4")

    label("loc_39C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3E4")

    label("loc_3A8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3E4")

    label("loc_3B4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3E4")

    label("loc_3C0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3E4")

    label("loc_3CC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3E4")

    label("loc_3D8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3E4")

    label("loc_3E4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3FB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3E4")

    label("loc_3FB")

    Return()

    # Function_0_34C end

    def Function_1_3FC(): pass

    label("Function_1_3FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4EF")
    SetChrPos(0x8, 630, -1000, 9000, 270)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x9, -620, -1000, 9000, 90)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0xA, 3250, 150, -9100, 180)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x6)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 0x7)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0x8)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x9)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x10)
    SetChrSubChip(0x10, 0x2)

    label("loc_4EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_4FE")
    ClearScenarioFlags(0x22, 0)
    Event(0, 17)

    label("loc_4FE")

    Return()

    # Function_1_3FC end

    def Function_2_4FF(): pass

    label("Function_2_4FF")

    Sound(480, 1, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_533")
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_533")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_553")
    SetChrSubChip(0xA, 0x1)
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_553")

    Return()

    # Function_2_4FF end

    def Function_3_554(): pass

    label("Function_3_554")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56B")
    Call(0, 13)
    Return()

    label("loc_56B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_57C")
    Jump("loc_8BE")

    label("loc_57C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_58A")
    Jump("loc_8BE")

    label("loc_58A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_598")
    Jump("loc_8BE")

    label("loc_598")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_5A8")
    Jump("loc_8BE")

    label("loc_5A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_5B6")
    Jump("loc_8BE")

    label("loc_5B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_5C4")
    Jump("loc_8BE")

    label("loc_5C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_5D2")
    Jump("loc_8BE")

    label("loc_5D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_5E0")
    Jump("loc_8BE")

    label("loc_5E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_8BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F8")
    Jump("loc_8BE")

    label("loc_5F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_847")

    ChrTalk(
        0x8,
        (
            "#00100FThings that came to a vacation so much,\x01",
            "If you do not enjoy it is a loss.\x02\x03",
            "#00104FSurely bell, surprise a lot\x01",
            "I was talking about preparing … ….\x02\x03",
            "#00102FHuhu, if you think so\x01",
            "Maybe it has become quite fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FSurprise … ….\x01",
            "I am a little worried as I am.\x02\x03",
            "#00003FMichelam total weights welcome to come\x01",
            "If it is something like that,\x01",
            "It will surely shrink.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00109FNo matter how bell likes flashy\x01",
            "I'm preparing something so far …\x02\x03",
            "#00103FI can not say even if I do not do it.\x02\x03",
            "#00102FSomething that is not at all a funny thing\x01",
            "Let's pray to the goddess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F(Well, I worry … …)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_8BE")

    label("loc_847")


    ChrTalk(
        0x8,
        (
            "#00103FWell, even so\x01",
            "I wonder what the surprise of Bell is.\x02\x03",
            "#00111F…… I do not have to be funny.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8BE")

    TalkEnd(0xFE)
    Return()

    # Function_3_554 end

    def Function_4_8C2(): pass

    label("Function_4_8C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8D9")
    Call(0, 13)
    Return()

    label("loc_8D9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_8EA")
    Jump("loc_B42")

    label("loc_8EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_8F8")
    Jump("loc_B42")

    label("loc_8F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_906")
    Jump("loc_B42")

    label("loc_906")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_916")
    Jump("loc_B42")

    label("loc_916")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_924")
    Jump("loc_B42")

    label("loc_924")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_932")
    Jump("loc_B42")

    label("loc_932")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_940")
    Jump("loc_B42")

    label("loc_940")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_94E")
    Jump("loc_B42")

    label("loc_94E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_B42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_966")
    Jump("loc_B42")

    label("loc_966")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AC8")

    ChrTalk(
        0x9,
        (
            "#10105FBy the way, Sergey manager\x01",
            "I regret that I could not come together.\x02\x03",
            "#10106FEnjoy it,\x01",
            "I was saying, but\x01",
            "I guess you're sorry ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FThe section chief is also quite a busy guy ……\x02\x03",
            "#00002FHahaha, maybe just\x01",
            "I can see a private figure\x01",
            "It may be only embarrassing though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#10109FHaha, that is surprising and funny.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_B42")

    label("loc_AC8")


    ChrTalk(
        0x9,
        (
            "#10103FSergey manager\x01",
            "I regret that I could not come together.\x02\x03",
            "#10102FAround this time, one in support section\x01",
            "Do you smoke a cigarette?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B42")

    TalkEnd(0xFE)
    Return()

    # Function_4_8C2 end

    def Function_5_B46(): pass

    label("Function_5_B46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B5D")
    Call(0, 14)
    Return()

    label("loc_B5D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_B6E")
    Jump("loc_E6C")

    label("loc_B6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_B7C")
    Jump("loc_E6C")

    label("loc_B7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_B8A")
    Jump("loc_E6C")

    label("loc_B8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_B98")
    Jump("loc_E6C")

    label("loc_B98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_BA6")
    Jump("loc_E6C")

    label("loc_BA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_BB4")
    Jump("loc_E6C")

    label("loc_BB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_BC2")
    Jump("loc_E6C")

    label("loc_BC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_E6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BDA")
    Jump("loc_E6C")

    label("loc_BDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DE4")

    ChrTalk(
        0xA,
        (
            "#00303FWell, I guess it's kind of spicy\x01",
            "It is not my character.\x02\x03",
            "#00301FIf this is the case, today is a fresh tattoo\x01",
            "Let's enjoy Michelam!\x02\x03",
            "#00309FLloyd, you can go out with a night pamp?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FWell, well, leave it to Randy\x01",
            "It will be, but if that is OK.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00306FWhat, it is passive.\x02\x03",
            "#00309FBecause you also like the material,\x01",
            "I feel like I have to break away my little brother character\x01",
            "Let's be in Ikei.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FWell, I do not know the meaning … …\x02\x03",
            "#00000F(… but, as usual\x01",
            "It seems they came back. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_E64")

    label("loc_DE4")


    ChrTalk(
        0xA,
        (
            "#00305FOh, that's right.\x01",
            "I wonder if I buy a souvenir …\x02\x03",
            "#00304FIt was a story to be promoted,\x01",
            "Would you mind even celebrating items somewhere?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E64")

    TalkEnd(0xFE)
    SetChrSubChip(0xA, 0x1)
    Return()

    label("loc_E6C")

    TalkEnd(0xFE)
    Return()

    # Function_5_B46 end

    def Function_6_E70(): pass

    label("Function_6_E70")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_E81")
    Jump("loc_1001")

    label("loc_E81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_E8F")
    Jump("loc_1001")

    label("loc_E8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_E9D")
    Jump("loc_1001")

    label("loc_E9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_1001")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F74")

    ChrTalk(
        0xB,
        (
            "Using today's water bus,\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "To everyone Mary Bell\x01",
            "Have you been invited?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Short temporary until Michelin,\x01",
            "A calm journey that is shaken by the waves\x01",
            "Please enjoy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1001")

    label("loc_F74")


    ChrTalk(
        0xB,
        (
            "When you get drunk,\x01",
            "On the deck with a view of the distant landscape\x01",
            "You should be distracted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "There is also preparation for a sickness stop\x01",
            "Please do not worry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1001")

    TalkEnd(0xFE)
    Return()

    # Function_6_E70 end

    def Function_7_1005(): pass

    label("Function_7_1005")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_10FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10A8")

    ChrTalk(
        0xC,
        (
            "As independent advocacy at the trade meeting\x01",
            "I was really surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "How is Dieter?\x01",
            "Is it going to make it happen …?\x01",
            "I am celebrating with pleasure.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_10FC")

    label("loc_10A8")


    ChrTalk(
        0xC,
        (
            "How is Dieter?\x01",
            "Is it going to realize independence ……\x01",
            "I am celebrating with pleasure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10FC")

    TalkEnd(0xFE)
    Return()

    # Function_7_1005 end

    def Function_8_1100(): pass

    label("Function_8_1100")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_1184")

    ChrTalk(
        0xD,
        (
            "Crossbell trip that I saw to my dreams,\x01",
            "Recreation area Michelin theme park!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Wow, I'm looking forward to it.\x01",
            "I will have a full eye with her!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1184")

    TalkEnd(0xFE)
    Return()

    # Function_8_1100 end

    def Function_9_1188(): pass

    label("Function_9_1188")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_120A")

    ChrTalk(
        0xE,
        (
            "Personally it is restaurant and\x01",
            "I'd like to go out with a boutique, ne ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Uhufu, today to the curry\x01",
            "I'm going to have a good time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_120A")

    TalkEnd(0xFE)
    Return()

    # Function_9_1188 end

    def Function_10_120E(): pass

    label("Function_10_120E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_121F")
    Jump("loc_13CD")

    label("loc_121F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_122D")
    Jump("loc_13CD")

    label("loc_122D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_123B")
    Jump("loc_13CD")

    label("loc_123B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1249")
    Jump("loc_13CD")

    label("loc_1249")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_13CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1348")

    ChrTalk(
        0xF,
        (
            "Is the crossbell independent?\x01",
            "As expected, Mayor Dieter\x01",
            "I do not think anything else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "In an easy way never\x01",
            "It probably is not … …\x01",
            "His words have a dream.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "The mayor surely crossbells\x01",
            "It will light up brightly.\x01",
            "I feel like that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_13CD")

    label("loc_1348")


    ChrTalk(
        0xF,
        (
            "Oops, with my family at large\x01",
            "Even though I came to play\x01",
            "I wonder if there was such a story either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Today in Lima and Corona\x01",
            "You have to have lots of fun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13CD")

    TalkEnd(0xFE)
    Return()

    # Function_10_120E end

    def Function_11_13D1(): pass

    label("Function_11_13D1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_13E2")
    Jump("loc_15A6")

    label("loc_13E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_13F0")
    Jump("loc_15A6")

    label("loc_13F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_13FE")
    Jump("loc_15A6")

    label("loc_13FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_140C")
    Jump("loc_15A6")

    label("loc_140C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_15A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1528")

    ChrTalk(
        0x11,
        (
            "After construction of the Orkis Tower is over\x01",
            "As my husband got a bonus,\x01",
            "I'm coming to a family trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "If it is true I am going to save money,\x01",
            "\"I want to do family service once in a while,\"\x01",
            "I was pushed by my husband.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "But it was nice to be able to come after all.\x01",
            "Because Lima is so pleased.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_15A6")

    label("loc_1528")


    ChrTalk(
        0x11,
        (
            "As my husband got a bonus,\x01",
            "I'm coming to a family trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Hehe, it was nice to come.\x01",
            "Because Lima is so pleased.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15A6")

    TalkEnd(0xFE)
    Return()

    # Function_11_13D1 end

    def Function_12_15AA(): pass

    label("Function_12_15AA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_15BB")
    Jump("loc_1623")

    label("loc_15BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_15C9")
    Jump("loc_1623")

    label("loc_15C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_15D7")
    Jump("loc_1623")

    label("loc_15D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_15E5")
    Jump("loc_1623")

    label("loc_15E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_1623")

    ChrTalk(
        0x10,
        (
            "Papa, look look! It is!\x01",
            "Fish flew away!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1623")

    TalkEnd(0xFE)
    Return()

    # Function_12_15AA end

    def Function_13_1627(): pass

    label("Function_13_1627")

    EventBegin(0x0)
    SoundLoad(3515)
    SoundLoad(3394)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10100.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00101.itp")
    Fade(500)
    OP_68(700, 200, 8350, 0)
    MoveCamera(15, 33, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(33390, 0)
    OP_64(0x8)
    OP_64(0x9)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x8, 500, -1000, 9000, 230)
    SetChrPos(0x9, -500, -1000, 9000, 80)
    SetChrPos(0x101, 1500, -1000, 8200, 315)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_1735():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1735)
    Sleep(50)

    def lambda_1745():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1745)
    WaitChrThread(0x9, 1)
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0x9,
        "#30W#3515VAh …… Lloyd.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_C9(0x1, 0x80000000)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sound(2189, 255, 100, 0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x8,
        "#30WDid you appear on the deck?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    ChrTalk(
        0x101,
        (
            "#00004F#12POh, in the wind.\x02\x03",
            "#00005FWell, was it obstructive?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#00108F#5POh, no …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10106F#5P…, that at the time of the Trade Council\x01",
            "About events ……\x02\x03",
            "#10113FAnd it's Mayor Dieter\x01",
            "I was talking about the proposal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#12PProposal …\x01",
            "Is it meant to be \"independent as a nation\"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00106F#5PYeah … for me\x01",
            "It is not quite a different person.\x02\x03",
            "#00108FNo way, my uncle\x01",
            "I was thinking about that … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10106F#5PI …\x01",
            "To be honest, I do not feel like anything else.\x02\x03",
            "#10108FTo the survival of the guard\x01",
            "Because it is a story involved … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#12PThat's right … … Empire and Republic\x01",
            "Reduce the scale of the Crossbell Guard\x01",
            "I am requesting it.\x02\x03",
            "#00013FInstead of using their troops\x01",
            "At the Tangram gate and the Belgard gate\x01",
            "Let's be stationed …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00103F#5PYeah ….\x02\x03",
            "#00108FWhatever you think from crossbell\x01",
            "To suck up further wealth\x01",
            "I can think only of collusion.\x02\x03",
            "#00101FAnd, perhaps\x01",
            "Merging aiming at gaps between each other\x01",
            "Hold the fruit all over … …\x02\x03",
            "#00106FThings that can only be thought of as preparation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12Psurely……\x02\x03",
            "#00001F… …, the mayor's suggestion\x01",
            "Is it also a plan to counter it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10103F#5PYes, as long as we are independent as a nation\x01",
            "I was suppressed by both countries so far\x01",
            "You can also enhance the equipment of the guard.\x02\x03",
            "#10101FNot just for the interpersonal armament,\x01",
            "To prevent invasion of other countries\x01",
            "Tanks and military flying boats, too.\x02\x03",
            "#10106F…… I think that way\x01",
            "It is a little disgusting though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#12PNoel …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00103F#5PBut my uncle's proposal\x01",
            "When it is said whether it is realistic or not … …\x02\x03",
            "#00108FImmediately from the empire and the republic,\x01",
            "A negative statement has been issued.\x02\x03",
            "#00100FHowever, Libert, Remiferia,\x01",
            "Alteria law countries etc favorably\x01",
            "Please give me a statement to receive ……\x02\x03",
            "#00106FHonestly, it's a frustrating situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#12PThat's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10113F#5P…… I invited you today.\x01",
            "Mr. Mariavel something\x01",
            "What do you think?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xE1, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "#00106F#11PIf anything she is\x01",
            "Now for the management of IBC\x01",
            "You seem to be concentrating.\x02\x03",
            "#00108FRegarding this proposal\x01",
            "It seems not to be involved.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x2D, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x9,
        (
            "#10106F#6PIs that so……\x02\x03",
            "#10108F…… Because it's a great opportunity\x01",
            "I thought that I would like to ask you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00103F#11PWell … I am also in the bell\x01",
            "There are quite a lot of things I want to hear ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00004F#12P── Hey, both of us.\x02\x03",
            "#00000FIt is such a moment so it is nothing.\x01",
            "Why do not you enjoy yourself?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_211F():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_211F)
    Sleep(50)

    def lambda_212F():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_212F)
    WaitChrThread(0x8, 2)
    WaitChrThread(0x9, 2)

    ChrTalk(
        0x8,
        "#00105F#5PHuh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#10105F#5P……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#12PWith rare vacations\x01",
            "You are staying at a Michelin hotel?\x02\x03",
            "And at that theme park\x01",
            "It's all you want to play.\x02\x03",
            "#00009FSuddenly empty my head\x01",
            "Is not it possible to do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#00106F#5P#30WBut,\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#10108F#5P#30W…… After such a thing … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#12PBecause there was such a thing.\x02\x03",
            "#00003FAhead, the situation of the crossbell\x01",
            "I do not know what will happen …\x02\x03",
            "Our work also\x01",
            "There is a high possibility that it will be serious.\x02\x03",
            "#00002FThat's why what …\x01",
            "I want to make \"memories\".\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x8,
        "#00112F#5PWell ……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#10114F#5PWell, that is …! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#12P(……Huh?\x01",
            "Why do you react so far? )\x02\x03",
            "#00012FHaha\x01",
            "I guess it was too harsh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10112F#5PI mean that it is too harsh ……\x02\x03",
            "#10108F(Erie-san … ….\x01",
            "Does it do on purpose? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00111F#5P(No……\x01",
            "The possibility of natural is high … …)\x02\x03",
            "#00113F─ ─ Well, Lloyd.\x02\x03",
            "#00112FThat \"memories\" is\x01",
            "Is not it someone specific?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#12PIs it? Of course it is ….\x02\x03",
            "#00000FI hope everyone can take a vacation\x01",
            "It is rare that it is.\x02\x03",
            "#00012FI can not tell the section chief, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#00113F#5PAhh ~ ~ っ …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10112F#5PThat's right, is not it?\x01",
            "That's why Lloyd's …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005F#12POh, perhaps I,\x01",
            "Have you taken out from a little while ago?\x02\x03",
            "#00006FBecause everyone seems depressed\x01",
            "Trying to cheer up even a little ─#500W─#30W#00011FAh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#10102F#5PPuff\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x8,
        (
            "#00114F#5PHahaha ……!\x02\x03",
            "#00116FOh, you really are … …\x01",
            "Is it called natural or clumsy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10109F#5PHuhu, what I was worrying about somehow\x01",
            "It became a foolish thing.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F#12P……It was bad.\x01",
            "I will wash my face and come back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00104F#5PHuhu, relax.#2RTo#Is not it?\x02\x03",
            "#00102F……I'm sorry.\x01",
            "We are a bit more\x01",
            "I could not read the air.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10102F#5PI agree……\x01",
            "After all if you go to vacation\x01",
            "I have to enjoy a lot of eyes!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#12PI see…\x01",
            "(For one, could you fulfill the purpose?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x8, 630, -1000, 9000, 270)
    SetChrPos(0x9, -620, -1000, 9000, 90)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    SetChrPos(0x0, 3000, -1000, 6500, 180)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x144, 2)
    EventEnd(0x5)
    Return()

    # Function_13_1627 end

    def Function_14_2967(): pass

    label("Function_14_2967")

    EventBegin(0x0)
    Fade(500)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00301.itp")
    OP_68(3170, 1300, -9560, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(34500, 0)
    OP_64(0xA)
    SetChrPos(0x101, 800, 0, -9770, 90)
    SetCameraDistance(34000, 1500)
    OP_9B(0x0, 0x101, 0x0, 0x3E8, 0x3E8, 0x0)
    OP_93(0x101, 0x2D, 0x1F4)
    OP_6F(0x79)
    OP_0D()
    SetChrSubChip(0xA, 0x0)
    Sleep(100)
    SetChrSubChip(0xA, 0x2)
    Sleep(200)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    Sound(2756, 255, 100, 0)

    AnonymousTalk(
        0xA,
        (
            "#30WYo, Lloyd\x02\x03",
            "#20WIndeed, Mary Bell\x01",
            "I'm pretty heavy.\x02\x03",
            "To a resort hotel in Michelin\x01",
            "All you can do is play the theme park.\x02\x03",
            "That's so incredibly generous\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xAC4)
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
            "#00002F#6PThat's true…\x02\x03",
            "#00008F….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#00302F#5PHaha\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xA)

    ChrTalk(
        0xA,
        (
            "#00304F#5PHey Lloyd\x02\x03",
            "#00300FBecause it seems to be different from kang\x01",
            "One thing to tell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PHuh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00303F#5PThe case of the terrorists who were killed\x02\x03",
            "#00301FTo my husband's doing something like that\x01",
            "When I'm shocked\x01",
            "Do not you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#6PT-that is\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00006F#6PNo, not exactly\x02\x03",
            "#00008FRandy, in her own thing\x01",
            "I feel like I'm dragging something.\x02\x03",
            "#00001FThat's all for my uncle\x01",
            "Is not it stuck?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    StopBGM(0xBB8)
    BeginChrThread(0x19, 1, 0, 15)

    ChrTalk(
        0xA,
        (
            "#00308F#5PI see…\x02\x03",
            "#00303F#30W…\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7534", 0)
    SetChrSubChip(0xA, 0x0)
    Sleep(150)
    SetChrSubChip(0xA, 0x1)
    SetCameraDistance(33000, 20000)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#00304F#5PI had a friend once\x02\x03",
            "One down from me\x01",
            "I was looking like a puppy ……\x02\x03",
            "#00300FProbably, I got to know it for the first time outside the group.\x01",
            "It is like a nigga that exists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6P…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00308F#5PThere are various\x01",
            "He's gone … …\x02\x03",
            "After all there was various\x01",
            "I got through the group and wandered.\x02\x03",
            "#00303FAnd reach the crossbell\x01",
            "Enter the guard … …\x01",
            "I met up with you ……\x02\x03",
            "#00302F…… But I'm in the midst of bone\x01",
            "I guess it was only me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PHuh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00312F#5P── Uncle As you said,\x01",
            "The way the terrorists were killed was\x01",
            "It was not rare for me.\x02\x03",
            "Certainly that extinction#4RAnxiomatosis#A battle\x01",
            "Because it was everyday in the battlefield.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6P…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00303F#5PI was the one who refreshed at that time …\x01",
            "I was not driven by righteousness.\x02\x03",
            "Even though I feel pity on terrorists,\x01",
            "Because my uncle broke my anger.\x02\x03",
            "#00308F#30WI, ─ ─ after two years\x01",
            "To me who does not change at all ……\x02\x03",
            "To myself that is only a hunter to the bone's mind\x01",
            "I was just amazed …\x02\x03",
            "#00306FThat's right\x01",
            "I grabbed it and was beaten up …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#6PI see…\x02\x03",
            "#00006F……surely\x01",
            "It might be bad parenthesis.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00302F#5PHaha, isn't it\x02\x03",
            "#00306FIndeed, a cool Date man's\x01",
            "I am not like anything ─\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6P…. But even then.\x01",
            "I am a bit happy.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0xA, 0x0)
    Sleep(120)
    SetChrSubChip(0xA, 0x2)
    Sleep(250)

    ChrTalk(
        0xA,
        "#00305F#5PHuh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PWhat is it, Randy?\x01",
            "Always have enough room for adults\x01",
            "Is not it just because I am relying on this?\x02\x03",
            "#00000FBut doing so\x01",
            "If you open yourself\x01",
            "I am a little happy as a friend.\x02\x03",
            "Maybe not just me ……\x01",
            "I think that everyone else is the same.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#00305F#5P…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6Pin addition……\x01",
            "I do not think it's a hunter to the bone's mind\x01",
            "Is not it just a belief?\x02\x03",
            "#00008FAt least I, Randy\x01",
            "It is important to undertake war for Mira\x01",
            "I do not think it is my favorite type.\x02\x03",
            "#00000FHe is a signed guy and likes to go out for a night out\x01",
            "Although it tends to be hotly militant and slightly\x01",
            "It also knows the closing properly …\x02\x03",
            "#00002FAnd always make us younger\x01",
            "Brother who will follow ……\x02\x03",
            "#00009FThat's what I know\x01",
            "Randy Orlando is a man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#00305F#5P…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PSo it's a bit long\x01",
            "Because I showed a bad place\x01",
            "There is no need to worry.\x02\x03",
            "#00000FRather, that person\x01",
            "I and Ellie 's - ──\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00303F#5PI got it. Don't say it all\x02\x03",
            "#00306FApparently your potential\x01",
            "I was still looking sweet … …\x02\x03",
            "#00310FGive me a break you airheaded asshole!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#6PAirheaded asshole?!\x02\x03",
            "#00006FI do not really know but until that\x01",
            "Did you say that you are going backwards?\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7565", 0)
    BeginChrThread(0x19, 1, 0, 16)

    ChrTalk(
        0xA,
        (
            "#00315F#5PAh, now depression#2RUzu#Do you know?\x01",
            "I'm getting stupid ……\x02\x03",
            "#00306FThis kind of thing,\x01",
            "I will enjoy Michelam!\x02\x03",
            "#00301FPlay around at the theme park\x01",
            "In the evening I will hit her sister!\x02\x03",
            "#00307FYou come along, you punk little bro\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PR-roger\x02\x03",
            "#00002F(I'm not sure but ….\x01",
            "I wonder if she cheered me up? )\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 980, 0, -10170, 270)
    SetChrSubChip(0xA, 0x1)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x144, 3)
    EventEnd(0x5)
    Return()

    # Function_14_2967 end

    def Function_15_38B3(): pass

    label("Function_15_38B3")

    OP_25(0x1E0, 0x5A)
    Sleep(200)
    OP_25(0x1E0, 0x50)
    Sleep(200)
    OP_25(0x1E0, 0x46)
    Sleep(200)
    OP_25(0x1E0, 0x3C)
    Sleep(200)
    OP_25(0x1E0, 0x32)
    Sleep(200)
    OP_25(0x1E0, 0x28)
    Return()

    # Function_15_38B3 end

    def Function_16_38DB(): pass

    label("Function_16_38DB")

    OP_25(0x1E0, 0x32)
    Sleep(200)
    OP_25(0x1E0, 0x3C)
    Sleep(200)
    OP_25(0x1E0, 0x46)
    Sleep(200)
    OP_25(0x1E0, 0x50)
    Sleep(200)
    OP_25(0x1E0, 0x5A)
    Sleep(200)
    OP_25(0x1E0, 0x64)
    Return()

    # Function_16_38DB end

    def Function_17_3903(): pass

    label("Function_17_3903")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch08502.itc", 0x1E)
    LoadChrToIndex("chr/ch05202.itc", 0x1F)
    LoadChrToIndex("chr/ch05102.itc", 0x20)
    LoadChrToIndex("chr/ch07502.itc", 0x21)
    LoadChrToIndex("chr/ch10002.itc", 0x22)
    LoadChrToIndex("chr/ch05502.itc", 0x23)
    LoadChrToIndex("chr/ch05602.itc", 0x24)
    LoadChrToIndex("chr/ch00102.itc", 0x25)
    LoadChrToIndex("chr/ch00202.itc", 0x26)
    LoadChrToIndex("chr/ch02902.itc", 0x28)
    LoadChrToIndex("chr/ch03002.itc", 0x29)
    LoadChrToIndex("chr/ch02702.itc", 0x2A)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x102, 0x25)
    SetChrSubChip(0x102, 0x1)
    SetChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x103, 0x26)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x104, 0x2)
    SetChrSubChip(0x104, 0x1)
    SetChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x109, 0x28)
    SetChrSubChip(0x109, 0x1)
    SetChrFlags(0x109, 0x4)
    SetChrChipByIndex(0x105, 0x29)
    SetChrSubChip(0x105, 0x2)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x18, 0x2A)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    OP_52(0x18, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x18, 1, 0, 0)
    SetChrChipByIndex(0x12, 0x1E)
    SetChrSubChip(0x12, 0x2)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x15, 0x1F)
    SetChrSubChip(0x15, 0x1)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x14, 0x20)
    SetChrSubChip(0x14, 0x1)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x13, 0x21)
    SetChrSubChip(0x13, 0x2)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x16, 0x22)
    SetChrSubChip(0x16, 0x2)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x23)
    SetChrSubChip(0x17, 0x2)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x101, 0, 0, 0, 0)
    SetChrFlags(0x101, 0x8)
    SetChrPos(0x102, 1000, -800, 7350, 0)
    SetChrPos(0x17, 0, -800, 7350, 0)
    SetChrPos(0x103, -2200, 150, -13850, 180)
    SetChrPos(0x18, -1200, 0, -14850, 270)
    SetChrPos(0x104, -3550, 150, -3850, 180)
    SetChrPos(0x105, -2350, 150, -3850, 180)
    SetChrPos(0x109, 2100, 150, -11350, 180)
    SetChrPos(0x12, 3250, 150, -11350, 180)
    SetChrPos(0x15, -3550, 150, -8850, 180)
    SetChrPos(0x16, -2350, 150, -8850, 180)
    SetChrPos(0x14, 2100, 150, -8850, 180)
    SetChrPos(0x13, 3250, 150, -8850, 180)
    OP_68(0, 1000, -15000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21000, 0)
    FadeToBright(1000, 0)
    OP_68(0, 1000, 10000, 20000)
    Sleep(14000)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 2)
    NewScene("e3000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_3903 end

    SaveToFile()

Try(main)
