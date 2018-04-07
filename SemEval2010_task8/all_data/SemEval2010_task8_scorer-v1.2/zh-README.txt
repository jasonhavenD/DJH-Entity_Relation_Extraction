包括两个SemEval-2010任务＃8的工具：
多对名词之间语义关系的多路分类

该任务在以下Web地址中描述：
	http://docs.google.com/View?id=dfvxd49s_36c28v9pmw


1.输出文件格式检查器
-----------------------------

这是SemEval-2010任务8的官方输出文件格式检查器。

使用：
   semeval2010_task8_format_checker.pl <PROPOSED_ANSWERS>

例子：
   semeval2010_task8_format_checker.pl proposed_answer1.txt
   semeval2010_task8_format_checker.pl proposed_answer2.txt
   semeval2010_task8_format_checker.pl proposed_answer3.txt
   semeval2010_task8_format_checker.pl proposed_answer4.txt
   semeval2010_task8_format_checker.pl proposed_answer5.txt

  在上面的例子中，前三个文件是正确的，而最后一个包含四个错误。
  answer_key2.txt包含* training *数据集的真实标签。

描述：
   记分员将建议的分类文件作为输入，
   它应该在格式中包含每行预测
   “<SENT_ID> <RELATION>”
   以TAB作为分隔符，例如，
         1组件 - 整体（e2，e1）
         2其他
         3仪器 - 机构（e2，e1）
             ...
   该文件不必以任何方式排序。
   重复的ID是不允许的。

   在出现问题时，检查员输出问题行和其编号。
   最后，报告发现的问题总数
   或者输出一条消息，说明文件格式正常。

   预计参赛者在提交前使用此检查器检查他们的输出。

最后修改日期：2010年3月10日



2.得分手
---------

这是SemEval-2010任务＃8的官方得分手。

最后修改日期：2010年3月22日

当前版本：1.2

修订记录：
  - 版本1.2（修正了（iii）得分的精确度错误）
  - 版本1.1（修正了计算精度的错误）

使用：
   semeval2010_task8_scorer-v1.1.pl <PROPOSED_ANSWERS> <ANSWER_KEY>

例子：
   semeval2010_task8_scorer-v1.2.pl proposed_answer1.txt answer_key1.txt> result_scores1.txt
   semeval2010_task8_scorer-v1.2.pl proposed_answer2.txt answer_key2.txt> result_scores2.txt
   semeval2010_task8_scorer-v1.2.pl proposed_answer3.txt answer_key3.txt> result_scores3.txt
   semeval2010_task8_scorer-v1.2.pl proposed_answer5.txt answer_key5.txt> result_scores5.txt

描述：
   记分员将建议的分类文件和答案密钥文件作为输入。
   两个文件都应该以“<SENT_ID> <RELATION>”格式包含每行预测
   以TAB作为分隔符，例如，
         1组件 - 整体（e2，e1）
         2其他
         3仪器 - 机构（e2，e1）
             ...
   这些文件不必以任何方式排序，并且第一个文件可以有预测
   仅用于第二个文件中的ID子集，例如，因为硬示例已被跳过。
   在任何一个文件中都不允许重复ID。

   记分员计算并输出以下统计数据：
      （1）混淆矩阵，如图所示
         - 每行/列的总和：-SUM-
         - 跳过的例子数量：跳过
         - 具有正确关系但方向错误的示例数目：xDIRx
         - 答案密钥文件中的示例数量：ACTUAL（= -SUM- + skip + xDIRx）
      （2）准确性和覆盖面
      （3）每个关系的精确度（P），召回率（R）和F1分数
      （4）微观平均P，R，F1，其中计算忽略其他类别。
      （5）宏观平均P，R，F1，其中计算忽略其他类别。

   请注意，在分数（4）和（5）中，跳过的示例等同于分类为“其他”的示例。
   因此，关键文件中不存在关系的例子（这可能不是最优的）。

   评分完成三次：
     （i）作为（2 * 9 + 1）分类
     （ii）作为（9 + 1）分类，忽略方向性
     （iii）作为（9 + 1）分类，并考虑方向性。
   
   （iii）的官方分数是宏观平均F1分数。