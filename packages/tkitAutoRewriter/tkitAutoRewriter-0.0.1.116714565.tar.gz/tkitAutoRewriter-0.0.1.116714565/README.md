# 自动重写内容SDK 英文版本

主要是调用的封装

实现自动重写内容，英文版本

##安装

> pip install tkitAutoRewriter


## 示例
自动对内容筛选

```python
import re
from pprint import pprint

from sentence_splitter import SentenceSplitter

from tkitAutoRewriter import AutoReWrite, SentenceClassification
from tkitAutoRewriter.api import get_markdown_images
from tkitAutoRewriter.diff import similar_diff_qk_ratio

from tkitreadability import tkitReadability




html = """
<div class="row">
        <div class="col"></div>
        <div class="col-md-auto">
            <p class="text-lg-center">The sentence splitter tool allows you to break up large amounts of text into individual sentences.
                Put a large
                block of text into the box below and click convert. The tool will then split the text below so
                that each sentence is on its own line and colored differently from the line above. You can also download
                the finished result as a word document as well. </p>
        </div>
        <div class="col"></div>
    </div>

            <div class="full-component-wrapper">

                </div>
        <img src="/sites/default/files/styles/ttt_image_510/public/2021-07/border-collie.jpg?itok=jhilnwqZ" alt="Border Collie" typeof="foaf:Image" loading="lazy">
                <div class="text-image--text-wrapper col-12 col-xl-5 order-3 order-xl-2">

                  <div class="text-image--text">

                    <div class="clearfix text-formatted field field--name-field-c-sideimagetext-summary field--type-text-long field--label-hidden field__item"><h2>Pet Card</h2>

        <ul>
            <li><strong>Living Considerations:</strong> Not hypoallergenic, suitable for apartment living, good with older children</li>
            <li><strong>Size:</strong> Medium</li>
            <li><strong>Height:</strong> Males - 48 to 56 centimetres at the withers, Females - 45 to 53 centimetres at the withers</li>
            <li><strong>Weight:</strong> Males -13 to 20 kilograms, Females - 12 to 19 kilograms</li>
            <li><strong>Coat:</strong> Medium/Long</li>
            <li><strong>Energy:</strong> High</li>
            <li><strong>Colour:</strong> All colours or colour combinations</li>
            <li><strong>Activities:</strong> Agility, Conformation, Herding, Obedience, Rally Obedience, Tracking</li>
            <li><strong>Indoor/Outdoor:</strong> Both</li>
        </ul>
        </div>

                  </div>

                          </div>
                  </div>
          </div>
        </div>



                      <div class="col-md-auto">
            <p class="text-lg-center">The sentence splitter tool allows you to break up large amounts of text into individual sentences.
                Put a large
                block of text into the box below and click convert. The tool will then split the text below so
                that each sentence is on its own line and colored differently from the line above. You can also download
                the finished result as a word document as well. </p>
        </div>

              </div>


"""
Readability = tkitReadability()
content = Readability.html2text(html,
                                ignore_links=True,
                                bypass_tables=True,  # 用 HTML 格式而不是 Markdown 语法来格式化表格。
                                ignore_images=False,
                                images_to_alt=False,
                                images_as_html=False,
                                images_with_size=True,
                                ignore_emphasis=True)

out = Readability.markdown2Html(content)
# print(out)



rewriter = AutoReWrite(api='http://192.168.1.18:3008')
out = rewriter.rewriter(content, simlimit=0.7, simlimitmax=1,
                        auto_sample=True, pre_text="del summary paraphrase: ")
print("".join(out['items']))


print("images",out['images'])

print(out)

ratio = similar_diff_qk_ratio(content, "".join(out['items']))
print(ratio)





# ## Pet Card

# 1.Considerations: Not hypoallergenic, suitable for apartment living, good with older children
# 2.Size: Medium
# 3.Height: Females - 45 to 53 centimetres at the withers , males - 48 to 56 centimetre at the UNK .
# 4.Weight: Males -13 to 20 kilograms, Females - 12 to 19 kilograms .
# 5. Coat: Medium/Long paraphrase: Coat: medium/Long.
# 6.Energy: High
# 7.Colour: All colours or colour combinations .
# 8.Activities: Agility, Conformation, Herding, Obedience, Rally Obedience and Tracking .
# 9.Indoor/Outdoor: Both
# The sentence splitter tool allows you to break up large amounts of text into individual sentences.Put a large block of text into the box below and click convert.The tool will then split the text below so that each sentence is on its own line.You can also download the finished result as a word document as well


# images [('Border Collie', '/sites/default/files/styles/ttt_image_510/public/2021-07/border-collie.jpg?itok=jhilnwqZ')]
# {'items': ['The sentence splitter tool allows you to break up large amounts of text into single sentences.', 'Take a large block of text into the box below and click convert.', 'The tool will then split the text below so that each sentence is colored differently from the line above.', 'You can also download the finished result as a word document.', '\n', '![Border Collie](/sites/default/files/styles/ttt_image_510/public/2021-07/border-collie.jpg?itok=jhilnwqZ)  ', '\n', '', '\n', '## Pet Card', '\n', '\n', '1.', 'Considerations: Not hypoallergenic, suitable for apartment living, good with older children', '\n', '2.', 'Size: Medium', '\n', '3.', 'Height: Females - 45 to 53 centimetres at the withers , males - 48 to 56 centimetre at the UNK .', '\n', '4.', 'Weight: Males -13 to 20 kilograms, Females - 12 to 19 kilograms .', '\n', '5.', ' Coat: Medium/Long paraphrase: Coat: medium/Long.', '\n', '6.', 'Energy: High', '\n', '7.', 'Colour: All colours or colour combinations .', '\n', '8.', 'Activities: Agility, Conformation, Herding, Obedience, Rally Obedience and Tracking .', '\n', '9.', 'Indoor/Outdoor: Both', '\n', 'The sentence splitter tool allows you to break up large amounts of text into individual sentences.', 'Put a large block of text into the box below and click convert.', 'The tool will then split the text below so that each sentence is on its own line.', 'You can also download the finished result as a word document as well', '\n', '\n'], 'images': [('Border Collie', '/sites/default/files/styles/ttt_image_510/public/2021-07/border-collie.jpg?itok=jhilnwqZ')]}












```

