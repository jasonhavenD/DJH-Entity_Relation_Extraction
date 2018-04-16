关系抽取:辨别实体间存在的关系.

文本示例:
Citing high fuel prices, [ORG United Airlines] said [TIME Friday] it has increased fares by [MONEY $6] per round trip on flights to some cities also
served by lower-cost carriers. [ORG American Airlines], a unit of [ORG AMR Corp.], immediately matched the move, spokesman [PER Tim Wagner] said.
[ORG United], a unit of [ORG UAL Corp.], said the increase took effect [TIME Thursday] and applies to most routes where it competes against discount carriers,
such as [LOC Chicago] to [LOC Dallas] and [LOC Denver] to [LOC San Francisco].

文本示例叙述了以下事实:
Time Wagner是美国航空发言人;
United是UAL公司的一部分;
美国航空是AMR的一部分;

以上二元关系是一般关系的示例,如part-of,part-of关系在文本中用的相当频繁.

下图为列举出ACE关系抽取中17种关系类型:

![](./pic/ACE关系示例.png)

下图为关系示例:<br>

![](./pic/语义关系示例和涉及命名实体类型.png)

也有一些领域关系,如航空路线的概念.
从文本中可总结出,United有到Chicago, Dallas, Denver和San Francisco等等的航线.


关系由领域顺序元组组成,领域元素相当于文中的命名实体.实体来与共指消解的结果,或者来源于领域本体中的实体.
下图为基于模型的实体和关系示例.

![](./pic/基于模型的关系和实体.png)

许多其它领域也定义了很多关系,比如UMLS(Unified Medical Language System),定义了134中广泛的主题分类(subject categories),
实体类型(entity types),54种实体之间的关系,如下图所示:<br>
![](./pic/实体关系.png)

给出医药句子如下:
Doppler echocardiography can be used to diagnose left anterior descending artery stenosis in patients with type 2 diabetes
可抽取UMLS关系:Echocardiography, Doppler Diagnoses Acquired stenosis

infoboxs:<br>
维基百科的infobox提供了大量关系,一些维基文章和机构化表关联.
维基包含结构化事实,比如 state = "California";
president = "John L. Hennessy".
这些事实可转化为关系,比如president-of或者located-in.
或者转化为RDF中的关系,RDF(Resource Description Framework).
一个RDF元组由实体-关系-实体(entity-relation-entity)组成.
也叫做主谓宾(subject-predicate-object).

RDF元组示例:<br>
      subject           predicate            object   <br>
Golden Gate Park        location            San Francisco   <br>

DBpedia源于维基,包含20亿RDF元组.还有源于维基infobox的数据集.<br>
Freebase的关系如下:<br>

people/person/nationality <br>
location/location/contains <br>
people/person/place-of-birth <br>
biology/organism classification <br>

WordNet或者其它本体提供本体关系,这些关系表示词和概念间的层次关系.WordNet包含is-a或者上位词关系.<br>
Giraffe is-a ruminant is-a ungulate is-a mammal is-a vertebrate is-a an- imal. . .

WordNet个体和类之间也有Instance-of的关系,比如San Francisco和city的关系是Instance-of.抽取这些官谢是在新语言和领域中扩展本体和构建本体的重要步骤
.
关系抽取有4种主要的算法:<br>
hand-written patterns  <br>
supervised machine learning <br>
semi-supervised <br>
unsupervised  <br>




一.模板抽取关系<br>
早期关系抽取使用的的模板,由Hearst在1992你那提出.<br>
假设有如下句子:<br>
Agar is a substance prepared from a mixture of red algae, such as Gelidium, for laboratory or industrial use.

Hearst指出大部分人不知道Gelidium是什么,但能推理出它是红藻(red algae).她提出西面的模式(lexico-syntactic pattern):

NP0 such as NP1{,NP2 ...,(and|or)NPi},i ≥ 1  <br>

寓意着以下语义: <br>
∀NPi,i ≥ 1,hyponym(NPi,NP0) <br>

可推理出:
hyponym(Gelidium,red algae)  <br>

![](./pic/句法模板发现上位词.png)

上图为hearst提出的5个模板,用于推理上位关系;NPH表示父节点(上位词).

现代版本基于模板方法基于以上添加了命名实体识别的限制.
比如我们的目标是,回复"who holds what office in which organizaiton"这种问句,我们可以用以下模板:<br>

![](./pic/模板.png)

模板的优点是准确率比较高,能够为特殊领域量身定制模板.缺点是查全率低,需要大量人工,考虑所有可能的模板.

