from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c0100_1.bin",                # FileName
        "c0100",                    # MapName
        "c0100",                    # Location
        0x0004,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 24000, 500, 30, 45, 0, 360, 1100, 0, -3500, 0, 0, 1, 4, 0, 7, 0, 8],
    )

    BuildStringList((
        "c0100_1",                # 0
    ))

    ChipFrameInfo(256, 0)                                        # 0

    ScpFunction((
        "Function_0_100",          # 00, 0
        "Function_1_DEA",          # 01, 1
        "Function_2_20A5",         # 02, 2
        "Function_3_2E47",         # 03, 3
        "Function_4_3498",         # 04, 4
        "Function_5_40FA",         # 05, 5
        "Function_6_4337",         # 06, 6
        "Function_7_4651",         # 07, 7
        "Function_8_4DCE",         # 08, 8
        "Function_9_4EE8",         # 09, 9
        "Function_10_56B2",        # 0A, 10
        "Function_11_605D",        # 0B, 11
        "Function_12_6304",        # 0C, 12
        "Function_13_6F23",        # 0D, 13
        "Function_14_7077",        # 0E, 14
        "Function_15_71D2",        # 0F, 15
        "Function_16_72FC",        # 10, 16
        "Function_17_7392",        # 11, 17
        "Function_18_73F8",        # 12, 18
        "Function_19_745B",        # 13, 19
        "Function_20_7594",        # 14, 20
        "Function_21_8EE3",        # 15, 21
        "Function_22_9453",        # 16, 22
        "Function_23_9614",        # 17, 23
        "Function_24_9B5A",        # 18, 24
        "Function_25_9CD7",        # 19, 25
        "Function_26_A1D0",        # 1A, 26
    ))


    def Function_0_100(): pass

    label("Function_0_100")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1A1")

    ChrTalk(
        0xFE,
        (
            "やっとお外に出られたと思ったら……\x01",
            "あの空に浮かんでいる樹は一体なんなの？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "まさかどこかに落ちて来ないわよね？\x01",
            "……はてしなく不安だわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE6")

    label("loc_1A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1AF")
    Jump("loc_DE6")

    label("loc_1AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_334")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29F")

    ChrTalk(
        0xFE,
        (
            "過去に起こった事故が、\x01",
            "２大国の“暗闘”によるものだった……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "それって、両国のスパイ同士が\x01",
            "お互いやり合った結果っていうこと？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……正直深く考えたことなかったけど、\x01",
            "もしそれが本当なら許せないことよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_32F")

    label("loc_29F")


    ChrTalk(
        0xFE,
        (
            "過去に起こった事故が、\x01",
            "２大国の“暗闘”によるものだった……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……正直深く考えたことなかったけど、\x01",
            "もしそれが本当なら許せないことよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32F")

    Jump("loc_DE6")

    label("loc_334")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_468")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EF")

    ChrTalk(
        0xFE,
        (
            "あの武装集団を雇ったのは\x01",
            "帝国政府だって噂But…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "そういう意味では、いつまた\x01",
            "襲ってくるか分からないのよね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "そう思うと、ものすごく不安だわ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_463")

    label("loc_3EF")


    ChrTalk(
        0xFE,
        (
            "あの武装集団を雇ったのは\x01",
            "帝国政府だって噂But…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "いつまた襲ってくるかと思うと、\x01",
            "ものすごく不安だわ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_463")

    Jump("loc_DE6")

    label("loc_468")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_505")

    ChrTalk(
        0xFE,
        (
            "マインツの人たち、きっと\x01",
            "今頃つらい思いをしてるわよね……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "武器を持った人たちが\x01",
            "突然乗り込んで来るだなんて、\x01",
            "想像するだけで怖いわ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE6")

    label("loc_505")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_572")

    ChrTalk(
        0xFE,
        "今日はママにお使いを頼まれたの。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……雨漏りしたから、\x01",
            "至急バケツを買って来てってね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE6")

    label("loc_572")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5CB")

    ChrTalk(
        0xFE,
        (
            "あんなに救急車が出動するなんて……\x01",
            "結構大きな事故が起こったみたいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE6")

    label("loc_5CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_655")

    ChrTalk(
        0xFE,
        "私って本当に一人暮らししたいのかな？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "確かに憧れはあるけど、\x01",
            "何だかんだ家に１人だけって\x01",
            "随分寂しい気がするわね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE6")

    label("loc_655")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_768")

    ChrTalk(
        0xFE,
        (
            "バイト、バイト……\x01",
            "無難な所ならウェイトレスとかかしら。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "けど、効率よく稼ぐなら\x01",
            "ホステスという選択肢も……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……いやいやいや、\x01",
            "私ってば、一体何考えてるのかしら。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "いくら稼ぎがよくてもオジサンの\x01",
            "お酒の相手なんて絶対に無理だからっ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_7B3")

    label("loc_768")


    ChrTalk(
        0xFE,
        (
            "一人暮らししたいならバイトしなきゃね……\x01",
            "どういう仕事が私向きかしら？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B3")

    Jump("loc_DE6")

    label("loc_7B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_97F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8EA")

    ChrTalk(
        0xFE,
        (
            "一人暮らしをするなら、個人的に\x01",
            "西通り方面が一番良いと思うんBut…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "家賃とか現実的な線を考えると、\x01",
            "結局、東通り方面に落ち着くのよね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "旧市街は流石に破格だけど、\x01",
            "何より治安が心配だし……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "っていうか、自立するなら\x01",
            "その前にバイトでも探さなくちゃね。\x01",
            "Hmm…\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_97A")

    label("loc_8EA")


    ChrTalk(
        0xFE,
        (
            "一人暮らしをするなら、個人的に\x01",
            "西通り方面が一番良いと思うんBut…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……っていうか、自立するなら\x01",
            "その前にバイトでも探さなくちゃね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_97A")

    Jump("loc_DE6")

    label("loc_97F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_9E0")

    ChrTalk(
        0xFE,
        "あら、もうこんな時間なのね。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "早くお家に帰って\x01",
            "ママのお手伝いをしないと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE6")

    label("loc_9E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A83")

    ChrTalk(
        0xFE,
        (
            "首脳たちのクロスベル入りも\x01",
            "終わってみればあっという間ね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "みんな車に乗ってたから\x01",
            "よく分からなかったけど……\x01",
            "ＶＩＰ感だけは伝わって来たわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE6")

    label("loc_A83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_BD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B37")

    ChrTalk(
        0xFE,
        (
            "明日から通商会議とだけあって、\x01",
            "流石にちょっと物々しい感じね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "さっき、巡回している\x01",
            "警察官に呼び止められて、\x01",
            "人生初の職務質問をされちゃったわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_BCC")

    label("loc_B37")


    ChrTalk(
        0xFE,
        (
            "職務質問なんて初めてだったけど、\x01",
            "何ていうか失礼しちゃうわよね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "誰だって家事手伝いだなんて\x01",
            "大きな声で言いたくないのに……\x01",
            "とんだ辱めだわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BCC")

    Jump("loc_DE6")

    label("loc_BD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_C4F")

    ChrTalk(
        0xFE,
        (
            "私、雨だからって家の中で\x01",
            "じっとしているのは嫌いなの。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "お気に入りの傘を差して、\x01",
            "レッツ・お散歩ってね♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE6")

    label("loc_C4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_DE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CD9")

    ChrTalk(
        0xFE,
        (
            "パトカーがいっぱい出てきて\x01",
            "びっくりしちゃったわ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "でも、なんだか警察らしくて\x01",
            "カッコよかったかも。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE6")

    label("loc_CD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D93")

    ChrTalk(
        0xFE,
        (
            "もう、うちのパパったらどうして\x01",
            "家の中を裸でうろうろするのかしら。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "年頃の娘に対する配慮に\x01",
            "欠けると言うか……もはや犯罪よね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "あ〜、一人暮らししたいな〜。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DE6")

    label("loc_D93")


    ChrTalk(
        0xFE,
        "あ〜、一人暮らししたいな〜。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "う〜ん、どこかに\x01",
            "いい物件はないものかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DE6")

    TalkEnd(0xFE)
    Return()

    # Function_0_100 end

    def Function_1_DEA(): pass

    label("Function_1_DEA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_FBD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F0D")

    ChrTalk(
        0xFE,
        (
            "詳細はよく判らんが、\x01",
            "どうやらあの《神機》とかいう\x01",
            "兵器は失われてしまったようじゃな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "方法の是非はともかく……\x01",
            "ディーター大統領は確かに\x01",
            "クロスベルを守る力を用意していた。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "結果、大きな混乱をもたらしたとはいえ、\x01",
            "わしは彼のことをとても責められんよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_FB8")

    label("loc_F0D")


    ChrTalk(
        0xFE,
        (
            "方法の是非はともかく……\x01",
            "ディーター大統領は確かに\x01",
            "クロスベルを守る力を用意していた。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "結果、大きな混乱をもたらしたとはいえ、\x01",
            "わしは彼のことをとても責められんよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FB8")

    Jump("loc_20A1")

    label("loc_FBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_FCB")
    Jump("loc_20A1")

    label("loc_FCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1133")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_109E")

    ChrTalk(
        0xFE,
        "Hmm.資産凍結を宣言、か。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "まさかディーター市長がここまでの\x01",
            "強硬策に出るとは思わなんだが……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "だが彼の言う通り、我々が立ち上がるには\x01",
            "今以外に時宜はないのかもしれんな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_112E")

    label("loc_109E")


    ChrTalk(
        0xFE,
        (
            "まさかディーター市長がここまでの\x01",
            "強硬策に出るとは思わなんだが……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "だが確かに、我々が立ち上がるには\x01",
            "今以外に時宜はないのかもしれんな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_112E")

    Jump("loc_20A1")

    label("loc_1133")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_12D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1236")

    ChrTalk(
        0xFE,
        (
            "先日の襲撃事件……\x01",
            "あれは帝国の仕業に決まっとる。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "最近は猫を被っていたようじゃが、\x01",
            "元来、手段を選ばぬのが奴らの本性……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "回りくどく、卑劣な手段を用いて\x01",
            "あわよくば侵略を目論Hmm\x01",
            "それがエレボニアというものじゃからな!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_12D3")

    label("loc_1236")


    ChrTalk(
        0xFE,
        (
            "先日の襲撃事件……\x01",
            "あれは帝国の仕業に決まっとる。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "回りくどく、卑劣な手段を用いて\x01",
            "あわよくば侵略を目論Hmm\x01",
            "それがエレボニアというものじゃからな!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12D3")

    Jump("loc_20A1")

    label("loc_12D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1370")

    ChrTalk(
        0xFE,
        "此度の事件、もしや背後には帝国が……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……ふむ、だとしたら\x01",
            "これまでと同じようにただ従うだけでは\x01",
            "クロスベルは守り切れんのかもな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20A1")

    label("loc_1370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_137E")
    Jump("loc_20A1")

    label("loc_137E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_146F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_141A")

    ChrTalk(
        0xFE,
        (
            "西の方で、何か\x01",
            "事故でもあったようじゃのう。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "くわばらくわばら……\x01",
            "空の女神#8Rエ イ ド ス#よ、どうか皆を護ってくだされ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_146A")

    label("loc_141A")


    ChrTalk(
        0xFE,
        (
            "くわばらくわばら……\x01",
            "空の女神#8Rエ イ ド ス#よ、どうか皆を護ってくだされ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_146A")

    Jump("loc_20A1")

    label("loc_146F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1593")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1536")

    ChrTalk(
        0xFE,
        (
            "一概には言えんが、\x01",
            "どうやら若い世代の方が\x01",
            "独立に賛成という者が多いようじゃな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "紛争を知らぬ世代、か……\x01",
            "事の深刻さが本当に分かって\x01",
            "おるのかどうか不安になるわい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_158E")

    label("loc_1536")


    ChrTalk(
        0xFE,
        (
            "紛争を知らぬ世代、か……\x01",
            "事の深刻さが本当に分かって\x01",
            "おるのかどうか不安になるわい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_158E")

    Jump("loc_20A1")

    label("loc_1593")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_169A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1660")

    ChrTalk(
        0xFE,
        (
            "ふむ、正直まさか\x01",
            "この歳になって独立という言葉を\x01",
            "耳にするとは思わんかったわい。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "独立、独立か……\x01",
            "確かに実現できれば夢のようじゃが、\x01",
            "果たしてうまく行くとも思えんのう……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1695")

    label("loc_1660")


    ChrTalk(
        0xFE,
        (
            "独立、独立か……\x01",
            "果たして叶う夢なのじゃろうか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1695")

    Jump("loc_20A1")

    label("loc_169A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_18A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1811")

    ChrTalk(
        0xFE,
        (
            "通商会議は傍聴などできんし、\x01",
            "導力通信で中継されるわけでもない。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "つまり、わしらはその結果を\x01",
            "市の広報と報道関係者を通して\x01",
            "知るわけじゃな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "特に一般的なのは、言わずと知れた\x01",
            "クロスベルタイムズじゃ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "記事の信頼性、安定性、スピード……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "どれを取っても、この地においては\x01",
            "クロスベルタイムズに勝る\x01",
            "情報源はなかなか存在せんのじゃよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_18A4")

    label("loc_1811")


    ChrTalk(
        0xFE,
        (
            "通商会議は傍聴などできんし、\x01",
            "導力通信で中継されるわけでもない。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "つまり、わしらはその結果を\x01",
            "市の広報と報道関係者を通して\x01",
            "知るわけじゃな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18A4")

    Jump("loc_20A1")

    label("loc_18A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_19E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_196E")

    ChrTalk(
        0xFE,
        (
            "おや、気付けばもうすっかり\x01",
            "日が暮れてしまっておるではないか。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "ほっほっ、これも通商会議の\x01",
            "空気にあてられたせいかのう。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "婆さんが心配せん内に早く帰らんとな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_19DB")

    label("loc_196E")


    ChrTalk(
        0xFE,
        (
            "おや、気付けばもうすっかり\x01",
            "日が暮れてしまっておるではないか。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "婆さんが心配せん内に早く帰らんとな。\x02",
    )

    CloseMessageWindow()

    label("loc_19DB")

    Jump("loc_20A1")

    label("loc_19E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1CB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A71")

    ChrTalk(
        0xFE,
        (
            "先ほど、そこのレストランに\x01",
            "東方風の女性が入っていったぞい。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "理知的な顔をした\x01",
            "美しい女性じゃったのう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CAB")

    label("loc_1A71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C0E")

    ChrTalk(
        0xFE,
        (
            "ふむ、新市庁ビルが\x01",
            "ようやっとその姿を現したか。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "建築計画の発表から実に５年。\x01",
            "噂では完成まで最低でもあと１年は\x01",
            "かかると言われておったんじゃが……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "クロイス市長の就任直後にＩＢＣの\x01",
            "資本を投入することが決定してな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "おかげで、くだらん利権争いに\x01",
            "影響されることなく急ピッチで工事が進み、\x01",
            "ついに先日完成に至ったというわけじゃ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "ほっほっ、まっこと\x01",
            "クロイス市長さまさまじゃのう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1CAB")

    label("loc_1C0E")


    ChrTalk(
        0xFE,
        (
            "建築計画の発表から実に５年。\x01",
            "噂では完成まで最低でもあと１年は\x01",
            "かかると言われておったんじゃが……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "ほっほっ、まっこと\x01",
            "クロイス市長さまさまじゃのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CAB")

    Jump("loc_20A1")

    label("loc_1CB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1E23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D99")

    ChrTalk(
        0xFE,
        (
            "ふむ、明日からいよいよ\x01",
            "通商会議が始まるわけじゃな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "提唱者のクロイス市長は\x01",
            "何と言っても、市長であると同時に\x01",
            "かのＩＢＣの総裁じゃ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "会議ではそのリーダーシップを\x01",
            "存分に発揮してもらわんとのう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E1E")

    label("loc_1D99")


    ChrTalk(
        0xFE,
        (
            "ふむ、明日からいよいよ\x01",
            "通商会議が始まるわけじゃな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "クロイス市長には、\x01",
            "そのリーダーシップを存分に\x01",
            "発揮してもらわんとのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E1E")

    Jump("loc_20A1")

    label("loc_1E23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1E31")
    Jump("loc_20A1")

    label("loc_1E31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_20A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EA9")

    ChrTalk(
        0xFE,
        (
            "ここからも、さっきの\x01",
            "逮捕劇が見えたよ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "警察もなかなか\x01",
            "がんばっとるようじゃな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20A1")

    label("loc_1EA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FDB")

    ChrTalk(
        0xFE,
        (
            "教団事件に絡んだ帝国・共和国派の\x01",
            "汚職議員が消え、裏社会からは\x01",
            "あのルバーチェ商会までもが消えた。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "じゃがそれでも、\x01",
            "未だ帝国派議員が議席数で\x01",
            "トップを行く現状は変わっておらん。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "法改正のスピードアップなど\x01",
            "健闘は伺えるが……クロイス市長には\x01",
            "もっともっと頑張ってもらわんとのう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_20A1")

    label("loc_1FDB")


    ChrTalk(
        0xFE,
        "……確か黒月じゃったか。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "ルバーチェがいなくなって、\x01",
            "ヤツラが幅を利かせ始めた\x01",
            "という噂もある。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "市民が安心して暮らせる法作り……\x01",
            "クロイス市長には、もっともっと\x01",
            "頑張ってもらわんとのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20A1")

    TalkEnd(0xFE)
    Return()

    # Function_1_DEA end

    def Function_2_20A5(): pass

    label("Function_2_20A5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2147")

    ChrTalk(
        0xFE,
        (
            "さてと、僕はこれから\x01",
            "オルキスタワーの方に戻るとするよ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "市役所も混乱の最中だろうけど、\x01",
            "とにかく顔を出さないことには\x01",
            "始まらないからね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E43")

    label("loc_2147")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2155")
    Jump("loc_2E43")

    label("loc_2155")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2163")
    Jump("loc_2E43")

    label("loc_2163")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_22C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2235")

    ChrTalk(
        0xFE,
        "はは、ミミは無邪気で可愛いなぁ。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "しかし、それにしても\x01",
            "武装集団はなぜクロスベルの鐘を\x01",
            "持ち去ったんだろうね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "盗んだって、そんなに価値の\x01",
            "あるものとは思えないんBut…\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_22C0")

    label("loc_2235")


    ChrTalk(
        0xFE,
        (
            "それにしても、\x01",
            "武装集団はなぜクロスベルの鐘を\x01",
            "持ち去ったんだろうね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "盗んだって、そんなに価値の\x01",
            "あるものとは思えないんBut…\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22C0")

    Jump("loc_2E43")

    label("loc_22C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_231C")

    ChrTalk(
        0xFE,
        (
            "マインツの人たち、心配だね……\x01",
            "ミミくらいの子たちもいるだろうに……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E43")

    label("loc_231C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2385")

    ChrTalk(
        0xFE,
        "ほらミミ、見てごらん。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "でんでん虫さんが、手すりの上を\x01",
            "行ったり来たりしているよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E43")

    label("loc_2385")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2424")

    ChrTalk(
        0xFE,
        (
            "当たり前のことBut…\x01",
            "救急車、かなり急いでたね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "ああいった緊急車両には\x01",
            "スピード制限がないとはいえ、\x01",
            "見ていると少しヒヤヒヤするよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E43")

    label("loc_2424")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_25A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_251D")

    ChrTalk(
        0xFE,
        "う〜ん、やはり導力車はいいよな〜。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "だが、いかんせん\x01",
            "まだまだ相場が高すぎて\x01",
            "庶民には手を出せないんだよ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今の半分、はまだまだ難しいとしても\x01",
            "２割程度下がってくれるだけでも\x01",
            "かなり手が出しやすくなるんだけどね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_25A1")

    label("loc_251D")


    ChrTalk(
        0xFE,
        "う〜ん、やはり導力車はいいよな〜。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今すぐにはとても無理だけど、\x01",
            "せめて僕が定年を迎える頃には\x01",
            "何としても手に入れたいなぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25A1")

    Jump("loc_2E43")

    label("loc_25A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2797")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26ED")

    ChrTalk(
        0xFE,
        (
            "最近、世間では\x01",
            "独立についての話にばかり\x01",
            "注目が行っているみたいBut…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "つい先日、交通基本法の改正が\x01",
            "行われたことも忘れないで欲しいね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今度の法改正では、\x01",
            "これまでの罰金制度に加えて\x01",
            "『免許停止制度』が加わったんだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "これで少しでも導力車による\x01",
            "事故が減ってくれることを願ってるよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2792")

    label("loc_26ED")


    ChrTalk(
        0xFE,
        (
            "今後は一定以上の違反を犯すと、\x01",
            "一定期間、運転免許が停止……\x01",
            "つまり運転ができなくなるんだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "これで少しでも導力車による\x01",
            "事故が減ってくれることを願ってるよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2792")

    Jump("loc_2E43")

    label("loc_2797")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_27A5")
    Jump("loc_2E43")

    label("loc_27A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_2806")

    ChrTalk(
        0xFE,
        (
            "さてと、待たせてしまって\x01",
            "すまなかったね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "それじゃ、早速行くとしようか。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E43")

    label("loc_2806")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2814")
    Jump("loc_2E43")

    label("loc_2814")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_289A")

    ChrTalk(
        0xFE,
        (
            "市庁舎の完全移転に伴って、\x01",
            "しばらくの間オルキスタワーに\x01",
            "詰めることになったんだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "さてと、忙しくなりそうだぞ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E43")

    label("loc_289A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2C1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BAC")

    ChrTalk(
        0xFE,
        (
            "昨日見かけたんBut…\x01",
            "君たち、随分珍しい導力車に\x01",
            "乗っているみたいだね？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000Fはい、実は\x01",
            "ＺＣＦの新型導力車なんです。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)

    ChrTalk(
        0xFE,
        "なんだって、あのＺＣＦが導力車を!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "ち、ちなみに、最高時速は分かるかい？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102Fええ、まだ試してはいないんですが、\x01",
            "１５００セルジュは固いみたいTrue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "な、なんと…!\x01",
            "あの型でそのスピードとは、\x01",
            "ＺＣＦもやってくれたね!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "う〜ん、何ということだ。\x01",
            "これで導力車メーカーも\x01",
            "いよいよ３強時代に突入かぁ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "ふむ、こうなると今後が\x01",
            "ますます楽しみになってしまうね!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109Fですよね〜!\x02\x03",
            "これで競争がますます過熱して、\x01",
            "もっと凄い子たちがどんどん……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x109, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)

    ChrTalk(
        0x101,
        "#00012Fず、随分と盛り上がってるな。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109Fふふ、ノエルさんも本当に好きよね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12E, 0)
    Jump("loc_2C1A")

    label("loc_2BAC")


    ChrTalk(
        0xFE,
        (
            "まさか、あのＺＣＦが\x01",
            "導力車を開発してたとはね!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "ふむむ、これは今後とも\x01",
            "各社の動向に目が離せないよ!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C1A")

    Jump("loc_2E43")

    label("loc_2C1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2E43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CA5")

    ChrTalk(
        0xFE,
        (
            "やはり交通法の整備は\x01",
            "早急にしてもらわないとね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "ミミを１人で遊ばせるのが\x01",
            "怖くなってしまうよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E43")

    label("loc_2CA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D87")

    ChrTalk(
        0xFE,
        (
            "この前、物凄いスピードで\x01",
            "この中央広場を駆け抜ける\x01",
            "導力車を見かけたんだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "明らかに危険な速度だったから、\x01",
            "すぐに警察に通報したんBut…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "ちゃんと捕まっただろうか。\x01",
            "……また現れないか心配だよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2E43")

    label("loc_2D87")


    ChrTalk(
        0xFE,
        (
            "とはいえ、現在の交通基本法では\x01",
            "たとえ危険運転で捕まっても\x01",
            "罰金だけで済んでしまうんだけどさ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "ただ最近は、議会でも\x01",
            "罰則の強化に踏み出している所だから\x01",
            "今後に期待はしているけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E43")

    TalkEnd(0xFE)
    Return()

    # Function_2_20A5 end

    def Function_3_2E47(): pass

    label("Function_3_2E47")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2EFB")

    ChrTalk(
        0xFE,
        (
            "旦那が市役所に戻るというので\x01",
            "私たちも家の方に帰ろうと思います。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "この先も色々と不安ですが……\x01",
            "家族が一緒にいる限りは、\x01",
            "何でも乗り切れそうな気がしますね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3494")

    label("loc_2EFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2F09")
    Jump("loc_3494")

    label("loc_2F09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2FAA")

    ChrTalk(
        0xFE,
        (
            "仕方のないことですが……\x01",
            "この一週間で観光客の姿を\x01",
            "ほとんど見かけなくなりましたね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……クロスベルはこの先\x01",
            "どうなって行くんでしょうか……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3494")

    label("loc_2FAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3044")

    ChrTalk(
        0xFE,
        (
            "ガイドの仕事は当分お休みなので、\x01",
            "今は家族３人で過ごしているんです。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "先のことは色々と不安ですけど……\x01",
            "子供の笑顔には救われますね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3494")

    label("loc_3044")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3052")
    Jump("loc_3494")

    label("loc_3052")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3060")
    Jump("loc_3494")

    label("loc_3060")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_306E")
    Jump("loc_3494")

    label("loc_306E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_307C")
    Jump("loc_3494")

    label("loc_307C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_308A")
    Jump("loc_3494")

    label("loc_308A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_325C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31AE")

    ChrTalk(
        0xFE,
        "えー、コホン。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "皆様の右手後方に見えますのは、\x01",
            "《オーバルストア》でございます。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "その名も《ゲンテン》と言いまして、\x01",
            "大陸中の導力製品が集まる\x01",
            "お店として有名なんです。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "市民はもちろん、\x01",
            "観光客の皆さんにも人気のある\x01",
            "時代の最先端を行くお店なんですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3257")

    label("loc_31AE")


    ChrTalk(
        0xFE,
        (
            "えー、皆様の右手後方に見えますのは、\x01",
            "オーバルストア《ゲンテン》でございます。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "市民はもちろん、\x01",
            "観光客の皆さんにも人気のある\x01",
            "時代の最先端を行くお店なんですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3257")

    Jump("loc_3494")

    label("loc_325C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_32A3")

    ChrTalk(
        0xFE,
        (
            "ええ、早く行きましょう。\x01",
            "ミミも私もお腹ペコペコよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3494")

    label("loc_32A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_346F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32BE")
    Call(1, 6)
    Jump("loc_346A")

    label("loc_32BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33D8")

    ChrTalk(
        0xFE,
        "えー、コホン。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "皆様の右手に見えますのは、\x01",
            "《クロスベルの鐘》でございます。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "その起源は古く５００年以上も前、\x01",
            "中世の時代に遡ると言われております。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "七耀暦１１８５年に発掘されて以来、\x01",
            "今ではすっかり街の象徴として\x01",
            "市民の間で親しまれているんですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_346A")

    label("loc_33D8")


    ChrTalk(
        0xFE,
        (
            "えー、皆様の右手に見えますのは、\x01",
            "《クロスベルの鐘》でございます。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "その起源は古く５００年以上も前、\x01",
            "中世の時代に遡ると言われております。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_346A")

    Jump("loc_3494")

    label("loc_346F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_347D")
    Jump("loc_3494")

    label("loc_347D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_348B")
    Jump("loc_3494")

    label("loc_348B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3494")

    label("loc_3494")

    TalkEnd(0xFE)
    Return()

    # Function_3_2E47 end

    def Function_4_3498(): pass

    label("Function_4_3498")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_35DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_357E")

    ChrTalk(
        0xFE,
        (
            "パパ、これからまた\x01",
            "お仕事に行くんだって〜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "そういえば、ロイド君たちも\x01",
            "ずっとお仕事中なんだよね？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "ミミ、みんなのこともずっと\x01",
            "応援してるからがんばってね!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000Fああ、ありがとう。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_35D5")

    label("loc_357E")


    ChrTalk(
        0xFE,
        (
            "パパもロイド君たちも\x01",
            "お仕事がんばってて偉いよね〜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "ミミも応援がんばるのっ。\x02",
    )

    CloseMessageWindow()

    label("loc_35D5")

    Jump("loc_40F6")

    label("loc_35DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_35E8")
    Jump("loc_40F6")

    label("loc_35E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_36BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3652")

    ChrTalk(
        0xFE,
        (
            "あの画面付きの導力車、\x01",
            "かっこよかったねー。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "お父さんが喜びそうなの。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_36B6")

    label("loc_3652")


    ChrTalk(
        0xFE,
        (
            "お父さん、市役所の仕事が\x01",
            "忙しくなったんだって。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "逆にお母さんのいる\x01",
            "旅行会社は休業中なの。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36B6")

    Jump("loc_40F6")

    label("loc_36BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_378C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3750")

    ChrTalk(
        0xFE,
        (
            "えー、みな様の右手にみえますのは\x01",
            "クロスベルのかねでございま〜すっ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "ってアレレ？\x01",
            "かねがどこかに行っちゃったよ？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3787")

    label("loc_3750")


    ChrTalk(
        0xFE,
        (
            "クロスベルのかね、\x01",
            "どこに行っちゃったんだろうね？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3787")

    Jump("loc_40F6")

    label("loc_378C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_38E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3882")

    ChrTalk(
        0xFE,
        (
            "なんか、今日は\x01",
            "むつかしい顔してる人が多いね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "あ、ロイドくんたちも……\x01",
            "ダメだよ、元気出さなきゃっ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000Fあ、うん、そうだね。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100Fありがとう、ミミちゃん。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "ううん。\x01",
            "どういたしまして、だよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_38DF")

    label("loc_3882")


    ChrTalk(
        0xFE,
        (
            "なんか、今日は\x01",
            "むつかしい顔してる人が多いね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "みんな、太陽さんに笑われちゃうぞっ。\x02",
    )

    CloseMessageWindow()

    label("loc_38DF")

    Jump("loc_40F6")

    label("loc_38E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_392C")

    ChrTalk(
        0xFE,
        "わー、ほんとだっ。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "もしかして迷子さんなのかな？\x02",
    )

    CloseMessageWindow()
    Jump("loc_40F6")

    label("loc_392C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_399C")

    ChrTalk(
        0xFE,
        (
            "救急車が通ったらね、\x01",
            "みんな道をゆずらなくちゃ\x01",
            "いけないんだよ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "それが交通ルールなのっ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_40F6")

    label("loc_399C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3A57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A1C")

    ChrTalk(
        0xFE,
        "ぷっぷ〜、ぷっぷ〜。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "お父さん、また\x01",
            "車のこと考えてるみたいなの。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "ほんと好きだよね〜。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3A52")

    label("loc_3A1C")


    ChrTalk(
        0xFE,
        "ぷっぷ〜、ぷっぷ〜。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "助手席はミミのものっ。\x02",
    )

    CloseMessageWindow()

    label("loc_3A52")

    Jump("loc_40F6")

    label("loc_3A57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3B1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AC7")

    ChrTalk(
        0xFE,
        (
            "えー、みなさまの\x01",
            "右手にみえますのは……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "???\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "あれ、右手は右手だよ？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3B18")

    label("loc_3AC7")


    ChrTalk(
        0xFE,
        (
            "うーんと、お母さん\x01",
            "なんて言ってたんだっけ？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "右手にみえるのは……右手？\x02",
    )

    CloseMessageWindow()

    label("loc_3B18")

    Jump("loc_40F6")

    label("loc_3B1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3BA1")

    ChrTalk(
        0xFE,
        "ふむふむ、なるほどなるほどー。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "これはぜひ、何かお土産を\x01",
            "買って行くしかありませんなー。\x01",
            "パシャッ、パシャッ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40F6")

    label("loc_3BA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_3C04")

    ChrTalk(
        0xFE,
        "外食、外食、今日は外食♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "ミミ、東通りのお店の\x01",
            "『ちゅーか』が食べたいのっ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40F6")

    label("loc_3C04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3C92")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C1F")
    Call(1, 6)
    Jump("loc_3C8D")

    label("loc_3C1F")


    ChrTalk(
        0xFE,
        "ふむふむ、なるほどなるほどー。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "これはぜひとも写真に\x01",
            "収めないといけませんねー。\x01",
            "パシャッ、パシャッ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C8D")

    Jump("loc_40F6")

    label("loc_3C92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3F8F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EAC")
    TurnDirection(0xB, 0x1A2, 0)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "あ、ロイド君たちが\x01",
            "ミミのしらない子を連れてるー。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "えへへ、その服かっこいいね。\x01",
            "とーほー風っていうんだっけー？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        (
            "ほう、この服の良さに気付くとは\x01",
            "お前なかなか見込みがあるな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "フフン、これは世界に一着しかない\x01",
            "オーダーメイドなんだぞ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "おーだーめいどー？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "へえ、それって\x01",
            "メイドさんの服だったんだー。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        "いや、そうじゃなくって……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F（はは、この２人のやり取りも\x01",
            "  何だか新鮮で面白いな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DC, 6)
    Jump("loc_3F1A")

    label("loc_3EAC")

    TurnDirection(0xB, 0x1A2, 0)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "メイドさんかー。\x01",
            "あれれ、君って実は女の子？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        "だから違うって……\x02",
    )

    CloseMessageWindow()

    label("loc_3F1A")

    Jump("loc_3F8A")

    label("loc_3F1F")


    ChrTalk(
        0xFE,
        (
            "お父さん、しばらくミミと\x01",
            "遊んでくれなくなっちゃうんだって。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "でも、お仕事だから我慢しないとねー。\x02",
    )

    CloseMessageWindow()

    label("loc_3F8A")

    Jump("loc_40F6")

    label("loc_3F8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4044")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FAA")
    Call(1, 5)
    Jump("loc_403F")

    label("loc_3FAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4000")

    ChrTalk(
        0xFE,
        "ぴっちぴっち、ぴっちぴっち♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "今日は雨だね〜、そんだけっ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_403F")

    label("loc_4000")


    ChrTalk(
        0xFE,
        (
            "ミミのお父さんは\x01",
            "導力車に目がないのっ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "どんだけっ。\x02",
    )

    CloseMessageWindow()

    label("loc_403F")

    Jump("loc_40F6")

    label("loc_4044")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_40F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_40A7")

    ChrTalk(
        0xFE,
        (
            "車は、ルールを守って\x01",
            "乗りましょう。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "ミミでも知ってるよ〜。\x02",
    )

    CloseMessageWindow()
    Jump("loc_40F6")

    label("loc_40A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40B9")
    Call(1, 5)
    Jump("loc_40F6")

    label("loc_40B9")


    ChrTalk(
        0xFE,
        (
            "ニュー・とくむしえんかのみんな。\x01",
            "お仕事がんばってね〜。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40F6")

    TalkEnd(0xFE)
    Return()

    # Function_4_3498 end

    def Function_5_40FA(): pass

    label("Function_5_40FA")


    ChrTalk(
        0xB,
        (
            "あ、ロイドくんにエリィちゃん!\x01",
            "それに……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "あれぇ、ティオちゃんと\x01",
            "ランディくんは？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "とくむしえんかは、\x01",
            "まだしばらくお休みなの？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012Fいや、そういうわけじゃ\x01",
            "ないんBut…\x02\x03",
            "#00000F２人はまだ\x01",
            "他にやるべき仕事があってね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100Fええ、それとこの２人は\x01",
            "特務支援課の新しいメンバーなのよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xB,
        "へえ、そうなんだー。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "それじゃ、これからは\x01",
            "ニュー・とくむしえんかだね♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302Fはは、なかなかどうして\x01",
            "的確なネーミングじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109Fふふ、これからもよろしくね。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "うん、よろしくー!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12E, 1)
    Return()

    # Function_5_40FA end

    def Function_6_4337(): pass

    label("Function_6_4337")

    OP_4B(0xB, 0xFF)
    OP_4B(0xF, 0xFF)
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xB, 0x0, 0)
    TurnDirection(0xF, 0x0, 0)

    ChrTalk(
        0xB,
        "あっ、ロイドくんたちだ。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "ミミのお母さんを紹介するね。\x01",
            "観光ガイドさんをしているの。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "ふふ、はじめまして。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "いつも娘のことを\x01",
            "構って下さっているみたいで\x01",
            "That's fine, thank you\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000Fいえ、そんな\x01",
            "大したことはしてませんが。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100Fそれにしても、観光ガイドを\x01",
            "されているなんて素敵True.\x02\x03",
            "今日もお仕事なんですか？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "いえ、それが通商会議の間は\x01",
            "お休みをいただきまして。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "なので、その間はこの子と\x01",
            "一緒に過ごすつもりなんです。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302Fふうん、なのに制服なんだね？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "ええ、それが……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "ミミがお願いして着てもらったんだよ。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "これからガイドさんごっこするの。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302Fはは、なるほどな。\x01",
            "そいつは良かったじゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "うん、そうなのっ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "ロイド君たちも\x01",
            "気を付けて行ってらっしゃーい。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xF, 0x0, 0x0)
    OP_93(0xB, 0x0, 0x0)
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0xB, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0xF, 0xFF)
    SetScenarioFlags(0x14A, 2)
    Return()

    # Function_6_4337 end

    def Function_7_4651(): pass

    label("Function_7_4651")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_468D")

    ChrTalk(
        0xFE,
        (
            "なにあの巨大な樹……\x01",
            "ありえなくない？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DCA")

    label("loc_468D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_469B")
    Jump("loc_4DCA")

    label("loc_469B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_46D1")

    ChrTalk(
        0xFE,
        "アリオス様、超かっこよかったね〜!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4DCA")

    label("loc_46D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4747")

    ChrTalk(
        0xFE,
        (
            "今日は行政区の方で\x01",
            "チャリティイベントってのを\x01",
            "やってるみたいじゃん。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "ちょっと見に行ってみる？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4DCA")

    label("loc_4747")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4806")

    ChrTalk(
        0xFE,
        (
            "謎の武装集団だなんて怖すぎだよね。\x01",
            "ああいう連中に舐められないためにも\x01",
            "独立すべきだってパパは言うけど……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "住民投票かぁ、アタシたちも\x01",
            "１８だったら投票できたんだけどね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DCA")

    label("loc_4806")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4814")
    Jump("loc_4DCA")

    label("loc_4814")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4863")

    ChrTalk(
        0xFE,
        (
            "救急車、凄い勢いだったね。\x01",
            "……急いで事故らなきゃいいけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DCA")

    label("loc_4863")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_48E4")

    ChrTalk(
        0xFE,
        "えー、ダイエット止めちゃうの!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "むむむ、妙に潔い顔をしてからに……\x01",
            "私はアンタみたいにはならないわよ!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DCA")

    label("loc_48E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4949")

    ChrTalk(
        0xFE,
        ".............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……何でもするなら、\x01",
            "運動するか、食事制限すれば？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DCA")

    label("loc_4949")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_49E6")

    ChrTalk(
        0xFE,
        (
            "ねえねえ、アリオス様と\x01",
            "アルバート大公って、\x01",
            "何でも凄く仲が良いらしいわね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "いいな〜、できるものなら\x01",
            "アタシもお２人と仲良くした〜い!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DCA")

    label("loc_49E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_4A58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A06")
    Call(1, 8)
    ClearChrFlags(0xC, 0x10)
    Jump("loc_4A53")

    label("loc_4A06")


    ChrTalk(
        0xFE,
        "ふーん、なるほどね〜。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "（……この調子だと\x01",
            "  全然やってないわね。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A53")

    Jump("loc_4DCA")

    label("loc_4A58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4B1A")

    ChrTalk(
        0xFE,
        (
            "アルバート大公、見た!?\x01",
            "あのアゴ髭、素敵すぎじゃない？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "オズボーン宰相もカッコイイんだけど、\x01",
            "ちょっと近寄りがたいって言うかぁ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "でも、２人ともイイ髭してるわよね〜。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4DCA")

    label("loc_4B1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4BC7")

    ChrTalk(
        0xFE,
        (
            "アリオス様はもちろんだけど、\x01",
            "やっぱりディーター市長も素敵よね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "ま、恋人にしたいってよりは\x01",
            "理想のパパって感じだけど。\x01",
            "私を養子にしてくれないかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DCA")

    label("loc_4BC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4BD5")
    Jump("loc_4DCA")

    label("loc_4BD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4DCA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C2F")

    ChrTalk(
        0xFE,
        "……はい？　何か用？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "今ちょっと忙しいんだけど〜。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4DCA")

    label("loc_4C2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D02")

    ChrTalk(
        0xFE,
        (
            "さっき、赤毛の変なオトコに\x01",
            "ナンパされちゃったの。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "結構かっこよかったけど\x01",
            "タイプじゃないのよね〜って言ったら、\x01",
            "『オレもだ、気にすんな☆』って……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "ム、ムカツク〜!!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4D65")

    label("loc_4D02")


    ChrTalk(
        0xFE,
        (
            "フツー、自分からナンパしといて\x01",
            "『オレもタイプじゃない』なんて言う!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "ム、ムカツク〜!!\x02",
    )

    CloseMessageWindow()

    label("loc_4D65")

    Jump("loc_4DCA")

    label("loc_4D6A")


    ChrTalk(
        0xFE,
        (
            "宿題〜？\x01",
            "そんなのするわけないじゃん。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "そういえばさー、\x01",
            "アリオス様、また出張らしいよ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DCA")

    TalkEnd(0xFE)
    Return()

    # Function_7_4651 end

    def Function_8_4DCE(): pass

    label("Function_8_4DCE")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xC,
        (
            "そういえば、リナリーって\x01",
            "ジョギング続けてんの？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "え、あ、Yeah…\x01",
            "まあ、それなりにはね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "無理してダイエットってのも\x01",
            "良くないって思ったから、\x01",
            "最近は気が向いたらBut…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "ふ〜ん、そうなんだ。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "（……この調子だと\x01",
            "  全然やってないわね。）\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 6)
    SetScenarioFlags(0x0, 7)
    Return()

    # Function_8_4DCE end

    def Function_9_4EE8(): pass

    label("Function_9_4EE8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4F59")

    ChrTalk(
        0xFE,
        (
            "うん、青白い光が\x01",
            "綺麗な気もするけど……\x01",
            "超不気味だね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "これから何が起こるんだろう……\x02",
    )

    CloseMessageWindow()
    Jump("loc_56AE")

    label("loc_4F59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4F67")
    Jump("loc_56AE")

    label("loc_4F67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4FE9")

    ChrTalk(
        0xFE,
        (
            "うんうん、あの白い軍服姿も\x01",
            "物凄く似合ってたし。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "アリオスさんがいれば、\x01",
            "何が起きても大丈夫って思えるよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56AE")

    label("loc_4FE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_505E")

    ChrTalk(
        0xFE,
        (
            "そうだね、ああいうのって\x01",
            "参加することに意義があるらしいし。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "何なら他にも誰か誘って行こうよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_56AE")

    label("loc_505E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_50E5")

    ChrTalk(
        0xFE,
        "あたしたち、まだ１５歳だもんね。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "でも独立の是非なんてよく分からないし……\x01",
            "正直、投票できなくてほっとしたかも。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56AE")

    label("loc_50E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_50F3")
    Jump("loc_56AE")

    label("loc_50F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5140")

    ChrTalk(
        0xFE,
        (
            "もう、プルーナってば\x01",
            "そんな物騒なこと言っちゃダメだって。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56AE")

    label("loc_5140")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_51A5")

    ChrTalk(
        0xFE,
        "……私、決めた。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "ダイエットは諦めて、今の私を\x01",
            "好きでいてくれる男性を探すわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56AE")

    label("loc_51A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_521A")

    ChrTalk(
        0xFE,
        (
            "はぁ〜、運動も食事制限もない\x01",
            "ダイエット方法ってないのかしら。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "何でもするから誰か教えてよ〜!\x02",
    )

    CloseMessageWindow()
    Jump("loc_56AE")

    label("loc_521A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_52BF")

    ChrTalk(
        0xFE,
        (
            "そういえばアリオスさんって\x01",
            "レミフェリア公国から勲章を\x01",
            "授与されたことがあるのよね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "お２人が仲良くなったのは、\x01",
            "それがきっかけだったのかしら？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56AE")

    label("loc_52BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_535C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52DF")
    Call(1, 8)
    ClearChrFlags(0xC, 0x10)
    Jump("loc_5357")

    label("loc_52DF")


    ChrTalk(
        0xFE,
        (
            "き、気が向いたらって言っても\x01",
            "ちゃんと続けてはいるんだからね？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "えっと、それじゃあ、\x01",
            "今日は走って帰ろうかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5357")

    Jump("loc_56AE")

    label("loc_535C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_54D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_543D")

    ChrTalk(
        0xFE,
        (
            "髭髭髭って……\x01",
            "ほんとプルーナも好きよね〜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "それより私は\x01",
            "オリヴァルト皇子の隣にいた\x01",
            "背の高い軍人さんがタイプかな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一度でいいから、ああいう体格の人に\x01",
            "お姫様抱っこをしてもらいたいわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_54D2")

    label("loc_543D")


    ChrTalk(
        0xFE,
        (
            "それより私は\x01",
            "オリヴァルト皇子の隣にいた\x01",
            "背の高い軍人さんがタイプかな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一度でいいから、ああいう体格の人に\x01",
            "お姫様抱っこをしてもらいたいわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54D2")

    Jump("loc_56AE")

    label("loc_54D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5553")

    ChrTalk(
        0xFE,
        (
            "確かにディーター市長は\x01",
            "理想のパパかもね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "とりあえず、うちのパパみたいに\x01",
            "オヤジ臭もしなさそうだし。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56AE")

    label("loc_5553")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5561")
    Jump("loc_56AE")

    label("loc_5561")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_56AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_55CE")

    ChrTalk(
        0xFE,
        "危険運転？　知らな〜い。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "あたしたちおしゃべりに\x01",
            "熱中してたもんね〜。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56AE")

    label("loc_55CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_564D")

    ChrTalk(
        0xFE,
        (
            "……あの赤毛のお兄さん、\x01",
            "なんかヘンな人だったね〜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "百貨店に入っていったけど、\x01",
            "何者だったんだろ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56AE")

    label("loc_564D")


    ChrTalk(
        0xFE,
        (
            "あ〜、そういえば今日って\x01",
            "夕方から日曜学校だったよね〜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "プルーナは前に出た宿題やった？\x02",
    )

    CloseMessageWindow()

    label("loc_56AE")

    TalkEnd(0xFE)
    Return()

    # Function_9_4EE8 end

    def Function_10_56B2(): pass

    label("Function_10_56B2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5742")

    ChrTalk(
        0xFE,
        (
            "な、なんであんな\x01",
            "でっかい樹が宙に浮いてんだ？\x01",
            "物理的にありえねえし。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "ってか、俺はここで\x01",
            "風船を配ってていいのか.......?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6059")

    label("loc_5742")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5750")
    Jump("loc_6059")

    label("loc_5750")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5803")

    ChrTalk(
        0xFE,
        (
            "クロスベル独立国か……\x01",
            "マジですげえことになって来たな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "浮かれるような雰囲気でもないけど、\x01",
            "とりあえず建国記念ってことで\x01",
            "オリジナル風船でも作るとすっかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6059")

    label("loc_5803")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5811")
    Jump("loc_6059")

    label("loc_5811")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_58A3")

    ChrTalk(
        0xFE,
        (
            "武装集団だが何だか知らないけど、\x01",
            "全くとんでもない事をするよな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "風船やるから今すぐどっか行けって\x01",
            "言ってやりたい気分だよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6059")

    label("loc_58A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_58B1")
    Jump("loc_6059")

    label("loc_58B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_592D")

    ChrTalk(
        0xFE,
        (
            "風船はいかが〜？\x01",
            "……何て言ってる空気じゃない感じRight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "う〜ん、事故って\x01",
            "一体何があったんだろうな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6059")

    label("loc_592D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5A25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59C8")

    ChrTalk(
        0xFE,
        "風船はいかが〜？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "大人の方も恥ずかしがらずに\x01",
            "ぜひどうぞ〜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "たまには難しいことを忘れて\x01",
            "童心に返ってみませんか〜？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5A20")

    label("loc_59C8")


    ChrTalk(
        0xFE,
        (
            "大人の方も恥ずかしがらずに\x01",
            "ぜひどうぞ〜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "たまには\x01",
            "童心に返ってみませんか〜？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A20")

    Jump("loc_6059")

    label("loc_5A25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5B79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B13")

    ChrTalk(
        0xFE,
        (
            "この前、観光客の子供に\x01",
            "『風船はなぜ浮かぶの？』\x01",
            "って聞かれたんだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "そこで俺はすかさず\x01",
            "『夢が詰まってるからさ』\x01",
            "って答えたんBut…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "最近の子供ってひどいもんRight.\x01",
            "言ったそばから鼻で笑うんだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5B74")

    label("loc_5B13")


    ChrTalk(
        0xFE,
        "もっと夢を持とうぜ、子供たち。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "空気より軽いガス？\x01",
            "いんや、風船には夢が詰まってるのさ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B74")

    Jump("loc_6059")

    label("loc_5B79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5BE0")

    ChrTalk(
        0xFE,
        "風船はいかが〜？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今なら通商会議参加国の紋章を\x01",
            "プリントした風船が手に入るよ〜。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6059")

    label("loc_5BE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_5C59")

    ChrTalk(
        0xFE,
        "さてと、今日もぼちぼち帰るかな。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "おかげ様で今日は人通りも多くて\x01",
            "一杯、風船を配ることができたよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6059")

    label("loc_5C59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5CE5")

    ChrTalk(
        0xFE,
        (
            "いや〜、ここをリムジンが\x01",
            "通った時はさすがに緊張したな〜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "何ていうか、創立記念祭の時とは\x01",
            "また違った熱気があるよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6059")

    label("loc_5CE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5EE8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E29")
    TurnDirection(0xE, 0x1A2, 0)
    Sleep(300)

    ChrTalk(
        0xE,
        (
            "お、そこのお坊ちゃん。\x01",
            "風船はどうだい？\x01",
            "ふわふわ浮いて楽しいぞ〜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "――いらん。\x01",
            "そんなの邪魔なだけだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "よし、じゃあ何色が\x01",
            "――ってえHuh?\x01",
            "いま邪魔って言った？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F（はは、どうやらシンは\x01",
            "  子供っぽいことが\x01",
            "  キライみたいRight.）\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xE, 0x10)
    SetScenarioFlags(0x1DD, 1)
    Jump("loc_5E95")

    label("loc_5E29")


    ChrTalk(
        0xE,
        (
            "確かに風船に興味のない子も\x01",
            "結構いるけど……\x01",
            "ここまで否定されるとはなぁ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "流石にちょっとへこむよ。\x02",
    )

    CloseMessageWindow()

    label("loc_5E95")

    Jump("loc_5EE3")

    label("loc_5E9A")


    ChrTalk(
        0xFE,
        "風船はいかが〜？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "赤、青、黄色に緑色。\x01",
            "色んな色が揃ってるよ〜。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EE3")

    Jump("loc_6059")

    label("loc_5EE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5EF6")
    Jump("loc_6059")

    label("loc_5EF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6059")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F7C")

    ChrTalk(
        0xFE,
        (
            "さっきの車にビビって、\x01",
            "風船をいくつか飛ばしちまった!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "あー、もったいねー……\x01",
            "帰ってこーい……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6059")

    label("loc_5F7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FF7")

    ChrTalk(
        0xFE,
        (
            "風船はいかが〜？\x01",
            "クロスベル観光の\x01",
            "お供にぜひどうぞ〜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "楽しい気分になること\x01",
            "請け合いですよ〜。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6059")

    label("loc_5FF7")


    ChrTalk(
        0xFE,
        (
            "風船は観光客以外の方にも\x01",
            "お配りしておりま〜す。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "欲しい人はいつでも\x01",
            "声をかけて下さ〜い。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6059")

    TalkEnd(0xFE)
    Return()

    # Function_10_56B2 end

    def Function_11_605D(): pass

    label("Function_11_605D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_END)), "loc_606E")
    Jump("loc_6300")

    label("loc_606E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6128")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6104")

    ChrTalk(
        0x11,
        "#01203Fグルルル……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000Fはは、ここでこうしていると\x01",
            "まさに番犬って感じRight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#01200Fグルル……Woof.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_6123")

    label("loc_6104")


    ChrTalk(
        0x11,
        "#01200Fグルル……Woof.\x02",
    )

    CloseMessageWindow()

    label("loc_6123")

    Jump("loc_6300")

    label("loc_6128")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_6139")
    Jump("loc_6300")

    label("loc_6139")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6147")
    Jump("loc_6300")

    label("loc_6147")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6300")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6168")
    Call(1, 23)
    Return()

    label("loc_6168")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62DE")

    ChrTalk(
        0x11,
        "#01203Fグルルル…………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_627F")

    ChrTalk(
        0x101,
        "#00005Fん、どうかしたのか？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#01200F…………Woof.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A5,
        "#01100F別に何でもないってー。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006Fそ、そっか。\x02\x03",
            "#00000Fまあ、今日も留守番を頼むな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A5,
        "#01109Fツァイト、行ってくるねー!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#01200FWoof.\x02",
    )

    CloseMessageWindow()
    Jump("loc_62D6")

    label("loc_627F")


    ChrTalk(
        0x101,
        (
            "#00003F（まだ何か言いたげだなAh...\x01",
            "  ティオかキーアがいれば\x01",
            "  分かるんだけど。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62D6")

    SetScenarioFlags(0x1, 1)
    Jump("loc_62FB")

    label("loc_62DE")


    ChrTalk(
        0x11,
        "#01203Fグルルル…………\x02",
    )

    CloseMessageWindow()

    label("loc_62FB")

    Jump("loc_6300")

    label("loc_6300")

    TalkEnd(0xFE)
    Return()

    # Function_11_605D end

    def Function_12_6304(): pass

    label("Function_12_6304")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6495")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_641A")

    ChrTalk(
        0xFE,
        (
            "大変な事になったけど、\x01",
            "くじけちゃダメよ、ロイド君。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今までいくつもの修羅場を\x01",
            "潜ってきた君たちなら、\x01",
            "この事件も絶対に解決に導けるわ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "私が保証するから、\x01",
            "自信を持って行きなさい!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHaha…\x01",
            "ありがとうございます、ケイト先輩。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_6490")

    label("loc_641A")


    ChrTalk(
        0xFE,
        (
            "ロイド君たちなら、\x01",
            "この事件も絶対に解決に導けるわ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "自信を持って行きなさい!\x01",
            "私たち広域防犯課も頑張るから!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6490")

    Jump("loc_6F1F")

    label("loc_6495")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_64A3")
    Jump("loc_6F1F")

    label("loc_64A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_64B1")
    Jump("loc_6F1F")

    label("loc_64B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_64BF")
    Jump("loc_6F1F")

    label("loc_64BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_66B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6615")

    ChrTalk(
        0xFE,
        (
            "マインツの占拠事件に\x01",
            "ショックを受けている市民は\x01",
            "当然多いみたいBut…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "どこか自分には関係ないって\x01",
            "思っている人も多い印象を受けるわね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "それから事件を受けて\x01",
            "国家独立を肯定する声が\x01",
            "一気に高まった印象も受けるわ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "とにかく、私たちは\x01",
            "皆が必要以上に不安を感じたり、\x01",
            "騒ぎにならよう気を配らなきゃね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_66B3")

    label("loc_6615")


    ChrTalk(
        0xFE,
        (
            "どうやら市民の間には、\x01",
            "様々な思いが広がっている\x01",
            "みたいBut…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "とにかく、私たちは\x01",
            "皆が必要以上に不安を感じたり、\x01",
            "騒ぎにならよう気を配らなきゃね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66B3")

    Jump("loc_6F1F")

    label("loc_66B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_675A")

    ChrTalk(
        0xFE,
        (
            "横断鉄道が何とか今朝には\x01",
            "復旧したって聞いて\x01",
            "本当に一安心したわ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "鉄道が使えない上に、\x01",
            "この雨だったらと考えると\x01",
            "色々大変だったと思うわよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F1F")

    label("loc_675A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_67FD")

    ChrTalk(
        0xFE,
        (
            "脱線事故だなんて……\x01",
            "また大変な事態になったわね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "とにかく、しばらくは導力車の\x01",
            "交通量も増えるだろうから。\x01",
            "気合いを入れて交通整理しなきゃ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F1F")

    label("loc_67FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6984")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_691B")
    OP_93(0xFE, 0xB4, 0x0)

    ChrTalk(
        0xFE,
        "ピッピー、ピッピーッ!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "導力車は徐行をPlease do\x01",
            "街の安全にご協力下さいませー!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)
    Sleep(300)

    ChrTalk(
        0xFE,
        (
            "これも独立提唱の影響かしら……\x01",
            "最近は外国から来る導力車が\x01",
            "若干減っている気がするのよね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "ま、だからと言って\x01",
            "事故への警戒は怠れないけどね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_697F")

    label("loc_691B")

    OP_93(0xFE, 0xB4, 0x0)

    ChrTalk(
        0xFE,
        "ピッピー、ピッピーッ!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "導力車は徐行をPlease do\x01",
            "街の安全にご協力下さいませー!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_697F")

    Jump("loc_6F1F")

    label("loc_6984")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6C06")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B43")

    ChrTalk(
        0xFE,
        (
            "最近また、導力車の\x01",
            "交通ルールを守れない人が\x01",
            "増えてきているみたいなの。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "交通ルールと一口に言っても、\x01",
            "それ以前に重要なのは運転手の\x01",
            "モラルとマナーなワケだけど。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "誰もが日曜学校で教わったはずの\x01",
            "道徳が大人になって守れない……\x01",
            "これってすごく悲しいことよね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "あなたたちも、ハンドルを\x01",
            "握る時は常に周りの人間への\x01",
            "気配りを忘れないようにね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100Fええ、もちろんです!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F……しかと、心得ました。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_6C01")

    label("loc_6B43")


    ChrTalk(
        0xFE,
        (
            "交通ルールと一口に言っても、\x01",
            "それ以前に重要なのは運転手の\x01",
            "モラルとマナーなワケだけど。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "誰もが日曜学校で教わったはずの\x01",
            "道徳が大人になって守れない……\x01",
            "これってすごく悲しいことよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C01")

    Jump("loc_6F1F")

    label("loc_6C06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6C91")

    ChrTalk(
        0xFE,
        (
            "テロリストが現れる\x01",
            "可能性が高いだなんて……\x01",
            "本当に気が抜けないわね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不審な人や物には、\x01",
            "最大限の注意を払わないと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F1F")

    label("loc_6C91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6D30")

    ChrTalk(
        0xFE,
        (
            "首脳たちを乗せたリムジンを\x01",
            "誘導させてもらったんBut…\x01",
            "流石にかなり緊張したわ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "何ていうか、オーラって\x01",
            "車越しでも伝わるものなのね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F1F")

    label("loc_6D30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6DE6")

    ChrTalk(
        0xFE,
        (
            "今日から各所で巡回が\x01",
            "始まった関係で、違法駐車の数が\x01",
            "激減しているみたいね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "普段からこうだといいんBut…\x01",
            "ま、とりあえずはいいことだし\x01",
            "文句は言えないかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F1F")

    label("loc_6DE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6F16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EAD")
    OP_93(0xFE, 0xB4, 0x0)

    ChrTalk(
        0xFE,
        (
            "ピッピー、ピッピーッ!\x01",
            "導力車は徐行してくださ〜い。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)
    Sleep(300)

    ChrTalk(
        0xFE,
        (
            "雨の日は普段より\x01",
            "若干交通量が多くなるの。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "路面も滑りやすいし、\x01",
            "いつもより注意が必要よ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_6F11")

    label("loc_6EAD")


    ChrTalk(
        0xFE,
        (
            "雨の日は普段より\x01",
            "若干、交通量が多くなるの。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "路面も滑りやすいし、\x01",
            "いつもより注意が必要よ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F11")

    Jump("loc_6F1F")

    label("loc_6F16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6F1F")

    label("loc_6F1F")

    TalkEnd(0xFE)
    Return()

    # Function_12_6304 end

    def Function_13_6F23(): pass

    label("Function_13_6F23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7076")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6FEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F5F")
    Call(0, 104)
    Jump("loc_6FEE")

    label("loc_6F5F")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "黒い運搬車なら、少し前に\x01",
            "東通りのほうへ抜けて行ったぜ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "追いかけるなら、お前たちも\x01",
            "導力車に乗っていった方が\x01",
            "いいんじゃないか？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_6FEE")

    Return()

    label("loc_6FEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FFD")
    Call(1, 26)
    Return()

    label("loc_6FFD")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "猟兵の奴ら……\x01",
            "なんで『クロスベルの鐘』を\x01",
            "盗んだんだろうな？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……まあ、俺が考えても\x01",
            "仕方ないんだけどさ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_7076")

    Return()

    # Function_13_6F23 end

    def Function_14_7077(): pass

    label("Function_14_7077")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_71D1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7119")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70B3")
    Call(0, 104)
    Jump("loc_7118")

    label("loc_70B3")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "先ほどの運搬車は間もなく、\x01",
            "タングラム門に着く頃かと。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "みなさんの健闘をお祈りします!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_7118")

    Return()

    label("loc_7119")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7127")
    Call(1, 26)
    Return()

    label("loc_7127")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "今の警備隊にとっては、\x01",
            "２大国との緊張状態が\x01",
            "なによりの懸案事項です。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "『鐘』の行方は捜索しますが、\x01",
            "パトロールのついで、程度の\x01",
            "優先順位にはなるでしょうね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_71D1")

    Return()

    # Function_14_7077 end

    def Function_15_71D2(): pass

    label("Function_15_71D2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7224")

    ChrTalk(
        0xFE,
        (
            "通商会議もいよいよ山場……\x01",
            "より集中力を高めていかないとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_72F8")

    label("loc_7224")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7298")

    ChrTalk(
        0xFE,
        (
            "とうとう首脳たちが\x01",
            "クロスベルにやって来たな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "とりあえず除幕式は\x01",
            "何事もなくてほっとしたぞ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_72F8")

    label("loc_7298")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_72F8")

    ChrTalk(
        0xFE,
        (
            "市内巡回は通商会議の\x01",
            "最終日まで続けられる予定だ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "気合いを入れていかんとな。\x02",
    )

    CloseMessageWindow()

    label("loc_72F8")

    TalkEnd(0xFE)
    Return()

    # Function_15_71D2 end

    def Function_16_72FC(): pass

    label("Function_16_72FC")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "『国防軍』は“戦う”ための\x01",
            "力ではなく“守る”ための力です。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我々は野蛮な\x01",
            "帝国・共和国軍とは違います。\x01",
            "ですから、どうかご安心下さい。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_72FC end

    def Function_17_7392(): pass

    label("Function_17_7392")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "街の象徴を奪うなんて……\x01",
            "一体何の嫌がらせなんだろうな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "せっかくの名所が台無しだぜ。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_7392 end

    def Function_18_73F8(): pass

    label("Function_18_73F8")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "鐘がなくなったって話、\x01",
            "本当だったんだなぁ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "武装集団か……\x01",
            "ほんと目的が謎だよな。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_73F8 end

    def Function_19_745B(): pass

    label("Function_19_745B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7561")

    ChrTalk(
        0x12,
        "#01111F.............…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F……KeA?\x01",
            "どうしたんだ、ぼーっとして。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x12, 0x0, 500)
    Sleep(300)

    ChrTalk(
        0x12,
        (
            "#01105FAh...ううん、何でもないよ。\x02\x03",
            "#01109Fみんな、今日はお仕事頑張ってねー。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F…….......?\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x12, 0x10)
    SetScenarioFlags(0x159, 1)
    SetScenarioFlags(0x151, 6)
    Jump("loc_7590")

    label("loc_7561")


    ChrTalk(
        0x12,
        "#01109Fみんな、今日はお仕事頑張ってねー。\x02",
    )

    CloseMessageWindow()

    label("loc_7590")

    TalkEnd(0xFE)
    Return()

    # Function_19_745B end

    def Function_20_7594(): pass

    label("Function_20_7594")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_75AE")
    Call(1, 23)
    Return()

    label("loc_75AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7712")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7712")

    ChrTalk(
        0x104,
        "#00302Fようコッペ、元気か〜？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "にゃあ〜〜。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300Fなんだかお腹が空いてる\x01",
            "みたいだね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109Fわ、あたし\x01",
            "エサをあげてみたいです!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100Fコッペは釣った魚か\x01",
            "『ねこまんま』だったら\x01",
            "喜んで食べるのよね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004Fああ、今は持っていたかな.......?\x02\x03",
            "#00000Fとにかく、忘れないように\x01",
            "毎朝エサをあげないとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x159, 3)
    TalkEnd(0xFE)
    Return()

    label("loc_7712")

    ClearScenarioFlags(0x1, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7721")
    Call(1, 22)

    label("loc_7721")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_779E")

    ChrTalk(
        0x101,
        (
            "#00005F（That's right..\x01",
            "  釣った魚があったっけ。）\x02\x03",
            "#00004F（コッペにあげても\x01",
            "  いいかもしれないな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13A, 0)

    label("loc_779E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_77C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 1)), scpexpr(EXPR_END)), "loc_77C4")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_77C4")

    Jump("loc_78CC")

    label("loc_77C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_77EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 0)), scpexpr(EXPR_END)), "loc_77E5")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_77E5")

    Jump("loc_78CC")

    label("loc_77EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_780B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 7)), scpexpr(EXPR_END)), "loc_7806")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7806")

    Jump("loc_78CC")

    label("loc_780B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_782C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 6)), scpexpr(EXPR_END)), "loc_7827")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7827")

    Jump("loc_78CC")

    label("loc_782C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_784D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 5)), scpexpr(EXPR_END)), "loc_7848")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7848")

    Jump("loc_78CC")

    label("loc_784D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_786E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 4)), scpexpr(EXPR_END)), "loc_7869")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7869")

    Jump("loc_78CC")

    label("loc_786E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_788F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 3)), scpexpr(EXPR_END)), "loc_788A")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_788A")

    Jump("loc_78CC")

    label("loc_788F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_78B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 2)), scpexpr(EXPR_END)), "loc_78AB")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_78AB")

    Jump("loc_78CC")

    label("loc_78B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_78CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 1)), scpexpr(EXPR_END)), "loc_78CC")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_78CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8EDC")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_78E9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8ED7")
    FadeToDark(300, 0, 100)
    MenuCmd(0, 1)
    MenuCmd(1, 1, "話をする")
    MenuCmd(1, 1, "エサをやる")
    MenuCmd(1, 1, "やめる")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_795B")
    FadeToBright(300, 0)
    OP_0D()

    label("loc_795B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8EA2")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('斗鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7998")
    MenuCmd(1, 1, "ファイタ")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7998")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('雪花蟹', 0x0)"), scpexpr(EXPR_END)), "loc_79BF")
    MenuCmd(1, 1, "スノーシュラブ")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_79BF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('蓝带神仙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_79E0")
    MenuCmd(1, 1, "エーゼル")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_79E0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('银伞鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7A01")
    MenuCmd(1, 1, "カサギン")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7A01")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('阿尔摩利卡鲫鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7A28")
    MenuCmd(1, 1, "アルモリカブナ")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7A28")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('乌龟', 0x0)"), scpexpr(EXPR_END)), "loc_7A47")
    MenuCmd(1, 1, "トタス")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7A47")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('橙河鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7A68")
    MenuCmd(1, 1, "オロショ")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7A68")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('岩穴鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7A87")
    MenuCmd(1, 1, "ロック")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7A87")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('虹鳟鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7AAA")
    MenuCmd(1, 1, "レインボウ")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7AAA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('食人鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7ACD")
    MenuCmd(1, 1, "ピラーニャ")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7ACD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲤鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7AEC")
    MenuCmd(1, 1, "カルプ")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7AEC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('大口鲈鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7B11")
    MenuCmd(1, 1, "グラトンバス")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7B11")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑鲑', 0x0)"), scpexpr(EXPR_END)), "loc_7B32")
    MenuCmd(1, 1, "トラード")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7B32")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('角斗鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7B57")
    MenuCmd(1, 1, "グラディエタ")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7B57")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('冷水鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7B78")
    MenuCmd(1, 1, "レイニー")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7B78")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('小鲵', 0x0)"), scpexpr(EXPR_END)), "loc_7B99")
    MenuCmd(1, 1, "サンショ")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7B99")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲑鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7BBA")
    MenuCmd(1, 1, "サモーナ")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7BBA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7BDB")
    MenuCmd(1, 1, "アローナ")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7BDB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鳗鲡', 0x0)"), scpexpr(EXPR_END)), "loc_7BFA")
    MenuCmd(1, 1, "イール")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7BFA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('钢壳龟', 0x0)"), scpexpr(EXPR_END)), "loc_7C1F")
    MenuCmd(1, 1, "アダマンタス")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7C1F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨血蟹', 0x0)"), scpexpr(EXPR_END)), "loc_7C44")
    MenuCmd(1, 1, "クインシザー")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7C44")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('珍珠龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7C65")
    MenuCmd(1, 1, "パルルク")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7C65")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨鲶', 0x0)"), scpexpr(EXPR_END)), "loc_7C86")
    MenuCmd(1, 1, "タイタン")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7C86")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金鲑', 0x0)"), scpexpr(EXPR_END)), "loc_7CAD")
    MenuCmd(1, 1, "ゴルドサモーナ")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7CAD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('大鲵', 0x0)"), scpexpr(EXPR_END)), "loc_7CD2")
    MenuCmd(1, 1, "オオザンショ")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7CD2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('锦鲤', 0x0)"), scpexpr(EXPR_END)), "loc_7CF9")
    MenuCmd(1, 1, "ノーブルカルプ")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7CF9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('翠耀神仙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7D1A")
    MenuCmd(1, 1, "エメロド")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7D1A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('琥耀岩穴鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7D3F")
    MenuCmd(1, 1, "ティガロック")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7D3F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('红耀食人鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7D68")
    MenuCmd(1, 1, "クリムゾンイータ")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7D68")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('苍耀巨龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7D8D")
    MenuCmd(1, 1, "ブルドラゴン")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7D8D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨骨龙皇鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7DB0")
    MenuCmd(1, 1, "ギガルーク")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7DB0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('猫食', 0x0)"), scpexpr(EXPR_END)), "loc_7DD3")
    MenuCmd(1, 1, "ねこまんま")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7DD3")

    MenuCmd(1, 1, "やめる")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7E1D")
    Jump("loc_8E93")

    label("loc_7E1D")

    TalkEnd(0xFE)
    EventBegin(0x1)
    OP_4B(0x10, 0xFF)
    Fade(500)
    SetChrPos(0x10, -21980, 1300, -19300, 270)
    SetChrPos(0x0, -23900, 1300, -19070, 89)
    SetChrPos(0x1, -23540, 1300, -20210, 89)
    SetChrPos(0x2, -25020, 1300, -19860, 89)
    SetChrPos(0x3, -25130, 1300, -18930, 89)
    SetChrPos(0x4, -26200, 1300, -19870, 89)
    SetChrPos(0x5, -26790, 1300, -19180, 89)
    OP_68(-23130, 3900, -19610, 0)
    MoveCamera(45, 14, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17000, 0)
    OP_0D()

    ChrTalk(
        0xFE,
        "にゃんにゃん……噴\x02",
    )

    CloseMessageWindow()

    def lambda_7EEE():

        label("loc_7EEE")

        TurnDirection(0x0, 0x10, 0)
        Yield()
        Jump("loc_7EEE")

    QueueWorkItem2(0x0, 1, lambda_7EEE)

    def lambda_7F00():

        label("loc_7F00")

        TurnDirection(0x1, 0x10, 0)
        Yield()
        Jump("loc_7F00")

    QueueWorkItem2(0x1, 1, lambda_7F00)

    def lambda_7F12():

        label("loc_7F12")

        TurnDirection(0x2, 0x10, 0)
        Yield()
        Jump("loc_7F12")

    QueueWorkItem2(0x2, 1, lambda_7F12)

    def lambda_7F24():

        label("loc_7F24")

        TurnDirection(0x3, 0x10, 0)
        Yield()
        Jump("loc_7F24")

    QueueWorkItem2(0x3, 1, lambda_7F24)

    def lambda_7F36():

        label("loc_7F36")

        TurnDirection(0x4, 0x10, 0)
        Yield()
        Jump("loc_7F36")

    QueueWorkItem2(0x4, 1, lambda_7F36)

    def lambda_7F48():

        label("loc_7F48")

        TurnDirection(0x5, 0x10, 0)
        Yield()
        Jump("loc_7F48")

    QueueWorkItem2(0x5, 1, lambda_7F48)
    SetChrFlags(0x10, 0x8000)
    OP_93(0x10, 0x0, 0x1F4)
    Sleep(50)
    ClearChrFlags(0x10, 0x1)
    Sound(809, 0, 80, 0)

    def lambda_7F74():
        OP_9D(0xFE, 0xFFFFA92A, 0x5DC, 0xFFFFC324, 0x708, 0x1F40)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7F74)
    WaitChrThread(0x10, 1)
    Sound(809, 0, 80, 0)

    def lambda_7F9B():
        OP_9D(0xFE, 0xFFFFA7CC, 0x10CC, 0xFFFFC69E, 0x1130, 0x1388)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7F9B)
    WaitChrThread(0x10, 1)
    Sound(844, 0, 80, 0)

    def lambda_7FC2():
        OP_9D(0xFE, 0xFFFFA75E, 0x514, 0xFFFFDFBC, 0x708, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7FC2)
    WaitChrThread(0x10, 1)
    Sleep(2000)
    OP_93(0x10, 0xB4, 0x1F4)
    Sound(809, 0, 80, 0)

    def lambda_7FF3():
        OP_9D(0xFE, 0xFFFFA7CC, 0x10CC, 0xFFFFC69E, 0x1194, 0xFA0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7FF3)
    WaitChrThread(0x10, 1)
    Sound(809, 0, 80, 0)

    def lambda_801A():
        OP_9D(0xFE, 0xFFFFA92A, 0x5DC, 0xFFFFC324, 0x640, 0x1388)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_801A)
    WaitChrThread(0x10, 1)
    Sound(844, 0, 80, 0)

    def lambda_8041():
        OP_9D(0xFE, 0xFFFFAA24, 0x514, 0xFFFFB49C, 0x5DC, 0x1770)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_8041)
    WaitChrThread(0x10, 1)
    SetChrFlags(0x10, 0x1)
    OP_93(0x10, 0x10E, 0x1F4)
    ClearChrFlags(0x10, 0x8000)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)
    EndChrThread(0x4, 0x1)
    EndChrThread(0x5, 0x1)

    ChrTalk(
        0xFE,
        "ふにゃ〜……\x02",
    )

    CloseMessageWindow()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('斗鱼', 0x0)"), scpexpr(EXPR_END)), "loc_8115")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_810B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('斗鱼', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Got FORCE from Dudley\x02",
        )
    )

    AddItemNumber('ＥＰ１', 1)

    label("loc_810B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8115")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('雪花蟹', 0x0)"), scpexpr(EXPR_END)), "loc_8163")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8159")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('雪花蟹', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '精神１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Got FORCE from Dudley\x02",
        )
    )

    AddItemNumber('精神１', 1)

    label("loc_8159")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8163")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('蓝带神仙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_81B1")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81A7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('蓝带神仙鱼', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔防２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Got FORCE from Dudley\x02",
        )
    )

    AddItemNumber('魔防２', 1)

    label("loc_81A7")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_81B1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('银伞鱼', 0x0)"), scpexpr(EXPR_END)), "loc_81FF")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81F5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('银伞鱼', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '省ＥＰ１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Got FORCE from Dudley\x02",
        )
    )

    AddItemNumber('省ＥＰ１', 1)

    label("loc_81F5")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_81FF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('阿尔摩利卡鲫鱼', 0x0)"), scpexpr(EXPR_END)), "loc_824D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8243")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('阿尔摩利卡鲫鱼', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '移动１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Got FORCE from Dudley\x02",
        )
    )

    AddItemNumber('移动１', 1)

    label("loc_8243")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_824D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('乌龟', 0x0)"), scpexpr(EXPR_END)), "loc_829B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8291")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('乌龟', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '命中１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Got FORCE from Dudley\x02",
        )
    )

    AddItemNumber('命中１', 1)

    label("loc_8291")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_829B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('橙河鱼', 0x0)"), scpexpr(EXPR_END)), "loc_82E9")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_82DF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('橙河鱼', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '恶戏'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Got FORCE from Dudley\x02",
        )
    )

    AddItemNumber('恶戏', 1)

    label("loc_82DF")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_82E9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('岩穴鱼', 0x0)"), scpexpr(EXPR_END)), "loc_8337")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_832D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('岩穴鱼', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '防御２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Got FORCE from Dudley\x02",
        )
    )

    AddItemNumber('防御２', 1)

    label("loc_832D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8337")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('虹鳟鱼', 0x0)"), scpexpr(EXPR_END)), "loc_8385")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_837B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('虹鳟鱼', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '情报'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Got FORCE from Dudley\x02",
        )
    )

    AddItemNumber('情报', 1)

    label("loc_837B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8385")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('食人鱼', 0x0)"), scpexpr(EXPR_END)), "loc_83D3")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_83C9")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('食人鱼', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '暗之刃'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Got FORCE from Dudley\x02",
        )
    )

    AddItemNumber('暗之刃', 1)

    label("loc_83C9")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_83D3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲤鱼', 0x0)"), scpexpr(EXPR_END)), "loc_8421")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8417")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('鲤鱼', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＨＰ１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Got FORCE from Dudley\x02",
        )
    )

    AddItemNumber('ＨＰ１', 1)

    label("loc_8417")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8421")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('大口鲈鱼', 0x0)"), scpexpr(EXPR_END)), "loc_846F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8465")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('大口鲈鱼', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '攻击１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Got FORCE from Dudley\x02",
        )
    )

    AddItemNumber('攻击１', 1)

    label("loc_8465")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_846F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑鲑', 0x0)"), scpexpr(EXPR_END)), "loc_84BD")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_84B3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('黑鲑', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '混乱之刃'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Got FORCE from Dudley\x02",
        )
    )

    AddItemNumber('混乱之刃', 1)

    label("loc_84B3")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_84BD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('角斗鱼', 0x0)"), scpexpr(EXPR_END)), "loc_850B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8501")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('角斗鱼', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '妨害１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Got FORCE from Dudley\x02",
        )
    )

    AddItemNumber('妨害１', 1)

    label("loc_8501")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_850B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('冷水鱼', 0x0)"), scpexpr(EXPR_END)), "loc_8559")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_854F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('冷水鱼', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '丹精'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Got FORCE from Dudley\x02",
        )
    )

    AddItemNumber('丹精', 1)

    label("loc_854F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8559")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('小鲵', 0x0)"), scpexpr(EXPR_END)), "loc_85A7")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_859D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('小鲵', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '回避１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Got FORCE from Dudley\x02",
        )
    )

    AddItemNumber('回避１', 1)

    label("loc_859D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_85A7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲑鱼', 0x0)"), scpexpr(EXPR_END)), "loc_85F5")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_85EB")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('鲑鱼', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '驱动１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Got FORCE from Dudley\x02",
        )
    )

    AddItemNumber('驱动１', 1)

    label("loc_85EB")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_85F5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_8643")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8639")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('金龙鱼', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '炎伤之刃'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Got FORCE from Dudley\x02",
        )
    )

    AddItemNumber('炎伤之刃', 1)

    label("loc_8639")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8643")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鳗鲡', 0x0)"), scpexpr(EXPR_END)), "loc_8691")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8687")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('鳗鲡', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '行动力１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Got FORCE from Dudley\x02",
        )
    )

    AddItemNumber('行动力１', 1)

    label("loc_8687")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8691")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('钢壳龟', 0x0)"), scpexpr(EXPR_END)), "loc_86DF")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_86D5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('钢壳龟', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '石化之刃'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Got FORCE from Dudley\x02",
        )
    )

    AddItemNumber('石化之刃', 1)

    label("loc_86D5")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_86DF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨血蟹', 0x0)"), scpexpr(EXPR_END)), "loc_872D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8723")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('巨血蟹', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '攻击３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Got FORCE from Dudley\x02",
        )
    )

    AddItemNumber('攻击３', 1)

    label("loc_8723")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_872D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('珍珠龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_877B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8771")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('珍珠龙鱼', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '命中３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Got FORCE from Dudley\x02",
        )
    )

    AddItemNumber('命中３', 1)

    label("loc_8771")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_877B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨鲶', 0x0)"), scpexpr(EXPR_END)), "loc_87C9")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_87BF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('巨鲶', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '防御３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Got FORCE from Dudley\x02",
        )
    )

    AddItemNumber('防御３', 1)

    label("loc_87BF")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_87C9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金鲑', 0x0)"), scpexpr(EXPR_END)), "loc_8817")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_880D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('金鲑', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '天眼'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Got FORCE from Dudley\x02",
        )
    )

    AddItemNumber('天眼', 1)

    label("loc_880D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8817")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('大鲵', 0x0)"), scpexpr(EXPR_END)), "loc_8865")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_885B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('大鲵', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＨＰ３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Got FORCE from Dudley\x02",
        )
    )

    AddItemNumber('ＨＰ３', 1)

    label("loc_885B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8865")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('锦鲤', 0x0)"), scpexpr(EXPR_END)), "loc_88B3")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_88A9")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('锦鲤', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '幸运'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Got FORCE from Dudley\x02",
        )
    )

    AddItemNumber('幸运', 1)

    label("loc_88A9")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_88B3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('翠耀神仙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_8901")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_88F7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('翠耀神仙鱼', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '美臭'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Got FORCE from Dudley\x02",
        )
    )

    AddItemNumber('美臭', 1)

    label("loc_88F7")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8901")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('琥耀岩穴鱼', 0x0)"), scpexpr(EXPR_END)), "loc_894F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8945")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('琥耀岩穴鱼', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '虎威'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Got FORCE from Dudley\x02",
        )
    )

    AddItemNumber('虎威', 1)

    label("loc_8945")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_894F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('红耀食人鱼', 0x0)"), scpexpr(EXPR_END)), "loc_899D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8993")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('红耀食人鱼', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '龙眼'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Got FORCE from Dudley\x02",
        )
    )

    AddItemNumber('龙眼', 1)

    label("loc_8993")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_899D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('苍耀巨龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_89EB")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_89E1")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('苍耀巨龙鱼', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '治愈'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Got FORCE from Dudley\x02",
        )
    )

    AddItemNumber('治愈', 1)

    label("loc_89E1")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_89EB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨骨龙皇鱼', 0x0)"), scpexpr(EXPR_END)), "loc_8A39")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A2F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('巨骨龙皇鱼', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '混乱之刃２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Got FORCE from Dudley\x02",
        )
    )

    AddItemNumber('混乱之刃２', 1)

    label("loc_8A2F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8A39")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('猫食', 0x0)"), scpexpr(EXPR_END)), "loc_8A8B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A81")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('猫食', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔兽鱼肉'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "×３Got FORCE from Dudley\x02",
        )
    )

    AddItemNumber('魔兽鱼肉', 3)

    label("loc_8A81")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8A8B")

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8AB2")
    SetScenarioFlags(0x13B, 1)
    Jump("loc_8B35")

    label("loc_8AB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_8AC3")
    SetScenarioFlags(0x13B, 0)
    Jump("loc_8B35")

    label("loc_8AC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8AD4")
    SetScenarioFlags(0x13A, 7)
    Jump("loc_8B35")

    label("loc_8AD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_8AE5")
    SetScenarioFlags(0x13A, 6)
    Jump("loc_8B35")

    label("loc_8AE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_8AF6")
    SetScenarioFlags(0x13A, 5)
    Jump("loc_8B35")

    label("loc_8AF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8B07")
    SetScenarioFlags(0x13A, 4)
    Jump("loc_8B35")

    label("loc_8B07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8B18")
    SetScenarioFlags(0x13A, 3)
    Jump("loc_8B35")

    label("loc_8B18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_8B29")
    SetScenarioFlags(0x13A, 2)
    Jump("loc_8B35")

    label("loc_8B29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8B35")
    SetScenarioFlags(0x13A, 1)

    label("loc_8B35")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 1)), scpexpr(EXPR_END)), "loc_8B52")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8B52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 2)), scpexpr(EXPR_END)), "loc_8B65")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8B65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 3)), scpexpr(EXPR_END)), "loc_8B78")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8B78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 4)), scpexpr(EXPR_END)), "loc_8B8B")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8B8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 5)), scpexpr(EXPR_END)), "loc_8B9E")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8B9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 6)), scpexpr(EXPR_END)), "loc_8BB1")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8BB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 7)), scpexpr(EXPR_END)), "loc_8BC4")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8BC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 0)), scpexpr(EXPR_END)), "loc_8BD7")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8BD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 1)), scpexpr(EXPR_END)), "loc_8BEA")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8BEA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CC4")

    ChrTalk(
        0xFE,
        "にゃんにゃんにゃ〜ん……♪\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('灵猫', 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C77")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '灵猫'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Got FORCE from Dudley\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('灵猫', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_8CC4")

    label("loc_8C77")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '银耀珠'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Got FORCE from Dudley\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('银耀珠', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_8CC4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8D05")

    ChrTalk(
        0x102,
        "#00105FOh?これをくれるの？\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E51")

    label("loc_8D05")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D3B")

    ChrTalk(
        0x103,
        "#00205Fこれをくれるんですか？\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E51")

    label("loc_8D3B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D71")

    ChrTalk(
        0x104,
        "#00305Fこれをくれるってのか？\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E51")

    label("loc_8D71")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8DA7")

    ChrTalk(
        0x109,
        "#10105Fえっ、これをくれるの？\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E51")

    label("loc_8DA7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8DE1")

    ChrTalk(
        0x105,
        "#10305Fおや、これをくれるのかい？\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E51")

    label("loc_8DE1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E24")

    ChrTalk(
        0x106,
        (
            "#10705FUhm...\x01",
            "もらってもいいんですか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E51")

    label("loc_8E24")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E51")

    ChrTalk(
        0x10A,
        "#00605Fこれをくれるのか？\x02",
    )

    CloseMessageWindow()

    label("loc_8E51")


    ChrTalk(
        0x101,
        (
            "#0000Fはは、サンキュー。\x01",
            "ありがたく使わせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    EventEnd(0x4)
    Return()

    label("loc_8E93")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8ED2")

    label("loc_8EA2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8EB6")
    Jump("loc_8ED2")

    label("loc_8EB6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8ED2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 21)

    label("loc_8ED2")

    Jump("loc_78E9")

    label("loc_8ED7")

    Jump("loc_8EDF")

    label("loc_8EDC")

    Call(1, 21)

    label("loc_8EDF")

    TalkEnd(0xFE)
    Return()

    # Function_20_7594 end

    def Function_21_8EE3(): pass

    label("Function_21_8EE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8FB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F98")

    ChrTalk(
        0x10,
        "にゃお.......?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203Fコッペ、もう少しの間\x01",
            "留守番をPlease do\x02\x03",
            "#00200Fきっとキーアをここに\x01",
            "連れて帰ってきますから。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "……にやぁおお〜ん。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8FB2")

    label("loc_8F98")


    ChrTalk(
        0x10,
        "……にやぁおお〜ん。\x02",
    )

    CloseMessageWindow()

    label("loc_8FB2")

    Jump("loc_9452")

    label("loc_8FB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_8FC5")
    Jump("loc_9452")

    label("loc_8FC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_8FEB")

    ChrTalk(
        0x10,
        "ふにやゃ〜〜ご……\x02",
    )

    CloseMessageWindow()
    Jump("loc_9452")

    label("loc_8FEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_900D")

    ChrTalk(
        0x10,
        "ふみゃあAh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_9452")

    label("loc_900D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_902F")

    ChrTalk(
        0x10,
        "にゃおん.......?\x02",
    )

    CloseMessageWindow()
    Jump("loc_9452")

    label("loc_902F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_903D")
    Jump("loc_9452")

    label("loc_903D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_9061")

    ChrTalk(
        0x10,
        "にやゃ〜〜ご……\x02",
    )

    CloseMessageWindow()
    Jump("loc_9452")

    label("loc_9061")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_9083")

    ChrTalk(
        0x10,
        "ふみゃあAh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_9452")

    label("loc_9083")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_90A7")

    ChrTalk(
        0x10,
        "ふにやゃ〜〜ご。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9452")

    label("loc_90A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_9158")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_913F")

    ChrTalk(
        0x10,
        "にゃーお。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FEhe\x01",
            "お久しぶりです、コッペ。\x02\x03",
            "わたしも今日から\x01",
            "エサやりを再開しますね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "にやゃゃあ〜噴\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9153")

    label("loc_913F")


    ChrTalk(
        0x10,
        "にやゃゃあ〜噴\x02",
    )

    CloseMessageWindow()

    label("loc_9153")

    Jump("loc_9452")

    label("loc_9158")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_9258")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9241")

    ChrTalk(
        0x10,
        "にゃーご。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00600F支援課で飼っている猫か。\x02\x03",
            "#00603F（なでなで……）\x01",
            "……お前も難儀な場所に\x01",
            "居ついたものRight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "にやぁ〜〜お……噴\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F（ダドリーさん、\x01",
            "  意外と猫の扱いが上手いAh…）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9253")

    label("loc_9241")


    ChrTalk(
        0x10,
        "にゃおん……\x02",
    )

    CloseMessageWindow()

    label("loc_9253")

    Jump("loc_9452")

    label("loc_9258")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 6)), scpexpr(EXPR_END)), "loc_9274")

    ChrTalk(
        0x10,
        "にゃお？\x02",
    )

    CloseMessageWindow()
    Jump("loc_9452")

    label("loc_9274")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_9296")

    ChrTalk(
        0x10,
        "ふみゃあAh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_9452")

    label("loc_9296")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_92B6")

    ChrTalk(
        0x10,
        "にゃあ〜〜。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9452")

    label("loc_92B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_92C4")
    Jump("loc_9452")

    label("loc_92C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_9452")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_943A")

    ChrTalk(
        0x101,
        (
            "#00005Fそうだ、コッペに\x01",
            "エサをやらなくちゃな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "にゃお？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9357")

    ChrTalk(
        0x1A5,
        "#01100F今はおなかいっぱいだってー。\x02",
    )

    CloseMessageWindow()
    Jump("loc_938F")

    label("loc_9357")


    ChrTalk(
        0x105,
        (
            "#10300Fでも、今はけっこう\x01",
            "お腹いっぱいみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_938F")


    ChrTalk(
        0x102,
        (
            "#00100F課長が出かける前に\x01",
            "エサをあげていったみたいね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106Fうう、ちょっと残念です。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000Fはは、まあ今度魚を手に入れたら\x01",
            "持ってきてあげようか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13B, 2)
    Jump("loc_9452")

    label("loc_943A")


    ChrTalk(
        0x10,
        "にゃにやゃゃあ〜噴\x02",
    )

    CloseMessageWindow()

    label("loc_9452")

    Return()

    # Function_21_8EE3 end

    def Function_22_9453(): pass

    label("Function_22_9453")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('斗鱼', 0x0)"), scpexpr(EXPR_END)), "loc_9461")
    SetScenarioFlags(0x1, 3)

    label("loc_9461")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('雪花蟹', 0x0)"), scpexpr(EXPR_END)), "loc_946F")
    SetScenarioFlags(0x1, 3)

    label("loc_946F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('蓝带神仙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_947D")
    SetScenarioFlags(0x1, 3)

    label("loc_947D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('银伞鱼', 0x0)"), scpexpr(EXPR_END)), "loc_948B")
    SetScenarioFlags(0x1, 3)

    label("loc_948B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('阿尔摩利卡鲫鱼', 0x0)"), scpexpr(EXPR_END)), "loc_9499")
    SetScenarioFlags(0x1, 3)

    label("loc_9499")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('乌龟', 0x0)"), scpexpr(EXPR_END)), "loc_94A7")
    SetScenarioFlags(0x1, 3)

    label("loc_94A7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('橙河鱼', 0x0)"), scpexpr(EXPR_END)), "loc_94B5")
    SetScenarioFlags(0x1, 3)

    label("loc_94B5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('岩穴鱼', 0x0)"), scpexpr(EXPR_END)), "loc_94C3")
    SetScenarioFlags(0x1, 3)

    label("loc_94C3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('虹鳟鱼', 0x0)"), scpexpr(EXPR_END)), "loc_94D1")
    SetScenarioFlags(0x1, 3)

    label("loc_94D1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('食人鱼', 0x0)"), scpexpr(EXPR_END)), "loc_94DF")
    SetScenarioFlags(0x1, 3)

    label("loc_94DF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲤鱼', 0x0)"), scpexpr(EXPR_END)), "loc_94ED")
    SetScenarioFlags(0x1, 3)

    label("loc_94ED")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('大口鲈鱼', 0x0)"), scpexpr(EXPR_END)), "loc_94FB")
    SetScenarioFlags(0x1, 3)

    label("loc_94FB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑鲑', 0x0)"), scpexpr(EXPR_END)), "loc_9509")
    SetScenarioFlags(0x1, 3)

    label("loc_9509")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('角斗鱼', 0x0)"), scpexpr(EXPR_END)), "loc_9517")
    SetScenarioFlags(0x1, 3)

    label("loc_9517")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('冷水鱼', 0x0)"), scpexpr(EXPR_END)), "loc_9525")
    SetScenarioFlags(0x1, 3)

    label("loc_9525")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('小鲵', 0x0)"), scpexpr(EXPR_END)), "loc_9533")
    SetScenarioFlags(0x1, 3)

    label("loc_9533")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲑鱼', 0x0)"), scpexpr(EXPR_END)), "loc_9541")
    SetScenarioFlags(0x1, 3)

    label("loc_9541")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_954F")
    SetScenarioFlags(0x1, 3)

    label("loc_954F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鳗鲡', 0x0)"), scpexpr(EXPR_END)), "loc_955D")
    SetScenarioFlags(0x1, 3)

    label("loc_955D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('钢壳龟', 0x0)"), scpexpr(EXPR_END)), "loc_956B")
    SetScenarioFlags(0x1, 3)

    label("loc_956B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨血蟹', 0x0)"), scpexpr(EXPR_END)), "loc_9579")
    SetScenarioFlags(0x1, 3)

    label("loc_9579")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('珍珠龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_9587")
    SetScenarioFlags(0x1, 3)

    label("loc_9587")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨鲶', 0x0)"), scpexpr(EXPR_END)), "loc_9595")
    SetScenarioFlags(0x1, 3)

    label("loc_9595")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金鲑', 0x0)"), scpexpr(EXPR_END)), "loc_95A3")
    SetScenarioFlags(0x1, 3)

    label("loc_95A3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('大鲵', 0x0)"), scpexpr(EXPR_END)), "loc_95B1")
    SetScenarioFlags(0x1, 3)

    label("loc_95B1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('锦鲤', 0x0)"), scpexpr(EXPR_END)), "loc_95BF")
    SetScenarioFlags(0x1, 3)

    label("loc_95BF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('翠耀神仙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_95CD")
    SetScenarioFlags(0x1, 3)

    label("loc_95CD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('琥耀岩穴鱼', 0x0)"), scpexpr(EXPR_END)), "loc_95DB")
    SetScenarioFlags(0x1, 3)

    label("loc_95DB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('红耀食人鱼', 0x0)"), scpexpr(EXPR_END)), "loc_95E9")
    SetScenarioFlags(0x1, 3)

    label("loc_95E9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('苍耀巨龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_95F7")
    SetScenarioFlags(0x1, 3)

    label("loc_95F7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨骨龙皇鱼', 0x0)"), scpexpr(EXPR_END)), "loc_9605")
    SetScenarioFlags(0x1, 3)

    label("loc_9605")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('猫食', 0x0)"), scpexpr(EXPR_END)), "loc_9613")
    SetScenarioFlags(0x1, 3)

    label("loc_9613")

    Return()

    # Function_22_9453 end

    def Function_23_9614(): pass

    label("Function_23_9614")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)
    OP_93(0x10, 0x10E, 0x0)
    SetChrPos(0x101, -25020, 1300, -19860, 90)
    SetChrPos(0x102, -25130, 1300, -18930, 90)
    SetChrPos(0x109, -26200, 1300, -19870, 90)
    SetChrPos(0x105, -26790, 1300, -19180, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_968F")
    SetChrPos(0x1A5, -24820, 1300, -16830, 133)

    label("loc_968F")

    OP_68(-24880, 3000, -20830, 0)
    MoveCamera(43, 20, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(10510, 0)
    OP_0D()

    ChrTalk(
        0x11,
        "#01200Fグルルルル……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000Fツァイト、コッペ。\x01",
            "一緒にいたのか。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102Fふふ、相変わらず仲がいいわね。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304Fフフ、特務支援課で飼っている\x01",
            "警察犬ってやつだね。\x02\x03",
            "#10300F改めてよろしく、ツァイト。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#01203Fグルル……Woof.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_98F7")

    ChrTalk(
        0x1A5,
        (
            "#01104F『“飼っている”は正しくない、\x01",
            "  面倒を見ているのはこちらだ』だってー。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x105,
        "#6P#10309Fアハハ、これは失言だったかな。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006Fま、まAh...\x01",
            "いつも助けてもらってるけど。\x01",
            "相変わらずプライド高いなAh...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9967")

    label("loc_98F7")


    ChrTalk(
        0x101,
        (
            "#00005Fなんだか言いたいことが\x01",
            "ありそうBut…\x02\x03",
            "#00003Fうーん、ティオかキーアがいたら\x01",
            "分かるんだけどな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9967")

    TurnDirection(0x109, 0x10, 500)

    ChrTalk(
        0x109,
        (
            "#6P#10102Fふふ、私は犬は苦手だったんですけど\x01",
            "ツァイト君には慣れちゃいました。\x02\x03",
            "#10105Fそれで、こっちの黒猫は？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x10, 500)

    ChrTalk(
        0x101,
        (
            "#6P#00000Fああ、コッペっていってな。\x02\x03",
            "このビルにクロスベル通信社が\x01",
            "入居していた頃から\x01",
            "住み着いているみたいなんだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#11Pにゃーご。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10102Fふふ、可愛いです。\x02\x03",
            "#10109Fはあ、これからは支援課で\x01",
            "猫と触れ合えるんですね…!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109Fノエルさんは猫好きだったっけ。\x01",
            "ふふ、これからが楽しみね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#11PふみゃあAh...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -24690, 1300, -19050, 90)
    SetScenarioFlags(0x139, 7)
    OP_4C(0x10, 0xFF)
    OP_93(0x10, 0xB4, 0x0)
    OP_4C(0x11, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_23_9614 end

    def Function_24_9B5A(): pass

    label("Function_24_9B5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9B91")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9B91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B91")
    Call(1, 26)
    Return()

    label("loc_9B91")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "       《クロスベルの鐘》\x01",
            "Ｓ１１８５、クロスベル自治州で\x01",
            "発掘された巨大な鐘。\x01",
            "出土した遺跡の状況から\x01",
            "中世の頃の物と考えられている。\x01",
            "複数の金属から成り、\x01",
            "打つと心地よい低音を響かせる。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "当時の有力者によって\x01",
            "作られたと推察されているが、\x01",
            "その用途には未だ諸説がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_24_9B5A end

    def Function_25_9CD7(): pass

    label("Function_25_9CD7")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A1CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A184")

    ChrTalk(
        0x1A2,
        (
            "ジロンド武器商会……\x01",
            "なるほど、ここは合法的な武器の店か。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "よし、ちょっと寄ってくぞ。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_9DA1")

    def lambda_9D71():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9D71)
    Sleep(50)

    def lambda_9D81():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9D81)
    Sleep(50)

    def lambda_9D91():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9D91)
    Sleep(300)
    Jump("loc_9E18")

    label("loc_9DA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_9DDF")

    def lambda_9DAF():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9DAF)
    Sleep(50)

    def lambda_9DBF():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9DBF)
    Sleep(50)

    def lambda_9DCF():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9DCF)
    Sleep(300)
    Jump("loc_9E18")

    label("loc_9DDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_9E18")

    def lambda_9DED():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9DED)
    Sleep(50)

    def lambda_9DFD():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9DFD)
    Sleep(50)

    def lambda_9E0D():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9E0D)
    Sleep(300)

    label("loc_9E18")


    ChrTalk(
        0x101,
        (
            "#00003Fごめん、シン。\x01",
            "君の言う通りここは武器の店なんだ。\x02\x03",
            "#00001F中には危ない商品もあるから、\x01",
            "さすがに案内するわけには……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "フンッ、ベツに\x01",
            "商品に触らなければいいんだろ？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "ここには興味があるんだ。\x01",
            "ボクが寄ってくったら寄ってくぞ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00006F（ふぅ……\x01",
            "  エリィ、お願いするよ。）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00100F（ふふ、了解よ。）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00103Fねえシン君、あなたは\x01",
            "大事な大事な預かり物よ。\x02\x03",
            "だから私たちは、\x01",
            "たとえ万が一の可能性でも\x01",
            "危険を排除しないといけないの。\x02\x03",
            "#00100Fシン君なら賢いから\x01",
            "事情は分かってくれるわよね？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "う……\x01",
            "確かに理解はできますが。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109Fふふ、よかった。\x01",
            "やっぱりシン君はお利口さんね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "は、Yes…\x01",
            "ボク、お利口さんなんです!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_A0FE")

    ChrTalk(
        0x104,
        "#00309F（はは、お嬢の効果は絶大Right.）\x02",
    )

    CloseMessageWindow()
    Jump("loc_A17C")

    label("loc_A0FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_A144")

    ChrTalk(
        0x109,
        (
            "#10109F（あはは、\x01",
            "  エリィさん効果は絶大True.）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A17C")

    label("loc_A144")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_A17C")

    ChrTalk(
        0x105,
        "#10302F（ふふ、エリィの効果は絶大だね。）\x02",
    )

    CloseMessageWindow()

    label("loc_A17C")

    SetScenarioFlags(0x1DC, 7)
    Jump("loc_A1CC")

    label("loc_A184")


    ChrTalk(
        0x101,
        (
            "#00000F今はシンを連れているんだ。\x01",
            "武器商会に入るのは止めておこう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A1CC")

    TalkEnd(0xFF)
    Return()

    # Function_25_9CD7 end

    def Function_26_A1D0(): pass

    label("Function_26_A1D0")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x14, 0x0)
    OP_4B(0x15, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 150, 0, -3900, 0)
    SetChrPos(0x109, 1330, 0, -4640, 0)
    SetChrPos(0x102, 2590, 0, -3300, 315)
    SetChrPos(0x103, -1610, 0, -4590, 0)
    SetChrPos(0x105, -900, 0, -5970, 0)
    SetChrPos(0x104, 740, 0, -6130, 0)
    OP_68(-1190, 1900, -5280, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(11710, 0)
    SetChrFlags(0xF, 0x8)
    OP_0D()
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 7)), scpexpr(EXPR_END)), "loc_A518")

    ChrTalk(
        0x14,
        "よう、ロイドたち。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "特務支援課の皆さん、\x01",
            "ノエル曹長もThanks for your hard work\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100Fお疲れ様です!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "ところで、さっきの仕事は\x01",
            "もういいのか？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_A3CF")

    ChrTalk(
        0x101,
        (
            "#00002F#2Pああ、さっき解決したところでね。\x01",
            "フランツのおかげだよ、ありがとう。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "はは、なんだかよく分からないけど\x01",
            "お役に立てて光栄だよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A490")

    label("loc_A3CF")


    ChrTalk(
        0x101,
        (
            "#00003F#2Pあ、あAh...さっき終わった所だよ。\x02\x03",
            "#00006F（話を無視してしまったせいで\x01",
            "  詐欺師を取り逃してしまったけど……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "はは、なんだかよく分からないけど\x01",
            "ひと段落したならよかったな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A490")


    ChrTalk(
        0x101,
        (
            "#00005F#2Pそういえばフランツ、\x01",
            "今日はお前がここの警備に\x01",
            "入ってたんだな？\x02\x03",
            "いつもはケイト先輩が\x01",
            "警備にあたっている場所だけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A602")

    label("loc_A518")


    ChrTalk(
        0x14,
        "やあ、ロイドたちじゃないか。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "特務支援課の皆さん、\x01",
            "ノエル曹長もThanks for your hard work\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100Fお疲れ様です!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#2Pフランツ、今日はお前が\x01",
            "ここの警備に入ってるんだな？\x02\x03",
            "いつもはケイト先輩が\x01",
            "警備にあたっている場所だけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A602")


    ChrTalk(
        0x14,
        (
            "ああ、先輩が別件で\x01",
            "他の場所に行っているからな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "臨時でこの場所を\x01",
            "警備する事になったんだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-2320, 2800, -900, 2000)
    MoveCamera(45, 8, 0, 2000)
    OP_6E(660, 2000)
    SetCameraDistance(15930, 2000)
    Sleep(2500)

    ChrTalk(
        0x102,
        (
            "#12P#00108F『クロスベルの鐘』……\x01",
            "赤い星座が盗んでいって\x01",
            "しまったのよね。\x02\x03",
            "#00101Fここの警備が強化されているのも\x01",
            "その関係なんですよね？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "何せ、クロスベルの重要な\x01",
            "文化財が盗まれた訳ですからね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "念の為、自分が警備隊から\x01",
            "応援に来ているのです。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-1190, 1900, -5280, 2000)
    MoveCamera(45, 21, 0, 2000)
    OP_6E(660, 2000)
    SetCameraDistance(11710, 2000)
    Sleep(2500)

    ChrTalk(
        0x103,
        (
            "#00206F#3P盗んだ目的や、\x01",
            "持って行かれた場所も\x01",
            "分かってないんですよね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "ああ、一応警察や警備隊も\x01",
            "捜索はしてるんだけど、\x01",
            "見つかっていない状態なんだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#4P叔父貴たち……\x01",
            "一体何のためにこんな事を\x01",
            "しやがったんだか。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F#4Pフフ、持ち歩くには少々\x01",
            "かさばりそうな代物だけど。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#2P……とにかく、\x01",
            "『鐘』のことは任せて\x01",
            "俺たちは俺たちの仕事をしよう。\x02\x03",
            "#00000Fそれじゃあな、フランツ。\x01",
            "市内警備がんばってくれ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "ああ、またな。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_4C(0x14, 0x0)
    OP_4C(0x15, 0x0)
    ClearChrFlags(0xF, 0x8)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 150, 0, -3900, 0)
    SetScenarioFlags(0x190, 4)
    EventEnd(0x5)
    Return()

    # Function_26_A1D0 end

    SaveToFile()

Try(main)