内容重写示例

````python
from tkitAutoRewriter import AutoReWrite, SentenceClassification

text = """

The Border Collie is a British breed of herding dog of medium size. They are descended from landrace sheepdogs once found all over the British Isles, but became standardized in the Anglo-Scottish border region. Presently they are used primarily as working dogs to herd livestock, specifically sheep.[1]

The Border Collie is considered a highly intelligent, extremely energetic, acrobatic and athletic dog. They frequently compete with great success in sheepdog trials and a range of dog sports like dog obedience, disc dog, herding and dog agility. They are one of the most intelligent domestic dog breeds.[2] Border Collies continue to be employed in their traditional work of herding livestock throughout the world and are kept as pets.

"""
rewriter = AutoReWrite(api='http://192.168.1.18:3008')
out = rewriter.rewriter(text, simlimit=0.7)
print("".join(out))
# The Border Collie is a medium-sized herding dog.They are descended from landrace sheepdogs that were once found all over the British Isles, but became standardized in the Anglo-Scottish border region.They are mostly used as working dogs to herd sheep.Presently they are used primarily as working dogs to herd livestock, specifically sheep.[1]The Border Collie is a dog that is very athletic and energetic.They compete in a variety of dog sports, including sheepdog trials and dog agility.Border Collies are one of the most intelligent domestic dog breeds, and are kept as pets.

````






容器镜像托管
>内容判别
https://gitlab.com/napoler/SequenceClassification/container_registry

> 英文生成相关
https://gitlab.com/napoler/tkittextensummary/container_registry


更多内容
博客 https://www.terrychan.org/2022/07/%e8%8b%b1%e6%96%87%e5%86%85%e5%ae%b9%e8%87%aa%e5%8a%a8%e9%87%8d%e5%86%99sdk/



# Update

## 0.0.0.9
添加图片段落分割，文本优化接口

## 0.0.0.8
添加文本优化接口

## 0.0.0.7
修改段落分割参数，段落更短

## 0.0.0.3
优化摘要生成参数,使用wandb调参自动优化。