二.监督学习关系抽取.<br>
基于监督学习方法的关系抽取目前已为大家熟悉的体系.固定的关系和实体.
手工标注关系和实体,标注文本用于训练分类器,然后标注未知测试集.

最直接的方法有3步,如下图所示:<br>
![](./pic/实体中发现和分类关系.png)

1.发现命名实体对(通常在相同的一句话中)<br>
2.为了提高efficiency，通常我们会训练两个分类器，第一个分类器是 yes/no的二分类,决策命名实体对是否相关,如果有关系，再送到第二个分类器，给实体分配关系类别。
正例直接在标注语料中抽取所有关系;负例为未标注关系的实体对.<br>
3.分类器给关系打标签,用过滤分类器能加速最后的分类,根据不同的任务使用不同的特征集,对于这两个分类器,可以使用标准的分类技术(逻辑回归,SVM,贝叶斯,随机森林,神经网络等)   <br>

三.基于Bootstrapping的半监督关系抽取
有监督机器学习的前提是有大量预标注语料来训练分类器,不幸的是,这种标注语料很难得到.
假设我们有一些高精度的种子模板(high-precision seed patterns),如模板抽取部分例句或者一些种子元组(seed tuples).
便足以利用bootstrap进行分类.把实体处理成种子对(seed pair),然后提取包含实体对的句子(web或者任意的数据集).
从所有的句子中,抽取和泛化上下文实体以学习新的模板.
下图为基本算法:<br>
![](./pic/基于bootsrapping的种子实体对学习关系.png)

举个例子,创建种子对airline/hub,我们知道Ryanair(瑞安航空)在Chrleroi(沙勒罗瓦)有一个hub(枢纽).就可以用这个种子事实去发现新的模板.
发现语料中提及的其它关系.搜索术语Ryanair,Charleroi和hub.可能发现以下句子集合:<br>
(21.6) Budget airline Ryanair, which uses Charleroi as a hub, scrapped all weekend flights out of the airport.   <br>
(21.7) All flights in and out of Ryanair’s Belgian hub at Charleroi airport were grounded on Friday...   <br>
(21.8) A spokesman at Charleroi, a main hub for Ryanair, estimated that 8000 passengers had already been affected.  <br>

从以上结果,可以使用实体上下文间提及的实体,实体掐你个词,后两个词,两个词的命名实体类型,或者其它特征,抽取通用的模板: <br>
/ [ORG], which uses [LOC] as a hub /<br>
   / [ORG]’s hub at [LOC] /<br>
   / [LOC] a main hub for [ORG] /<br>

这些新的模板可用于搜索新的元组.
Bootstrapping可以给新的元组分配置信度(confidence values)以避免语义转移(semantic drift).
语义转移问题中,错误的模板会导致错误的元组,导致抽取关系的意思转移.例如:<br>
(21.9) Sydney has a ferry hub at Circular Quay.   <br>
如果以上例子作为一个正例,那么会导致元组⟨Sydney,CircularQuay⟩错误.基于此模板的元组讲会导致更多的错误.

模板置信度基于两个因子:<br>
(1)模板性能遵循目前的元组<br>
(2)模板的生产率,也就是匹配到的数量.<br>


给出文档集合D,元组集合T,模板p,那么需要跟踪两个因素:

(1)hit:在文档D中,模板p匹配的元组集合T.(the set of tuples in T that p matches while looking in D)<br>
(2)finds:模板p在文档D中匹配的所有元组.(finds:The total set of tuples that p finds in D) <br>

公式如下(Riloff and Jones,1999)<br>

![](./pic/公式1.png)

以上公式会形式化的产生一个概率.

提出的新元组可以做置信度估计,通过在文档集D中匹配的所有的模板P′ (Agichtein and Gravano, 2000).
结合这个置信度的一个方法是the noisy-or technique.
假设模板P支持给出的元组,每个都进行了置信度估计.在noisy-or模型中,有两个假设.
第一个,如果提出的元组是错误的,那么所有支持的模板都是错误的.
第二个,个别错误是独立的.
如果宽松的处理置信度,那么个别模板P错误的置信度为1 − Conf ( p);
新元组置信度公式如下:<br>

![](./pic/公式2.png)

设置保守的置信度去接受新模板将会帮助系统防止转移目标关系.
(settring conservative confidence thresholds for th acceptance of new patterns and tuples during the bootstrapping process helps prevent the
system from drifting away from the targeted relation)