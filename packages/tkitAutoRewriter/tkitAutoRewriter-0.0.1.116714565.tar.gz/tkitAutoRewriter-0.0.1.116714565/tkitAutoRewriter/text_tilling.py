import nltk
import os
# print(os.getcwd())
# nltk.data.path.append("./nltk_data")
nltk.data.path.append(os.path.join(os.getcwd(),"nltk_data"))
def text_tilling(text,text_length=1000,paragraph_limit=5,text_limit=168):
    """
    The text_tilling function takes a text and splits it into smaller texts.
    The function takes two arguments:
        1) text - the input text to be split,
        2) paragraph_limit - the maximum number of paragraphs in each output chunk. Default is 5.

    :param text: Used to Pass the text to be tiled.
    :param text_length=1000: Used to Determine the length of each tile.
    :param paragraph_limit=5: Used to Limit the number of paragraphs to be returned.
    :return: A list of paragraphs from a text.

    """
    # ttt = nltk.tokenize.TextTilingTokenizer()
    ttt = nltk.tokenize.TextTilingTokenizer(w=15, k=10, similarity_method=0, stopwords=None, smoothing_method=[0], smoothing_width=2, smoothing_rounds=1, cutoff_policy=1, demo_mode=False)
    tiles = ttt.tokenize(text)
    out=[]
    for i,it in enumerate(tiles):
        out.append(it)
        text="\n".join(out)
        # 防止段落过短
        if len(text.split(" "))>text_limit:
            out=[]
            yield text
            continue

        if i+1==len(tiles):
            yield text

def auto_text_tilling(text,text_length=1000,paragraph_limit=5):
    """
    自动拆分文本，对文本进行自动分段
    """

    if len(text.split("\n"))>paragraph_limit or len(text.split(" "))>text_length:
        try:
            ttt = nltk.tokenize.TextTilingTokenizer()

            tiles = ttt.tokenize(text)
            # print("==================\n\n".join(tiles))
            items=[]
            for it in tiles:
                # print("================\n\n")
                # print(it.replace("\n"," "))
                items.append(it.replace("\n"," ").replace("<n>"," ").strip())

            text="\n".join(items)
        except:
            pass
    else:
        text=text.replace("<n>"," ").strip()
        pass
    return text

