from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t2520.bin",                # FileName
        "t2520",                    # MapName
        "t2520",                    # Location
        0x005A,                     # MapIndex
        "ed7126",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1B,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 90, 0, 3, 0, 4],
    )

    BuildStringList((
        "t2520",                  # 0
        "フラミー隊員",           # 1
        "ダグラス副司令",         # 2
    ))

    AddCharChip((
        "chr/ch34100.itc",                   # 00
        "chr/ch44902.itc",                   # 01
        "chr/ch41800.itc",                   # 02
    ))

    DeclNpc(4294934546, 9,       40700,   0,    261,  0x0, 0,   0,   0,   0,   1,   0,   6,   255,  0)
    DeclNpc(6210,    150,     4294967146, 270,  325,  0x0, 0,   1,   0,   255, 255, 0,   9,   255,  0)

    DeclActor(4760,    0,       4294967016, 1200,    6210,    1500,    4294967146, 0x007E, 0,  8,  0x0000)
    DeclActor(4294883616, 0,       22050,   1200,    4294883616, 1200,    22050,   0x007C, 0,  5,  0x0000)

    ChipFrameInfo(384, 0)                                        # 0

    ScpFunction((
        "Function_0_180",          # 00, 0
        "Function_1_238",          # 01, 1
        "Function_2_263",          # 02, 2
        "Function_3_2C4",          # 03, 3
        "Function_4_40A",          # 04, 4
        "Function_5_532",          # 05, 5
        "Function_6_5DD",          # 06, 6
        "Function_7_1371",         # 07, 7
        "Function_8_14CA",         # 08, 8
        "Function_9_151C",         # 09, 9
        "Function_10_357B",        # 0A, 10
        "Function_11_4045",        # 0B, 11
        "Function_12_4177",        # 0C, 12
        "Function_13_41A7",        # 0D, 13
        "Function_14_41FF",        # 0E, 14
        "Function_15_4257",        # 0F, 15
        "Function_16_42A2",        # 10, 16
        "Function_17_42ED",        # 11, 17
        "Function_18_4403",        # 12, 18
        "Function_19_45CD",        # 13, 19
        "Function_20_560F",        # 14, 20
        "Function_21_5DBA",        # 15, 21
        "Function_22_5F09",        # 16, 22
        "Function_23_6851",        # 17, 23
    ))


    def Function_0_180(): pass

    label("Function_0_180")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_1C0"),
        (1, "loc_1CC"),
        (2, "loc_1D8"),
        (3, "loc_1E4"),
        (4, "loc_1F0"),
        (5, "loc_1FC"),
        (6, "loc_208"),
        (SWITCH_DEFAULT, "loc_214"),
    )


    label("loc_1C0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_220")

    label("loc_1CC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_220")

    label("loc_1D8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_220")

    label("loc_1E4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_220")

    label("loc_1F0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_220")

    label("loc_1FC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_220")

    label("loc_208")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_220")

    label("loc_214")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_220")

    label("loc_220")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_237")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_220")

    label("loc_237")

    Return()

    # Function_0_180 end

    def Function_1_238(): pass

    label("Function_1_238")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_262")
    OP_94(0xFE, 0xFFFF86E8, 0xA5A0, 0xFFFF793C, 0x9858, 0x3E8)
    Sleep(300)
    Jump("Function_1_238")

    label("loc_262")

    Return()

    # Function_1_238 end

    def Function_2_263(): pass

    label("Function_2_263")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2C3")
    OP_95(0xFE, -33890, 0, 4560, 2000, 0x0)
    OP_95(0xFE, -33890, 0, -11290, 2000, 0x0)
    OP_95(0xFE, -33890, 0, 4560, 2000, 0x0)
    OP_95(0xFE, -53890, 0, 4560, 2000, 0x0)
    Jump("Function_2_263")

    label("loc_2C3")

    Return()

    # Function_2_263 end

    def Function_3_2C4(): pass

    label("Function_3_2C4")

    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_303")
    SetChrChipByIndex(0x8, 0x2)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0x8, -40000, 0, 4560, 90)
    BeginChrThread(0x8, 0, 0, 2)
    Jump("loc_3B9")

    label("loc_303")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_311")
    Jump("loc_3B9")

    label("loc_311")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_31F")
    Jump("loc_3B9")

    label("loc_31F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_32D")
    Jump("loc_3B9")

    label("loc_32D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_366")
    SetChrPos(0x8, 3900, 0, -150, 90)
    BeginChrThread(0x8, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_361")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)

    label("loc_361")

    Jump("loc_3B9")

    label("loc_366")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_390")
    SetChrPos(0x8, 740, 0, 4470, 0)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrFlags(0x9, 0x80)
    Jump("loc_3B9")

    label("loc_390")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_39E")
    Jump("loc_3B9")

    label("loc_39E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3B9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B9")
    SetChrFlags(0x9, 0x80)

    label("loc_3B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_3CD")
    ClearScenarioFlags(0x22, 0)
    Event(0, 19)
    Jump("loc_3DC")

    label("loc_3CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_3DC")
    ClearScenarioFlags(0x22, 1)
    Event(0, 23)

    label("loc_3DC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_409")
    Event(0, 10)

    label("loc_409")

    Return()

    # Function_3_2C4 end

    def Function_4_40A(): pass

    label("Function_4_40A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_426")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_438")

    label("loc_426")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_438")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x236), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_438")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_44A")
    OP_65(0x0, 0x1)
    Jump("loc_4C0")

    label("loc_44A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_458")
    Jump("loc_4C0")

    label("loc_458")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_466")
    Jump("loc_4C0")

    label("loc_466")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_474")
    Jump("loc_4C0")

    label("loc_474")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_486")
    OP_65(0x0, 0x1)
    Jump("loc_4C0")

    label("loc_486")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_498")
    OP_65(0x0, 0x1)
    Jump("loc_4C0")

    label("loc_498")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4A6")
    Jump("loc_4C0")

    label("loc_4A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4C0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C0")
    OP_65(0x0, 0x1)

    label("loc_4C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E6")
    SetMapObjFrame(0xFF, "hikari_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_4E6")

    SetMapObjFrame(0xFF, "bear", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_519")
    SetMapObjFrame(0xFF, "cgf2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "cda2", 0x0, 0x1)
    Jump("loc_531")

    label("loc_519")

    SetMapObjFrame(0xFF, "cgf2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "cda2", 0x1, 0x1)

    label("loc_531")

    Return()

    # Function_4_40A end

    def Function_5_532(): pass

    label("Function_5_532")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『おいしい鍋料理　土鍋編』がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('料理手册', 0x0)"), scpexpr(EXPR_END)), "loc_5D9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D9")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『芳醇潮鍋』\x07\x00",
            "のレシピを覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_5D9")

    TalkEnd(0xFF)
    Return()

    # Function_5_532 end

    def Function_6_5DD(): pass

    label("Function_6_5DD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_812")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_749")

    NpcTalk(
        0x8,
        "兵士フラミー",
        (
            "ダグラス副司令は、\x01",
            "現在クロスベル市で今後の対応を\x01",
            "検討しているみたいです。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "兵士フラミー",
        (
            "あの青白い大樹、起こりうる\x01",
            "帝国と共和国の侵攻……\x01",
            "まだまだ問題は山積みですから。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "兵士フラミー",
        (
            "国防軍として、どれだけの事を\x01",
            "できるかは分かりませんが……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "兵士フラミー",
        (
            "なんとか希望を捨てずに\x01",
            "頑張っていきたいTrue.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_80D")

    label("loc_749")


    NpcTalk(
        0x8,
        "兵士フラミー",
        (
            "ダグラス副司令は、\x01",
            "現在クロスベル市で今後の対応を\x01",
            "検討しているみたいです。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "兵士フラミー",
        (
            "国防軍として、どれだけの事を\x01",
            "できるかは分かりませんが……\x01",
            "なんとか頑張りたいTrue.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80D")

    Jump("loc_136D")

    label("loc_812")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_A09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_960")

    ChrTalk(
        0x8,
        (
            "ノエルSergent!\x01",
            "妹さん、助かって本当に\x01",
            "良かったTrue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108FえUh…警備隊の被害を見ると\x01",
            "素直には喜べませんけど。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "……ええ、正直\x01",
            "私たちも堪えていますが……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "こんな状況だからこそ\x01",
            "ノエルさんの妹さんが助かったことが\x01",
            "とても嬉しいんです。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103F……すみません。\x01",
            "That's fine, thank you\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A04")

    label("loc_960")


    ChrTalk(
        0x8,
        (
            "こんな状況だからこそ、\x01",
            "私たちは耐えていかなければ\x01",
            "ならないんだと思います。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "クロスベルを守るために\x01",
            "その命を燃やし、捧げる……\x01",
            "それが警備隊の使命ですから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A04")

    Jump("loc_136D")

    label("loc_A09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_B75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AF0")

    ChrTalk(
        0x8,
        "昨日の列車の脱線事故……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "住民投票が近づいている\x01",
            "このタイミングで起こったことを\x01",
            "考えると、やはり２大国が……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "……決め付けはいけないと\x01",
            "分かってはいるんですが、\x01",
            "どうしても勘繰ってしまいます。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B70")

    label("loc_AF0")


    ChrTalk(
        0x8,
        (
            "昨日の列車の脱線事故は、\x01",
            "やはり２大国のどちらかが……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "圧力も日増しに高まっていますし、\x01",
            "どうしても勘繰ってしまいます。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B70")

    Jump("loc_136D")

    label("loc_B75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_D53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C98")

    ChrTalk(
        0x8,
        (
            "住民投票の結果、\x01",
            "実際に独立に踏み切るかは\x01",
            "まだ不確定だと言われていますが……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "帝国や共和国の圧力が増している\x01",
            "この状況を考えると、その影響力は\x01",
            "脅威と捉えられているはずです。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "住民投票は私たちが\x01",
            "考えている以上に、周辺諸国に\x01",
            "大きな影響を与えそうTrue.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D4E")

    label("loc_C98")


    ChrTalk(
        0x8,
        (
            "帝国や共和国の圧力が増している\x01",
            "この状況を考えると、その影響力は\x01",
            "脅威と捉えられているはずです。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "住民投票は私たちが\x01",
            "考えている以上に、周辺諸国に\x01",
            "大きな影響を与えそうTrue.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D4E")

    Jump("loc_136D")

    label("loc_D53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_DCC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D6E")
    Call(0, 7)
    Jump("loc_DC7")

    label("loc_D6E")


    ChrTalk(
        0x8,
        (
            "共和国は、日増しに圧力を\x01",
            "強めてきているみたいです。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "やはり気は抜けませんね……\x02",
    )

    CloseMessageWindow()

    label("loc_DC7")

    Jump("loc_136D")

    label("loc_DCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_F28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E8B")

    ChrTalk(
        0x8,
        (
            "ダグラス副司令は、\x01",
            "テロ対策の打ち合わせのため\x01",
            "ベルガード門に向かいました。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "本会議が始まるまでには、\x01",
            "なんとしても警備体制を\x01",
            "万全にしておきたいですからね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F23")

    label("loc_E8B")


    ChrTalk(
        0x8,
        (
            "ダグラス副司令は、\x01",
            "テロ対策の打ち合わせのため\x01",
            "ベルガード門に向かいました。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "ソーニャ司令となら、\x01",
            "きっと万全の警備体制を\x01",
            "整えられるでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F23")

    Jump("loc_136D")

    label("loc_F28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_11FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1152")

    ChrTalk(
        0x8,
        (
            "ソーニャ司令の異動と\x01",
            "ノエル曹長の出向が\x01",
            "重なってしまったんですよね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "おかげで、タングラム門の\x01",
            "女子比率が下がってしまって……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106Fうーん、仕方ないとはいえ\x01",
            "申し訳ないです。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "うう、夜中に噂話をする相手も\x01",
            "減ってしまって、寂しいですよ〜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FUhm...\x01",
            "それは、男性隊員を相手に\x01",
            "話すんじゃダメなんですか？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304Fフフ、分かってないなあ。\x02\x03",
            "#10309F女の子の噂話なんて、\x01",
            "その場に男がいたら\x01",
            "できないことがほとんどだよ？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F（へ、偏見混じりだとは思うけど……\x01",
            "  微妙に恐ろしいものを感じるな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11F5")

    label("loc_1152")


    ChrTalk(
        0x8,
        (
            "ノエルSergent!早く警備隊に\x01",
            "もどってきてくださいよ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "それまでに、噂話をたくさん\x01",
            "ストックしておきますから!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106F（も、戻ったら大変そうだなAh...）\x02",
    )

    CloseMessageWindow()

    label("loc_11F5")

    Jump("loc_136D")

    label("loc_11FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_136D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12E8")

    ChrTalk(
        0x8,
        (
            "ダグラス副司令は以前、\x01",
            "左遷されて長らく警察学校に\x01",
            "勤めていたそうですが……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "先日、ソーニャ司令の要請で\x01",
            "再び警備隊に勤務することに\x01",
            "なったんです。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "私たちも、副司令の復帰を\x01",
            "とても喜んでいるんですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_136D")

    label("loc_12E8")


    ChrTalk(
        0x8,
        (
            "ダグラス副司令は、昔から\x01",
            "とても優秀な警備隊員として\x01",
            "知られていました。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "私たちも、副司令の復帰を\x01",
            "とても喜んでいるんですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_136D")

    TalkEnd(0xFE)
    Return()

    # Function_6_5DD end

    def Function_7_1371(): pass

    label("Function_7_1371")

    OP_4B(0x8, 0xFF)

    ChrTalk(
        0x8,
        "──報告は以上です。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "なるほどな、\x01",
            "タングラム丘陵での模擬演習か……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "小規模なものではあるが、\x01",
            "圧力のかけ方があからさまに\x01",
            "なってきてやがる。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "ええ、やはり住民投票までは\x01",
            "気を抜くわけにはいきませんね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "各方面と連携をとりつつ\x01",
            "警戒していくしかあるまい。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "ご苦労だった、引き続き監視を頼む。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "ハッ!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 2)
    OP_4C(0x8, 0xFF)
    Return()

    # Function_7_1371 end

    def Function_8_14CA(): pass

    label("Function_8_14CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14F3")
    Call(0, 11)
    Return()

    label("loc_14F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1518")
    Call(0, 20)
    Return()

    label("loc_1518")

    Call(0, 9)
    Return()

    # Function_8_14CA end

    def Function_9_151C(): pass

    label("Function_9_151C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1545")
    Call(0, 11)
    Return()

    label("loc_1545")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_156A")
    Call(0, 20)
    Return()

    label("loc_156A")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_21E3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_1DAE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1732")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1695")

    ChrTalk(
        0x9,
        (
            "古戦場の封鎖は解除するよう\x01",
            "すでに連絡はしておいた。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "アルモリカ古道方面から\x01",
            "魔獣の発生現場に向かってくれ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "警備隊として、魔獣退治に\x01",
            "手を割けないのは心苦しい思いだが……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "お前さんたちならこの件を\x01",
            "解決してくれると信じているぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_172D")

    label("loc_1695")


    ChrTalk(
        0x9,
        (
            "古戦場の封鎖は解除するよう\x01",
            "すでに連絡はしておいた。\x02\x03",
            "古道方面から現場に向かってくれ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "お前さんたちならこの件を\x01",
            "解決してくれると信じているぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_172D")

    Jump("loc_1DAA")

    label("loc_1732")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D15")

    ChrTalk(
        0x9,
        "ご苦労だったな、支援課諸君。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "まだまだ問題は山積みだが、\x01",
            "おかげで懸案していた事が\x01",
            "一つ片付いた。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "あの襲撃事件で受けた被害で、\x01",
            "人手も足らない所だったからな。\x01",
            "本当に感謝している。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000Fいえ、困った時はお互い様ですから。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F……警備隊の被害は\x01",
            "本当に甚大だったんですよね。\x02\x03",
            "#00101F今後の建て直しの見込みは、\x01",
            "どれくらい立っているんでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "……この緊張状態への対応もあって、\x01",
            "正直言ってままなっていない。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "だが、ノエル曹長が警備隊に戻れば\x01",
            "そちらにも手が回せるようになるだろう。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "その際は、是非とも然るべきポストで\x01",
            "組織の建て直しに貢献してもらう\x01",
            "ことになるだろう。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19BC")
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    label("loc_19BC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19DF")
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    label("loc_19DF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A02")
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    label("loc_1A02")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A22")
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_1A22")

    Sleep(1000)

    ChrTalk(
        0x104,
        "#00305Fそいつは……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108F……昇進、ということですか？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "……今回、警備隊の被害が\x01",
            "ある意味最も大きかったのは、\x01",
            "『士気』へのダメージだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "仲間の犠牲のショックを受け、\x01",
            "警備隊の役割そのものへの恐怖に\x01",
            "蝕まれた者は相当数に上るだろう。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "一部の隊員たちは、\x01",
            "怒りや矜持を拠り所にして\x01",
            "何とかそれを保っているようだが……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FHmm \x01",
            "そういった想いは\x01",
            "ひしひしと伝わってきます。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "失われた士気を取り戻す為にも、\x01",
            "優秀な士官は必ず必要になる。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "まだ確定事項ではないが……\x01",
            "お前さんにはその能力が\x01",
            "充分にあるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103F……ミレイユ三尉のように\x01",
            "できるかは分かりませんけど……\x02\x03",
            "#10101Fそうなった場合は謹んで、\x01",
            "使命を全うさせていただきます。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "……すまない。\x01",
            "しばらく辛い時が続くだろうが、\x01",
            "よろしく頼むぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19D, 3)
    Jump("loc_1DAA")

    label("loc_1D15")


    ChrTalk(
        0x9,
        (
            "警備隊を立て直す為にも、\x01",
            "曹長には然るべきポストについて\x01",
            "力を貸してもらうことになるだろう。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "しばらく辛い時が続くだろうが、\x01",
            "よろしく頼むぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DAA")

    TalkEnd(0x9)
    Return()

    label("loc_1DAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2149")

    ChrTalk(
        0x9,
        (
            "あの一連の事件で受けた\x01",
            "警備隊の被害は計り知れない。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "ノエル曹長が警備隊に戻った暁には、\x01",
            "然るべきポストで組織の建て直しに\x01",
            "貢献してもらうことになるだろう。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FThat is\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108F……昇進、ということですか？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "……今回、警備隊の被害が\x01",
            "ある意味最も大きかったのは、\x01",
            "『士気』へのダメージだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "仲間の死のショックを受け、\x01",
            "警備隊の役割そのものへの恐怖に\x01",
            "蝕まれた者は相当数に上るだろう。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "一部の隊員たちは、\x01",
            "怒りや矜持を拠り所にして\x01",
            "何とかそれを保っているようだが……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FHmm \x01",
            "そういった想いは\x01",
            "ひしひしと伝わってきます。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "失われた士気を取り戻す為にも、\x01",
            "優秀な士官は必ず必要になる。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "まだ確定事項ではないが……\x01",
            "お前さんにはその能力が\x01",
            "充分にあるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103F……ミレイユ三尉のように\x01",
            "できるかは分かりませんけど……\x02\x03",
            "#10101Fそうなった場合は謹んで、\x01",
            "使命を全うさせていただきます。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "……すまない。\x01",
            "しばらく辛い時が続くだろうが、\x01",
            "よろしく頼むぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18E, 3)
    Jump("loc_21DE")

    label("loc_2149")


    ChrTalk(
        0x9,
        (
            "警備隊を立て直す為にも、\x01",
            "曹長には然るべきポストについて\x01",
            "力を貸してもらうことになるだろう。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "しばらく辛い時が続くだろうが、\x01",
            "よろしく頼むぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21DE")

    Jump("loc_3577")

    label("loc_21E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_27DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_249A")

    ChrTalk(
        0x9,
        (
            "お前さんたち、\x01",
            "昨日は脱線事故の現場で\x01",
            "大層役に立ったYeah we should\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300Fはは、我らが支援課のリーダーが\x01",
            "大活躍してくれてな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FちょUh\x01",
            "さすがに持ち上げすぎだって。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100Fふふ、そんなことないでしょう。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "俺が警察学校で教えたのは\x01",
            "戦闘技術が主だったが……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "ロイド、お前さんは\x01",
            "立派な捜査官に成長してたんRight.\x01",
            "何やら感慨深いぞ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012Fふ、副司令まで……\x02\x03",
            "#00003F……本当にまだまだなんです。\x01",
            "兄貴の足元にも及んじゃいない。\x02\x03",
            "#00000F俺には、その差を埋めてくれる\x01",
            "仲間たちがいるってだけですから。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FLloyd…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "フフ、それでいい。\x01",
            "そのまま、おまえはどこまでも\x01",
            "成長していけるだろう。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "将来を楽しみにしてるぞ、ロイド。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x170, 2)
    Jump("loc_27D5")

    label("loc_249A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2691")

    ChrTalk(
        0x9,
        "Oh that's true\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "お前さんたち、\x01",
            "この本を読んでみないか？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '沐浴阳光的阿尼艾丝９卷'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Got Access Card\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('沐浴阳光的阿尼艾丝９卷', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x189, 0)

    ChrTalk(
        0x102,
        "#00105FThis is..娯楽小説ですか？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309Fダグラスの兄さんが、\x01",
            "こういうモンを読むとは意外だなぁ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "ハハ、俺だって小説くらい読むさ。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "そいつはソーニャ司令に\x01",
            "勧められていたんだが……\x01",
            "知っての通り、最近は忙しくてな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "まあ、そういうわけだから\x01",
            "時間があるときにでも楽しむといい。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000Fええ、That's fine, thank you\x02",
    )

    CloseMessageWindow()
    Jump("loc_27D5")

    label("loc_2691")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_274C")

    ChrTalk(
        0x9,
        "さて、それはそれとして……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "まだ脱線事故から一晩だ。\x01",
            "完全に安心するのは早いだろう。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "しばらくは警備隊のほうでも\x01",
            "鉄道付近を警戒した方が\x01",
            "いいかもしれないな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_27D5")

    label("loc_274C")


    ChrTalk(
        0x9,
        (
            "まだ脱線事故から一晩だ。\x01",
            "完全に安心するのは早いだろう。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "しばらくは警備隊のほうでも\x01",
            "鉄道付近を警戒した方が\x01",
            "いいかもしれないな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27D5")

    Jump("loc_3577")

    label("loc_27DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2B22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A86")

    ChrTalk(
        0x9,
        (
            "お前らの調査で分かった\x01",
            "《プレロマ草》とやら……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "あの《グノーシス》の\x01",
            "原料だったんだってな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "厄介なクスリだとは\x01",
            "思っていたが……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FI see…\x01",
            "副司令は教団事件のときも\x01",
            "警察学校にいたんですね？\x02\x03",
            "#00003F操られた警備隊が\x01",
            "最初に襲撃したあの現場に……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "……隊員たちが操られて\x01",
            "突然襲ってきたときは、\x01",
            "正直、面食らったもんだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "結局、俺と警察学校の人員じゃ\x01",
            "対処しきれず……拘置所から\x01",
            "秘書#4Rアーネスト#を取り逃がしちまったんだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108FOh is that right\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "あれだけの力をもつクスリの原料が、\x01",
            "幻獣が出現する原因でもあったわけだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "今回の幻獣騒ぎ……\x01",
            "考えられてる以上にやばいヤマ\x01",
            "なのかもしれねえな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x170, 1)
    Jump("loc_2B1D")

    label("loc_2A86")


    ChrTalk(
        0x9,
        (
            "あれだけの力をもつクスリの原料が、\x01",
            "幻獣が出現する原因でもあったわけだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "今回の幻獣騒ぎ……\x01",
            "考えられてる以上にやばいヤマ\x01",
            "なのかもしれねえな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B1D")

    Jump("loc_3577")

    label("loc_2B22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2BC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B3D")
    Call(0, 7)
    Jump("loc_2BC3")

    label("loc_2B3D")


    ChrTalk(
        0x9,
        (
            "ご覧の通り、とても《幻獣》に\x01",
            "手を回している余裕は無さそうだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "お前さんたちには苦労をかけるが、\x01",
            "調査の方はよろしく頼んだぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BC3")

    Jump("loc_3577")

    label("loc_2BC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2BD6")
    Jump("loc_3577")

    label("loc_2BD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3338")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31F1")

    ChrTalk(
        0x109,
        "#10100F副司令、お疲れ様です!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "おう、お前さんたちか。\x01",
            "丁度いいとこに来たな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "そろそろ息抜きでもしようと\x01",
            "思っていたところだ、\x01",
            "折角だからゆっくりしていきな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300Fふう、兄さんの事だから\x01",
            "また演習に付き合えとか\x01",
            "言ってくるかとおもったぜ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "んん、そうしたいのは山々だが、\x01",
            "さすがにそこまでの時間はな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha…\x01",
            "さすがに忙しそうTrue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "なんと言っても\x01",
            "明日は本会議だからな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "一応、通商会議中の警備体制は\x01",
            "万全にしているつもりだが、\x01",
            "状況は常に変わるものだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "ミシュラムを警備している\x01",
            "ソーニャ司令とも、明朝に改めて\x01",
            "打ち合わせる必要があるだろう。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FYes…\x01",
            "オルキスタワーでは国賓たちが\x01",
            "一同に会するわけですし。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300Fどれだけ準備しても\x01",
            "しすぎるということはないだろうね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300Fま、警備隊に任せときゃ\x01",
            "ひとまずは安心できるだろ。\x02\x03",
            "#00304Fなんたって今の警備隊にゃ、\x01",
            "『迅雷のダグラス』もいるわけだし。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F75")
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)

    label("loc_2F75")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F9F")
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)

    label("loc_2F9F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FC9")
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)

    label("loc_2FC9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FF0")
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_2FF0")

    Sleep(1000)

    ChrTalk(
        0x109,
        "#10105F迅雷……ですか？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "ハハ、また懐かしい名前を\x01",
            "持ち出してきたもんだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "警察学校にトバされる前に、\x01",
            "一部でそんな風に呼ばれた\x01",
            "時期があってな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "しかし、迅雷だの鬼だの……\x01",
            "どいつもこいつも勝手な名前で\x01",
            "呼んでくれるもんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000Fはは、どっちも\x01",
            "似合ってると思いますけど。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "茶化すな茶化すな。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "コホン、話を戻すが……\x01",
            "通商会議の警備は万全に\x01",
            "させてもらうつもりだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "お前さんたちはあまり気にせず、\x01",
            "自分たちの仕事に務めるんRight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000Fええ、そうさせていただきます。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x159, 0)
    Jump("loc_3333")

    label("loc_31F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32BD")

    ChrTalk(
        0x9,
        (
            "『迅雷』か……\x01",
            "はは、懐かしい二つ名だぜ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "コホン、とにかく……\x01",
            "通商会議の警備は万全に\x01",
            "させてもらうつもりだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "お前さんたちはあまり気にせず、\x01",
            "自分たちの仕事に務めるんRight.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3333")

    label("loc_32BD")


    ChrTalk(
        0x9,
        (
            "通商会議の警備は万全に\x01",
            "させてもらうつもりだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "お前さんたちはあまり気にせず、\x01",
            "自分たちの仕事に努めるといい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3333")

    Jump("loc_3577")

    label("loc_3338")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3577")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3577")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34FA")

    ChrTalk(
        0x9,
        (
            "#4P演習への参加、ご苦労だった。\x01",
            "また何かあったら頼むぞ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#4Pあと、さっきの件だが……\x01",
            "くれぐれも『ここだけの話』に\x01",
            "しておいてくれるか。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FRight, got it\x01",
            "とにかくこちらでは\x01",
            "気をつけるように──\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F……今度、ティオすけには\x01",
            "教えてやらないとな♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309Fフフ、そうだね。\x01",
            "不公平というものだし。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011Fお、おいそこ!\x01",
            "速攻で前言撤回させるなって!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#4P……頼んだからな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3577")

    label("loc_34FA")


    ChrTalk(
        0x9,
        (
            "#4P演習への参加、ご苦労だった。\x01",
            "また何かあったら頼むぞ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#4P……さっきの件も、\x01",
            "『ここだけの話』に\x01",
            "しておくんだぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3577")

    TalkEnd(0x9)
    Return()

    # Function_9_151C end

    def Function_10_357B(): pass

    label("Function_10_357B")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-1120, 900, -310, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x9, 6630, 0, -20, 270)
    SetChrPos(0x101, -5500, 0, -20, 90)
    SetChrPos(0x102, -5500, 0, -20, 90)
    SetChrPos(0x104, -5500, 0, -20, 90)
    SetChrPos(0x109, -5500, 0, -20, 90)
    SetChrPos(0x105, -5500, 0, -20, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(105, 0, 100, 0)
    BeginChrThread(0x101, 3, 0, 12)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 13)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 14)
    OP_68(930, 900, -520, 3000)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 15)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 16)
    WaitChrThread(0x105, 3)
    OP_6F(0x79)

    ChrTalk(
        0x9,
        "#11P──ようやく来たな。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#00002FAh...\x02",
    )

    CloseMessageWindow()
    OP_68(3420, 900, 80, 3000)
    MoveCamera(45, 19, 0, 3000)
    OP_6E(350, 3000)
    SetCameraDistance(25500, 3000)

    def lambda_377E():
        OP_98(0xFE, 0x9C4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_377E)
    Sleep(100)

    def lambda_379B():
        OP_98(0xFE, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_379B)
    Sleep(100)

    def lambda_37B8():
        OP_98(0xFE, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_37B8)
    Sleep(100)

    def lambda_37D5():
        OP_98(0xFE, 0xAF0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_37D5)
    Sleep(100)

    def lambda_37F2():
        OP_98(0xFE, 0x9C4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_37F2)
    Sleep(1000)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x109,
        (
            "#10100Fダグラス副司令……\x01",
            "お疲れ様です!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11Pよう、シーカー曹長。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P特務支援課とやらの\x01",
            "居心地はどうだ？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100Fハッ!\x01",
            "毎日色々と勉強させて\x01",
            "いただいています!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11Pはは、それはなによりだ。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P今後のためにも、\x01",
            "しっかり精進するといい。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00105Fノエルさん、この方が.......?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P……おっと、自己紹介が\x01",
            "まだだったな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P俺の名はダグラス。\x01",
            "この度、警備隊の\x01",
            "副司令に就任した者だ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pお前たちのことは\x01",
            "司令から詳しく聞いている。\x01",
            "以後お見知りおき願おう。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100FPlease do\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302Fフフ、見た目通りの\x01",
            "人物のようだね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00300Fあんたも相変わらず元気そうだな、\x01",
            "ダグラスの兄さん。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pお前さんもな、ランディ。\x01",
            "ベルガード門でのリハビリ訓練、\x01",
            "ご苦労だった。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pそれと──ロイド。\x01",
            "会うのは久しぶりRight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P先の教団事件じゃ、\x01",
            "随分と活躍したらしいが。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FHaha…\x01",
            "Nice to see you again\x02\x03",
            "#00004F教官が副司令に\x01",
            "なったって聞いて\x01",
            "本当に驚きましたよ。\x02\x03",
            "#00012Fあの『鬼のダグラス』に\x01",
            "こってり絞られた記憶が\x01",
            "鮮明に蘇ったというか……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pおいおい、昔のあだ名なんか\x01",
            "持ち出すもんじゃないぞ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11Pまったく、恥ずかしいだろうが。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100F（うーん、警察学校では\x01",
            "  厳しい人だったみたいね……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P……おっと、\x01",
            "これくらいにしておこう。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P今日は仕事でわざわざ\x01",
            "来てもらったんだからな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300F仕事というと……\x01",
            "『演習への参加要請』だね？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11Pああ、そのとおりだ。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P今回の演習は、お前たち\x01",
            "特務支援課を叩き直すのが目的だ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P俺の厳し〜い訓練を\x01",
            "バッチリ受けていってもらうぞ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FHuh?\x01",
            "警備隊じゃなく、\x01",
            "俺たちのためなんですか？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pま、もちろん警備隊員にも\x01",
            "いい経験になるだろうしな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pなお、警察の上層部には\x01",
            "すでに話を通していてな。\x01",
            "公式な合同訓練という名目だ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00300FI see..\x01",
            "支援要請っていうよりは\x01",
            "割とちゃんとした訓練みてえRight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11Pハハ、まあそういうことRight.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pこちらの準備はすでにできている。\x01",
            "あとはお前たち次第だが……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#12P#00100F一度、装備を整えた方が\x01",
            "いいかもしれないわね。\x02\x03",
            "#00104Fクオーツの構成も\x01",
            "見直したほうがいいかも。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pどうする、\x01",
            "早速演習を始めてもいいか？\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x6F, 0x1, 0x0)
    Call(0, 17)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_10_357B end

    def Function_11_4045(): pass

    label("Function_11_4045")

    EventBegin(0x0)
    Fade(500)
    OP_68(3420, 900, 80, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, 2500, 0, -20, 90)
    SetChrPos(0x109, 2500, 0, 980, 90)
    SetChrPos(0x102, 2500, 0, -1020, 90)
    SetChrPos(0x104, 1300, 0, 680, 90)
    SetChrPos(0x105, 1000, 0, -720, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "#11P隊員たちの訓練のために、\x01",
            "ぜひ演習の相手を\x01",
            "してもらいたくてな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pこちらの準備はすでにできている。\x01",
            "早速演習を始めてもいいか？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 17)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_11_4045 end

    def Function_12_4177(): pass

    label("Function_12_4177")


    def lambda_417C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_417C)

    def lambda_418D():
        OP_98(0xFE, 0x157C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_418D)
    WaitChrThread(0x101, 1)
    Return()

    # Function_12_4177 end

    def Function_13_41A7(): pass

    label("Function_13_41A7")


    def lambda_41AC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_41AC)

    def lambda_41BD():
        OP_98(0xFE, 0xFA0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_41BD)
    WaitChrThread(0x109, 1)
    OP_97(0x109, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
    OP_97(0x109, 0x3E8, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_13_41A7 end

    def Function_14_41FF(): pass

    label("Function_14_41FF")


    def lambda_4204():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4204)

    def lambda_4215():
        OP_98(0xFE, 0xFA0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4215)
    WaitChrThread(0x102, 1)
    OP_97(0x102, 0x0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
    OP_97(0x102, 0x3E8, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_14_41FF end

    def Function_15_4257(): pass

    label("Function_15_4257")


    def lambda_425C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_425C)

    def lambda_426D():
        OP_98(0xFE, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_426D)
    WaitChrThread(0x104, 1)
    OP_97(0x104, 0x3E8, 0x0, 0x2BC, 0x7D0, 0x0)
    OP_93(0x104, 0x5A, 0x1F4)
    Return()

    # Function_15_4257 end

    def Function_16_42A2(): pass

    label("Function_16_42A2")


    def lambda_42A7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_42A7)

    def lambda_42B8():
        OP_98(0xFE, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_42B8)
    WaitChrThread(0x105, 1)
    OP_97(0x105, 0x3E8, 0x0, 0xFFFFFD44, 0x7D0, 0x0)
    OP_93(0x105, 0x5A, 0x1F4)
    Return()

    # Function_16_42A2 end

    def Function_17_42ED(): pass

    label("Function_17_42ED")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【演習を始める】\x01",            # 0
            "【準備ができていない】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4365"),
        (1, "loc_436D"),
        (SWITCH_DEFAULT, "loc_4402"),
    )


    label("loc_4365")

    Call(0, 18)
    Jump("loc_4402")

    label("loc_436D")


    ChrTalk(
        0x101,
        (
            "#6P#00000Fすみませんが……\x01",
            "少し時間をもらえますか？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11Pふむ、そうか。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pそれでは、準備ができたら\x01",
            "もう一度声をかけてくれ。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x152, 0)
    Jump("loc_4402")

    label("loc_4402")

    Return()

    # Function_17_42ED end

    def Function_18_4403(): pass

    label("Function_18_4403")


    ChrTalk(
        0x101,
        (
            "#6P#00000Fええ、こちらも\x01",
            "準備はできてます。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x5A, 0x1F4)
    Sleep(500)

    ChrTalk(
        0x9,
        "#11Pよし。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pシーカー曹長も、\x01",
            "警備隊が相手だからといって\x01",
            "戸惑わないようにな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P警備隊員と相対することで\x01",
            "新たに学べることもあるだろう。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100Fはっ、Roger that!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pそれでは、\x01",
            "早速演習を開始するぞ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P全員、屋外の駐車場に\x01",
            "移動してくれ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【警備隊演習の参加要請】\x07\x00",
            "を開始した!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x6F, 0x1, 0x1)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x22, 1)
    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_18_4403 end

    def Function_19_45CD(): pass

    label("Function_19_45CD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(3420, 900, 80, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x9, 6630, 0, -20, 270)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x101, 2500, 0, -20, 90)
    SetChrPos(0x109, 2500, 0, 980, 90)
    SetChrPos(0x102, 2500, 0, -1020, 90)
    SetChrPos(0x104, 1300, 0, 680, 90)
    SetChrPos(0x105, 1000, 0, -720, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "#11P──改めて、\x01",
            "演習への参加ご苦労だった。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P隊員にとっても\x01",
            "いい経験になったはずだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000Fいえ、俺たちのほうこそ。\x01",
            "とてもいい経験だったと思います。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306Fしっかし、あんたは\x01",
            "ちっとも衰えちゃいないなァ。\x02\x03",
            "#00300F初めての演習で\x01",
            "ブチのめされたのを思い出したぜ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pそういうお前さんは\x01",
            "なかなか成長したようじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P俺が教えたスタンハルバードも、\x01",
            "完全に自分のものにしたようだしな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304Fおうよ、今となっちゃあ\x01",
            "超スタイリッシュ＆エレガントな\x01",
            "ランディ流に進化したぜ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000Fスタンハルバードを……\x01",
            "そうだったんですか。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00109Fふふ、ランディにとっては\x01",
            "恩人のような方だったんTrue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pまあ、こいつがライフルを\x01",
            "扱いたがらなかったんで\x01",
            "集中して仕込んだってわけだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pその甲斐あってか、\x01",
            "ハルバードだけで充分に一線を張れる\x01",
            "実力を手にいれやがってな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pそれが前司令殿に嫌われる\x01",
            "要因にもなったようだが。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00300Fはは、まあ規律に縛られるのは\x01",
            "俺の性分じゃねえからな。\x02\x03",
            "#00309Fおかげさまで支援課に移れたし、\x01",
            "せいせいしてるくらいさ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304Fフフ、良くも悪くも\x01",
            "副司令殿のおかげって\x01",
            "ところかな。\x02\x03",
            "#10302F警察学校への左遷は\x01",
            "やはり采配ミスだった\x01",
            "みたいだね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F例の教団事件まで、\x01",
            "警備隊はあの前司令の\x01",
            "指揮下だったから。\x02\x03",
            "#10109Fそれでなくても副司令は、\x01",
            "部下からの信頼が厚くて\x01",
            "実力もありましたし……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pそんな大したモンじゃないが……\x01",
            "まァ、目障りだったんだろうな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P警察学校に行ってからは、\x01",
            "あの腐った体制を建てなおせる\x01",
            "人材を育成するのに専念してた。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P今考えれば、ある意味\x01",
            "それもラッキーだったかも\x01",
            "しれないけどな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pまだ何色にも染まっていない\x01",
            "警備隊員や警察官の卵たちを\x01",
            "教育してやれたことだし。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00012Fさすがに当時は\x01",
            "厳しすぎると思ってましたけど。\x02\x03",
            "#00006Fフランツなんか\x01",
            "たまに泣いてましたし。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pはは、まあそう言うな。\x01",
            "ちゃんとタメになってるだろう？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pま、色々あったが\x01",
            "こうして警備隊に戻って来れた。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pこれからはお前たちとも\x01",
            "協力しあって、共に自治州を\x01",
            "守っていかせてもらうさ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FEhe\x01",
            "力を尽くさせていただきます。\x02\x03",
            "#00104F私たちなんて、まだまだ\x01",
            "未熟もいいところですけど。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pなァに、謙遜することはない。\x01",
            "お前たちはそれだけの力を\x01",
            "ちゃんと持っているはずだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pセルゲイ先輩の立ち上げた\x01",
            "特務支援課で、しっかり\x01",
            "仕事をしてきたおかげだろうさ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#00005Fセルゲイ先輩.......?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00305Fなんだ、あのオヤジとも\x01",
            "知り合いだったのか？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11Pあ？　知り合いも何も……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pセルゲイ先輩と\x01",
            "ソーニャ先輩には、\x01",
            "昔から世話になっててな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P俺は、あの２人の結婚の\x01",
            "仲立ちをしたくらいなんだぞ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#00011Fけっ…!!!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4S#6P#00105F結婚…………!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#4S#10111Fソーニャ司令と、\x01",
            "セルゲイ課長が!？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10305Fへぇ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306Fおいおいおい、\x01",
            "いきなり衝撃的な事実を\x01",
            "ぶっちゃけやがって…!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P……な、なんだ。\x01",
            "お前らYou didn't know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pまあ、５年くらい前に\x01",
            "別れちまったんだがな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pセルゲイ先輩の左遷や\x01",
            "ソーニャ先輩の昇進とかが、\x01",
            "色々重なったからなぁ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FHa, I see\x01",
            "大人の男と女ならではの\x01",
            "ドラマがあったみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105Fへぇぇぇ……\x01",
            "あのソーニャ司令が……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303F確かになんとな〜く\x01",
            "怪しいとは思ってたが……\x02\x03",
            "#00309Fなんつーか、謎が\x01",
            "一つ解けた感じだな♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00011Fちょ、ちょっとみんAh…\x01",
            "面白がるのはやめとけって。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00109F（わ、私もちょっと\x01",
            "  気になるけど……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#11PCrap…\x01",
            "うっかり口を滑らせちまったか。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pと、とにかく。\x01",
            "この件に関してはあまり\x01",
            "ペラペラと他言しないようにな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pコホン、とりあえず……\x01",
            "演習の件に関してはご苦労だった。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11Pまた何かあったらよろしく頼むぞ。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000Fは、Yes.\x01",
            "ご連絡をお待ちしてます。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【警備隊演習の参加要請】\x07\x00",
            "を達成した!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_29(0x6F, 0x1, 0x4)
    OP_29(0x6F, 0x1, 0x5)
    OP_29(0x6F, 0x4, 0x10)
    OP_29(0xA3, 0x1, 0x4)
    SetChrPos(0x0, 3000, 0, 0, 90)
    EventEnd(0x5)
    Return()

    # Function_19_45CD end

    def Function_20_560F(): pass

    label("Function_20_560F")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(3420, 900, 80, 0)
    MoveCamera(44, 23, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, 2500, 0, -20, 90)
    SetChrPos(0x102, 2300, 0, -1020, 90)
    SetChrPos(0x103, 2300, 0, 980, 90)
    SetChrPos(0x104, 1000, 0, -20, 90)
    SetChrPos(0x109, 900, 0, 980, 90)
    SetChrPos(0x105, 900, 0, -1020, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_93(0x9, 0x10E, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D35")

    ChrTalk(
        0x101,
        (
            "#6P#00000Fダグラス副司令、\x01",
            "Thanks for your hard work\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P……よう、お前たちか。\x01",
            "お疲れさまだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pどうやら、依頼を見て\x01",
            "来てくれたようだな？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00300Fま、そういうわけだが……\x02\x03",
            "#00303F……ダグラスの兄さん、\x01",
            "なんだかピリピリしてんな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_59E6")

    ChrTalk(
        0x9,
        (
            "#11P門に入ってきてお前たちも\x01",
            "ひしひし感じているだろうが……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P現在、クロスベル警備隊は\x01",
            "厳戒態勢にあってな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pその上、指名手配犯が\x01",
            "無理やりゲートを通るなんて事も\x01",
            "起こってしまっている。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pそんなわけで、ますます\x01",
            "気が抜けない状態なのさ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100FAha, is that right\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pま、指名手配犯の方はお前らが\x01",
            "捕まえてくれたらしいがな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pそれに関しては、\x01",
            "礼を言わせてもらおう。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003Fいえ、当然の事をしたまでです。\x02\x03",
            "#00001F……今回の依頼はそのあたりも\x01",
            "関係しているわけですね？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CA0")

    label("loc_59E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_5BA1")

    ChrTalk(
        0x9,
        (
            "#11P門に入ってきてお前たちも\x01",
            "ひしひし感じているだろうが……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P現在、クロスベル警備隊は\x01",
            "厳戒態勢にあってな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pその上、不届きな輩が\x01",
            "無理やりゲートを通るなんて事も\x01",
            "起こってしまっている。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pそんなわけで、\x01",
            "気が抜けない状態なのさ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100FAha, is that right\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F（俺たちが取り逃がしてしまった\x01",
            "　医療物資の窃盗犯か……）\x02\x03",
            "#00001F……でも、今回の依頼はそのあたりも\x01",
            "関係しているわけですね？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CA0")

    label("loc_5BA1")


    ChrTalk(
        0x9,
        (
            "#11P門に入ってきてお前たちも\x01",
            "ひしひし感じているだろうが……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P現在、クロスベル警備隊は\x01",
            "厳戒態勢にあってな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pちぃっとばかし、\x01",
            "気が抜けねえ状態なのさ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001FI see..\x01",
            "今回の依頼はそのあたりのことも\x01",
            "関係しているわけTrue.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CA0")


    ChrTalk(
        0x9,
        "#11Pあぁ、そういうことになるな。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pさっそく、仕事の内容を\x01",
            "説明しようと思うが……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pお前さんたち、\x01",
            "依頼を引き受けてくれるか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D8B")

    label("loc_5D35")


    ChrTalk(
        0x9,
        "#11Pお前さんたち、手は空いたのか？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11P早速依頼を引き受けてもらいたいが……\x02",
    )

    CloseMessageWindow()

    label("loc_5D8B")

    Call(0, 21)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 2710, 0, -330, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_20_560F end

    def Function_21_5DBA(): pass

    label("Function_21_5DBA")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【Choice 1: Accept】\x01",      # 0
            "【やめる】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E25")
    Call(0, 22)
    Jump("loc_5F08")

    label("loc_5E25")


    ChrTalk(
        0x101,
        (
            "#6P#00006F……すみません。\x01",
            "こちらも手持ちの仕事で\x01",
            "いっぱいいっぱいでして……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PHmm.\x01",
            "まあ、こんな時だから\x01",
            "仕方がないかもしれんな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P分かった、もし手が空くようなら\x01",
            "もう一度頼むことにしよう。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x19B, 3)

    label("loc_5F08")

    Return()

    # Function_21_5DBA end

    def Function_22_5F09(): pass

    label("Function_22_5F09")


    ChrTalk(
        0x101,
        "#6P#00000FRight, thanks a lot!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11Pうむ、恩に着るぞ。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P──依頼にも書いていたことだが、\x01",
            "近頃、謎の『黒い魔獣』が出るという\x01",
            "目撃情報が寄せられていてな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pアルモリカ村の付近などで\x01",
            "農作物や家畜などに\x01",
            "被害が出てしまっているらしい。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105F黒い魔獣……\x01",
            "どこかで聞いたことが\x01",
            "あるような印象ね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303F作物を襲うってのも\x01",
            "聞き覚えがあるような。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FCould it be\x01",
            "以前起こった『狼型魔獣』の事件に\x01",
            "似ているんじゃないですかね。\x02\x03",
            "#10103Fあの時は、マフィアの操る\x01",
            "軍用犬が犯人でしたけど……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P……俺もその事件は\x01",
            "報告書で読んでいたから、\x01",
            "気になっていてな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P実際、ルバーチェは解体されたが\x01",
            "所有していた軍用犬の多数は\x01",
            "行方が分からなくなっている。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11P可能性は決して低くはないだろう。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F警備隊ではどの程度\x01",
            "調査が進んでいるんですか？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P被害現場の検証と\x01",
            "周辺の住民への聞き込みは\x01",
            "軽く行ったってところだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pその結果、『黒い魔獣』は\x01",
            "古戦場方面から来ている\x01",
            "ということが判明した。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pそこでお前たちには、\x01",
            "古戦場に向かってもらいたい。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pこの魔獣たちの調査、\x01",
            "可能ならば退治をしてもらう。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302F事情はおおむね理解したよ。\x02\x03",
            "#10303Fにしても、やっぱり随分と\x01",
            "忙しいみたいだね？\x02\x03",
            "#10300Fこういう仕事は\x01",
            "警備隊でやるもんだと\x01",
            "思っていたけど……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pそうしたいところだが……\x01",
            "さっきも言ったように、\x01",
            "警備隊は厳戒態勢なんだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pクロスベル市襲撃犯と目される\x01",
            "Red Constellationも姿をくらまし、\x01",
            "尻尾すらつかめていない。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pさらに帝国と共和国が\x01",
            "巨大な演習を始めようと\x01",
            "しているこの状況……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_6547")

    ChrTalk(
        0x9,
        (
            "#11P先ほどのような事がないよう\x01",
            "警備隊としては、国境の警備は\x01",
            "特に厳重にする必要があるだろう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_658E")

    label("loc_6547")


    ChrTalk(
        0x9,
        (
            "#11P警備隊としては、国境の警備は\x01",
            "特に厳重にする必要があるだろう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_658E")


    ChrTalk(
        0x102,
        (
            "#6P#00108F《不戦条約》締結直前……\x01",
            "それに相当する状況に\x01",
            "なってしまっているわけTrue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11P……うむ。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pいくら魔獣被害といえども、\x01",
            "さすがにこの状況では、\x01",
            "優先順位が低くなってしまう。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pそこまで深刻な被害が\x01",
            "確認されてるわけじゃないし、\x01",
            "人を割くわけにはいかないのさ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304F……確かに、\x01",
            "警備隊に魔獣退治なんか\x01",
            "やらせてる場合じゃねえだろうな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F……状況は概ね分かりました。\x02\x03",
            "#00000Fそれでは、『黒い魔獣』の\x01",
            "調査はこちらにお任せください。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11Pうむ、すまない。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PよろしくWe're counting on you SSS\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【古戦場の調査】\x07\x00",
            "を開始した!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x19B, 4)
    OP_29(0x91, 0x1, 0x0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 2710, 0, -330, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_22_5F09 end

    def Function_23_6851(): pass

    label("Function_23_6851")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(3420, 1800, 80, 0)
    MoveCamera(44, 23, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, 2500, 0, -20, 90)
    SetChrPos(0x102, 2300, 0, -1020, 90)
    SetChrPos(0x103, 2300, 0, 980, 90)
    SetChrPos(0x104, 1000, 0, -20, 90)
    SetChrPos(0x109, 900, 0, 980, 90)
    SetChrPos(0x105, 900, 0, -1020, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_93(0x9, 0x10E, 0x0)
    OP_68(3420, 900, 80, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#6P#00000F──以上が今回の依頼の顛末です。\x02\x03",
            "#00003Fおそらく、これ以上軍用犬による\x01",
            "被害がでることはないと思います。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11P……I see…\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)

    ChrTalk(
        0x101,
        "#6P#00012Fえ、Uhm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00305Fなんだ、ダグラスの兄さん。\x01",
            "すっかり黙っちまってよ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F軍用犬を退治しなかったのは\x01",
            "やっぱマズかったでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11P……いや、上出来だろうぜ。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P予想を超えた結果なんで\x01",
            "ちょっとおどろいちまってな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300Fま、そうだろうね。\x02\x03",
            "#10309F『軍用犬を説得した』だなんて、\x01",
            "普通なら眉唾物の話だもの。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106Fた、確かに信じられない\x01",
            "かもしれないわね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200Fでも、事実ですから\x01",
            "何も問題はないかと。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11P……いや、結構だ。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P穏便な解決ができるなら\x01",
            "それに越したことはない。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pご苦労だったな、支援課諸君。\x01",
            "おかげで懸案していた事が\x01",
            "一つ片付いたぞ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00004Fそれは良かったです。\x02\x03",
            "#00000Fまた何かあったらいつでも\x01",
            "呼んでください。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11Pああ、そうさせてもらおう。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P──では、引き続き俺たちは\x01",
            "厳戒態勢を続ける。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11Pそちらも気をつけるようにな。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000F……Roger!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【古戦場の調査】\x07\x00",
            "を達成した!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x91, 0x1, 0x2)
    OP_29(0x91, 0x1, 0x3)
    OP_29(0x91, 0x4, 0x10)
    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 2710, 0, -330, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_23_6851 end

    SaveToFile()

Try(main)
